#!/usr/bin/env python3
"""
Extract metadata from all EMT research PDFs using PyMuPDF.
Outputs a structured metadata.json for wiki bootstrap.
"""

import json
import os
import re
import fitz  # PyMuPDF

EMT_DOC_ROOT = "/home/chenying/researches/EMT_LLM_Wiki/EMT_Doc"
OUTPUT_PATH = "/home/chenying/researches/EMT_LLM_Wiki/wiki/sources/metadata.json"


def extract_pdf_metadata(pdf_path: str) -> dict:
    """Extract metadata and first-page text from a PDF."""
    doc = fitz.open(pdf_path)
    meta = doc.metadata
    page0 = doc[0].get_text() if doc.page_count > 0 else ""

    # Extract abstract (first 50 lines after title)
    abstract = ""
    lines = page0.split("\n")
    in_abstract = False
    abstract_lines = []
    for line in lines:
        stripped = line.strip()
        if re.search(r"(?i)^abstract", stripped):
            in_abstract = True
            # Remove "Abstract -" prefix if present
            content = re.sub(r"(?i)^abstract[\s:\-]*", "", stripped)
            if content:
                abstract_lines.append(content)
            continue
        if in_abstract:
            if stripped == "" or len(abstract_lines) > 15:
                break
            abstract_lines.append(stripped)
    abstract = " ".join(abstract_lines).strip()

    # If no abstract found, use first 300 chars of body text
    if not abstract:
        # Skip header-like lines (journal names, dates, etc.)
        body_lines = []
        for line in lines:
            stripped = line.strip()
            if len(stripped) > 50 and not re.match(r"(?i)^(IEEE|Received|Published|Digital|Color|Index|Vol|NO|doi|10\.|ISSN|ISBN)", stripped):
                body_lines.append(stripped)
                if len(body_lines) >= 5:
                    break
        abstract = " ".join(body_lines).strip()[:500]

    page_count = doc.page_count

    # Parse year from CreationDate or filename
    year = None
    creation_date = meta.get("creationDate", "")
    if creation_date:
        match = re.search(r"(\d{4})", creation_date)
        if match:
            year = int(match.group(1))

    if year is None:
        # Try to find year in filename (e.g., "Cao 等 - 2025 - ...")
        fname = os.path.basename(pdf_path)
        match = re.search(r"-\s*(\d{4})\s*-", fname)
        if match:
            year = int(match.group(1))

    doc.close()

    return {
        "title": meta.get("title", "").strip(),
        "authors": meta.get("author", "").strip(),
        "subject": meta.get("subject", "").strip(),
        "year": year,
        "pages": page_count,
        "abstract": abstract[:1000],  # Limit abstract length
        "file_path": pdf_path,
        "relative_path": os.path.relpath(pdf_path, EMT_DOC_ROOT),
        "folder": os.path.basename(os.path.dirname(pdf_path)),
    }


def main():
    """Walk EMT_Doc and extract metadata from all PDFs."""
    all_metadata = []
    error_files = []

    for root, dirs, files in os.walk(EMT_DOC_ROOT):
        for fname in sorted(files):
            if not fname.lower().endswith(".pdf"):
                continue
            pdf_path = os.path.join(root, fname)
            print(f"  Processing: {os.path.relpath(pdf_path, EMT_DOC_ROOT)}")
            try:
                meta = extract_pdf_metadata(pdf_path)
                all_metadata.append(meta)
            except Exception as e:
                error_files.append({"path": pdf_path, "error": str(e)})
                print(f"    ERROR: {e}")

    # Sort by relative path
    all_metadata.sort(key=lambda x: x["relative_path"])

    # Write output
    output = {
        "total_papers": len(all_metadata),
        "folders": sorted(set(m["folder"] for m in all_metadata)),
        "years": sorted(set(m["year"] for m in all_metadata if m["year"])),
        "papers": all_metadata,
        "errors": error_files,
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Extracted metadata for {len(all_metadata)} papers.")
    print(f"  Errors: {len(error_files)}")
    print(f"  Output: {OUTPUT_PATH}")
    if output["years"]:
        print(f"  Year range: {min(output['years'])}-{max(output['years'])}")
    print(f"  Folders: {', '.join(output['folders'])}")


if __name__ == "__main__":
    main()
