#!/usr/bin/env python3
"""
批量修复英文缩写链接
将缩写形式（如 [[mmc]]）映射到完整页面名（如 [[mmc-model]]）
"""

import json
import re
from pathlib import Path

WIKI_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki")
REPORT_FILE = Path("/home/chenying/researches/EMT_LLM_Wiki/reports/wiki_lint_report.json")

# 缩写到完整页面名的映射
ABBREV_MAPPING = {
    # 模型缩写
    'state-space': 'state-space-method',
    'mmc': 'mmc-model',
    'transformer': 'transformer-model',
    'synchronous-machine': 'synchronous-machine-model',
    'svc': 'svc-tcr-model',
    'tcr': 'svc-tcr-model',
    'igbt': 'igbt-model',
    'hvdc': 'vsc-hvdc',
    'dfig': 'dfig-model',
    'lcc': 'lcc-model',
    'pmsm': 'pmsm-model',
    'pll': 'pll-model',
    'fdne': 'fdne-model',
    'bess': 'bess-model',
    'mtdc': 'mtdc-model',
    'pet': 'pet-sst-model',
    'vsc': 'vsc-model',
    'avm': 'average-value-model',
    'converter-transformer': 'converter-transformer-model',
    'induction-machine': 'induction-machine-model',
    'pv-system': 'pv-system-model',
    'surge-arrester': 'surge-arrester-model',
    'grounding-system': 'grounding-system-model',
    'circuit-breaker': 'circuit-breaker-model',
    'load': 'load-model',
    'pi-controller': 'pi-controller-model',
    'pwm-modulator': 'pwm-modulator-model',
    'coordinate-transformation': 'coordinate-transformation-model',
    'vector-control': 'vector-control-model',
    'droop-control': 'droop-control-model',
    'voltage-current-sensor': 'voltage-current-sensor-model',
    'emi-filter': 'emi-filter-model',
    'gfl-inverter': 'gfl-inverter-model',
    'gfm-inverter': 'gfm-inverter-model',
    'energy-storage-converter': 'energy-storage-converter-model',
    'hybrid-converter': 'hybrid-converter-model',
    'resistor': 'resistor-model',
    'capacitor': 'capacitor-model',
    'inductor': 'inductor-model',
    'diode': 'diode-model',
    'cable': 'cable-model',

    # 主题缩写
    'harmonic': 'harmonic-analysis',
    'parallel': 'parallel-computing',
    'real-time': 'real-time-simulation',
    'co-simulation': 'co-simulation',
    'wind-farm': 'wind-farm-modeling',
    'switching': 'switching-transient',
    'lightning': 'lightning-overvoltage',
    'protection': 'protection-relay-modeling',
    'grounding': 'grounding-lightning-overvoltage',

    # 方法缩写
    'interpolation': 'interpolation-method',
    'fixed-admittance': 'fixed-admittance',
    'switch-modeling': 'switch-modeling',
    'model-order-reduction': 'model-order-reduction',
    'numerical-integration': 'numerical-integration-methods',
    'vector-fitting': 'vector-fitting',
    'prony': 'prony-analysis',
    'passivity-enforcement': 'passivity-enforcement',
    'dynamic-phasor': 'dynamic-phasor',
    'shifted-frequency-analysis': 'dynamic-phasor',  # SFA是动态相量的一种
    'sfa': 'dynamic-phasor',
    'multirate': 'multirate-method',
    'stiff': 'stiff-system-handling',
    'sparse-matrix': 'sparse-matrix-solver',
    'iterative': 'iterative-solvers',
    'small-signal': 'small-signal-analysis',
    'parameter-identification': 'parameter-identification',
    'thevenin-norton': 'thevenin-norton-equivalent',
    'switching-function': 'switching-function',
    'discretization': 'discretization-methods',
    'rational-approximation': 'vector-fitting',

    # 实体/其他
    'ieee': 'ieee',
    'cigre': 'cigre',
    'matlab-simulink': 'matlab-simulink',
    'bjorn-gustavsen': 'bjorn-gustavsen',
    'adam-semlyen': 'adam-semlyen',
    'tsinghua-university': 'tsinghua-university',
    'china-epri': 'china-epri',
    'abb': 'abb',
    'siemens': 'siemens',
    'comsol': 'comsol',
    'ansys': 'ansys',
    'adpss': 'adpss',
    'psmodel': 'psmodel',
    'cloudpss': 'cloudpss',
    'pscad-emtdc': 'pscad-emtdc',
    'emtp': 'emtp-emtp-rv',
    'atp-emtp': 'atp-emtp',
    'rtds': 'rtds',
    'manitoba': 'university-of-manitoba',
    'montreal': 'polytechnique-montreal',
    'gole': 'gole',
    'mahseredjian': 'mahseredjian',

    # 其他常见缩写
    'emt': 'emt-mathematical-foundation',
    'emtp': 'emtp-emtp-rv',
    'emtdc': 'pscad-emtdc',
    'cdsm': 'mmc-model',  # CDSM是MMC子模块的一种
    'ch-mmc': 'mmc-model',
    'statcom': 'svc-tcr-model',
    'upfc': 'svc-tcr-model',
    'tcsc': 'svc-tcr-model',
    'facts': 'svc-tcr-model',
    'sst': 'pet-sst-model',
    'dab': 'pet-sst-model',
    'cllc': 'pet-sst-model',
    'vsm': 'gfm-inverter-model',
    'gfl': 'gfl-inverter-model',
    'gfm': 'gfm-inverter-model',
    'lvrt': 'gfl-inverter-model',
    'hvrt': 'gfl-inverter-model',
    'pll': 'pll-model',
    'srfsogipll': 'pll-model',
    'park': 'coordinate-transformation-model',
    'clarke': 'coordinate-transformation-model',
    'dq0': 'coordinate-transformation-model',
    'abc': 'coordinate-transformation-model',
    'fo': 'vector-control-model',
    'dtc': 'vector-control-model',
    'mtpa': 'vector-control-model',
    'pwm': 'pwm-modulator-model',
    'svpwm': 'pwm-modulator-model',
    'spwm': 'pwm-modulator-model',
    'pi': 'pi-controller-model',
    'pr': 'pi-controller-model',
    'crowbar': 'dfig-model',
    'chopper': 'dfig-model',
    'rsc': 'dfig-model',
    'gsc': 'dfig-model',
    'lcl': 'emi-filter-model',
    'lc': 'emi-filter-model',
    'rc': 'emi-filter-model',
    'rl': 'inductor-model',
    'rlc': 'transmission-line-modeling',
    'pt': 'voltage-current-sensor-model',
    'ct': 'voltage-current-sensor-model',

    # 第二批修复的缩写
    'transmission-line': 'transmission-line-modeling',
    'frequency-dependent': 'frequency-dependent-modeling',
    'passivity': 'passivity-enforcement',
    'pmsg': 'pmsm-model',
    'chb-dab': 'pet-sst-model',
    'chb': 'pet-sst-model',
    'dab': 'pet-sst-model',
    'ibr': 'gfl-inverter-model',
    'hbsm': 'mmc-model',
    'fbsm': 'mmc-model',
    'mbsm': 'mmc-model',
    'dsogi-pll': 'pll-model',
    'srf-pll': 'pll-model',
    'ccvt': 'voltage-current-sensor-model',
    'tsc': 'svc-tcr-model',
    'emtp-atp': 'atp-emtp',
    'emtp-atpdraw': 'atp-emtp',
    'dccb': 'circuit-breaker-model',
    'cl-dccb': 'circuit-breaker-model',
    'dc-fcl': 'fdne-model',
    'dc-pfc': 'fdne-model',
    'dc-cb': 'circuit-breaker-model',
    'gis': 'grounding-lightning-overvoltage',
    'm3c': 'mmc-model',
    'modular-multilevel-converter': 'mmc-model',
    'solid-state-transformer': 'pet-sst-model',
    'sst': 'pet-sst-model',
    'half-bridge-submodule': 'mmc-model',
    'n-port-network': 'fdne-model',
    'emt-simulation': 'emt-mathematical-foundation',
    'power-electronics-modeling': 'vsc-model',
    'dem': 'mmc-model',
    'midc': 'mtdc-model',
    'tbs': 'transformer-model',
    'gan-hemt': 'igbt-model',
    'pv-statcom': 'svc-tcr-model',
    'modal-analysis': 'state-space-method',
    'recursive-convolution': 'transmission-line-modeling',
    'thermal-electrical-modeling': 'transformer-model',
    'multiscale-modeling': 'dynamic-phasor',
    'coherency-clustering': 'model-order-reduction',
    'current-trajectory-similarity': 'parameter-identification',
    'energy-storage-system': 'bess-model',
    'virtual-synchronous-generator': 'gfm-inverter-model',
    'vsg': 'gfm-inverter-model',
    'frequency-response': 'harmonic-analysis',
    'frequency-control': 'pi-controller-model',
    'inertia-control': 'gfm-inverter-model',
    'power-electronics-control': 'vector-control-model',
    'equivalent-modeling': 'fdne-model',
    'capacitive-voltage-transformer': 'voltage-current-sensor-model',
    'gas-insulated-switchgear': 'grounding-lightning-overvoltage',
    'fault-current-limiter': 'fdne-model',
    'thyristor-switched-capacitor': 'svc-tcr-model',
    'permanent-magnet-synchronous-generator': 'pmsm-model',
    'cascaded-h-bridge': 'pet-sst-model',
    'inverter-based-resource': 'gfl-inverter-model',
    'half-bridge-sm': 'mmc-model',
    'full-bridge-sm': 'mmc-model',
    'mixed-bridge-sm': 'mmc-model',
    'dual-second-order-generalized-integrator-pll': 'pll-model',
    'synchronous-reference-frame-pll': 'pll-model',
    'dc-circuit-breaker': 'circuit-breaker-model',
    'current-limiting-unit': 'fdne-model',
    'power-flow-controller': 'fdne-model',
    'rogerskii': 'transformer-model',
    'jiles-atherton': 'transformer-model',
    'preisach': 'transformer-model',
    'tlm': 'transmission-line-modeling',
    'fd': 'frequency-dependent-modeling',
    'vf': 'vector-fitting',
    'mvf': 'vector-fitting',
    'cvf': 'vector-fitting',
    'mpm': 'vector-fitting',
    'nilt': 'numerical-integration-methods',
    'fft': 'harmonic-analysis',
    'dft': 'harmonic-analysis',
    'lti': 'state-space-method',
    'ltv': 'state-space-method',
    'dae': 'emt-mathematical-foundation',
    'ode': 'emt-mathematical-foundation',
    'pde': 'emt-mathematical-foundation',
    'kcl': 'network-equation-solution',
    'kvl': 'network-equation-solution',
    'mana': 'network-equation-solution',
    'adc': 'switch-modeling',
    'cda': 'numerical-integration-methods',
    'be': 'numerical-integration-methods',
    'trapezoidal': 'numerical-integration-methods',
    'gear': 'numerical-integration-methods',
    'dirk': 'numerical-integration-methods',
    'fe': 'numerical-integration-methods',
    'gpu': 'parallel-computing',
    'fpga': 'real-time-simulation',
    'cpu': 'parallel-computing',
    'hil': 'real-time-simulation',
    'phasor': 'dynamic-phasor',
    'rms': 'dynamic-phasor',
    'em': 'electromechanical-electromagnetic-hybrid',
    't': 'transmission-line-modeling',
    'pi': 'transmission-line-modeling',
    'bergeron': 'transmission-line-modeling',
    'fd-line': 'transmission-line-modeling',
    'ulm': 'transmission-line-modeling',
    'marti': 'transmission-line-modeling',
    'noda': 'transmission-line-modeling',
}


def is_abbreviation(link):
    """检查链接是否可能是缩写（不在现有页面中）"""
    # 检查链接是否在映射中
    return link in ABBREV_MAPPING


def fix_abbreviations_in_file(filepath, abbrev_map):
    """修复单个文件中的缩写链接"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixed_count = 0
    fixed_links = []

    # 查找所有wikilink
    # 格式: [[target]] 或 [[target|display]]
    pattern = r'\[\[([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'

    def replace_link(match):
        nonlocal fixed_count
        target = match.group(1)
        display = match.group(2)

        # 检查是否是缩写
        if target in ABBREV_MAPPING:
            new_target = ABBREV_MAPPING[target]
            fixed_count += 1
            fixed_links.append((target, new_target))

            if display:
                return f'[[{new_target}|{display}]]'
            else:
                return f'[[{new_target}]]'

        return match.group(0)

    content = re.sub(pattern, replace_link, content)

    if fixed_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return fixed_count, fixed_links


def main():
    # 读取 lint 报告
    with open(REPORT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 按文件分组收集需要修复的缩写链接
    from collections import defaultdict
    by_file = defaultdict(list)

    for link in data['broken_links']:
        if link['to'] in ABBREV_MAPPING:
            by_file[link['file']].append(link['to'])

    print(f"发现 {len(by_file)} 个文件包含可修复的缩写链接")
    print()

    # 统计各缩写的出现次数
    abbrev_counts = defaultdict(int)
    for link in data['broken_links']:
        if link['to'] in ABBREV_MAPPING:
            abbrev_counts[link['to']] += 1

    print("最常见缩写（前20）：")
    for abbrev, count in sorted(abbrev_counts.items(), key=lambda x: -x[1])[:20]:
        print(f"  {abbrev} → {ABBREV_MAPPING[abbrev]} ({count}次)")
    print()

    # 逐个文件修复
    total_fixed = 0
    processed = 0
    all_fixed = []

    for filepath, targets in by_file.items():
        try:
            fixed, links = fix_abbreviations_in_file(filepath, targets)
            total_fixed += fixed
            processed += 1
            all_fixed.extend(links)

            if fixed > 0 and processed % 100 == 0:
                print(f"进度: {processed}/{len(by_file)} 文件，已修复 {total_fixed} 个链接")

        except Exception as e:
            print(f"错误处理 {filepath}: {e}")

    print()
    print(f"✅ 完成！处理了 {processed} 个文件，共修复 {total_fixed} 个缩写链接")

    # 输出修复摘要
    if all_fixed:
        summary = defaultdict(int)
        for old, new in all_fixed:
            summary[f"{old} → {new}"] += 1

        print()
        print("修复摘要（前30）：")
        for mapping, count in sorted(summary.items(), key=lambda x: -x[1])[:30]:
            print(f"  {mapping}: {count}次")


if __name__ == "__main__":
    main()
