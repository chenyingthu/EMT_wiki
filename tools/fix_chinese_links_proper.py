#!/usr/bin/env python3
"""
正确修复中文链接 - 将中文链接映射到英文页面，同时保留中文显示文本
"""

import re
import json
from pathlib import Path
from collections import defaultdict, Counter

# 导入映射字典
from chinese_to_english_mapping import CHINESE_TO_ENGLISH

WIKI_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki")
SOURCES_DIR = WIKI_DIR / "sources"
REPORT_FILE = Path("/home/chenying/researches/EMT_LLM_Wiki/reports/wiki_lint_current.json")


def extract_wikilinks(content):
    """提取所有wiki链接 [[target|display]] 或 [[target]]"""
    pattern = r'\[\[([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'
    return re.findall(pattern, content)


def find_chinese_links(content):
    """查找包含中文的链接"""
    chinese_pattern = re.compile(r'[一-鿿]')
    all_links = extract_wikilinks(content)
    chinese_links = []

    for target, display in all_links:
        # 检查目标或显示文本是否包含中文
        if chinese_pattern.search(target) or (display and chinese_pattern.search(display)):
            chinese_links.append((target, display))

    return chinese_links


def fix_chinese_links_in_file(filepath, dry_run=False):
    """修复单个文件中的中文链接"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixed_count = 0
    fixed_links = []

    # 查找所有wiki链接
    pattern = r'\[\[([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'

    def replace_link(match):
        nonlocal fixed_count
        target = match.group(1)
        display = match.group(2)

        # 标准化目标名用于查找
        target_normalized = target.lower().strip()

        # 检查是否在映射中
        if target_normalized in CHINESE_TO_ENGLISH:
            new_target = CHINESE_TO_ENGLISH[target_normalized]

            # 决定显示文本：优先保留原有显示文本，否则使用原始目标
            if display:
                new_display = display
            else:
                new_display = target  # 保留原始中文作为显示文本

            fixed_count += 1
            fixed_links.append((target, new_target, new_display))
            return f'[[{new_target}|{new_display}]]'

        # 如果目标不是中文但在显示文本中有中文，且目标是缩写
        elif display and re.search(r'[一-鿿]', display):
            # 检查显示文本是否在映射中
            display_normalized = display.lower().strip()
            if display_normalized in CHINESE_TO_ENGLISH:
                new_target = CHINESE_TO_ENGLISH[display_normalized]
                new_display = display
                fixed_count += 1
                fixed_links.append((target, new_target, new_display))
                return f'[[{new_target}|{new_display}]]'

        return match.group(0)

    new_content = re.sub(pattern, replace_link, content)

    if fixed_count > 0 and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return fixed_count, fixed_links, new_content != original_content


def main():
    import argparse
    parser = argparse.ArgumentParser(description='修复中文链接到英文页面')
    parser.add_argument('--dry-run', action='store_true', help='仅预览，不实际修改')
    parser.add_argument('--file', type=str, help='仅处理指定文件')
    args = parser.parse_args()

    # 统计映射覆盖率
    print("=" * 60)
    print("中文链接修复工具")
    print("=" * 60)
    print(f"\n映射字典包含 {len(CHINESE_TO_ENGLISH)} 个中文术语")
    print()

    if args.file:
        # 处理单个文件
        filepath = Path(args.file)
        if not filepath.exists():
            print(f"文件不存在: {filepath}")
            return

        fixed, links, changed = fix_chinese_links_in_file(filepath, args.dry_run)
        print(f"处理文件: {filepath}")
        print(f"修复链接数: {fixed}")
        if links:
            print("\n修复详情:")
            for old, new, display in links:
                print(f"  [[{old}]] → [[{new}|{display}]]")
    else:
        # 批量处理所有来源页
        source_files = list(SOURCES_DIR.glob("*.md"))
        print(f"扫描 {len(source_files)} 个来源页...")
        print()

        total_fixed = 0
        processed = 0
        all_fixed = []
        unmatched_chinese = Counter()

        for filepath in source_files:
            try:
                # 首先检查是否有中文链接
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                chinese_links = find_chinese_links(content)
                if not chinese_links:
                    continue

                # 修复文件
                fixed, links, changed = fix_chinese_links_in_file(filepath, args.dry_run)

                if fixed > 0:
                    total_fixed += fixed
                    all_fixed.extend(links)

                # 记录未匹配的中文链接
                for target, display in chinese_links:
                    target_normalized = target.lower().strip()
                    if target_normalized not in CHINESE_TO_ENGLISH:
                        unmatched_chinese[target] += 1

                processed += 1
                if processed % 100 == 0:
                    action = "预览" if args.dry_run else "处理"
                    print(f"{action}进度: {processed}/{len(source_files)} 文件，已修复 {total_fixed} 个链接")

            except Exception as e:
                print(f"错误处理 {filepath}: {e}")

        print()
        print("=" * 60)
        if args.dry_run:
            print("📋 预览模式 - 未实际修改文件")
        else:
            print("✅ 修复完成！")
        print("=" * 60)
        print(f"处理文件数: {processed}")
        print(f"修复链接数: {total_fixed}")

        if all_fixed:
            print()
            print("修复摘要（前30）:")
            summary = Counter(f"{old} → {new}" for old, new, _ in all_fixed)
            for mapping, count in summary.most_common(30):
                print(f"  {mapping}: {count}次")

        # 显示未匹配的中文链接
        if unmatched_chinese:
            print()
            print(f"⚠️  未匹配的中文链接（前30，共{len(unmatched_chinese)}种）:")
            for name, count in unmatched_chinese.most_common(30):
                print(f"  [[{name}]]: {count}次")
            print()
            print(f"提示: 可以将这些术语添加到 chinese_to_english_mapping.py 中")


if __name__ == "__main__":
    main()
