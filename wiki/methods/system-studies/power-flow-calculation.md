---
title: "潮流计算 (Power Flow Calculation)"
type: method
tags: [power-flow, load-flow, steady-state, newton-raphson, gauss-seidel, fast-decoupled, dc-power-flow, harmonic-power-flow, emt-initialization]
created: "2026-05-02"
updated: "2026-05-16"
---

# 潮流计算 (Power Flow Calculation)

## 定义

潮流计算（Power Flow / Load Flow）是在给定网络拓扑、发电机组出力、负荷功率和运行控制设定后，求解电力系统稳态相量运行点的方法。系统处于基频稳态（50/60 Hz）时，各节点满足复功率平衡方程：

$$
S_i = P_i + jQ_i = V_i \angle \theta_i \cdot I_i^* = V_i \angle \theta_i \cdot \left( \sum_{j=1}^{n} Y_{ij} V_j \angle \theta_j \right)^* = V_i \angle \theta_i \cdot \sum_{j=1}^{n} Y_{ij}^* V_j \angle (-\theta_j)
$$

其中 $Y_{ij} = G_{ij} + jB_{ij}$ 为节点导纳矩阵元素，$V_i = |V_i|e^{j\theta_i}$ 为节点电压相量，$\theta_i - \theta_j$ 为两端电压相角差。

展开为极坐标下的有功-相角、无功-电压平衡方程：

$$
P_i = |V_i| \sum_{j=1}^{n} |V_j| \left( G_{ij} \cos(\theta_i - \theta_j) + B_{ij} \sin(\theta_i - \theta_j) \right) \tag{1}
$$

$$
Q_i = |V_i| \sum_{j=1}^{n} |V_j| \left( G_{ij} \sin(\theta_i - \theta_j) - B_{ij} \cos(\theta_i - \theta_j) \right) \tag{2}
$$

潮流计算输出节点电压幅值 $|V_i|$ 和相角 $\theta_i$、发电机无功出力 $Q_g$、平衡节点有功吸收 $P_{slack}$、以及支路有功 $P_{ij}$、无功 $Q_{ij}$ 和网损 $P_{loss}$。潮流结果是电力系统规划、运行校核、优化调度和动态仿真初始化的基础输入。

## EMT中的角色

潮流计算在电磁暂态（EMT）仿真工作流中处于**初始化前置**地位，而非核心求解环节。EMT程序以微秒级步长（如 $1\,\mu s$、$10\,\mu s$、$50\,\mu s$）推进三相瞬时电压电流、开关动作事件和电力电子控制动态，而潮流模型假定系统处于基频稳态或准稳态，输出是单一频率（50/60 Hz）的相量而非时域波形。

潮流计算在 EMT 中的具体作用包括：

1. **稳态初始化（Steady-State Initialization）**：潮流结果提供节点电压相量、支路功率和发电机出力，作为 EMT 仿真 $t=0$ 时刻的初始条件，使仿真从系统实际运行点而非零状态启动，避免漫长的非物理启动暂态过程。
2. **同步机状态初始化**：根据潮流解计算转子功角 $\delta$、内部电势 $E'$、励磁电压 $E_f$ 和机械功率 $P_m$ 的稳态值，建立同步机的电磁暂态初值。
3. **换流器控制器设定值**：潮流提供 PCC 电压幅值/相角、有功/无功指令，作为 VSC-HVDC、MMC、储能变流器等电力电子设备的内环或外环控制参考。
4. **机电-电磁混合仿真的接口**：在全系统机电暂态（RMS）与局部 EMT 协同仿真中，潮流结果作为机电侧向 EMT 侧提供的等值外部系统运行点。

潮流解转换为 EMT 初值并非自动无误。电容电压的初始电荷、电感电流的初始磁链、PLL 的锁相相位、控制积分器的历史状态、限幅器的饱和标志都可能需要额外初始化或时域松弛，否则控制器初值不匹配会引发启动振荡或仿真失败（见 [[steady-state-initialization]]）。

## 潮流方程与节点类型

### 节点功率平衡方程

对于每个节点 $i$，复功率注入定义为：

$$
P_i^{inj} = |V_i| \sum_j |V_j| \left( G_{ij} \cos\theta_{ij} + B_{ij} \sin\theta_{ij} \right) \tag{3}
$$

$$
Q_i^{inj} = |V_i| \sum_j |V_j| \left( G_{ij} \sin\theta_{ij} - B_{ij} \cos\theta_{ij} \right) \tag{4}
$$

其中 $\theta_{ij} = \theta_i - \theta_j$。待求量是有功不匹配 $\Delta P_i = P_i^{spec} - P_i^{inj}$ 和无功不匹配 $\Delta Q_i = Q_i^{spec} - Q_i^{inj}$。

### 节点分类体系

电力系统潮流分析将节点分为三类，对应不同的已知/未知量组合：

| 节点类型 | 已知量 | 未知量 | 物理含义 |
|---------|--------|--------|---------|
| **PQ 节点** | $P_i^{spec}, Q_i^{spec}$ | $|V_i|, \theta_i$ | 负荷节点、普通发电机 |
| **PV 节点** | $P_i^{spec}, |V_i|^{spec}$ | $Q_i^{inj}, \theta_i$ | 具备电压调节能力的发电机 |
| **平衡节点（Slack）** | $|V_i|^{spec}, \theta_i^{spec}=0$ | $P_i^{inj}, Q_i^{inj}$ | 系统频率/相位参考，吸收功率不平衡 |

PV 节点的无功越限时需切换为 PQ 节点（$Q_i^{spec} = Q_i^{limit}$），此时控制约束失效，运行点由网络方程决定。该处理会改变雅可比矩阵结构和收敛路径，应在算例中明确。

### 雅可比矩阵结构

牛顿法求解功率不匹配方程的核心是雅可比矩阵 $J = \partial(\Delta P, \Delta Q) / \partial(\theta, |V|)$。以直角坐标为例，节点功率对电压的偏导数涉及 $G_{ij}$ 和 $B_{ij}$：

$$
\frac{\partial P_i}{\partial \theta_i} = |V_i| \sum_j |V_j| \left( -G_{ij} \sin\theta_{ij} + B_{ij} \cos\theta_{ij} \right) \tag{5}
$$

$$
\frac{\partial P_i}{\partial |V_j|} = |V_i| \left( G_{ij} \cos\theta_{ij} + B_{ij} \sin\theta_{ij} \right) \tag{6}
$$

## 主流算法体系

### 高斯-赛德尔迭代法

高斯-赛德尔（Gauss-Seidel, GS）迭代以导纳矩阵逐节点求解电压更新：

$$
V_i^{(k+1)} = \frac{1}{Y_{ii}} \left( \frac{P_i - jQ_i}{(V_i^{(k)})^*} - \sum_{j \neq i} Y_{ij} V_j^{(k+1)} \right) \tag{7}
$$

GS 迭代实现简单，每步只需一次前代-回代，但其收敛速度为线性收敛（$\mathcal{O}(n)$ 迭代次数），对病态系统（高 $R/X$ 比、弱连系）可能收敛很慢或发散。

### 牛顿-拉夫森法

牛顿-拉夫森（Newton-Raphson, NR）法利用雅可比矩阵 $J$ 求解不匹配修正量：

$$
\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix}^{(k)} = -J^{(k)} \begin{bmatrix} \Delta \theta \\ \Delta |V| \end{bmatrix}^{(k)} \tag{8}
$$

对大规模系统，$J$ 为稀疏矩阵，NR 法收敛速度为二阶收敛，通常 5-10 次迭代即可收敛到容差 $10^{-6}$ pu（见 [[newton-raphson-method]]）。直角坐标 NR 方程为：

$$
\Delta P_i = \sum_j \left( G_{ij} \Delta e_j - B_{ij} \Delta f_j \right) - e_i \sum_j \left( G_{ij} e_j + B_{ij} f_j \right) - f_i \sum_j \left( G_{ij} f_j - B_{ij} e_j \right) = 0 \tag{9}
$$

其中 $V_j = e_j + jf_j$ 为直角坐标电压，$Y_{ij} = G_{ij} + jB_{ij}$。

### 快速解耦潮流

快速解耦潮流（Fast Decoupled Power Flow, FDPF）利用输电线路 $B_{ij} \gg G_{ij}$ 和相角-有功、无功-电压近似解耦的假设，将雅可比矩阵分裂为：

$$
J = \begin{bmatrix} H & 0 \\ 0 & L \end{bmatrix} \approx \begin{bmatrix} -B & 0 \\ 0 & -B \end{bmatrix} \tag{10}
$$

其中 $H \approx -B$（相角相关子阵），$L \approx -B$（电压相关子阵），$B_{ij} = \text{Im}(Y_{ij})$。修正方程变为：

$$
\Delta P_i = -B_{ii} \Delta \theta_i - \sum_{j \neq i} B_{ij} \Delta \theta_j \tag{11}
$$

$$
\Delta Q_i = -B_{ii} \Delta |V_i| - \sum_{j \neq i} B_{ij} \Delta |V_j| \tag{12}
$$

FDPF 将每次迭代的计算量从 $O(n^2)$ 降为 $O(n)$，但仅适用于 $R/X$ 比小的输电网络，对配电网络（$R/X$ 比大）或弱连系系统可能不收敛。

### 直流潮流

直流潮流（DC Power Flow）忽略支路电阻和节点无功功率，用线性方程近似有功分布：

$$
P_{ij} = \frac{\theta_i - \theta_j}{x_{ij}} \quad \text{或} \quad P_{ij} = B_{ij} (\theta_i - \theta_j) \tag{13}
$$

$$
\mathbf{P}_{bus} = \mathbf{B}_{bus} \cdot \boldsymbol{\theta} \tag{14}
$$

其中 $\mathbf{B}_{bus} = \text{Im}(Y_{bus})$ 为纯电纳矩阵，$\boldsymbol{\theta}$ 为相角向量。直流潮流的计算复杂度为 $O(n)$，适合快速估计大规模电力系统的有功功率分布，但无法给出电压幅值、无功功率和网损。

### 多相潮流与EMTP接口

传统单相平衡潮流无法描述三相不平衡工况。高压输电线路通常不完全换位，导致负序和零序电流不为零，可能引起继电保护误动。多相潮流算法将每相作为独立节点处理，采用三相导纳矩阵 $\mathbf{Y}_{abc}$：

$$
\begin{bmatrix} I_a \\ I_b \\ I_c \end{bmatrix} = \begin{bmatrix} Y_{aa} & Y_{ab} & Y_{ac} \\ Y_{ba} & Y_{bb} & Y_{bc} \\ Y_{ca} & Y_{cb} & Y_{cc} \end{bmatrix} \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix} \tag{15}
$$

Multiphase Power Flow Solutions Using EMTP and Newton's Method（IEEE, 2011）将 Newton 法改写为直角坐标下的支路电流约束问题，直接复用 EMTP 组装的 $\mathbf{Y}_{bus}$ 表示线性网络，把非线性设备作为未知电流和约束方程加入，从而避免另建潮流网络模型。算法接口关系为：

$$
[\mathbf{Y}] \mathbf{V} = [\mathbf{I}_s] + [\mathbf{I}_u] \tag{16}
$$

其中 $\mathbf{I}_s$ 为已知注入电流源，$\mathbf{I}_u$ 为非线性设备的不平衡电流。该方法使复杂接线方式（三角形负荷、相间电压源等）能按支路量自然建模，并与 EMTP 网络矩阵直接接口。

### 谐波潮流与时域打靶

A Time-Domain Harmonic Power Flow Algorithm（2010）将潮流约束嵌入周期稳态打靶方程，同时满足周期性和有功/无功/电压约束。核心机制是把传统潮流方程变成打靶法边界条件的一部分，而非先求基波潮流再叠加谐波。算法框架为：

1. **初始化**：给定候选状态初值 $\mathbf{x}_0$、指定母线的基波电压幅值/相角
2. **时域积分**：EMT 程序从 $\mathbf{x}_0$ 积分一个周期 $T$，得到 $\mathbf{x}(T) = \boldsymbol{\Phi}(\mathbf{x}_0, T)$
3. **周期性约束**：$\mathbf{F}(\mathbf{x}_0) = \boldsymbol{\Phi}(\mathbf{x}_0, T) - \mathbf{x}_0 = \mathbf{0}$（周期不动点条件）
4. **潮流约束**：有功/无功/电压不匹配方程作为额外约束加入非线性方程组
5. **牛顿修正**：联合求解 $\mathbf{F}(\mathbf{x}_0) = \mathbf{0}$ 和潮流失配方程

该方法把电力电子和非线性负荷产生的谐波约束耦合进潮流方程，使求解结果与 EMT 时域稳态一致，而非仅在基波频率下近似。

## EMT初始化方法

### 直接初始化

最简策略是直接将潮流结果映射为 EMT 初值：
- 节点电压相量 $\rightarrow$ 三相瞬时电压 $\sqrt{2}|V_i|\cos(\omega t + \theta_i)$
- 支路功率 $\rightarrow$ 电流源幅值
- 平衡节点功率 $\rightarrow$ 电压源

直接初始化仅适用于纯线性 RLC 网络，不适用于含开关器件或控制器的系统。

### 三阶段VSC初始化流程

A Steady-State Initialization Procedure for Generic Voltage-Source Converters（2023）提出系统化三阶段流程：

**第一阶段：交流潮流等效**
- 同步机/高压侧按 P-V 节点建模
- 负荷按 P-Q 节点建模
- VSC 根据控制模式等效为 P-Q 或 P-V 节点

**第二阶段：状态推导**
- 从潮流相量反向推算控制器积分器历史项
- 计算 dq 轴电流/电压参考值
- 确定 PLL 锁相相位

**第三阶段：电路状态初始化**
- 电容电压初值：$\displaystyle V_C(0) = \sqrt{2} |V_{pcc}|$
- 电感电流初值：$\displaystyle I_L(0) = \sqrt{2} \frac{P+jQ}{V_{pcc}^*}$
- 直流电容电压：$\displaystyle V_{dc}(0) = V_{dc}^{ref}$

### 构网型换流器初始化

Initializing EMT Models of Grid-Forming VSCs in MTDC Systems（2024）针对 MTDC 系统中采用 V/f 控制的构网型换流器（GVSC），提出两条路径：

**CISS（Controlled Internal State Setting）**
- 利用潮流相量和已知换流器参数解析计算外环积分器初值
- 前提：可获得 GVSC 平均值模型及外环控制参数
- 步骤：PCC 电压相量 $\rightarrow$ 交流电流相量 $\rightarrow$ dq 坐标系变换 $\rightarrow$ 外环 PI 状态

**DI（Decoupling Interface）**
- 通过接口辅助源将 GVSC 与交流孤岛临时电气解耦
- 使黑盒模型也能独立进入稳态后再重耦合
- 不需要知道控制器内部参数

### 打靶法周期稳态初始化

Shooting Method Based Modular Multilevel Converter Initialization（2021）将 MMC 初始化表述为打靶问题：

$$
\mathbf{F}(\mathbf{x}_0) = \boldsymbol{\Phi}(\mathbf{x}_0, T) - \mathbf{x}_0 = \mathbf{0} \tag{17}
$$

其中 $\boldsymbol{\Phi}(\mathbf{x}_0, T)$ 为从一个基波周期 $T = 1/f_0$ 的状态转移映射。求解使用牛顿迭代，通过灵敏度矩阵修正 $\mathbf{x}_0$ 直到周期末状态与初始状态一致。两阶段实现：
1. 先在平均值模型中求稳态，降低由大量子模块带来的维数和开关事件负担
2. 再将平均模型得到的状态映射到 Thévenin 等效/详细模型

该方法不要求事先假定控制信号只含基波，兼容含环流抑制和电容电压平衡的闭环控制 MMC。

## EMT仿真算法对比

| 算法 | 收敛速度 | 计算复杂度 | 适用场景 | 不适用场景 |
|------|---------|-----------|---------|-----------|
| 高斯-赛德尔 | 线性 $\mathcal{O}(n)$ | $O(n)$ | 小规模系统、教学 | 大规模、病态系统 |
| 牛顿-拉夫森 | 二阶收敛 | $O(n^2)$/迭代 | 通用、中大规模 | 初值敏感 |
| 快速解耦 | 超线性 | $O(n)$/迭代 | 输电网（$R \ll X$） | 配电、强连系弱网 |
| 直流潮流 | 直接求解 | $O(n)$ | 快速有功估计 | 无功、电压、网损 |
| 多相潮流 | 二阶收敛 | $O(3n^2)$ | 三相不平衡分析 | 单相平衡系统 |
| 时域谐波潮流 | 超线性 | $O(n^2)$/迭代 | 电力电子谐波初始化 | 纯线性系统 |

## 量化性能边界

| 指标 | 典型值 | 数据来源 |
|------|--------|---------|
| NR 法收敛迭代次数 | 4-10 次 | 通用电力系统 |
| FDPF 收敛迭代次数 | 8-15 次 | 输电网测试 |
| DC 潮流误差 | < 5%（有功） | IEEE 30/118 系统 |
| 多相潮流误差（负序电流） | < 2%（完全换位线路） | Cigre WG C4.601 |
| 时域打靶法迭代次数 | 3-8 次 | Agarwal 2010, 6节点系统 |
| VSC 初始化残差（启动暂态） | < 0.1% (电压偏差) | Cao 2023, IEEE 39 |

**初始化暂态抑制效果**：充分初始化相比零初值启动可将初始化阶段的 CPU 时间从 $10^4$ 数量级时间步减少到 $<100$ 时间步（特定测试系统，数据来源：Adequate Initialization for Generic VSC，2023）。

## 适用边界与选择指南

### 算法选择决策表

| 系统特征 | 推荐算法 | 备选算法 |
|---------|---------|---------|
| 小规模 (< 100 节点)、教学 | 高斯-赛德尔 | NR |
| 中大规模 (> 1000 节点)、输电网 | 快速解耦 | NR |
| 配电网络 ($R/X$ 比大) | NR（直角坐标） | GS（初值好时） |
| 三相不平衡分析 | 多相潮流 | 三相 NR |
| 快速有功估计 | 直流潮流 | - |
| 含电力电子谐波初始化 | 时域谐波潮流/打靶法 | 分段初始化 |
| MMC/HVDC 系统 | 打靶法周期初始化 | 三阶段初始化 |

### 失效模式与处理

1. **潮流不收敛**：靠近电压稳定边界、重载或弱网工况，可能存在多解或无解。处理方法：调整初值、放宽 PV 节点电压限制、切换为连续潮流。
2. **PV-PQ 节点切换振荡**：无功越限触发的切换改变雅可比矩阵结构，可能导致收敛路径振荡。处理方法：采用弧度连续模型或 Hansen 法。
3. **不平衡工况初始化不一致**：单相等值潮流无法保证三相 EMT 初始化的一致性。处理方法：使用多相潮流或时域谐波潮流。
4. **电力电子启动暂态**：潮流结果不包含控制器状态和 PWM 波形初值，导致启动振荡。处理方法：采用三阶段初始化或打靶法初始化。

## 相关方法与模型

| 相关概念 | 关系 | 说明 |
|---------|------|------|
| [[steady-state-initialization]] | 上游接口 | 潮流结果转换为 EMT 初值的具体流程 |
| [[newton-raphson-method]] | 核心算法 | NR 法是交流潮流最通用的高效求解方法 |
| [[electromechanical-electromagnetic-hybrid-simulation]] | 接口场景 | 机电 RMS 与 EMT 协同仿真中潮流作为接口数据 |
| [[phasor-model]] | 模型边界 | 相量模型近似 EMT 瞬时值，但与潮流更接近 |
| [[optimal-power-flow]] | 优化扩展 | 在潮流方程上叠加目标函数和约束优化 |
| [[economic-dispatch]] | 前置步骤 | 经济调度提供有功出力设定，潮流映射到网络运行点 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag]] | 进阶初始化 | 打靶法用于 MMC-HVDC 的周期稳态初始化 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in]] | VSC 初始化 | 三阶段流程初始化通用电压源换流器 |

## 来源论文

| 论文 | 年份 | 主要贡献 |
|------|------|---------|
| [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee]] | 2011 | 多相潮流嵌入 EMTP 网络矩阵，支路电流约束 Newton 法 |
| [[a-time-domain-harmonic-power-flow-algorithm]] | 2010 | 时域谐波潮流框架，潮流约束嵌入周期打靶方程 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in]] | 2023 | 三阶段 VSC 初始化流程，潮流到 EMT 状态映射 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]] | 2024 | CISS 和 DI 两条路径初始化 MTDC 构网型换流器 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag]] | 2021 | 打靶法 MMC 周期稳态初始化，含环流抑制和电容平衡 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-]] | 2024 | 全功率变流器风电场 FCI 初始化，从潮流反向推算控制器状态 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode]] | 2024 | TDSS 时域稳态分析，保留 EMT 模型一致性同时避免长时间积分 |

## 开放问题

1. **潮流到 EMT 映射的一致性**：电容电压、电感电流、控制器状态、PLL 相位、限幅器的初始化映射缺乏统一理论，不同软件工具链的做法不统一。
2. **电力电子高占比弱网**：稳态控制模式、限幅器和 PLL 初值可能比传统 PQ/PV 节点分类更关键，潮流模型尚未覆盖。
3. **多频率混合 AC/DC 系统**：多端 VSC-HVDC、柔性直流配电的稳态初始化不应被简化为单一基频潮流问题。
4. **时域稳态与传统潮流的差异**：现代电网中潮流解与 EMT 时域稳态（TDSS）可能存在显著差异（Agarwal 2024 表明逆变器非线性可使两者相差 5-10%），需要在初始化精度和计算代价之间权衡。