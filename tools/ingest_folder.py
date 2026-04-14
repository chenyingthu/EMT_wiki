#!/usr/bin/env python3
"""
Bootstrap: Generate source summary pages for a batch of PDFs.
Usage: python tools/ingest_folder.py <folder_number>
Example: python tools/ingest_folder.py 01
"""

import json
import os
import re
import sys
import fitz  # PyMuPDF for PDF title extraction

WIKI_ROOT = "/home/chenying/researches/EMT_LLM_Wiki"
METADATA_PATH = os.path.join(WIKI_ROOT, "wiki/sources/metadata.json")
SOURCES_DIR = os.path.join(WIKI_ROOT, "wiki/sources")
INDEX_PATH = os.path.join(WIKI_ROOT, "wiki/index.md")
LOG_PATH = os.path.join(WIKI_ROOT, "wiki/log.md")


def slugify(title: str) -> str:
    """Convert title to kebab-case filename."""
    # Remove special chars, lowercase, replace spaces/special with hyphens
    s = title.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")[:80]


def is_bad_title(title: str) -> bool:
    """Check if title is a DOI, PII, or other non-meaningful string."""
    if not title:
        return True
    # DOI, PII, IEEE paper IDs, DOI filenames, journal abbreviations
    if re.match(r"^(doi|10\.|pii|s0378|s0142|tpwrs|tpwrd|tste|pesmg|pesgm|j\.epsr|j\.ijepes|ACCESS)", title, re.IGNORECASE):
        return True
    # DOI-style filename (e.g. "TPWRD.2017.2690145.pdf" without extension)
    if re.match(r"^(tpwrd|tpwrs|pesmg|pesgm|ijepes|epsr|TSTE)\d+", title, re.IGNORECASE):
        return True
    # NONE, empty-looking
    if title.upper() in ("NONE", "UNTITLED", "NULL"):
        return True
    # All symbols / garbled
    cleaned = re.sub(r"[\s\-\(\):,.;/]", "", title)
    if cleaned and all(not c.isalnum() for c in cleaned):
        return True
    # Starts with non-alphanumeric
    if cleaned and not cleaned[0].isalnum():
        return True
    # IEEE copyright line (e.g., "0885-8977 (c) 2015 IEEE")
    if re.match(r'^0885-', title):
        return True
    # IEEE submission metadata (e.g., "Received June 8, 2020, accepted...")
    if title.startswith('Received ') and 'date of publication' in title.lower():
        return True
    # Chinese journal names
    if re.match(r'^[\u4e00-\u9fff\s　]+$', title) and len(title) < 20:
        return True
    return False


def extract_title_from_filename(rel_path: str) -> str:
    """Extract a human-readable title from the file path."""
    fname = os.path.basename(rel_path)
    # Remove extension
    name = re.sub(r"\.\w+$", "", fname)
    # Pattern: "Author 等 - YEAR - Title" → extract Title
    match = re.match(r"^[^-]*?[-–]\s*\d{4}\s*[-–]\s*(.+)$", name)
    if match:
        return match.group(1).strip()
    # Fallback: use full name without extension
    return name.strip()


def extract_title_from_pdf(pdf_path: str) -> str:
    """Try to extract the real title from the first page of a PDF."""
    try:
        doc = fitz.open(pdf_path)
        text = doc[0].get_text() if doc.page_count > 0 else ""
        doc.close()
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        # Skip journal headers and boilerplate
        skip = [
            "This article has been accepted", "Citation information", "IEEE TRANSACTIONS",
            "Electric Power Systems Research", "Contents lists available", "Printed in Great Britain",
            "journal homepage", "PII:", "doi:", "10.1109", "Electrical Power & Energy Systems",
            "0142-0615", "Crown Copyright", "All rights reserved", "Personal use is permitted",
            "Abstract", "Abstract–", "Abstract—", "Digital Object Identifier",
        ]
        filtered = [l for l in lines if not any(l.startswith(s) for s in skip) and len(l) > 20]
        if filtered:
            # First meaningful line is often the title
            title = filtered[0].strip()
            # Validate it's not another header
            if re.match(r"^(doi|pii|10\.|vol\.|no\.)", title, re.IGNORECASE):
                return ""
            return title[:120]
    except Exception:
        pass
    return ""


def build_source_page(paper: dict) -> str:
    """Generate a markdown source summary page."""
    title = paper.get("title", "").strip()
    if is_bad_title(title):
        # Try PDF first page before filename
        pdf_path = paper.get("file_path", "")
        if pdf_path and os.path.exists(pdf_path):
            pdf_title = extract_title_from_pdf(pdf_path)
            if pdf_title and not is_bad_title(pdf_title):
                title = pdf_title
        if not title or is_bad_title(title):
            title = extract_title_from_filename(paper.get("relative_path", ""))
    if not title or is_bad_title(title):
        title = "未知论文"

    authors_str = paper.get("authors", "").strip()
    year = paper.get("year", "未知")
    journal = paper.get("subject", "").strip()
    abstract = paper.get("abstract", "").strip()[:800]
    rel_path = paper.get("relative_path", "")
    file_path = paper.get("file_path", "")

    # Generate slug for filename
    slug = slugify(title)
    if not slug:
        slug = "unknown-" + os.path.basename(rel_path).replace(" ", "-")[:40]

    # Simple keyword tagging from title
    tags = []
    title_lower = title.lower()
    tag_keywords = {
        "adc": ["adc", "associated discrete circuit"],
        "fixed-admittance": ["fixed-admittance", "固定导纳"],
        "mmc": ["mmc", "modular multilevel"],
        "vsc": ["vsc", "voltage source converter", "电压源换流器"],
        "lcc": ["lcc", "line-commutated"],
        "real-time": ["real-time", "实时"],
        "fpga": ["fpga"],
        "frequency-dependent": ["frequency dependent", "频变"],
        "network-equivalent": ["network equivalent", "网络等值"],
        "cosimulation": ["cosimulation", "co-simulation", "联合仿真"],
        "average-value": ["average-value", "平均值"],
        "state-space": ["state-space", "状态空间"],
        "model-order-reduction": ["order reduction", "降阶"],
        "harmonic": ["harmonic", "谐波"],
        "transformer": ["transformer", "变压器"],
        "transmission-line": ["transmission line", "输电线路"],
        "renewable": ["renewable", "新能源", "风电", "光伏"],
        "ibg": ["inverter-based", "ibg"],
        "dynamic-phasor": ["dynamic phasor", "动态相量"],
        "pmsm": ["pmsm", "永磁同步"],
        "emtp": ["emtp"],
        "pscad": ["pscad"],
        "rtds": ["rtds"],
    }
    for tag, keywords in tag_keywords.items():
        if any(kw in title_lower for kw in keywords):
            tags.append(tag)
    if not tags:
        tags = ["emt"]

    # Authors list
    authors = []
    if authors_str:
        # Split by common separators
        authors = [a.strip() for a in re.split(r"[,;、]", authors_str) if a.strip()]
        if len(authors) == 1 and " " in authors[0]:
            # Might be single string with spaces
            parts = authors[0].split()
            if len(parts) > 2:
                authors = parts

    authors_yaml = authors if authors else ["未知"]
    authors_display = ", ".join(authors[:3])
    if len(authors) > 3:
        authors_display += " 等"

    page = f"""---
title: "{title}"
type: source
authors: {authors_yaml}
year: {year}
journal: "{journal}"
tags: {tags}
created: "2026-04-13"
sources: ["EMT_Doc/{rel_path}"]
---

# {title}

**作者**: {authors_display}
**年份**: {year}
**来源**: `{rel_path}`

## 摘要

{abstract if abstract else "*（摘要未提取到）*"}

## 核心贡献

*（待 LLM 分析补充）*

## 使用的方法

*（待分析）*

## 涉及的模型

*（待分析）*

## 相关主题

*（待分析）*

## 主要发现

*（待分析）*
"""
    return page, slug


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/ingest_folder.py <folder_number>")
        print("Example: python tools/ingest_folder.py 01")
        sys.exit(1)

    folder_num = sys.argv[1]

    # Load metadata
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter papers for this folder
    folder_papers = [p for p in data["papers"] if p["folder"] == folder_num]
    if not folder_papers:
        print(f"No papers found for folder {folder_num}")
        sys.exit(1)

    print(f"Ingesting folder {folder_num}: {len(folder_papers)} papers")

    created_pages = []
    for paper in folder_papers:
        page_content, slug = build_source_page(paper)
        out_path = os.path.join(SOURCES_DIR, f"{slug}.md")

        # Avoid overwriting existing files
        if os.path.exists(out_path):
            out_path = os.path.join(SOURCES_DIR, f"{slug}-{folder_num}.md")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_content)

        title = paper.get("title", "")[:60]
        if not title:
            title = paper.get("relative_path", "")[:60]
        print(f"  Created: {os.path.basename(out_path)} | {title}")
        created_pages.append(os.path.basename(out_path))

    # Update log
    log_entry = f"""
## [2026-04-13] ingest | 文件夹 {folder_num} 批量摄入
- 来源: EMT_Doc/{folder_num}/ ({len(folder_papers)} 篇论文)
- 创建来源页: {len(created_pages)}
  {', '.join(created_pages[:10])}{'...' if len(created_pages) > 10 else ''}
- 主题/方法/模型页: 待分析后创建
"""
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"\nDone! Created {len(created_pages)} source pages.")
    print(f"Log updated in {LOG_PATH}")


if __name__ == "__main__":
    main()
