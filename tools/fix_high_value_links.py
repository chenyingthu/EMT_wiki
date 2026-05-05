#!/usr/bin/env python3
"""
高价值断链修复脚本 - 只修复引用次数>=3的断链
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

def should_create_page(link_name):
    """判断是否应该为此链接创建页面"""
    generic_words = {'wikilink', 'link', 'page', 'url', 'ref', 'note', 'source', 'file'}
    if link_name.lower() in generic_words:
        return False
    if len(link_name) < 3:
        return False
    if link_name.isdigit():
        return False
    return True

def create_stub_page(link_name, link_type='method'):
    """创建一个stub页面"""
    if not should_create_page(link_name):
        return False, "Filtered by generic word filter"

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

    # 中文链接
    if any('一' <= c <= '鿿' for c in link_name):
        title = link_name
    else:
        title = link_name.replace('-', ' ').title()

    content = f"""---
title: "{title}"
type: {link_type}
tags: [{link_name.lower().replace(' ', '-')}, high-value-link]
created: "2026-05-05"
---

# {title}

## 定义与边界

本页面为高价值断链修复页面（被引用≥3次），用于建立wiki内部连接网络。

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

*本页面为高价值断链自动修复生成，需要进一步补充完善。*
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
    print("高价值断链修复脚本 (引用>=3)")
    print("=" * 60)

    existing = get_existing_files()
    print(f"现有页面数: {len(existing)}")

    links = get_all_links()
    print(f"总链接数: {len(links)}")

    broken = find_broken_links(links, existing)
    print(f"断链数: {len(broken)}")

    # 只处理高引用断链(>=3)
    high_value_broken = {k: v for k, v in broken.items() if len(v) >= 3}
    print(f"高价值断链数(>=3引用): {len(high_value_broken)}")

    if not high_value_broken:
        print("\n✓ 没有高价值断链需要修复！")
        return 0

    # 按引用次数排序（从高到低）
    sorted_broken = sorted(high_value_broken.items(), key=lambda x: len(x[1]), reverse=True)

    # 每次处理5个
    batch_size = 5
    processed = 0

    print(f"\n开始创建stub页面（本次最多{batch_size}个）...")

    for link_name, locations in sorted_broken[:batch_size]:
        success, result = create_stub_page(link_name)
        if success:
            print(f"  ✓ 创建: {link_name} ({len(locations)}次引用)")
            processed += 1
        else:
            print(f"  ✗ 失败: {link_name} - {result}")

    print(f"\n本批次共处理: {processed} 个高价值断链")
    print(f"剩余高价值断链: {len(high_value_broken) - processed} 个")
    print(f"总断链数: {len(broken)} 个")

    return len(high_value_broken) - processed

if __name__ == '__main__':
    remaining = main()
    sys.exit(0 if remaining == 0 else 1)
