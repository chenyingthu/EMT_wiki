#!/usr/bin/env python3
"""Fill remaining source-page journals from high-confidence Crossref matches."""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

import repair_source_summaries


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"
REPORT_PATH = ROOT / "reports" / "crossref_journal_repairs.json"

CONTAINER_NORMALIZATIONS = {
    "2011 IEEE Power and Energy Society General Meeting": "IEEE Power & Energy Society General Meeting",
    "2012 IEEE Power and Energy Society General Meeting": "IEEE Power & Energy Society General Meeting",
    "2013 IEEE Power & Energy Society General Meeting": "IEEE Power & Energy Society General Meeting",
    "2015 IEEE Power & Energy Society General Meeting": "IEEE Power & Energy Society General Meeting",
    "2017 IEEE Power & Energy Society General Meeting": "IEEE Power & Energy Society General Meeting",
    "2018 IEEE Power & Energy Society General Meeting": "IEEE Power & Energy Society General Meeting",
    "2020 IEEE Power & Energy Society General Meeting (PESGM)": "IEEE Power & Energy Society General Meeting",
    "2021 IEEE Power & Energy Society General Meeting (PESGM)": "IEEE Power & Energy Society General Meeting",
    "2022 IEEE Power & Energy Society General Meeting (PESGM)": "IEEE Power & Energy Society General Meeting",
    "2023 IEEE Power & Energy Society General Meeting (PESGM)": "IEEE Power & Energy Society General Meeting",
    "2024 IEEE Power & Energy Society General Meeting (PESGM)": "IEEE Power & Energy Society General Meeting",
    "2025 IEEE Power & Energy Society General Meeting (PESGM)": "IEEE Power & Energy Society General Meeting",
    "11th IET International Conference on Developments in Power Systems Protection (DPSP 2012)": "IET International Conference on Developments in Power Systems Protection",
}


def normalize_text(value: str) -> str:
    value = value.replace("&amp;", "&")
    value = re.sub(r"[_\W]+", " ", value, flags=re.UNICODE).casefold()
    return re.sub(r"\s+", " ", value).strip()


def frontmatter(content: str) -> str:
    return repair_source_summaries.frontmatter(content)


def frontmatter_value(content: str, key: str) -> str:
    return repair_source_summaries.frontmatter_value(content, key)


def first_source(content: str) -> str:
    return repair_source_summaries.first_source(content)


def title_candidates(content: str) -> list[str]:
    candidates = [frontmatter_value(content, "title")]
    source = first_source(content)
    source_title = re.sub(r"\.pdf(?:\.pdf)?$", "", Path(source).name, flags=re.IGNORECASE)
    source_title = re.sub(r"^.+?\s*[-–]\s*(?:19|20)\d{2}\s*[-–]\s*", "", source_title)
    source_title = re.sub(r";\s*\[[^\]]+$", "", source_title)
    candidates.append(source_title)
    candidates = [candidate.strip().strip('"') for candidate in candidates if candidate.strip().strip('"')]
    deduped = []
    seen = set()
    for candidate in candidates:
        key = normalize_text(candidate)
        if key and key not in seen:
            deduped.append(candidate)
            seen.add(key)
    return deduped


def title_similarity(a: str, b: str) -> float:
    left = normalize_text(a)
    right = normalize_text(b)
    if not left or not right:
        return 0.0
    return SequenceMatcher(None, left, right).ratio()


def normalized_container(container: str) -> str:
    container = container.replace("&amp;", "&").strip()
    if not container:
        return ""
    if container in CONTAINER_NORMALIZATIONS:
        return CONTAINER_NORMALIZATIONS[container]
    if re.search(r"IEEE\s+Power\s*(?:&|and)\s*Energy\s+Society\s+General\s+Meeting", container, re.IGNORECASE):
        return "IEEE Power & Energy Society General Meeting"
    if re.search(r"International\s+Conference\s+on\s+Developments\s+in\s+Power\s+Systems\s+Protection", container, re.IGNORECASE):
        return "IET International Conference on Developments in Power Systems Protection"
    return repair_source_summaries.journal_from_text(container) or container


def query_crossref(title: str, rows: int = 3) -> list[dict]:
    query = urllib.parse.urlencode(
        {
            "query.title": title,
            "rows": str(rows),
            "select": "DOI,title,container-title,score,type",
        }
    )
    request = urllib.request.Request(
        f"https://api.crossref.org/works?{query}",
        headers={"User-Agent": "EMT_LLM_Wiki metadata repair (mailto:metadata@example.invalid)"},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data.get("message", {}).get("items", [])


def best_match(content: str) -> dict | None:
    best = None
    for candidate in title_candidates(content):
        try:
            items = query_crossref(candidate)
        except Exception as exc:  # pragma: no cover - network failures are reported.
            return {"error": str(exc), "query": candidate}
        time.sleep(0.12)
        for item in items:
            titles = item.get("title") or []
            item_title = titles[0] if titles else ""
            containers = item.get("container-title") or []
            container = normalized_container(containers[0] if containers else "")
            similarity = title_similarity(candidate, item_title)
            if not container or similarity < 0.88:
                continue
            scored = {
                "query": candidate,
                "crossref_title": item_title,
                "container": container,
                "doi": item.get("DOI", ""),
                "score": item.get("score", 0),
                "similarity": round(similarity, 4),
            }
            if best is None or (scored["similarity"], scored["score"]) > (best["similarity"], best["score"]):
                best = scored
    if not best:
        return None
    if best["similarity"] >= 0.96:
        return best
    if best["similarity"] >= 0.92 and best["score"] >= 45:
        return best
    if best["similarity"] >= 0.88 and best["score"] >= 55:
        return best
    return None


def is_active_blank_source(content: str) -> bool:
    if repair_source_summaries.is_inactive_source(content):
        return False
    return not frontmatter_value(content, "journal").strip('"')


def replace_journal(content: str, journal: str) -> str:
    escaped = journal.replace('"', '\\"')
    content = repair_source_summaries.replace_frontmatter_value(content, "journal", f'"{escaped}"')
    return repair_source_summaries.remove_stale_metadata_gap_markers(content)


def process(limit: int = 0, dry_run: bool = False) -> list[dict]:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    repairs = []
    checked = 0
    for path in sorted(SOURCE_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        if not is_active_blank_source(content):
            continue
        checked += 1
        match = best_match(content)
        if not match or match.get("error"):
            continue
        journal = match["container"]
        updated = replace_journal(content, journal)
        repairs.append({"path": str(path.relative_to(ROOT)), **match})
        if not dry_run:
            path.write_text(updated, encoding="utf-8")
        if limit and len(repairs) >= limit:
            break
    report = {"checked_blank_sources": checked, "repairs": repairs}
    if not dry_run:
        REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return repairs


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair source journals from high-confidence Crossref matches")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    repairs = process(limit=args.limit, dry_run=args.dry_run)
    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(repairs)} source pages")
    for repair in repairs[:40]:
        print(f"{repair['path']} -> {repair['container']} ({repair['similarity']}, {repair['doi']})")
    if len(repairs) > 40:
        print(f"... {len(repairs) - 40} more")


if __name__ == "__main__":
    main()
