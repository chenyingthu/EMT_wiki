#!/usr/bin/env python3
"""
Extract abstracts from PDFs for papers with empty abstracts.
Updates metadata.json and source page frontmatter.
"""

import os
import re
import json
import subprocess
import argparse

def extract_pdf_text(pdf_path, pages=2):
    """Extract first N pages of text from PDF."""
    if not os.path.exists(pdf_path):
        return None
    try:
        result = subprocess.run(
            ['pdftotext', '-l', str(pages), '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=30
        )
        text = result.stdout
        if len(text) < 100:
            result = subprocess.run(
                ['pdftotext', '-l', str(pages), pdf_path, '-'],
                capture_output=True, text=True, timeout=30
            )
            text = result.stdout
        return text
    except Exception as e:
        return None

def extract_abstract_from_text(text, title):
    """Extract a likely abstract from PDF text.
    Strategy: First meaningful paragraph(s) after title/author block.
    """
    if not text or len(text) < 100:
        return None

    # Clean text
    text = text[:8000]

    # Remove header/footer-like lines
    lines = text.split('\n')

    # Find abstract: typically starts after title and authors
    # Look for first substantial paragraph (50+ words, not all caps)
    paragraphs = []
    current = []
    for line in lines:
        line = line.strip()
        if not line:
            if current:
                para = ' '.join(current)
                if len(para) > 50:
                    paragraphs.append(para)
                current = []
        else:
            current.append(line)
    if current:
        para = ' '.join(current)
        if len(para) > 50:
            paragraphs.append(para)

    # Skip first few (title, authors, affiliations, dates)
    # Abstract is usually paragraph 3-6
    candidates = paragraphs[2:6] if len(paragraphs) > 2 else paragraphs

    # Pick the first candidate that looks like an abstract
    for p in candidates:
        words = p.split()
        if len(words) < 30:
            continue
        # Skip if mostly junk/artifacts
        if sum(1 for c in p if c.isalpha() or c.isalpha()) < len(p) * 0.3:
            continue
        # Skip headers/metadata lines
        if p.lower().startswith('article history') or p.lower().startswith('index terms') or p.lower().startswith('keywords') and len(p) < 100:
            continue
        # Should not be all references/headers
        if p.count('http') > 2 or p.count('IEEE') > 3:
            continue
        # Clean up
        cleaned = re.sub(r'\s+', ' ', p).strip()
        if len(cleaned) > 80:
            return cleaned

    # Fallback: first long paragraph
    for p in paragraphs:
        if len(p) > 80:
            return p

    return None

def extract_abstract(pdf_path, title):
    """Extract abstract from PDF."""
    text = extract_pdf_text(pdf_path)
    if not text:
        return None
    return extract_abstract_from_text(text, title)

def find_source_page_by_title(title, sources_dir='wiki/sources'):
    """Find source page that might match this title."""
    import glob
    for filepath in glob.glob(os.path.join(sources_dir, '*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        t_match = re.search(r'title:\s*["\'](.+?)["\']', content)
        if t_match:
            pg_title = t_match.group(1).lower()
            if title.lower() in pg_title or pg_title in title.lower():
                return filepath
    return None

def update_source_abstract(filepath, abstract):
    """Update abstract in source page markdown body."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if abstract section exists with placeholder
    placeholders = [
        '## 摘要\n\n*（摘要未提取到）*',
        '## 摘要\n\n*（待分析）*',
        '## 摘要\n\n（待进一步分析）',
        '## 摘要\n\n*（待 LLM 分析补充）*',
    ]

    for placeholder in placeholders:
        if placeholder in content:
            # Truncate abstract for display if too long
            display_abstract = abstract if len(abstract) <= 300 else abstract[:297] + '...'
            new_content = content.replace(placeholder, f'## 摘要\n\n{display_abstract}', 1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True

    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=0, help='Limit to N papers')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    args = parser.parse_args()

    with open('wiki/sources/metadata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data['papers']
    no_abstract = [p for p in papers if not p.get('abstract') or len(p.get('abstract', '').strip()) < 10]

    if args.limit > 0:
        no_abstract = no_abstract[:args.limit]

    print(f"Found {len(no_abstract)} papers without abstracts")

    success = 0
    failed = 0
    skipped = 0

    for i, p in enumerate(no_abstract):
        title = (p.get('title', '') or '').strip()
        file_path = p.get('file_path', '')

        if not file_path or not os.path.exists(file_path):
            print(f"  [{i+1}/{len(no_abstract)}] ❌ PDF not found: {title[:50]}")
            failed += 1
            continue

        print(f"  [{i+1}/{len(no_abstract)}] Extracting abstract from: {title[:50] or file_path.split('/')[-1][:50]}...", end=' ')

        abstract = extract_abstract(file_path, title)
        if abstract and len(abstract) > 30:
            # Clean up
            abstract = re.sub(r'\s+', ' ', abstract).strip()
            # Truncate to 500 chars if too long
            if len(abstract) > 500:
                abstract = abstract[:497] + '...'
            # Escape quotes
            abstract = abstract.replace('"', "'").replace('\n', ' ').replace('\r', '')

            print(f"✅ {abstract[:60]}...")

            if not args.dry_run:
                # Update metadata
                p['abstract'] = abstract
                # Update source page if exists
                src_file = find_source_page_by_title(title)
                if src_file:
                    if update_source_abstract(src_file, abstract):
                        print(f"    Updated source: {os.path.basename(src_file)}")
                    else:
                        print(f"    Source already has abstract or format issue")

            success += 1
        else:
            print(f"❌ No abstract found")
            failed += 1

    # Save metadata
    if not args.dry_run:
        data['papers'] = papers
        with open('wiki/sources/metadata.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n=== Summary ===")
    print(f"Success: {success}, Failed: {failed}, Skipped: {skipped}")
    print(f"Updated metadata.json: {'yes' if not args.dry_run else 'no (dry run)'}")

if __name__ == '__main__':
    main()
