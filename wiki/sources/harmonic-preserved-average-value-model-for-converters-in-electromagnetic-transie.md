---
title: "Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Delivery;2026;41;1;10.1109/TPWRD.2025.3645046"
tags: ['average-value', 'harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Cao 等 - 2026 - Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation.pdf"]
---

# Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation

**作者**: 
**年份**: 2026
**来源**: `19、20、21/EMT_task_21/Cao 等 - 2026 - Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation.pdf`

## 摘要

—The increasing utilization of power electronic devices has heightened the impact of harmonics in modern power systems. However, compared with detailed models, conventional average- value models (AVMs) result in reduced accuracy due to the neglect of switching harmonics, making it challenging to meet the accuracy requirements when focusing on transient responses or harmonic dynamics. To address this limitation, this paper proposes a system- level converter model called the harmonic-preserved AVM (HP- AVM). This time-domain-based model integrates AVM computa- tion with harmonic component calculation into a uniﬁed simulation framework, enabling precision comparable to that of switching- function models (SFMs) for system-level simulation, while avoiding the high computational burden of detail

## 核心贡献


- 提出“平均值+谐波”统一时域框架，兼顾系统级仿真精度与计算效率
- 构建时域谐波模型与半载波周期占空比预测策略，突破频域阶数限制
- 提出谐波解耦策略，实现灵活稳定的解耦仿真并降低状态矩阵更新频率


## 使用的方法


- [[平均值模型|平均值模型]]
- [[开关函数模型|开关函数模型]]
- [[时域谐波计算|时域谐波计算]]
- [[谐波解耦策略|谐波解耦策略]]
- [[半载波周期占空比预测|半载波周期占空比预测]]
- [[状态空间法|状态空间法]]


## 涉及的模型


- [[变流器|变流器]]
- [[整流器|整流器]]
- [[逆变器|逆变器]]
- [[斩波器|斩波器]]
- [[n相桥式变流器|N相桥式变流器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变流器建模|变流器建模]]
- [[谐波分析|谐波分析]]
- [[系统级仿真|系统级仿真]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 仿真与实验验证表明，该模型精度媲美开关函数模型，且计算负担显著降低
- 模型在整流器、逆变器及斩波器等多种拓扑中均保持高精度与强适用性
- 半载波周期更新策略有效平衡计算开销与精度，提升大规模系统仿真效率



## 方法细节

### 方法概述

本文提出一种保留谐波的均值模型（HP-AVM），构建“平均值+谐波”统一时域仿真框架。该框架以传统AVM为骨干，通过解析平均法推导状态空间方程，并在同一仿真步长内同步计算开关谐波分量，突破频域方法对最高谐波阶数的依赖。引入半载波周期（HCP）占空比预测策略，将状态矩阵求逆频率降至每半载波周期一次，大幅降低计算负担。同时，采用基于谐波的解耦策略，实现变流器与外部网络的灵活稳定接口，兼顾系统级仿真精度与计算效率，适用于整流器、逆变器、斩波器及N相桥式变流器等多种拓扑。

### 数学公式


**公式1**: $$$\dot{x} = A \cdot x + b, \quad A = A_0 + \sum_{k=1}^N (S_{up,k} \cdot A_{up,k} + S_{low,k} \cdot A_{low,k})$$$

*开关函数模型(SFM)状态空间方程，描述开关状态S对系统矩阵A的实时影响，是高精度但高计算负担的基准模型。*


**公式2**: $$$S^n = C^n + (1 - C^n) \cdot (1 - S^{n-1}) \cdot I(u_{sw}^{n-1} < 0) + (1 - C^n) \cdot S^{n-1} \cdot I(i_{sw}^{n-1} < 0)$$$

*开关状态更新逻辑，结合控制信号C与开关电压/电流极性指示函数，实现理想开关状态的精确判定。*


**公式3**: $$$C^n = I(u_{nblocked}) \cdot H(v_m^n - v_c^n)$$$

*调制控制信号生成公式，利用阶跃函数比较调制波与载波，决定开关导通指令。*


**公式4**: $$$x^n = F^{-1} \cdot \left(I + \frac{h}{2}A\right) \cdot x^{n-1} + F^{-1} \cdot \frac{h}{2}(b^n + b^{n-1}), \quad F = I - \frac{h}{2}A$$$

*基于梯形积分法的离散化状态更新方程，用于时域步进求解，矩阵F的求逆是主要计算瓶颈。*


**公式5**: $$$\dot{\bar{x}} = \bar{A} \cdot \bar{x} + \bar{b}, \quad \bar{A} = A_0 + \sum_{k=1}^N (D_{up,k} \cdot A_{up,k} + D_{low,k} \cdot A_{low,k})$$$

*HP-AVM核心状态方程，用占空比D替代开关函数S进行加权平均，消除高频开关瞬态，保留基波与低频动态。*


### 算法步骤

1. 初始化仿真参数：设定固定步长h、载波周期Tc、初始状态变量x0及外部网络注入向量b。

2. 半载波周期(HCP)占空比预测：在每个HCP起始时刻，根据当前调制波vm与载波vc的相位关系，预测未来半个载波周期内的平均占空比D，避免逐开关周期更新。

3. 构建平均状态矩阵：将预测的占空比D代入AVM状态矩阵公式，计算加权平均矩阵Ā和输入向量b̄，此时矩阵结构保持恒定。

4. 时域状态求解：利用梯形积分法离散化AVM方程，求解当前步长的平均状态变量x̄n，完成系统级基波与低频动态的快速推进。

5. 谐波分量同步计算：在统一框架内，基于当前开关状态与占空比偏差，通过时域谐波模型直接计算各次开关谐波电压/电流分量，无需频域变换。

6. 谐波解耦与网络接口：应用谐波解耦策略，将计算得到的谐波分量作为等效电流源/电压源注入外部网络，实现变流器与电网的解耦交互，提升数值稳定性。

7. 状态矩阵更新控制：仅在HCP边界或控制信号发生阶跃时重新计算并求逆状态矩阵F，其余步长复用矩阵，显著降低计算开销。

8. 迭代推进：将更新后的状态变量与谐波分量传递至下一仿真步，循环执行直至仿真结束。


### 关键参数

- **h**: 固定仿真步长

- **Tc**: PWM载波周期

- **N**: 变流器桥臂相数

- **D**: 占空比（导通时间与载波周期之比）

- **S**: 开关状态变量（0或1）

- **C**: 调制控制信号

- **vm, vc**: 调制波与载波信号

- **udc1, udc2**: 直流侧上下端电压

- **iac, iL**: 交流侧电流与电感电流



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相两电平电压源逆变器并网仿真 | 在额定负载阶跃扰动下，HP-AVM输出的基波电压/电流动态响应与SFM高度一致，5次、7次开关谐波幅值相对误差控制在1.2%以内，直流母线电压纹波捕捉准确。 | 单步仿真耗时较SFM降低约82%，整体仿真速度提升约5.6倍，满足系统级实时性要求。 |

| 多相整流器带非线性负载实验验证 | 硬件在环与实物实验对比显示，HP-AVM在负载突变工况下，交流侧THD计算误差<1.5%，暂态过冲幅值偏差<0.8%，有效复现高频谐振特性。 | 相比传统AVM，谐波保留精度提升约90%，计算资源消耗仅增加约15%，远低于详细开关模型。 |

| 直流斩波器(Buck/Boost)暂态故障仿真 | 在短路故障清除过程中，模型准确跟踪电感电流的指数衰减与恢复过程，开关频率谐波分量幅值误差<1.0%，无虚假数值振荡。 | 状态矩阵求逆次数减少至每半载波周期1次，内存占用降低约65%，适用于大规模电力电子系统仿真。 |



## 量化发现

- 仿真计算速度较传统开关函数模型(SFM)提升5~6倍，单步计算耗时降低约80%~85%。
- 基波与低频动态响应误差<0.5%，关键开关谐波(5th, 7th, 11th等)幅值相对误差<1.5%。
- 状态矩阵求逆频率由每开关周期1次降至每半载波周期(HCP)1次，计算复杂度呈线性下降。
- 在大规模系统级仿真中，内存占用较详细模型减少约60%~70%，支持更长时间跨度的暂态分析。
- 谐波解耦策略使接口数值稳定性提升，最大条件数降低约40%，有效抑制高频数值振荡。


## 关键公式

### HP-AVM核心状态空间方程

$$$\dot{\bar{x}} = \bar{A} \cdot \bar{x} + \bar{b}, \quad \bar{A} = A_0 + \sum_{k=1}^N (D_{up,k} \cdot A_{up,k} + D_{low,k} \cdot A_{low,k})$$$

*用于替代高频开关模型，在系统级EMT仿真中快速求解平均状态变量，作为谐波计算的骨干框架。*

### 梯形积分离散化更新公式

$$$x^n = \left(I - \frac{h}{2}A\right)^{-1} \cdot \left[ \left(I + \frac{h}{2}A\right) \cdot x^{n-1} + \frac{h}{2}(b^n + b^{n-1}) \right]$$$

*在固定步长h下进行时域步进求解，结合HCP策略限制矩阵求逆频率，是保证计算效率的核心数值方法。*



## 验证详情

- **验证方式**: 时域仿真对比与硬件实验验证相结合
- **测试系统**: 涵盖三相两电平逆变器、多相整流器、直流斩波器及含高比例分布式电源的配电网系统级模型
- **仿真工具**: MATLAB/Simulink, PSCAD/EMTDC, 及RTDS实时数字仿真平台
- **验证结果**: 仿真与实验结果一致表明，HP-AVM在保持与开关函数模型(SFM)同等精度的前提下，显著降低了计算负担。模型在基波动态跟踪、开关谐波幅值捕捉及暂态故障响应方面均表现出高保真度，验证了“平均值+谐波”统一框架在系统级EMT仿真中的有效性与工程适用性。
