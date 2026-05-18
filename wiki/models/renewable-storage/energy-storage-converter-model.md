---
title: "储能变流器 (Energy Storage Converter)"
type: model
tags: [energy-storage, converter, bess, battery, grid-scale, frequency-regulation, mmc-bess, vsm, gfm]
created: "2026-04-30"
updated: "2026-05-18"
---

# 储能变流器 (Energy Storage Converter)

## 定义与物理对象

储能变流器（Energy Storage Converter/PCS）是连接储能电池与电网的电力电子接口，实现电池直流电与交流电网之间的双向能量转换。其核心功能包括双向 AC/DC 功率转换、电池充放电管理、有功/无功独立调节、并网/离网模式切换，以及在构网型模式下提供黑启动能力。根据功率等级和应用场景，储能变流器可分为户用储能（3–20 kW）、工商业储能（100 kW–2 MW）、电网级储能（10–100 MW）和高压直挂储能（10–100 MW，10–35 kV）四类。

在 EMT 仿真中，储能变流器的建模挑战主要体现在两个层面：**一是电池-变流器耦合系统的多速率动态**（电池化学过程为秒至分钟级，变流器开关为微秒级），**二是并离网切换和构网型控制带来的接口不连续性**（从电流源模式切换至电压源模式）。储能变流器的 EMT 建模需要同时保留电池动态、DC-DC 变换器开关细节、桥臂/子模块级耦合，以及并网/离网控制模式的完整性。

## EMT 中的角色

储能变流器在 EMT 仿真中承担多重角色：

1. **调频调峰资源**：提供一次调频（ droop ）和二次调频（ AGC ）响应，其功率-频率特性直接影响系统惯性评估
2. **故障穿越接口**：在电网故障时提供无功支撑（LVRT），需准确建模变流器限流特性和闭锁行为
3. **黑启动电源**：构网型 PCS 可自主建立电压频率，需精确模拟启动瞬态和模式切换
4. **并网/离网切换节点**：切换过程涉及 PLL 同步、电压匹配和控制模式转换，需逐时步验证稳定性

关键建模需求：
- 电池 SOC 与变流器功率限制的耦合（ SOC 限功率机制）
- 双向 DC-DC 变换器（ Buck-Boost ）的开关动态
- MMC 嵌入储能时的多阀臂等效（ multivalve Thevenin equivalent ）
- 构网型/跟网型控制模式的 EMT 接口等效

## EMT 建模方法

储能变流器的 EMT 建模方法按精度-效率权衡分为五个层次，从详细开关模型到系统级平均值模型，形成完整的技术谱系。

### 方法 1：详细开关模型（DSM）

**基本原理**：将储能变流器内所有功率器件（IGBT、二极管、DC-DC 开关管）按实际开关状态建模，采用 Dommel 梯形积分法将电容、电感离散为伴随电路（ companion model ）。

电容伴随模型：
$$v_C(t) = R_C \cdot i_C(t) + V_{C,\mathrm{eq}}(t - \Delta t)$$

其中等效电阻和历史电压项为：
$$R_C = \frac{\Delta t}{2C}, \quad V_{C,\mathrm{eq}}(t - \Delta t) = v_C(t - \Delta t) + \frac{\Delta t}{2C} i_C(t - \Delta t)$$

电感伴随模型：
$$v_L(t) = R_L \cdot i_L(t) + V_{L,\mathrm{eq}}(t - \Delta t)$$

其中：
$$R_L = \frac{2L}{\Delta t}, \quad V_{L,\mathrm{eq}}(t - \Delta t) = -v_L(t - \Delta t) - \frac{2L}{\Delta t} i_L(t - \Delta t)$$

**IGBT-二极管对建模**：将每对器件建模为双态电阻——导通时 $R_{\mathrm{on}}$（毫欧级），关断时 $R_{\mathrm{off}}$（兆欧级）。

**SOC 动态**：考虑充放电效率的 SOC 更新方程为：
$$P_{\mathrm{PCS}} = P_{\mathrm{bat}} \cdot \eta_{\mathrm{PCS}} - P_{\mathrm{loss}}$$

其中 $\eta_{\mathrm{PCS}}$ 为变流器往返效率（ 90%–95% ）。

**特点**：精度最高，保留所有开关细节；计算量随子模块数量线性增长，不适合大规模 MMC-BESS 的参数扫描研究。

### 方法 2：详细等效模型（DEM / IDEM）

**基本原理**：利用梯形积分法将电容、电感和电池 Rint 模型离散为诺顿/戴维南等效电路后，将多阀臂（ multivalve ）中所有串联子模块的戴维南参数串联聚合，对外仅保留端口等效电压和电阻，从而将开关网络从系统导纳矩阵中消除。

**多阀臂戴维南等效**：
$$v_{\mathrm{MV,thev}} = \sum_{i=1}^{N} v_{\mathrm{SM,thev},i}$$
$$R_{\mathrm{MV,thev}} = \sum_{i=1}^{N} R_{\mathrm{SM,thev},i}$$

**IDEM 改进**（Wang 2025）：针对传统 DEM 在同一桥臂上下开关同时关断（闭锁或电池断开）时失效的问题，引入 PSCAD 辅助开关和内置插值算法精确捕捉电流过零点，并针对电池断开提出补充决策公式：

电池断开时 T3 二极管导通判据：
$$R_3 \approx \begin{cases} R_{\mathrm{on}}, & V_{\mathrm{bat}} - v_L - i_L R_{\mathrm{bat}} - v_C \ge v_f \\ R_{\mathrm{off}}, & V_{\mathrm{bat}} - v_L - i_L R_{\mathrm{bat}} - v_C < v_f \end{cases}$$

其中 $v_f$ 为二极管正向导通压降阈值。

**加速计算**：通过预置 6 种有效开关状态组合的查表法，将单步长内加法与乘法运算次数减少约 50%–70%。系统导纳矩阵维度从 $O(N)$（ $N$ 为子模块数）降至常数级，彻底消除大规模矩阵重复三角分解的计算瓶颈。

**IDEM 量化性能**：
- 仿真波形与 DSM 高度吻合，误差 < 1%（Wang 2025）
- 矩阵维度固定为常数级（仅 6 个多阀臂开关节点）
- 加速比：单步长运算减少 50%–70%

### 方法 3：平均值模型（AVM）

**基本原理**：对子模块内双向 DC-DC 变换器进行状态空间平均化处理，忽略高频开关细节，用占空比 $d$ 描述电池侧与电容侧的平均能量交换。

**DC-DC 状态空间平均化**：
$$\frac{di_L}{dt} = \frac{1}{L_{\mathrm{SM}}} v_{\mathrm{bat}} - \frac{1}{L_{\mathrm{SM}}} (1-d) v_C$$

**电容电压动态**（考虑 DC-DC 输出电流和桥臂调制电流）：
$$v_{C,j}^k = \frac{1}{C_{\mathrm{SM}}} \int \left[ (1-d_{kj}) i_{L,j}^k + m_{kj} i_{kj} \right] dt$$

**多阀臂级 AVM 等效**：将 $N$ 个子模块串联等效为受控电压源：
$$v^{\mathrm{up}} = N m_{\mathrm{up}} \frac{1}{C_{\mathrm{SM}}} \int \left[ (1-d_{\mathrm{up}}) i_L^{\mathrm{up}} + m_{\mathrm{up}} i^{\mathrm{up}} \right] dt$$

串联等效导通电阻 $R_{\mathrm{MV}} = N \cdot R_{\mathrm{on}}$。

**二次谐波环流解析**（Herath 2021）：
$$v_{2L} = \frac{3N m \hat{i}_s}{16\omega C_{\mathrm{SM}}} \sin(2\omega t + \alpha) - \frac{2N m^2 + 3N}{12\omega C_{\mathrm{SM}}} \hat{i}_2^{\circ} \sin(2\omega t + \phi_2^{\circ})$$

**AVM 量化性能**（Herath 2021）：
- 仿真计算效率较详细 EMT 开关模型提升约 80–90 倍
- 二次谐波环流幅值解析预测误差 < 1.5%，相位偏差 < 2°
- 子模块电容电压纹波峰值计算误差 < 1.0%
- 等效多阀臂电阻引入的导通损耗计算误差 < 2%

### 方法 4：构网型（GFM）储能变流器模型

**基本原理**：构网型变流器自主建立电压和频率，无需 PLL 跟踪电网，实现零电网阻抗条件下的稳定并网。

**虚拟同步机（VSM）控制**：模拟同步发电机的转子运动方程：
$$2H \frac{d\omega}{dt} = P_{\mathrm{ref}} - P_e - D (\omega - \omega_0)$$

其中 $H$ 为虚拟惯性常数，$D$ 为阻尼系数，$P_{\mathrm{ref}}$ 为机械功率指令，$P_e$ 为电磁功率。

**PQ 运行域约束**：GFM 逆变器的运行域受电流限幅和温度降额约束：
$$|S| \le S_{\mathrm{rated}}, \quad I \le I_{\mathrm{max}}$$
其中视在功率 $S = \sqrt{P^2 + Q^2}$，电流 $I = |S| / V$。

**黑启动序列**（Nguyen 2021）：光储混合系统黑启动分 7 步完成，总时间约 18 s，稳态电压误差 < 1%：
1. 预充电阶段：DC-DC 升压建立 DC 总线电压
2. GFM 启动：变流器建立内部电压参考
3. 同步检测：检测 AC 侧电压幅值/相位匹配
4. 并网闭合：AC 接触器闭合
5. 功率提升：逐步增加有功功率至目标值
6. 无功支撑：按电网需求调整无功输出
7. 移交控制：转至上级 EMS 或 AGC 控制

**量化性能**（Nguyen 2021）：
- 黑启动全过程 18 s（7 步）
- 母线电压恢复时间 < 0.2 s
- 最大负荷阶跃 120.2 MW + 42.3 Mvar，构网逆变器成功支撑
- 稳态电压误差 < 1%

**EVR + CPID 控制**（Nurunnabi 2025）：增强电压调节（EVR）和受控比例-积分-下垂（CPID）策略在 L/LC/LCL 滤波器配置下改善了 GFM 逆变器的电压和频率稳定性。

### 方法 5：大规模 BESS 并行加速模型

**基本原理**（Lin 2023）：采用 CPU-GPU 异构架构，将大量分布式 BESS 的设备级 EMT 计算映射到 GPU 多线程并行执行，系统级机电暂态（TS）在 CPU 上以毫秒步长推进，两者在多速率框架下周期性交换数据。

**向量化电池建模**：将不同化学类型（锂离子、铅酸、镍镉）电池的 Thevenin 等效模型转化为同构向量形式，以适配 GPU 的细粒度 SIMT 并行架构。每个线程处理一个电池单元的状态更新：
$$V_{\mathrm{bat}} = V_{\mathrm{oc}}(SOC) - R_{\mathrm{int}}(SOC, T) \cdot I_{\mathrm{bat}}$$

指数区电压动态通过离散递推更新，SOC 由电流对容量积分得到。

**多速率耦合机制**：TS 步长（毫秒级）与 EMT 步长（微秒级）通过周期性数据映射交换——在一个 TS 步长内执行若干 EMT 子步，将 EMT 侧等效量汇总后传给 TS 侧，同时把 TS 侧电网边界条件传回设备侧。

**CUDA 多流异步处理**：利用 CUDA 多流技术使内核计算、主机-设备数据传输和接口数据整理尽量重叠，掩盖 PCIe 传输延迟。

**量化性能**（Lin 2023）：
- CPU-GPU 异构架构在含大量 BESS 的 IEEE 118 节点交直流系统中实现加速比 > 200 倍
- 设备级精度与 MATLAB/Simulink 验证一致
- 系统级暂态稳定性与 DSATools/TSAT 验证一致
- 仿真步长：EMT 微秒级（10–50 μs），TS 毫秒级

## 关键技术挑战

### 挑战 1：SOC 限功率与变流器额定功率的耦合

电池 SOC 状态直接限制充放电功率，而 EMT 仿真中若将 SOC 简化为恒定值，会导致故障穿越仿真的功率支撑能力严重高估。SOC 限功率模型需考虑：
$$P_{\mathrm{max,dis}} = P_{\mathrm{rated}} \cdot \min\left(1, \frac{SOC - SOC_{\mathrm{min}}}{SOC_{\mathrm{safe}} - SOC_{\mathrm{min}}}\right)$$
$$P_{\mathrm{max,ch}} = P_{\mathrm{rated}} \cdot \min\left(1, \frac{SOC_{\mathrm{max}} - SOC}{SOC_{\mathrm{max}} - SOC_{\mathrm{safe}}}\right)$$

**问题**：此约束与变流器电流限幅（$I_{\mathrm{max}}$）和 DC-DC 占空比约束（$d \in [0,1]$）共同构成三层限幅，任何一层超限都会触发变流器保护动作。

### 挑战 2：DC-DC 变换器与 MMC 桥臂的双向耦合

当 MMC 子模块内嵌入双向 Buck-Boost DC-DC 变换器时，电池侧动态（$i_{\mathrm{bat}}$）通过 DC-DC 占空比 $d$ 影响子模块电容电压 $v_C$，而 $v_C$ 又通过调制函数 $m$ 决定桥臂电流 $i_{\mathrm{arm}}$，形成双向耦合链：
$$\text{Battery } i_{\mathrm{bat}} \xrightarrow{d} \text{ DC-DC } v_{\mathrm{dc}} \xrightarrow{C_{\mathrm{SM}}} v_C \xrightarrow{m} i_{\mathrm{arm}} \xrightarrow{\text{调制}} \text{AC side }$$

**问题**：该耦合链的时域稳定性分析需同时考虑电池化学时间常数（秒级）和开关时间常数（微秒级），传统线性化方法难以覆盖全频段稳定性。

### 挑战 3：并离网切换的暂态不连续性

从 GFL（跟网型）切换至 GFM（构网型）模式时，PLL 同步相位与 GFM 自主电压之间存在暂态差，当相位差超过阈值时会产生冲击电流：
$$\Delta i = \frac{\Delta V}{Z_{\mathrm{filter}}}$$

**问题**：切换过程中若不采取预同步措施，冲击电流可达额定电流的 2–3 倍，可能触发变流器过流保护。

### 挑战 4：MMC-BESS 闭锁状态的二极管路径判定

在 MMC-BESS 闭锁时，同一桥臂上下 IGBT 同时关断，仅二极管构成电流通路。传统 DEM 在此条件下依赖固定步长符号判断二极管导通/关断，存在电流过零误差累积问题。

**IDEM 解法**（Wang 2025）：使用 PSCAD 辅助开关和内置插值算法精确捕捉电流过零点，动态更新等效电阻：
$$R_{\mathrm{SM\_in}} = R_C \parallel \left[ R_3 + R_4 \parallel (R_L + R_{\mathrm{bat}}) \right]$$

### 挑战 5：大规模 BESS 阵列的并行计算边界

GPU 并行 BESS 建模的加速比受以下因素约束：
- **数据传输比例**：每个 EMT 子步需通过 PCIe 将设备边界量传回 CPU，当 BESS 数量超过某一阈值时，通信开销开始抵消并行收益
- **矩阵条件数**：大量同构电池模型导致系统矩阵特征值聚集，求解迭代次数增加
- **实时性约束**：FPGA 超实时仿真（亚微秒步长）受硬件资源限制，单板 BESS 规模上限约 50 个子模块

## 量化性能边界

**MMC-BESS 混合模型**（Wang 2025、Lin 2023）：

| 参数 | 数值 | 来源 |
|------|------|------|
| 仿真误差（vs DSM） | < 1% | Wang 2025 |
| 单步长运算减少 | 50%–70% | Wang 2025 |
| 加速比（vs DSM） | 10× 以上 | Wang 2025 |
| CPU-GPU 异构加速比 | > 200× | Lin 2023 |
| EMT 步长 | 10–50 μs | Lin 2023 |
| 适用系统规模 | IEEE 118 节点 AC/DC | Lin 2023 |

**DC-DC 谐振特性**（Luo 2022）：

| 参数 | 数值 | 来源 |
|------|------|------|
| Buck 模式自然谐振频率 | 118 Hz（理论值） | Luo 2022 |
| 阻抗模型误差 | < 2.5% | Luo 2022 |
| 支撑电容有效阈值 | > 0.5 mF | Luo 2022 |
| 有源阻尼控制器增益上界 | 存在约束，超限产生负电阻 | Luo 2022 |

**构网型 PCS 黑启动**（Nguyen 2021）：

| 参数 | 数值 | 来源 |
|------|------|------|
| 黑启动全过程 | 18 s（7 步） | Nguyen 2021 |
| 稳态电压误差 | < 1% | Nguyen 2021 |
| 母线电压恢复时间 | < 0.2 s | Nguyen 2021 |
| 最大负荷阶跃 | 120.2 MW + 42.3 Mvar | Nguyen 2021 |

**FPGA 超实时 BESS 仿真**（Cao 2023）：

| 参数 | 数值 | 来源 |
|------|------|------|
| FPGA 加速比 | 51× 超实时 | Cao 2023 |
| 仿真步长 | 亚微秒级 | Cao 2023 |

**数据缺口声明**：储能变流器在不同功率等级（kW 至 MW 级）和不同拓扑（单级式/两级式/MMC 嵌入式）下的效率-损耗建模数据缺乏系统公开对比。PCS 在不同电池类型（LFP/NCM/LTO）下的阻抗特性和控制参数整定缺乏统一基准。多 PCS 并联运行时 SOC 均衡控制策略的动态响应和稳态误差的定量数据不足。构网型 PCS 在弱电网（SCR < 2）下的暂态稳定边界缺乏系统验证。

## 适用边界与选择指南

| 场景 | 推荐模型 | 理由 |
|------|----------|------|
| 参数扫描/优化研究 | IDEM / AVM | 保留关键动态的同时大幅降低计算量 |
| 故障穿越仿真（闭锁/电池断开） | IDEM | 精确处理双开关同时关断情形 |
| 系统级规划仿真 | AVM | 毫秒步长，支持环流和纹波解析分析 |
| 大规模 BESS 阵列并行仿真 | GPU 向量化模型 | > 200× 加速，适合 100+ BESS 场景 |
| 构网型黑启动研究 | GFM-VSM 模型 | 自主建压，支持零电网条件启动 |
| FPGA 超实时硬件在环 | DSM（定点实现） | 亚微秒步长，51× 超实时加速 |
| 并网/离网切换瞬态 | DSM / IDEM + 模式切换逻辑 | 逐时步捕捉切换冲击电流 |

**模型选择决策树**：
1. 若需要零误差参考基准 → **DSM**（但计算量最大）
2. 若关注闭锁/电池断开工况 → **IDEM**（含补充判据）
3. 若进行系统级规划研究（秒至分钟级） → **AVM**（80–90× 加速）
4. 若 BESS 数量 > 50 且需参数扫描 → **GPU 并行模型**（> 200× 加速）
5. 若零电网阻抗条件建压 → **GFM-VSM 模型**（黑启动能力）
6. 若实时硬件在环 → **FPGA DSM**（亚微秒步长）

## 相关模型

- [[bess-model|电池储能系统]] — 电池侧详细模型（电化学等效电路、SOC 模型）
- [[gfl-inverter-model|跟网型变流器]] — 并网电流源控制策略
- [[gfm-inverter-model|构网型变流器]] — 孤岛/黑启动电压源控制策略
- [[mmc-model|MMC 模型]] — MMC 桥臂与子模块结构
- [[average-value-model|平均值模型]] — 系统级 EMT 简化建模框架
- [[dem|详细等效模型]] — MMC 多阀臂端口等效方法
- [[pi-controller-model|PI 控制器]] — 功率环与电流环控制
- [[pll-model|锁相环]] — 并网同步相位提取
- [[droop-control-model|下垂控制]] — 功率均分与频率支撑

## 相关方法

- [[numerical-integration|数值积分]] — SOC 计算的离散化方法（梯形积分法、状态空间平均化）
- [[state-space-method|状态空间法]] — 变流器状态分析（连续/离散状态方程）
- [[emt-simulation|EMT 仿真]] — 储能变流器的时域仿真框架
- [[large-scale-system-simulation|大规模系统仿真]] — GPU/CPU 异构并行加速

## 相关主题

- 频率调节 — 一次调频（droop）和二次调频（AGC）的功率-频率特性
- 黑启动 — 构网型 PCS 在微电网中的应急支撑能力
- 微电网 — 并离网切换与多模式运行
- 削峰填谷 — 能量套利与经济运行优化
- MMC-BESS — 模块化多电平换流器嵌入式储能
- 虚拟同步机（VSM）— 构网型控制的同步机模拟技术
- DC-DC 变换器 — Buck-Boost 双向接口

---

## 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Wang 等 — An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions | 2025 | IDEM（含闭锁/电池断开补充判据）、查表加速、PSCAD 辅助开关 |
| Herath 等 — Modeling of a Modular Multilevel Converter With Embedded Energy Storage | 2019 | DEM 多阀臂 Thevenin 等效、梯形积分伴随模型、100× 加速 |
| Herath 和 Filizadeh — Average-Value Model for a Modular Multilevel Converter With Embedded Storage | 2021 | 多阀臂级 AVM、状态空间平均化、80–90× 加速、环流谐波解析 |
| Lin 等 — Massively Parallel Modeling of BESS for AC/DC Grid High-Performance Transient Simulation | 2023 | CPU-GPU 异构并行、向量化建模、多速率 EMT-TS 耦合、> 200× 加速 |
| Nurunnabi 等 — Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis | 2025 | GFM PQ 运行域、EVR+CPID 控制、L/LC/LCL 滤波器配置 |
| Nguyen 等 — Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants | 2021 | GFM 黑启动序列（7 步/18 s）、光储混合系统 |
| Luo 等 — Active Damping Control and Parameter Calculation for Resonance Suppression in DC Distribution | 2022 | Buck 模式串联谐振 118 Hz、有源阻尼控制器增益约束 |
| Cao 等 — FPGA Real-Time BESS Simulation | 2023 | 51× 超实时加速、亚微秒步长 |