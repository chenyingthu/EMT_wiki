# 二级分类目录重组方案

## Context

当前 wiki 使用平铺结构，methods/、models/、topics/、entities/ 四类目录下的所有页面直接放在一级目录中。以 methods/ 为例，253 个 .md 文件全部平铺在同一层，查找不便，缺乏领域组织。目标是建立二级子目录，将相关页面归类迁移。

## 分析结论

**wikilink 兼容性**：所有 wikilink 使用裸 slug 格式（`[[vector-fitting]]`），不含目录路径。但链接解析脚本（`wiki_lint.py`、`diagnostic_scan.py`、`build_backrefs.py`）硬编码了 `methods/{name}` 模式，移动文件到子目录后会将这些链接报告为断链。

**需要修改的核心脚本**：`tools/wiki_lint.py` 的 `resolve_link()` 函数（当前仅尝试 `{category}/{name}` 模式），`tools/diagnostic_scan.py` 的硬编码路径列表，`tools/build_backrefs.py` 的硬编码页面列表。

## 计划

### Step 1: 先修 — 升级链接解析工具

修改 `tools/wiki_lint.py` 的 `resolve_link()` 和 `get_all_wiki_pages()`，使其支持子目录递归查找。同时更新 `tools/diagnostic_scan.py` 和 `tools/build_backrefs.py`。

关键改动：
- `wiki_lint.py`: `resolve_link()` step 2 改为遍历 pages 字典，对每个 category 前缀查找 key 以 `/{name}` 结尾的条目
- `diagnostic_scan.py`: `possible_paths` 改为用 `os.walk` 或 `rglob` 构建
- `build_backrefs.py`: 页面发现改为 `rglob("*.md")` 动态扫描

### Step 2: methods/ 二级分类（10 个子目录）

| 子目录 | 中文名 | 页面数 | 包含内容示例 |
|--------|--------|--------|------------|
| numerical-methods/ | 数值方法与积分 | ~25 | numerical-integration, trapezoidal-rule, backward-euler, companion-circuit, discretization, stiff-system-handling, runge-kutta-in-emt 等 |
| network-solution/ | 网络求解与矩阵方法 | ~15 | nodal-analysis, sparse-matrix-solver, newton-raphson, state-space-method, iterative-solvers, thevenin-equivalent 等 |
| transmission-line/ | 输电线路与电缆建模 | ~30 | bergeron-line-model, universal-line-model, phase-domain-modeling, modal-transformation, cable, soil, corona 等 |
| power-electronics/ | 电力电子建模 | ~35 | switching-function, average-value-model, pwm, submodule (hbsm/fbsm/cdsm), dccb, converter, commutation-failure 等 |
| control/ | 控制方法与系统 | ~30 | dq-transformation, pll, vector-control, droop-control, grid-forming, hvdc-control, mppt 等 |
| stability-analysis/ | 稳定性与振荡分析 | ~25 | small-signal-stability, eigenvalue-analysis, transient-stability, impedance-modeling, frequency-scan, energy-function 等 |
| signal-processing/ | 信号处理与系统辨识 | ~25 | vector-fitting, fft, fourier, prony-analysis, hilbert-transform, least-squares, modal-analysis 等 |
| simulation-technology/ | 仿真技术与高性能计算 | ~25 | multirate-method, gpu-accelerated, fpga-real-time, hil-simulation, parallel-in-time, code-generation 等 |
| protection-fault/ | 保护与故障分析 | ~20 | fault-analysis, distance-protection, dc-protection, symmetrical-components, anti-islanding, ieee-1547 等 |
| system-studies/ | 系统分析与专题 | ~25 | back-to-back-hvdc, multi-terminal-dc, dfig-offshore, dynamic-phasor, power-flow, electromechanical-hybrid 等 |

### Step 3: models/ 二级分类（约 6 个子目录）

| 子目录 | 中文名 | 页面数 |
|--------|--------|--------|
| rotating-machine/ | 旋转电机模型 | ~15 | synchronous-machine, induction-machine, dfig, pmsm 等 |
| power-electronics/ | 电力电子模型 | ~20 | mmc, vsc, converter, inverter, submodule 等 |
| transformer/ | 变压器模型 | ~10 | transformer, magnetic, saturation 等 |
| line-cable/ | 线路电缆模型 | ~10 | transmission-line, cable, overhead-line 等 |
| control-protection/ | 控制保护模型 | ~10 | exciter, governor, pss, relay 等 |
| renewable-storage/ | 新能源与储能 | ~10 | wind-farm, pv-array, battery 等 |

### Step 4: topics/ 二级分类（约 6 个子目录）

| 子目录 | 中文名 | 页面数 |
|--------|--------|--------|
| simulation/ | 仿真技术主题 | ~20 | real-time-simulation, co-simulation, parallel-computing 等 |
| modeling/ | 建模方法主题 | ~15 | frequency-dependent-modeling, network-equivalent, dynamic-phasor 等 |
| stability/ | 稳定性主题 | ~15 | wideband-oscillation, harmonic-analysis, small-signal-stability 等 |
| hvdc-facts/ | HVDC 与 FACTS 主题 | ~15 | vsc-hvdc, mmc-hvdc, facts 等 |
| protection/ | 保护主题 | ~10 | protection, insulation-coordination, grounding 等 |
| renewable/ | 新能源主题 | ~10 | wind-farm, solar-integration, grid-code 等 |

### Step 5: entities/ 二级分类（约 3 个子目录）

| 子目录 | 中文名 | 页面数 |
|--------|--------|--------|
| institution/ | 机构 | ~10 | cigre, ieee, china-epri, tsinghua-university 等 |
| software/ | 软件工具 | ~8 | pscad, emtp, matlab-simulink, rtds 等 |
| scholar/ | 学者 | ~5 | mahseredjian, gustavsen, gole 等 |

### Step 6: 创建分类索引页

每个二级子目录创建 `_index.md`（用下划线前缀避免与正常页面命名冲突），列出该子目录下的页面。

### Step 7: 验证

1. 运行 `python3 tools/wiki_lint.py` 确认无新增断链
2. 运行 `python3 tools/strict_audit.py` 确认无孤立页面
3. 抽查 10 个页面手动验证 wikilink 跳转

## 关键文件清单

| 文件 | 操作 |
|------|------|
| `tools/wiki_lint.py` (resolve_link, get_all_wiki_pages) | 修改：支持子目录递归 |
| `tools/diagnostic_scan.py` (possible_paths) | 修改：支持子目录递归 |
| `tools/build_backrefs.py` (page_dirs) | 修改：动态发现页面 |
| `tools/fix_broken_links.py` (create_stub_page) | 修改：正确推断子目录 |
| `tools/add_diagrams_to_pages.py` | 确认兼容（rglob 已支持递归） |
| `wiki/index.md` | 更新分类计数和路径 |
| `wiki/methods/*.md` (253 个文件) | 迁移到子目录 |
| `wiki/models/*.md` (87 个文件) | 迁移到子目录 |
| `wiki/topics/*.md` (90 个文件) | 迁移到子目录 |
| `wiki/entities/*.md` (23 个文件) | 迁移到子目录 |

## 验证方式

1. `git mv` 迁移文件，保留 git 历史
2. `python3 tools/wiki_lint.py` 全量扫描检查断链
3. 对调后的 `resolve_link` 单元测试：裸 slug → 子目录路径
4. 随机抽取 20 个 wikilink 手动验证跳转正确性
