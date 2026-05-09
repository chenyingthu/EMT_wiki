#!/usr/bin/env python3
"""Academic expression audit — scan wiki pages for non-academic language patterns.

Checks against academic-style-guide.md: strong assertions, vague quantifiers,
anthropomorphism, marketing language, unbounded conclusions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
REPORTS_DIR = ROOT / "reports"
TAXONOMY_DIRS = ("entities", "methods", "models", "topics")

# ---------------------------------------------------------------------------
# Pattern groups — grouped by violation category
# ---------------------------------------------------------------------------

STRONG_ASSERTIONS = [
    # 全球领先 / 国际领先
    re.compile(r"全球[一二三四五六七八九十]*[^。]*?领先"),
    re.compile(r"国际[一二三四五六七八九十]*[^。]*?领先"),
    re.compile(r"世界[一二三四五六七八九十]*[^。]*?领先"),
    # 最X (superlatives without context — requires manual review per match)
    re.compile(r"最(?:经典|重要|先进|广泛|主要|核心|关键|全面|权威|优秀|知名|具影响力)"),
    # 第一等绝对排名
    re.compile(r"(?:第|创)[一二三四五六七八九十]个|首(?:个|款|套|家|次)"),
    # 突破 / 重大突破
    re.compile(r"突破(?:性|了)?(?:成果|进展|贡献|技术)?"),
    re.compile(r"重大(?:突破|进展|贡献|创新)"),
    # 彻底 / 完全 + 解决/克服
    re.compile(r"彻底(?:解决|克服|消除|改变)"),
    re.compile(r"完全(?:解决|克服|消除|替代)"),
    # 泰斗 / 权威 / 大师
    re.compile(r"泰斗|学界泰斗|行业泰斗"),
    re.compile(r"(?:业界|行业|学术|技术)权威"),
    re.compile(r"(?:一代|学术|技术)大师"),
    # 金标准 / 黄金标准
    re.compile(r'金[标准]标准|“黄金标准”'),
    # 独一无二 / 独具特色 / 无可替代
    re.compile(r"独一无二|无可替代|无与伦比|不可替代"),
    re.compile(r"独具(?:特色|优势|匠心)"),
]

VAGUE_QUANTIFIERS = [
    re.compile(r"(?:显著|大幅|明显)(?:提高|提升|降低|减少|增加|改善|优化|加速|抑制)"),
    re.compile(r"极大(?:提高|提升|降低|减少|节省|简化)"),
    re.compile(r"良好(?:的)?(?:性能|效果|精度|收敛性|稳定性|一致性|适用性)"),
    re.compile(r"优秀(?:的)?(?:性能|效果|精度|收敛性|准确性)"),
]

ANTHROPOMORPHISM = [
    re.compile(r"论文提出(?!了[^。]*?(?:等|作者|学者))"),
    re.compile(r"本文提出|本文介绍|本文分析|本文讨论|本文研究|本文采用"),
    re.compile(r"文章提出|文章介绍|文章分析"),
    re.compile(r"文献提出|文献介绍|文献指出"),
    re.compile(r"该文提出|该文介绍|该文采用|该文提出|该文指出"),
]

MARKETING_LANGUAGE = [
    re.compile(r"革命性(?:的)?(?:技术|突破|创新|产品|方案)"),
    re.compile(r"颠覆性(?:的)?(?:技术|创新|突破|方案)"),
    re.compile(r"划时代(?:的)?(?:技术|创新|产品|意义)"),
    re.compile(r"全新(?:的)?(?:技术|方案|架构|一代|平台|理念)"),
    re.compile(r"业界第[一二三四五六七八九十][^。]*?(?:平台|产品|工具|方案)"),
    re.compile(r"完美(?:解决|适配|支持|兼容|实现|满足)"),
]

UNBOUNDED_CLAIMS = [
    re.compile(r"适用于所有|适用于任何"),
    re.compile(r"任意[^。]*?(?:场景|条件|系统|工况)"),
]

# Compiled combined pattern for line scanning
ALL_ACADEMIC_PATTERNS: list[tuple[str, re.Pattern]] = []
for label, patterns in [
    ("强断言", STRONG_ASSERTIONS),
    ("模糊量词", VAGUE_QUANTIFIERS),
    ("拟人化", ANTHROPOMORPHISM),
    ("营销语言", MARKETING_LANGUAGE),
    ("无边界声明", UNBOUNDED_CLAIMS),
]:
    for p in patterns:
        ALL_ACADEMIC_PATTERNS.append((label, p))


@dataclass
class Violation:
    category: str
    pattern: str
    line: int
    text: str
    fix_suggestion: str


@dataclass
class PageReport:
    path: str
    page_type: str
    total_violations: int
    violations: list[Violation]
    categories: dict[str, int]


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def categorize_fix(category: str, matched: str) -> str:
    """Suggest a fix pattern based on the violation category and matched text."""
    suggestions = {
        "全球领先": "降级为 有研究成果 / 用于",
        "国际领先": "降级为 有研究成果 / 用于",
        "世界领先": "降级为 有研究成果 / 用于",
        "最经典": "降级为 经典",
        "最重要": "降级为 重要 / 主要之一",
        "最广泛": "降级为 被用于",
        "最权威": "降级为 权威（需引用支持）",
        "泰斗": "降级为 学者 / 研究者",
        "突破": "降级为 贡献 / 技术贡献",
        "金标准": "降级为 参考标准",
        "独一无二": "删除或替换为 具有特征",
        "彻底解决": "降级为 能够处理 / 适用于",
        "显著": "替换为量化比较（含数值）",
        "大幅": "替换为具体百分比或倍数",
        "广泛": "替换为 用于 / 被应用于",
        "论文提出": "替换为 X等提出 / X等(年份)",
        "本文提出": "替换为 X等提出（引用原文）",
        "革命性": "删除或替换为 新的",
        "完美": "替换为 有效 / 能够",
    }
    for key, suggestion in suggestions.items():
        if key in matched:
            return suggestion
    return "需人工判断"


def scan_file(path: Path) -> PageReport | None:
    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Skip YAML frontmatter
    start_line = 0
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                start_line = i + 1
                break

    # Determine page type from parent directory
    type_names = {
        "topics": "topic",
        "methods": "method",
        "models": "model",
        "entities": "entity",
    }
    page_type = type_names.get(path.parent.name, "other")

    violations: list[Violation] = []
    seen = set()  # avoid duplicate reports for same line+pattern

    for lineno in range(start_line, len(lines)):
        line = lines[lineno]
        # Skip code blocks, mermaid, HTML comments
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("<!--") or stripped.startswith("$"):
            continue
        if stripped.startswith("|") and "---" in stripped:
            continue  # table separators

        for category, pattern in ALL_ACADEMIC_PATTERNS:
            match = pattern.search(line)
            if match:
                key = (lineno + 1, match.group()[:60])
                if key in seen:
                    continue
                seen.add(key)
                matched_text = match.group()[:80]
                violations.append(
                    Violation(
                        category=category,
                        pattern=matched_text,
                        line=lineno + 1,
                        text=line.strip()[:120],
                        fix_suggestion=categorize_fix(category, matched_text),
                    )
                )

    if not violations:
        return None

    cat_counts: dict[str, int] = {}
    for v in violations:
        cat_counts[v.category] = cat_counts.get(v.category, 0) + 1

    return PageReport(
        path=display_path(path),
        page_type=page_type,
        total_violations=len(violations),
        violations=violations,
        categories=cat_counts,
    )


def collect_reports() -> list[PageReport]:
    reports: list[PageReport] = []
    for dirname in TAXONOMY_DIRS:
        for path in sorted((WIKI_DIR / dirname).glob("*.md")):
            report = scan_file(path)
            if report:
                reports.append(report)
    return sorted(reports, key=lambda r: (-r.total_violations, r.path))


def write_reports(reports: list[PageReport], json_path: Path, md_path: Path) -> None:
    json_path.parent.mkdir(exist_ok=True)

    # Convert to serializable
    json_data = []
    for r in reports:
        json_data.append({
            "path": r.path,
            "page_type": r.page_type,
            "total_violations": r.total_violations,
            "categories": r.categories,
            "violations": [asdict(v) for v in r.violations],
        })
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Summary stats
    total_violations = sum(r.total_violations for r in reports)
    cat_totals: dict[str, int] = {}
    for r in reports:
        for cat, cnt in r.categories.items():
            cat_totals[cat] = cat_totals.get(cat, 0) + cnt

    lines = [
        "# 学术表达审计报告",
        "",
        f"审核页面数: {len(reports)} (含违规)",
        f"违规总数: {total_violations}",
        "",
        "## 按类别统计",
        "",
        "| 类别 | 数量 |",
        "|------|:----:|",
    ]
    for cat in ["强断言", "模糊量词", "拟人化", "营销语言", "无边界声明"]:
        cnt = cat_totals.get(cat, 0)
        if cnt:
            lines.append(f"| {cat} | {cnt} |")
    lines.append("")
    lines.append("## 按页面统计（违规数降序）")
    lines.append("")
    lines.append("| 页面 | 类型 | 违规数 | 主要类别 |")
    lines.append("|------|:----:|:------:|----------|")
    for r in reports[:80]:
        cats = ", ".join(f"{k}:{v}" for k, v in sorted(r.categories.items()))
        lines.append(f"| `{r.path}` | {r.page_type} | {r.total_violations} | {cats} |")

    lines.append("")
    lines.append("## 详细违规列表")
    lines.append("")
    for r in reports:
        lines.append(f"### {r.path} ({r.total_violations} 处违规)")
        lines.append("")
        lines.append("| 行号 | 类别 | 匹配文本 | 建议修正 |")
        lines.append("|:----:|------|---------|---------|")
        for v in r.violations[:20]:  # cap per page
            text_escaped = v.text.replace("|", "\|")[:80]
            pattern_escaped = v.pattern.replace("|", "\|")[:60]
            fix_escaped = v.fix_suggestion.replace("|", "\|")
            lines.append(f"| {v.line} | {v.category} | `{text_escaped}` | {fix_escaped} |")
        if len(r.violations) > 20:
            lines.append(f"| ... | ... | 剩余 {len(r.violations) - 20} 条 | ... |")
        lines.append("")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Academic expression audit for EMT Wiki")
    parser.add_argument("--json", default=str(REPORTS_DIR / "academic_audit.json"))
    parser.add_argument("--markdown", default=str(REPORTS_DIR / "academic_audit.md"))
    parser.add_argument("--dir", choices=TAXONOMY_DIRS, help="Scan only one directory")
    args = parser.parse_args()

    reports = collect_reports()
    if args.dir:
        reports = [r for r in reports if r.path.startswith(f"wiki/{args.dir}/")]

    write_reports(reports, Path(args.json), Path(args.markdown))

    total = sum(r.total_violations for r in reports)
    cat_totals: dict[str, int] = {}
    for r in reports:
        for cat, cnt in r.categories.items():
            cat_totals[cat] = cat_totals.get(cat, 0) + cnt
    print(f"Academic audit: {len(reports)} pages with violations, {total} total violations")
    for cat, cnt in sorted(cat_totals.items()):
        print(f"  {cat}: {cnt}")


if __name__ == "__main__":
    main()