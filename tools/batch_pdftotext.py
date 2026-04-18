#!/usr/bin/env python3
"""
Fast batch extract text from all PDFs using pdftotext.

Saves extracted text to extracted_text/pdftotext/ directory.
Much faster than MinerU (5 seconds vs 10+ minutes per PDF).
"""

import os
import re
import json
import subprocess
import time
from pathlib import Path

WIKI_SOURCES = Path("wiki/sources")
OUTPUT_DIR = Path("extracted_text/pdftotext")
CHECKPOINT = Path(".pdftotext_texts.json")

# Load checkpoint
checkpoint = {"done": [], "failed": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))


def extract_with_pdftotext(pdf_path: str, timeout_sec: int = 30) -> tuple[str, bool]:
    """Extract text using pdftotext. Returns (text, success)"""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        text = result.stdout
        if text and len(text.strip()) > 100:
            return text[:20000], True
        return "", False
    except subprocess.TimeoutExpired:
        print(f"timeout after {timeout_sec}s")
        return "", False
    except Exception as e:
        print(f"error: {e}")
        return "", False


def get_pdf_path(filepath: Path) -> str:
    """Extract PDF path from source file"""
    content = filepath.read_text(encoding='utf-8')
    match = re.search(r'sources:\s*\["([^"]*EMT_Doc[^"]*)"\]', content)
    if match:
        pdf_rel_path = match.group(1)
        pdf_path = f"/home/chenying/researches/EMT_LLM_Wiki/{pdf_rel_path}"
        if os.path.exists(pdf_path):
            return pdf_path
    return None


def save_checkpoint():
    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)


# Main
print("=" * 60)
print("Fast batch extract text from all PDFs using pdftotext")
print("=" * 60)

# Create output directory
OUTPUT_DIR.mkdir(exist_ok=True)

# Get all source files
source_files = sorted([f for f in WIKI_SOURCES.glob("*.md") if f.name not in done_set])
total = len(source_files) + len(done_set)
print(f"Total files: {total}, Remaining: {len(source_files)}")

if not source_files:
    print("No files to process!")
    exit(0)

# Process files
count = len(checkpoint['done'])
start_time = time.time()

for src_file in source_files:
    count += 1
    filename = src_file.name

    # Find corresponding PDF
    pdf_path = get_pdf_path(src_file)
    if not pdf_path:
        print(f"  [{count}/{total}] {filename[:50]}... SKIP (PDF not found)")
        checkpoint['failed'].append(filename)
        save_checkpoint()
        continue

    # Extract with pdftotext
    print(f"  [{count}/{total}] {filename[:50]}... ", end='', flush=True)
    text, success = extract_with_pdftotext(pdf_path, timeout_sec=30)

    if success:
        # Save text file
        txt_path = OUTPUT_DIR / f"{filename.replace('.md', '')}.txt"
        txt_path.write_text(text, encoding='utf-8')

        print(f"✅ Saved: {len(text)} chars")
        checkpoint['done'].append(filename)
    else:
        print(f"pdftotext FAILED")
        checkpoint['failed'].append(filename)

    # Save checkpoint every 10 files
    if count % 10 == 0:
        save_checkpoint()
        elapsed = (time.time() - start_time) / 60
        rate = elapsed / count if count > 0 else 0
        print(f"  Checkpoint saved: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed ({elapsed:.1f}m, {rate:.2f}s/file)")

save_checkpoint()

elapsed = (time.time() - start_time) / 60
print(f"\n{'=' * 60}")
print(f"Completed in {elapsed:.1f} minutes")
print(f"Done: {len(checkpoint['done'])}")
print(f"Failed: {len(checkpoint['failed'])}")
print(f"Output directory: {OUTPUT_DIR.absolute()}")
print(f"{'=' * 60}")

if checkpoint['failed']:
    print(f"\nFailed files (can retry again):")
    for f in checkpoint['failed'][:20]:
        print(f"  - {f}")
