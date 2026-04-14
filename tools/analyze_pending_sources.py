#!/usr/bin/env python3
"""
Analyze source pages with "待分析" placeholders.
Extracts PDF text, uses LLM for structured analysis,
updates source markdown files with filled sections.
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


def analyze_with_llm(title, abstract, pdf_text):
    """Use LLM to generate structured analysis."""
    content = f"论文标题：{title}\n"
    if abstract:
        content += f"摘要：{abstract}\n"
    if pdf_text:
        content += f"\n论文内容（前3页）：\n{pdf_text[:4000]}"

    prompt = f"""分析以下EMT仿真领域论文，用中文输出JSON：

```json
{{
  "contributions": ["核心贡献1", "核心贡献2", "核心贡献3"],
  "methods": ["使用的方法/技术"],
  "models": ["涉及的设备/模型"],
  "topics": ["相关主题"],
  "findings": ["主要发现/关键结果1", "主要发现/关键结果2"]
}}
```

只输出JSON，不要其他文字。

{content}"""

    try:
        response = client.messages.create(
            model="qwen3.6-plus",
            max_tokens=800,
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


def format_wikilinks(items, category='method'):
    """Convert items to wikilink format."""
    links = []
    for item in items:
        slug = re.sub(r'[^\w\u4e00-\u9fff]+', '-', item.lower()).strip('-')
        links.append(f'[[{slug}|{item}]]')
    return links


def update_source_file(filepath, analysis):
    """Replace 待分析 sections in source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'error' in analysis:
        return False

    # Build new sections
    sections = {}
    if analysis.get('contributions'):
        sections['核心贡献'] = '\n'.join(f'- {c}' for c in analysis['contributions'])
    if analysis.get('methods'):
        links = format_wikilinks(analysis['methods'])
        sections['使用的方法'] = '\n'.join(f'- {l}' for l in links)
    if analysis.get('models'):
        links = format_wikilinks(analysis['models'])
        sections['涉及的模型'] = '\n'.join(f'- {l}' for l in links)
    if analysis.get('topics'):
        links = format_wikilinks(analysis['topics'])
        sections['相关主题'] = '\n'.join(f'- {l}' for l in links)
    if analysis.get('findings'):
        sections['主要发现'] = '\n'.join(f'- {f}' for f in analysis['findings'])

    # Replace each 待分析 section (handles multiple placeholder formats)
    for section_name, section_content in sections.items():
        # Match: 待分析, *（待分析）*, *（待 LLM 分析补充）*, （待进一步分析）, *（待 LLM 分析补充）*
        pattern = rf'(## {section_name}\s*\n)(?:待分析|\*（待分析）\*|\*（待 LLM 分析补充）\*|（待进一步分析）)'
        replacement = rf'\1{section_content}'
        content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True


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
    """Extract abstract from source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    abs_match = re.search(r'abstract:\s*["\']?(.+?)["\']?\s*\n(?:abstract:|authors:|year:|tags:|sources:|---)', content, re.DOTALL)
    if abs_match:
        return abs_match.group(1).strip().strip("'\"").strip()
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=0, help='Limit to N files')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    args = parser.parse_args()

    # Find files with 待分析
    source_files = []
    for filepath in sorted(glob.glob('wiki/sources/*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
        if '待分析' in c:
            source_files.append(filepath)

    if args.limit > 0:
        source_files = source_files[:args.limit]

    print(f"Found {len(source_files)} files with 待分析")

    # Checkpoint
    checkpoint_file = '.analysis_sources.json'
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

        print(f"  [{i+1}/{len(source_files)}] Analyzing: {title[:50]}...", end=' ')

        analysis = analyze_with_llm(title, abstract, pdf_text)
        if 'error' in analysis:
            print(f"❌ {analysis['error']}")
            failed += 1
        else:
            if not args.dry_run:
                ok = update_source_file(filepath, analysis)
                if ok:
                    print(f"✅ {len(analysis.get('contributions', []))} contributions")
                    success += 1
                else:
                    print("❌ Update failed")
                    failed += 1
            else:
                print(f"✅ (dry-run) {json.dumps(analysis, ensure_ascii=False)[:80]}")
                success += 1

        # Checkpoint every 5
        if (i + 1) % 5 == 0 and not args.dry_run:
            done_list = [f for f in source_files[:i+1] if os.path.exists(f) and '待分析' not in open(f).read()]
            json.dump({'done': done_list}, open(checkpoint_file, 'w'), ensure_ascii=False, indent=2)

        time.sleep(1.5)

    # Save final checkpoint
    if not args.dry_run:
        done_list = [f for f in source_files if os.path.exists(f) and '待分析' not in open(f).read()]
        with open(checkpoint_file, 'w') as f:
            json.dump({'done': done_list}, f, ensure_ascii=False, indent=2)

    print(f"\n=== Summary ===")
    print(f"Success: {success}, Failed: {failed}")


if __name__ == '__main__':
    main()
