#!/usr/bin/env python3
"""
断链修复脚本 - 每次修复5个断链
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
    links = {}  # link -> [(filepath, line_num, line_content), ...]
    for root, dirs, files in os.walk('wiki'):
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        for i, line in enumerate(file, 1):
                            # 匹配 [[link]] 或 [[link|text]]，提取link部分
                            matches = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', line)
                            for match in matches:
                                link = match.strip()
                                if link not in links:
                                    links[link] = []
                                links[link].append((filepath, i, line))
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

def fix_backslash_links(links_dict, existing):
    """修复带反斜杠的链接"""
    fixed = 0
    for link in list(links_dict.keys()):
        if '\\' in link:
            clean_link = link.replace('\\', '')
            if clean_link in existing:
                # 修复所有出现的位置
                for filepath, line_num, line_content in links_dict[link]:
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        # 替换链接
                        new_content = content.replace(f'[[{link}', f'[[{clean_link}')
                        if new_content != content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            fixed += 1
                    except Exception as e:
                        print(f"  修复失败 {filepath}: {e}")
    return fixed

def create_stub_page(link_name, link_type='method'):
    """创建一个stub页面"""
    # 根据链接名称确定类型
    if any(kw in link_name for kw in ['model', 'machine', 'transformer', 'inverter', 'mmc', 'vsc', 'lcc']):
        link_type = 'model'
        folder = 'wiki/models'
    elif any(kw in link_name for kw in ['topic', 'analysis', 'simulation', 'system']):
        link_type = 'topic'
        folder = 'wiki/topics'
    else:
        link_type = 'method'
        folder = 'wiki/methods'

    # 检查是否已有相似页面
    existing_files = get_existing_files()

    # 中文链接 - 创建stub页面
    if any('一' <= c <= '鿿' for c in link_name):
        title = link_name
    else:
        title = link_name.replace('-', ' ').title()

    content = f"""---
title: "{title}"
type: {link_type}
tags: [{link_name.lower().replace(' ', '-')}]
created: "2026-05-04"
---

# {title}

## 定义与边界

本页面为自动创建的{link_type}类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充

## 主要分支与机制

- 待补充

## 形式化表达

- 待补充

## 适用边界与失败模式

- 待补充

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础

## 代表性来源

- 待补充

---

*本页面为自动生成的stub，需要进一步补充完善。*
"""

    filepath = os.path.join(folder, f"{link_name}.md")
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, filepath
    except Exception as e:
        return False, str(e)

def main():
    print("=" * 60)
    print("断链修复脚本 - 批次修复")
    print("=" * 60)

    existing = get_existing_files()
    print(f"现有页面数: {len(existing)}")

    links = get_all_links()
    print(f"总链接数: {len(links)}")

    broken = find_broken_links(links, existing)
    print(f"断链数: {len(broken)}")

    if not broken:
        print("\n✓ 没有断链需要修复！")
        return 0

    # 优先修复带反斜杠的链接
    print("\n步骤1: 修复带反斜杠的链接...")
    fixed_backslash = fix_backslash_links(broken, existing)
    print(f"  修复了 {fixed_backslash} 个反斜杠链接")

    # 重新获取断链列表
    existing = get_existing_files()
    links = get_all_links()
    broken = find_broken_links(links, existing)

    # 按优先级排序断链
    # 1. 英文断链（较易处理）
    # 2. 中文断链
    english_broken = [(k, v) for k, v in broken.items() if not any('一' <= c <= '鿿' for c in k)]
    chinese_broken = [(k, v) for k, v in broken.items() if any('一' <= c <= '鿿' for c in k)]

    # 每次处理5个
    batch_size = 5
    processed = 0

    print(f"\n步骤2: 创建stub页面（本次最多{batch_size}个）...")

    # 优先处理英文断链
    for link_name, locations in english_broken[:batch_size]:
        success, result = create_stub_page(link_name)
        if success:
            print(f"  ✓ 创建: {link_name}")
            processed += 1
        else:
            print(f"  ✗ 失败: {link_name} - {result}")

    # 如果有剩余配额，处理中文断链
    remaining = batch_size - processed
    if remaining > 0:
        for link_name, locations in chinese_broken[:remaining]:
            success, result = create_stub_page(link_name)
            if success:
                print(f"  ✓ 创建: {link_name}")
                processed += 1
            else:
                print(f"  ✗ 失败: {link_name} - {result}")

    print(f"\n本批次共处理: {processed} 个断链")
    print(f"剩余断链: {len(broken) - processed} 个")

    return len(broken) - processed  # 返回剩余断链数

if __name__ == '__main__':
    remaining = main()
    sys.exit(0 if remaining == 0 else 1)
