#!/usr/bin/env python3
"""Synchronize source-page metadata from metadata.json and PDF filenames."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"
METADATA_PATH = SOURCE_DIR / "metadata.json"

BAD_AUTHOR_RE = re.compile(r"^\s*$|未知|CNKI|IEEE|Periodicals|作者|\[\]|''|\"\"", re.IGNORECASE)
BAD_TITLE_RE = re.compile(
    r"^\s*$|untitled|Published in|^第\d+\s*卷|标题|\.pdf$|^\d+&\d+/|^32/j\.epsr",
    re.IGNORECASE,
)


def load_metadata() -> dict[str, dict]:
    data = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    by_source = {}
    for paper in data.get("papers", []):
        rel = paper.get("relative_path") or ""
        if rel:
            by_source[f"EMT_Doc/{rel}"] = paper
            by_source[Path(rel).name] = paper
    return by_source


def frontmatter(content: str) -> str:
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL | re.MULTILINE)
    return match.group(1) if match else ""


def frontmatter_value(content: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter(content), re.MULTILINE)
    return match.group(1).strip().strip('"') if match else ""


def first_source(content: str) -> str:
    match = re.search(r'sources:\s*\["([^"]+)"\]', content)
    return match.group(1) if match else ""


def is_inactive_source(content: str) -> bool:
    return "type: duplicate-source" in content or "type: out-of-scope-source" in content


def is_bad_author(value: str) -> bool:
    return bool(BAD_AUTHOR_RE.search(value or ""))


def is_bad_title(value: str) -> bool:
    return bool(BAD_TITLE_RE.search(value or ""))


def split_authors(value: str) -> list[str]:
    value = value.strip()
    if not value or is_bad_author(value):
        return []
    authors = [item.strip() for item in re.split(r"[,;、]", value) if item.strip()]
    return authors[:12]


def authors_from_filename(source: str) -> list[str]:
    name = Path(source).name
    stem = re.sub(r"\.pdf(?:\.pdf)?$", "", name, flags=re.IGNORECASE)
    match = re.match(r"(.+?)\s*[-–]\s*(?:19|20)\d{2}\s*[-–]\s*.+", stem)
    if not match:
        return []
    prefix = match.group(1).strip()
    if is_bad_author(prefix) or len(prefix) > 80:
        return []
    return [prefix]


def title_from_filename(source: str) -> str:
    name = Path(source).name
    stem = re.sub(r"\.pdf(?:\.pdf)?$", "", name, flags=re.IGNORECASE)
    match = re.match(r".+?\s*[-–]\s*(?:19|20)\d{2}\s*[-–]\s*(.+)", stem)
    title = match.group(1).strip() if match else stem.strip()
    return title if not is_bad_title(title) else ""


def yaml_list(values: list[str]) -> str:
    escaped = [value.replace("\\", "\\\\").replace("'", "\\'") for value in values]
    return "[" + ", ".join(f"'{value}'" for value in escaped) + "]"


def replace_frontmatter_value(content: str, key: str, rendered_value: str) -> str:
    if re.search(rf"^{re.escape(key)}:", frontmatter(content), re.MULTILINE):
        return re.sub(rf"^{re.escape(key)}:\s*.*$", f"{key}: {rendered_value}", content, count=1, flags=re.MULTILINE)
    return content


def replace_section(content: str, section: str, replacement: str) -> str:
    pattern = rf"(^## {re.escape(section)}\s*\n)(.*?)(?=^## |\Z)"
    return re.sub(pattern, rf"\1\n{replacement.strip()}\n\n", content, count=1, flags=re.DOTALL | re.MULTILINE)


def display_authors(authors: list[str]) -> str:
    if not authors:
        return ""
    shown = "; ".join(authors[:5])
    if len(authors) > 5:
        shown += " 等"
    return shown


def sync_page(content: str, metadata: dict | None = None) -> str:
    if is_inactive_source(content):
        return content
    source = first_source(content)
    metadata = metadata or {}

    title = frontmatter_value(content, "title")
    metadata_title = (metadata.get("title") or "").strip()
    filename_title = title_from_filename(source)
    new_title = title
    if is_bad_title(title):
        if metadata_title and not is_bad_title(metadata_title):
            new_title = metadata_title
        elif filename_title:
            new_title = filename_title

    authors_raw = frontmatter_value(content, "authors")
    metadata_authors = split_authors(metadata.get("authors") or "")
    filename_authors = authors_from_filename(source)
    new_authors = metadata_authors or filename_authors

    journal = frontmatter_value(content, "journal")
    metadata_journal = (metadata.get("subject") or "").strip()
    year = frontmatter_value(content, "year")
    metadata_year = metadata.get("year")
    abstract = (metadata.get("abstract") or "").strip()

    updated = content
    if new_title != title:
        escaped_title = new_title.replace('"', '\\"')
        updated = replace_frontmatter_value(updated, "title", f'"{escaped_title}"')
        updated = re.sub(r"^# .+$", f"# {new_title}", updated, count=1, flags=re.MULTILINE)
    if is_bad_author(authors_raw) and new_authors:
        updated = replace_frontmatter_value(updated, "authors", yaml_list(new_authors))
        updated = re.sub(r"^\*\*作者\*\*:.*$", f"**作者**: {display_authors(new_authors)}", updated, count=1, flags=re.MULTILINE)
    if (not journal) and metadata_journal:
        escaped_journal = metadata_journal.replace('"', '\\"')
        updated = replace_frontmatter_value(updated, "journal", f'"{escaped_journal}"')
    if (not year or year == "None") and metadata_year:
        updated = replace_frontmatter_value(updated, "year", str(metadata_year))
        updated = re.sub(r"^\*\*年份\*\*:.*$", f"**年份**: {metadata_year}", updated, count=1, flags=re.MULTILINE)

    current_abstract = re.search(r"^## 摘要\s*\n(.*?)(?=^## |\Z)", updated, re.DOTALL | re.MULTILINE)
    current_abstract_text = current_abstract.group(1).strip() if current_abstract else ""
    if abstract and len(current_abstract_text) < 180 and len(abstract) > len(current_abstract_text):
        updated = replace_section(updated, "摘要", abstract[:1200])
    return updated


def process_sources(limit: int = 0, dry_run: bool = False) -> list[Path]:
    metadata_by_source = load_metadata()
    changed = []
    for path in sorted(SOURCE_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        source = first_source(content)
        metadata = metadata_by_source.get(source) or metadata_by_source.get(Path(source).name) or {}
        new_content = sync_page(content, metadata)
        if new_content == content:
            continue
        changed.append(path)
        if not dry_run:
            path.write_text(new_content, encoding="utf-8")
        if limit and len(changed) >= limit:
            break
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize source page metadata")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    changed = process_sources(limit=args.limit, dry_run=args.dry_run)
    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(changed)} source pages")
    for path in changed[:30]:
        print(path.relative_to(ROOT))
    if len(changed) > 30:
        print(f"... {len(changed) - 30} more")


if __name__ == "__main__":
    main()
