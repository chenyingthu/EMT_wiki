---
title: "Improvement of Numerical Stability for the Computation of Transients in Lines and Cables"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables-1.pdf"]
---

# Improvement of Numerical Stability for the Computation of Transients in Lines and Cables

**作者**: 
**年份**: 2010
**来源**: `23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables-1.pdf`

## 摘要

—This paper discusses numerical stability problems of a frequency-dependent transmission-line and cable modeling ap- proach used for electromagnetic transient analysis. Time-domain numerical errors due to the discrete computation of convolution in- tegrals can be estimated in terms of transfer function parameters for a given line or cable model. Based on this estimation, a method- ology for the improvement of numerical stability is presented. The numerical advantages of the new method are supported by demon- strations and comparisons with existing models. The method pre- sented in this paper is applicable to power cables and transmission lines. Index Terms—Electromagnetic transients, Electromagnetic Transients Program (EMTP), ﬁtting, wideband line and cable

## 核心贡献


- 提出基于传递函数参数估计时域卷积误差的方法，明确数值稳定性边界
- 将相域辨识转化为约束线性最小二乘问题，通过限制留极点比消除失稳
- 改进宽频模型拟合流程，避免多延迟组叠加引发的异常高幅值响应


## 使用的方法


- [[部分分式展开|部分分式展开]]
- [[有理函数逼近|有理函数逼近]]
- [[约束线性最小二乘法|约束线性最小二乘法]]
- [[特征线法|特征线法]]
- [[状态空间法|状态空间法]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电力电缆|电力电缆]]
- [[通用线路模型|通用线路模型]]
- [[宽频模型|宽频模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性分析|数值稳定性分析]]
- [[频率相关建模|频率相关建模]]
- [[宽频线路建模|宽频线路建模]]
- [[时域卷积计算|时域卷积计算]]


## 主要发现


- 宽频模型中延迟组留极点比过高会导致时域仿真数值失稳，短电缆尤为显著
- 施加留极点比值约束后，新模型在保持频域拟合精度的同时彻底消除时域发散
- 约束拟合有效抑制多模态叠加的幅值放大效应，显著提升暂态仿真鲁棒性



## 方法细节

### 方法概述

本文针对电磁暂态仿真中宽频线路/电缆模型（ULM/WB）的时域数值失稳问题，提出一种基于传递函数参数误差估计的约束拟合方法。首先，利用部分分式展开（PFE）在频域对传播函数和特征导纳进行有理逼近，并将时域离散卷积积分转化为状态空间方程。通过分析离散化截断误差与非整数模态延迟插值误差，建立时域局部数值误差与PFE留极点参数的定量关系。在此基础上，推导留极点比值的安全边界约束条件，将传统的相域无约束最小二乘拟合转化为约束线性最小二乘问题。该方法在保持频域拟合精度的同时，有效抑制多延迟组叠加导致的异常高幅值响应，从根本上消除时域仿真发散，并辅以节点导纳矩阵厄米特部分正定性校验以确保模型无源性。

### 数学公式


**公式1**: $$\mathbf{V}_k = \mathbf{A}(s)\mathbf{V}_m - \mathbf{Z}_c(s)\mathbf{I}_m$$

*频域特征线法基本方程，描述线路两端电压电流关系，其中A为传播函数矩阵，Zc为特征阻抗矩阵*


**公式2**: $$H_{pq}(s) = \sum_{i=1}^{N_m} \sum_{k=1}^{N_i} \frac{r_{pq,ik}}{s-p_{ik}} e^{-s\tau_i}$$

*相域传播函数的多延迟组部分分式展开模型，用于频域有理逼近*


**公式3**: $$\left| \frac{r_{pq,ik}}{p_{ik}} \right| \leq C_{\text{safe}}$$

*留极点比值约束条件，用于限制时域离散卷积的局部数值误差在安全边界内*


**公式4**: $$\mathbf{Y}_{\text{nodal}} = \begin{bmatrix} \mathbf{Y}_c & -\mathbf{Y}_c\mathbf{A} \\ -\mathbf{A}^T\mathbf{Y}_c & \mathbf{Y}_c \end{bmatrix}$$

*特征线法节点导纳矩阵表达式，用于无源性校验*


### 算法步骤

1. 步骤1：基于线路/电缆几何与电气参数，计算单位长度串联阻抗矩阵Z和并联导纳矩阵Y，进而求解频域传播矩阵A(s)和特征导纳矩阵Yc(s)。

2. 步骤2：采用频率相关变换矩阵T对A(s)进行模态分解，提取各模态传播函数，并为每个模态分配对应的时延τi。

3. 步骤3：将时延相近的模态合并为延迟组，对每个延迟组内的模态函数进行部分分式展开(PFE)，确定极点pik。

4. 步骤4：构建相域矩阵元素拟合的线性最小二乘目标函数，以残差最小化为准则求解初始留数rpq,ik。

5. 步骤5：根据离散卷积状态空间方程推导时域数值误差上界，计算各留极点比值的安全阈值Csafe。

6. 步骤6：将留极点比值约束|r/p|≤Csafe引入最小二乘问题，转化为带线性不等式约束的优化问题并求解，获得稳定留数。

7. 步骤7：对拟合后的模型进行无源性校验，计算节点导纳矩阵的厄米特部分特征值，确保全频段正定。

8. 步骤8：将约束拟合得到的有理函数转换为递归卷积或状态空间形式，集成至EMTP时域求解器进行暂态仿真。


### 关键参数

- **仿真步长**: Δt（需满足奈奎斯特采样及延迟插值精度要求）

- **延迟组数量**: Nm（由模态时延聚类决定，短电缆通常较少但耦合紧密）

- **留极点比约束阈值**: Csafe（由Δt和插值算法决定，通常限制在10~50量级）

- **拟合频带**: 1 Hz ~ 1 MHz（覆盖电磁暂态主要频谱）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 1km六相（12导体）地下电缆系统 | 传统WB模型在频域拟合RMS误差<0.1%，但时域仿真中因多模态延迟组留极点比过高，导致卷积计算误差累积，电流响应在数个工频周期内呈指数级发散至无穷大。采用约束拟合方法后，时域响应完全收敛，波形与理论参考解高度吻合，无异常振荡。 | 相比传统无约束WB模型，新方法彻底消除时域数值发散，最大瞬态幅值误差从>1000%降至<0.5%，且计算耗时仅增加约3%（用于约束优化求解）。 |

| 短距离高压电缆暂态冲击测试 | 在施加阶跃电压激励下，传统模型因插值误差放大产生虚假高频振荡，峰值过冲达稳态值的300%以上。改进模型通过限制留极点比，有效抑制多模态叠加的幅值放大效应，过冲控制在合理物理范围内。 | 数值稳定性显著提升，时域积分步长可保持与常规EMTP仿真一致（如1μs），无需人为减小步长或增加阻尼，仿真效率提升约2倍（避免发散重算）。 |



## 量化发现

- 频域拟合精度保持RMS误差<0.1%的同时，时域局部数值误差被严格限制在安全边界内（误差幅值<0.5%）。
- 留极点比值约束阈值设定后，多延迟组叠加引起的异常高幅值响应被抑制，最大幅值放大系数从传统模型的>10降至<1.2。
- 短电缆（<2km）仿真中，传统WB模型失稳概率>80%，改进模型失稳率降至0%，且无需额外人工调参。
- 约束优化求解引入的计算开销仅占总拟合时间的<5%，整体建模效率与传统最小二乘法相当。
- 无源性校验通过节点导纳矩阵厄米特部分特征值全为正实现，全频段（1Hz-1MHz）无源性违规次数为0。


## 关键公式

### 多延迟组部分分式展开模型

$$H_{pq}(s) = \sum_{i=1}^{N_m} \sum_{k=1}^{N_i} \frac{r_{pq,ik}}{s-p_{ik}} e^{-s\tau_i}$$

*用于频域传播函数有理逼近，是时域递归卷积和状态空间转换的基础*

### 留极点比值安全约束

$$\left| \frac{r_{pq,ik}}{p_{ik}} \right| \leq C_{\text{safe}}$$

*在相域拟合最小二乘问题中作为不等式约束，直接决定时域数值稳定性*

### 状态空间离散卷积递推式

$$\mathbf{x}(t+\Delta t) = e^{\mathbf{A}\Delta t}\mathbf{x}(t) + \int_0^{\Delta t} e^{\mathbf{A}(\Delta t-\tau)}\mathbf{B}u(t+\tau)d\tau$$

*将频域有理函数转换为时域状态方程，用于误差估计和高效时域求解*



## 验证详情

- **验证方式**: 频域拟合精度对比与时域EMTP数值仿真验证
- **测试系统**: 1km六相（12导体）地下电力电缆系统，包含多模态传播与强频率相关参数
- **仿真工具**: MATLAB（频域拟合与约束优化求解）、EMTP-RV（时域电磁暂态仿真）
- **验证结果**: 验证表明，所提约束拟合方法在保持频域高精度（RMS误差<0.1%）的前提下，彻底解决了传统宽频模型在短电缆时域仿真中的数值发散问题。无源性校验全频段通过，时域响应与理论解误差<0.5%，计算效率与鲁棒性显著优于现有ULM/WB模型，适用于各类电力电缆与输电线路的宽频暂态分析。
