#!/usr/bin/env python3
"""
清理低价值链接脚本 - 将引用1-2次的断链改为普通文本
"""
import os
import re
import sys

def get_existing_files():
    """获取所有存在的文件名"""
    existing = {}
    for root, dirs, files in os.walk('wiki'):
        for f in files:
            if f.endswith('.md'):
                name = f[:-3]
                existing[name] = os.path.join(root, f)
    return existing

def get_all_links():
    """获取所有链接及其位置"""
    links = {}
    for root, dirs, files in os.walk('wiki'):
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        for i, line in enumerate(file, 1):
                            # 匹配 [[link]] 或 [[link|text]]
                            matches = re.findall(r'\[\[([^\]|]+)(?:\|([^\]]*))?\]\]', line)
                            for match in matches:
                                link = match[0].strip()
                                display = match[1].strip() if match[1] else link
                                if link not in links:
                                    links[link] = []
                                links[link].append((filepath, i, line, display))
                except:
                    pass
    return links

def find_broken_links(links, existing):
    """找出断链"""
    broken = {}
    for link, locations in links.items():
        if link not in existing:
            broken[link] = locations
    return broken

def cleanup_low_value_links(broken_links, max_refs=2):
    """清理低价值链接（引用次数<=max_refs）"""
    low_value_links = {k: v for k, v in broken_links.items() if len(v) <= max_refs}

    total_cleaned = 0
    files_modified = set()

    for link, locations in low_value_links.items():
        for filepath, line_num, line_content, display in locations:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换 [[link]] 或 [[link|display]] 为普通文本
                # 如果有display text，保留display text
                if display:
                    # 处理 [[link|display]] 格式
                    new_content = content.replace(f'[[{link}|{display}]]', display)
                else:
                    # 处理 [[link]] 格式
                    new_content = content.replace(f'[[{link}]]', link)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    total_cleaned += 1
                    files_modified.add(filepath)
            except Exception as e:
                print(f"  清理失败 {filepath}:{line_num}: {e}")

    return total_cleaned, len(files_modified), len(low_value_links)

def main():
    print("=" * 60)
    print("清理低价值链接脚本 (引用<=2)")
    print("=" * 60)

    existing = get_existing_files()
    print(f"现有页面数: {len(existing)}")

    links = get_all_links()
    print(f"总链接数: {len(links)}")

    broken = find_broken_links(links, existing)
    print(f"断链数: {len(broken)}")

    # 统计
    low_value = {k: v for k, v in broken.items() if len(v) <= 2}
    print(f"低价值断链(<=2引用): {len(low_value)}个")

    print("\n开始清理...")
    total_cleaned, files_modified, total_links = cleanup_low_value_links(broken, max_refs=2)

    print(f"\n清理完成:")
    print(f"  - 处理链接数: {total_links}")
    print(f"  - 清理次数: {total_cleaned}")
    print(f"  - 修改文件数: {files_modified}")

    # 再次检查
    print("\n再次检查断链...")
    links = get_all_links()
    broken = find_broken_links(links, existing)
    print(f"剩余断链数: {len(broken)}")

    return len(broken)

if __name__ == '__main__':
    remaining = main()
    sys.exit(0 if remaining == 0 else 1)
