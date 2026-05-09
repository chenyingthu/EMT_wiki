#!/usr/bin/env python3
"""
二级分类迁移脚本 — 将 wiki/methods|models|topics|entities 中的页面
迁移到二级子目录，并创建 _index.md 索引页。

用法:
  python3 tools/migrate_subdirs.py [--dry-run] [--category methods]
"""

import os
import re
import sys
import argparse
from pathlib import Path

WIKI_DIR = Path("wiki")

# ── methods 二级分类映射 ──────────────────────────────────────

METHODS_MAP = {
    "numerical-methods": [  # 数值方法与积分
        "backward-euler", "trapezoidal-rule", "gear-method",
        "runge-kutta-in-emt", "numerical-integration",
        "numerical-integration-error", "discretization-methods",
        "companion-circuit", "companion-model", "fixed-admittance",
        "stiff-system-handling", "numerical-oscillation-suppression",
        "numerical-damping-optimization", "exponential-integrator",
        "variable-time-step-solver", "dae-solvers",
        "bilinear-transform", "large-timestep-simulation",
        "voltage-interpolation", "interpolation-method",
        "steady-state-initialization", "state-space-method",
        "state-space-average-method",
    ],
    "network-solution": [  # 网络求解与矩阵方法
        "nodal-analysis", "nodal-admittance-matrix",
        "sparse-matrix-solver", "sparse-matrix-techniques",
        "iterative-solvers", "low-rank-solver",
        "newton-raphson-method", "current-injection",
        "network-partitioning", "transformer-network",
        "n-port-network", "compensation-method",
        "thevenin-equivalent", "thevenin-norton-equivalent",
        "norton-equivalent",
        "equivalent-circuit-method", "finite-element-method",
        "ideal-transformer-equivalent",
    ],
    "transmission-line": [  # 输电线路与电缆建模
        "transmission-line-theory", "bergeron-line-model",
        "bergeron-model",
        "distributed-parameter-line", "distributed-parameter-model",
        "universal-line-model", "phase-domain-modeling",
        "modal-domain-decoupling", "modal-decomposition",
        "modal-transformation", "quasi-tem-approximation",
        "lumped-parameter-model", "pi-model",
        "single-phase-line-model", "balanced-three-phase-line",
        "transposed-three-phase-line", "underground-cable-modeling",
        "cross-bonded-cable", "corona-effect-modeling",
        "earth-return-impedance", "frequency-dependent-soil",
        "frequency-dependent-soil-model", "mutual-impedance",
        "characteristic-method", "folded-line-equivalent",
        "parallel-transmission-line",
        "frequency-dependent-network-equivalent",
        "wideband-modeling", "layered-connection",
    ],
    "power-electronics": [  # 电力电子建模
        "switching-function-method", "average-value-model",
        "delarue-enhanced-avm", "ould-bachir-2019-unified-avm",
        "detailed-equivalent-model", "switch-modeling",
        "pwm-modulation", "nearest-level-control",
        "nearest-level-modulation", "half-bridge-submodule",
        "fbsm", "hbsm", "cdsm", "mbsm", "tbs", "tsc",
        "m3c", "midc", "csg", "dem",
        "chb-dab", "dual-active-bridge", "pet",
        "cl-dccb", "dccb", "dc-fcl", "dc-pfc",
        "commutation-failure", "concurrent-commutation-failure",
        "extinction-angle-calculation", "converter-station-inverter",
        "lcl-filter", "gan-hemt",
        "jiles-atherton-model", "magnetic-saturation-modeling",
    ],
    "control": [  # 控制方法与系统
        "control-system", "vector-control", "vsc-control",
        "hvdc-control", "dq-transformation",
        "coordinate-transformation", "phase-locked-loop",
        "srf-pll", "dsogi-pll", "pll-design",
        "power-electronics-control", "hierarchical-control",
        "distributed-control", "droop-control",
        "adaptive-droop", "grid-forming-control",
        "dual-loop-pi-controller", "h-infinity-control",
        "mixed-sensitivity-optimization",
        "circulating-current-suppression", "mppt-control",
        "frequency-control", "inertia-control",
        "lvrt-control", "microgrid-control",
        "virtual-synchronous-generator", "thyristor-control",
    ],
    "stability-analysis": [  # 稳定性与振荡分析
        "small-signal-stability", "small-signal-stability-analysis",
        "small-signal-analysis", "eigenvalue-analysis",
        "transient-stability", "transient-stability-analysis",
        "swing-equation", "equal-area-criterion", "eeac",
        "energy-function", "sensitivity-analysis",
        "impedance-modeling", "frequency-scan",
        "frequency-scanning", "frequency-response",
        "power-system-stabilizer", "excitation-system",
        "pss-model", "electromechanical-modeling",
        "small-perturbation-linearization",
        "generalized-eigenvalue-method",
        "ac-fault-transient-analysis",
    ],
    "signal-processing": [  # 信号处理与系统辨识
        "vector-fitting", "passivity-enforcement",
        "prony-analysis", "recursive-convolution",
        "curve-fitting", "least-squares-method",
        "partial-fraction-expansion", "parameter-identification",
        "modal-analysis", "discrete-fourier-transform",
        "fft", "fourier-series", "fourier-filtering",
        "hilbert-transform", "signal-processing",
        "filtering", "harmonic-analysis-methods",
        "harmonic-interaction", "harmonic-transfer-coefficient",
        "numerical-laplace-transform",
        "numerical-inverse-laplace-transform",
        "impedance-measurement", "time-domain-impedance-estimation",
        "heidler-function",
    ],
    "simulation-technology": [  # 仿真技术与高性能计算
        "multirate-method", "parallel-in-time",
        "gpu-accelerated-simulation", "gpu-parallel-acceleration",
        "multithreaded-parallel-computing",
        "heterogeneous-computing", "hardware-acceleration",
        "high-performance-computing", "computational-acceleration",
        "fpga-real-time-simulation", "hil-simulation",
        "offline-to-realtime-porting", "fixed-point-conversion",
        "automatic-code-generation", "declarative-modeling",
        "modeling-language", "netlist-import-export",
        "fdtd", "interface-technique",
        "direct-interface-technique",
        "hybrid-modeling", "coherency-clustering",
    ],
    "protection-fault": [  # 保护与故障分析
        "fault-analysis", "fault-analysis-methods",
        "distance-protection", "digital-distance-protection",
        "parallel-line-protection", "impedance-relay",
        "equivalent-fault-loop", "symmetrical-components",
        "sequence-component-method", "sequence-network-model",
        "dc-protection", "anti-islanding", "ieee-1547",
        "insulation-coordination", "lightning-transient-analysis",
        "high-frequency-transient-analysis", "gis",
        "ccvt", "yang-2018-dc-protection",
        "grounding-system-modeling",
        "wide-area-monitoring-protection",
    ],
    "system-studies": [  # 系统分析与专题
        "back-to-back-hvdc", "multi-terminal-dc",
        "beerten-2012-mtdc-powerflow",
        "haileselassie-2012-mtdc-control",
        "dfig-offshore-wind-farm", "pmsg-single-unit",
        "pv-statcom", "renewable-integration", "ibr",
        "distribution-network",
        "electromechanical-electromagnetic-hybrid-simulation",
        "dynamic-phasor", "phasor-model",
        "phasor-measurement-unit", "state-estimation",
        "power-flow-calculation", "optimal-power-flow",
        "economic-dispatch", "emtp-atp", "emtp-atpdraw",
        "simulation-tools-status", "emt-simulation-verification",
        "algebraic-characterization",
        "complex-differential-equation-solving",
        "time-domain-formulation",
        "three-phase-instantaneous-model",
        "model-compatibility-layer",
        "ac-coupled-network-equivalent",
        "current-trajectory-similarity",
        "lumped-resistance-approximation",
        "electromechanical-simulation",
        "model-order-reduction",
    ],
}

# ── models 二级分类映射 ───────────────────────────────────────

MODELS_MAP = {
    "rotating-machine": [  # 旋转电机模型
        "synchronous-machine-model", "induction-machine",
        "induction-machine-model", "dfig-model", "pmsm-model",
        "single-phase-induction-machine", "electromechanical-model",
        "grid-side-converter",
    ],
    "converter": [  # 换流器与逆变器模型
        "vsc-model", "mmc-model", "lcc-model", "hybrid-converter-model",
        "dc-dc-converter", "three-phase-bridge-inverter", "inverter-model",
        "grid-connected-inverter", "grid-forming-inverter", "gfl-inverter-model",
        "gfm-inverter-model", "power-electronics-modeling", "switching-model",
        "pwm-modulator-model",
    ],
    "submodule": [  # 子模块与开关模型
        "submodule", "submodule-model", "half-bridge-smb", "full-bridge-smb",
        "cs-dam-model", "detailed-switch-model", "ideal-switch-model",
        "arm-reactor", "mmc-hvdc-5-level",
    ],
    "transformer": [  # 变压器模型
        "transformer-model", "converter-transformer-model",
        "distribution-transformer", "multi-winding-transformer",
        "solid-state-transformer", "pet-sst-model",
    ],
    "transmission-line": [  # 输电线路与电缆模型
        "transmission-line-model", "cable-model", "ac-transmission-line",
        "frequency-dependent-line-model", "cross-bonded-cable",
    ],
    "renewable-storage": [  # 新能源与储能模型
        "pv-system-model", "bess-model", "energy-storage-converter-model",
    ],
    "protection": [  # 保护设备模型
        "differential-protection", "distance-relay",
        "protection-control-device", "surge-arrester-model",
        "circuit-breaker-model", "fault-impedance-model",
        "grounding-system-model", "insulator-string-model",
    ],
    "control": [  # 控制器模型
        "droop-control-model", "pi-controller-model", "pll-model",
        "vector-control-model", "coordinate-transformation-model",
        "model-predictive-control",
    ],
    "compensation": [  # 无功补偿与滤波
        "statcom", "statcom-model", "svc-model", "svc-tcr-model",
        "tcsc-model", "upfc-model", "reactive-compensation-device",
        "emi-filter-model", "capacitor-model", "inductor-model",
    ],
    "equivalent": [  # 等值与降阶模型
        "equivalent-modeling", "fdne-model", "multiscale-modeling",
        "thevenin-equivalent-model", "user-defined-code-model",
        "weak-grid-vsc", "gnanarathna-2011-efficient-mmc",
        "gruson-2011-reduced-mmc", "peralta-2012-detailed-mmc",
        "mtdc-model", "vsc-mmc-test-system",
    ],
    "basic-component": [  # 基本元件模型
        "resistor-model", "dc-rlc-filter", "load-model",
        "constant-power-load", "voltage-current-sensor-model",
        "diode-model", "igbt-model",
    ],
}

TOPICS_MAP = {
    "simulation": [  # 仿真技术与方法
        "co-simulation", "emt-simulation", "real-time-simulation",
        "hybrid-simulation", "time-domain-simulation",
        "fast-system-simulation", "large-scale-grid-simulation",
        "large-scale-hybrid-acdc-simulation", "large-scale-system-simulation",
        "large-scale-power-system", "digital-simulator",
        "emt-mathematical-foundation", "numerical-integration-methods",
        "numerical-stability", "steady-state-initialization",
        "parallel-computing",
        "fpga-real-time-simulation", "hardware-in-loop", "hil-simulation",
        "electromechanical-electromagnetic-hybrid-simulation",
    ],
    "modeling-methods": [  # 建模方法
        "frequency-dependent-modeling", "phase-domain-modeling",
        "time-domain-modeling", "network-equivalent",
        "model-order-reduction", "shifted-frequency-analysis",
        "phase-domain-model", "power-electronic-device-modeling",
        "multirate-and-network-partitioning", "network-partitioning",
        "network-equation-solution", "transmission-line-theory",
        "dynamic-phasor", "low-rank-and-efficient-solvers",
    ],
    "component-modeling": [  # 元件建模专题
        "load-modeling", "load-and-dg-modeling", "rotating-machine-modeling",
        "transformer-modeling", "transmission-line-modeling",
        "mmc-modeling", "cable-modeling", "power-electronics",
        "ferroresonance",
    ],
    "stability-analysis": [  # 稳定性分析
        "wideband-oscillation-stability", "transient-stability-analysis",
        "electromagnetic-transient", "electromechanical-transient",
        "harmonic-analysis", "switching-transient",
    ],
    "hvdc-facts": [  # HVDC 与 FACTS
        "vsc-hvdc", "facts", "hybrid-acdc-network", "hybrid-acdc-system",
        "dc-fault-blocking", "mt-hvdc-test-system", "fault-ride-through",
    ],
    "protection-lightning": [  # 保护与防雷
        "protection-system", "protection-relay-modeling",
        "grounding-lightning-overvoltage", "grounding-system",
        "ground-potential-rise", "lightning-overvoltage",
        "lightning-transient-analysis", "lightning-induced-voltage",
        "unbalanced-fault-analysis", "relay-protection",
    ],
    "renewable-storage": [  # 新能源与储能
        "renewable-energy-integration", "renewable-energy-units",
        "wind-farm-modeling", "pv-power-plant", "distributed-generation",
        "energy-storage-system", "microgrid-distribution-network",
        "dispatch-operation", "power-quality",
        "electromechanical-electromagnetic-hybrid",
    ],
    "test-system": [  # 测试系统
        "ieee-118-bus-system", "ieee-300-bus-system", "ieee-39-bus-system",
        "new-england-test-system", "microgrid-test-system",
        "svc-test-system", "model-verification-benchmark",
    ],
    "tools-software": [  # 工具与软件
        "emt-software-history", "tools-comparison-guide",
        "simulation-practice-guide", "power-system",
        "power-system-network", "transmission-network",
        "frequency-domain-analysis",
    ],
}

ENTITIES_MAP = {
    "institution": [  # 机构
        "cigre", "ieee", "china-epri", "tsinghua-university",
        "polytechnique-montreal", "university-manitoba", "manitoba-hydro",
    ],
    "software": [  # 软件工具
        "pscad-emtdc", "emtp", "atp-emtp", "matlab-simulink",
        "rtds", "cloudpss", "adpss", "psmodel", "ansys", "comsol",
    ],
    "industry": [  # 企业
        "abb", "siemens",
    ],
    "scholar": [  # 学者
        "adam-semlyen", "bjorn-gustavsen", "gole", "mahseredjian",
    ],
}


def get_mapping(category: str) -> dict:
    if category == "methods":
        return METHODS_MAP
    elif category == "models":
        return MODELS_MAP
    elif category == "topics":
        return TOPICS_MAP
    elif category == "entities":
        return ENTITIES_MAP
    return {}


def migrate_category(category: str, dry_run: bool = False):
    """迁移单个分类下的所有页面到二级子目录。"""
    mapping = get_mapping(category)
    if not mapping:
        print(f"分类 {category} 尚未配置映射，跳过")
        return 0

    cat_dir = WIKI_DIR / category
    if not cat_dir.exists():
        print(f"目录不存在: {cat_dir}")
        return 0

    slug_to_subdir = {}
    for subdir, slugs in mapping.items():
        for slug in slugs:
            slug_to_subdir[slug] = subdir

    moved = 0
    for f in sorted(cat_dir.glob("*.md")):
        slug = f.stem
        if slug in ("index", "_index"):
            continue
        if slug in slug_to_subdir:
            subdir = slug_to_subdir[slug]
            target_dir = cat_dir / subdir
            target = target_dir / f.name
            if dry_run:
                print(f"  [DRY-RUN] mv {f.relative_to(WIKI_DIR)} → {target.relative_to(WIKI_DIR)}")
            else:
                target_dir.mkdir(parents=True, exist_ok=True)
                os.rename(str(f), str(target))
                print(f"  ✓ {f.name} → {category}/{subdir}/")
            moved += 1
        else:
            print(f"  ⚠️  {f.name} 未分配二级分类，留在原处")

    return moved


def create_index_files(category: str, dry_run: bool = False):
    """为每个子目录创建 _index.md。"""
    mapping = get_mapping(category)
    cat_dir = WIKI_DIR / category

    for subdir, slugs in mapping.items():
        target_dir = cat_dir / subdir
        if not target_dir.exists():
            if not dry_run:
                target_dir.mkdir(parents=True, exist_ok=True)
            continue

        existing = []
        for slug in sorted(slugs):
            f = target_dir / f"{slug}.md"
            if f.exists():
                try:
                    content = f.read_text(encoding="utf-8")
                    title_match = re.search(r'^title:\s*"(.+)"', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else slug
                except Exception:
                    title = slug
                existing.append((slug, title))

        if not existing:
            continue

        lines = [
            "---",
            f'title: "{subdir} — {category}"',
            "---",
            "",
            f"# {subdir}",
            "",
            "| 页面 | 说明 |",
            "|------|------|",
        ]
        for slug, title in existing:
            lines.append(f"| [[{slug}|{title}]] | |")

        content = "\n".join(lines) + "\n"
        index_path = target_dir / "_index.md"

        if dry_run:
            print(f"  [DRY-RUN] 创建 {index_path.relative_to(WIKI_DIR)}")
        else:
            index_path.write_text(content, encoding="utf-8")
            print(f"  ✓ 创建 {index_path.relative_to(WIKI_DIR)}")


def main():
    parser = argparse.ArgumentParser(description="二级分类迁移")
    parser.add_argument("--category", choices=["methods", "models", "topics", "entities"],
                        help="仅处理指定分类")
    parser.add_argument("--dry-run", action="store_true", help="只预览不执行")
    parser.add_argument("--index-only", action="store_true", help="仅创建索引页")
    args = parser.parse_args()

    if args.category:
        categories = [args.category]
    else:
        categories = ["methods", "models", "topics", "entities"]

    for cat in categories:
        print(f"\n{'='*60}")
        print(f"分类: {cat}")
        print(f"{'='*60}")

        if not args.index_only:
            n = migrate_category(cat, dry_run=args.dry_run)
            print(f"  迁移: {n} 个页面")

        create_index_files(cat, dry_run=args.dry_run)

    print("\n完成。")


if __name__ == "__main__":
    main()
