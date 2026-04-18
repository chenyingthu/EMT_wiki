---
title: "Improving numerical efficiency of frequency dependent transmission line models for EMT simulations"
type: source
authors: ['H.M.Jeewantha', 'De', 'Silva']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112328. doi:10.1016/j.epsr.2025.112328"
tags: ['frequency-dependent', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations.pdf"]
---

# Improving numerical efficiency of frequency dependent transmission line models for EMT simulations

**作者**: H.M.Jeewantha, De, Silva
**年份**: 2025
**来源**: `23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations.pdf`

## 摘要

Improving numerical efficiency of frequency dependent transmission line This paper compares two model order reduction techniques for frequency dependent transmission line models to enhance numerical performance for large cable or overhead line systems. The Modal Truncation and Balanced Truncation methods are applied to reduce the order of propagation matrix. The simulation examples involving underground cable systems are presented for comparison. Time domain simulation results with linear termi­

## 核心贡献


- 提出将模态截断与平衡截断技术应用于频变线路传播矩阵降阶
- 设计基于残差极点比与汉克尔特征值的迭代筛选流程降低计算负担
- 验证平衡截断法在保障系统渐近稳定与提供先验误差界方面的优势


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[模态截断|模态截断]]
- [[平衡截断|平衡截断]]
- [[模型降阶|模型降阶]]
- [[有理函数逼近|有理函数逼近]]
- [[递归卷积|递归卷积]]


## 涉及的模型


- [[频变输电线路模型|频变输电线路模型]]
- [[通用线路模型|通用线路模型]]
- [[地下电缆|地下电缆]]
- [[多回路电缆系统|多回路电缆系统]]
- [[传播矩阵|传播矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[模型降阶|模型降阶]]
- [[实时仿真|实时仿真]]
- [[广域建模|广域建模]]
- [[数值效率优化|数值效率优化]]


## 主要发现


- 模态截断法直接应用效果不佳需结合残差极点比迭代筛选满足精度
- 平衡截断法能有效降低传播矩阵阶数同时严格保证降阶模型稳定性
- 降阶后的频变线路模型在多回路电缆时域仿真中显著提升计算效率



## 方法细节

### 方法概述

本文提出将模型降阶技术(MOR)应用于频变输电线路模型的传播矩阵A(ω)有理函数逼近，以解决多回路电缆系统中因过拟合导致的高阶数问题。方法基于通用线路模型(ULM)的两阶段拟合框架：首先计算模态延迟并独立拟合Amodes(ω)矩阵的各个模态，然后利用模态极点和延迟拟合相位A(ω)矩阵。针对降阶环节，比较了模态截断(MT)和平衡截断(BT)两种技术。MT通过残差/极点比筛选并迭代移除非主导极点；BT则通过求解Lyapunov方程获得可控性和可观性Gramian矩阵，基于Hankel特征值截断状态空间，保证降阶系统的渐近稳定性并提供先验误差界。

### 数学公式


**公式1**: $$$f_{model_j}(s) = \sum_{k=1}^{N_j} \frac{c_{jk}e^{-s\tau_j}}{s-a_{jk}}$$$

*第j个模态传播函数的有理函数逼近形式，其中$c_{jk}$为留数，$a_{jk}$为极点，$\tau_j$为模态延迟，$N_j$为模态阶数*


**公式2**: $$$f(s)(p,q) = \sum_{j=1}^{M} \sum_{k=1}^{N_j} \frac{c_{jk}e^{-s\tau_j}}{s-a_{jk}}$$$

*相位A(ω)矩阵元素(p,q)的有理函数逼近，M为模态数，利用模态极点和延迟构建相位函数*


**公式3**: $$$\frac{\| c_k \|}{|a_k|} > \text{tol}$$$

*模态截断(MT)的筛选条件，基于留数与极点幅值比，保留大于容差tol的项*


**公式4**: $$$\left\| \frac{c_k}{s-a_k} + \frac{c_{k+1}}{s-a_{k+1}} \right\| > \text{tol}, \quad s_k = \text{imag}(a_k)$$$

*针对复共轭极点对的联合筛选条件，确保复数模态对的完整性*


**公式5**: $$$\tilde{A} = S^{-1}AS, \quad \tilde{B} = S^{-1}B, \quad \tilde{C} = CS$$$

*平衡截断(BT)中的块对角变换，将状态空间系统(A,B,C)转换为实块对角形式以便截断*


### 算法步骤

1. 阶段一：模态函数拟合。计算A(ω)矩阵的模态延迟，使用矢量拟合(Vector Fitting)技术独立拟合各模态Amodes(ω)，设定公共误差容差ε₁，确保各模态满足精度要求

2. 阶段二：相位矩阵拟合。利用阶段一获得的模态极点$a_{jk}$和延迟$\tau_j$，拟合相位A(ω)矩阵各元素，计算拟合误差ε。若ε超过最大相位误差$\varepsilon_{max}$（0.5%），则减小模态容差$\varepsilon_1 = \alpha\varepsilon_1$（$\alpha<1$）并重复阶段一、二直至收敛

3. MT降阶步骤1：计算各模态的留数/极点比$\|c_k\|/|a_k|$，按升序排列，识别非主导极点

4. MT降阶步骤2：设定容差tol，移除低于该容差的留数/极点比对应项（对复极点对使用联合范数条件）

5. MT降阶步骤3：利用剩余模态极点重新拟合相位A(ω)矩阵，计算新的拟合误差ε

6. MT降阶步骤4：若ε小于目标容差$\varepsilon_1$，则迭代执行步骤1-3，采用缩减的容差（$tol = k \times tol, k<1.0$）进一步降阶直至满足精度-效率平衡

7. BT降阶步骤1：将Amodes(ω)有理函数转换为状态空间形式(A,B,C)，求解Lyapunov方程获得可控性Gramian矩阵$W_c$和可观性Gramian矩阵$W_o$

8. BT降阶步骤2：通过块对角变换矩阵S将系统转换为平衡实现，计算Hankel奇异值$\sigma_i$（$W_cW_o$特征值的平方根）

9. BT降阶步骤3：设定容差tol，删除对应小Hankel特征值（$\sigma_1 < tol$）的状态，获得降阶系统$(\tilde{A}, \tilde{B}, \tilde{C})$

10. BT降阶步骤4：计算降阶后$\tilde{A}$矩阵的特征值作为新的极点集，结合原模态延迟重新拟合相位A(ω)矩阵，验证误差界


### 关键参数

- **max_order_per_mode**: 20（每个模态或Yc(ω)函数的最大极点数限制）

- **max_phase_fitting_error**: 0.5%（相位A(ω)矩阵拟合的最大允许误差）

- **soil_resistivity**: 100 Ohm.m（土壤电阻率，频率依赖性被忽略）

- **conductor_resistivity**: 6.99×10⁻⁸ Ohm.m（内导体电阻率）

- **sheath_resistivity**: 5.1667×10⁻⁸ Ohm.m（护套电阻率）

- **armour_resistivity**: 8.223×10⁻⁸ Ohm.m（铠装电阻率）

- **relative_permittivity_layers**: [3.156, 2.3, 2.3]（三层绝缘介质的相对介电常数）

- **cable_length**: 30 km（仿真案例电缆长度）

- **reduction_tolerance_factor**: k < 1.0（MT迭代中的容差缩减系数）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双回路30km三相地下电缆系统（扁平配置） | 系统包含4个模态延迟组，时间延迟分别为0.240345ms、0.296956ms、1.191263ms和1.194583ms，对应原始传递函数阶数分别为18、8、18和18。经MT和BT降阶后，相位A(ω)矩阵的阶数显著降低，同时保持拟合误差低于0.5%的约束条件。BT方法严格保证降阶后系统的渐近稳定性，并提供基于Hankel奇异值的先验误差界。 | 相比传统ULM方法中可能出现的过拟合（部分模态阶数高达18阶），降阶后的模型在保持相同精度（误差<0.5%）的前提下，显著降低了递归卷积算法的计算负担和内存需求，避免了因过拟合导致的无源性违反问题 |



## 量化发现

- ULM方法中单个模态的最大阶数限制为20个极点
- 相位A(ω)函数的最大允许拟合误差为0.5%
- 测试电缆系统包含4个不同的模态延迟组，延迟时间范围从0.240ms到1.195ms
- 原始模态传递函数阶数分别为18、8、18、18，总阶数达62阶
- 电缆内导体半径22mm，护套外径39.95mm，铠装外径44.1mm，电缆总外径49.3mm
- MT方法通过残差/极点比迭代筛选，逐步降低容差直至相位误差满足$\varepsilon < \varepsilon_{max}$
- BT方法通过计算Hankel奇异值，删除$\sigma_1 < \text{tol}$的弱可控且弱可观状态，保证降阶系统特征值实部为负（渐近稳定）
- 降阶后的模型在多回路电缆时域仿真中显著减少计算时间，避免实时仿真中的时间步长越界（time step overshoot）


## 关键公式

### 模态传播函数有理逼近

$$$f_{model_j}(s) = \sum_{k=1}^{N_j} \frac{c_{jk}e^{-s\tau_j}}{s-a_{jk}}$$$

*用于表示第j个模态的频变传播特性，是ULM第一阶段拟合的基础形式*

### 模态截断判别条件

$$$\frac{\| c_k \|}{|a_k|} > \text{tol}$$$

*MT方法中判断极点是否主导的准则，基于留数幅值与极点幅值之比*

### 平衡变换方程

$$$\tilde{A} = S^{-1}AS$$$

*BT方法中将状态空间转换为平衡实现的核心变换，确保可控性和可观性Gramian矩阵相等且对角*



## 验证详情

- **验证方式**: 数值仿真对比分析
- **测试系统**: 30km双回路三相地下电缆系统（扁平配置），包含导体、护套、铠装三层金属结构及三层绝缘介质，土壤电阻率100 Ohm.m
- **仿真工具**: 基于RTDS Technologies的仿真平台（作者所在单位），采用通用线路模型(ULM)框架，结合Vector Fitting进行有理函数逼近
- **验证结果**: 通过对比MT和BT两种降阶方法在处理高阶传播矩阵时的性能，验证了BT在保证系统渐近稳定性和提供先验误差界方面的理论优势。仿真表明，两种方法均能有效降低模型阶数，但MT需要迭代调整容差tol以满足0.5%的相位误差约束，而BT通过Hankel奇异值直接确定降阶阶数。降阶后的模型在保持时域仿真精度的同时，显著提升了多回路电缆系统的计算效率，解决了广域建模中因详细电缆模型导致的仿真速度下降问题。
