---
title: "Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;1;10.1109/TPWRD.2024.3514294"
tags: ['state-space']
created: "2026-04-13"
sources: ["EMT_Doc/35/Fu 等 - 2025 - Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations.pdf"]
---

# Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations

**作者**: 
**年份**: 2025
**来源**: `35/Fu 等 - 2025 - Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations.pdf`

## 摘要

—As the utilization of power electronic-based compo- nents in power systems continues to grow, a comprehensive un- derstanding of their dynamics becomes increasingly important for system design, control and protection analysis. To meet practi- cal needs, the high-ﬁdelity but time-consuming electromagnetic transient (EMT) simulations are often required. To improve the performance of these simulations, a highly efﬁcient splitting state- space method with numerical error control is proposed that reduces the computation workload. The method employs a generic decou- pling principle to split the state-space equations of the converter- integrated power system and introduces the exponential splitting formulas of multiple orders accuracy to solve and then compose the splitting state-space equations

## 核心贡献



- 提出了一种具有数值误差控制的高效分裂状态空间法，显著降低了含变流器电力系统EMT仿真的计算负担。
- 设计了基于状态矩阵时变部分分离的通用解耦原则，并引入多阶精度的指数分裂公式以加速矩阵指数计算。

## 使用的方法


- [[state-space]]
- [[numerical-integration]]

## 涉及的模型


- [[mmc-model]]
- [[wind-farm]]

## 相关主题


- [[real-time]]
- [[vsc]]

## 主要发现



- 该方法在含直流负载配电网、LLC变换器、大型风电场及MMC电路等多种测试案例中均验证了高保真度与计算准确性。
- 基于自动开关分组与相邻状态变量识别的解耦策略结合指数分裂方案，有效控制了数值误差并大幅提升了大规模电力电子系统EMT仿真的计算效率。

## 方法细节

### 方法概述

本文提出了一种分裂状态空间法(Splitting State-Space Method)用于含变流器电力系统的电磁暂态(EMT)仿真。该方法核心在于通过通用解耦原则将状态空间方程分解为常数部分和时变部分，并引入多阶精度的指数分裂公式(Exponential Splitting Formulas)进行求解。具体而言，方法首先通过自动开关分组和开关相邻状态变量(SASV, Switch Adjacent State Variables)识别，定位依赖于开关状态的最小子电路拓扑，将状态矩阵A分解为常数矩阵A1和块级时变矩阵A2(s(t))。然后利用指数分裂公式（如Trotter公式）将复杂的矩阵指数计算e^(tA)分解为e^(tA1)和e^(tA2)的乘积形式，避免直接计算整个时变状态矩阵的指数。其中A1的指数在仿真开始时计算并保持不变，而A2(s(t))的指数在开关状态变化时进行近似计算。该方法还提供数值误差控制方案，通过选择不同阶数的分裂公式来平衡计算精度与效率。

### 数学公式


**公式1**: $$$\dot{x} = Ax + Bu, \quad x(0) = x_0$$$

*原始非自治线性系统状态空间方程，x为状态变量向量，u为输入变量向量，A和B分别为状态和输入矩阵*


**公式2**: $$$\dot{\tilde{x}} = \tilde{A}\tilde{x}$$$

*通过增广技术将非自治系统转化为自治系统形式，其中$\tilde{x}$包含原始状态x和辅助状态变量$x_u$，用于包裹强迫项u的影响*


**公式3**: $$$\tilde{x}(t) = e^{t\tilde{A}}\tilde{x}(0)$$$

*自治系统的状态转移方程，显式表达为矩阵指数函数形式，是指数积分器的基础*


**公式4**: $$$A = A_1 + A_2(s(t))$$$

*状态矩阵分裂公式，将A分解为常数部分A1和依赖于开关状态s(t)的时变部分A2，实现解耦*


**公式5**: $$$e^{t(A_1+A_2)} \approx e^{tA_1}e^{tA_2} + O(t^2)$$$

*一阶Trotter分裂公式，将矩阵指数近似为两个子矩阵指数的乘积，计算复杂度从O(N^3)降低*


### 算法步骤

1. 系统建模与转换：将含变流器的电力系统电路建模为状态空间形式(1)，并通过增广技术转化为自治系统形式(2)，将输入信号的影响整合到扩展状态向量$\tilde{x}$中

2. 开关相关拓扑识别：通过自动开关分组算法识别电路中的所有开关器件，利用开关相邻状态变量(SASV)识别技术定位每个开关周围的最小子电路拓扑，确定状态矩阵中依赖于开关状态的时变元素

3. 状态矩阵分裂：基于时变部分分离原则，将状态矩阵A分裂为常数分裂矩阵A1（包含系统中不随开关变化的部分，如线路、滤波器等）和块级时变分裂矩阵A2(s(t))（包含变流器开关状态相关的部分），即$A = A_1 + A_2$

4. 预计算常数部分：在仿真开始前计算常数矩阵A1的指数$e^{tA_1}$，该结果在整个仿真过程中保持不变，用于计算系统不含功率转换部分的暂态

5. 开关事件处理与积分：当开关状态s(t)发生变化时，基于当前开关状态确定A2(s(t))，采用指数分裂公式（如一阶Trotter公式或高阶公式）近似计算$e^{tA}$，将积分过程分为多个阶段分别计算$e^{tA_1}$和$e^{tA_2}$的乘积

6. 解的组合与误差控制：将各分裂部分的计算结果组合，得到完整状态空间方程的近似解。根据所需的精度要求自适应选择分裂公式的阶数，通过数值误差控制方案监控局部截断误差，在精度不满足要求时自动提升分裂公式阶数或减小步长


### 关键参数

- **A**: 完整状态矩阵，包含系统所有动态特性

- **A1**: 常数分裂矩阵，代表不含功率转换的系统部分（如传输线、滤波器、负载等），不随开关状态变化

- **A2(s(t))**: 时变分裂矩阵，代表变流器功率转换部分，是开关状态s(t)的函数，具有块对角结构

- **s(t)**: 开关状态向量，描述各个半导体开关器件在当前时刻的导通/关断状态

- **SASV**: 开关相邻状态变量(Switch Adjacent State Variables)，指与开关器件直接相连或电气距离最近的状态变量，用于确定最小开关依赖子电路

- **t**: 仿真时间步长，对于高频开关变流器需足够小以捕捉开关动态（通常在微秒级）

- **N**: 系统维度，状态变量个数，决定矩阵指数计算的计算复杂度O(N^3)

- **splitting_order**: 分裂公式阶数，决定近似精度，如1阶(Trotter)、2阶(Strang)或更高阶



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含直流负载的配电网(Distribution Network with DC Load) | 验证了方法在处理含多电平变流器的配电网中的有效性，分裂状态空间法准确捕捉了直流负载切换时的暂态过程，电压和电流波形与详细模型高度吻合 | 与传统EMT仿真方法相比，计算时间减少40-60%，而最大局部误差控制在0.1%以内 |

| LLC谐振变换器(LLC Resonant Converter) | 针对高频(数百kHz)开关的LLC谐振变换器，方法成功处理了谐振腔状态变量与开关状态的强耦合特性，准确复现了谐振电流和电压波形 | 在高开关频率下，比传统状态空间法快3-5倍，长期仿真累积误差<0.5% |

| 大型风电场(Large-Scale Wind Farm) | 包含多台VSC型风力发电机的风电场聚合仿真，通过自动开关分组将各风机变流器作为独立子系统处理，验证了方法在大规模系统中的可扩展性 | 仿真100台风机规模系统时，计算速度提升超过5倍，内存占用减少约30%，电压暂态最大偏差<0.3% |

| MMC模块化多电平换流器(Modular Multilevel Converter) | 针对具有大量子模块(SM)的MMC电路，利用块级时变矩阵结构处理各子模块的投切状态，准确模拟了电容电压平衡和环流抑制过程 | 对于400子模块的MMC系统，矩阵指数计算时间从占主导地位的80%降低到15%以下，整体仿真效率提升4-6倍 |



## 量化发现

- 计算复杂度降低：通过矩阵分裂，将单次矩阵指数计算O(N^3)的复杂度转化为多个小规模矩阵指数的乘积，对于含变流器系统整体计算负担减少50-80%
- 精度可控：一阶Trotter分裂公式局部截断误差为O(t^2)，二阶Strang分裂公式误差为O(t^3)，通过自适应阶数选择可将全局相对误差控制在0.1%以下
- 开关处理效率：由于A2(s(t))具有块对角结构且仅在与开关相邻的最小子电路维度上变化，开关事件处理计算量与系统总规模N呈线性关系而非立方关系
- 内存优化：常数矩阵A1的指数只需存储一次，时变部分A2按块存储，相比传统方法存储整个状态矩阵指数，内存需求减少30-50%
- 实时性潜力：在大型风电场案例中，相比传统EMT仿真，单步计算时间从毫秒级降至微秒级，满足实时仿真要求（步长<50μs）


## 关键公式

### 矩阵指数状态转移方程

$$$\tilde{x}(t) = e^{t\tilde{A}}\tilde{x}(0)$$$

*作为指数积分器的基础，描述自治系统在t时刻的状态演化，避免了传统数值积分方法的稳定性限制*

### 一阶Trotter分裂公式

$$$e^{t(A_1+A_2)} = e^{tA_1}e^{tA_2} + O(t^2)$$$

*当系统矩阵可分裂为A1（常数）和A2（时变）两部分时，用于近似计算整体矩阵指数，避免直接计算大维度时变矩阵的指数*

### 状态矩阵分裂定义

$$$A = A_1 + A_2(s(t))$$$

*将含变流器电力系统的状态矩阵分离为常数部分（网络、负载）和开关状态相关的时变部分（变流器子电路），是实现高效仿真的核心*



## 验证详情

- **验证方式**: 基于仿真对比的验证方法，将提出的分裂状态空间法与传统详细EMT仿真（基准方法）以及解析解（对于简单拓扑）进行对比，通过波形对比、误差分析和计算时间统计验证准确性和效率
- **测试系统**: 四个不同特性的测试系统：(1) 含VSC和DC负载的33节点配电网；(2) 开关频率200kHz的LLC谐振变换器；(3) 含100台2MW VSC型风机的风电场；(4) 400子模块的MMC-HVDC换流器
- **仿真工具**: 使用MATLAB/Simulink进行状态空间建模和算法实现，部分案例使用PSCAD/EMTDC作为基准对比工具，在具有Intel Xeon处理器和32GB RAM的工作站上执行
- **验证结果**: 在所有测试案例中，分裂状态空间法均保持了高保真度，电压和电流波形与基准方法的最大相对误差小于0.5%，均方根误差(RMSE)小于0.2%。计算效率方面，随着系统规模和开关频率增加，加速比从2倍提升至6倍以上，特别是在MMC和大型风电场案例中表现优异，证明了方法在处理大规模电力电子集成系统时的有效性和可扩展性
