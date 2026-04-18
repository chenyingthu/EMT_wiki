#!/home/chenying/anaconda3/bin/python3
"""
High-quality batch PDF to Markdown conversion using pdftotext + LLM.

Strategy:
1. Extract raw text using pdftotext (fast, ~0.1s per PDF)
2. Use LLM to convert to clean Markdown with LaTeX formulas
3. Save to extracted_text/markdown_enhanced/ directory

Output includes:
- Clean section headings
- LaTeX math formulas ($...$ and $$...$$)
- Proper table formatting
- Removed page breaks/headers/footers
- Preserved references and citations
"""

import os
import re
import json
import subprocess
import time
from pathlib import Path

import anthropic

WIKI_SOURCES = Path("wiki/sources")
OUTPUT_DIR = Path("extracted_text/markdown_enhanced")
CHECKPOINT = Path(".markdown_enhanced.json")

# LLM client (uses default auth from environment)
client = anthropic.Anthropic()

# Load checkpoint
checkpoint = {"done": [], "failed": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))


def extract_with_pdftotext(pdf_path: str, timeout_sec: int = 30) -> str:
    """Extract raw text using pdftotext."""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        return result.stdout[:30000]  # Limit input size
    except Exception as e:
        return ""


def convert_to_markdown(raw_text: str) -> str:
    """Convert raw PDF text to clean Markdown with LaTeX using LLM."""
    prompt = f"""Convert the following academic paper text into clean Markdown format.

Rules:
1. Use ## and ### for section headings
2. Convert all math equations to LaTeX ($...$ for inline, $$...$$ for display)
3. Remove page breaks, running headers, footers, page numbers
4. Preserve references [1], [2], etc.
5. Format tables using Markdown table syntax
6. Keep author affiliations and abstract intact
7. Preserve all technical content - do NOT summarize

Return ONLY the Markdown content, no other text.

Text to convert:
{raw_text[:8000]}"""

    try:
        response = client.messages.create(
            model="qwen3.6-plus",
            max_tokens=8000,
            temperature=0.1,
            messages=[{"role": "user", "content": prompt}]
        )

        for block in response.content:
            if hasattr(block, 'text') and block.text:
                return block.text.strip()
        return ""
    except Exception as e:
        return ""


def get_pdf_path(filepath: Path) -> str:
    """Extract PDF path from source file."""
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
print("High-quality PDF to Markdown conversion (pdftotext + LLM)")
print("=" * 60)

OUTPUT_DIR.mkdir(exist_ok=True)

source_files = sorted([f for f in WIKI_SOURCES.glob("*.md") if f.name not in done_set])
total = len(source_files) + len(done_set)
print(f"Total files: {total}, Remaining: {len(source_files)}")

if not source_files:
    print("No files to process!")
    exit(0)

count = len(checkpoint['done'])
start_time = time.time()

for src_file in source_files:
    count += 1
    filename = src_file.name

    pdf_path = get_pdf_path(src_file)
    if not pdf_path:
        print(f"  [{count}/{total}] {filename[:50]}... SKIP (PDF not found)")
        checkpoint['failed'].append(filename)
        save_checkpoint()
        continue

    print(f"  [{count}/{total}] {filename[:50]}... ", end='', flush=True)

    # Step 1: Extract with pdftotext
    raw_text = extract_with_pdftotext(pdf_path)
    if not raw_text:
        print("pdftotext FAILED")
        checkpoint['failed'].append(filename)
        save_checkpoint()
        continue

    print(f"pdftotext: {len(raw_text)} chars, ", end='', flush=True)

    # Step 2: Convert to Markdown with LLM
    markdown = convert_to_markdown(raw_text)
    if markdown:
        # Save markdown file
        md_path = OUTPUT_DIR / f"{filename}"
        md_path.write_text(markdown, encoding='utf-8')

        print(f"✅ LLM: {len(markdown)} chars")
        checkpoint['done'].append(filename)
    else:
        print(f"LLM FAILED")
        checkpoint['failed'].append(filename)

    # Save checkpoint every 5 files
    if count % 5 == 0:
        save_checkpoint()
        elapsed = (time.time() - start_time) / 60
        print(f"  Checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed ({elapsed:.1f}m)")

save_checkpoint()

elapsed = (time.time() - start_time) / 60
print(f"\n{'=' * 60}")
print(f"Completed in {elapsed:.1f} minutes")
print(f"Done: {len(checkpoint['done'])}")
print(f"Failed: {len(checkpoint['failed'])}")
print(f"Output: {OUTPUT_DIR.absolute()}")
print(f"{'=' * 60}")
