#!/usr/bin/env python3
"""
Update topic/method/model/entity pages with back-references to source papers.
Scans all source files for wikilinks and builds reference tables.
"""

import glob
import os
import re


def normalize_wikilink(link):
    """Return page slug from [[slug]] or [[slug|label]]."""
    target = link.split('|', 1)[0].strip()
    target = target.rsplit('/', 1)[-1]
    return target


def collect_wikilinks(source_dir='wiki/sources'):
    """Collect all wikilinks from source files."""
    wikilinks = {}  # link -> [(title, year, filepath)]

    for filepath in sorted(glob.glob(os.path.join(source_dir, '*.md'))):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        title_match = re.search(r'title:\s*["\'](.+?)["\']', content)
        year_match = re.search(r'year:\s*(\d{4})', content)
        title = title_match.group(1) if title_match else '未知'
        year = year_match.group(1) if year_match else '未知'

        # Skip frontmatter - get body only
        body = content.split('---', 2)[-1] if content.count('---') >= 2 else content
        links = re.findall(r'\[\[([^\]]+)\]\]', body)

        for link in links:
            slug = normalize_wikilink(link)
            if slug not in wikilinks:
                wikilinks[slug] = []
            wikilinks[slug].append((title, year, filepath))

    return wikilinks


def get_page_slug(filename):
    """Get the slug (filename without extension) from a taxonomy page."""
    return os.path.splitext(os.path.basename(filename))[0]


def update_page(filepath, papers, page_slug):
    """Add or update back-references section on a taxonomy page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build reference table
    if not papers:
        return  # No papers to add

    # Sort by year, then title
    papers_sorted = sorted(papers, key=lambda x: (x[1], x[0]))

    table_lines = []
    for title, year, paper_path in papers_sorted:
        paper_slug = os.path.splitext(os.path.basename(paper_path))[0]
        table_lines.append(f'| [[{paper_slug}|{title[:60]}]] | {year} |')

    table = '\n'.join(table_lines)

    # Check if section already exists
    ref_pattern = r'## 来源论文\n\n\| 论文 \| 年份 \|'
    ref_section = f'## 来源论文\n\n| 论文 | 年份 |\n|------|------|\n{table}'

    if re.search(ref_pattern, content):
        # Replace existing section
        content = re.sub(
            r'## 来源论文\n\n.*?(?=\n## |\Z)',
            ref_section,
            content,
            flags=re.DOTALL
        )
    else:
        # Append new section
        # Ensure trailing newline
        content = content.rstrip() + '\n\n' + ref_section + '\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return len(papers)


def main():
    wikilinks = collect_wikilinks()

    categories = ['wiki/topics', 'wiki/methods', 'wiki/models', 'wiki/entities']

    total_updated = 0
    for cat_dir in categories:
        for md_file in sorted(glob.glob(os.path.join(cat_dir, '**', '*.md'), recursive=True)):
            slug = get_page_slug(md_file)
            papers = wikilinks.get(slug, [])
            count = update_page(md_file, papers, slug)
            if count:
                print(f'  {slug}.md: {count} papers')
                total_updated += 1

    print(f'\nUpdated {total_updated} taxonomy pages')
    print(f'Total unique wikilinks: {len(wikilinks)}')
    print(f'Total references: {sum(len(v) for v in wikilinks.values())}')


if __name__ == '__main__':
    main()
