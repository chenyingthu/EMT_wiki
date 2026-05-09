#!/home/chenying/anaconda3/bin/python3
"""
为 wiki/ 中的 methods/ 和 models/ 页面批量生成 Mermaid 示意图。

策略：读取页面内容 → 分析章节结构和关键概念 → 确定适合的图表类型 →
生成 Mermaid 代码 → 嵌入页面。

运行：
  python3 tools/add_diagrams_to_pages.py              # 处理所有 methods + models
  python3 tools/add_diagrams_to_pages.py --pages 20    # 仅处理前 20 页（测试）
  python3 tools/add_diagrams_to_pages.py --category methods  # 仅处理 methods
  python3 tools/add_diagrams_to_pages.py --dry-run     # 只预览，不写入
"""

import os
import re
import json
import argparse
import glob
from pathlib import Path
from typing import Any

WIKI_DIR = Path("wiki")
MIMOJI = "```mermaid"
MIMOJI_END = "```"

# ── 图表类型判断关键词 ──────────────────────────────────────────

CLS_KW = ["分类", "类型", "种类", "变体", "variant", "type", "category", "种类"]
PROC_KW = ["流程", "步骤", "过程", "algorithm", "step", "process", "procedure"]
CMP_KW = ["比较", "对比", "comparison", "vs", "versus", "差异"]
ARCH_KW = ["拓扑", "结构", "架构", "topology", "structure", "architecture", "组成"]
CTRL_KW = ["控制", "controller", "control", "调节"]
# 新增：开关相关关键词
SWITCH_KW = ["开关", "switch", "换流", "导通", "关断"]


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """简易 frontmatter 解析，返回 (meta, body)。"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[m.end():]


def _get_sections(body: str) -> list[dict]:
    """提取所有 ## / ### 章节标题及其下内容。"""
    sections = []
    current = None
    for line in body.split("\n"):
        if line.startswith("## "):
            current = {"level": 2, "heading": line[3:].strip(), "lines": []}
            sections.append(current)
        elif line.startswith("### ") and current:
            # 作为子段添加到当前章
            current["lines"].append(line)
        elif current and line.strip():
            current["lines"].append(line)
    return sections


def _has_list_item(lines: list[str]) -> list[str]:
    """提取列表项（- 开头的行）。"""
    return [l.strip("- ").strip() for l in lines if l.strip().startswith("-")]


def _has_table(lines: list[str]) -> bool:
    """判断是否含 Markdown 表格（排除 LaTeX 行）。"""
    for l in lines:
        if "\\" in l:
            continue  # 跳过 LaTeX
        if "|" in l and "---" in l:
            return True
    return False


def _find_between(text: str, start: str, end: str) -> str | None:
    """返回 start 和 end 之间的内容。"""
    i = text.find(start)
    if i < 0:
        return None
    j = text.find(end, i + len(start))
    if j < 0:
        return None
    return text[i + len(start):j].strip()


def _extract_bullets_from_section(body: str, heading: str) -> list[str]:
    """从某个 ## 章节中提取 - 开头的列表项（去除非文本标记）。"""
    # 定位章节
    pattern = rf"##\s+{re.escape(heading)}[^\n]*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pattern, body, re.DOTALL)
    if not m:
        return []
    sec_text = m.group(1)
    bullets = re.findall(r"^\s*[-*]\s+(.+)$", sec_text, re.MULTILINE)
    # 去除 [[wikilink]] 中的竖线后等噪音
    cleaned = []
    for b in bullets:
        b = re.sub(r"\[\[[^\]]+\|([^\]]+)\]\]", r"\1", b)  # [[a|b]] → b
        b = re.sub(r"\[\[([^\]]+)\]\]", r"\1", b)  # [[a]] → a
        b = b.replace("**", "").replace("`", "")
        if len(b) < 80:
            cleaned.append(b.strip())
    return cleaned


def _extract_table_data(body: str) -> list[list[str]]:
    """提取第一张 markdown 表格的前两列作为节点（排除 LaTeX 行）。"""
    lines = body.split("\n")
    header_idx = None
    for i, line in enumerate(lines):
        if "\\" in line:
            continue  # 跳过 LaTeX 公式（含反斜杠）
        if line.startswith("|") and "|" in line[1:]:
            header_idx = i
            break
    if header_idx is None:
        return []
    # 返回第 1 列和第 2 列
    rows = []
    for line in lines[header_idx + 2:]:  # 跳过表头和分隔行
        if not line.startswith("|"):
            break
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) >= 2:
            rows.append(cols[:2])
    return rows


def determine_diagram_type(body: str, sections: list[dict]) -> str:
    """判断最适合的图表类型。"""
    # 检查是否有表格 —— 表格页适合做对比图
    if _has_table(body.split("\n")):
        return "comparison"
    # 检查各章节标题
    headings_text = " ".join(s["heading"] for s in sections)
    body_lower = body.lower()
    # 检查分类关键词
    if any(kw in headings_text or kw in body_lower for kw in CLS_KW):
        return "classification"
    # 检查流程关键词（优先匹配）
    if any(kw in headings_text or kw in body_lower for kw in PROC_KW):
        return "process"
    # 检查架构关键词
    if any(kw in headings_text or kw in body_lower for kw in ARCH_KW):
        return "architecture"
    # 检查控制关键词
    if any(kw in headings_text or kw in body_lower for kw in CTRL_KW):
        return "control"
    # 检查开关关键词
    if any(kw in headings_text or kw in body_lower for kw in SWITCH_KW):
        return "switch"
    return "concept"


def _sanitize_mermaid_id(s: str) -> str:
    """清理字符串为合法 Mermaid ID（只保留字母数字和中文）。"""
    # 保留中文、字母、数字
    s = re.sub(r"[^\w一-鿿]", "", s)[:20]
    if not s or s[0].isdigit():
        s = "N" + s
    return s


def _short_label(s: str, max_len: int = 18) -> str:
    """截断过长标签。"""
    if len(s) <= max_len:
        return s
    return s[:max_len - 2] + "…"


def _safe_id(idx: int) -> str:
    return f"N{idx}"


# ── 各类图生成 ──────────────────────────────────────────────────

def gen_classification(body: str, title: str) -> str | None:
    """根据分类/类型章节生成分类树图。"""
    items = []
    # 找 "分类" / "类型" / "变体" 章
    for kw in ["分类", "类型", "变体", "种类"]:
        items = _extract_bullets_from_section(body, kw)
        if items:
            break
    if not items and "## " in body:
        # 尝试用表格数据
        rows = _extract_table_data(body)
        if rows:
            lines = []
            lines.append(f"    {_safe_id(0)}[{_short_label(title)}]")
            for i, (col1, col2) in enumerate(rows[:8], 1):
                label = _short_label(f"{col1}: {col2}")
                lines.append(f"    {_safe_id(i)}[{label}]")
                lines.append(f"    {_safe_id(0)} --> {_safe_id(i)}")
            return "graph TD\n" + "\n".join(lines)
        # 回退：取各章节标题
        sections = _get_sections(body)
        headings = [s["heading"] for s in sections if s["level"] == 2][:8]
        if headings:
            lines = [f"    {_safe_id(0)}[{_short_label(title)}]"]
            for i, h in enumerate(headings, 1):
                lines.append(f"    {_safe_id(i)}[{_short_label(h)}]")
                lines.append(f"    {_safe_id(0)} --> {_safe_id(i)}")
            return "graph TD\n" + "\n".join(lines)
    if not items:
        return None
    lines = [f"    {_safe_id(0)}[{_short_label(title)}]"]
    for i, item in enumerate(items[:10], 1):
        label = _short_label(item)
        lines.append(f"    {_safe_id(i)}[{label}]")
        lines.append(f"    {_safe_id(0)} --> {_safe_id(i)}")
    return "graph TD\n" + "\n".join(lines)


def gen_process(body: str, title: str) -> str | None:
    """根据流程/步骤生成流程图。"""
    items = []
    for kw in ["流程", "步骤", "过程"]:
        items = _extract_bullets_from_section(body, kw)
        if items:
            break
    if not items:
        sections = _get_sections(body)
        headings = [s["heading"] for s in sections if s["level"] == 2][:8]
        if headings:
            items = headings
    items = items[:10]
    if len(items) < 2:
        return None
    lines = []
    for i, item in enumerate(items):
        lines.append(f"    {_safe_id(i)}[{_short_label(item)}]")
        if i > 0:
            lines.append(f"    {_safe_id(i-1)} --> {_safe_id(i)}")
    return "graph LR\n" + "\n".join(lines)


def gen_comparison(body: str, title: str) -> str | None:
    """从表格数据生成对比图。"""
    rows = _extract_table_data(body)
    if not rows:
        return None
    lines = []
    lines.append(f"    subgraph {_safe_id('cmp')}[{_short_label(title, 30)}]")
    for i, (col1, col2) in enumerate(rows[:8]):
        label = _short_label(f"{col1}: {col2}", 30)
        lines.append(f"        {_safe_id(i)}[{label}]")
    lines.append("    end")
    return "graph TD\n" + "\n".join(lines)


def gen_architecture(body: str, title: str) -> str | None:
    """生成架构/拓扑图。"""
    sections = _get_sections(body)
    top_sections = [s["heading"] for s in sections if s["level"] == 2][:6]
    if len(top_sections) < 2:
        # 尝试提取 bullets
        items = _extract_bullets_from_section(body, "分类") or _extract_bullets_from_section(body, "类型")
        if items:
            top_sections = ["核心概念"] + items[:7]
        else:
            return None
    lines = [f"    subgraph S0[{_short_label(title, 30)}]"]
    for i, s in enumerate(top_sections):
        lines.append(f"        {_safe_id(i)}[{_short_label(s)}]")
    lines.append("    end")
    # 连线
    for i in range(len(top_sections) - 1):
        lines.append(f"    {_safe_id(i)} --> {_safe_id(i+1)}")
    return "graph TD\n" + "\n".join(lines)


def gen_control(body: str, title: str) -> str | None:
    """生成控制回路图。"""
    items = _extract_bullets_from_section(body, "控制") or _extract_bullets_from_section(body, "机制") or _extract_bullets_from_section(body, "原理")
    items = items[:8]
    if len(items) < 2:
        # 回退：用章节标题
        sections = _get_sections(body)
        h = [s["heading"] for s in sections if s["level"] == 2][:6]
        if len(h) >= 2:
            items = h
        else:
            return None
    lines = []
    for i, item in enumerate(items):
        lines.append(f"    {_safe_id(i)}[{_short_label(item)}]")
        if i > 0:
            lines.append(f"    {_safe_id(i-1)} -->|{_safe_id('f'+str(i))}| {_safe_id(i)}")
    return "graph LR\n" + "\n".join(lines)


def gen_concept(body: str, title: str) -> str | None:
    """简单概念图（回退默认）。"""
    sections = _get_sections(body)
    headings = [s["heading"] for s in sections if s["level"] == 2][:6]
    if len(headings) < 2:
        return None
    lines = [f"    {_safe_id(0)}[{_short_label(title)}]"]
    for i, h in enumerate(headings, 1):
        lines.append(f"    {_safe_id(i)}[{_short_label(h)}]")
        lines.append(f"    {_safe_id(0)} --> {_safe_id(i)}")
    return "graph TD\n" + "\n".join(lines)


def gen_switch(body: str, title: str) -> str | None:
    """开关/换流相关图。"""
    # 尝试提取包含开关、导通、关断相关的内容
    items = _extract_bullets_from_section(body, "开关") or _extract_bullets_from_section(body, "换相")
    items = items[:8]
    if len(items) >= 2:
        lines = []
        for i, item in enumerate(items):
            lines.append(f"    {_safe_id(i)}[{_short_label(item)}]")
            if i > 0:
                lines.append(f"    {_safe_id(i-1)} --> {_safe_id(i)}")
        return "graph LR\n" + "\n".join(lines)
    # 回退到 process
    return gen_process(body, title) or gen_concept(body, title)


# ── 图生成器注册表 ──────────────────────────────────────────────

GENERATORS = {
    "classification": gen_classification,
    "process": gen_process,
    "comparison": gen_comparison,
    "architecture": gen_architecture,
    "control": gen_control,
    "switch": gen_switch,
    "concept": gen_concept,
}


def has_mermaid(text: str) -> bool:
    return f"```mermaid" in text


def find_insert_position(body: str) -> int:
    """找到合适的插入位置：第一个 ## 之前（即概述后）。"""
    lines = body.split("\n")
    # 找第一个 ## 的位置
    for i, line in enumerate(lines):
        if line.startswith("## "):
            return i
    # 回退：插在 body 开头
    return 0


def build_mermaid_block(mermaid_code: str) -> str:
    return f"""
{MIMOJI}
{mermaid_code}
{MIMOJI_END}

"""


def process_page(filepath: Path, dry_run: bool = False) -> bool:
    """处理单个页面。返回 True 表示已修改。"""
    text = filepath.read_text(encoding="utf-8")
    if has_mermaid(text):
        return False  # 跳过已有图的
    meta, body = parse_frontmatter(text)
    title = meta.get("title", "") or filepath.stem
    sections = _get_sections(body)
    if not sections:
        return False
    dtype = determine_diagram_type(body, sections)
    gen = GENERATORS.get(dtype)
    if not gen:
        return False
    mermaid_code = gen(body, title)
    if not mermaid_code:
        return False
    mermaid_block = build_mermaid_block(mermaid_code)
    # 确定插入位置
    pos = find_insert_position(body)
    lines = body.split("\n")
    lines.insert(pos, mermaid_block)
    new_body = "\n".join(lines)
    # 重组：frontmatter 不变
    fm_match = re.match(r"^(---.*?---)\s*\n", text, re.DOTALL)
    if fm_match:
        new_text = text[:fm_match.end()] + new_body
    else:
        new_text = new_body
    if dry_run:
        print(f"[DRY-RUN] {filepath} → {dtype}:\n{mermaid_code}\n")
        return True
    filepath.write_text(new_text, encoding="utf-8")
    print(f"  ✓ {filepath.relative_to(WIKI_DIR)} → {dtype}")
    return True


def main():
    parser = argparse.ArgumentParser(description="批量生成 Mermaid 图表")
    parser.add_argument("--category", choices=["methods", "models"], help="仅处理指定类别")
    parser.add_argument("--pages", type=int, default=0, help="限制处理页数（测试用）")
    parser.add_argument("--dry-run", action="store_true", help="只预览，不写入")
    args = parser.parse_args()

    categories = []
    if args.category:
        categories.append(args.category)
    else:
        categories = ["methods", "models", "topics", "entities", "test-systems"]

    total_modified = 0
    for cat in categories:
        cat_dir = WIKI_DIR / cat
        files = sorted(cat_dir.rglob("*.md")) if cat_dir.exists() else []
        # 过滤 index.md / _index.md
        files = [f for f in files if not f.name.endswith("index.md")]
        count_limit = args.pages if args.pages > 0 else len(files)
        print(f"\n{'='*60}")
        print(f"类别: {cat}  |  待处理: {min(count_limit, len(files))}/{len(files)} 页")
        print(f"{'='*60}")
        for fpath_str in files[:count_limit]:
            try:
                modified = process_page(Path(fpath_str), dry_run=args.dry_run)
                if modified:
                    total_modified += 1
            except Exception as e:
                print(f"  ✗ 错误 {fpath_str}: {e}")
    print(f"\n{'='*60}")
    action = "(dry-run) 将修改" if args.dry_run else "已修改"
    print(f"{action} {total_modified} 个页面")


if __name__ == "__main__":
    main()
