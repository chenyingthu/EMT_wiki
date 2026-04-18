#!/usr/bin/env python3
"""
Retry MinerU extraction for all 699 papers.
Force use MinerU first, fallback to pdftotext only if MinerU fails.
"""

import os
import json
import time
import requests
from pathlib import Path

MINERU_API = "http://localhost:8000"
WIKI_SOURCES = Path("wiki/sources")
CHECKPOINT = Path(".retry_mineru.json")

# Load checkpoint
checkpoint = {"done": [], "failed": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))

# Get all source files
source_files = sorted([f for f in WIKI_SOURCES.glob("*.md") if f.name not in done_set])
total = len(source_files) + len(done_set)
print(f"Total files: {total}, Remaining: {len(source_files)}")

def extract_with_mineru(pdf_path: str) -> tuple[str, bool]:
    """Extract text using MinerU API. Returns (text, success)"""
    try:
        # Submit task with correct format
        with open(pdf_path, 'rb') as f:
            files = {'files': (os.path.basename(pdf_path), f, 'application/pdf')}
            data = {
                'backend': 'hybrid-auto-engine',
                'return_md': 'true',
                'formula_enable': 'true',
                'table_enable': 'true'
            }
            response = requests.post(f"{MINERU_API}/tasks", files=files, data=data, timeout=60)

        if response.status_code != 202:
            return "", False

        task_id = response.json().get('task_id')
        if not task_id:
            return "", False

        # Poll for result (max 5 min)
        for _ in range(60):
            time.sleep(5)
            result = requests.get(f"{MINERU_API}/tasks/{task_id}/result", timeout=30)
            if result.status_code == 200:
                data = result.json()
                if data.get('status') == 'completed':
                    markdown = data.get('markdown', '')
                    if markdown:
                        return markdown[:15000], True
                elif data.get('status') == 'failed':
                    return "", False
        return "", False  # Timeout
    except Exception as e:
        return "", False

def save_checkpoint():
    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

# Process files
count = len(checkpoint['done'])
for src_file in source_files:
    count += 1
    filename = src_file.name

    # Find corresponding PDF
    # Read the source file to get the PDF path from sources frontmatter
    import re
    content = src_file.read_text(encoding='utf-8')
    pdf_rel_path = ""

    # Try to extract PDF path using regex
    # Match patterns like: sources: ["EMT_Doc/xxx/file.pdf"]
    match = re.search(r'sources:\s*\["([^"]*EMT_Doc[^"]*)"\]', content)
    if match:
        pdf_rel_path = match.group(1)
    else:
        # Fallback: find EMT_Doc in content
        for line in content.split('\n'):
            if 'EMT_Doc/' in line and '.pdf' in line:
                match = re.search(r'EMT_Doc/[^"\]]+\.pdf', line, re.IGNORECASE)
                if match:
                    pdf_rel_path = match.group()
                    break

    if not pdf_rel_path:
        print(f"  [{count}/{total}] {filename[:50]}...  SKIP (no PDF path)")
        continue

    # Construct absolute PDF path (EMT_Doc is in current directory)
    pdf_paths_to_try = [
        f"/home/chenying/researches/EMT_LLM_Wiki/{pdf_rel_path}",
    ]

    pdf_path = None
    for p in pdf_paths_to_try:
        if os.path.exists(p):
            pdf_path = p
            break

    if not pdf_path:
        print(f"  [{count}/{total}] {filename[:50]}...  SKIP (PDF not found: {pdf_rel_path})")
        checkpoint['failed'].append(filename)
        save_checkpoint()
        continue

    # Try MinerU
    print(f"  [{count}/{total}] {filename[:50]}... ", end='', flush=True)
    text, success = extract_with_mineru(pdf_path)

    if success:
        print(f"MinerU: {len(text)} chars")
        checkpoint['done'].append(filename)
    else:
        print(f"MinerU FAILED")
        checkpoint['failed'].append(filename)

    # Save checkpoint every 5 files
    if count % 5 == 0:
        save_checkpoint()
        print(f"  Checkpoint saved: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

save_checkpoint()
print(f"\n=== Final Summary ===")
print(f"Done: {len(checkpoint['done'])}")
print(f"Failed: {len(checkpoint['failed'])}")
if checkpoint['failed']:
    print(f"\nFailed files:")
    for f in checkpoint['failed'][:20]:
        print(f"  - {f}")
