#!/usr/bin/env python3
"""
C级页面深度增强脚本 v2
- 从Sources提取数学公式、验证详情、边界限定
- 添加形式化表达、量化证据、适用边界
- 真正提升页面质量到A/B级标准
"""
import os
import re
import json
import glob

def load_audit():
    """加载审计数据"""
    try:
        with open('reports/wiki_quality_audit_final.json', 'r') as f:
            return json.load(f)
    except:
        with open('reports/wiki_quality_audit.json', 'r') as f:
            return json.load(f)

def get_c_pages():
    """获取所有C级页面"""
    audit = load_audit()
    return [p for p in audit if p.get('grade') == 'C' and p.get('page_type') in ['method', 'topic', 'model']]

def extract_keywords(title):
    """从标题提取关键词"""
    title_clean = title.lower().replace('-', ' ').replace('_', ' ')
    words = re.findall(r'\b[a-z]{3,}\b', title_clean)

    # 技术缩写映射
    abbrev_map = {
        'mmc': ['modular', 'multilevel', 'converter'],
        'vsc': ['voltage', 'source', 'converter', 'hvdc'],
        'lcc': ['line', 'commutated', 'converter'],
        'hvdc': ['high', 'voltage', 'direct', 'current'],
        'emt': ['electromagnetic', 'transient'],
        'avm': ['average', 'value', 'model'],
        'pll': ['phase', 'locked', 'loop'],
        'pwm': ['pulse', 'width', 'modulation'],
        'facts': ['flexible', 'ac', 'transmission'],
        'fcl': ['fault', 'current', 'limiter'],
        'fdne': ['frequency', 'dependent', 'network', 'equivalent'],
        'hil': ['hardware', 'loop'],
        'dfig': ['doubly', 'fed', 'induction', 'generator'],
        'pmsm': ['permanent', 'magnet', 'synchronous', 'motor'],
    }

    keywords = set(words)
    for abbrev, expansions in abbrev_map.items():
        if abbrev in title_clean:
            keywords.add(abbrev)
            keywords.update(expansions)

    return list(keywords)

def search_sources(keywords, max_results=5, require_deep_content=False):
    """搜索相关sources

    Args:
        keywords: 关键词列表
        max_results: 最大返回结果数
        require_deep_content: 是否要求source有deep-enrich或deep-review内容
    """
    if not keywords:
        return []

    sources = glob.glob('wiki/sources/*.md')
    scored = []

    for source_path in sources:
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 如果要求深度内容，跳过没有deep-enrich/deep-review的文件
            has_deep_enrich = 'deep-enrich:start' in content
            has_deep_review = 'deep-review:start' in content

            if require_deep_content and not (has_deep_enrich or has_deep_review):
                continue

            score = 0
            content_lower = content.lower()

            for kw in keywords:
                if len(kw) < 3:
                    continue
                # 标题匹配
                if kw in os.path.basename(source_path).lower():
                    score += 5
                # 内容匹配
                if kw in content_lower:
                    score += 1
                # deep-review匹配加分更多
                if has_deep_review:
                    review = re.search(r'<!-- deep-review:start -->(.+?)<!-- deep-review:end -->', content, re.DOTALL)
                    if review and kw in review.group(1).lower():
                        score += 5
                # deep-enrich匹配加分最多
                if has_deep_enrich:
                    score += 10  # 有deep-enrich的source优先级最高

            if score > 5:
                scored.append((source_path, score, has_deep_enrich, has_deep_review))
        except:
            pass

    scored.sort(key=lambda x: -x[1])
    return [(p[0], p[1]) for p in scored[:max_results]]

def extract_deep_content(source_path):
    """从source提取深度内容 - 重点提取公式、验证、边界"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        extracted = {
            'has_math': False,
            'has_validation': False,
            'has_boundary': False,
        }

        # 1. 从deep-enrich提取公式（最重要）
        enrich_match = re.search(r'<!-- deep-enrich:start -->(.+?)<!-- deep-enrich:end -->', content, re.DOTALL)
        if enrich_match:
            enrich_text = enrich_match.group(1)

            # 提取所有公式 - 支持 $...$ 和 $$...$$ 格式
            equations = []
            # LaTeX块公式 $$...$$
            blocks = re.findall(r'\$\$[^$]+\$\$', enrich_text)
            equations.extend(blocks)
            # LaTeX行内公式 $...$ (不包括$$)
            inline = re.findall(r'(?<!\$)\$[^$\n]+\$(?!\$)', enrich_text)
            equations.extend(inline)

            if equations:
                extracted['equations'] = equations[:8]  # 最多8个公式
                extracted['has_math'] = True

            # 提取方法细节
            method_match = re.search(r'## 方法细节\n\n(.+?)(?=##|<!--)', enrich_text, re.DOTALL)
            if method_match:
                extracted['method_details'] = method_match.group(1).strip()[:1500]

            # 提取仿真结果
            result_match = re.search(r'## 仿真结果\n\n(.+?)(?=##|<!--)', enrich_text, re.DOTALL)
            if result_match:
                extracted['simulation_results'] = result_match.group(1).strip()[:1000]
                extracted['has_validation'] = True

            # 提取量化发现
            quant_match = re.search(r'## 量化发现\n\n(.+?)(?=##|<!--)', enrich_text, re.DOTALL)
            if quant_match:
                extracted['quantitative'] = quant_match.group(1).strip()[:800]

            # 提取关键公式章节
            formula_match = re.search(r'## 关键公式\n\n(.+?)(?=##|<!--)', enrich_text, re.DOTALL)
            if formula_match:
                extracted['key_formulas'] = formula_match.group(1).strip()[:1200]
                extracted['has_math'] = True

            # 提取验证详情
            validation_match = re.search(r'## 验证详情\n\n(.+?)(?=##|<!--)', enrich_text, re.DOTALL)
            if validation_match:
                extracted['validation_details'] = validation_match.group(1).strip()[:1200]
                extracted['has_validation'] = True

            # 提取适用边界 - 支持多种标题格式
            boundary_patterns = [
                r'## 适用边界\n\n(.+?)(?=##|<!--)',
                r'## 适用边界与限制\n\n(.+?)(?=##|<!--)',
                r'### 适用边界\n\n(.+?)(?=###|##|<!--)',
            ]
            for pattern in boundary_patterns:
                boundary_match = re.search(pattern, enrich_text, re.DOTALL)
                if boundary_match:
                    extracted['boundary'] = boundary_match.group(1).strip()[:800]
                    extracted['has_boundary'] = True
                    break

        # 2. 从deep-review提取
        review_match = re.search(r'<!-- deep-review:start -->(.+?)<!-- deep-review:end -->', content, re.DOTALL)
        if review_match:
            review_text = review_match.group(1)

            # 提取模型算法
            model_match = re.search(r'### 2\. 模型、算法与实现技术\n\n(.+?)(?=###|<!--)', review_text, re.DOTALL)
            if model_match:
                extracted['model'] = model_match.group(1).strip()[:1200]

            # 提取验证优势
            val_match = re.search(r'### 3\. 验证、优势与不足\n\n(.+?)(?=###|<!--)', review_text, re.DOTALL)
            if val_match:
                extracted['validation'] = val_match.group(1).strip()[:800]
                extracted['has_validation'] = True

            # 提取证据边界
            boundary_match = re.search(r'### 证据边界\n\n(.+?)(?=###|<!--)', review_text, re.DOTALL)
            if boundary_match:
                extracted['evidence_boundary'] = boundary_match.group(1).strip()[:600]
                extracted['has_boundary'] = True

        return extracted
    except:
        return {}

def enhance_page_v2(target_path, contents_list, source_names):
    """深度增强目标页面 v2 - 添加公式、验证、边界"""
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        enhancements = []
        changed = False

        # 收集所有来源的内容
        all_equations = []
        all_validations = []
        all_boundaries = []
        all_method_details = []
        all_quantitative = []

        for sections in contents_list:
            if 'equations' in sections:
                all_equations.extend(sections['equations'])
            if 'validation_details' in sections:
                all_validations.append(sections['validation_details'])
            if 'validation' in sections:
                all_validations.append(sections['validation'])
            if 'boundary' in sections:
                all_boundaries.append(sections['boundary'])
            if 'evidence_boundary' in sections:
                all_boundaries.append(sections['evidence_boundary'])
            if 'method_details' in sections:
                all_method_details.append(sections['method_details'])
            if 'quantitative' in sections:
                all_quantitative.append(sections['quantitative'])
            if 'simulation_results' in sections:
                all_validations.append(sections['simulation_results'])

        # 1. 增强形式化表达 - 添加数学公式（最高优先级）
        if all_equations and '## 形式化表达' in content:
            current_eq_count = content.count('$') // 2  # 估算公式数量
            has_placeholder = '- 待补充' in content.split('## 形式化表达')[1].split('##')[0] if '## 形式化表达' in content else False

            if current_eq_count < 3 or has_placeholder:  # 如果公式很少或有待补充，添加更多
                # 构建公式章节
                new_section = '\n### 核心数学表达\n\n基于相关研究的公式体系：\n\n'

                # 去重
                seen = set()
                unique_eqs = []
                for eq in all_equations:
                    eq_clean = eq.strip()
                    if eq_clean not in seen and len(eq_clean) > 3:
                        seen.add(eq_clean)
                        unique_eqs.append(eq_clean)

                for i, eq in enumerate(unique_eqs[:5], 1):
                    new_section += f'{eq}\n\n'

                # 查找形式化表达章节并替换"待补充"或追加
                pattern = r'(## 形式化表达\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + new_section, content)
                    enhancements.append(f'{len(unique_eqs[:5])}个公式')
                    changed = True
                else:
                    pattern = r'(## 形式化表达\n\n)([^#]+)'
                    match = re.search(pattern, content, re.DOTALL)
                    if match and current_eq_count < 3:
                        insert_pos = match.end(2)
                        content = content[:insert_pos] + new_section + content[insert_pos:]
                        enhancements.append(f'{len(unique_eqs[:5])}个公式')
                        changed = True

        # 2. 增强EMT中的作用 - 添加方法细节
        if all_method_details and '## EMT中的作用' in content:
            if '- 待补充' in content or len(re.findall(r'- ', content.split('## EMT中的作用')[1].split('##')[0] if '## EMT中的作用' in content else '')) < 3:
                new_section = '\n基于相关研究的技术应用：\n\n'
                for i, detail in enumerate(all_method_details[:2], 1):
                    # 提取要点
                    points = re.findall(r'- (.+?)(?=\n|$)', detail[:800])
                    if points:
                        for j, point in enumerate(points[:2], 1):
                            new_section += f'{i}.{j}. {point.strip()[:150]}\n\n'
                    else:
                        # 提取句子
                        sentences = re.findall(r'[^.!?\n]+[.!?]', detail[:600])
                        if sentences:
                            new_section += f'{i}. {sentences[0].strip()[:200]}\n\n'

                pattern = r'(## EMT中的作用\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + new_section + '\n', content)
                    enhancements.append('方法细节')
                    changed = True

        # 3. 增强适用边界与失败模式 - 添加边界限定
        if all_boundaries and '## 适用边界与失败模式' in content:
            boundary_section = content.split('## 适用边界与失败模式')[1].split('##')[0] if '## 适用边界与失败模式' in content else ''
            has_placeholder = '- 待补充' in boundary_section

            if has_placeholder:
                new_section = '\n基于证据边界的分析：\n\n'

                for i, boundary in enumerate(all_boundaries[:2], 1):
                    # 提取列表项
                    items = re.findall(r'- (.+?)(?=\n|$)', boundary[:600])
                    for item in items[:3]:
                        new_section += f'- {item.strip()[:120]}\n'
                    new_section += '\n'

                pattern = r'(## 适用边界与失败模式\n\n)(- 待补充\n*)'
                if re.search(pattern, content):
                    content = re.sub(pattern, r'\1' + new_section, content)
                    enhancements.append('边界限定')
                    changed = True

        # 4. 添加验证与测试部分 - 使用验证详情
        if all_validations and '## 验证与测试' not in content:
            # 在主要分支与机制后添加
            if '## 主要分支与机制' in content:
                val_section = '\n## 验证与测试\n\n基于相关研究的验证证据：\n\n'

                for i, val in enumerate(all_validations[:2], 1):
                    # 提取测试系统信息
                    test_system = re.search(r'测试系统[：:]\s*([^\n]+)', val)
                    if test_system:
                        val_section += f'- **测试系统**: {test_system.group(1).strip()[:100]}\n'

                    # 提取仿真工具
                    simulator = re.search(r'仿真工具[：:]\s*([^\n]+)', val)
                    if simulator:
                        val_section += f'- **仿真工具**: {simulator.group(1).strip()[:100]}\n'

                    # 提取指标
                    metrics = re.findall(r'指标[：:]\s*([^\n]+)', val)
                    for metric in metrics[:2]:
                        val_section += f'- **评估指标**: {metric.strip()[:100]}\n'

                    # 提取数值结果
                    numbers = re.findall(r'[\d.]+\s*(?:ms|us|s|kV|V|MW|kW|Hz|%|pu|×10\^?[\d]+)', val)
                    if numbers:
                        val_section += '- **数值结果**: ' + ', '.join(numbers[:3]) + '\n'

                    val_section += '\n'

                # 插入到主要分支与机制后
                pattern = r'(## 主要分支与机制\n\n[^#]+)'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    insert_pos = match.end()
                    content = content[:insert_pos] + val_section + content[insert_pos:]
                    enhancements.append('验证详情')
                    changed = True

        # 5. 添加量化证据到主要分支
        if all_quantitative and '## 主要分支与机制' in content:
            quant_section = '\n### 量化证据\n\n从相关研究提取的数值指标：\n\n'
            has_numbers = False

            for quant in all_quantitative[:2]:
                numbers = re.findall(r'[\d.]+\s*(?:ms|us|s|kV|V|MW|kW|Hz|%|pu|×10\^?[\d]+)', quant)
                for num in numbers[:5]:
                    # 找上下文
                    context = re.search(rf'.{{0,30}}{re.escape(num)}.{{0,30}}', quant)
                    if context:
                        quant_section += f'- {context.group(0).strip()}\n'
                        has_numbers = True
                    else:
                        quant_section += f'- {num}\n'
                        has_numbers = True

            if has_numbers and '量化证据' not in content:
                pattern = r'(## 主要分支与机制\n\n[^#]+)'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    insert_pos = match.end()
                    content = content[:insert_pos] + quant_section + '\n' + content[insert_pos:]
                    enhancements.append('量化证据')
                    changed = True

        # 6. 添加多个来源引用
        if source_names and '## 代表性来源' in content:
            if '- 待补充' in content or content.count('[[', content.find('## 代表性来源')) < 3:
                source_section = '\n'
                for name in source_names[:5]:
                    source_section += f'- [[{name}]]\n'

                pattern = r'(## 代表性来源\n\n)([^#]+)'
                match = re.search(pattern, content, re.DOTALL)
                if match and len(match.group(2).strip().split('\n')) < 5:
                    content = content[:match.end(2)] + source_section + content[match.end(2):]
                    enhancements.append(f'{len(source_names[:5])}个来源')
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
    print("C级页面深度增强 v2")
    print("=" * 70)

    # 获取C级页面
    c_pages = get_c_pages()
    print(f"\n发现C级页面: {len(c_pages)}个")

    # 分批处理
    batch_size = 50
    processed = 0
    success = 0
    stats = {
        'added_equations': 0,
        'added_validation': 0,
        'added_boundary': 0,
    }

    print(f"\n开始增强（本批{batch_size}个）...")

    for page in c_pages[:batch_size]:
        target_path = page['path']
        target_name = os.path.basename(target_path).replace('.md', '')

        # 提取关键词
        keywords = extract_keywords(target_name)

        if not keywords:
            print(f"  - 跳过: {target_name[:45]:45s} (无关键词)")
            continue

        # 搜索相关sources
        sources = search_sources(keywords)

        if not sources:
            print(f"  - 跳过: {target_name[:45]:45s} (未找到source)")
            continue

        # 提取内容
        contents_list = []
        source_names = []
        for source_path, score in sources:
            sections = extract_deep_content(source_path)
            if sections:
                contents_list.append(sections)
                source_names.append(os.path.basename(source_path).replace('.md', ''))

        if not contents_list:
            print(f"  - 跳过: {target_name[:45]:45s} (无可用内容)")
            continue

        # 增强页面
        ok, enhancements = enhance_page_v2(target_path, contents_list, source_names)

        if ok:
            print(f"  ✓ 增强: {target_name[:45]:45s} {enhancements}")
            success += 1

            # 统计
            for e in enhancements:
                if '公式' in e:
                    stats['added_equations'] += 1
                if '验证' in e:
                    stats['added_validation'] += 1
                if '边界' in e:
                    stats['added_boundary'] += 1
        else:
            print(f"  - 跳过: {target_name[:45]:45s} (增强失败或无变化)")

        processed += 1

    print(f"\n本批结果:")
    print(f"  - 处理: {processed}个")
    print(f"  - 成功: {success}个")
    print(f"  - 添加公式: {stats['added_equations']}个页面")
    print(f"  - 添加验证: {stats['added_validation']}个页面")
    print(f"  - 添加边界: {stats['added_boundary']}个页面")
    print(f"  - 剩余: {len(c_pages) - batch_size}个")

if __name__ == '__main__':
    main()
