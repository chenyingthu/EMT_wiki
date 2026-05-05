#!/usr/bin/env python3
"""
基于Sources内容增强Method/Topic/Model页面
- 提取Sources中的公式、方法、发现
- 用于增强分类页面的内容深度
"""
import os
import re
import json
import glob
from collections import Counter

def load_quality_audit():
    """加载质量审计数据"""
    with open('reports/wiki_quality_audit.json', 'r') as f:
        return json.load(f)

def get_pages_with_issues(audit_data, issue_patterns):
    """获取有特定问题的页面"""
    pages = []
    for page in audit_data:
        issues = page.get('issues', [])
        for issue in issues:
            if any(pattern in issue.lower() for pattern in issue_patterns):
                pages.append(page)
                break
    return pages

def extract_math_from_source(source_path):
    """从source页面提取数学公式"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        equations = []

        # 提取LaTeX行内公式 $...$
        inline = re.findall(r'\$[^\$]+\$', content)
        equations.extend(inline[:5])  # 最多5个

        # 提取LaTeX块公式 $$...$$
        blocks = re.findall(r'\$\$[^\$]+\$\$', content)
        equations.extend(blocks[:3])  # 最多3个

        return equations
    except:
        return []

def extract_methods_from_source(source_path):
    """从source页面提取方法描述"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        methods = []

        # 查找方法细节部分
        method_match = re.search(r'## 方法细节\n\n([^#]+)', content)
        if method_match:
            methods.append(method_match.group(1).strip()[:500])

        # 查找核心贡献
        contrib_match = re.search(r'## 核心贡献\n\n([^#]+)', content)
        if contrib_match:
            methods.append(contrib_match.group(1).strip()[:500])

        return methods
    except:
        return []

def find_related_sources(target_path, target_title, audit_data, max_sources=3):
    """查找与目标页面相关的sources"""
    related = []

    # 1. 从标题提取关键词
    keywords = set(re.findall(r'[\w\-]+', target_title.lower()))
    keywords.discard('model')
    keywords.discard('method')
    keywords.discard('system')
    keywords.discard('the')
    keywords.discard('and')

    # 2. 从目标页面内容提取现有的wikilinks作为关键词
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 提取所有wikilinks
        wikilinks = re.findall(r'\[\[([^\]|]+)', content)
        for link in wikilinks:
            link_keywords = re.findall(r'[\w\-]+', link.lower())
            keywords.update(link_keywords)
    except:
        pass

    # 3. 特定主题的关键词扩展
    topic_keywords = {
        'mmc': ['modular', 'multilevel', 'converter', 'hvdc'],
        'vsc': ['voltage', 'source', 'converter', 'hvdc'],
        'emt': ['electromagnetic', 'transient', 'simulation'],
        'transformer': ['transformer', 'saturation', 'inrush'],
        'fault': ['fault', 'protection', 'relay'],
        'parallel': ['parallel', 'gpu', 'cuda', 'multicore'],
        'hil': ['hardware', 'loop', 'realtime'],
    }

    for key, extra_kws in topic_keywords.items():
        if key in target_title.lower():
            keywords.update(extra_kws)

    # 4. 遍历所有source进行匹配
    for page in audit_data:
        if page['page_type'] != 'source':
            continue

        # 检查标题匹配
        page_title = os.path.basename(page['path']).lower()
        score = 0
        for kw in keywords:
            if len(kw) > 2 and kw in page_title:  # 只匹配长度>2的关键词
                score += 1

        # 也检查source的tags
        try:
            with open(page['path'], 'r', encoding='utf-8') as f:
                content = f.read()
            # 提取frontmatter中的tags
            tags_match = re.search(r'tags:\s*\[([^\]]+)\]', content)
            if tags_match:
                tags = tags_match.group(1).lower()
                for kw in keywords:
                    if len(kw) > 2 and kw in tags:
                        score += 2  # tags匹配权重更高
        except:
            pass

        if score > 0:
            related.append((page, score))

    # 按相关性排序
    related.sort(key=lambda x: -x[1])
    return [p[0] for p in related[:max_sources]]

def enhance_page(target_path, target_page, related_sources):
    """增强目标页面的内容"""
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        enhancements = []

        # 从sources收集内容
        all_equations = []
        all_methods = []

        for source in related_sources:
            source_path = source['path']
            equations = extract_math_from_source(source_path)
            methods = extract_methods_from_source(source_path)
            all_equations.extend(equations)
            all_methods.extend(methods)

        changed = False

        # 1. 如果有公式，添加到形式化表达部分
        if all_equations and '## 形式化表达' in content:
            # 检查是否已经有公式（避免重复）
            if content.count('$') < 5:  # 如果公式很少
                math_section = '\n### 基于相关研究的公式表达\n\n'
                for i, eq in enumerate(all_equations[:3], 1):
                    math_section += f'**公式{i}**: {eq}\n\n'

                # 找到"形式化表达"部分并替换"待补充"
                pattern = r'(## 形式化表达\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + math_section, content)
                    enhancements.append(f'添加了{len(all_equations[:3])}个公式')
                    changed = True

        # 2. 如果有方法描述，添加到EMT中的作用部分
        if all_methods and '## EMT中的作用' in content:
            if '- 待补充' in content:  # 只在未补充时添加
                method_section = '\n基于相关研究的应用：\n\n'
                for i, method in enumerate(all_methods[:2], 1):
                    # 清理方法文本
                    clean_method = method.replace('\n', ' ').strip()[:150]
                    method_section += f'{i}. {clean_method}...\n\n'

                pattern = r'(## EMT中的作用\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + method_section, content)
                    enhancements.append(f'添加了{len(all_methods[:2])}个应用描述')
                    changed = True

        # 3. 添加相关来源引用
        if related_sources and '## 代表性来源' in content:
            if '- 待补充' in content:  # 只在未补充时添加
                source_section = '\n'
                for source in related_sources[:3]:
                    source_name = os.path.basename(source['path']).replace('.md', '')
                    source_section += f'- [[{source_name}]]\n'

                pattern = r'(## 代表性来源\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + source_section, content)
                    enhancements.append(f'添加了{len(related_sources[:3])}个来源引用')
                    changed = True

        if changed and content != original:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, enhancements

    except Exception as e:
        return False, [str(e)]

    return False, []

def main():
    print("=" * 70)
    print("基于Sources内容增强分类页面")
    print("=" * 70)

    audit_data = load_quality_audit()

    # 获取需要增强的method/topic/model页面
    target_pages = get_pages_with_issues(audit_data, [
        'short',
        'mathematical form'
    ])

    # 只处理method/topic/model
    target_pages = [p for p in target_pages if p['page_type'] in ['method', 'topic', 'model']]

    print(f"\n发现 {len(target_pages)} 个需要增强的分类页面")

    # 分批处理
    batch_size = 50
    processed = 0
    success = 0

    print(f"\n开始增强（本批处理{batch_size}个）...")

    for page in target_pages[:batch_size]:
        target_path = page['path']
        target_title = os.path.basename(target_path).replace('.md', '')

        # 查找相关sources
        related_sources = find_related_sources(target_path, target_title, audit_data)

        if related_sources:
            ok, enhancements = enhance_page(target_path, page, related_sources)
            if ok:
                print(f"  ✓ 增强: {target_title}")
                for e in enhancements:
                    print(f"      - {e}")
                success += 1
            else:
                print(f"  - 跳过: {target_title} (无有效增强)")
        else:
            print(f"  - 跳过: {target_title} (未找到相关source)")

        processed += 1

    print(f"\n本批处理: {processed} 个")
    print(f"成功增强: {success} 个")
    print(f"剩余待处理: {len(target_pages) - processed} 个")

if __name__ == '__main__':
    main()
