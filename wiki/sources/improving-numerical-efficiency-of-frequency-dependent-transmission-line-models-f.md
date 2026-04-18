---
title: "Improving numerical efficiency of frequency dependent transmission line models for EMT simulations"
type: source
authors: ['H.M.Jeewantha', 'De', 'Silva']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112328. doi:10.1016/j.epsr.2025.112328"
tags: ['frequency-dependent', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations-1.pdf"]
---

# Improving numerical efficiency of frequency dependent transmission line models for EMT simulations

**作者**: H.M.Jeewantha, De, Silva
**年份**: 2025
**来源**: `23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations-1.pdf`

## 摘要

Improving numerical efficiency of frequency dependent transmission line This paper compares two model order reduction techniques for frequency dependent transmission line models to enhance numerical performance for large cable or overhead line systems. The Modal Truncation and Balanced Truncation methods are applied to reduce the order of propagation matrix. The simulation examples involving underground cable systems are presented for comparison. Time domain simulation results with linear termi­

## 核心贡献


- 提出将模态截断与平衡截断算法应用于频变线路传播矩阵降阶提升仿真效率
- 首次将平衡截断法引入频变线路建模保证降阶模型稳定并提供先验误差界
- 设计迭代降阶流程保留关键模态极点有效降低递归卷积计算负担


## 使用的方法


- [[模型降阶|模型降阶]]
- [[模态截断|模态截断]]
- [[平衡截断|平衡截断]]
- [[矢量拟合|矢量拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[递归卷积|递归卷积]]


## 涉及的模型


- [[频变输电线路模型|频变输电线路模型]]
- [[通用线路模型|通用线路模型]]
- [[地下电缆|地下电缆]]
- [[多回电缆系统|多回电缆系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[模型降阶|模型降阶]]
- [[实时仿真|实时仿真]]
- [[数值效率优化|数值效率优化]]


## 主要发现


- 平衡截断法降阶后严格保证模型渐近稳定性且提供明确先验误差上界
- 模态截断法剔除小留数极点项显著降低传播矩阵阶数并缩短仿真耗时
- 两种方法在双回电缆算例中保持高精度有效缓解过拟合导致的无源性破坏



## 方法细节

### 方法概述

本文针对电磁暂态(EMT)仿真中大型多回电缆系统频变线路模型（特别是传播矩阵$A(\omega)$）阶数过高导致的计算效率低下及过拟合引发无源性破坏问题，提出并对比了两种模型降阶(MOR)技术：模态截断(MT)与平衡截断(BT)。传统通用线路模型(ULM)采用统一误差容限对各模态传播函数进行矢量拟合，易造成部分模态过拟合。本文在频域有理函数逼近阶段引入降阶策略：MT通过剔除留数/极点比值较小的非主导极点项直接降低阶数；BT则基于状态空间实现，通过求解Lyapunov方程计算能控/能观Gramian矩阵，利用Hankel奇异值截断弱能控能观状态，严格保证降阶后模型的渐近稳定性并提供先验误差界。两种方法均设计为迭代流程，在降阶后重新进行相域矩阵拟合，直至满足预设精度要求，从而显著降低时域递归卷积的计算复杂度。

### 数学公式


**公式1**: $$$f_{\text{model}j}(s) = \sum_{k=1}^{N_j} \frac{c_{jk} e^{-s\tau_j}}{s - a_{jk}}$$$

*第$j$个模态传播函数的有理函数逼近表达式，包含极点$a_{jk}$、留数$c_{jk}$和模态时延$\tau_j$*


**公式2**: $$$\frac{\| c_k \|}{|a_k|} > \text{tol}$$$

*模态截断(MT)的保留条件，仅保留留数与极点幅值比值大于设定容限的项*


**公式3**: $$$A = S^{-1}AS, \quad B = S^{-1}B, \quad C = CS$$$

*平衡截断(BT)中用于将状态空间矩阵转换为实块对角形式的坐标变换*


**公式4**: $$$\varepsilon = \| f(s)_{(p,q)} - f(s)_{\text{actual}} \|$$$

*相域传播矩阵元素的拟合误差范数，用于迭代降阶的收敛判断*


### 算法步骤

1. 步骤1（模态拟合与初始评估）：使用矢量拟合技术对解耦后的模态传播函数$A_{\text{modes}}(\omega)$进行独立有理函数逼近，设定统一的最大阶数限制（如20阶）和初始模态误差容限$\varepsilon_1$。

2. 步骤2（MT降阶筛选）：计算每个模态拟合结果中各极点项的留数/极点比值$\|c_k\|/|a_k|$，按升序排列。剔除比值小于预设容限tol的非主导项，保留主导极点集合。

3. 步骤3（BT状态空间降阶）：将模态传递函数转换为状态空间形式$(A,B,C)$，通过变换矩阵$S$转换为实块对角型。求解Lyapunov方程获取能控与能观Gramian矩阵，计算Hankel奇异值$\sigma_i$。截断满足$\sigma_i < \text{tol}$的弱能控能观状态，得到降阶系统矩阵$\tilde{A}$。

4. 步骤4（相域矩阵重构与拟合）：提取MT或BT降阶后保留的新极点集合，结合原始模态时延$\tau_j$，对相域传播矩阵$A(\omega)$的元素进行二次有理函数拟合。

5. 步骤5（误差校验与迭代）：计算相域拟合误差$\varepsilon$。若$\varepsilon < \varepsilon_{\max}$（如0.5%），则终止流程；否则，按比例缩小容限（$\text{tol} = k \times \text{tol}, k<1.0$）或收紧模态误差容限（$\varepsilon_1 = \alpha \varepsilon_1, \alpha<1$），返回步骤2或3重新执行降阶与拟合，直至满足精度要求。


### 关键参数

- **最大模态/导纳函数阶数限制**: 20

- **相域最大允许拟合误差(ε_max)**: 0.5%

- **土壤电阻率**: 100 Ω·m

- **MT/BT截断容限(tol)**: 迭代动态调整的小正数

- **模态时延组1**: 0.240345 ms (初始阶数18)

- **模态时延组2**: 0.296956 ms (初始阶数8)

- **模态时延组3**: 1.191263 ms (初始阶数18)

- **模态时延组4**: 1.194583 ms (初始阶数18)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双回30km三相地下电缆系统（扁平排列） | 在时域线性终端条件下进行EMT仿真。应用MT与BT降阶后，传播矩阵$A(\omega)$的阶数显著降低，递归卷积计算量大幅减少。仿真波形与全阶模型高度吻合，相域拟合误差严格控制在0.5%以内，且有效消除了因过拟合导致的无源性破坏现象。 | 相比传统ULM全阶拟合，降阶模型在保持同等精度的前提下，显著降低了内存占用与单步计算耗时，有效避免了实时仿真中的时间步长越限问题，数值稳定性与计算效率均得到实质性提升。 |



## 量化发现

- 相域传播矩阵拟合误差严格控制在0.5%以内（ε_max = 0.5%）
- 初始模态拟合阶数最高达18阶，经降阶后有效剔除冗余极点，阶数显著压缩
- 模态时延分布明确分为4组，分别为0.240345ms、0.296956ms、1.191263ms和1.194583ms
- BT方法提供严格的先验误差上界，并数学保证降阶后系统的渐近稳定性
- MT方法通过留数/极点比值筛选，直接降低递归卷积的极点数量，缩短仿真耗时
- 土壤电阻率设定为100 Ω·m，忽略土壤参数的频变特性以简化计算


## 关键公式

### 模态截断(MT)主导项筛选准则

$$$\frac{\| c_k \|}{|a_k|} > \text{tol}$$$

*在MT降阶流程中，用于判断是否保留特定极点-留数项的核心判据，剔除比值过小的非主导动态分量*

### 相域传播矩阵元素重构公式

$$$f(s)_{(p,q)} = \sum_{j=1}^{M} \sum_{k=1}^{N_j} \frac{c_{jk} e^{-s\tau_j}}{s - a_{jk}}$$$

*在降阶获得新极点集合后，用于重新拟合相域$A(\omega)$矩阵元素，是连接模态降阶与全相域仿真的关键桥梁*

### 平衡截断(BT)状态空间坐标变换

$$$A = S^{-1}AS, \quad B = S^{-1}B, \quad C = CS$$$

*在BT方法中，将原始状态空间模型转换为实块对角形式，为后续求解Lyapunov方程和计算Hankel奇异值做准备*



## 验证详情

- **验证方式**: 时域电磁暂态(EMT)仿真对比分析（线性终端条件）
- **测试系统**: 双回30km三相地下电缆系统（扁平排列配置），包含导体、屏蔽层、铠装层及多层绝缘结构
- **仿真工具**: 基于RTDS Technologies Inc.开发的EMT仿真平台（集成通用线路模型ULM与自定义降阶算法）
- **验证结果**: 验证表明MT与BT降阶技术均能在保证相域拟合误差<0.5%的前提下，有效降低传播矩阵阶数。BT法严格保障系统稳定性并提供误差界，MT法计算更直接。两者均成功抑制了过拟合引发的无源性破坏，显著提升了大规模电缆系统EMT仿真的数值效率与实时仿真可行性。
