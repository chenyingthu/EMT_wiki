#!/home/chenying/anaconda3/bin/python3
"""
Deep enrichment of wiki source pages with detailed technical content.

Uses pdftotext + enhanced markdown as input, LLM extracts:
- Mathematical formulas (LaTeX)
- Algorithm steps and parameters
- Simulation results with evidence-backed numerical data when reported
- Model details and assumptions
- Applicability boundaries and failure modes

Writes new sections to wiki/sources/*.md files.
"""

import os
import re
import json
import subprocess
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

from llm_client import make_llm_client

WIKI_SOURCES = Path("wiki/sources")
ENHANCED_DIR = Path("extracted_text/markdown_enhanced")
MARKDOWN_DIR = Path("extracted_text/markdown")
PDFTOTEXT_DIR = Path("extracted_text/pdftotext")
CHECKPOINT = Path(".deep_enrich.json")
DEFAULT_STRICT_REPORT = Path("reports/wiki_strict_audit.json")
DEEP_SECTION_MARKER_START = "<!-- deep-enrich:start -->"
DEEP_SECTION_MARKER_END = "<!-- deep-enrich:end -->"
REQUIRED_DEEP_SECTIONS = ("方法细节", "仿真结果", "量化发现", "关键公式", "验证详情", "适用边界")


def extract_full_text(pdf_path: str, timeout_sec: int = 30) -> str:
    """Extract full text from PDF using pdftotext (no length limit)."""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=timeout_sec
        )
        return result.stdout if is_usable_extracted_text(result.stdout) else ""
    except Exception:
        return ""


def get_pdf_path(filepath: Path) -> str:
    """Extract PDF path from source file."""
    content = filepath.read_text(encoding='utf-8')
    match = re.search(r'sources:\s*\["([^"]*EMT_Doc[^"]*)"\]', content)
    if match:
        pdf_rel_path = match.group(1)
        pdf_path = f"/home/chenying/researches/EMT_LLM_Wiki/{pdf_rel_path}"
        if os.path.exists(pdf_path):
            return pdf_path
    return None


def load_checkpoint() -> dict:
    if CHECKPOINT.exists():
        with open(CHECKPOINT, 'r') as f:
            data = json.load(f)
        data.setdefault('done', [])
        data.setdefault('failed', [])
        return data
    return {"done": [], "failed": []}


def save_checkpoint(checkpoint: dict) -> None:
    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)


def update_failed(checkpoint: dict, filename: str) -> None:
    if filename not in checkpoint.get('failed', []):
        checkpoint.setdefault('failed', []).append(filename)


def update_done(checkpoint: dict, filename: str) -> None:
    if filename not in checkpoint.get('done', []):
        checkpoint.setdefault('done', []).append(filename)
    checkpoint['failed'] = [name for name in checkpoint.get('failed', []) if name != filename]


def strict_priority(strict_report: Path = DEFAULT_STRICT_REPORT) -> dict[str, tuple[int, int]]:
    """Return source filename priority from strict audit findings."""
    if not strict_report.exists():
        return {}
    try:
        findings = json.loads(strict_report.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    priority: dict[str, tuple[int, int]] = {}
    for index, item in enumerate(findings):
        if item.get("page_type") != "source":
            continue
        path = Path(item.get("path", ""))
        if path.name:
            priority[path.name] = (-int(item.get("score", 0)), index)
    return priority


def sort_source_files_by_priority(source_files: list[Path], strict_report: Path = DEFAULT_STRICT_REPORT) -> list[Path]:
    priorities = strict_priority(strict_report)
    return sorted(source_files, key=lambda path: priorities.get(path.name, (0, 10**9)) + (path.name,))


def get_enhanced_text(filename: str) -> str:
    """Get LLM-enhanced markdown if available."""
    candidate_names = [filename]
    stem = filename[:-3] if filename.endswith('.md') else filename
    base_stem = re.sub(r'-(?:\d+|fix)$', '', stem)
    if base_stem != stem:
        candidate_names.append(f"{base_stem}.md")

    for candidate in candidate_names:
        md_path = ENHANCED_DIR / candidate
        if md_path.exists():
            text = md_path.read_text(encoding='utf-8')
            if is_usable_extracted_text(text):
                return text
    for candidate in candidate_names:
        plain_md_path = MARKDOWN_DIR / candidate
        if plain_md_path.exists():
            text = plain_md_path.read_text(encoding='utf-8')
            if is_usable_extracted_text(text):
                return text
    # Fallback to pdftotext
    for candidate in candidate_names:
        txt_path = PDFTOTEXT_DIR / candidate.replace('.md', '.txt')
        if txt_path.exists():
            text = txt_path.read_text(encoding='utf-8')
            if is_usable_extracted_text(text):
                return text
    return ""


def is_usable_extracted_text(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) < 500:
        return False
    if stripped.lower().startswith("please provide the academic paper text"):
        return False
    return True


def is_inactive_source_page(content: str) -> bool:
    """Return true for provenance-only pages that should not be LLM-expanded."""
    return "type: duplicate-source" in content or "type: out-of-scope-source" in content


def build_prompt(full_text: str, enhanced_md: str, current_content: str) -> str:
    """Build detailed extraction prompt."""
    # Combine sources: enhanced markdown (has LaTeX) + full text (has results)
    if full_text.strip():
        combined = enhanced_md[:30000] + "\n\n--- FULL TEXT ---\n\n" + full_text[:20000]
    else:
        combined = enhanced_md[:35000]

    prompt = f"""你是电磁暂态(EMT)仿真领域的专家。请详细分析以下论文，提取所有技术细节。

当前source page已有摘要信息：
{current_content[:2000]}

请结合以下论文全文，提取更深层次的技术内容：
{combined[:50000]}

用中文输出JSON，包含以下字段：
{{
  "methodology": {{
    "approach": "整体方法的详细描述（200-400字）",
    "equations": [
      {{"latex": "数学公式LaTeX代码", "description": "公式含义和用途"}}
    ],
    "algorithm_steps": ["算法步骤1（详细描述）", "步骤2", ...],
    "parameters": {{"关键参数名": "值或说明"}}
  }},
  "simulation_results": [
    {{"test_case": "测试场景名称", "description": "结果描述；只包含原文明确报告的具体数值", "comparison": "与基线的对比；若原文未报告则写'原文未报告'"}}
  ],
  "quantitative_findings": [
    "原文明确报告的数值型发现1；若没有数值证据，写'原文未报告可核验的数值结果'",
    "发现2；不得根据摘要或常识补造数字",
    ...
  ],
  "key_equations": [
    {{"latex": "最重要的公式LaTeX", "name": "公式名称", "context": "在什么情况下使用"}}
  ],
  "validation_details": {{
    "method": "验证方式（仿真/实验/现场数据/对比分析）",
    "test_system": "测试系统描述（如'IEEE 39节点系统'）",
    "tools": "使用的仿真工具（如PSCAD/EMTDC、MATLAB、RTDS等）",
    "results_summary": "验证结果总结"
  }},
  "applicability_boundaries": {{
    "valid_when": ["适用条件1，例如模型假设、频率范围、系统类型或接口条件"],
    "invalid_when": ["失效条件1，例如强非线性、未建模控制、极端拓扑变化或文本未覆盖的场景"],
    "assumptions": ["论文显式假设或从方法中可直接推出的前提；推断必须标注'据方法推断'"],
    "evidence_gaps": ["原文未给出或抽取文本无法确认的关键信息"]
  }}
}}

要求：
1. 所有公式必须保留LaTeX格式（$...$或$$...$$）
2. 仿真结果和量化发现只能写原文明确报告的数值；如果原文没有数值，必须写“原文未报告可核验的数值结果”，不得编造
3. 算法步骤要详细，不能简化为几个词
4. 区分“原文证据”和“据方法推断”：推断内容必须显式标注，不得伪装成论文结论
5. 只输出JSON，不要其他文字
"""
    return prompt


def extract_json_from_response(text: str) -> dict:
    """Extract JSON from LLM response."""
    # Try direct parse
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass
    # Try to find JSON block
    match = re.search(r'\{[\s\S]*\}', text)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    # Try fixing common issues
    text = text.strip()
    if text.startswith('```json'):
        text = text[7:]
    if text.startswith('```'):
        text = text[3:]
    if text.endswith('```'):
        text = text[:-3]
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def format_section(title: str, content: str) -> str:
    """Format a section for the markdown file."""
    return f"\n## {title}\n\n{content}\n"


def fix_latex_delimiters(text: str) -> str:
    """Fix $$$...$$$ to $$...$$ for proper display math."""
    text = re.sub(r'\$\$\$', '$$', text)
    return text


def render_deep_data(data: dict) -> str:
    """Render extracted data into markdown sections."""
    sections = []

    # Methodology
    meth = data.get('methodology', {})
    if meth:
        parts = []
        if meth.get('approach'):
            parts.append(f"### 方法概述\n\n{meth['approach']}\n")
        eqs = meth.get('equations', [])
        if eqs:
            parts.append("### 数学公式\n")
            for i, eq in enumerate(eqs, 1):
                latex = fix_latex_delimiters(eq.get('latex', ''))
                desc = eq.get('description', '')
                if latex:
                    parts.append(f"\n**公式{i}**: $${latex}$$\n\n*{desc}*\n")
        steps = meth.get('algorithm_steps', [])
        if steps:
            parts.append("\n### 算法步骤\n")
            for i, step in enumerate(steps, 1):
                # Clean up numbering artifacts like "1. 1."
                step = re.sub(r'^\d+\.\s*\d+\.\s*', '', step.strip())
                parts.append(f"{i}. {step}\n")
        params = meth.get('parameters', {})
        if params:
            parts.append("\n### 关键参数\n")
            for k, v in params.items():
                parts.append(f"- **{k}**: {v}\n")
        if parts:
            sections.append(("方法细节", "\n".join(parts)))

    # Simulation Results
    results = data.get('simulation_results', [])
    if results:
        parts = ["### 仿真测试\n"]
        parts.append("| 测试场景 | 结果描述 | 对比基线 |\n")
        parts.append("|---------|---------|----------|\n")
        for r in results:
            tc = r.get('test_case', '')
            desc = r.get('description', '')
            comp = r.get('comparison', '')
            parts.append(f"| {tc} | {desc} | {comp} |\n")
        sections.append(("仿真结果", "\n".join(parts)))

    # Quantitative Findings
    findings = data.get('quantitative_findings', [])
    if findings:
        parts = []
        for f in findings:
            parts.append(f"- {f}")
        sections.append(("量化发现", "\n".join(parts)))

    # Key Equations
    keqs = data.get('key_equations', [])
    if keqs:
        parts = []
        for eq in keqs:
            latex = fix_latex_delimiters(eq.get('latex', ''))
            name = eq.get('name', '')
            ctx = eq.get('context', '')
            if latex:
                parts.append(f"### {name}\n\n$${latex}$$\n\n*{ctx}*\n")
        if parts:
            sections.append(("关键公式", "\n".join(parts)))

    # Validation Details
    vd = data.get('validation_details', {})
    if vd and any(vd.values()):
        parts = []
        if vd.get('method'):
            parts.append(f"- **验证方式**: {vd['method']}")
        if vd.get('test_system'):
            parts.append(f"- **测试系统**: {vd['test_system']}")
        if vd.get('tools'):
            parts.append(f"- **仿真工具**: {vd['tools']}")
        if vd.get('results_summary'):
            parts.append(f"- **验证结果**: {vd['results_summary']}")
        if parts:
            sections.append(("验证详情", "\n".join(parts)))

    # Applicability boundaries and evidence gaps
    boundaries = data.get('applicability_boundaries', {})
    if boundaries and any(boundaries.values()):
        labels = (
            ("valid_when", "适用条件"),
            ("invalid_when", "失效边界"),
            ("assumptions", "关键假设"),
            ("evidence_gaps", "证据缺口"),
        )
        parts = []
        for key, label in labels:
            values = boundaries.get(key, [])
            if isinstance(values, str):
                values = [values]
            cleaned = [str(value).strip() for value in values if str(value).strip()]
            if cleaned:
                parts.append(f"### {label}\n")
                parts.extend(f"- {value}\n" for value in cleaned)
        if parts:
            sections.append(("适用边界", "\n".join(parts)))

    return "\n".join(format_section(title, content) for title, content in sections)


def strip_deep_enrichment(content: str) -> str:
    """Remove generated enrichment before writing a fresh block."""
    marker_pattern = rf'\n?{re.escape(DEEP_SECTION_MARKER_START)}[\s\S]*?{re.escape(DEEP_SECTION_MARKER_END)}\n?'
    content = re.sub(marker_pattern, '\n', content).rstrip() + '\n'
    section_names = "|".join(re.escape(name) for name in REQUIRED_DEEP_SECTIONS)
    legacy_pattern = rf'\n## ({section_names})\n[\s\S]*?(?=\n## (?!({section_names})\b)|\Z)'
    return re.sub(legacy_pattern, '', content).rstrip() + '\n'


def has_complete_deep_enrichment(content: str) -> bool:
    if not all(f"## {name}" in content for name in REQUIRED_DEEP_SECTIONS):
        return False
    findings = re.search(r'## 量化发现\s*\n(.*?)(?=\n##|$)', content, re.DOTALL)
    if findings and not re.search(r'\d|原文未报告|未给出|无法确认', findings.group(1)):
        return False
    return True


def render_marked_deep_data(data: dict) -> str:
    rendered = render_deep_data(data)
    if not rendered.strip():
        return ""
    return f"\n{DEEP_SECTION_MARKER_START}\n{rendered.strip()}\n{DEEP_SECTION_MARKER_END}\n"


def process_single_file(filename: str, src_file: Path, llm_client: Any, dry_run: bool = False, force: bool = False) -> tuple:
    """Process one file. Returns (filename, success, message)."""
    # Get PDF text
    pdf_path = get_pdf_path(src_file)
    full_text = ""
    if pdf_path:
        full_text = extract_full_text(pdf_path)

    # Get enhanced markdown
    enhanced_md = get_enhanced_text(filename)

    # Get current content
    current_content = src_file.read_text(encoding='utf-8')

    if is_inactive_source_page(current_content):
        return (filename, True, "skipped inactive source")

    if has_complete_deep_enrichment(current_content) and not force:
        return (filename, True, "already enriched")

    # Build prompt
    input_text = full_text if is_usable_extracted_text(full_text) else enhanced_md
    if not input_text.strip():
        return (filename, False, "no text available")

    prompt = build_prompt(input_text, enhanced_md, current_content)

    # Call LLM with retry and timeout
    try:
        llm_text = llm_client.complete(prompt, max_tokens=8000, temperature=0.1, timeout=180.0)
        if not llm_text:
            return (filename, False, "empty LLM response")

        data = extract_json_from_response(llm_text)
        if not data:
            return (filename, False, "failed to parse JSON")

        # Render and append
        rendered = render_marked_deep_data(data)
        if not rendered.strip():
            return (filename, False, "no data extracted")

        new_content = strip_deep_enrichment(current_content) + rendered
        if dry_run:
            return (filename, True, f"dry-run enriched ({len(rendered)} chars)")

        src_file.write_text(new_content, encoding='utf-8')

        return (filename, True, f"enriched ({len(rendered)} chars)")

    except Exception as e:
        return (filename, False, str(e)[:100])


def main(dry_run: bool = False, limit: int = 0, concurrency: int = 8, provider: str = None, model: str = None, force: bool = False, retry_failed: bool = False, strict_report: Path = DEFAULT_STRICT_REPORT):
    print("=" * 60)
    print("Deep enrichment of source pages")
    print("=" * 60)

    checkpoint = load_checkpoint()
    print(f"Checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")
    done_set = set(checkpoint.get('done', []))

    if retry_failed:
        source_files = sorted([WIKI_SOURCES / name for name in checkpoint.get('failed', []) if (WIKI_SOURCES / name).exists()])
    else:
        source_files = []
        for f in sorted(WIKI_SOURCES.glob("*.md")):
            content = f.read_text(encoding="utf-8")
            if is_inactive_source_page(content):
                continue
            if not force and f.name in done_set and has_complete_deep_enrichment(content):
                continue
            source_files.append(f)
        source_files = sort_source_files_by_priority(source_files, strict_report)
    total = len(source_files) + len(done_set)
    print(f"Total: {total}, Remaining: {len(source_files)}")

    if limit > 0:
        source_files = source_files[:limit]
        print(f"Limited to {len(source_files)} files (dry run)")

    if not source_files:
        print("No files to process!")
        return

    llm_client = make_llm_client(provider=provider, model=model)
    start_time = time.time()
    count = len(checkpoint['done'])
    completed = 0

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {}
        for src_file in source_files:
            future = executor.submit(process_single_file, src_file.name, src_file, llm_client, dry_run, force)
            futures[future] = src_file.name

        for future in as_completed(futures):
            filename, success, msg = future.result()
            count += 1
            completed += 1

            if success:
                if not dry_run:
                    update_done(checkpoint, filename)
                print(f"  [{count}/{total}] {filename[:50]}... OK: {msg}")
            else:
                if not dry_run:
                    update_failed(checkpoint, filename)
                print(f"  [{count}/{total}] {filename[:50]}... FAIL: {msg}")

            if completed % 10 == 0 and not dry_run:
                save_checkpoint(checkpoint)
                elapsed = (time.time() - start_time) / 60
                print(f"  >> Checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed ({elapsed:.1f}m)")

    if not dry_run:
        save_checkpoint(checkpoint)

    elapsed = (time.time() - start_time) / 60
    print(f"\n{'=' * 60}")
    print(f"Completed in {elapsed:.1f} minutes")
    print(f"Done: {len(checkpoint['done'])}")
    print(f"Failed: {len(checkpoint['failed'])}")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    parser.add_argument('--limit', type=int, default=0, help='Limit to N files')
    parser.add_argument('--concurrency', type=int, default=8, help='Parallel workers')
    parser.add_argument('--llm-provider', choices=['codex', 'openai', 'anthropic'], default=os.environ.get('WIKI_LLM_PROVIDER', 'codex'))
    parser.add_argument('--model', default=None, help='Override provider model')
    parser.add_argument('--force', action='store_true', help='Regenerate even if sections already exist')
    parser.add_argument('--retry-failed', action='store_true', help='Process only files listed in checkpoint failed list')
    parser.add_argument('--strict-report', type=Path, default=DEFAULT_STRICT_REPORT, help='Strict audit JSON used to prioritize risky source pages')
    args = parser.parse_args()
    main(dry_run=args.dry_run, limit=args.limit, concurrency=args.concurrency, provider=args.llm_provider, model=args.model, force=args.force, retry_failed=args.retry_failed, strict_report=args.strict_report)
