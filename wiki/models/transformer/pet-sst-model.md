---
title: "电力电子变压器 (PET/SST)"
type: model
tags: [pet, sst, solid-state-transformer, power-electronics, high-frequency, isolation, dab, chb, sab, mab]
created: "2026-04-29"
updated: "2026-05-18"
---

# 电力电子变压器 (Power Electronic Transformer / Solid-State Transformer)

## 定义与概述

电力电子变压器（PET）也称固态变压器（SST），是基于电力电子技术的新型智能变压器，通过 AC-DC-AC 多级变换实现电压等级转换和电气隔离。相比传统变压器，PET 具有体积小、功率双向流动、功率因数可控、谐波隔离和故障限流等优势。按拓扑结构划分，PET 主要分为三级式 AC-DC-DC-AC（整流级+隔离级+逆变级），隔离级按功率模块类型分为 CHB-DAB、CHB-SAB、CHB-MAB 三种路线。按等效建模粒度划分，EMT 仿真模型分为详细开关模型（SFB-DEM）、开关函数平均值模型（SFB-AVM）、恒导纳等效模型和多速率协同仿真模型。

**核心挑战**：大规模 ISOP/ISOS 级联 PET 的节点导纳矩阵阶数高、开关频率 10-100 kHz 导致步长受限微秒级，详细模型计算代价很高。不同隔离级拓扑（DAB/CLLC/SAB/MAB）的等效电路结构和 EMT 接口方式存在显著差异，需要针对性建模方法。

**关键需求**：
- 保留高频开关暂态（开关瞬态、触发脉冲时序）
- 减少 ISOP/ISOS 级联带来的网络矩阵节点膨胀
- 支持大步长实时仿真（RT-HIL）同时保持数值稳定性
- 多速率子系统协同（CHB 低频侧与 DAB 高频侧步长解耦）

## EMT 中的角色

PET 在 EMT 仿真中承担多电压等级变换和电气隔离的核心功能：

1. **配电系统接入**：10 kV/35 kV 中压输入 → 380 V/750 V 低压输出，连接配电网与微网/电动汽车充电
2. **新能源并网**：作为分布式能源与配电网之间的接口，实现 DC link 与 AC bus 的电压变换和功率控制
3. **HVDC 穿通**：MMC 型 SST 的 DAB 高频链路（HFL）在柔性直流输电中实现 DC-DC 隔离
4. **系统级仿真**：大步长等效模型用于保护继电器配合、谐波传播分析、电能质量评估

**EMT 建模的三个层级**：
- **详细开关层**（开关级，100 ns-1 μs）：保留 IGBT/MOSFET 开关暂态，用于器件级损耗分析和控制验证
- **等效端口层**（端口级，10-100 μs）：保留端口外特性，隐藏内部开关状态，用于系统级动态响应
- **平均等效层**（周期平均，100-500 μs）：基于开关函数平均化，用于稳态功率流和长期动态

## EMT 建模方法

### 方法 1：开关函数详细等效模型（SFB-DEM）

**核心思想**：用开关函数 $s(t) \in \{-1, 0, 1\}$ 描述各桥臂对直流电容电压和端口电压的映射，将开关半导体网络改写为等效电路接口，使网络求解的节点导纳矩阵 **G 矩阵不随开关动作变化**，避免每步 LU 分解。

**DAB 桥臂电压**：

$$
v_{p}(t) = V_{dc1} \cdot s_1(t), \quad s_1 \in \{-1, 0, 1\}
$$

$$
v_{s}(t) = n \cdot V_{dc2} \cdot s_2(t), \quad s_2 \in \{-1, 0, 1\}
$$

**变压器漏感方程**：

$$
v_{p} - v_{s} = L_{leak} \frac{di_{L}}{dt}
$$

**SFB-DEM 的 G 矩阵固定化机制**：利用 DAB 桥臂互补导通特性 $G_{ON} + G_{OFF} = G_x$ 为常数，使内部节点块可预先计算并在端口层面递归消除（Kron 消去）。ISOP 配置下多 DAB 模块可在端口层面聚合进入 EMT 网络求解，节点数从 $6N+1$ 降至 $2N+3$。

**适用范围**：ISOP/ISOS/IPOP/IPOS 多种串并联配置、多模块 SST 系统级仿真、RT-HIL 实时仿真
**失效场景**：开关器件的非理想特性（反向恢复、结电容）、磁芯饱和故障、热耦合动态

### 方法 2：开关函数平均值模型（SFB-AVM）

**核心思想**：对开关函数在一个仿真步长内按触发占空比 $\beta$ 做时间平均，将离散的开关状态转化为连续等效：

$$
\bar{s} = \frac{\tau_{on}}{T_s} = \beta
$$

**DAB 等效电压源**：

$$
\bar{v}_p = \beta_1 V_{dc1}, \quad \bar{v}_s = n \beta_2 V_{dc2}
$$

**平均传输功率**：

$$
\bar{P} = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \phi (1 - \frac{|\phi|}{\pi})
$$

**IFP（interpolated firing pulse）机制**：触发脉冲在步长内部发生时，用 $\beta = \tau_{on}/T_s$ 代替整步长恒定假设，避免步端触发延迟引入直流偏置。

**适用范围**：控制参数设计、稳态效率评估、长期动态（热松弛）仿真
**失效场景**：需要保留开关谐波和高频暂态的场景、快速故障暂态

### 方法 3：恒导纳等效模型

**核心思想**：将 DAB 高频链路等效为端口导纳 $G_{eq}$ 和历史电流源的并联，接口方程为：

$$
i_{port} = G_{eq} \cdot v_{port} + i_{hist}(t-\Delta t)
$$

**DAB 恒导纳**：

$$
G_{eq,DAB} = \frac{P_{rated}}{V_{dc1}^2 - V_{dc2}^2/n^2}
$$

**优势**：单步矩阵求逆运算量为 $O(N)$ 而非 $O(N^3)$，适合大规模 ISOP 级联 PET 的系统级 EMT 仿真。

**适用范围**：需要快速仿真的系统级 EMT 场景、保护继电器配合仿真
**失效场景**：开关暂态详细分析、非线性磁芯动态

### 方法 4：多速率协同仿真模型

**核心思想**：利用 PET 多级变换电路的固有频率差异，将 CHB 慢速子系统（~500 Hz）与 DAB 快速子系统（kHz 级）分配不同步长，避免低频部分被迫以高频步长求解。

**步长比例**：CHB 取 50-100 μs，DAB 取 1-10 μs，比例 10:1~20:1。

**跨速率数据传输机制**：接口处用等效电压/电流边界量传递信息，使各子系统可独立组装和求解，避免因开关状态变化或跨区耦合频繁重构整个系统矩阵。

**DAB 端口等效**：以高频变压器两侧电流 $i_L(t)$ 作为状态变量，由改进节点分析（MNA）建立方程：

$$
\mathbf{A} \mathbf{x}_{DAB} = \mathbf{b}(v_{port}, i_{hist})
$$

高精度触发信号进入 DAB 方程后，开关发生时刻不必完全受固定仿真步长网格限制。

**适用范围**：含 CHB-DAB 拓扑的大规模 PET 仿真、兼顾慢速控制和快速开关的协同仿真
**失效场景**：强非线性耦合、故障暂态下多速率稳定性边界不清晰

### 方法 5：广义状态空间平均模型（GSSA/GSSM）

**核心思想**：对 DAB 交流链路电流/电压的开关周期波形展开为傅里叶系数（动态相量），将周期信号转化为随时间缓慢变化的相量：

$$
x(t) = \sum_{k} X_k(t) e^{jk\omega_s t}
$$

**动态相量微分性质**（引入 $-jk\omega_s$ 频移项）：

$$
\frac{dX_k}{dt} = \frac{1}{T_s}\left[ -jk\omega_s X_k + (x(t) e^{-jk\omega_s t}\right]_{avg}
$$

**混合 SSA/GSSA 小信号建模**：直流端口用 SSA 表示，变压器交流侧用 GSSA 表示，形成混合框架用于求取 3p-DAB 开环传递函数 $G_{vd}(s)$、$G_{vg}(s)$、驱动点输入阻抗 $Z_D(s)$、输出阻抗 $Z_o(s)$ 等。

**适用范围**：小信号稳定性分析、DAB 阻抗建模、控制器带宽设计
**失效场景**：大信号故障暂态、非周期谐波动态

## 形式化表达

### DAB 移相控制方程

**单移相（SPS）传输功率**：

$$
P_{SPS} = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \phi \left(1 - \frac{|\phi|}{\pi}\right), \quad \phi \in [-\frac{\pi}{2}, \frac{\pi}{2}]
$$

**回流功率**：

$$
Q = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \left[ \phi\left(1-\frac{\phi}{\pi}\right) - \frac{d(1-d)^2 \pi}{4} \right]
$$

其中 $d = V_{dc2}/(nV_{dc1})$ 为电压传输比。

**扩展移相（EPS）传输功率**：

$$
P_{EPS} = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \phi_2 \left(1 - \phi_2 - \frac{\phi_1}{2}\right)
$$

其中 $\phi_1$ 为原边 H 桥内移相，$\phi_2$ 为两桥间外移相。

### CLLC 谐振变换器

**谐振频率**：

$$
f_r = \frac{1}{2\pi\sqrt{L_r C_r}}
$$

**电压增益**：

$$
M_g = \frac{V_{out}}{n V_{in}} = \frac{1}{\sqrt{\left(1+k-\frac{k}{F^2}\right)^2 + Q^2\left(F-\frac{1}{F}\right)^2}}
$$

其中 $k = L_m/L_r$，$Q = \sqrt{L_r/C_r}/R_{eq}$，$F = f_s/f_r$。

**ZVS 软开关条件（原边）**：

$$
f_s \geq f_r \quad \text{或} \quad I_{mag} > \frac{2 C_{oss} V_{dc}}{t_{dead}}
$$

## 关键技术挑战

### 挑战 1：ISOP/ISOS 级联网络的矩阵膨胀

当 PET 采用输入串联、输出并联（ISOP）或输入串联、输出串联（ISOS）配置时，$N$ 个子模块的串联导致节点导纳矩阵规模为 $O(N)$，开关状态变化引起的矩阵重构成为实时仿真的主要瓶颈。**解法**：利用互补导通特性实现 G 矩阵固定化，通过 Kron 消去在端口层面聚合。

### 挑战 2：步内开关事件的时序精度

百 kHz 级 DAB 的触发脉冲可能落在仿真步长内部，若只在步长起点更新开关状态，会造成触发时刻误差并在交流变压器电流中引入直流偏置。**解法**：IFP（步内触发等效）和开关插值算法（对切换时刻附近状态量修正）。

### 挑战 3：Stage I/II 两级耦合

整流级（Stage I）与隔离级（Stage II）通过直流电容强耦合，电容电压作为两级共享状态导致联立求解时的数值刚性增加。**解法**：DC-link 解耦（在直流电容处切断两级直接耦合）或 ImEx-Gear 显隐多步法（显式处理电容变量，隐式处理电感/电阻网络）。

### 挑战 4：多速率稳定性边界

多速率仿真中，慢速 CHB 与快速 DAB 子系统的交互边界在故障暂态下可能失稳。**解法**：精确的接口等效和时序交错（interleaved equivalence multirate interaction algorithm）。

### 挑战 5：磁芯非线性和热耦合

SST 高频变压器的磁芯饱和特性与开关损耗产生的热耦合，在 EMT 中通常简化处理。**解法**：需要额外的饱和模型和热网络，目前文献中尚未系统验证。

## 量化性能边界

### 加速比数据

| 建模方法 | 测试配置 | 步长 | 加速比 | 来源 |
|---------|---------|------|--------|------|
| SFB-DEM + ImEx-G3O | 60 SM ISOP SST | 20-50 μs | **171×** vs 详细模型；**7.5×** vs VG-DEM | Li 2026 |
| 端口导纳预处理 + Kron 消去 | MMC型SST DAB-HFL | 1-10 μs | **10-100×**（1-2 数量级），特定工况达 2-3 数量级 | Gao 2022 |
| SFB-DEM / SFB-AVM | 10相 FBSM + 30 DAB + NPC三电平 | 20-50 μs | 波形偏差 **<0.5%**，相关系数 >0.99 | Li 2025 |
| 多速率（CHB-DAB）| CHB-DAB ISOP PET | CHB 50-100 μs, DAB 1-10 μs | 数值运算次数减少（原文未量化） | Wang 2025 |

### 节点数缩减

| 等效方法 | 原始节点数 | 等效后节点数 | 缩减比例 |
|---------|-----------|-------------|---------|
| SFB-DEM（ISOP） | $6N+1$ | $2N+3$ | ~67% |
| SFB-AVM（ISOP） | $6N+1$ | 3-5 | ~95% |
| 恒定导纳等效（ISOP） | $6N+1$ | 块对角三级独立 | ~60%（矩阵稀疏化） |

**数据缺口声明**：不同论文的测试基准不统一（详细模型步长从 1 μs 到详细开关级别不一致），横向对比加速比时需注意基准定义差异。大多数验证在离线 EMT 环境（PSCAD/EMTDC）完成，实时硬件平台（OPAL-RT/RTDS/FPGA）数据仅 Li 2026 报告。

## 适用边界与选择指南

| 应用场景 | 推荐模型 | 步长 | 精度目标 | 关键判据 |
|---------|---------|------|---------|---------|
| 器件级损耗分析 | SFB-DEM | 100 ns-1 μs | 开关瞬态精度 | 触发脉冲时序精度 |
| 控制参数设计 | SFB-AVM / GSSA | 10-100 μs | 周期平均精度 | 控制传递函数匹配 |
| 系统级稳态/长期动态 | 恒导纳等效 | 100-500 μs | 端口外特性 | 功率平衡误差 <1% |
| RT-HIL 实时仿真 | SFB-DEM + ImEx-Gear | 20-50 μs | 稳态误差 <0.5% | 单步 $O(N)$ 复杂度 |
| 小信号稳定性分析 | GSSA/动态相量 | 频域扫频 | 阻抗精度 | 频率分辨率 |
| 多速率协同仿真 | CHB-DAB 多速率 | CHB 50-100 μs, DAB 1-10 μs | 子系统接口精度 | 步长比例 10:1~20:1 |

**拓扑选型参考**：
- **CHB-DAB**：适合高压输入（10 kV+）多级串联场景，控制成熟，但 DAB 高频开关仍是仿真瓶颈
- **CHB-SAB**（双主动桥串联谐振）：适合宽电压范围、高效率（>98%）需求
- **CHB-MAB**（多主动桥）：适合需要双向功率灵活分配的多端口应用

## 相关方法
- [[methods/power-electronics/average-value-model.md|average-value-model]] - DAB/CLLC 平均值建模
- [[methods/numerical-methods/state-space-method.md|state-space-method]] - SST 状态空间建模
- [[methods/numerical-methods/fixed-admittance.md|fixed-admittance]] - 高频变换器恒导纳实现
- [[methods/system-studies/dynamic-phasor.md|dynamic-phasor]] - SST 动态相量简化

## 相关模型
- [[models/converter/vsc-model.md|vsc-model]] - 整流/逆变级建模
- [[models/converter/mmc-model.md|mmc-model]] - MMC 型 SST 对比
- [[models/transformer/transformer-model.md|transformer-model]] - 高频变压器建模
- [[models/compensation/emi-filter-model.md|emi-filter-model]] - 高频噪声滤波

## 相关主题
- [[topics/hvdc-facts/vsc-hvdc.md|vsc-hvdc]] - 柔性直流输电
- [[topics/simulation/real-time-simulation.md|real-time-simulation]] - SST 实时仿真
- [[topics/simulation/co-simulation.md|co-simulation]] - SST 多域混合仿真
- [[topics/modeling-methods/frequency-dependent-modeling.md|frequency-dependent-modeling]] - 宽频变压器建模

## 来源论文
- [[sources/accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf.md]] — Gao 2022, MMC型SST DAB高频链路端口导纳等效，Kron消去加速
- [[sources/a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta.md]] — Li 2026, SFB-DEM + ImEx-Gear 实时仿真，60模块ISOP SST
- [[sources/universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc.md]] — Li 2025, 通用解耦等效电路模型，恒定G矩阵
- [[sources/multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi.md]] — Wang 2025, CHB-DAB多速率EMT仿真，步长比例10:1~20:1