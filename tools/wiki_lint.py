#!/usr/bin/env python3
"""
Wiki Lint Tool - 检查EMT Wiki的链接准确性和页面健康状态
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki")
REPORTS_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/reports")

def extract_wiki_links(content):
    """提取wiki链接 [[link|display]] 或 [[link]]"""
    # 匹配 [[link|display]] 或 [[link]] 格式
    # 处理转义的 \| 作为分隔符的情况
    pattern = r'\[\[([^\]]+?)(?:\\?\|[^\]]*?)?\]\]'
    matches = re.findall(pattern, content)
    # 清理链接名称（去除转义和处理末尾反斜杠）
    cleaned = []
    for m in matches:
        # 移除末尾的反斜杠（来自转义的 \|）
        link = m.rstrip('\\').strip()
        # 如果包含转义的 \|，只取链接部分
        if '\\|' in link:
            link = link.split('\\|')[0].strip()
        cleaned.append(link)
    return cleaned

def get_all_wiki_pages():
    """获取所有wiki页面文件路径和对应的链接名称"""
    pages = {}
    for md_file in WIKI_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(WIKI_DIR)
        # 链接名称: 去掉.md后缀，路径分隔符用/
        # 对于子目录中的文件，链接名包含目录前缀如 "topics/co-simulation"
        link_name = str(rel_path.with_suffix('')).replace('\\', '/')
        pages[link_name] = md_file
    return pages

def resolve_link(link_name, pages):
    """
    解析链接到实际页面路径
    尝试多种匹配策略:
    1. 直接匹配 (如: topics/co-simulation)
    2. 在categories中查找 (如: co-simulation -> topics/co-simulation)
    """
    categories = ['topics', 'methods', 'models', 'entities', 'sources']

    # 1. 直接匹配
    if link_name in pages:
        return link_name

    # 2. 在各分类目录中查找
    for cat in categories:
        full_path = f"{cat}/{link_name}"
        if full_path in pages:
            return full_path

    # 3. 尝试子目录链接 (如 methods/vector-fitting 中的 vector-fitting 链接)
    # 返回原始名称作为失败标记
    return None

def check_links():
    """检查所有链接"""
    pages = get_all_wiki_pages()
    print(f"总共发现 {len(pages)} 个wiki页面")

    # 反向链接映射: page -> list of pages linking to it
    backlinks = defaultdict(list)
    # 断链统计
    broken_links = []
    # 所有链接统计
    all_links = []

    for link_name, md_file in pages.items():
        content = md_file.read_text(encoding='utf-8')
        links = extract_wiki_links(content)

        for link in links:
            all_links.append({
                'from': link_name,
                'to': link,
                'file': str(md_file)
            })

            # 尝试解析链接
            resolved = resolve_link(link, pages)
            if resolved:
                backlinks[resolved].append(link_name)
            else:
                broken_links.append({
                    'from': link_name,
                    'to': link,
                    'file': str(md_file)
                })

    # 找出孤立页面（没有入链的页面）
    orphaned = []
    for link_name in pages.keys():
        # 排除index, overview, log等核心页面
        if link_name not in ['index', 'overview', 'log'] and not backlinks[link_name]:
            orphaned.append(link_name)

    return {
        'total_pages': len(pages),
        'total_links': len(all_links),
        'broken_links': broken_links,
        'orphaned_pages': orphaned,
        'backlinks': dict(backlinks),
        'all_pages': list(pages.keys())
    }

def check_topics_methods_models_entities():
    """检查分类页面的反向引用完整性"""
    results = {
        'topics': [],
        'methods': [],
        'models': [],
        'entities': []
    }

    for category in ['topics', 'methods', 'models', 'entities']:
        category_dir = WIKI_DIR / category
        if category_dir.exists():
            for md_file in category_dir.glob("*.md"):
                link_name = f"{category}/{md_file.stem}"
                results[category].append(link_name)

    return results

def main():
    print("=" * 60)
    print("EMT Wiki Lint Report")
    print("=" * 60)

    # 运行链接检查
    results = check_links()

    print(f"\n📊 统计概览:")
    print(f"  - 总页面数: {results['total_pages']}")
    print(f"  - 总链接数: {results['total_links']}")
    print(f"  - 断链数量: {len(results['broken_links'])}")
    print(f"  - 孤立页面: {len(results['orphaned_pages'])}")

    # 断链详情
    if results['broken_links']:
        print(f"\n❌ 断链详情 (前20个):")
        for i, link in enumerate(results['broken_links'][:20], 1):
            print(f"  {i}. [[{link['to']}]] 从 {link['from']} 引用")

    # 孤立页面
    if results['orphaned_pages']:
        print(f"\n⚠️ 孤立页面 (前20个，无入链):")
        for i, page in enumerate(results['orphaned_pages'][:20], 1):
            print(f"  {i}. [[{page}]]")

    # 分类页面统计
    categories = check_topics_methods_models_entities()
    print(f"\n📁 分类页面统计:")
    for cat, pages in categories.items():
        print(f"  - {cat}: {len(pages)} 个页面")

    # 保存详细报告
    REPORTS_DIR.mkdir(exist_ok=True)
    report_file = REPORTS_DIR / "wiki_lint_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 详细报告已保存: {report_file}")

    # 返回状态码
    if results['broken_links'] or results['orphaned_pages']:
        print("\n⚠️ 发现需要修复的问题")
        return 1
    else:
        print("\n✅ 所有检查通过")
        return 0

if __name__ == "__main__":
    exit(main())
