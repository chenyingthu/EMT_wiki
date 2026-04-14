#!/usr/bin/env python3
"""
Generate enriched taxonomy page from LLM analysis results.
Reads checkpoint JSON and produces an enriched markdown file.
"""

import json
import os
import re
import argparse


def load_analysis(taxonomy_key):
    """Load analysis results from checkpoint file."""
    checkpoint_file = f'.analysis_{taxonomy_key}.json'
    if not os.path.exists(checkpoint_file):
        print(f"No analysis found for {taxonomy_key}")
        return []
    with open(checkpoint_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def group_by_category(results):
    """Group papers by their analysis category."""
    categories = {}
    for r in results:
        info = r.get('analysis', {})
        cat = info.get('category', 'unknown')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)
    return categories


def collect_methods(results):
    """Collect and count all methods across papers."""
    methods = {}
    for r in results:
        info = r.get('analysis', {})
        for m in info.get('methods', []):
            m_lower = m.lower()
            if m_lower not in methods:
                methods[m_lower] = {'name': m, 'count': 0, 'papers': []}
            methods[m_lower]['count'] += 1
            methods[m_lower]['papers'].append(r['title'][:70])
    return sorted(methods.values(), key=lambda x: -x['count'])


def collect_models(results):
    """Collect and count all models across papers."""
    models = {}
    for r in results:
        info = r.get('analysis', {})
        for m in info.get('models', []):
            m_lower = m.lower()
            if m_lower not in models:
                models[m_lower] = {'name': m, 'count': 0}
            models[m_lower]['count'] += 1
    return sorted(models.values(), key=lambda x: -x['count'])


def collect_validations(results):
    """Collect validation approaches."""
    vals = {}
    for r in results:
        info = r.get('analysis', {})
        v = info.get('validation', '未知')
        if v not in vals:
            vals[v] = 0
        vals[v] += 1
    return sorted(vals.items(), key=lambda x: -x[1])


def build_enriched_page(taxonomy_key, config, results):
    """Build the enriched markdown page content."""
    successful = [r for r in results if 'analysis' in r and 'error' not in r['analysis']]
    methods = collect_methods(results)
    models = collect_models(results)
    validations = collect_validations(results)
    by_year = {}
    for r in results:
        y = r.get('year', 'unknown')
        if y not in by_year:
            by_year[y] = []
        by_year[y].append(r)

    lines = []

    # Read existing page to preserve frontmatter and overview
    existing_path = f'wiki/models/{taxonomy_key.replace("-model", "-model")}.md'
    if os.path.exists(existing_path):
        with open(existing_path, 'r', encoding='utf-8') as f:
            existing = f.read()
        # Keep everything up to and including the "来源论文" section
        # We'll replace from "## 主要方法" onwards
        sections = existing.split('## ')
        # Find where to insert new content
        # Keep: frontmatter + overview + main types + EMT modeling + special effects + applications + related methods/topics
        # Replace/enrich: add new sections before source papers

        # Find the ## 来源论文 section
        sp_idx = existing.find('## 来源论文')
        if sp_idx > 0:
            before_sp = existing[:sp_idx]
            after_sp = existing[sp_idx:]
        else:
            before_sp = existing
            after_sp = ''
    else:
        before_sp = f'''---
title: "{config.get('title', taxonomy_key)}"
type: model
tags: []
created: "2026-04-13"
---

# {config.get('title', taxonomy_key)}
'''
        after_sp = ''

    lines.append(before_sp)

    # ─── New Section: Methods Analysis ───
    if methods:
        lines.append('\n## 论文方法分析\n')
        lines.append(f'> 基于 {len(successful)} 篇相关论文的深度内容分析生成\n')
        lines.append('')
        lines.append('### 使用的方法/技术\n')
        lines.append('| 方法/技术 | 使用次数 | 代表论文 |\n|----------|---------|----------|')
        for m in methods[:15]:  # Top 15
            rep = m['papers'][0] if m['papers'] else ''
            lines.append(f'| {m["name"]} | {m["count"]} | {rep} |\n')
        lines.append('')

    # ─── New Section: Models ───
    if models:
        lines.append('### 涉及的设备/模型\n')
        lines.append('| 设备/模型 | 使用次数 |\n|----------|----------|')
        for m in models[:15]:
            lines.append(f'| {m["name"]} | {m["count"]} |\n')
        lines.append('')

    # ─── New Section: Validation ───
    if validations:
        lines.append('### 验证方式分布\n')
        for v, c in validations:
            lines.append(f'- **{v}**: {c} 篇\n')
        lines.append('')

    # ─── New Section: Innovation Timeline ───
    lines.append('## 技术演进脉络\n')
    for year in sorted(by_year.keys()):
        papers = by_year[year]
        lines.append(f'### {year}年 ({len(papers)}篇)\n')
        for p in papers:
            info = p.get('analysis', {})
            innov = info.get('innovation', '')
            contribs = info.get('contributions', [])
            lines.append(f'- **{p["title"][:80]}**\n')
            if innov:
                lines.append(f'  - 💡 {innov}\n')
            if contribs:
                for c in contribs[:2]:
                    lines.append(f'  - {c}\n')
        lines.append('')

    # ─── New Section: Key Insights ───
    lines.append('## 关键发现汇总\n')
    insights = []
    for r in successful:
        info = r.get('analysis', {})
        for kr in info.get('key_results', []):
            insights.append({
                'year': r['year'],
                'title': r['title'][:60],
                'result': kr
            })

    if insights:
        # Group by result type
        for ins in sorted(insights, key=lambda x: x['year'])[:30]:
            lines.append(f'- [{ins["year"]}] **{ins["title"]}**: {ins["result"]}\n')
    lines.append('')

    # ─── Original Source Papers ───
    if after_sp:
        lines.append(after_sp)

    return ''.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('taxonomy', help='Taxonomy key')
    parser.add_argument('--title', default='', help='Page title')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    args = parser.parse_args()

    results = load_analysis(args.taxonomy)
    if not results:
        print("No analysis results found")
        return

    config = {'title': args.title or args.taxonomy}
    content = build_enriched_page(args.taxonomy, config, results)

    if args.dry_run:
        print(content[:2000])
    else:
        # Write to taxonomy page
        if 'lcc' in args.taxonomy or 'mmc' in args.taxonomy or 'vsc' in args.taxonomy or 'pmsm' in args.taxonomy:
            page_path = f'wiki/models/{args.taxonomy}.md'
        else:
            page_path = f'wiki/models/{args.taxonomy}.md'

        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {page_path}")

    successful = [r for r in results if 'analysis' in r and 'error' not in r['analysis']]
    print(f"Based on {len(successful)}/{len(results)} analyzed papers")


if __name__ == '__main__':
    main()
