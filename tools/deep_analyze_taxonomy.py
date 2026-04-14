#!/usr/bin/env python3
"""
Deep analysis of papers for a specific taxonomy page.
Extracts text from PDFs, uses LLM for structured analysis,
generates enriched taxonomy page with comparison tables and technical synthesis.
"""

import os
import re
import glob
import json
import subprocess
import argparse
import time

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://coding.dashscope.aliyuncs.com/apps/anthropic"),
)

# ─── Paper-Taxonomy Mapping ───────────────────────────────────────

TAXONOMY_PAPERS = {
    'mmc-model': {
        'wikilink': 'mmc-model',
        'title': '模块化多电平换流器 (MMC)',
        'chinese_name': 'MMC',
        'description': 'MMC是HVDC输电的核心拓扑',
    },
    'transmission-line-model': {
        'wikilink': 'transmission-line-model',
        'title': '输电线路模型',
        'chinese_name': '输电线路',
        'description': 'EMT仿真中的线路建模方法',
    },
    'real-time-simulation': {
        'wikilink': 'real-time-simulation',
        'title': '实时仿真',
        'chinese_name': '实时仿真',
        'description': 'FPGA/RTDS/GPU实时仿真技术',
    },
    'frequency-dependent-modeling': {
        'wikilink': 'frequency-dependent-modeling',
        'title': '频率相关建模',
        'chinese_name': '频变建模',
        'description': '矢量拟合、频变参数、宽频阻抗建模',
    },
    'parallel-computing': {
        'wikilink': 'parallel-computing',
        'title': '并行计算',
        'chinese_name': '并行计算',
        'description': '空间分解、时间并行、GPU加速',
    },
    'transformer-model': {
        'wikilink': 'transformer-model',
        'title': '变压器模型',
        'chinese_name': '变压器',
        'description': '磁滞、白盒、对偶电路、高频模型',
    },
    'co-simulation': {
        'wikilink': 'co-simulation',
        'title': '混合仿真',
        'chinese_name': '混合仿真',
        'description': '机电-电磁暂态混合仿真、多速率',
    },
    'vsc-model': {
        'wikilink': 'vsc-model',
        'title': '电压源换流器 (VSC)',
        'chinese_name': 'VSC',
        'description': '两电平/三电平拓扑、HVDC核心设备',
    },
    'synchronous-machine-model': {
        'wikilink': 'synchronous-machine-model',
        'title': '同步电机模型',
        'chinese_name': '同步电机',
        'description': '相域/dq0/VBR模型、交叉磁化',
    },
    'average-value-model': {
        'wikilink': 'average-value-model',
        'title': '平均值模型',
        'chinese_name': '平均值模型',
        'description': '换流器开关周期平均化建模',
    },
    'state-space-method': {
        'wikilink': 'state-space-method',
        'title': '状态空间法',
        'chinese_name': '状态空间法',
        'description': '一阶微分方程组建模、矩阵指数法',
    },
    'numerical-integration': {
        'wikilink': 'numerical-integration',
        'title': '数值积分',
        'chinese_name': '数值积分',
        'description': '梯形法、Gear法、2S-DIRK等',
    },
    'vector-fitting': {
        'wikilink': 'vector-fitting',
        'title': '矢量拟合',
        'chinese_name': '矢量拟合',
        'description': '频率响应的有理函数逼近算法',
    },
    'network-equivalent': {
        'wikilink': 'network-equivalent',
        'title': '网络等值',
        'chinese_name': '网络等值',
        'description': 'Ward/FDNE/Thevenin等值',
    },
    'dynamic-phasor': {
        'wikilink': 'dynamic-phasor',
        'title': '动态相量法',
        'chinese_name': '动态相量',
        'description': '扩展频率范围的相量域建模',
    },
    'vsc-hvdc': {
        'wikilink': 'vsc-hvdc',
        'title': 'VSC-HVDC',
        'chinese_name': '柔性直流输电',
        'description': '柔性直流输电、独立有功无功控制',
    },
}


def find_papers(wikilink, source_dir='wiki/sources'):
    """Find all source papers that reference a given wikilink."""
    papers = []
    for filepath in sorted(glob.glob(os.path.join(source_dir, '*.md'))):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        body = content.split('---', 2)[-1] if content.count('---') >= 2 else content
        if f'[[{wikilink}]]' in body:
            title_match = re.search(r'title:\s*["\'](.+?)["\']', content)
            year_match = re.search(r'year:\s*(\d{4})', content)
            sources_match = re.search(r'sources:\s*\["(.*?)"\]', content)
            title = title_match.group(1) if title_match else '未知'
            year = year_match.group(1) if year_match else '未知'
            sources = sources_match.group(1) if sources_match else ''
            papers.append({
                'title': title,
                'year': year,
                'sources': sources,
                'source_file': filepath,
            })
    return papers


def extract_pdf_text(pdf_path, max_pages=4):
    """Extract text from PDF (first N pages for key content)."""
    if not pdf_path or not os.path.exists(pdf_path):
        return None
    try:
        result = subprocess.run(
            ['pdftotext', '-l', str(max_pages), '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=30
        )
        text = result.stdout
        if len(text) < 100:
            # Try without layout
            result = subprocess.run(
                ['pdftotext', '-l', str(max_pages), pdf_path, '-'],
                capture_output=True, text=True, timeout=30
            )
            text = result.stdout
        return text[:8000]  # Limit to first 8000 chars
    except Exception as e:
        return None


def find_pdf(paper, base_dir='/home/chenying/researches/EMT_LLM_Wiki'):
    """Find PDF for a paper from its sources field."""
    sources = paper.get('sources', '')
    if not sources:
        return None
    # Try direct path
    pdf_path = os.path.join(base_dir, sources)
    if os.path.exists(pdf_path):
        return pdf_path
    # Try searching
    title = paper.get('title', '').lower()
    keywords = [w for w in re.split(r'[\s\-_]+', title) if len(w) > 4][:4]
    if not keywords:
        return None
    for root, dirs, files in os.walk(os.path.join(base_dir, 'EMT_Doc')):
        for fn in files:
            if not fn.endswith('.pdf'):
                continue
            fn_lower = fn.lower()
            if any(kw in fn_lower for kw in keywords):
                return os.path.join(root, fn)
    return None


def analyze_paper(text, title, year):
    """Use LLM to analyze a paper and extract structured information."""
    prompt = f"""分析以下EMT仿真领域论文，提取结构化信息。以JSON格式输出：

```json
{{
  "methods": ["使用的方法/技术，如平均值建模、状态空间法等"],
  "models": ["涉及的设备/模型，如MMC、变压器等"],
  "contributions": ["3-5个核心贡献，每个一句话"],
  "validation": "验证方式：仿真/实验/对比",
  "key_results": ["2-3个关键结果/数据，每个一句话"],
  "innovation": "创新点（一句话）",
  "category": "论文类型：review/method/experiment/application"
}}
```

只输出JSON，不要其他文字。

论文标题：{title}
年份：{year}

论文内容（前4页）：
{text[:5000]}"""

    try:
        response = client.messages.create(
            model="qwen3.6-plus",
            max_tokens=1500,
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}],
        )
        for block in response.content:
            if block.type == "text" and block.text:
                # Extract JSON from response
                text_result = block.text.strip()
                # Try to find JSON block
                json_match = re.search(r'```json\s*\n(.*?)\n```', text_result, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group(1))
                # Try direct JSON parse
                return json.loads(text_result)
    except Exception as e:
        return {'error': str(e)}


def generate_enhanced_page(taxonomy_key, papers_data, existing_content):
    """Generate enriched taxonomy page content."""
    # Group papers by year for timeline
    by_year = {}
    for p in papers_data:
        y = p.get('year', 'unknown')
        if y not in by_year:
            by_year[y] = []
        by_year[y].append(p)

    # Collect all methods
    all_methods = {}
    all_categories = {}
    for p in papers_data:
        info = p.get('analysis', {})
        for m in info.get('methods', []):
            m_lower = m.lower()
            if m_lower not in all_methods:
                all_methods[m_lower] = {'name': m, 'count': 0, 'papers': []}
            all_methods[m_lower]['count'] += 1
            all_methods[m_lower]['papers'].append(p['title'][:60])

    # Collect innovations
    innovations = []
    for p in papers_data:
        info = p.get('analysis', {})
        if info.get('innovation'):
            innovations.append({
                'title': p['title'][:80],
                'year': p['year'],
                'innovation': info['innovation']
            })

    # Build content
    sections = []

    # 1. Methods comparison table
    if all_methods:
        sorted_methods = sorted(all_methods.values(), key=lambda x: -x['count'])
        method_table = '| 方法/技术 | 论文数 | 代表论文 |\n|----------|--------|----------|\n'
        for m in sorted_methods:
            rep = m['papers'][0] if m['papers'] else ''
            method_table += f'| {m["name"]} | {m["count"]} | {rep}... |\n'
        sections.append(('## 主要方法与技对比', method_table))

    # 2. Technical timeline
    timeline = ''
    for year in sorted(by_year.keys()):
        papers = by_year[year]
        timeline += f'### {year}年 ({len(papers)}篇)\n'
        for p in papers:
            info = p.get('analysis', {})
            innov = info.get('innovation', '')
            timeline += f'- **{p["title"][:80]}**: {innov}\n'
        timeline += '\n'
    sections.append(('## 技术演进脉络', timeline))

    # 3. Key innovations summary
    if innovations:
        innov_text = ''
        for inv in sorted(innovations, key=lambda x: x['year'])[:20]:
            innov_text += f'- [{inv["year"]}] {inv["title"]}: {inv["innovation"]}\n'
        sections.append(('## 核心创新点汇总', innov_text))

    return sections


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('taxonomy', help='Taxonomy key (e.g., mmc-model)')
    parser.add_argument('--limit', type=int, default=0, help='Limit to N papers')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    args = parser.parse_args()

    if args.taxonomy not in TAXONOMY_PAPERS:
        print(f"Unknown taxonomy: {args.taxonomy}")
        print(f"Available: {', '.join(TAXONOMY_PAPERS.keys())}")
        return

    config = TAXONOMY_PAPERS[args.taxonomy]
    print(f"=== Deep Analysis: {config['title']} ===")

    # Find papers
    papers = find_papers(config['wikilink'])
    if args.limit > 0:
        papers = papers[:args.limit]
    print(f"Found {len(papers)} papers")

    # Find PDFs and analyze
    results = []
    checkpoint_file = f'.analysis_{args.taxonomy}.json'
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            results = json.load(f)
        processed_titles = {r['title'] for r in results}
        papers = [p for p in papers if p['title'] not in processed_titles]
        print(f"Resuming: {len(results)} already done, {len(papers)} remaining")

    for i, paper in enumerate(papers):
        pdf_path = find_pdf(paper)
        if not pdf_path:
            print(f"  [{i+1}/{len(papers)}] ❌ PDF not found: {paper['title'][:60]}")
            results.append({**paper, 'analysis': {'error': 'PDF not found'}})
            continue

        text = extract_pdf_text(pdf_path)
        if not text or len(text) < 200:
            print(f"  [{i+1}/{len(papers)}] ❌ Text extraction failed: {paper['title'][:60]}")
            results.append({**paper, 'analysis': {'error': 'Text extraction failed'}})
            continue

        print(f"  [{i+1}/{len(papers)}] Analyzing: {paper['title'][:60]}...", end=' ')
        analysis = analyze_paper(text, paper['title'], paper['year'])
        if 'error' in analysis:
            print(f"❌ LLM error: {analysis['error']}")
        else:
            print(f"✅ {analysis.get('innovation', 'OK')[:50]}")

        results.append({**paper, 'analysis': analysis})

        # Save checkpoint every 5 papers
        if (i + 1) % 5 == 0:
            with open(checkpoint_file, 'w') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"    [checkpoint saved: {len(results)} papers]")

        time.sleep(2)  # Rate limiting

    # Final save
    with open(checkpoint_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Generate enriched content
    sections = generate_enhanced_page(args.taxonomy, results, None)

    print(f"\n=== Summary ===")
    print(f"Total analyzed: {len(results)}")
    successful = [r for r in results if 'analysis' in r and 'error' not in r['analysis']]
    print(f"Successful: {len(successful)}")
    print(f"\nGenerated sections:")
    for heading, _ in sections:
        print(f"  - {heading}")


if __name__ == '__main__':
    main()
