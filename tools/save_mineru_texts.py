#!/usr/bin/env python3
"""
Batch extract and save MinerU text from all PDFs.

Saves full MinerU-extracted text (with LaTeX formulas, tables, images) to extracted_text/ directory.
These texts can be used for future learning and mining.
"""

import os
import re
import json
import time
import requests
from pathlib import Path

MINERU_API = os.environ.get("MINERU_API_URL", "http://localhost:8000")
WIKI_SOURCES = Path("wiki/sources")
OUTPUT_DIR = Path("extracted_text")
CHECKPOINT = Path(".mineru_texts.json")

# Load checkpoint
checkpoint = {"done": [], "failed": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))

def extract_with_mineru(pdf_path: str, timeout_min: int = 15) -> tuple[str, bool]:
    """Extract text using MinerU API. Returns (markdown, success)"""
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

        print(f"Task {task_id[:8]} submitted", end='', flush=True)

        # Poll for result (max timeout_min minutes)
        max_polls = timeout_min * 12  # 5 seconds per poll
        for i in range(max_polls):
            time.sleep(5)
            result = requests.get(f"{MINERU_API}/tasks/{task_id}/result", timeout=30)
            if result.status_code == 200:
                data = result.json()
                # Check for new API format: {'backend', 'version', 'results'}
                if 'results' in data:
                    # New format: extract md_content from results
                    results = data.get('results', {})
                    for filename, content in results.items():
                        if isinstance(content, dict) and 'md_content' in content:
                            markdown = content.get('md_content', '')
                            if markdown:
                                print(f" done! {len(markdown)} chars")
                                return markdown, True
                    print(" done but empty")
                    return "", False
                # Legacy format: {'status', 'markdown'}
                status = data.get('status', 'unknown')
                if status == 'completed':
                    markdown = data.get('markdown', '')
                    if markdown:
                        print(f" done! {len(markdown)} chars")
                        return markdown, True
                    else:
                        print(" done but empty")
                        return "", False
                elif status == 'failed':
                    print(f" failed: {data.get('message', 'unknown')}")
                    return "", False
                else:
                    if i % 12 == 0:  # Print every minute
                        print(f" {status}({i//12+1}m)...", end='', flush=True)

        print(f" timeout after {timeout_min} min")
        return "", False
    except Exception as e:
        print(f" error: {e}")
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
print("Batch extract and save MinerU texts from all PDFs")
print("=" * 60)

# Create output directory
OUTPUT_DIR.mkdir(exist_ok=True)
(OUTPUT_DIR / "markdown").mkdir(exist_ok=True)
(OUTPUT_DIR / "json").mkdir(exist_ok=True)

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

    # Extract with MinerU
    print(f"  [{count}/{total}] {filename[:50]}... ", end='', flush=True)
    markdown, success = extract_with_mineru(pdf_path, timeout_min=12)

    if success:
        # Save markdown file
        md_filename = filename.replace('.md', '.md')
        md_path = OUTPUT_DIR / "markdown" / md_filename
        md_path.write_text(markdown, encoding='utf-8')

        # Save metadata JSON
        metadata = {
            "source_file": filename,
            "pdf_path": pdf_path,
            "extracted_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "char_count": len(markdown),
            "mineru_api": MINERU_API
        }
        json_path = OUTPUT_DIR / "json" / filename.replace('.md', '.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        print(f"✅ Saved: {len(markdown)} chars")
        checkpoint['done'].append(filename)
    else:
        print(f"MinerU FAILED")
        checkpoint['failed'].append(filename)

    # Save checkpoint every 5 files
    if count % 5 == 0:
        save_checkpoint()
        elapsed = (time.time() - start_time) / 60
        print(f"  Checkpoint saved: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed ({elapsed:.1f}m elapsed)")

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
