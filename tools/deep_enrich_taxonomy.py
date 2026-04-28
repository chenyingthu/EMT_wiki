#!/home/chenying/anaconda3/bin/python3
"""
Deep enrichment of taxonomy pages (topics, methods, models, entities).

Aggregates data from enriched source pages to create comprehensive
taxonomy pages with performance tables, parameter comparisons, etc.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

from llm_client import make_llm_client

WIKI_DIR = Path("wiki")
SOURCES_DIR = WIKI_DIR / "sources"
TOPICS_DIR = WIKI_DIR / "topics"
METHODS_DIR = WIKI_DIR / "methods"
MODELS_DIR = WIKI_DIR / "models"
ENTITIES_DIR = WIKI_DIR / "entities"

CHECKPOINT = Path(".deep_enrich_taxonomy.json")
TAXONOMY_MARKER_START = "<!-- taxonomy-enrich:start -->"
TAXONOMY_MARKER_END = "<!-- taxonomy-enrich:end -->"
BATCH_SIZE = 30


def load_checkpoint():
    """Load checkpoint if exists."""
    if CHECKPOINT.exists():
        with open(CHECKPOINT, 'r') as f:
            return json.load(f)
    return {"done": [], "failed": []}


def save_checkpoint(data):
    """Save checkpoint."""
    with open(CHECKPOINT, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def extract_wikilinks(content: str) -> list:
    """Extract all wikilinks from content."""
    # Match [[link|text]] or [[link]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)


def parse_source_page(filepath: Path) -> dict:
    """Parse a source page and extract relevant data."""
    content = filepath.read_text(encoding='utf-8')

    # Extract frontmatter
    frontmatter = {}
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                frontmatter[key.strip()] = val.strip().strip('"\'')

    # Extract sections
    data = {
        'title': frontmatter.get('title', filepath.stem),
        'authors': frontmatter.get('authors', ''),
        'year': frontmatter.get('year', ''),
        'tags': frontmatter.get('tags', []),
    }

    # Extract wikilinks from different sections
    wikilinks = extract_wikilinks(content)

    # Extract method details if available
    method_section = re.search(r'## 方法细节\s*\n(.*?)(?=##|$)', content, re.DOTALL)
    if method_section:
        data['method_details'] = method_section.group(1).strip()

    # Extract simulation results
    results_section = re.search(r'## 仿真结果\s*\n(.*?)(?=##|$)', content, re.DOTALL)
    if results_section:
        data['simulation_results'] = results_section.group(1).strip()

    # Extract quantitative findings
    findings_section = re.search(r'## 量化发现\s*\n(.*?)(?=##|$)', content, re.DOTALL)
    if findings_section:
        data['quantitative_findings'] = findings_section.group(1).strip()

    # Extract key equations
    equations_section = re.search(r'## 关键公式\s*\n(.*?)(?=##|$)', content, re.DOTALL)
    if equations_section:
        data['key_equations'] = equations_section.group(1).strip()

    # Extract core contributions
    contrib_section = re.search(r'## 核心贡献\s*\n(.*?)(?=##|$)', content, re.DOTALL)
    if contrib_section:
        data['core_contributions'] = contrib_section.group(1).strip()

    return data, wikilinks


def collect_papers_for_taxonomy(taxonomy_file: Path, all_sources: dict) -> list:
    """Find all papers that reference this taxonomy."""
    taxonomy_name = taxonomy_file.stem
    papers = []

    for source_name, (data, wikilinks) in all_sources.items():
        # Check if this paper references the taxonomy
        if taxonomy_name in [wl.lower().replace(' ', '-') for wl in wikilinks]:
            papers.append({
                'name': source_name,
                'data': data
            })
        else:
            # Also check if taxonomy name appears in the file content
            content = str(data)
            if taxonomy_name.lower().replace('-', ' ') in content.lower():
                papers.append({
                    'name': source_name,
                    'data': data
                })

    return papers


def format_paper_summaries(papers: list) -> str:
    paper_summaries = []
    for p in papers:
        summary = f"""
论文: {p['name']}
标题: {p['data'].get('title', 'N/A')}
年份: {p['data'].get('year', 'N/A')}
核心贡献: {p['data'].get('core_contributions', 'N/A')[:500]}
仿真结果: {p['data'].get('simulation_results', 'N/A')[:500]}
量化发现: {p['data'].get('quantitative_findings', 'N/A')[:500]}
"""
        paper_summaries.append(summary)
    return "\n---\n".join(paper_summaries)


def build_evidence_prompt(taxonomy_type: str, taxonomy_name: str, papers: list) -> str:
    papers_text = format_paper_summaries(papers)
    return f"""你是电力系统电磁暂态(EMT)仿真领域的专家。请从以下论文批次中提取"{taxonomy_name}"相关证据。

分类类型: {taxonomy_type}
论文批次数: {len(papers)}

{papers_text}

请输出紧凑中文Markdown，只包含可追溯证据：
- 方法/模型/主题关键点
- 数学公式或参数
- 仿真平台、测试系统、数值结果
- 工程限制和适用条件

每条证据尽量带论文名或年份。不要写泛泛背景。"""


def build_taxonomy_prompt(taxonomy_type: str, taxonomy_name: str, taxonomy_content: str, evidence_blocks: list, paper_count: int) -> str:
    """Build LLM prompt for taxonomy enrichment."""

    evidence_text = "\n\n--- 批次证据 ---\n\n".join(evidence_blocks)

    prompt = f"""你是一位电力系统电磁暂态(EMT)仿真领域的专家。请基于以下论文数据，为"{taxonomy_name}"生成深度增强内容。

## 当前分类页面内容

{taxonomy_content[:3000]}

## 相关论文证据（覆盖{paper_count}篇）

{evidence_text[:50000]}

## 任务

请根据分类页面的类型（topic/method/model），生成相应的深度增强内容。

如果是**方法页(method)**，请输出以下章节：
1. 核心原理详解（基于论文的方法细节，包含数学公式LaTeX）
2. 算法流程（详细步骤）
3. 参数选取指南（不同场景下的参数策略）
4. 性能分析（汇总所有论文的性能数据，用Markdown表格）
5. 最佳实践与注意事项
6. 与其他方法的对比

如果是**模型页(model)**，请输出：
1. 各类模型数学描述（详细模型、平均值模型、等效模型的数学公式）
2. 仿真参数参考表（汇总论文中的参数，用表格）
3. 模型选择指南（不同场景推荐）
4. 前沿研究方向

如果是**主题页(topic)**，请输出：
1. 关键技术详解
2. 硬件平台对比（如果有）
3. 实际应用案例汇总
4. 研究趋势与开放问题

请用中文输出，所有数学公式使用LaTeX格式。输出纯Markdown，不要JSON。
"""

    return prompt


def strip_taxonomy_enrichment(content: str) -> str:
    marker_pattern = rf'\n?{re.escape(TAXONOMY_MARKER_START)}[\s\S]*?{re.escape(TAXONOMY_MARKER_END)}\n?'
    content = re.sub(marker_pattern, '\n', content)
    return re.sub(r'\n## 深度增强内容\n[\s\S]*?(?=\n## 来源论文|\Z)', '\n', content).rstrip() + '\n'


def has_taxonomy_enrichment(content: str) -> bool:
    if TAXONOMY_MARKER_START in content and TAXONOMY_MARKER_END in content:
        return True
    return '## 深度增强内容' in content


def chunked(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def process_taxonomy(taxonomy_file: Path, taxonomy_type: str, all_sources: dict, llm_client, dry_run: bool = False, force: bool = False) -> tuple:
    """Process a single taxonomy file."""
    taxonomy_name = taxonomy_file.stem
    taxonomy_content = taxonomy_file.read_text(encoding='utf-8')

    if has_taxonomy_enrichment(taxonomy_content) and not force:
        return (taxonomy_name, True, "already enriched")

    # Collect papers
    papers = collect_papers_for_taxonomy(taxonomy_file, all_sources)

    if not papers:
        return (taxonomy_name, False, "no papers found")

    try:
        evidence_blocks = []
        for batch in chunked(papers, BATCH_SIZE):
            evidence_prompt = build_evidence_prompt(taxonomy_type, taxonomy_name, batch)
            evidence = llm_client.complete(evidence_prompt, max_tokens=6000, temperature=0.1, timeout=240.0)
            if evidence.strip():
                evidence_blocks.append(evidence.strip())

        if not evidence_blocks:
            return (taxonomy_name, False, "empty evidence response")

        prompt = build_taxonomy_prompt(taxonomy_type, taxonomy_name, taxonomy_content, evidence_blocks, len(papers))
        llm_text = llm_client.complete(prompt, max_tokens=12000, temperature=0.1, timeout=300.0)

        if not llm_text:
            return (taxonomy_name, False, "empty LLM response")

        new_content = (
            strip_taxonomy_enrichment(taxonomy_content)
            + f"\n{TAXONOMY_MARKER_START}\n## 深度增强内容\n\n{llm_text.strip()}\n{TAXONOMY_MARKER_END}\n"
        )
        if dry_run:
            return (taxonomy_name, True, f"dry-run enriched with {len(llm_text)} chars from {len(papers)} papers")

        taxonomy_file.write_text(new_content, encoding='utf-8')

        return (taxonomy_name, True, f"enriched with {len(llm_text)} chars from {len(papers)} papers")

    except Exception as e:
        return (taxonomy_name, False, str(e)[:100])


def main(dry_run: bool = False, provider: str = None, model: str = None, force: bool = False):
    print("=" * 60, flush=True)
    print("Deep enrichment of taxonomy pages", flush=True)
    print("=" * 60, flush=True)

    checkpoint = load_checkpoint()
    done_set = set(checkpoint.get('done', []))
    print(f"Checkpoint: {len(done_set)} already done", flush=True)
    llm_client = make_llm_client(provider=provider, model=model)

    # Load all source pages (with progress)
    print("Loading source pages...", flush=True)
    all_sources = {}
    source_files = list(SOURCES_DIR.glob("*.md"))
    total_sources = len(source_files)

    for i, source_file in enumerate(source_files):
        try:
            data, wikilinks = parse_source_page(source_file)
            all_sources[source_file.stem] = (data, wikilinks)
            if (i + 1) % 100 == 0:
                print(f"  Loaded {i + 1}/{total_sources}...", flush=True)
        except Exception as e:
            print(f"  Warning: failed to parse {source_file.name}: {e}", flush=True)

    print(f"Loaded {len(all_sources)} source pages", flush=True)

    # Process taxonomy files
    taxonomy_files = []

    if TOPICS_DIR.exists():
        for f in TOPICS_DIR.glob("*.md"):
            taxonomy_files.append(('topic', f))

    if METHODS_DIR.exists():
        for f in METHODS_DIR.glob("*.md"):
            taxonomy_files.append(('method', f))

    if MODELS_DIR.exists():
        for f in MODELS_DIR.glob("*.md"):
            taxonomy_files.append(('model', f))

    if ENTITIES_DIR.exists():
        for f in ENTITIES_DIR.glob("*.md"):
            taxonomy_files.append(('entity', f))

    # Filter out already done
    taxonomy_files = [(t, f) for t, f in taxonomy_files if force or f.stem not in done_set]

    total = len(taxonomy_files) + len(done_set)
    print(f"Total taxonomy pages: {total}, Remaining: {len(taxonomy_files)}")

    if not taxonomy_files:
        print("All taxonomy pages already enriched!")
        return

    # Process
    count = len(done_set)
    failed = []

    for taxonomy_type, taxonomy_file in taxonomy_files:
        count += 1
        name = taxonomy_file.stem
        print(f"\n[{count}/{total}] Processing {taxonomy_type}: {name}...")

        result_name, success, msg = process_taxonomy(taxonomy_file, taxonomy_type, all_sources, llm_client, dry_run, force)

        if success:
            if not dry_run:
                checkpoint['done'] = sorted(set(checkpoint.get('done', []) + [name]))
                checkpoint['failed'] = [failed_name for failed_name in checkpoint.get('failed', []) if failed_name != name]
            print(f"  ✓ OK: {msg}")
        else:
            if not dry_run:
                checkpoint['failed'] = sorted(set(checkpoint.get('failed', []) + [name]))
            failed.append(name)
            print(f"  ✗ FAIL: {msg}")

        # Save checkpoint periodically
        if count % 5 == 0 and not dry_run:
            save_checkpoint(checkpoint)
            print(f"  >> Checkpoint saved: {len(checkpoint['done'])} done")

    if not dry_run:
        save_checkpoint(checkpoint)

    print("\n" + "=" * 60)
    print(f"Completed!")
    print(f"Done: {len(checkpoint['done'])}")
    print(f"Failed: {len(checkpoint['failed'])}")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing files or checkpoint')
    parser.add_argument('--llm-provider', choices=['codex', 'openai', 'anthropic'], default=os.environ.get('WIKI_LLM_PROVIDER', 'codex'))
    parser.add_argument('--model', default=None, help='Override provider model')
    parser.add_argument('--force', action='store_true', help='Regenerate even if page already has enrichment')
    args = parser.parse_args()
    main(dry_run=args.dry_run, provider=args.llm_provider, model=args.model, force=args.force)
