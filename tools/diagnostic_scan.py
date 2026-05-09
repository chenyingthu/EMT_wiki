#!/usr/bin/env python3
"""
Wiki全面诊断扫描工具
生成问题定位报告，为工作计划提供输入
"""
import os
import re
import json
import glob
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# 诊断维度
DIAGNOSTIC_CATEGORIES = {
    'structural': '结构性缺失',
    'evidence': '证据问题',
    'network': '网络问题',
    'format': '格式问题',
    'quality': '质量问题'
}

def load_quality_audit():
    """加载质量审计数据"""
    try:
        with open('reports/wiki_quality_audit.json', 'r') as f:
            return json.load(f)
    except:
        try:
            with open('reports/wiki_quality_audit_final.json', 'r') as f:
                return json.load(f)
        except:
            return []

def check_structural_issues(content, page_type):
    """检查结构性缺失"""
    issues = []

    required_sections = {
        'method': ['## 定义与边界', '## EMT中的作用', '## 核心机制', '## 适用边界与失败模式'],
        'topic': ['## 定义与边界', '## EMT中的作用', '## 主要分支与机制', '## 代表性来源'],
        'model': ['## 定义与边界', '## EMT中的作用', '## 建模层级', '## 验证与测试'],
        'entity': ['## 定义与边界', '## 在EMT生态中的角色', '## 适用边界']
    }

    sections = required_sections.get(page_type, [])
    for section in sections:
        if section not in content:
            issues.append(f'缺少{section}')
        elif '- 待补充' in content.split(section)[1].split('##')[0] if section in content else False:
            issues.append(f'{section}内容为空')

    return issues

def check_evidence_issues(content):
    """检查证据问题"""
    issues = []

    # 强断言模式
    strong_assertions = [
        (r'首次|首创|突破', '强断言：首次/首创/突破'),
        (r'完全|彻底|显著', '强断言：完全/彻底/显著'),
        (r'最优|最佳|首选', '强断言：最优/最佳/首选'),
        (r'主流|通用|标准', '强断言：主流/通用/标准'),
        (r'高精度|高效率|实时', '强断言：高精度/高效率/实时'),
        (r'误差\s*<\s*\d+|提升\s*\d+\s*倍', '无上下文数值'),
        (r'适用于所有|无需代价|无缝', '绝对化表述'),
    ]

    for pattern, desc in strong_assertions:
        if re.search(pattern, content):
            # 检查是否有来源限定
            context = re.search(r'.{0,50}' + pattern + r'.{0,50}', content)
            if context and '作者' not in context.group() and '论文' not in context.group():
                issues.append(desc)

    # 数值无上下文
    numbers = re.findall(r'[\d.]+\s*(?:ms|us|s|kV|V|MW|kW|Hz|%|pu)', content)
    if len(numbers) > 3:
        # 检查这些数值是否有来源说明
        for num in numbers[:5]:
            context = re.search(r'.{0,30}' + re.escape(num) + r'.{0,30}', content)
            if context:
                ctx = context.group()
                if '测试' not in ctx and '算例' not in ctx and '作者' not in ctx and '论文' not in ctx:
                    issues.append(f'数值"{num}"缺少上下文')
                    break

    return issues

def check_network_issues(content, all_pages):
    """检查网络问题"""
    issues = []

    # 提取wikilinks
    wikilinks = re.findall(r'\[\[([^\]|]+)', content)

    # 检查断链
    for link in wikilinks:
        link_clean = link.split('|')[0].strip()
        # 构建可能的文件路径
        # 在 wiki/ 下递归搜索文件（支持子目录）
        matches = list(Path('wiki').rglob(f'{link_clean}.md'))
        if not matches:
            issues.append(f'断链: [[{link_clean}]]')
            if len(issues) > 5:  # 限制报告数量
                break

    return issues

def check_format_issues(content):
    """检查格式问题"""
    issues = []

    # 破损表格
    if re.search(r'\|\s*\|\s*\|', content):
        issues.append('表格格式破损')

    # frontmatter问题
    if not re.search(r'^---\s*\n', content):
        issues.append('缺少frontmatter开始标记')

    # deep-review/deep-enrich标记不成对
    if 'deep-review:start' in content and 'deep-review:end' not in content:
        issues.append('deep-review标记不成对')
    if 'deep-enrich:start' in content and 'deep-enrich:end' not in content:
        issues.append('deep-enrich标记不成对')

    return issues

def check_quality_issues(page_info):
    """检查质量问题"""
    issues = []

    grade = page_info.get('grade', 'D')
    score = page_info.get('score', 0)
    page_issues = page_info.get('issues', [])

    if grade == 'C':
        issues.append(f'C级页面(分数:{score})')
    elif grade == 'D':
        issues.append(f'D级页面(分数:{score})')

    for issue in page_issues:
        if 'mathematical form' in issue.lower():
            issues.append('缺少数学形式')
        if 'short' in issue.lower():
            issues.append('页面太短')

    return issues

def scan_single_page(page_path, page_info, all_pages):
    """扫描单个页面"""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return {'error': '无法读取文件'}

    page_type = page_info.get('page_type', 'unknown')

    issues = {
        'structural': check_structural_issues(content, page_type),
        'evidence': check_evidence_issues(content),
        'network': check_network_issues(content, all_pages),
        'format': check_format_issues(content),
        'quality': check_quality_issues(page_info)
    }

    return {
        'path': page_path,
        'type': page_type,
        'grade': page_info.get('grade', 'D'),
        'score': page_info.get('score', 0),
        'issues': issues,
        'total_issues': sum(len(v) for v in issues.values())
    }

def prioritize_issues(scan_results):
    """优先级排序"""
    # 高优先级：影响范围大、容易修复
    # 中优先级：影响单个页面但需要深度修改
    # 低优先级：细节优化

    high = []
    medium = []
    low = []

    for result in scan_results:
        total = result['total_issues']
        grade = result['grade']

        if grade == 'D' or total >= 5:
            high.append(result)
        elif grade == 'C' or total >= 3:
            medium.append(result)
        elif total > 0:
            low.append(result)

    # 按分数排序（分数低的优先）
    high.sort(key=lambda x: x['score'])
    medium.sort(key=lambda x: x['score'])
    low.sort(key=lambda x: x['score'])

    return {'high': high, 'medium': medium, 'low': low}

def generate_summary(scan_results, priority_queues):
    """生成摘要报告"""
    summary = {
        'scan_date': datetime.now().isoformat(),
        'total_pages': len(scan_results),
        'pages_with_issues': len([r for r in scan_results if r['total_issues'] > 0]),
        'issue_breakdown': {
            'structural': sum(len(r['issues']['structural']) for r in scan_results),
            'evidence': sum(len(r['issues']['evidence']) for r in scan_results),
            'network': sum(len(r['issues']['network']) for r in scan_results),
            'format': sum(len(r['issues']['format']) for r in scan_results),
            'quality': sum(len(r['issues']['quality']) for r in scan_results)
        },
        'priority_distribution': {
            'high': len(priority_queues['high']),
            'medium': len(priority_queues['medium']),
            'low': len(priority_queues['low'])
        }
    }
    return summary

def main():
    print("=" * 70)
    print("Wiki全面诊断扫描")
    print("=" * 70)

    # 加载质量审计
    audit_data = load_quality_audit()
    print(f"\n加载审计数据: {len(audit_data)}个页面")

    # 获取所有页面路径
    all_pages = set()
    for root, dirs, files in os.walk('wiki'):
        for f in files:
            if f.endswith('.md'):
                all_pages.add(os.path.join(root, f))

    print(f"扫描文件系统: {len(all_pages)}个页面")

    # 扫描所有页面
    print("\n执行诊断扫描...")
    scan_results = []

    # 优先扫描taxonomy页面
    taxonomy_pages = [p for p in audit_data if p.get('page_type') in ['method', 'topic', 'model', 'entity']]

    for i, page_info in enumerate(taxonomy_pages, 1):
        path = page_info.get('path', '')
        if not path or not os.path.exists(path):
            continue

        result = scan_single_page(path, page_info, all_pages)
        scan_results.append(result)

        if i % 50 == 0:
            print(f"  已扫描: {i}/{len(taxonomy_pages)}")

    print(f"\n扫描完成: {len(scan_results)}个页面")

    # 优先级排序
    print("\n优先级排序...")
    priority_queues = prioritize_issues(scan_results)

    print(f"  高优先级: {len(priority_queues['high'])}个页面")
    print(f"  中优先级: {len(priority_queues['medium'])}个页面")
    print(f"  低优先级: {len(priority_queues['low'])}个页面")

    # 生成摘要
    summary = generate_summary(scan_results, priority_queues)

    # 创建报告目录
    os.makedirs('reports/diagnostic-reports', exist_ok=True)

    # 保存完整报告
    report_path = f'reports/diagnostic-reports/diagnostic-{datetime.now().strftime("%Y-%m-%d")}.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'full_results': scan_results,
            'priority_queues': priority_queues
        }, f, ensure_ascii=False, indent=2)

    print(f"\n报告已保存: {report_path}")

    # 保存优先级队列（供后续使用）
    for level in ['high', 'medium', 'low']:
        queue_path = f'reports/diagnostic-reports/priority-queue-{level}.json'
        with open(queue_path, 'w', encoding='utf-8') as f:
            json.dump(priority_queues[level], f, ensure_ascii=False, indent=2)

    # 生成人工可读摘要
    summary_md = f"""# 诊断报告摘要

生成时间: {summary['scan_date']}

## 总体情况

- 总页面数: {summary['total_pages']}
- 有问题页面: {summary['pages_with_issues']}

## 问题分布

| 类型 | 数量 |
|------|------|
| 结构性缺失 | {summary['issue_breakdown']['structural']} |
| 证据问题 | {summary['issue_breakdown']['evidence']} |
| 网络问题 | {summary['issue_breakdown']['network']} |
| 格式问题 | {summary['issue_breakdown']['format']} |
| 质量问题 | {summary['issue_breakdown']['quality']} |

## 优先级队列

- **高优先级**: {summary['priority_distribution']['high']}个页面（需要立即处理）
- **中优先级**: {summary['priority_distribution']['medium']}个页面（需要近期处理）
- **低优先级**: {summary['priority_distribution']['low']}个页面（可以延后处理）

## 前10个高优先级页面

"""
    for i, p in enumerate(priority_queues['high'][:10], 1):
        summary_md += f"{i}. `{os.path.basename(p['path'])}` - {p['total_issues']}个问题\n"

    with open('reports/diagnostic-reports/issue-summary.md', 'w', encoding='utf-8') as f:
        f.write(summary_md)

    print("摘要已保存: reports/diagnostic-reports/issue-summary.md")

    print("\n" + "=" * 70)
    print("诊断扫描完成!")
    print("=" * 70)

    return summary

if __name__ == '__main__':
    main()
