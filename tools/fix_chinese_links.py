#!/usr/bin/env python3
"""
批量修复 sources/ 目录中的中文概念链接
将 [[中文概念]] 转换为纯文本 中文概念
"""

import json
import re
from pathlib import Path

WIKI_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki")
REPORT_FILE = Path("/home/chenying/researches/EMT_LLM_Wiki/reports/wiki_lint_report.json")


def is_chinese(text):
    """检查文本是否包含中文字符"""
    return any(ord(c) > 127 for c in text)


def fix_chinese_links_in_file(filepath, chinese_targets):
    """修复单个文件中的中文链接"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixed_count = 0

    for target in chinese_targets:
        # 处理带显示文本的链接 [[目标|显示文本]]
        # 处理无显示文本的链接 [[目标]]
        patterns = [
            (rf'\[\[{re.escape(target)}\\?\|([^\]]+)\]\]', r'\1'),  # [[目标|显示]] → 显示
            (rf'\[\[{re.escape(target)}\]\]', target),  # [[目标]] → 目标
        ]

        for pattern, replacement in patterns:
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                fixed_count += len(matches)

    if fixed_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return fixed_count


def main():
    # 读取 lint 报告
    with open(REPORT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 筛选 sources/ 目录中的中文链接
    chinese_links = [l for l in data['broken_links']
                     if l['from'].startswith('sources/') and is_chinese(l['to'])]

    print(f"发现 {len(chinese_links)} 个中文概念链接需要修复")

    # 按文件分组
    from collections import defaultdict
    by_file = defaultdict(set)
    for link in chinese_links:
        by_file[link['file']].add(link['to'])

    print(f"分布在 {len(by_file)} 个文件中")
    print()

    # 逐个文件修复
    total_fixed = 0
    processed = 0

    for filepath, targets in by_file.items():
        try:
            fixed = fix_chinese_links_in_file(filepath, targets)
            total_fixed += fixed
            processed += 1

            if fixed > 0 and processed % 50 == 0:
                print(f"进度: {processed}/{len(by_file)} 文件，已修复 {total_fixed} 个链接")

        except Exception as e:
            print(f"错误处理 {filepath}: {e}")

    print()
    print(f"✅ 完成！处理了 {processed} 个文件，共修复 {total_fixed} 个中文链接")


if __name__ == "__main__":
    main()
