---
title: "Electromagnetic Transient Analysis Using a Frequency Dependent Network Equivalent for Power Systems Integrating Wind Generation Sources"
type: source
authors: ['未知']
year: 2024
journal: "2024 IEEE Power & Energy Society General Meeting (PESGM);2024; ; ;10.1109/PESGM51994.2024.10688470"
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic transient analysis using a frequency dependent network equivalent for power systems_Verduzco-Durán 等_2024.pdf"]
---

# Electromagnetic Transient Analysis Using a Frequency Dependent Network Equivalent for Power Systems Integrating Wind Generation Sources

**作者**: 
**年份**: 2024
**来源**: `15/Electromagnetic transient analysis using a frequency dependent network equivalent for power systems_Verduzco-Durán 等_2024.pdf`

## 摘要

—This article addresses the application of a reduced order representation for analysis of power systems with wind gen- eration sources under fault conditions. A frequency-dependent network equivalent (FDNE) based on a rational function in the discrete-time is used to model the external area of the power system. The characterization of the frequency-dependent terminal admittance at the boundary busbar is carried out through the excitation of a constant voltage source at variable frequency modeled by a multisine signal. Parameter identiﬁcation techniques based on the recursive least squares method are applied. Regarding the wind energy conversion system (WECS), a type-4 wind turbine based on a permanent magnet synchronous generator with a full-scale back-to-back converter is used. The WECS c

## 核心贡献


- 提出基于离散时间有理函数的频变网络等值模型，实现外部电网降阶建模
- 采用多正弦信号激励与递推最小二乘法，完成边界母线频变导纳参数辨识
- 在含四型风电机组的两区域系统中验证等值模型，显著提升故障仿真效率


## 使用的方法


- [[fdne-model|FDNE]]
- [[离散时间有理函数逼近|离散时间有理函数逼近]]
- [[多正弦信号激励|多正弦信号激励]]
- [[递推最小二乘法参数辨识|递推最小二乘法参数辨识]]
- [[诺顿等值源集成|诺顿等值源集成]]


## 涉及的模型


- [[四型风力发电机组|四型风力发电机组]]
- [[永磁同步发电机-pmsg|永磁同步发电机(PMSG)]]
- [[全功率背靠背变流器|全功率背靠背变流器]]
- [[kundur两区域电力系统|Kundur两区域电力系统]]
- [[频变网络等值模型|频变网络等值模型]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[动态等值与降阶建模|动态等值与降阶建模]]
- [[风电并网仿真|风电并网仿真]]
- [[故障暂态分析|故障暂态分析]]
- [[参数辨识|参数辨识]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 等值模型在单相与三相接地故障下能高精度复现全阶模型的暂态响应波形
- 相比全阶详细模型，FDNE显著降低CPU计算耗时，同时保持高仿真精度
- 仿真结果与PSCAD/EMTDC对比验证，证实了降阶等值方法的有效性



## 方法细节

### 方法概述

本文提出一种基于离散时间有理函数的频变网络等值（FDNE）方法，用于含风电电力系统电磁暂态仿真中的外部电网降阶建模。首先将系统划分为详细研究区与外部等值区，在边界母线注入多正弦扫频电压信号以激励网络。通过采集边界电压电流响应，构建单输入单输出离散传递函数模型。采用递推最小二乘法（RLS）在线辨识有理函数分子分母系数，避免矩阵求逆带来的计算负担。随后将辨识得到的频变导纳转换为时域差分方程，计算FDNE动态注入电流。为匹配稳态潮流，额外并联一个基频恒流源以补偿被FDNE滤除的工频分量。最终将FDNE诺顿等效源集成至研究区域边界，在含风电机组动态特性及多重故障的EMT环境中进行联合仿真，实现宽频带高精度与计算效率的平衡。

### 数学公式


**公式1**: $$$Y(z^{-1}) = \frac{b_1 z^{-1} + b_2 z^{-2} + \cdots + b_n z^{-n}}{1 + a_1 z^{-1} + a_2 z^{-2} + \cdots + a_n z^{-n}}$$$

*离散时间频变导纳传递函数，用于表征边界母线对外部网络的等效导纳特性*


**公式2**: $$$x(t) = \sum_{k=1}^{M} A_k \sin(2\pi f_k t + \phi_k)$$$

*多正弦激励信号数学模型，通过优化相位实现平坦频谱，用于宽频带网络扫频*


**公式3**: $$$\theta_k = \theta_{k-1} + K_k (\phi_k - x_k^T \theta_{k-1})$$$

*递推最小二乘法（RLS）核心参数更新公式，用于在线迭代辨识传递函数系数*


**公式4**: $$$I_f(k) = -\sum_{i=1}^{n} a_i I_f(k-i) + \sum_{i=1}^{n} b_i V_b(k-i)$$$

*FDNE时域差分递推方程，将频域有理函数转换为可直接嵌入EMT求解器的离散电流源*


### 算法步骤

1. 系统划分与边界定义：将目标电网划分为需精细建模的研究区域（含风电机组及关键母线）和待等值的外部区域，确定连接两者的边界母线（如母线10）。

2. 多正弦扫频激励与数据采集：在边界母线施加幅值恒定、频率覆盖1Hz至2500Hz（步长2Hz）的多正弦电压源，同步记录边界注入电流响应，获取宽频带导纳数据。

3. RLS参数辨识：构建离散SISO系统状态空间，初始化协方差矩阵$P_0$与参数向量$\theta_0$。按时间步迭代计算增益矩阵$K_k$、更新协方差$P_k$，并利用预测误差修正参数向量，直至收敛得到200阶有理函数系数$a_i, b_i$。

4. 诺顿等效源构建与基频补偿：将辨识系数代入时域差分方程计算FDNE动态电流$I_f(k)$；根据边界母线稳态潮流数据计算基频恒流源$I_{inj} = I_b - Y(60\text{Hz})V_b$，消除FDNE模型中的工频分量以避免重复计算。

5. EMT集成与暂态仿真：将FDNE动态电流源与基频恒流源并联接入研究区域边界节点，设置仿真步长为60Hz基频下512点/周期，在风速波动、功率控制切换及单相/三相接地故障工况下运行15秒电磁暂态仿真，记录电压电流轨迹并评估计算耗时。


### 关键参数

- **FDNE模型阶数**: 200

- **扫频范围**: 1 Hz ~ 2500 Hz

- **扫频步长**: 2 Hz

- **仿真时间步长**: 60 Hz基频下512点/周期

- **仿真总时长**: 15 s

- **风电机组额定容量**: 2 MW

- **风电机组额定线电压**: 2500 V

- **RLS遗忘因子/权重**: 文中隐含使用标准RLS结构，通过协方差矩阵$P_k$动态调整权重



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 频域导纳特性拟合验证 | 在1Hz至2500Hz宽频范围内，FDNE等值导纳的幅频与相频特性与全阶模型高度重合。幅值均方误差（MSE）为1.2950e-7，相位MSE为0.0461 rad，仅在高频段存在极微小的相角偏差。 | 频域拟合精度达到工程极高要求，幅值误差<1e-6，相位误差<0.05 rad，完全满足EMT宽频分析需求。 |

| 含风电多重故障时域暂态仿真 | 在11-11.2s施加母线7单相接地故障，12-12.2s施加母线8三相接地故障。风电机组参考角速度在5-5.2s和10-10.2s分别阶跃下降，稳态有功输出维持在约1.8 MW。FDNE动态电压/电流波形与PSCAD全阶基准完全一致。 | 计算效率显著提升，FDNE模型CPU耗时为66.28秒，全阶模型为107.57秒，仿真速度提升约1.62倍（提速38.4%），且时域波形偏差可忽略。 |



## 量化发现

- 频域导纳拟合精度极高，幅值均方误差低至1.2950×10⁻⁷，相位均方误差为0.0461 rad。
- 计算效率提升显著，FDNE降阶模型仿真耗时66.28秒，较全阶模型（107.57秒）提速1.62倍。
- 风电机组在风速波动与功率控制指令切换下，稳态有功输出稳定在约1.8 MW，等值模型能精准跟踪该非线性动态过程。
- 在11-11.2s单相接地与12-12.2s三相接地故障期间，FDNE时域响应与PSCAD基准结果最大偏差<0.5%，验证了宽频带等值在强暂态扰动下的鲁棒性。


## 关键公式

### 离散频变导纳传递函数

$$$Y(z^{-1}) = \frac{\sum_{i=1}^{n} b_i z^{-i}}{1 + \sum_{i=1}^{n} a_i z^{-i}}$$$

*用于在频域表征外部电网从边界母线看入的等效导纳，是FDNE建模的数学基础*

### FDNE时域差分递推方程

$$$I_f(k) = -\sum_{i=1}^{n} a_i I_f(k-i) + \sum_{i=1}^{n} b_i V_b(k-i)$$$

*将频域有理函数转换为可直接嵌入EMT电磁暂态求解器的离散时间电流源计算公式*

### 基频诺顿补偿电流公式

$$$I_{inj} \angle \beta_{inj} = I_b \angle \delta_b - Y(60\text{Hz})V_b \angle \theta_b$$$

*用于计算并联在FDNE旁的恒流源，以精确匹配边界母线稳态潮流并消除FDNE中的工频分量*

### 递推最小二乘参数更新方程

$$$\theta_k = \theta_{k-1} + K_k (\phi_k - x_k^T \theta_{k-1})$$$

*在扫频数据采集过程中实时迭代更新有理函数系数，避免大规模矩阵求逆，提升辨识效率*



## 验证详情

- **验证方式**: 对比分析（频域扫频响应曲线对比与时域多重故障暂态波形对比）
- **测试系统**: 改进型Kundur两区域测试系统（研究区含G1、G2及2MW四型PMSG风电机组，外部区含G3、G4，边界位于母线10）
- **仿真工具**: PSCAD/EMTDC®（作为全阶基准验证工具），自定义算法实现（用于多正弦激励生成、RLS参数辨识及FDNE诺顿源集成）
- **验证结果**: 频域1-2500Hz范围内导纳幅相特性高度一致（MSE极小）；时域在风速波动、功率控制切换及单相/三相接地故障工况下，电压电流动态轨迹与PSCAD全阶仿真完全吻合；计算耗时降低38.4%，在保证EMT精度的前提下显著提升了含高比例电力电子设备的电网仿真效率。
