#!/usr/bin/env python3
"""Audit EMT Wiki pages against schema/QUALITY.md."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
REPORTS_DIR = ROOT / "reports"

SOURCE_REQUIRED_SECTIONS = [
    "核心贡献",
    "使用的方法",
    "涉及的模型",
    "相关主题",
    "主要发现",
    "方法细节",
    "仿真结果",
    "量化发现",
    "关键公式",
    "验证详情",
]

TAXONOMY_DIRS = ["topics", "methods", "models", "entities"]
PAGE_TYPE_BY_DIR = {
    "topics": "topic",
    "methods": "method",
    "models": "model",
    "entities": "entity",
}

GENERIC_PATTERNS = [
    r"提高(?:了)?(?:仿真)?(?:效率|精度)",
    r"效果(?:良好|显著)",
    r"高度(?:一致|吻合)",
    r"验证(?:了)?(?:方法)?(?:的)?(?:有效性|准确性)",
    r"具有(?:较高|良好)的",
]

LIMIT_PATTERNS = [
    r"局限|限制|不足|适用|不适用|假设|前提|边界|未来工作|未.*验证|需要进一步",
    r"limitation|assumption|future work|not suitable|applicability",
]

EVIDENCE_PATTERNS = [
    r"PSCAD|EMTDC|EMTP|ATP|RTDS|MATLAB|Simulink|FPGA|GPU|IEEE\s*\d+|Nelson River",
    r"测试系统|仿真工具|算例|case|benchmark|baseline|对比",
]


@dataclass
class PageAudit:
    path: str
    page_type: str
    score: int
    grade: str
    issues: list[str]
    strengths: list[str]
    metrics: dict[str, int | bool]


def section_text(content: str, section: str) -> str:
    match = re.search(rf"^## {re.escape(section)}\s*\n(.*?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else ""


def has_any(patterns: list[str], text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def count_wikilinks(text: str) -> int:
    return len(re.findall(r"\[\[[^\]]+\]\]", text))


def count_numbers(text: str) -> int:
    return len(re.findall(r"(?<![A-Za-z])\d+(?:\.\d+)?\s*(?:%|kV|MW|MVA|Hz|s|ms|us|μs|倍|次|节点|bus|µs)?", text))


def count_equations(text: str) -> int:
    return text.count("$$") // 2 + len(re.findall(r"(?<!\$)\$[^$\n]{3,}\$(?!\$)", text))


def grade_for(score: int) -> str:
    if score >= 85:
        return "A"
    if score >= 65:
        return "B"
    if score >= 40:
        return "C"
    return "D"


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def is_duplicate_pointer(content: str) -> bool:
    return "type: duplicate-source" in content


def is_inactive_source(content: str) -> bool:
    return "type: duplicate-source" in content or "type: out-of-scope-source" in content


def audit_source(path: Path) -> PageAudit:
    content = path.read_text(encoding="utf-8")
    issues: list[str] = []
    strengths: list[str] = []
    score = 0

    present_sections = [section for section in SOURCE_REQUIRED_SECTIONS if f"## {section}" in content]
    section_score = round(30 * len(present_sections) / len(SOURCE_REQUIRED_SECTIONS))
    score += section_score
    if len(present_sections) == len(SOURCE_REQUIRED_SECTIONS):
        strengths.append("all required source sections present")
    else:
        missing = sorted(set(SOURCE_REQUIRED_SECTIONS) - set(present_sections))
        issues.append("missing sections: " + ", ".join(missing))

    method_details = section_text(content, "方法细节")
    findings = section_text(content, "量化发现") + "\n" + section_text(content, "主要发现")
    validation = section_text(content, "验证详情") + "\n" + section_text(content, "仿真结果")
    contributions = section_text(content, "核心贡献")

    equations = count_equations(section_text(content, "关键公式") + "\n" + method_details)
    numbers = count_numbers(findings + "\n" + validation)
    wikilinks = count_wikilinks(content)
    has_evidence = has_any(EVIDENCE_PATTERNS, validation)
    has_limits = has_any(LIMIT_PATTERNS, content)
    generic_hits = sum(1 for pattern in GENERIC_PATTERNS if re.search(pattern, content))

    if len(method_details) >= 500:
        score += 15
        strengths.append("method details are substantial")
    elif method_details:
        score += 8
        issues.append("method details are thin")
    else:
        issues.append("missing method mechanism")

    if equations >= 1:
        score += 10
        strengths.append("has equations")
    else:
        issues.append("missing key equations")

    if numbers >= 3:
        score += 15
        strengths.append("has multiple quantitative details")
    elif numbers >= 1:
        score += 8
        issues.append("limited quantitative evidence")
    else:
        issues.append("missing quantitative evidence")

    if has_evidence:
        score += 10
        strengths.append("validation setup/tool appears")
    else:
        issues.append("validation setup/tool unclear")

    if has_limits:
        score += 10
        strengths.append("mentions assumptions or limits")
    else:
        issues.append("assumptions/limits not explicit")

    if wikilinks >= 3:
        score += 5
    else:
        issues.append("few knowledge graph links")

    if len(contributions) >= 120:
        score += 5
    else:
        issues.append("contributions are thin")

    if generic_hits >= 3:
        score -= 8
        issues.append("many generic quality claims")
    elif generic_hits:
        score -= 3
        issues.append("some generic quality claims")

    score = max(0, min(100, score))
    metrics = {
        "required_sections": len(present_sections),
        "equations": equations,
        "numbers": numbers,
        "wikilinks": wikilinks,
        "has_evidence": has_evidence,
        "has_limits": has_limits,
        "generic_hits": generic_hits,
        "bytes": path.stat().st_size,
    }
    return PageAudit(display_path(path), "source", score, grade_for(score), issues[:8], strengths[:6], metrics)


def audit_taxonomy(path: Path) -> PageAudit:
    content = path.read_text(encoding="utf-8")
    issues: list[str] = []
    strengths: list[str] = []
    score = 0

    headings = re.findall(r"^##\s+", content, re.MULTILINE)
    tables = content.count("|")
    wikilinks = count_wikilinks(content)
    equations = count_equations(content)
    numbers = count_numbers(content)
    has_limits = has_any(LIMIT_PATTERNS, content)
    has_synthesis = any(
        marker in content
        for marker in [
            "深度增强内容",
            "核心原理详解",
            "关键技术详解",
            "各类模型数学描述",
            "开放问题",
            "最佳实践",
            "定义与概述",
            "作用机制",
            "合成定位",
            "适用边界",
            "失败边界",
            "代表性来源",
            "代表性论文",
            "验证共识",
        ]
    )

    if len(content) >= 5000:
        score += 20
        strengths.append("substantial page length")
    elif len(content) >= 2000:
        score += 12
    else:
        issues.append("taxonomy page is short")

    if len(headings) >= 5:
        score += 15
        strengths.append("multiple synthesis sections")
    else:
        issues.append("few synthesis sections")

    if has_synthesis:
        score += 20
        strengths.append("has synthesis-oriented sections")
    else:
        issues.append("may be mostly index/list content")

    if wikilinks >= 10:
        score += 10
    elif wikilinks >= 3:
        score += 5
    else:
        issues.append("few cross-links")

    if equations >= 1:
        score += 10
        strengths.append("has equations")
    else:
        issues.append("missing mathematical form")

    if numbers >= 5:
        score += 10
        strengths.append("has quantitative details")
    elif numbers:
        score += 5
    else:
        issues.append("few quantitative details")

    if has_limits:
        score += 10
    else:
        issues.append("limits/open problems not explicit")

    table_ratio = tables / max(1, len(content) / 1000)
    if table_ratio > 20 and not has_synthesis:
        score -= 10
        issues.append("table-heavy without synthesis")

    score = max(0, min(100, score))
    page_type = PAGE_TYPE_BY_DIR.get(path.parent.name, path.parent.name)
    metrics = {
        "headings": len(headings),
        "equations": equations,
        "numbers": numbers,
        "wikilinks": wikilinks,
        "has_limits": has_limits,
        "has_synthesis": has_synthesis,
        "bytes": path.stat().st_size,
    }
    return PageAudit(display_path(path), page_type, score, grade_for(score), issues[:8], strengths[:6], metrics)


def collect_audits() -> list[PageAudit]:
    audits: list[PageAudit] = []
    for path in sorted((WIKI_DIR / "sources").glob("*.md")):
        content = path.read_text(encoding="utf-8")
        if is_inactive_source(content):
            continue
        audits.append(audit_source(path))
    for dirname in TAXONOMY_DIRS:
        for path in sorted((WIKI_DIR / dirname).glob("*.md")):
            audits.append(audit_taxonomy(path))
    return audits


def write_reports(audits: list[PageAudit], json_path: Path, md_path: Path) -> None:
    json_path.parent.mkdir(exist_ok=True)
    md_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps([asdict(audit) for audit in audits], ensure_ascii=False, indent=2), encoding="utf-8")

    grade_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    for audit in audits:
        grade_counts[audit.grade] = grade_counts.get(audit.grade, 0) + 1
        type_counts[audit.page_type] = type_counts.get(audit.page_type, 0) + 1

    worst = sorted(audits, key=lambda item: (item.score, item.path))[:50]
    lines = [
        "# Wiki Quality Audit",
        "",
        "Generated: 2026-04-26",
        "",
        "This is a heuristic triage report based on `schema/QUALITY.md`. Scores indicate review priority, not final truth.",
        "",
        "## Summary",
        "",
        f"- Pages audited: {len(audits)}",
        "- Grades: " + ", ".join(f"{grade}={grade_counts.get(grade, 0)}" for grade in ["A", "B", "C", "D"]),
        "- Types: " + ", ".join(f"{key}={value}" for key, value in sorted(type_counts.items())),
        "",
        "## Lowest Scoring Pages",
        "",
        "| Score | Grade | Type | Page | Main issues |",
        "|------:|:-----:|------|------|-------------|",
    ]
    for audit in worst:
        issues = "; ".join(audit.issues[:3]).replace("|", "\\|")
        lines.append(f"| {audit.score} | {audit.grade} | {audit.page_type} | `{audit.path}` | {issues} |")

    lines.extend(["", "## Upgrade Queues", ""])
    for page_type in ["source", "topic", "method", "model", "entity"]:
        subset = [audit for audit in audits if audit.page_type == page_type and audit.grade in {"C", "D"}]
        if not subset:
            continue
        lines.append(f"### {page_type}")
        for audit in sorted(subset, key=lambda item: (item.score, item.path))[:20]:
            lines.append(f"- `{audit.path}` — {audit.score}/{audit.grade}: {', '.join(audit.issues[:3])}")
        lines.append("")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit EMT Wiki page quality")
    parser.add_argument("--json", default=str(REPORTS_DIR / "wiki_quality_audit.json"))
    parser.add_argument("--markdown", default=str(REPORTS_DIR / "wiki_quality_audit.md"))
    args = parser.parse_args()
    audits = collect_audits()
    write_reports(audits, Path(args.json), Path(args.markdown))
    print(f"Audited {len(audits)} pages")
    print(f"Wrote {args.markdown}")
    print(f"Wrote {args.json}")


if __name__ == "__main__":
    main()
