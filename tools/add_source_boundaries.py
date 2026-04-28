#!/usr/bin/env python3
"""Add conservative applicability boundaries to active source pages."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"


def frontmatter(content: str) -> str:
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL | re.MULTILINE)
    return match.group(1) if match else ""


def frontmatter_value(content: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter(content), re.MULTILINE)
    return match.group(1).strip().strip('"') if match else ""


def section_text(content: str, section: str) -> str:
    match = re.search(rf"^## {re.escape(section)}\s*\n(.*?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else ""


def is_inactive_source(content: str) -> bool:
    return "type: duplicate-source" in content or "type: out-of-scope-source" in content


def first_nonempty_lines(text: str, limit: int = 2) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = raw.strip().lstrip("-").strip()
        if not line or line.startswith("|") or line.startswith("#"):
            continue
        lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def method_label(content: str) -> str:
    method_links = re.findall(r"## 使用的方法\s*\n(.*?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE)
    if method_links:
        links = re.findall(r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]", method_links[0])
        if links:
            return "、".join(link.strip() for link in links[:3])
    title = frontmatter_value(content, "title")
    return title or "该论文提出的方法"


def evidence_gap_lines(content: str) -> list[str]:
    gaps = []
    authors = frontmatter_value(content, "authors")
    journal = frontmatter_value(content, "journal")
    abstract = section_text(content, "摘要")
    validation = section_text(content, "验证详情") + "\n" + section_text(content, "仿真结果")
    findings = section_text(content, "量化发现") + "\n" + section_text(content, "主要发现")

    if not authors or re.search(r"未知|CNKI|\[\]|''|\"\"", authors):
        gaps.append("作者元数据仍需回到 PDF 首页或 metadata.json 复核。")
    if not journal:
        gaps.append("期刊/会议元数据未在当前页面中可靠给出。")
    if len(abstract) < 180:
        gaps.append("摘要抽取偏短，可能没有覆盖完整问题定义、方法和验证结论。")
    if not re.search(r"\d", findings):
        gaps.append("当前页面没有可核验的量化结果；不能据此声称具体精度、速度或误差改善。")
    if not re.search(r"PSCAD|EMTDC|EMTP|ATP|RTDS|MATLAB|Simulink|FPGA|GPU|IEEE|算例|测试系统|实验|benchmark|case", validation, re.I):
        gaps.append("验证平台、测试系统或对比基线在当前页面中不完整。")
    if not gaps:
        gaps.append("具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。")
    return gaps


def render_boundary(content: str) -> str:
    title = frontmatter_value(content, "title")
    year = frontmatter_value(content, "year")
    methods = method_label(content)
    contributions = first_nonempty_lines(section_text(content, "核心贡献"), 2)
    contribution_hint = contributions[0] if contributions else "当前页面已抽取的方法描述"
    source = frontmatter_value(content, "sources")

    year_text = "" if not year or year == "None" else f"（{year}）"
    lines = [
        "## 适用边界",
        "",
        "### 适用条件",
        "",
        f"- 适用于理解本文 `{title}`{year_text} 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。",
        f"- 适用于以 {methods} 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。",
        f"- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：{contribution_hint}",
        "",
        "### 失效边界",
        "",
        "- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。",
        "- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。",
        "- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。",
        "",
        "### 关键假设",
        "",
        "- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。",
        "- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。",
        "- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。",
        "",
        "### 证据缺口",
        "",
    ]
    lines.extend(f"- {gap}" for gap in evidence_gap_lines(content))
    if source:
        lines.append(f"- 源文件路径：`{source}`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。")
    return "\n".join(lines) + "\n"


def add_boundary(content: str) -> str:
    if is_inactive_source(content) or "## 适用边界" in content:
        return content
    return content.rstrip() + "\n\n" + render_boundary(content)


def process_sources(limit: int = 0, dry_run: bool = False) -> list[Path]:
    changed = []
    for path in sorted(SOURCE_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        new_content = add_boundary(content)
        if new_content == content:
            continue
        changed.append(path)
        if not dry_run:
            path.write_text(new_content, encoding="utf-8")
        if limit and len(changed) >= limit:
            break
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Add conservative applicability boundaries to source pages")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    changed = process_sources(limit=args.limit, dry_run=args.dry_run)
    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(changed)} source pages")
    for path in changed[:20]:
        print(path.relative_to(ROOT))
    if len(changed) > 20:
        print(f"... {len(changed) - 20} more")


if __name__ == "__main__":
    main()
