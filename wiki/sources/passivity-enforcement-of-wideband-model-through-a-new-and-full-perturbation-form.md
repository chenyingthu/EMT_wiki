---
title: "Passivity enforcement of wideband model through a new and full perturbation formulation"
type: source
authors: ['Juan', 'Miguel', 'David', 'Becerra']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109668. doi:10.1016/j.epsr.2023.109668"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/David Becerra 等 - 2023 - Passivity enforcement of wideband model through a new and full perturbation formulation.pdf"]
---

# Passivity enforcement of wideband model through a new and full perturbation formulation

**作者**: Juan, Miguel, David 等
**年份**: 2023
**来源**: `31/David Becerra 等 - 2023 - Passivity enforcement of wideband model through a new and full perturbation formulation.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Passivity enforcement of wideband model through a new and full Juan Miguel David Becerra a, Ilhan Kocar b,*, Jean Mahseredjian a b Department of Electrical Engineering, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong Passive component models are necessary to ensure numerical stability in the simulation of electromagnetic

## 核心贡献


- 提出同时扰动特征导纳与传播函数留数的新型无源性强制方法。
- 首次推导全相域下基于传播函数留数的无源性强制完整方程组。
- 构建最小化扰动优化模型，在保持拟合精度下优于现有简化方法。


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[留数扰动法|留数扰动法]]
- [[全相域建模|全相域建模]]
- [[约束优化|约束优化]]
- [[特征值分析|特征值分析]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[频率相关电缆模型-fdcm|频率相关电缆模型(FDCM)]]
- [[节点导纳矩阵|节点导纳矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[无源性强制|无源性强制]]
- [[频率相关建模|频率相关建模]]
- [[宽频线路建模|宽频线路建模]]
- [[数值稳定性|数值稳定性]]


## 主要发现


- 新方法收敛速度更快，所需参数扰动量显著小于现有简化算法。
- 在强制无源性的同时有效保持模型原始拟合精度与频响特性。
- 算例验证表明全相域联合扰动策略优于单一函数或对角线扰动。



## 方法细节

### 方法概述

提出了一种基于全相域（full phase domain）的混合扰动无源性强制方法。该方法通过同时扰动特征导纳（characteristic admittance, $Y_C$）和传播函数（propagation function, $H_I$）的留数矩阵（residue matrices），构建约束优化问题以最小化整体扰动。与传统方法仅扰动$Y_C$或$H_I$的对角元素不同，本方法首次建立了传播函数在全相域下留数扰动的完整方程组，通过线性化特征值约束处理非线性依赖关系，在保证模型无源性的同时最大程度保持拟合精度。

### 数学公式


**公式1**: $$$\lambda_i \geq 0, \forall \lambda_i \in \lambda(\Theta(s)); \quad s = j\omega$$$

*无源性基本条件：Hermitian矩阵$\Theta(s)$的所有特征值必须非负*


**公式2**: $$$\Theta(s) = Y_n(s) + Y_n^H(s)$$$

*Hermitian矩阵构造，其中$Y_n^H(s)$为节点导纳矩阵的共轭转置*


**公式3**: $$$Y_n = \begin{bmatrix} (I-H_I^2)^{-1}(I+H_I^2)Y_C & -2(I-H_I^2)^{-1}H_I Y_C \\ -2(I-H_I^2)^{-1}H_I Y_C & (I-H_I^2)^{-1}(I+H_I^2)Y_C \end{bmatrix}$$$

*宽频线路/电缆模型的节点导纳矩阵，由特征导纳$Y_C$和传播函数$H_I$构成*


**公式4**: $$$Y_C(s) = \sum_{i=1}^{n} \frac{R_i}{s-p_i} + D$$$

*特征导纳的有理函数拟合形式，$R_i$为留数矩阵，$p_i$为极点，$D$为常数矩阵*


**公式5**: $$$H_I(s) = \sum_{g=1}^{G} e^{-s\tau_g} \sum_{i=1}^{n_g} \frac{\hat{R}_{i,g}}{s-\hat{p}_{i,g}}$$$

*传播函数的多延时有理拟合，$G$为模态组数，$\tau_g$为第$g$组时延，$\hat{R}_{i,g}$为相应留数*


**公式6**: $$$\min_{\Delta \tilde{r}_R} \left\| \begin{bmatrix} T(s_1) \\ \vdots \\ T(s_m) \end{bmatrix} \Delta \tilde{r}_R \right\|_2 \quad \text{s.t.} \quad P(s_m)\Delta \tilde{r}_R + \alpha \lambda(\Theta(s_m)) \geq 0$$$

*核心优化问题：最小化留数相对扰动$\Delta \tilde{r}_R$，约束为线性化后的特征值非负条件，$\alpha$为略大于1的常数*


### 算法步骤

1. 计算$\Theta(s)$的特征值，在对数坐标频率范围内进行密集采样（每decade至少100个采样点），覆盖拟合频率范围

2. 基于特征值计算结果识别模型的无源和非无源频段数量$n_b$，确定频率样本分布策略

3. 对每个频段进行对数采样，计算每个频段的样本数$m_b = \lfloor m_d/n_b \rfloor$（当$m_d/n_b > 1$时），确保总样本数接近$m_d$

4. 对每个非无源频段，额外添加一个特征值最小（违反最严重）的频率采样点，形成最终频率样本集$s_1, \dots, s_m$

5. 构建目标函数矩阵$T(s_m)$和约束矩阵$P(s_m)$，其中$P(s_m)$表示特征值函数一阶微分与留数相对扰动的关系

6. 求解约束最小二乘问题（公式6和8），更新$Y_C$和$H_I$的留数矩阵

7. 检查更新后模型的无源性，若仍存在非无源频段且未达到最大迭代次数（21次），则返回步骤1继续迭代


### 关键参数

- **frequency_sampling**: 每decade至少100个采样点（对数坐标）

- **alpha**: 略大于1的常数，用于约束条件中的松弛因子

- **max_iterations**: 21次（判定为失败的阈值）

- **md**: 期望的频率样本总数

- **mb**: 每个频段的样本数，由floor(md/nb)计算

- **perturbation_type**: 相对扰动（relative perturbations），定义为元素偏差除以元素原始值

- **convergence_criterion**: 模型在所有采样频率处满足$\lambda_i \geq 0$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 混合扰动方法（C-All）收敛性能测试 | 在大多数测试案例中，同时扰动$Y_C$和$H_I$的方法（C-All）在少于5次迭代内即可收敛到无源模型，远低于设定的21次迭代上限 | 相比传统单一函数扰动方法，收敛速度显著提升，且所需参数扰动量更小 |

| 模型精度保持验证（FSV方法） | 使用Feature Selective Validation (FSV)方法评估，频率范围DC至100 MHz（每decade 100个样本），通过Global Difference Measure (GDM)指标量化$Y_C$和$H_I$在强制无源性前后的偏差 | 提出的全相域联合扰动策略在保持拟合精度方面优于仅扰动对角线元素的简化方法 |



## 量化发现

- 最大迭代次数阈值设定为21次，超过则判定为强制失败
- C-All（同时扰动特征导纳和传播函数）在大多数情况下收敛于少于5次迭代
- 频率采样密度：每decade至少100个对数分布采样点用于初始特征值分析
- FSV验证频率范围：DC至100 MHz，采样密度100点/decade
- 约束条件中的常数$\alpha$略大于1，用于确保特征值严格非负
- 相比现有简化方法（仅扰动$Y_C$或$H_I$对角元素），新方法在相同精度要求下所需留数扰动量显著降低


## 关键公式

### 混合扰动优化问题

$$$\min_{\Delta \tilde{r}_R} \left\| \begin{bmatrix} T(s_1) \\ \vdots \\ T(s_m) \end{bmatrix} \Delta \tilde{r}_R \right\|_2 \quad \text{s.t.} \quad P(s_m)\Delta \tilde{r}_R + \alpha \lambda(\Theta(s_m)) \geq 0$$$

*当宽频模型不满足无源性条件时，通过同时调整$Y_C$和$H_I$的留数，最小化相对扰动向量$\Delta \tilde{r}_R$的范数，同时保证Hermitian矩阵特征值非负*

### 节点导纳矩阵

$$$Y_n = \begin{bmatrix} (I-H_I^2)^{-1}(I+H_I^2)Y_C & -2(I-H_I^2)^{-1}H_I Y_C \\ -2(I-H_I^2)^{-1}H_I Y_C & (I-H_I^2)^{-1}(I+H_I^2)Y_C \end{bmatrix}$$$

*基于传播函数$H_I$和特征导纳$Y_C$构建线路/电缆的节点导纳矩阵，用于无源性验证和EMT仿真*

### 传播函数多延时有理拟合

$$$H_I(s) = \sum_{g=1}^{G} e^{-s\tau_g} \sum_{i=1}^{n_g} \frac{\hat{R}_{i,g}}{s-\hat{p}_{i,g}}$$$

*宽频模型中传播函数的有理函数近似，包含$G$个模态组的时延$\tau_g$和相应留数$\hat{R}_{i,g}$，是本文扰动策略的核心对象*



## 验证详情

- **验证方式**: 数值仿真验证与对比分析
- **测试系统**: 多导体输电线路和电缆系统的宽频模型（基于ULM和FDCM模型架构）
- **仿真工具**: MATLAB（用于算法实现和矢量拟合），特征值分析工具，FSV（Feature Selective Validation）方法用于精度评估
- **验证结果**: 提出的全相域混合扰动方法在21次迭代限制内对所有测试案例成功强制无源性，其中大多数案例在少于5次迭代内收敛；通过FSV方法验证，该方法在DC至100 MHz范围内有效保持了原始模型的频响特性，相比仅扰动$Y_C$或$H_I$对角元素的方法，具有更小的GDM偏差指标和更快的收敛速度
