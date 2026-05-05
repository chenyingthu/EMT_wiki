#!/usr/bin/env python3
"""
内容分发策略 - 将Sources内容分发到相关分类页面
"""
import os
import re
import json
import glob

def load_quality_audit():
    """加载质量审计数据"""
    with open('reports/wiki_quality_audit.json', 'r') as f:
        return {p['path']: p for p in json.load(f)}

def get_method_pages_needing_enrichment(audit_data):
    """获取需要增强的method/topic/model页面"""
    pages = []
    for path, page in audit_data.items():
        if page['page_type'] not in ['method', 'topic', 'model']:
            continue
        issues = page.get('issues', [])
        needs_enrich = any('short' in i.lower() or 'mathematical' in i.lower() for i in issues)
        if needs_enrich:
            pages.append((path, page))
    return pages

def extract_content_sections(source_path):
    """从source提取各个内容章节"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        sections = {}

        # 1. 从 deep-review 提取方法描述（最详细）
        review_match = re.search(r'<!-- deep-review:start -->\n## 研究解读(.*?)<!-- deep-review:end -->', content, re.DOTALL)
        if review_match:
            review_text = review_match.group(1)

            # 提取模型算法部分
            model_match = re.search(r'### 2\. 模型、算法与实现技术\n\n(.+?)(?=###|<!--)', review_text, re.DOTALL)
            if model_match:
                sections['methods'] = model_match.group(1).strip()[:1000]

            # 提取验证优势部分
            validation_match = re.search(r'### 3\. 验证、优势与不足\n\n(.+?)(?=###|<!--)', review_text, re.DOTALL)
            if validation_match:
                sections['validation'] = validation_match.group(1).strip()[:800]

        # 2. 从 deep-enrich 提取公式
        enrich_match = re.search(r'<!-- deep-enrich:start -->(.*?)<!-- deep-enrich:end -->', content, re.DOTALL)
        if enrich_match:
            enrich_text = enrich_match.group(1)
            # 提取公式
            equations = re.findall(r'\$[^$]+\$', enrich_text)
            if equations:
                sections['formal'] = '\n'.join(equations[:5])

        # 3. 从摘要提取基本信息
        abstract_match = re.search(r'## 摘要\n\n(.+?)(?=##|<!--)', content, re.DOTALL)
        if abstract_match:
            sections['abstract'] = abstract_match.group(1).strip()[:500]

        # 4. 提取使用的标签（用于匹配）
        tags_match = re.search(r'tags:\s*\[([^\]]+)\]', content)
        if tags_match:
            sections['tags'] = [t.strip().strip("'\"") for t in tags_match.group(1).split(',')]

        # 5. 从标题提取更多关键词
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
            # 提取技术关键词
            keywords = re.findall(r'[A-Z]{2,}|\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', title)
            sections['title_keywords'] = keywords

        return sections
    except Exception as e:
        return {}

def score_relevance(target_path, target_page, source_sections):
    """计算source与目标页面的相关度分数"""
    score = 0

    # 1. 文件名匹配
    target_name = os.path.basename(target_path).replace('.md', '').lower()
    source_tags = source_sections.get('tags', [])

    for tag in source_tags:
        tag_clean = tag.lower().replace('-', '').replace('_', '')
        target_clean = target_name.lower().replace('-', '').replace('_', '')

        # 完全匹配
        if tag_clean == target_clean:
            score += 10
        # 包含匹配
        elif tag_clean in target_clean or target_clean in tag_clean:
            score += 5
        # 关键词匹配（如 mmc 和 modular-multilevel-converter）
        elif len(tag_clean) > 3:
            for part in target_clean.split('-'):
                if len(part) > 2 and part in tag_clean:
                    score += 2

    return score

def enrich_page_with_content(target_path, target_page, source_path, source_sections):
    """使用source内容增强目标页面"""
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        enhancements = []
        changed = False

        # 1. 添加方法细节到EMT中的作用
        if 'methods' in source_sections and '## EMT中的作用' in content:
            if '- 待补充' in content or '待补充' in content:
                method_text = source_sections['methods']
                # 提取要点
                points = re.findall(r'- (.+?)(?=\n|$)', method_text)
                if points:
                    new_section = '基于相关研究的应用场景：\n\n'
                    for p in points[:3]:
                        new_section += f'- {p[:150]}...\n'

                    # 替换待补充
                    pattern = r'(## EMT中的作用\n\n)(- 待补充\n*)'
                    if re.search(pattern, content):
                        content = re.sub(pattern, r'\1' + new_section + '\n', content)
                        enhancements.append('EMT作用')
                        changed = True

        # 2. 添加公式到形式化表达
        if 'formal' in source_sections and '## 形式化表达' in content:
            if content.count('$') < 5:  # 公式很少
                formal_text = source_sections['formal']
                # 提取公式
                equations = re.findall(r'\$[^$]+\$', formal_text)
                if equations:
                    new_section = '\n从相关研究提取的关键公式：\n\n'
                    for i, eq in enumerate(equations[:3], 1):
                        new_section += f'{eq}\n\n'

                    pattern = r'(## 形式化表达\n\n)([^#]+)'
                    match = re.search(pattern, content)
                    if match and '待补充' in match.group(2):
                        content = content[:match.end(2)] + new_section + content[match.end(2):]
                        enhancements.append(f'{len(equations[:3])}个公式')
                        changed = True

        # 3. 添加量化发现
        if 'quantitative' in source_sections:
            quant_text = source_sections['quantitative']
            # 提取数值
            numbers = re.findall(r'[\d.]+\s*(?:ms|us|s|kV|V|MW|kW|Hz|%|pu)', quant_text)
            if numbers and '## 主要发现' not in content:
                # 在形式化表达后添加
                new_section = f'\n### 关键参数\n\n从相关研究提取的量化指标：\n'
                for n in numbers[:5]:
                    new_section += f'- {n}\n'

                if '形式化表达' in content:
                    # 找到形式化表达部分结尾
                    pattern = r'(## 形式化表达\n\n[^#]+)'
                    match = re.search(pattern, content, re.DOTALL)
                    if match:
                        end_pos = match.end()
                        content = content[:end_pos] + new_section + '\n' + content[end_pos:]
                        enhancements.append('量化参数')
                        changed = True

        # 4. 添加来源引用
        if '## 代表性来源' in content:
            if '- 待补充' in content:
                source_name = os.path.basename(source_path).replace('.md', '')
                pattern = r'(## 代表性来源\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + f'- [[{source_name}]]\n', content)
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
    print("内容分发增强 - 基于Sources分发内容到分类页面")
    print("=" * 70)

    audit_data = load_quality_audit()

    # 获取需要增强的分类页面
    target_pages = get_method_pages_needing_enrichment(audit_data)
    print(f"\n需要增强的分类页面: {len(target_pages)}个")

    # 获取所有sources
    source_files = glob.glob('wiki/sources/*.md')
    print(f"可用Sources: {len(source_files)}个")

    # 处理策略：对每个source，找到最相关的3个目标页面进行增强
    batch_size = 20  # 每批处理20个sources
    processed = 0
    success = 0

    print(f"\n开始内容分发（本批处理{batch_size}个Sources）...")

    for source_path in source_files[:batch_size]:
        source_name = os.path.basename(source_path)

        # 提取source内容
        sections = extract_content_sections(source_path)
        if not sections:
            continue

        # 计算与所有目标页面的相关度
        scored_targets = []
        for target_path, target_page in target_pages:
            score = score_relevance(target_path, target_page, sections)
            if score > 5:  # 只考虑相关度>5的
                scored_targets.append((target_path, target_page, score))

        # 按相关度排序
        scored_targets.sort(key=lambda x: -x[2])

        # 增强最相关的1-2个页面
        enhanced_count = 0
        for target_path, target_page, score in scored_targets[:2]:
            ok, enhancements = enrich_page_with_content(
                target_path, target_page, source_path, sections
            )
            if ok:
                target_name = os.path.basename(target_path)
                print(f"  ✓ {source_name[:40]:40s} → {target_name[:30]:30s} (score:{score}) {enhancements}")
                success += 1
                enhanced_count += 1

        if enhanced_count > 0:
            processed += 1

    print(f"\n本批处理:")
    print(f"  - 处理Sources: {batch_size}个")
    print(f"  - 成功分发: {processed}个sources")
    print(f"  - 增强页面: {success}次")

if __name__ == '__main__':
    main()
