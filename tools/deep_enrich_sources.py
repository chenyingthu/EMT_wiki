#!/home/chenying/anaconda3/bin/python3
"""
Deep enrichment of wiki source pages with detailed technical content.

Uses pdftotext + enhanced markdown as input, LLM extracts:
- Mathematical formulas (LaTeX)
- Algorithm steps and parameters
- Simulation results with numerical data
- Model details and assumptions

Writes new sections to wiki/sources/*.md files.
"""

import os
import re
import json
import subprocess
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

import anthropic

WIKI_SOURCES = Path("wiki/sources")
ENHANCED_DIR = Path("extracted_text/markdown_enhanced")
PDFTOTEXT_DIR = Path("extracted_text/pdftotext")
CHECKPOINT = Path(".deep_enrich.json")

# Initialize client with environment-based configuration
client = anthropic.Anthropic(
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://qianfan.baidubce.com/anthropic/coding")
)

# Model selection priority: env > default
LLM_MODEL = os.environ.get("ANTHROPIC_MODEL", "kimi-k2.5")

# Load checkpoint
checkpoint = {"done": [], "failed": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))


def extract_full_text(pdf_path: str, timeout_sec: int = 30) -> str:
    """Extract full text from PDF using pdftotext (no length limit)."""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=timeout_sec
        )
        return result.stdout
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


def get_enhanced_text(filename: str) -> str:
    """Get LLM-enhanced markdown if available."""
    md_path = ENHANCED_DIR / filename
    if md_path.exists():
        return md_path.read_text(encoding='utf-8')
    # Fallback to pdftotext
    txt_path = PDFTOTEXT_DIR / filename.replace('.md', '.txt')
    if txt_path.exists():
        return txt_path.read_text(encoding='utf-8')
    return ""


def build_prompt(full_text: str, enhanced_md: str, current_content: str) -> str:
    """Build detailed extraction prompt."""
    # Combine sources: enhanced markdown (has LaTeX) + full text (has results)
    combined = enhanced_md + "\n\n--- FULL TEXT ---\n\n" + full_text[:20000]

    prompt = f"""你是电磁暂态(EMT)仿真领域的专家。请详细分析以下论文，提取所有技术细节。

当前source page已有摘要信息：
{current_content[:2000]}

请结合以下论文全文，提取更深层次的技术内容：
{combined[:60000]}

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
    {{"test_case": "测试场景名称", "description": "结果描述，包含具体数值", "comparison": "与基线的对比（如'比传统方法快X倍'）"}}
  ],
  "quantitative_findings": [
    "具体数值型发现1（如：仿真速度提升X倍，误差<Y%，最大偏差Z%等）",
    "发现2",
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
  }}
}}

要求：
1. 所有公式必须保留LaTeX格式（$...$或$$...$$）
2. 仿真结果必须包含具体数值（不要只说'效果好'，要说'误差<0.5%'）
3. 算法步骤要详细，不能简化为几个词
4. 只输出JSON，不要其他文字
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

    return "\n".join(format_section(title, content) for title, content in sections)


def process_single_file(filename: str, src_file: Path) -> tuple:
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

    # Skip if already has detailed sections
    if '## 方法细节' in current_content or '## 仿真结果' in current_content:
        return (filename, True, "already enriched")

    # Build prompt
    input_text = full_text or enhanced_md
    if not input_text.strip():
        return (filename, False, "no text available")

    prompt = build_prompt(input_text, enhanced_md, current_content)

    # Call LLM with retry and timeout
    try:
        response = client.messages.create(
            model=LLM_MODEL,
            max_tokens=8000,
            temperature=0.1,
            timeout=180.0,  # 3 minute HTTP timeout
            messages=[{"role": "user", "content": prompt}]
        )

        llm_text = ""
        for block in response.content:
            if hasattr(block, 'text') and block.text:
                llm_text = block.text
                break

        if not llm_text:
            return (filename, False, "empty LLM response")

        data = extract_json_from_response(llm_text)
        if not data:
            return (filename, False, "failed to parse JSON")

        # Render and append
        rendered = render_deep_data(data)
        if not rendered.strip():
            return (filename, False, "no data extracted")

        # Check if file ends with newline
        if not current_content.endswith('\n'):
            current_content += '\n'

        # Append new sections
        new_content = current_content + rendered
        src_file.write_text(new_content, encoding='utf-8')

        return (filename, True, f"enriched ({len(rendered)} chars)")

    except Exception as e:
        return (filename, False, str(e)[:100])


def main(dry_run: bool = False, limit: int = 0, concurrency: int = 8):
    print("=" * 60)
    print("Deep enrichment of source pages")
    print("=" * 60)

    source_files = sorted([f for f in WIKI_SOURCES.glob("*.md") if f.name not in done_set])
    total = len(source_files) + len(done_set)
    print(f"Total: {total}, Remaining: {len(source_files)}")

    if limit > 0:
        source_files = source_files[:limit]
        print(f"Limited to {len(source_files)} files (dry run)")

    if not source_files:
        print("No files to process!")
        return

    start_time = time.time()
    count = len(checkpoint['done'])
    completed = 0

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {}
        for src_file in source_files:
            future = executor.submit(process_single_file, src_file.name, src_file)
            futures[future] = src_file.name

        for future in as_completed(futures):
            filename, success, msg = future.result()
            count += 1
            completed += 1

            if success:
                checkpoint['done'].append(filename)
                print(f"  [{count}/{total}] {filename[:50]}... OK: {msg}")
            else:
                checkpoint['failed'].append(filename)
                print(f"  [{count}/{total}] {filename[:50]}... FAIL: {msg}")

            if completed % 10 == 0:
                with open(CHECKPOINT, 'w') as f:
                    json.dump(checkpoint, f, indent=2, ensure_ascii=False)
                elapsed = (time.time() - start_time) / 60
                print(f"  >> Checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed ({elapsed:.1f}m)")

    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

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
    args = parser.parse_args()
    main(dry_run=args.dry_run, limit=args.limit, concurrency=args.concurrency)
