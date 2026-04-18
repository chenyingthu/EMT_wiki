#!/usr/bin/env python3
"""
Batch extract and save MinerU text from all PDFs using local CLI.

Uses mineru CLI directly instead of API server.
"""

import os
import re
import json
import subprocess
import time
import shutil
from pathlib import Path

WIKI_SOURCES = Path("wiki/sources")
OUTPUT_DIR = Path("extracted_text")
CHECKPOINT = Path(".mineru_cli_texts.json")

# Load checkpoint
checkpoint = {"done": [], "failed": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))


def extract_with_mineru_cli(pdf_path: str, timeout_min: int = 10) -> tuple[str, bool]:
    """Extract text using mineru CLI. Returns (markdown, success)"""
    try:
        # Create temp output directory
        temp_output = Path("/tmp/mineru_extract")
        temp_output.mkdir(exist_ok=True)

        # Run mineru CLI
        cmd = [
            "mineru",
            "--path", pdf_path,
            "--output", str(temp_output),
            "--backend", "hybrid-auto-engine"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_min * 60
        )

        if result.returncode != 0:
            print(f"CLI error: {result.stderr[:200]}")
            return "", False

        # Find output markdown file
        md_files = list(temp_output.glob("*.md"))
        if not md_files:
            print("No output file")
            return "", False

        # Read markdown content
        markdown = md_files[0].read_text(encoding='utf-8')

        # Cleanup temp files
        for f in temp_output.glob("*"):
            f.unlink()
        temp_output.rmdir()

        return markdown[:20000], True

    except subprocess.TimeoutExpired:
        print(f"timeout after {timeout_min} min")
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
print("Batch extract and save MinerU texts from all PDFs (CLI mode)")
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

    # Extract with mineru CLI
    print(f"  [{count}/{total}] {filename[:50]}... ", end='', flush=True)
    markdown, success = extract_with_mineru_cli(pdf_path, timeout_min=8)

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
            "method": "mineru-cli"
        }
        json_path = OUTPUT_DIR / "json" / filename.replace('.md', '.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        print(f"✅ Saved: {len(markdown)} chars")
        checkpoint['done'].append(filename)
    else:
        print(f"MinerU CLI FAILED")
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
