#!/usr/bin/env python3
"""
修复审计发现的问题
- 修复缺失的wikilinks
- 增强内部链接
"""
import os
import re
import json
import glob

def get_existing_files():
    """获取所有存在的文件名"""
    existing = {}
    for root, dirs, files in os.walk('wiki'):
        for f in files:
            if f.endswith('.md'):
                name = f[:-3]
                existing[name] = os.path.join(root, f)
    return existing

def find_missing_links(filepath):
    """找出文件中缺失的wikilinks"""
    existing = get_existing_files()
    missing = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 匹配所有wikilinks
        matches = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', content)
        for match in matches:
            link = match.strip()
            if link not in existing:
                missing.append(link)
    except:
        pass

    return missing

def fix_missing_links(filepath, missing_links):
    """修复缺失的wikilinks - 改为普通文本"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for link in missing_links:
            # 替换 [[link]] 为普通文本
            content = re.sub(rf'\[\[{re.escape(link)}\]\]', link, content)
            # 替换 [[link|display]] 为 display
            content = re.sub(rf'\[\[{re.escape(link)}\|([^\]]+)\]\]', r'\1', content)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"  修复失败 {filepath}: {e}")

    return False

def enhance_internal_links(filepath):
    """增强内部链接 - 添加相关页面引用"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已有足够链接
        existing_links = re.findall(r'\[\[[^\]]+\]\]', content)
        if len(existing_links) >= 5:
            return False  # 已有足够链接

        # 解析标题
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if not title_match:
            return False

        title = title_match.group(1).strip()

        # 根据标题推荐相关页面
        related_pages = suggest_related_pages(title)

        # 查找"与相关页面的关系"部分
        section_match = re.search(r'(## 与相关页面的关系\n\n)([^#]+)', content)
        if section_match:
            section_start = section_match.start(2)
            section_end = section_match.end(2)
            current_section = section_match.group(2)

            # 添加新链接
            new_links = []
            for page in related_pages[:3]:  # 最多添加3个
                if page not in content:
                    new_links.append(f'- [[{page}]]\n')

            if new_links:
                new_section = current_section.rstrip() + '\n' + ''.join(new_links)
                content = content[:section_start] + new_section + content[section_end:]

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True

    except Exception as e:
        print(f"  增强失败 {filepath}: {e}")

    return False

def suggest_related_pages(title):
    """根据标题推荐相关页面"""
    # 知识图谱映射
    related = {
        '电力系统网络': ['transmission-network', 'nodal-analysis', 'power-flow'],
        'EMT': ['emt-simulation', 'numerical-integration', 'transient-analysis'],
        '仿真': ['real-time-simulation', 'hil-simulation', 'co-simulation'],
        'MMC': ['mmc-model', 'modular-multilevel-converter', 'vsc-hvdc'],
        '变压器': ['transformer-model', 'magnetic-saturation-modeling'],
        '线路': ['transmission-line-model', 'cable-model', 'pi-model'],
        '故障': ['fault-analysis-methods', 'protection-relay-modeling'],
        '控制': ['control-system', 'vsc-control', 'pll-design'],
        '并行': ['parallel-computing', 'gpu-accelerated-simulation'],
    }

    suggestions = []
    for keyword, pages in related.items():
        if keyword in title or keyword in title.lower():
            suggestions.extend(pages)

    # 默认建议
    defaults = ['emt-simulation', 'power-system', 'electromagnetic-transient']

    return suggestions + defaults

def main():
    print("=" * 60)
    print("修复审计问题脚本")
    print("=" * 60)

    # 读取审计报告
    with open('reports/wiki_strict_audit.json', 'r') as f:
        audit_data = json.load(f)

    # 统计需要修复的页面
    pages_with_missing = []
    pages_with_weak = []

    for item in audit_data:
        path = item['path']
        if 'issues' in item:
            if any('missing wikilinks' in issue for issue in item['issues']):
                pages_with_missing.append(path)
            if any('weak internal linking' in issue for issue in item['issues']):
                pages_with_weak.append(path)

    print(f"\n发现 {len(pages_with_missing)} 个页面有缺失链接")
    print(f"发现 {len(pages_with_weak)} 个页面需要增强内部链接")

    # 1. 修复缺失链接
    print("\n步骤1: 修复缺失链接...")
    fixed_missing = 0
    for filepath in pages_with_missing:  # 处理所有
        missing = find_missing_links(filepath)
        if missing and fix_missing_links(filepath, missing):
            print(f"  ✓ 修复: {os.path.basename(filepath)} ({len(missing)}个链接)")
            fixed_missing += 1

    # 2. 增强内部链接
    print("\n步骤2: 增强内部链接...")
    enhanced = 0
    for filepath in pages_with_weak:  # 处理所有
        if enhance_internal_links(filepath):
            print(f"  ✓ 增强: {os.path.basename(filepath)}")
            enhanced += 1

    print(f"\n修复完成:")
    print(f"  - 修复缺失链接: {fixed_missing} 个页面")
    print(f"  - 增强内部链接: {enhanced} 个页面")

if __name__ == '__main__':
    main()
