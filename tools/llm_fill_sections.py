#!/usr/bin/env python3
"""
LLM deep analysis for source pages with empty 使用的方法/涉及的模型/相关主题 sections.
Only fills these 3 sections (not 核心贡献 or 主要发现 which are already filled).
Extracts PDF text, uses LLM for structured analysis, updates source markdown files.
"""

import os
import re
import glob
import json
import subprocess
import time
import argparse

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://coding.dashscope.aliyuncs.com/apps/anthropic"),
)

# Taxonomy wikilinks for validation (maps keywords to wikilink format)
TAXONOMY_WIKILINKS = {
    'mmc': '[[mmc-model|MMC]]',
    'mmc-model': '[[mmc-model|MMC]]',
    'vsc': '[[vsc-model|VSC]]',
    'vsc-model': '[[vsc-model|VSC]]',
    'lcc': '[[lcc-model|LCC]]',
    'lcc-model': '[[lcc-model|LCC]]',
    'dfig': '[[dfig-model|DFIG]]',
    'dfig-model': '[[dfig-model|DFIG]]',
    'pmsm': '[[pmsm-model|PMSM]]',
    'pmsm-model': '[[pmsm-model|PMSM]]',
    'transformer': '[[transformer-model|变压器]]',
    'transformer-model': '[[transformer-model|变压器]]',
    'transmission-line': '[[transmission-line-model|输电线路]]',
    'transmission-line-model': '[[transmission-line-model|输电线路]]',
    'synchronous-machine': '[[synchronous-machine-model|同步电机]]',
    'synchronous-machine-model': '[[synchronous-machine-model|同步电机]]',
    'fdne': '[[fdne-model|FDNE]]',
    'fdne-model': '[[fdne-model|FDNE]]',
    'cable': '[[cable-model|电缆]]',
    'cable-model': '[[cable-model|电缆]]',
    'co-simulation': '[[co-simulation|混合仿真]]',
    'cosimulation': '[[co-simulation|混合仿真]]',
    'co_simulation': '[[co-simulation|混合仿真]]',
    'real-time': '[[real-time-simulation|实时仿真]]',
    'realtime': '[[real-time-simulation|实时仿真]]',
    'dynamic-phasor': '[[dynamic-phasor|动态相量法]]',
    'dynamic phasor': '[[dynamic-phasor|动态相量法]]',
    'parallel': '[[parallel-computing|并行计算]]',
    'parallel-computing': '[[parallel-computing|并行计算]]',
    'frequency-dependent': '[[frequency-dependent-modeling|频率相关建模]]',
    'freq-dependent': '[[frequency-dependent-modeling|频率相关建模]]',
    'network-equivalent': '[[network-equivalent|网络等值]]',
    'net-equivalent': '[[network-equivalent|网络等值]]',
    'vsc-hvdc': '[[vsc-hvdc|VSC-HVDC]]',
    'hvdc': '[[vsc-hvdc|VSC-HVDC]]',
    'ferroresonance': '[[ferroresonance|铁磁谐振]]',
    'harmonic': '[[harmonic-analysis|谐波分析]]',
    'harmonic-analysis': '[[harmonic-analysis|谐波分析]]',
    'wind-farm': '[[wind-farm-modeling|风电场建模]]',
    'wind-farm-modeling': '[[wind-farm-modeling|风电场建模]]',
    'vector-fitting': '[[vector-fitting|矢量拟合]]',
    'average-value-model': '[[average-value-model|平均值模型]]',
    'avm': '[[average-value-model|平均值模型]]',
    'nodal-analysis': '[[nodal-analysis|节点分析]]',
    'state-space': '[[state-space-method|状态空间法]]',
    'numerical-integration': '[[numerical-integration|数值积分]]',
    'trapezoidal': '[[numerical-integration|数值积分]]',
    'gear': '[[numerical-integration|数值积分]]',
    'dirk': '[[numerical-integration|数值积分]]',
    'passivity': '[[passivity-enforcement|无源性强制]]',
    'passivity-enforcement': '[[passivity-enforcement|无源性强制]]',
    'multirate': '[[multirate-method|多速率方法]]',
    'multi-rate': '[[multirate-method|多速率方法]]',
    'multirate-method': '[[multirate-method|多速率方法]]',
    'fixed-admittance': '[[fixed-admittance|恒导纳模型]]',
    'nodal': '[[fixed-admittance|恒导纳模型]]',
    'interpolation': '[[interpolation-method|插值方法]]',
    'prony': '[[prony-analysis|Prony分析]]',
    'bergeron': '[[transmission-line-model|Bergeron线路模型]]',
}


def extract_pdf_text(pdf_path, max_pages=3):
    """Extract text from PDF first pages."""
    if not pdf_path or not os.path.exists(pdf_path):
        return None
    try:
        result = subprocess.run(
            ['pdftotext', '-l', str(max_pages), '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=30
        )
        text = result.stdout
        if len(text) < 100:
            result = subprocess.run(
                ['pdftotext', '-l', str(max_pages), pdf_path, '-'],
                capture_output=True, text=True, timeout=30
            )
            text = result.stdout
        return text[:6000]
    except Exception:
        return None


def analyze_with_llm(title, abstract, pdf_text, sections_needed):
    """Use LLM to generate methods, models, topics analysis."""
    content = f"论文标题：{title}\n"
    if abstract:
        content += f"摘要：{abstract}\n"
    if pdf_text:
        content += f"\n论文内容（前3页）：\n{pdf_text[:4000]}"

    needed = ', '.join(sections_needed)
    prompt = f"""分析以下EMT仿真领域论文，用中文输出JSON。只需要以下字段：{needed}

```json
{{
  "methods": ["使用的方法/技术，如：矢量拟合、Bergeron模型、动态相量法、多速率仿真、节点分析等"],
  "models": ["涉及的设备/模型，如：MMC、VSC、LCC、DFIG、变压器、输电线路等"],
  "topics": ["相关主题，如：实时仿真、混合仿真、并行计算、频率相关建模等"]
}}
```

只输出JSON，不要其他文字。只包含有内容的字段，没有内容的字段可以省略。

{content}"""

    try:
        response = client.messages.create(
            model="qwen3.6-plus",
            max_tokens=600,
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}],
        )
        for block in response.content:
            if block.type == "text" and block.text:
                text_result = block.text.strip()
                json_match = re.search(r'```json\s*\n(.*?)\n```', text_result, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group(1))
                return json.loads(text_result)
    except Exception as e:
        return {'error': str(e)}


def format_wikilink(item, section_type):
    """Convert item to wikilink format, matching existing taxonomy pages."""
    # Try exact taxonomy match
    slug = re.sub(r'[^\w\u4e00-\u9fff]+', '-', item.lower()).strip('-')

    # Check if matches known taxonomy
    for key, wikilink in TAXONOMY_WIKILINKS.items():
        if key in slug or slug in key:
            return wikilink

    # Generate generic wikilink
    return f'[[{slug}|{item}]]'


def update_source_file(filepath, analysis, sections_needed):
    """Replace 待进一步分析 sections in source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'error' in analysis:
        return False

    updated = False
    section_map = {
        '使用的方法': ('methods', '方法'),
        '涉及的模型': ('models', '模型'),
        '相关主题': ('topics', '主题'),
    }

    for section_name, (analysis_key, section_type) in section_map.items():
        if section_name not in sections_needed:
            continue
        if analysis_key not in analysis:
            continue

        items = analysis[analysis_key]
        if not items:
            continue

        # Convert to wikilinks
        links = [format_wikilink(item, section_type) for item in items]
        section_content = '\n'.join(f'- {l}' for l in links)

        # Replace placeholder OR fill empty section
        pattern = rf'(## {section_name}\s*\n)\n?（待进一步分析）'
        replacement = rf'\1{section_content}'
        new_content = re.sub(pattern, replacement, content)
        if new_content == content:
            # Section is empty, insert content after header
            pattern_empty = rf'(## {section_name}\s*\n)'
            replacement_empty = rf'\1{section_content}\n'
            new_content = re.sub(pattern_empty, replacement_empty, content, count=1)
        if new_content != content:
            content = new_content
            updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return updated


def get_pdf_path(filepath, base_dir='/home/chenying/researches/EMT_LLM_Wiki'):
    """Get PDF path from source file's sources field."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    src_match = re.search(r'sources:\s*\["(.*?)"\]', content)
    if src_match:
        path = src_match.group(1)
        full_path = os.path.join(base_dir, path)
        if os.path.exists(full_path):
            return full_path
    return None


def get_abstract(filepath):
    """Extract abstract from source file (from body 摘要 section)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    abs_match = re.search(r'## 摘要\s*\n\n(.+?)(?=\n##|$)', content, re.DOTALL)
    if abs_match:
        return abs_match.group(1).strip()
    # Try frontmatter
    abs_match2 = re.search(r'abstract:\s*["\']?(.+?)["\']?\s*\n(?:abstract:|authors:|year:|tags:|sources:|---)', content, re.DOTALL)
    if abs_match2:
        return abs_match2.group(1).strip().strip("'\"").strip()
    return None


def check_section_empty(content, section_name):
    """Check if a section has 待进一步分析 placeholder OR is empty."""
    # Has placeholder text
    pattern = rf'## {section_name}\s*\n.*?（待进一步分析）'
    if re.search(pattern, content, re.DOTALL):
        return True
    # Section exists but content is empty/whitespace until next section or EOF
    pattern_empty = rf'## {section_name}\s*\n\s*(?:\n|##|$)'
    if re.search(pattern_empty, content, re.DOTALL):
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=0, help='Limit to N files')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    parser.add_argument('--sections', nargs='+', default=['使用的方法', '涉及的模型', '相关主题'],
                        help='Sections to fill')
    args = parser.parse_args()

    # Find files with 待进一步分析 in target sections
    source_files = []
    sections_per_file = {}

    for filepath in sorted(glob.glob('wiki/sources/*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        needed = []
        for section_name in args.sections:
            if check_section_empty(content, section_name):
                needed.append(section_name)

        if needed:
            source_files.append(filepath)
            sections_per_file[filepath] = needed

    if args.limit > 0:
        source_files = source_files[:args.limit]

    print(f"Found {len(source_files)} files with empty sections to fill")

    # Checkpoint
    checkpoint_file = '.analysis_deep.json'
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            done = json.load(f).get('done', [])
        source_files = [f for f in source_files if f not in done]
        print(f"Resuming: {len(done)} done, {len(source_files)} remaining")

    success = 0
    failed = 0

    for i, filepath in enumerate(source_files):
        title_match = re.search(r'title:\s*["\'](.+?)["\']', open(filepath).read())
        title = title_match.group(1) if title_match else 'unknown'

        pdf_path = get_pdf_path(filepath)
        pdf_text = extract_pdf_text(pdf_path) if pdf_path else None
        abstract = get_abstract(filepath)
        needed = sections_per_file.get(filepath, args.sections)

        # Map to LLM field names
        section_map = {'使用的方法': 'methods', '涉及的模型': 'models', '相关主题': 'topics'}
        llm_fields = [section_map.get(s, s) for s in needed]

        print(f"  [{i+1}/{len(source_files)}] Analyzing: {title[:50]}...", end=' ')

        analysis = analyze_with_llm(title, abstract, pdf_text, llm_fields)
        if 'error' in analysis:
            print(f"❌ {analysis['error']}")
            failed += 1
        else:
            if not args.dry_run:
                ok = update_source_file(filepath, analysis, needed)
                if ok:
                    methods_count = len(analysis.get('methods', []))
                    models_count = len(analysis.get('models', []))
                    topics_count = len(analysis.get('topics', []))
                    print(f"✅ methods={methods_count}, models={models_count}, topics={topics_count}")
                    success += 1
                else:
                    print("❌ Update failed")
                    failed += 1
            else:
                print(f"✅ (dry-run) {json.dumps(analysis, ensure_ascii=False)[:100]}")
                success += 1

        # Checkpoint every 5
        if (i + 1) % 5 == 0 and not args.dry_run:
            done_list = [f for f in source_files[:i+1] if f not in [ff for ff in source_files[:i+1] if '待进一步分析' in open(ff).read()]]
            json.dump({'done': done_list}, open(checkpoint_file, 'w'), ensure_ascii=False, indent=2)

        time.sleep(1.5)

    # Save final checkpoint
    if not args.dry_run:
        done_list = [f for f in source_files if os.path.exists(f) and '待进一步分析' not in open(f).read()]
        with open(checkpoint_file, 'w') as f:
            json.dump({'done': done_list}, f, ensure_ascii=False, indent=2)

    print(f"\n=== Summary ===")
    print(f"Success: {success}, Failed: {failed}")


if __name__ == '__main__':
    main()
