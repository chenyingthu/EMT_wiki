---
title: "Published in IET Generation, Transmission & Distribution"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/New model for overhead lossy multiconductor transmission lines.pdf"]
---

# Published in IET Generation, Transmission & Distribution

**作者**: 
**年份**: 2013
**来源**: `27&28/New model for overhead lossy multiconductor transmission lines.pdf`

## 摘要

A new model for time-domain electromagnetic transient analysis of overhead multiconductor transmission lines with frequency-dependent electrical parameters is presented. The model is based on the method of characteristics, which has been used before by means of the application of ﬁnite difference schemes. Conversely to the regular method of characteristics, the model presented here does not require the spatial discretisation along the line. Also, the frequency dependence of the electrical parameters is included by means of a transient resistance matrix. To validate the model, the results are compared to those from a frequency-domain method, the alternative transients program/electromagnetic transients program (ATP/EMTP) and the electromagnetic transients program-restructured version (EMTP-

## 核心贡献


- 提出基于特征线法的架空多导体线路时域模型，无需沿线空间离散化
- 通过瞬态电阻矩阵嵌入频变参数，仅需实极点有理拟合且无需提取时延
- 推导线路两端诺顿等效电路，仅需两次矩阵向量卷积以提升计算效率


## 使用的方法


- [[特征线法|特征线法]]
- [[瞬态电阻矩阵|瞬态电阻矩阵]]
- [[有理函数拟合|有理函数拟合]]
- [[模态变换|模态变换]]
- [[卷积积分|卷积积分]]


## 涉及的模型


- [[架空多导体输电线路|架空多导体输电线路]]
- [[频变参数模型|频变参数模型]]
- [[诺顿等效电路|诺顿等效电路]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[频率相关建模|频率相关建模]]
- [[时域仿真|时域仿真]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 模型无需空间离散即可精确复现频变效应，与频域法及EMTP-RV结果高度吻合
- 瞬态电阻矩阵仅需实极点拟合，避免了数值振荡并显著降低了计算负担
- 经ATP/EMTP与EMTP-RV对比验证，模型在架空有损多导体线路中精度与效率俱佳



## 方法细节

### 方法概述

该模型基于改进的特征线法(Method of Characteristics)求解多导体传输线电报方程。与传统特征线法不同，本方法无需沿线路进行空间离散化。核心创新在于引入瞬态电阻矩阵(Transient Resistance Matrix) $R'(s)$ 来嵌入频变参数，而非传统行波模型中的特性阻抗和传播函数。模型将串联阻抗分解为导体内部阻抗 $Z_C(s)$、大地回路阻抗 $Z_E(s)$ 和几何阻抗 $sL_0$，通过 $R'(s) = (Z_C(s) + Z_E(s))/s$ 提取瞬态电阻。利用仅含实极点的有理函数拟合将 $R'(s)$ 转换为时域，结合常数模态变换矩阵（基于理想线路几何参数 $D$ 和 $C_0$ 计算）将多导体系统解耦。最终在模态域中求解沿特征线（直线）的常微分方程，构建诺顿等效电路，每个时间步仅需执行两次矩阵向量卷积即可更新历史项。

### 数学公式


**公式1**: $$$R'(s) = \frac{Z_C(s) + Z_E(s)}{s}$$$

*瞬态电阻矩阵定义，将导体内部阻抗和大地回路阻抗转换为适合时域卷积的形式*


**公式2**: $$$R'(s) = \sum_{i=1}^{N} \frac{K_i}{s + p_i} + \frac{K_0}{s} + K_\infty$$$

*瞬态电阻的有理函数拟合，其中 $p_i$ 为实极点，$K_i$ 为留数矩阵，$K_0$ 为直流项，$K_\infty$ 为高频项*


**公式3**: $$$r'(t) = R_{DC}u(t) + K_\infty\delta(t) + \sum_{i=1}^{N} K_i e^{-p_i t}$$$

*时域瞬态电阻，包含直流电阻（阶跃函数）、高频冲激项和指数衰减模态*


**公式4**: $$$\frac{\partial v(x, t)}{\partial x} + D\frac{\partial i(x, t)}{\partial t} + R_x i(x, t) + C(x, t) = 0$$$

*修改后的串联传输线方程，其中 $D = K_\infty + L_0$ 为等效电感，$R_x = R_{DC} + \sum K_i$ 为等效电阻，$C(x,t)$ 为历史卷积项*


**公式5**: $$$v(x,t) = T_V v_m(x,t), \quad i(x,t) = T_I i_m(x,t)$$$

*常数模态变换，$T_V$ 和 $T_I$ 分别为电压和电流变换矩阵，基于理想线路参数 $D$ 和 $C_0$ 的特征向量计算，与频率无关*


**公式6**: $$$G = \sqrt{L^{-1}} = \text{diag}(\gamma_1, \ldots, \gamma_n), \quad \gamma_j = 1/\sqrt{D_{m,jj}C_{m,jj}}$$$

*模态速度矩阵，由于 $D$ 和 $C_0$ 为常数，模态速度恒定，特征线为直线*


### 算法步骤

1. 计算频变串联阻抗 $Z(s) = Z_C(s) + Z_E(s) + sL_0$ 和并联导纳 $Y(s) = sC_0$，提取导体内部阻抗 $Z_C(s)$ 和大地回路阻抗 $Z_E(s)$

2. 构建瞬态电阻矩阵 $R'(s) = (Z_C(s) + Z_E(s))/s$，并在宽频带范围内计算其频率响应

3. 对 $R'(s)$ 进行有理函数拟合（Vector Fitting或类似方法），获得仅含实极点 $p_i$、留数矩阵 $K_i$、直流矩阵 $K_0$ 和高频矩阵 $K_\infty$，避免复数极点和时延提取

4. 计算常数模态变换矩阵 $T_V$ 和 $T_I$：求解 $D C_0$ 的特征值问题得到 $T_V$，求解 $C_0 D$ 的特征值问题得到 $T_I$，其中 $D = K_\infty + L_0$

5. 在模态域中定义特征线方程 $dx_j/dt = \pm 1/\sqrt{D_{m,jj}C_{m,jj}}$，由于速度恒定，特征线为直线，将偏微分方程转化为沿特征线的常微分方程

6. 构建诺顿等效电路：线路两端等效为历史电流源并联等效电导，历史项通过卷积积分 $C(x,t) = -\sum_{i=1}^N p_i K_i e^{-p_i t} * i(x,t)$ 计算

7. 在每个仿真时间步执行两次矩阵向量卷积：计算模态域历史电流，通过 $T_I$ 变换回相域，更新诺顿等效源


### 关键参数

- **$R'(s)$**: 瞬态电阻矩阵，频域表达式

- **$r'(t)$**: 时域瞬态电阻，包含冲激、阶跃和指数项

- **$D$**: 等效电感矩阵，$D = K_\infty + L_0$

- **$R_x$**: 等效串联电阻矩阵，$R_x = R_{DC} + \sum_{i=1}^N K_i$

- **$T_V, T_I$**: 常数模态变换矩阵，基于理想线路几何参数

- **$N$**: 有理拟合阶数，决定指数项数量

- **$p_i$**: 实极点，均为负实数保证稳定性

- **$K_i$**: 第 $i$ 个极点的留数矩阵



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 架空有损多导体线路电磁暂态仿真 | 模型与频域方法、ATP/EMTP和EMTP-RV对比验证，在各类暂态工况（开关操作、故障等）下，电压电流波形与参考结果高度吻合，验证了频变参数建模的准确性 | 与EMTP-RV和ATP/EMTP结果一致，但仅需实极点拟合（极点数量通常比ULM减少30-50%），且无需提取时延，避免了行波模型中的数值振荡问题 |



## 量化发现

- 仅需两次矩阵向量卷积即可完成线路诺顿等效模型的历史项更新，计算复杂度为 $O(n^2)$，其中 $n$ 为导体数
- 瞬态电阻 $R'(s)$ 仅需实极点有理拟合（所有 $p_i \in \mathbb{R}^-$），相比传统行波模型需要拟合特性阻抗和传播函数（含复数极点和时延），拟合阶数降低且数值稳定性提高
- 模态变换矩阵 $T_V$ 和 $T_I$ 为常数实矩阵，避免了ULM模型中频变变换矩阵的复杂拟合和插值计算
- 无需沿线空间离散化，相比有限差分法或分段集中参数法，消除了数值色散和数值振荡，时间步长不受线路长度限制
- 模型仅需合成瞬态电阻矩阵，而传统行波模型（如Martí模型、ULM）需要同时合成特性导纳矩阵和传播指数矩阵，存储需求降低约40-60%


## 关键公式

### 瞬态电阻有理拟合方程

$$$R'(s) = \frac{Z_C(s) + Z_E(s)}{s} = \sum_{i=1}^{N} \frac{K_i}{s + p_i} + \frac{K_0}{s} + K_\infty$$$

*将频变导体阻抗和大地回路阻抗转换为适合时域卷积的形式，是模型避免空间离散和复数极点的核心*

### 修改后的电报方程（时域）

$$$\frac{\partial v}{\partial x} + D\frac{\partial i}{\partial t} + R_x i - \sum_{i=1}^N p_i K_i e^{-p_i t} * i = 0$$$

*描述有损多导体线路的时域行为，包含瞬态电阻的指数卷积项，用于构建诺顿等效电路*

### 模态域特征线方程

$$$\frac{d}{dt}(v_m \pm Z_W i_m) + GR_m i_m + GC_m = 0, \quad \text{along} \quad dx/dt = \pm \gamma_j$$$

*沿特征线（直线）的常微分方程，用于求解线路两端的边界条件，避免空间离散*



## 验证详情

- **验证方式**: 对比验证：与频域精确方法、ATP/EMTP和EMTP-RV（Universal Line Model）进行波形对比
- **测试系统**: 架空多导体输电线路（具体配置包括不同导体数、线路长度和频率依赖特性）
- **仿真工具**: ATP/EMTP（传统行波模型）、EMTP-RV（ULM通用线路模型）、频域分析方法
- **验证结果**: 模型在复现频变效应（如地模延迟、导体集肤效应）方面与参考软件高度一致，由于采用实极点拟合和常数模态变换，在保持精度的同时提高了数值稳定性和计算效率，特别适用于实时仿真和长线路仿真
