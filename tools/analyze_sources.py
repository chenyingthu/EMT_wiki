#!/usr/bin/env python3
"""
EMT Wiki Source Page Analyzer - Rule-based version
Uses tags + title keywords to populate method/model/topic wikilinks
and generate Chinese summaries from existing abstracts.
No LLM API calls needed - runs in seconds.
"""

import argparse
import glob
import json
import os
import re

# ─── Keyword-to-Taxonomy Mapping ───────────────────────────────────────

TITLE_KEYWORDS = {
    'mmc': '[[mmc-model]]',
    'modular multilevel': '[[mmc-model]]',
    'vsc': '[[vsc-model]]',
    'voltage source converter': '[[vsc-model]]',
    'dfig': '[[dfig-model]]',
    'doubly-fed': '[[dfig-model]]',
    'transmission line': '[[transmission-line-model]]',
    'cable': '[[cable-model]]',
    'transformer': '[[transformer-model]]',
    'synchronous machine': '[[synchronous-machine-model]]',
    'synchronous generator': '[[synchronous-machine-model]]',
    'fdne': '[[fdne-model]]',
    'network equivalent': '[[fdne-model]]',
    'frequency dependent': '[[fdne-model]]',
    'vector fitting': '[[vector-fitting]]',
    'average value': '[[average-value-model]]',
    'nodal': '[[nodal-analysis]]',
    'companion circuit': '[[nodal-analysis]]',
    'state space': '[[state-space-method]]',
    'passivity': '[[passivity-enforcement]]',
    'multi-rate': '[[multirate-method]]',
    'multirate': '[[multirate-method]]',
    'fixed admittance': '[[fixed-admittance]]',
    'adc model': '[[fixed-admittance]]',
    'associated discrete': '[[fixed-admittance]]',
    'numerical integration': '[[numerical-integration]]',
    'trapezoidal': '[[numerical-integration]]',
    'gear': '[[numerical-integration]]',
    'dynamic phasor': '[[dynamic-phasor]]',
    'phasor': '[[dynamic-phasor]]',
    'shifted frequency': '[[dynamic-phasor]]',
    'real-time': '[[real-time-simulation]]',
    'real time': '[[real-time-simulation]]',
    'fpga': '[[real-time-simulation]]',
    'rtds': '[[real-time-simulation]]',
    'hardware-in-the-loop': '[[real-time-simulation]]',
    'parallel': '[[parallel-computing]]',
    'gpu': '[[parallel-computing]]',
    'massively parallel': '[[parallel-computing]]',
    'co-simulation': '[[co-simulation]]',
    'cosimulation': '[[co-simulation]]',
    'hybrid simulation': '[[co-simulation]]',
    'electromechanical': '[[co-simulation]]',
    'frequency-dependent': '[[frequency-dependent-modeling]]',
    'wideband': '[[frequency-dependent-modeling]]',
    'wide-band': '[[frequency-dependent-modeling]]',
}

TAG_METHODS = {
    'vector-fitting': '[[vector-fitting]]',
    'average-value': '[[average-value-model]]',
    'nodal-analysis': '[[nodal-analysis]]',
    'state-space': '[[state-space-method]]',
    'numerical-integration': '[[numerical-integration]]',
    'passivity': '[[passivity-enforcement]]',
    'multirate': '[[multirate-method]]',
    'multi-rate': '[[multirate-method]]',
    'fixed-admittance': '[[fixed-admittance]]',
    'adc': '[[fixed-admittance]]',
    'interpolation': '[[numerical-integration]]',
}

TAG_MODELS = {
    'mmc': '[[mmc-model]]',
    'vsc': '[[vsc-model]]',
    'lcc': '[[lcc-model]]',
    'dfig': '[[dfig-model]]',
    'pmsm': '[[pmsm-model]]',
    'transformer': '[[transformer-model]]',
    'synchronous-machine': '[[synchronous-machine-model]]',
    'transmission-line': '[[transmission-line-model]]',
    'cable': '[[cable-model]]',
    'fdne': '[[fdne-model]]',
    'network-equivalent': '[[fdne-model]]',
    'renewable': '[[dfig-model]]',
    'ibg': '[[dfig-model]]',
    'wind': '[[dfig-model]]',
    'solar': '[[dfig-model]]',
    'pv': '[[dfig-model]]',
    'statcom': '[[vsc-model]]',
    'converter': '[[vsc-model]]',
    'hvdc': '[[mmc-model]]',
    'induction-machine': '[[dfig-model]]',
}

TAG_TOPICS = {
    'real-time': '[[real-time-simulation]]',
    'fpga': '[[real-time-simulation]]',
    'rtds': '[[real-time-simulation]]',
    'dynamic-phasor': '[[dynamic-phasor]]',
    'phasor': '[[dynamic-phasor]]',
    'sfa': '[[dynamic-phasor]]',
    'shifted-frequency': '[[dynamic-phasor]]',
    'frequency-dependent': '[[frequency-dependent-modeling]]',
    'wideband': '[[frequency-dependent-modeling]]',
    'cosimulation': '[[co-simulation]]',
    'co-simulation': '[[co-simulation]]',
    'hybrid': '[[co-simulation]]',
    'parallel': '[[parallel-computing]]',
    'gpu': '[[parallel-computing]]',
    'massively-parallel': '[[parallel-computing]]',
    'harmonic': '[[frequency-dependent-modeling]]',
    'ferroresonance': '[[frequency-dependent-modeling]]',
    'protection': '[[co-simulation]]',
    'relay': '[[co-simulation]]',
}

VALID_METHODS = list(set(list(TAG_METHODS.values()) + ['[[vector-fitting]]', '[[average-value-model]]', '[[nodal-analysis]]', '[[state-space-method]]', '[[numerical-integration]]', '[[passivity-enforcement]]', '[[multirate-method]]', '[[fixed-admittance]]']))
VALID_MODELS = list(set(list(TAG_MODELS.values())))
VALID_TOPICS = list(set(list(TAG_TOPICS.values())))


def analyze_title(title):
    """Extract taxonomy links from title keywords."""
    title_lower = title.lower()
    methods = set()
    models = set()
    topics = set()

    for keyword, link in TITLE_KEYWORDS.items():
        if keyword in title_lower:
            if link in VALID_METHODS:
                methods.add(link)
            elif link in VALID_MODELS:
                models.add(link)
            elif link in VALID_TOPICS:
                topics.add(link)

    return sorted(methods), sorted(models), sorted(topics)


def analyze_tags(tags):
    """Extract taxonomy links from tags."""
    methods = set()
    models = set()
    topics = set()

    for tag in tags:
        tag_lower = tag.lower().strip()
        if tag_lower in TAG_METHODS:
            methods.add(TAG_METHODS[tag_lower])
        if tag_lower in TAG_MODELS:
            models.add(TAG_MODELS[tag_lower])
        if tag_lower in TAG_TOPICS:
            topics.add(TAG_TOPICS[tag_lower])

    return sorted(methods), sorted(models), sorted(topics)


def generate_summary(title, abstract, methods, models, topics):
    """Generate a Chinese summary from abstract + taxonomy."""
    if not abstract or len(abstract) < 30:
        return f"本文研究了{', '.join(t.replace('[[', '').replace(']]', '') for t in topics[:3])}相关问题，涉及{', '.join(m.replace('[[', '').replace(']]', '') for m in methods[:3])}等方法。"

    # Extract the first meaningful sentence from abstract
    sentences = re.split(r'[.。]', abstract)
    meaningful = [s.strip() for s in sentences if len(s.strip()) > 15 and not s.strip().startswith(('0885', '10.', 'ISBN', 'Abstract', 'abstract', 'Abstract:', 'Index'))]

    if meaningful:
        return meaningful[0].strip()[:200]
    return f"本文研究了{', '.join(t.replace('[[', '').replace(']]', '') for t in topics[:3])}相关问题。"


def generate_contributions(title, methods, models, topics):
    """Generate contribution bullets from title analysis."""
    contributions = []

    # Model-related contributions
    for m in models:
        name = m.replace('[[', '').replace(']]', '').replace('-model', '')
        if 'mmc' in name:
            contributions.append(f"提出了一种改进的{name}建模方法，提高了EMT仿真效率和精度")
        elif 'transformer' in name:
            contributions.append(f"建立了更精确的{name}电磁暂态模型，考虑了频率相关特性和非线性效应")
        elif 'vsc' in name or 'lcc' in name:
            contributions.append(f"改进了{name}的EMT建模方法，提升了系统级暂态分析精度")
        elif 'line' in name or 'cable' in name:
            contributions.append(f"建立了考虑频率相关特性的{name}模型，提高了暂态仿真精度")
        elif 'dfig' in name:
            contributions.append(f"提出了适用于EMT仿真的{name}建模方法，适用于大规模风电场仿真")
        elif 'fdne' in name:
            contributions.append(f"改进了多端口频率相关网络等值方法，保证无源性和宽频精度")
        elif 'synchronous' in name:
            contributions.append(f"改进了{name}的相域/dq0建模方法，提升了暂态仿真精度")

    # Method-related contributions
    for m in methods:
        name = m.replace('[[', '').replace(']]', '').replace('-model', '').replace('-method', '')
        if 'vector-fitting' in name:
            contributions.append(f"应用矢量拟合算法实现频率响应的有理函数逼近")
        elif 'average-value' in name:
            contributions.append(f"采用平均值模型简化换流器开关过程，大幅提升计算效率")
        elif 'state-space' in name:
            contributions.append(f"使用状态空间法建立系统方程，便于稳定性分析和实时仿真")
        elif 'passivity' in name:
            contributions.append(f"提出无源性强制校正方法，确保频率相关模型的数值稳定性")
        elif 'multirate' in name:
            contributions.append(f"采用多速率方法对不同子系统采用不同时间步长，提高仿真效率")
        elif 'fixed-admittance' in name:
            contributions.append(f"采用恒导纳ADC模型避免导纳矩阵重构，适用于实时仿真")
        elif 'nodal' in name:
            contributions.append(f"基于节点分析和伴随电路法建立EMT求解框架")
        elif 'numerical' in name:
            contributions.append(f"研究了数值积分方法对EMT仿真精度和稳定性的影响")

    # Topic-related contributions
    for t in topics:
        name = t.replace('[[', '').replace(']]', '').replace('-simulation', '')
        if 'real-time' in name:
            contributions.append(f"实现了{name}仿真方法，满足硬件在环测试的实时性要求")
        elif 'co-simulation' in name:
            contributions.append(f"提出了混合仿真接口算法，实现不同时间尺度仿真的数据同步")
        elif 'dynamic-phasor' in name:
            contributions.append(f"应用动态相量法进行宽频暂态分析，兼顾计算效率和精度")
        elif 'parallel' in name:
            contributions.append(f"设计了并行计算策略，加速大规模电网EMT仿真")
        elif 'frequency-dependent' in name:
            contributions.append(f"考虑了设备参数的频率相关特性，提高宽频暂态分析精度")

    if not contributions:
        contributions.append(f"针对EMT仿真中的{', '.join(t.replace('[[', '').replace(']]', '') for t in topics[:2])}问题进行了研究")

    return contributions[:4]  # Limit to 4


def get_paper_info(filepath):
    """Extract metadata from source markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'title:\s*["\'](.+?)["\']', content)
    year_match = re.search(r'year:\s*(\d{4})', content)
    tags_match = re.search(r'tags:\s*\[(.*?)\]', content)
    abstract_match = re.search(r'## 摘要\n\n(.*?)(?=\n## )', content, re.DOTALL)

    title = title_match.group(1) if title_match else '未知'
    year = year_match.group(1) if year_match else '未知'
    tags = [t.strip().strip("'\"") for t in tags_match.group(1).split(',')] if tags_match else []
    abstract = abstract_match.group(1).strip() if abstract_match else ''

    return title, year, tags, abstract


def update_source_file(filepath, methods, models, topics, contributions, findings):
    """Update a source markdown file with analysis results."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Flexible pattern matching both Chinese and ASCII parentheses
    def make_pattern(section_name):
        return rf'## {section_name}\n\n\*?[\(（].*?[\)）]\*?'

    # 核心贡献
    if contributions:
        core_text = '\n'.join(f'- {c}' for c in contributions)
    else:
        core_text = '（待进一步分析）'
    content = re.sub(
        make_pattern('核心贡献'),
        lambda m: f'## 核心贡献\n\n{core_text}',
        content,
        flags=re.DOTALL
    )

    # 使用的方法
    if methods:
        methods_text = '\n'.join(f'- {m}' for m in methods)
    else:
        methods_text = '（待进一步分析）'
    content = re.sub(
        make_pattern('使用的方法'),
        lambda m: f'## 使用的方法\n\n{methods_text}',
        content,
        flags=re.DOTALL
    )

    # 涉及的模型
    if models:
        models_text = '\n'.join(f'- {m}' for m in models)
    else:
        models_text = '（待进一步分析）'
    content = re.sub(
        make_pattern('涉及的模型'),
        lambda m: f'## 涉及的模型\n\n{models_text}',
        content,
        flags=re.DOTALL
    )

    # 相关主题
    if topics:
        topics_text = '\n'.join(f'- {t}' for t in topics)
    else:
        topics_text = '（待进一步分析）'
    content = re.sub(
        make_pattern('相关主题'),
        lambda m: f'## 相关主题\n\n{topics_text}',
        content,
        flags=re.DOTALL
    )

    # 主要发现
    if findings:
        findings_text = findings
    else:
        findings_text = '（待进一步分析）'
    content = re.sub(
        make_pattern('主要发现'),
        lambda m: f'## 主要发现\n\n{findings_text}',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description='Analyze EMT wiki source pages (rule-based)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--limit', type=int, default=0, help='Limit to N files')
    parser.add_argument('--resume', action='store_true', help='Resume from checkpoint')
    args = parser.parse_args()

    source_dir = 'wiki/sources'
    checkpoint_file = os.path.join(source_dir, '.analysis_progress.json')

    source_files = sorted(glob.glob(os.path.join(source_dir, '*.md')))
    if args.limit > 0:
        source_files = source_files[:args.limit]

    if args.resume:
        processed = []
        if os.path.exists(checkpoint_file):
            with open(checkpoint_file, 'r') as f:
                processed = json.load(f).get('processed', [])
        source_files = [f for f in source_files if os.path.basename(f) not in processed]
        print(f"Resuming: {len(source_files)} files remaining")

    total = len(source_files)
    print(f"Processing {total} source files (rule-based analysis)...")

    success = 0
    skipped = 0

    for i, filepath in enumerate(source_files):
        title, year, tags, abstract = get_paper_info(filepath)

        # Combine tag-based and title-based analysis
        t_methods, t_models, t_topics = analyze_tags(tags)
        ti_methods, ti_models, ti_topics = analyze_title(title)

        # Merge and deduplicate
        methods = sorted(set(t_methods + ti_methods))
        models = sorted(set(t_models + ti_models))
        topics = sorted(set(t_topics + ti_topics))

        if not abstract or len(abstract) < 20:
            skipped += 1
            continue

        # Generate content
        contributions = generate_contributions(title, methods, models, topics)
        findings = generate_summary(title, abstract, methods, models, topics)

        if not args.dry_run:
            update_source_file(filepath, methods, models, topics, contributions, findings)

        success += 1
        if (i + 1) % 50 == 0 or i == total - 1:
            print(f"  Processed {i + 1}/{total} ({success} success, {skipped} skipped)")

    # Save checkpoint
    if not args.dry_run:
        all_processed = [os.path.basename(f) for f in source_files]
        save_checkpoint(all_processed, checkpoint_file)

    print(f"\n=== Summary ===")
    print(f"Total: {total}")
    print(f"Success: {success}")
    print(f"Skipped: {skipped}")
    if args.dry_run:
        print("(Dry run - no files modified)")


def save_checkpoint(processed, checkpoint_file):
    # Merge with existing
    existing = []
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'r') as f:
            existing = json.load(f).get('processed', [])
    all_processed = list(set(existing + processed))
    with open(checkpoint_file, 'w') as f:
        json.dump({'processed': all_processed}, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
