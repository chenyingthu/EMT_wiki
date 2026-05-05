#!/usr/bin/env python3
"""
批量生成页面内容脚本
自动从Source提取内容，快速填充所有待编辑页面
"""
import os
import re
import json
import glob
from pathlib import Path

def load_manual_edit_queue():
    """加载人工编辑队列"""
    try:
        with open('reports/manual_edit_queue.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def find_related_sources(page_name, max_sources=3):
    """找到相关的Source文件"""
    keywords = set(page_name.lower().replace('-', ' ').replace('_', ' ').split())

    sources = glob.glob('wiki/sources/*.md')
    scored = []

    for source_path in sources:
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()

            score = 0
            source_name = os.path.basename(source_path).lower()

            for kw in keywords:
                if len(kw) < 3:
                    continue
                if kw in source_name:
                    score += 5
                if kw in content.lower():
                    score += 1

            has_deep = 'deep-enrich:start' in content or 'deep-review:start' in content
            if has_deep:
                score += 10

            if score > 5:
                scored.append((source_path, score))
        except:
            pass

    scored.sort(key=lambda x: -x[1])
    return [p[0] for p in scored[:max_sources]]

def extract_from_source(source_path):
    """从Source提取内容"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        extracted = {'equations': [], 'abstract': '', 'methods': [], 'validation': ''}

        # 提取deep-enrich
        enrich_match = re.search(r'<!-- deep-enrich:start -->(.+?)<!-- deep-enrich:end -->', content, re.DOTALL)
        if enrich_match:
            text = enrich_match.group(1)

            # 提取公式
            equations = re.findall(r'\$\$[^$]+\$\$', text)
            extracted['equations'] = equations[:4]

            # 提取方法细节
            method_match = re.search(r'## 方法细节\n\n(.+?)(?=##|<!--)', text, re.DOTALL)
            if method_match:
                extracted['methods'] = method_match.group(1).strip()[:800]

            # 提取验证
            val_match = re.search(r'## 验证详情\n\n(.+?)(?=##|<!--)', text, re.DOTALL)
            if val_match:
                extracted['validation'] = val_match.group(1).strip()[:500]

        # 提取摘要
        abstract_match = re.search(r'## 摘要\n\n(.+?)(?=##|<!--)', content, re.DOTALL)
        if abstract_match:
            extracted['abstract'] = abstract_match.group(1).strip()[:400]

        return extracted
    except:
        return {'equations': [], 'abstract': '', 'methods': [], 'validation': ''}

def generate_page_content(page_name, page_type, sources_content):
    """生成页面内容"""
    # 收集所有内容
    all_equations = []
    all_abstracts = []
    all_methods = []
    all_validations = []

    for content in sources_content:
        if content['equations']:
            all_equations.extend(content['equations'])
        if content['abstract']:
            all_abstracts.append(content['abstract'])
        if content['methods']:
            all_methods.append(content['methods'])
        if content['validation']:
            all_validations.append(content['validation'])

    # 生成定义与边界
    definition = all_abstracts[0] if all_abstracts else f'{page_name}是电力系统电磁暂态仿真中的重要方法/模型。'

    # 生成EMT作用
    emt_role = f'基于相关研究，{page_name}在EMT仿真中用于解决特定问题。'
    if all_methods:
        sentences = all_methods[0].split('.')[:2]
        emt_role = '. '.join(sentences) + '.'

    # 生成公式
    equations_section = ''
    if all_equations:
        equations_section = '\n### 核心数学表达\n\n从相关研究提取的关键公式：\n\n'
        seen = set()
        for eq in all_equations[:4]:
            if eq not in seen:
                seen.add(eq)
                equations_section += f'{eq}\n\n'

    # 生成验证
    validation_section = ''
    if all_validations:
        validation_section = '\n基于相关研究的验证证据：\n\n'
        val = all_validations[0]
        test_sys = re.search(r'测试系统[：:]\s*([^\n]+)', val)
        if test_sys:
            validation_section += f'- **测试系统**: {test_sys.group(1)[:100]}\n'
        sim = re.search(r'仿真工具[：:]\s*([^\n]+)', val)
        if sim:
            validation_section += f'- **仿真工具**: {sim.group(1)[:100]}\n'
        numbers = re.findall(r'[\d.]+\s*(?:ms|us|s|kV|V|MW|kW|Hz|%|pu)', val)
        if numbers:
            validation_section += f'- **数值结果**: {", ".join(numbers[:3])}\n'

    # 生成来源引用
    source_refs = ''
    for i, sc in enumerate(sources_content[:3], 1):
        source_name = sc.get('name', f'source-{i}')
        source_refs += f'- [[{source_name}]]\n'

    # 构建完整页面
    content = f"""---
title: "{page_name.replace('-', ' ').title()}"
type: {page_type}
tags: [{page_name}]
created: "{os.popen('date +%Y-%m-%d').read().strip()}"
---

# {page_name.replace('-', ' ').title()}

## 定义与边界

{definition[:300]}...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

{emt_role[:400]}

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

- 待补充

{equations_section}

## 适用边界与失败模式

- 待补充

**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

{source_refs if source_refs else '- 待补充'}

---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
"""

    return content

def main():
    print("=" * 70)
    print("批量生成页面内容")
    print("=" * 70)

    # 加载待编辑队列
    queue = load_manual_edit_queue()
    print(f"\n待编辑页面: {len(queue)}个")

    if not queue:
        print("无待编辑页面，退出")
        return

    # 处理每个页面
    success = 0
    failed = 0

    for i, page in enumerate(queue, 1):
        path = page['path']
        name = page['name']
        page_type = page['type']

        print(f"\n[{i}/{len(queue)}] 处理: {name[:40]}")

        try:
            # 查找相关Source
            sources = find_related_sources(name)

            if not sources:
                print(f"  - 无相关Source，跳过")
                failed += 1
                continue

            # 提取Source内容
            sources_content = []
            for src in sources:
                content = extract_from_source(src)
                content['name'] = os.path.basename(src).replace('.md', '')
                sources_content.append(content)

            # 生成页面内容
            new_content = generate_page_content(name, page_type, sources_content)

            # 保存
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ 已生成")
            success += 1

        except Exception as e:
            print(f"  ✗ 失败: {e}")
            failed += 1

        # 每10个页面显示进度
        if i % 10 == 0:
            print(f"\n进度: {i}/{len(queue)} (成功: {success}, 失败: {failed})")

    print(f"\n{'=' * 70}")
    print(f"批量生成完成!")
    print(f"  - 成功: {success}个")
    print(f"  - 失败: {failed}个")
    print(f"  - 总计: {len(queue)}个")
    print("=" * 70)

if __name__ == '__main__':
    main()
