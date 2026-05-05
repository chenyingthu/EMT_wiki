#!/usr/bin/env python3
"""
基于关键词搜索增强分类页面
- 对每个需要增强的页面，搜索标题相关的sources
- 提取内容并增强
"""
import os
import re
import json
import glob

def load_quality_audit():
    """加载质量审计数据"""
    with open('reports/wiki_quality_audit.json', 'r') as f:
        return json.load(f)

def get_pages_needing_enrichment():
    """获取需要增强的页面"""
    audit = load_quality_audit()
    pages = []
    for page in audit:
        if page['page_type'] not in ['method', 'topic', 'model']:
            continue
        issues = page.get('issues', [])
        needs_enrich = any('short' in i.lower() or 'mathematical' in i.lower() for i in issues)
        if needs_enrich:
            pages.append(page)
    return pages

def extract_keywords(title):
    """从标题提取关键词"""
    # 清理标题
    title_clean = title.lower()
    title_clean = re.sub(r'[-_]', ' ', title_clean)

    # 技术词汇映射
    tech_terms = {
        'mmc': ['modular', 'multilevel', 'converter'],
        'vsc': ['voltage', 'source', 'converter'],
        'hvdc': ['high', 'voltage', 'direct', 'current'],
        'emt': ['electromagnetic', 'transient'],
        'lcc': ['line', 'commutated', 'converter'],
        'facts': ['flexible', 'ac', 'transmission'],
        'pwm': ['pulse', 'width', 'modulation'],
        'pll': ['phase', 'locked', 'loop'],
        'fpga': ['field', 'programmable', 'gate', 'array'],
        'gpu': ['graphics', 'processing', 'unit'],
        'hil': ['hardware', 'loop'],
        'avm': ['average', 'value', 'model'],
        'dem': ['detailed', 'equivalent', 'model'],
    }

    keywords = set()

    # 添加标题中的词汇
    words = re.findall(r'\b[a-z]+\b', title_clean)
    for w in words:
        if len(w) > 2:
            keywords.add(w)

    # 检查技术缩写
    for abbrev, expansions in tech_terms.items():
        if abbrev in title_clean:
            keywords.add(abbrev)
            keywords.update(expansions)

    return list(keywords)

def search_related_sources(keywords, max_results=3):
    """搜索相关sources"""
    if not keywords:
        return []

    sources = glob.glob('wiki/sources/*.md')
    scored = []

    for source_path in sources:
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()

            score = 0
            content_lower = content.lower()

            for kw in keywords:
                if len(kw) < 3:
                    continue
                # 标题匹配权重高
                if kw in os.path.basename(source_path).lower():
                    score += 5
                # 内容匹配
                if kw in content_lower:
                    score += 1
                # deep-review部分匹配权重更高
                if 'deep-review:start' in content:
                    review_match = re.search(r'<!-- deep-review:start -->(.+?)<!-- deep-review:end -->', content, re.DOTALL)
                    if review_match and kw in review_match.group(1).lower():
                        score += 3

            if score > 3:  # 最低阈值
                scored.append((source_path, score))
        except:
            pass

    scored.sort(key=lambda x: -x[1])
    return [p[0] for p in scored[:max_results]]

def extract_enrichable_content(source_path):
    """提取可用于增强的内容"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        extracted = {}

        # 从deep-review提取模型算法
        review_match = re.search(r'<!-- deep-review:start -->.+?### 2\. 模型、算法与实现技术\n\n(.+?)(?=###|<!--)', content, re.DOTALL)
        if review_match:
            text = review_match.group(1).strip()
            # 提取要点
            points = re.findall(r'[^.!?\n]+[.!?]', text[:1500])
            if points:
                extracted['methods'] = points[:3]

        # 从deep-enrich提取公式
        enrich_match = re.search(r'<!-- deep-enrich:start -->(.+?)<!-- deep-enrich:end -->', content, re.DOTALL)
        if enrich_match:
            equations = re.findall(r'\$[^$]+\$', enrich_match.group(1))
            if equations:
                extracted['equations'] = equations[:3]

        # 从摘要提取
        abstract_match = re.search(r'## 摘要\n\n(.+?)(?=##|<!--)', content, re.DOTALL)
        if abstract_match:
            extracted['abstract'] = abstract_match.group(1).strip()[:300]

        return extracted
    except:
        return {}

def enrich_page(target_path, content_sections, source_name):
    """增强目标页面"""
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        enhancements = []
        changed = False

        # 1. 增强EMT中的作用
        if 'methods' in content_sections and '## EMT中的作用' in content:
            if '- 待补充' in content:
                new_section = '基于相关研究的应用：\n\n'
                for i, point in enumerate(content_sections['methods'], 1):
                    clean = point.strip().replace('\n', ' ')[:120]
                    if clean:
                        new_section += f'{i}. {clean}\n\n'

                pattern = r'(## EMT中的作用\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + new_section, content)
                    enhancements.append('应用场景')
                    changed = True

        # 2. 增强形式化表达
        if 'equations' in content_sections and '## 形式化表达' in content:
            if content.count('$') < 5:
                new_section = '\n\n相关研究中的关键公式：\n\n'
                for eq in content_sections['equations']:
                    new_section += f'{eq}\n\n'

                pattern = r'(## 形式化表达\n\n)([^#]+)'
                match = re.search(pattern, content, re.DOTALL)
                if match and '待补充' in match.group(2):
                    content = content[:match.end(2)] + new_section + content[match.end(2):]
                    enhancements.append(f'{len(content_sections["equations"])}个公式')
                    changed = True

        # 3. 添加来源引用
        if '## 代表性来源' in content:
            if '- 待补充' in content:
                pattern = r'(## 代表性来源\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1- [[{}]]\n'.format(source_name), content)
                    enhancements.append('来源引用')
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
    print("基于搜索的页面增强")
    print("=" * 70)

    # 获取需要增强的页面
    pages = get_pages_needing_enrichment()
    print(f"\n需要增强的页面: {len(pages)}个")

    # 分批处理
    batch_size = 100
    processed = 0
    success = 0

    print(f"\n开始增强（本批{batch_size}个）...")

    for page in pages[200:]:  # 处理第200个之后的所有
        target_path = page['path']
        target_name = os.path.basename(target_path).replace('.md', '')

        # 提取关键词
        title = target_name.replace('-', ' ')
        keywords = extract_keywords(title)

        if not keywords:
            print(f"  - 跳过: {target_name[:40]:40s} (无关键词)")
            continue

        # 搜索相关sources
        sources = search_related_sources(keywords)

        if not sources:
            print(f"  - 跳过: {target_name[:40]:40s} (未找到相关source)")
            continue

        # 使用第一个最相关的source增强
        best_source = sources[0]
        source_name = os.path.basename(best_source).replace('.md', '')

        # 提取内容
        content_sections = extract_enrichable_content(best_source)

        if not content_sections:
            print(f"  - 跳过: {target_name[:40]:40s} (source无可用内容)")
            continue

        # 增强页面
        ok, enhancements = enrich_page(target_path, content_sections, source_name)

        if ok:
            print(f"  ✓ 增强: {target_name[:40]:40s} ← {source_name[:25]:25s} {enhancements}")
            success += 1
        else:
            print(f"  - 跳过: {target_name[:40]:40s} (无有效增强)")

        processed += 1

    print(f"\n本批结果:")
    print(f"  - 处理: {processed}个")
    print(f"  - 成功: {success}个")
    print(f"  - 剩余: {len(pages) - batch_size}个")

if __name__ == '__main__':
    main()
