#!/usr/bin/env python3
"""
Retry MinerU extraction for papers that previously used pdftotext fallback.

Strategy:
1. Identify papers with low content quality (likely pdftotext fallback):
   - No LaTeX formulas ($$, \mathbf, \left, \right)
   - Short extracted content
   - Simple text patterns in 核心贡献 section
2. Re-extract PDF using MinerU API
3. Re-analyze with LLM if new content is richer
"""

import os
import re
import json
import time
import requests
from pathlib import Path

MINERU_API = "http://localhost:8000"
WIKI_SOURCES = Path("wiki/sources")
CHECKPOINT = Path(".retry_pdftotext.json")

# Load checkpoint
checkpoint = {"done": [], "failed": [], "skipped": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed, {len(checkpoint['skipped'])} skipped")

done_set = set(checkpoint.get('done', []))

def is_likely_pdftotext(filepath: Path) -> bool:
    """Check if a source file likely used pdftotext (no LaTeX formulas, simple text)"""
    content = filepath.read_text(encoding='utf-8')

    # Check for LaTeX markers (MinerU produces these)
    latex_markers = ['$$', '\\mathbf', '\\left', '\\right', '\\frac', '\\sum', '\\prod', '\\alpha', '\\beta', '\\gamma', '\\Delta', '\\delta']
    has_latex = any(marker in content for marker in latex_markers)

    # If no LaTeX at all, likely pdftotext
    if not has_latex:
        return True

    return False

def extract_with_mineru(pdf_path: str) -> tuple[str, bool]:
    """Extract text using MinerU API. Returns (text, success)"""
    try:
        with open(pdf_path, 'rb') as f:
            files = {'files': (os.path.basename(pdf_path), f, 'application/pdf')}
            data = {
                'backend': 'pipeline',
                'return_md': 'true',
                'formula_enable': 'true',
                'table_enable': 'true'
            }
            response = requests.post(f"{MINERU_API}/tasks", files=files, data=data, timeout=60)

        if response.status_code != 202:
            print(f"Submit failed: {response.status_code}")
            return "", False

        task_id = response.json().get('task_id')
        if not task_id:
            return "", False

        print(f"Task {task_id[:8]} submitted, polling...", end='', flush=True)

        # Poll for result (max 5 min)
        for i in range(60):
            time.sleep(5)
            result = requests.get(f"{MINERU_API}/tasks/{task_id}/result", timeout=30)
            if result.status_code == 200:
                data = result.json()
                status = data.get('status', 'unknown')
                if status == 'completed':
                    markdown = data.get('markdown', '')
                    if markdown:
                        print(f" completed! {len(markdown)} chars")
                        return markdown[:15000], True
                    else:
                        print(" completed but empty")
                        return "", False
                elif status == 'failed':
                    print(f" failed: {data.get('message', 'unknown error')}")
                    return "", False
                else:
                    if i % 6 == 0:  # Print every 30 seconds
                        print(f"{status}({i*5}s)...", end='', flush=True)

        print(f" timeout after 5 min")
        return "", False  # Timeout
    except Exception as e:
        print(f" error: {e}")
        return "", False

def save_checkpoint():
    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)

def get_pdf_path(filepath: Path) -> str:
    """Extract PDF path from source file"""
    content = filepath.read_text(encoding='utf-8')

    # Try to extract PDF path using regex
    match = re.search(r'sources:\s*\["([^"]*EMT_Doc[^"]*)"\]', content)
    if match:
        pdf_rel_path = match.group(1)
        # Construct absolute path
        pdf_path = f"/home/chenying/researches/EMT_LLM_Wiki/{pdf_rel_path}"
        if os.path.exists(pdf_path):
            return pdf_path

    return None

# Get all source files that are likely pdftotext
print("Scanning for pdftotext fallback papers...")
pdftotext_papers = []

for src_file in WIKI_SOURCES.glob("*.md"):
    if src_file.name in done_set:
        continue  # Already retried

    if is_likely_pdftotext(src_file):
        pdf_path = get_pdf_path(src_file)
        if pdf_path:
            pdftotext_papers.append((src_file, pdf_path))
        else:
            print(f"  SKIP (PDF not found): {src_file.name[:50]}")
            checkpoint['skipped'].append(src_file.name)

print(f"\nFound {len(pdftotext_papers)} pdftotext fallback papers with PDFs available")
print(f"To retry: {len(pdftotext_papers)} papers")

# Process papers
total = len(pdftotext_papers)
count = len(checkpoint['done'])

for idx, (src_file, pdf_path) in enumerate(pdftotext_papers):
    count += 1
    filename = src_file.name

    print(f"[{count}/{total}] {filename[:50]}... ", end='', flush=True)

    # Try MinerU
    text, success = extract_with_mineru(pdf_path)

    if success:
        print(f"  -> MinerU success! {len(text)} chars")
        checkpoint['done'].append(filename)
    else:
        print(f"  -> MinerU FAILED")
        checkpoint['failed'].append(filename)

    # Save checkpoint every 3 files
    if count % 3 == 0:
        save_checkpoint()
        print(f"  Checkpoint saved: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

save_checkpoint()

print(f"\n=== Final Summary ===")
print(f"Done: {len(checkpoint['done'])}")
print(f"Failed: {len(checkpoint['failed'])}")
print(f"Skipped: {len(checkpoint['skipped'])}")

if checkpoint['failed']:
    print(f"\nFailed files (can retry again):")
    for f in checkpoint['failed'][:20]:
        print(f"  - {f}")
