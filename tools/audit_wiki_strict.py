#!/usr/bin/env python3
"""Strict wiki quality triage beyond the coarse A/B score.

This script is intentionally conservative: it flags pages that need human or
LLM review, even when the heuristic quality audit already marks them as A.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
REPORTS_DIR = ROOT / "reports"
SOURCE_DIR = WIKI_DIR / "sources"
TAXONOMY_DIRS = ("topics", "methods", "models", "entities")

BAD_AUTHOR_RE = re.compile(r"未知|CNKI|IEEE|作者|\[\]|''|\"\"")
BAD_TITLE_RE = re.compile(r"untitled|Published in|第\d+\s*卷|标题|\.pdf$", re.IGNORECASE)
GENERIC_STRONG_RE = re.compile(
    r"高度吻合|显著|精确|准确|大幅|彻底|完美|优异|最高|\d+(?:\.\d+)?\s*%|\d+(?:\.\d+)?\s*倍"
)
UNCERTAINTY_RE = re.compile(r"原文未|未明确|not provided|未给出|抽取文本")
JOURNAL_GAP_RE = re.compile(r"期刊/会议元数据未在当前页面中可靠给出|期刊/会议元数据未可靠给出")
DEEP_REVIEW_REQUIRED = (
    "1. 需求、对象、挑战与贡献",
    "2. 模型、算法与实现技术",
    "3. 验证、优势与不足",
    "4. 价值、认知与可复用场景",
    "证据边界",
)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
OUT_OF_SCOPE_RE = re.compile(
    r"Annals of Oncology|hepatocellular|colon cancer|clinical study|oncology|medical oncology|"
    r"gastric|tumou?r|chemotherapy|millimeter wave beam steering",
    re.IGNORECASE,
)


@dataclass
class StrictFinding:
    path: str
    page_type: str
    score: int
    issues: list[str]
    metrics: dict[str, int | bool]


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def frontmatter(content: str) -> str:
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL | re.MULTILINE)
    return match.group(1) if match else ""


def frontmatter_value(content: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter(content), re.MULTILINE)
    return match.group(1).strip() if match else ""


def section_text(content: str, section: str) -> str:
    match = re.search(rf"^## {re.escape(section)}\s*\n(.*?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else ""


def count_h1(content: str) -> int:
    return len(re.findall(r"^#\s+", content, re.MULTILINE))


def count_wikilinks(content: str) -> int:
    return len(WIKILINK_RE.findall(content))


def count_missing_wikilinks(content: str) -> int:
    missing = 0
    for target in WIKILINK_RE.findall(content):
        normalized = target.strip()
        if not normalized:
            continue
        if not list(WIKI_DIR.glob(f"**/{normalized}.md")):
            missing += 1
    return missing


def is_inactive_source(content: str) -> bool:
    return "type: duplicate-source" in content or "type: out-of-scope-source" in content


def has_numeric_evidence_sections(content: str) -> bool:
    evidence = "\n".join(
        section_text(content, section)
        for section in ("量化发现", "验证详情", "仿真结果", "主要发现")
    )
    return bool(re.search(r"\d|原文未报告|未给出|无法确认", evidence))


def has_complete_deep_review(content: str) -> bool:
    if "<!-- deep-review:start -->" not in content or "<!-- deep-review:end -->" not in content:
        return False
    block = content.split("<!-- deep-review:start -->", 1)[1].split("<!-- deep-review:end -->", 1)[0]
    return all(item in block for item in DEEP_REVIEW_REQUIRED) and len(block.strip()) >= 1000


def audit_source(path: Path) -> StrictFinding | None:
    content = path.read_text(encoding="utf-8")
    if is_inactive_source(content):
        return None

    score = 0
    issues: list[str] = []

    authors = frontmatter_value(content, "authors")
    title = frontmatter_value(content, "title")
    journal = frontmatter_value(content, "journal").strip('"')
    abstract = section_text(content, "摘要")
    contributions = section_text(content, "核心贡献")

    if BAD_AUTHOR_RE.search(authors):
        score += 20
        issues.append("bad or placeholder author metadata")
    if BAD_TITLE_RE.search(title):
        score += 18
        issues.append("bad or placeholder title metadata")
    if not journal and not JOURNAL_GAP_RE.search(content):
        score += 4
        issues.append("blank journal metadata")
    if len(abstract) < 180:
        score += 8
        issues.append("abstract is short or truncated")
    if re.search(r"\b(the|this|paper|abstract)\b", abstract[:500], re.IGNORECASE) and not re.search(
        r"[\u4e00-\u9fff]", abstract[:500]
    ):
        score += 3
        issues.append("abstract is untranslated English only")
    if "## 适用边界" not in content and "### 适用边界" not in content:
        score += 12
        issues.append("missing explicit applicability boundary section")
    if OUT_OF_SCOPE_RE.search(content[:4000]):
        score += 30
        issues.append("likely out-of-scope extracted content")
    if len(contributions) < 160:
        score += 8
        issues.append("contributions are thin")
    if GENERIC_STRONG_RE.search(content) and not (UNCERTAINTY_RE.search(content) or has_numeric_evidence_sections(content)):
        score += 4
        issues.append("strong numeric or quality claims need evidence check")
    if count_h1(content) != 1:
        score += 6
        issues.append("unexpected H1 count")
    if not has_complete_deep_review(content):
        score += 6
        issues.append("missing reader-facing deep review")

    metrics = {
        "bytes": path.stat().st_size,
        "h1_count": count_h1(content),
        "wikilinks": count_wikilinks(content),
        "missing_wikilinks": count_missing_wikilinks(content),
        "has_limits": "适用边界" in content,
        "has_uncertainty_markers": bool(UNCERTAINTY_RE.search(content)),
        "has_journal_gap_marker": bool(JOURNAL_GAP_RE.search(content)),
        "has_numeric_evidence_sections": has_numeric_evidence_sections(content),
        "has_deep_review": has_complete_deep_review(content),
    }
    if score <= 0:
        return None
    return StrictFinding(display_path(path), "source", score, issues, metrics)


def audit_taxonomy(path: Path) -> StrictFinding | None:
    content = path.read_text(encoding="utf-8")
    type_names = {
        "topics": "topic",
        "methods": "method",
        "models": "model",
        "entities": "entity",
    }
    page_type = type_names.get(path.parent.name, path.parent.name)
    score = 0
    issues: list[str] = []

    h1_count = count_h1(content)
    links = count_wikilinks(content)
    missing_links = count_missing_wikilinks(content)
    has_definition = "## 定义" in content or "## 概述" in content
    has_boundaries = "边界" in content or "限制" in content or "局限" in content
    has_representative = "代表性" in content or "来源论文" in content

    if h1_count != 1:
        score += 12
        issues.append("duplicate or missing H1")
    if not has_definition:
        score += 10
        issues.append("missing definition/overview section")
    if not has_boundaries:
        score += 12
        issues.append("missing boundaries or limitations")
    if not has_representative:
        score += 8
        issues.append("missing representative sources")
    if links < 8 and path.parent.name in {"topics", "methods", "models"}:
        score += 8
        issues.append("weak internal linking")
    if links < 6 and path.parent.name == "entities":
        score += 6
        issues.append("weak entity cross-linking")
    if missing_links:
        score += min(20, missing_links * 2)
        issues.append("contains missing wikilinks")

    metrics = {
        "bytes": path.stat().st_size,
        "h1_count": h1_count,
        "wikilinks": links,
        "missing_wikilinks": missing_links,
        "has_definition": has_definition,
        "has_boundaries": has_boundaries,
        "has_representative": has_representative,
    }
    if score <= 0:
        return None
    return StrictFinding(display_path(path), page_type, score, issues, metrics)


def collect_findings() -> list[StrictFinding]:
    findings: list[StrictFinding] = []
    for path in sorted(SOURCE_DIR.glob("*.md")):
        finding = audit_source(path)
        if finding:
            findings.append(finding)
    for dirname in TAXONOMY_DIRS:
        for path in sorted((WIKI_DIR / dirname).glob("*.md")):
            finding = audit_taxonomy(path)
            if finding:
                findings.append(finding)
    return sorted(findings, key=lambda item: (-item.score, item.path))


def write_reports(findings: list[StrictFinding], json_path: Path, md_path: Path, limit: int) -> None:
    json_path.parent.mkdir(exist_ok=True)
    md_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Strict Wiki Quality Audit",
        "",
        "This report flags review risks beyond the coarse A/B score. It is a work queue, not a final judgment.",
        "",
        f"- Findings: {len(findings)}",
        "",
        "| Risk | Type | Page | Issues |",
        "|-----:|------|------|--------|",
    ]
    for item in findings[:limit]:
        issues = "; ".join(item.issues[:4]).replace("|", "\\|")
        lines.append(f"| {item.score} | {item.page_type} | `{item.path}` | {issues} |")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Strict EMT wiki quality triage")
    parser.add_argument("--json", default=str(REPORTS_DIR / "wiki_strict_audit.json"))
    parser.add_argument("--markdown", default=str(REPORTS_DIR / "wiki_strict_audit.md"))
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()

    findings = collect_findings()
    write_reports(findings, Path(args.json), Path(args.markdown), args.limit)
    print(f"Strict findings: {len(findings)}")
    print(f"Wrote {args.markdown}")
    print(f"Wrote {args.json}")


if __name__ == "__main__":
    main()
