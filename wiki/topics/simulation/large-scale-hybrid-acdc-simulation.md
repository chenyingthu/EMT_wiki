---
title: "大型交直流混联电网仿真 (Large-Scale Hybrid AC/DC Simulation)"
type: topic
tags: [hybrid-grid, acdc, large-scale, hvdc, mmc, multi-terminal, co-simulation, multirate]
created: "2026-05-02"
updated: "2026-05-14"
---

# 大型交直流混联电网仿真 (Large-Scale Hybrid AC/DC Simulation)

## 定义

大型交直流混联电网仿真研究交流网络、LCC-HVDC、[[vsc-hvdc]]、[[mmc-model]]、多端直流（MTDC）、FACTS 和新能源并网设备在同一运行场景中的动态耦合。其核心挑战在于：交直流系统具有截然不同的时间尺度和动态特性——交流侧以机电暂态（秒级）和电磁暂态（微秒级）共存，直流侧则以阀换相、控制环（毫秒级）和开关暂态（微秒级）为主导。因此，"全 EMT 建模"在工程上几乎不可行，必须在 EMT、机电暂态、动态相量、平均值模型和网络等值之间做出分层选择。

本页关注大系统、交直流接口和多时间尺度仿真的知识边界。单个 MMC、VSC、STATCOM 或线路模型的内部方程应回到对应模型页讨论。

## EMT 中的作用

EMT 在交直流混联系统中主要用于捕捉正序机电模型难以表示的现象：

- LCC 换相失败、阀触发、交流故障导致的直流侧暂态和恢复过程（毫秒级换相角动态）。
- VSC/MMC 控制环、限流器、PLL、调制和直流网络故障之间的快速耦合（微秒级开关动态）。
- 直流线路、电缆、换流变压器、滤波器和接地回路引起的宽频暂态（行波传播、高频振荡）。
- 保护与控制设备闭环验证，特别是直流断路器、换流站控制器和广域控制接口。

以 Hydro-Québec 2023 年全系统 EMT 模型为例（Table 1），该系统包含 1666 个母线、111 台发电机、6 座 HVDC 换流站、6 座风电场和 90,405 个控制模块。在 RTDS 实时仿真平台上，此类规模的全 EMT 模型需要精确的初始化、模型兼容和分区策略才能稳定运行。

| 组件类别 | 数量 |
|---------|------|
| 三相母线 | 1,666 |
| 发电机 | 111 |
| 线路和电缆 | 432 |
| 三相变压器 | 338 |
| 调速器 | 86 |
| 励磁系统 | 81 |
| 稳定器 | 54 |
| STATCOM | 10 |
| 风电场 | 6 |
| HVDC 换流站 | 6 |
| 动态负荷 | 165 |
| 控制模块 | 90,405 |

*Table 1 · Hydro-Québec 2023 全系统 EMT 模型组件统计（来源：Le-Huy 2023）*

## 仿真方法体系

大型交直流混联系统仿真方法可分为四个层次：全 EMT 求解、EMT-机电混合、多速率 EMT、以及等值降阶。这四类方法并非互斥，而是根据研究目的和系统规模组合使用。

### 方法一：全 EMT 建模

全 EMT 建模将所有元件（交流网络、LCC/VSC 换流器、直流网络、控制系统、保护逻辑）统一在相域 EMT 模型中求解。它适合故障暂态分析、控制保护验证和小规模系统的高精度研究。

**网络方程**采用传统节点导纳 formulation（与 [[nodal-analysis]] 一致）：

$$G \cdot v(t) = i(t) + i_{\mathrm{hist}}(t - \Delta t)$$

其中 $G$ 为网络电导矩阵（由所有伴 circuit 等效电阻构成），$v(t)$ 为节点三相瞬时电压向量，$i(t)$ 为节点电流注入向量，$i_{\mathrm{hist}}(t-\Delta t)$ 为伴 circuit 历史电流向量。

为抑制数值振荡，ParaEMT 在 L/C 元件上并联/串联人工电阻：

$$R_p \approx \frac{4L}{3\Delta t}, \quad R_s \approx \frac{3\Delta t}{40C}$$

全 EMT 建模的计算量随系统规模呈超线性增长。对于含有数百座换流器的大规模 MMC-MTDC 系统，即使采用 [[sparse-matrix-techniques]] 和 [[parallel-computing]]，单步仿真时间仍可达数十毫秒（在 50 μs 步长下）。

### 方法二：EMT-机电混合仿真

EMT-机电混合仿真（[[electromechanical-electromagnetic-hybrid-simulation]]）将局部 EMT 区域嵌入较大机电系统。其核心是**接口一致性约束**：

$$\begin{aligned}
x^{\mathrm{ac}}_{k+1} &= F_{\mathrm{ac}}(x^{\mathrm{ac}}_k, y^{\mathrm{dc}}_k, u_k), \\
x^{\mathrm{dc}}_{k+1} &= F_{\mathrm{dc}}(x^{\mathrm{dc}}_k, y^{\mathrm{ac}}_k, u_k), \\
0 &= \Phi(y^{\mathrm{ac}}_k, y^{\mathrm{dc}}_k)
\end{aligned}$$

其中 $x^{\mathrm{ac}}$ 和 $x^{\mathrm{dc}}$ 分别表示交流和直流侧状态向量，$y^{\mathrm{ac}}, y^{\mathrm{dc}}$ 是接口电压、电流或功率变量，$\Phi$ 表示接口一致性约束（如功率平衡、电压匹配）。

**接口实现方式**主要有三种：

1. **Thevenin/Norton 等值接口**：将外部系统表示为时变 Thevenin 或 Norton 等值，通过移动窗预测（moving-window prediction）更新等值参数。Shu 2018 提出的方法使用步长修正和平均技术消除混叠和时延误差。

2. **动态相量接口**：用动态相量（[[dynamic-phasor]]）表示慢速子系统，与 EMT 子系统的交互通过频域映射实现。Zhu 2021 提出的"接口位移-动态相量映射等价"方法证明了其在 HVACDC 混合仿真中的数值稳定性。

3. **直接互连法**：通过松弛法（relaxation approach）或波形松弛法（waveform relaxation）直接耦合 EMT 和相量求解器。Plumier 2016 提出的松弛法通过迭代修正接口变量，收敛速度取决于松弛因子选择。

EMT-机电混合仿真的主要风险包括接口延迟、能量不一致和数值反射。van der Meer 2015 提出的改进协议包括：(1) 故障后交流系统等值阻抗重新因式分解；(2) 修正的 Thevenin 等值源更新交互协议；(3) 故障期间改进的相量确定协议。

### 方法三：多速率 EMT 仿真

多速率 EMT（[[multirate-method]]）按动态快慢划分步长，例如 MMC 和直流网络使用微秒级步长（2-50 μs），交流外部系统使用毫秒级步长（100-500 μs）。

**速率比确定准则**：Shu 2018 提出了基于 EMT 仿真精度的速率比判定准则。设快子系统步长为 $\Delta t_f$，慢子系统步长为 $\Delta t_s$，则速率比 $r = \Delta t_s / \Delta t_f$ 必须满足：

$$r \leq \frac{1}{f_{\max} \cdot \Delta t_f}$$

其中 $f_{\max}$ 为快子系统中最高关注频率。对于 MMC 系统，$f_{\max}$ 通常为开关频率的 1/10（约 1-2 kHz），因此 $r$ 通常在 10-50 之间。

Li 2020 提出了多速率多域传输线模型（MD-TLM）和多速率频变 MD-TLM，分别用于表征宽频带交互。在含大规模风电场的系统中，该方法可将步长扩展至 500 μs，同时保持对次同步振荡（SSO）的准确捕捉。

**接口离散化与数值振荡抑制**：多速率仿真的核心难点在于接口模型的离散化。Shu 2018 开发了数值振荡抑制算法，通过在接口模型中引入阻尼项：

$$i_{\mathrm{damp}} = \alpha \cdot (v_f - v_s)$$

其中 $\alpha$ 为阻尼系数，$v_f$ 和 $v_s$ 分别为快慢侧接口电压。$\alpha$ 的选择需要在数值稳定性和物理准确性之间权衡。

### 方法四：等值与降阶

等值和降阶方法通过简化外部系统降低计算规模：

- **FDNE 等值**（[[fdne-model]]）：用频域网络等值表示外部系统的频率相关特性，适用于宽频分析。
- **平均值模型**（[[average-value-model]]）：将 MMC 换流器简化为平均值模型，忽略开关谐波，适合低频和控制层分析。
- **动态相量**（[[dynamic-phasor]]）：将高频开关动态转换为低频相量动态，适合大规模系统稳态和低频暂态分析。
- **多区域 Thevenin 等值**（MATE）：将多个区域分别表示为 Thevenin 等值，适用于大规模交直流系统的控制设计。

等值方法的适用边界需明确说明保留和舍弃的频带、状态和开关细节。例如，平均值模型适合低频和控制层分析，但会丢失开关谐波、子模块电容不均衡、阀级应力和保护依赖的瞬时波形。

## 形式化表达

### 核心公式汇总

**伴 circuit 离散化**（梯形积分法，数值 A 稳定）：

$$i(t) = \frac{v(t)}{R_{\mathrm{eq}}} + i_{\mathrm{hist}}(t - \Delta t)$$

$$i_{\mathrm{hist}}(t - \Delta t) = a \cdot i(t - \Delta t) + b \cdot v(t - \Delta t)$$

其中 $R_{\mathrm{eq}}$ 为等效电阻，$a$ 和 $b$ 为梯形积分系数。

**BBD 分区并行**（ParaEMT 网络求解）：

$$G = \begin{bmatrix}
G_{11} & & & G_{1n} \\
& G_{22} & & G_{2n} \\
& & \ddots & \vdots \\
G_{n1} & G_{n2} & \cdots & G_{nn}
\end{bmatrix}$$

其中 $n = m+1$，$m$ 为分区数。通过 Schur 补法进行块矩阵 LU 分解，实现并行前代和回代。

**多速率接口更新**（移动窗预测）：

$$y_{k+1}^{\mathrm{interface}} = y_k^{\mathrm{interface}} + \Delta y_{\mathrm{prediction}} + \Delta y_{\mathrm{correction}} + \Delta y_{\mathrm{averaging}}$$

三种修正项分别消除混叠、时延和离散化误差。

**初始化**（正序潮流转换）：

$$\begin{aligned}
v_a &= V_{\mathrm{mag}} \cos(\theta_{\mathrm{ang}}) \\
v_b &= V_{\mathrm{mag}} \cos(\theta_{\mathrm{ang}} - 2\pi/3) \\
v_c &= V_{\mathrm{mag}} \cos(\theta_{\mathrm{ang}} + 2\pi/3)
\end{aligned}$$

## 关键技术挑战

### 挑战一：接口稳定性与数值反射

EMT-机电混合和多速率仿真的核心挑战是接口稳定性。当快慢子系统通过接口交换信息时，如果接口模型缺少适当的阻尼或延迟补偿，可能引入非物理反射波，导致数值振荡甚至仿真发散。Shu 2018 的数值振荡抑制算法和 van der Meer 2015 的修正交互协议是两种代表性解决方案。

### 挑战二：大规模系统初始化

全 EMT 仿真需要精确的初始稳态条件。ParaEMT 采用正序潮流（Newton-Raphson 法）求解后转换为三相波形初始化。然而，对于包含大量电力电子设备的系统，控制器初始化和状态变量反向传播是难点。Le-Huy 2023 指出，离线仿真中常用的"阻塞-释放"初始化方法在实时仿真中不可用，因为实时仿真没有足够时间等待系统收敛。

### 挑战三：计算可扩展性

ParaEMT 在 10,080 总线系统（30,240 节点）上的 HPC 仿真表明，网络求解占总计算时间的 60% 以上，是加速的主要瓶颈。BBD 分区方法在 42 个分区时达到最大加速比 36×，但超过此数量后，角矩阵非零元素增加导致同步开销超过并行收益。

### 挑战四：模型移植与兼容性

从离线 EMT 工具移植到实时仿真平台时，模型兼容性层是主要障碍。Le-Huy 2023 的 Hydro-Québec 经验表明，1666 母线系统的移植需要：(1) 节点缩减（部分变电站节点数超过 300）；(2) π 型线路合并为常参数线路；(3) 控制代数环消除（实时求解器不支持迭代求解）。

### 挑战五：UHVDC 分层接入的耦合复杂性

Xiong 2020 对 ±800 kV 雅中-江西 UHVDC 分层接入工程的研究表明，特高压直流分层接入在提升受端电网电压支撑的同时，引入了不同层间系统的复杂耦合关系。混合仿真模型在关断角独立控制指令阶跃响应下，与纯 EMT 模型的误差控制在 2% 以内，但机电暂态模型与 EMT 模型的误差可达 15-20%。

## 量化性能边界

### 加速性能数据

| 系统规模 | 方法 | 加速比 | 验证平台 | 来源 |
|---------|------|--------|---------|------|
| 240 总线 WECC | ParaEMT 串行 (JIT Numba) | 参考基准 | Intel Xeon Platinum 8280 | Xiong 2024 |
| 240 总线 WECC | ParaEMT 并行 (8核) | ~1.0×（同步开销抵消收益） | Intel Xeon Platinum 8280 | Xiong 2024 |
| 10,080 总线 | ParaEMT HPC (42分区, 42 MPI) | 36× | NREL Eagle 超算 | Xiong 2024 |
| 10,080 总线 | ParaEMT HPC (28-48分区) | 25-35× | NREL Eagle 超算 | Xiong 2024 |
| Nelson River LCC HVDC | RTDS 混合 HIL | 实时 (1:1) | RTDS + 硬件控制器 | Zhou 2021 |
| Hydro-Québec 1666母线 | EMTP → HYPERSIM 移植 | 实时 (1:1) | HYPERSIM | Le-Huy 2023 |

### 精度数据

| 对比场景 | 最大绝对误差 | 来源 |
|---------|-------------|------|
| ParaEMT 并行 vs 串行 (240总线, 5s仿真) | < 4×10⁻¹² pu | Xiong 2024 |
| 混合仿真 vs 纯EMT (UHVDC阶跃响应) | < 2% | Xiong 2020 |
| 混合仿真 vs 机电暂态 (UHVDC故障) | 15-20% | Xiong 2020 |
| EMTP vs HYPERSIM (Hydro-Québec潮流) | 8 MW / 35 Mvar (0.02% / 0.83%) | Le-Huy 2023 |

### 多速率步长扩展

| 系统 | 原始步长 | 多速率步长 | 效率提升 | 来源 |
|------|---------|-----------|---------|------|
| 大规模风电+AC电网 | 2-50 μs | 500 μs (慢侧) | ~10-25× | Li 2020 |
| 大型AC + MMC-MTDC | 2-50 μs (统一) | 2-50 μs / 100-500 μs | ~5-20× | Shu 2018 |

## 适用边界与选择指南

### 方法选择决策表

| 应用场景 | 推荐方法 | 理由 | 注意事项 |
|---------|---------|------|---------|
| 换相失败/阀故障分析 | 全 EMT | 需要毫秒级阀动态 | 计算量大，适合小规模 |
| 控制保护闭环验证 | 全 EMT 或 HIL | 需要精确开关时序 | HIL 需要硬件在环平台 |
| UHVDC 分层接入动态 | EMT-机电混合 | 不同层间耦合复杂 | 接口稳定性是关键 |
| 大规模 MMC-MTDC + AC | 多速率 EMT | 快慢系统时间尺度差异大 | 速率比需按精度准则确定 |
| 次同步振荡宽频分析 | 多速率 + MD-TLM | 需要宽频带交互表征 | 频变传输线模型增加复杂度 |
| 实时仿真 / HIL | RTDS 混合 + 硬件控制器 | 需要 1:1 实时性 | 模型移植和节点缩减是前提 |
| 大规模系统控制设计 | 多区域 Thevenin 等值 | 平衡精度和效率 | 等值参数需定期更新 |
| 低频稳态/控制层分析 | 平均值模型 + 机电暂态 | 忽略开关谐波 | 不适用于保护动作分析 |

### 外部系统等值选择

- **精细等值**：保留低频振荡模式和无功支撑特性，适用于故障后功率转移分析。使用频变 FDNE 等值，保留 0-500 Hz 频带。
- **中等等值**：保留主导机电模式，适用于控制环设计。使用固定 Thevenin 等值，在关键工况点重新校准。
- **粗糙等值**：仅保留等效注入功率，适用于大规模并行仿真的外部系统简化。可能低估低频振荡和无功不足。

## 相关方法 / 相关模型 / 相关主题

- [[vsc-hvdc]] 和 [[mmc-model]] 解释换流器和直流系统对象；本页讨论它们进入大系统仿真后的接口和规模问题。
- [[electromechanical-electromagnetic-hybrid-simulation]] 关注 EMT-机电接口方法；本页把它放在交直流系统应用背景下。
- [[multirate-method]] 是多步长求解方法，是大型交直流系统仿真中的关键加速技术。
- [[parallel-computing]] 和 [[real-time-simulation]] 讨论计算结构；本页引用其作为大系统可计算性的支撑条件。
- [[fdne-model]]、[[frequency-dependent-modeling]]、[[average-value-model]] 和 [[dynamic-phasor]] 是等值与降阶方法。
- [[co-simulation]] 是混合仿真的通用框架。
- [[large-scale-system-simulation]] 讨论更大规模的仿真挑战。
- [[computational-acceleration]] 讨论计算加速的整体框架。

## 来源论文

- **Shu 等 2018** — "A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems"：提出了大型交流系统与 MMC-MTDC 的多速率协同仿真方法，包括 Thevenin/Norton 接口模型、移动窗预测、步长修正和数值振荡抑制算法。速率比判定准则是该方法的核心贡献。
- **Zhou 等 2021** — "Large-scale hybrid real time simulation modeling and benchmark for Nelson River multi-infeed HVdc system"：Manitoba Hydro 在 Nelson River LCC-HVDC 多端系统中的大规模混合实时仿真工程实践，展示了 RTDS 软件模型与硬件控制器混合 HIL 的完整建模流程，为 LCC-HVDC 多端系统提供了工程基准。
- **Xiong 等 2020** — "Electromechanical-electromagnetic transient hybrid simulation of an AC/DC hybrid power grid with UHVDC"：针对 ±800 kV 雅中-江西 UHVDC 分层接入工程，在 ADPSS 上搭建混合仿真模型，验证了混合仿真在关断角阶跃响应下与纯 EMT 模型的一致性（误差 < 2%），以及相比机电暂态模型的精度优势。
- **van der Meer 等 2015** — "Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems"：提出了 VSC-HVDC 混合仿真中的三项改进：(1) 故障后交流系统等值阻抗重新因式分解；(2) 修正的 Thevenin 等值源更新协议；(3) 故障期间改进的相量确定协议。显著提高了交直流系统暂态稳定性评估的准确性。
- **Le-Huy 等 2023** — "Lessons learned in porting offline large-scale power system simulation to real-time"：Hydro-Québec 从 EMTP 移植 1666 母线全系统模型到 HYPERSIM 实时平台的经验总结，涵盖 GUI 兼容性、模型兼容层、系统初始化、控制建模和节点缩减等关键挑战，为大规模 EMT 到实时仿真的移植提供了系统性指导。
- **Li 等 2020** — "A Multi-Rate Co-Simulation of Combined Phasor-Domain and Time-Domain Models for Large-scale Wind Farms"：提出了相量域与时域结合的多速率协同仿真方法，引入多域传输线模型（MD-TLM）和频变 MD-TLM，将大规模风电场仿真步长扩展至 500 μs，同时保持对次同步振荡的准确捕捉。
- **Xiong 等 2024** — "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids"：开发了基于 Python 的开源并行 EMT 仿真器 ParaEMT，采用 BBD 分区并行网络求解，在 NREL Eagle 超算上对 10,080 总线系统实现了 36× 加速比，为大规模 IBR 电网的 EMT 仿真提供了可扩展的开源平台。
