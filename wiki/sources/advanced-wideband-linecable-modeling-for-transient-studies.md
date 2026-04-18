---
title: "Advanced Wideband Line/Cable Modeling for Transient Studies"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Delivery;2024;39;5;10.1109/TPWRD.2024.3449868"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Ramirez 等 - 2024 - Advanced Wideband LineCable Modeling for Transient Studies.pdf"]
---

# Advanced Wideband Line/Cable Modeling for Transient Studies

**作者**: 
**年份**: 2024
**来源**: `06/Ramirez 等 - 2024 - Advanced Wideband LineCable Modeling for Transient Studies.pdf`

## 摘要

—The grouping of propagation modes in line/cable sys- tems involving a large number of conductors has been central in recent research regarding the stability of simulations for elec- tromagnetic transient (EMT) studies. This article presents three improvements to the existing wideband line/cable modeling tech- niques for EMT analysis. The ﬁrst improvement consists of cal- culating optimum time delays such that the oscillations in the phase angle of the propagation function are reduced. The second is a novel strategy for grouping propagation modes. As a third improvement, the maximum ﬁtting frequency of a rapidly decaying mode is limited when its magnitude is below a threshold value. It is demonstrated that these modiﬁcations improve the stability characteristics oftime-domainsimulation,com

## 核心贡献


- 提出基于最小相位函数的最优时延计算方法有效降低传播函数相位角振荡
- 设计基于时延相近性的自适应传播模式分组策略显著降低残差与极点比值
- 引入快速衰减模式最大拟合频率阈值限制机制提升高频段拟合精度与稳定性


## 使用的方法


- [[极点-留数拟合|极点-留数拟合]]
- [[最小相位函数分析|最小相位函数分析]]
- [[布伦特优化算法|布伦特优化算法]]
- [[自适应模式分组|自适应模式分组]]
- [[频域综合|频域综合]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[输电线路|输电线路]]
- [[地下电缆|地下电缆]]
- [[频变电缆模型-fdcm|频变电缆模型(FDCM)]]
- [[多导体电缆系统|多导体电缆系统]]


## 相关主题


- [[宽频线路电缆建模|宽频线路电缆建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性|数值稳定性]]
- [[无源性违规|无源性违规]]
- [[频率相关参数|频率相关参数]]
- [[时域仿真|时域仿真]]


## 主要发现


- 改进方法显著降低残差极点比与无源性违规解决传统ULM短电缆系统失稳
- 在含九十六根电缆与双回架空线复杂系统中验证时域仿真稳定性与精度均提升
- 最优时延与频率阈值限制有效减少传播函数高频相位振荡降低有理逼近阶数



## 方法细节

### 方法概述

本文针对通用线路模型（ULM）在短电缆及多导体系统中易出现高残差/极点比与无源性违规导致时域失稳的问题，提出三项核心改进。首先，基于最小相位函数理论，利用Bode公式初估时延，并结合Brent优化算法在$[0.9\tau_B, 1.1\tau_B]$区间内搜索最优时延，以最小化传播函数相位振荡并降低有理逼近阶数。其次，摒弃传统固定相移差分组准则，提出基于时延相近性的自适应分组策略，根据组内最小时延是否小于1μs动态设定容差范围，有效合并相似模式。最后，针对快速衰减模式，设定幅值阈值$10^{-3}$作为最大拟合频率截断点，抑制高频相位畸变。三者协同显著提升了宽频线路/电缆模型的数值稳定性与拟合效率。

### 数学公式


**公式1**: $$$H = T H_m T^{-1} = T \text{diag}\{e^{\lambda_1}, e^{\lambda_2}, \dots, e^{\lambda_{N_c}}\} T^{-1}$$$

*传播矩阵的模态分解公式，将相域传播矩阵$H$通过特征向量矩阵$T$解耦为对角模态矩阵$H_m$，其中$\lambda_n$为$-YZl$的特征值。*


**公式2**: $$$H_i = \sum_{n=1}^{M_i} \frac{c_n}{s - p_n} e^{-s\tau_i}$$$

*第$i$个模态传播函数的极点-留数有理逼近模型，$p_n$和$c_n$分别为极点和留数，$\tau_i$为模态时延，$M_i$为逼近阶数。*


**公式3**: $$$H = \sum_{i=1}^{N} \sum_{k=1}^{M_i} \frac{R_{i,k}}{s - p_{i,k}} e^{-s\tau_i}$$$

*相域传播矩阵综合公式，将分组后的模态极点与留数通过残差矩阵$R_{i,k}$重构回相域，用于时域卷积计算。*


### 算法步骤

1. 利用Bode公式计算初始时延$\tau_B$作为优化基准。

2. 设定Brent无导数优化算法的搜索区间为左边界$0.9\tau_B$与右边界$1.1\tau_B$。

3. 在区间内迭代评估候选时延对传播函数$H_i$相位展开（unwinding）的影响，监测相位曲线跨越$\pm 180^\circ$的频率点。

4. 选择使相位曲线在宽频带内最接近最小相位函数特性的候选时延。

5. 结合极点数量动态调整，计算当前时延配置下的有理逼近误差。

6. 输出使逼近误差最小且相位振荡最低的最优时延$\tau_o$。

7. 执行自适应分组：遍历所有模式时延，若组内最小时延$<1\mu s$，则将相差一个十进制位内的时延归入同组；若$>1\mu s$，则按整数位相近性合并，最终输出各组代表时延以替代传统固定相移差准则。


### 关键参数

- **幅值截断阈值**: $10^{-3}$（用于确定快速衰减模式的最大拟合频率$f_{max}$）

- **Brent优化区间**: $[0.9\tau_B, 1.1\tau_B]$

- **分组容差基准**: 1 μs（区分小数位与整数位合并策略的临界值）

- **拟合误差容限测试集**: 5%, 1%, 0.5%, 0.1%, 0.01%, 0.001%

- **无源性扫描范围**: 拟合最低频前两个数量级至$f_{max}$后两个数量级



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 9电缆地下系统 | 在0.5%、0.1%、0.01%和0.001%拟合容差下均实现时域稳定，残差/极点比显著降低，且4个工况完全满足无源性要求。 | 传统ULM在0.1%容差下即发生数值失稳，改进版在同等精度要求下保持全工况稳定且逼近阶数更低。 |

| 96电缆+双回架空线混合系统（250m） | 在5%和1%容差下稳定运行，模式分组数由36组大幅压缩至8组，总逼近阶数下降，残差/极点比优于基线。 | 传统ULM在所有测试容差下均失稳；改进版通过自适应分组将分组数量减少77.8%，彻底解决短线路多导体发散问题。 |

| 地上双回电缆系统（1km，时延跨度1.18~3.58μs） | 在5%、1%和0.5%容差下稳定，模式分组数由10组降至4组，高频相位振荡得到有效抑制。 | 传统ULM仅在5%容差下稳定，改进版在更严苛的1%和0.5%容差下仍保持稳定，残差/极点比降低超60%。 |

| 非对称电缆系统（15km） | 在5%、1%和0.5%容差下均输出稳定时域波形，与数值拉普拉斯变换（NLT）基准高度吻合。 | 传统ULM仅在5%容差下稳定，改进版将稳定容限扩展至0.5%，且波形误差在工程允许范围内。 |



## 量化发现

- 快速衰减模式最大拟合频率截断阈值设定为幅值$10^{-3}$，可使高频相位振荡显著降低，有理逼近阶数平均减少约20%~30%。
- 自适应分组策略将96电缆系统的模式分组数由36组压缩至8组，地上双回系统由10组压缩至4组，大幅降低矩阵维度。
- 拟合容差低于0.5%（如0.1%、0.01%）对时域波形精度提升无实质性影响（波形重合度>99.9%），但会成倍增加计算阶数。
- 改进模型在全部4个测试案例中均实现时域稳定，残差/极点比最大值较传统方法下降超过一个数量级，无源性违规程度显著减轻。


## 关键公式

### 模态传播函数极点-留数拟合模型

$$$H_i = \sum_{n=1}^{M_i} \frac{c_n}{s - p_n} e^{-s\tau_i}$$$

*用于在频域对解耦后的各模态传播函数进行有理逼近，提取最优时延$\tau_i$以消除相位振荡，是ULM频变参数拟合的核心。*

### 相域传播矩阵综合公式

$$$H = \sum_{i=1}^{N} \sum_{k=1}^{M_i} \frac{R_{i,k}}{s - p_{i,k}} e^{-s\tau_i}$$$

*将分组优化后的模态极点、留数及时延通过残差矩阵重构回相域，直接用于EMTP时域递归卷积计算，决定仿真稳定性。*



## 验证详情

- **验证方式**: 频域拟合精度评估、时域波形对比、无源性特征值扫描验证、与数值拉普拉斯变换(NLT)基准对比分析
- **测试系统**: 9电缆地下系统、96电缆+双回架空线混合系统(250m)、地上双回电缆系统(1km)、非对称电缆系统(15km)
- **仿真工具**: EMTP (内置改进版ULM模块)、数值拉普拉斯变换(NLT)算法
- **验证结果**: 改进版在所有测试容差下均输出稳定时域波形，与NLT基准高度吻合；残差/极点比与无源性违规程度显著优于传统实现，验证了算法在复杂多导体短线路场景下的鲁棒性与工程适用性。
