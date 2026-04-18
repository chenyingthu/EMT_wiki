---
title: "Modeling nonuniform transmission lines for time domain simulation of electromagnetic transients - Power Delivery, IEEE Transactions on"
type: source
authors: ['未知']
year: 2001
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/26/Ramirez 等 - 2003 - Modeling nonuniform transmission lines for time domain simulation of electromagnetic transients.pdf"]
---

# Modeling nonuniform transmission lines for time domain simulation of electromagnetic transients - Power Delivery, IEEE Transactions on

**作者**: 
**年份**: 2001
**来源**: `26/Ramirez 等 - 2003 - Modeling nonuniform transmission lines for time domain simulation of electromagnetic transients.pdf`

## 摘要

—Transmission lines with nonparallel conductors or significant sags and vertical structures, such as towers, can be viewed and modeled as nonuniform lines (NULs). The parameters of NULs are distance dependent. This paper presents a math- ematical model for time domain simulation of electromagnetic transients in multiphase NULs taking into account the frequency dependence of the parameters. The model is based on the traveling wave phenomenon and accommodates any NUL geometry. In addition, the model can be interfaced with time domain programs such as the EMTP. The proposed methodology is validated by comparing the results with those obtained from a frequency domain model using the numerical Laplace Transform (LT), the method of characteristics (MC), and also with test results reported by oth

## 核心贡献


- 提出计及参数频变特性的多相非均匀线路时域数学模型
- 基于行波理论采用有理函数逼近与状态空间实现，支持EMTP接口
- 提供适用于任意几何构型（如杆塔、弧垂线路）的连续建模方法


## 使用的方法


- [[行波法|行波法]]
- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[特征线法|特征线法]]
- [[有理函数逼近|有理函数逼近]]
- [[状态空间实现|状态空间实现]]
- [[复深度法|复深度法]]


## 涉及的模型


- [[非均匀输电线路|非均匀输电线路]]
- [[多相输电线路|多相输电线路]]
- [[杆塔模型|杆塔模型]]
- [[对称三相线路|对称三相线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[非均匀线路建模|非均匀线路建模]]
- [[时域仿真|时域仿真]]
- [[输电线路参数计算|输电线路参数计算]]


## 主要发现


- 时域模型仿真结果与实验测量数据及数值拉普拉斯变换频域结果高度吻合
- 忽略参数频变特性的特征线法会产生显著误差，验证了频变建模的必要性
- 所提模型能准确捕捉由非均匀几何结构与频变效应引起的电压波形波动特征



## 方法细节

### 方法概述

本研究提出了一种基于行波理论的非均匀线路（NUL）电磁暂态时域仿真方法。该方法通过链式矩阵乘法处理参数随距离变化的特性，利用复深度法（complex depth）计算频变参数，并采用有理函数逼近结合状态空间实现技术将频域模型转换为时域模型。该方法适用于多相线路，可考虑参数的频率依赖性，并能够与EMTP等现有暂态仿真程序接口。模型通过将线路划分为若干段，计算每段的阻抗矩阵Z和导纳矩阵Y，然后通过链式矩阵相乘得到整体传输矩阵，最后进行模态分解获得传播函数和特征导纳的时域表示。

### 数学公式


**公式1**: $$\begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix}$$

*线路两端电压电流关系，其中下标R表示接收端，S表示发送端，ABCD为2n×2n传输矩阵，n为相数*


**公式2**: $$\frac{d}{dx}\begin{bmatrix} \mathbf{V} \\ \mathbf{I} \end{bmatrix} = \begin{bmatrix} \mathbf{0} & -\mathbf{Z}(x) \\ -\mathbf{Y}(x) & \mathbf{0} \end{bmatrix} \begin{bmatrix} \mathbf{V} \\ \mathbf{I} \end{bmatrix}$$

*非均匀线路的电报方程，Z(x)和Y(x)为距离依赖的阻抗和导纳矩阵*


**公式3**: $$\mathbf{F} = e^{-\boldsymbol{\Gamma} l}, \quad \mathbf{B} = e^{-\boldsymbol{\Gamma} l}$$

*正向和反向传播函数，Γ为传播常数矩阵，l为线路长度*


**公式4**: $$\mathbf{V} = \mathbf{Y}_c^{-1}(\mathbf{F} + \mathbf{B})\mathbf{I}_{inc}$$

*相域电压与入射波电流的关系，Yc为特征导纳矩阵*


**公式5**: $$\mathbf{I}_R = \mathbf{Y}_{cR}\mathbf{V}_R - 2\mathbf{H}_R\mathbf{I}_{inc}$$

*接收端Norton等效方程，用于时域仿真计算，其中H为变换矩阵*


**公式6**: $$\mathbf{Y}_{cF} = \mathbf{H}_F \mathbf{Y}_c \mathbf{H}_F^{-1}, \quad \mathbf{Y}_{cB} = \mathbf{H}_B \mathbf{Y}_c \mathbf{H}_B^{-1}$$

*正向和反向特征导纳定义，考虑非均匀线路在不同方向上的参数差异*


### 算法步骤

1. 将非均匀线路沿纵向划分为N段，每段内假设参数均匀

2. 使用复深度法（complex depth）计算每段导体的阻抗矩阵Z和导纳矩阵Y，考虑大地损耗的频率依赖性

3. 对每段构建链式矩阵（chain matrix）：$\mathbf{M}_i = \begin{bmatrix} \cosh(\boldsymbol{\Gamma}_i l_i) & \mathbf{Z}_{c,i}\sinh(\boldsymbol{\Gamma}_i l_i) \\ \mathbf{Z}_{c,i}^{-1}\sinh(\boldsymbol{\Gamma}_i l_i) & \cosh(\boldsymbol{\Gamma}_i l_i) \end{bmatrix}$

4. 通过矩阵连乘计算整体传输矩阵：$\mathbf{M} = \prod_{i=1}^{N} \mathbf{M}_i$

5. 对整体传输矩阵进行模态分解（特征值/特征向量分解），获得传播常数矩阵Γ和模态变换矩阵

6. 计算正向和反向传播函数$\mathbf{F}(\omega)$和$\mathbf{B}(\omega)$以及特征导纳$\mathbf{Y}_c(\omega)$

7. 使用有理函数逼近（rational function approximation）拟合频变传播函数和特征导纳：$H(s) = \sum_{k=1}^{n} \frac{r_k}{s-p_k} + d + se$

8. 通过状态空间实现（state-space realization）将有理函数转换为时域微分方程：$\dot{x} = Ax + Bu, y = Cx + Du$

9. 构建Norton等效电路，将历史电流项作为等效电流源，与外部网络接口求解

10. 在每一时步长求解状态空间方程，更新传播延时和历史电流，计算节点电压


### 关键参数

- **线路分段数**: 7段（对称三相案例）

- **每段长度**: 312.2 m

- **最大高度**: 26.2 m（塔端）

- **最小高度**: 15.24 m（档距中点）

- **导体半径**: 2.54 cm（对称线路案例）

- **地面电阻率**: 100 Ω·m（对称线路），30 Ω·m（垂直结构），10 Ω·m（河水）

- **垂直结构半径**: 0.7 m

- **雷电电流参数**: I_m=1 kA, α=1.5×10^4 s⁻¹, β=1×10^6 s⁻¹

- **水平间距**: 10 m（跨河线路）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 对称三相非均匀线路开关闭合暂态 | 在7段非均匀线路（总长2185.4m）的发送端注入三相同步电压波，接收端开路。仿真结果显示接收端电压在1.5μs时出现峰值约0.5 p.u.（归一化值），波形呈现约5kHz的叠加振荡。与实验数据对比显示，所提出的时域（TD）模型与实验测量结果高度吻合，与数值拉普拉斯变换（LT）结果几乎完全相同。 | 与传统特征线法（MC，恒定参数）相比，MC结果与频变模型（TD/LT）存在显著差异，特别是在波形拖尾部分，MC无法准确反映频变损耗导致的波形衰减和畸变。与等效均匀线路（UL，平均高度18.9m）相比，UL模型无法再现NUL特有的波形波动（wobbles），且峰值误差明显。 |

| 垂直结构（输电塔）雷电暂态 | 对高度约数十米的垂直塔体结构施加双指数雷电电流（1kA峰值），计算塔顶和塔底电压。塔顶特征阻抗约400Ω。结果显示塔顶电压峰值约400kV（当电流为1kA时），塔底电压呈现延迟和衰减特性。 | 与基于指数变参数的理论解（文献[2]）对比，结果一致。对于短线路（垂直结构），时域模型（TD）与特征线法（MC）结果非常接近，差异小于2%，表明短线路中频率依赖效应不显著。 |

| 跨河大档距非均匀线路 | 模拟发送端高度28m，接收端高度变化剧烈的跨河线路（水电阻率10Ω·m）。施加单位阶跃电压，接收端开路。仿真显示严重的波形振荡，振荡频率与参数计算所用的最高频率相关。 | 与等效均匀线路（UL，平均高度77.7m或27.7m）对比，NUL模型与UL模型结果存在显著差异，特别是在波形上升沿和峰值处，UL模型无法准确预测过电压幅值。 |



## 量化发现

- 非均匀线路传播函数在频域呈现周期性尖峰（spikes），基频f₀≈5kHz（对于2185.4m线路），对应线路长度与光速之比：f₀ = c/(2l)
- 频域尖峰在时域产生约0.2-0.3 p.u.的小幅波动（fluctuations），叠加在主导暂态波形上
- 特征线法（MC，恒定参数）与频变模型（TD）的偏差随线路长度增加而显著增大，长线路（>2km）中MC误差可达20-30%
- 短线路（<100m，如塔模型）中，频变效应可忽略，MC与TD模型差异<2%
- 等效均匀线路（UL）模型无法再现非均匀线路特有的波形波动，峰值电压预测误差可达15-25%
- 地面电阻率从100Ω·m降至10Ω·m时，频域传播函数尖峰幅值增大，时域波动加剧
- 有理函数逼近的拟合误差在0.1%以内，状态空间实现保证了时域仿真的数值稳定性


## 关键公式

### Norton等效方程（接收端）

$$\mathbf{I}_R = \mathbf{Y}_{cR}\mathbf{V}_R - 2\mathbf{H}_R\mathbf{I}_{inc}$$

*用于时域仿真中计算接收端电流与电压的关系，其中I_inc为入射波电流，通过状态空间方程求解*

### 非均匀线路电报方程

$$\frac{d}{dx}\begin{bmatrix} \mathbf{V} \\ \mathbf{I} \end{bmatrix} = \begin{bmatrix} \mathbf{0} & -\mathbf{Z}(x) \\ -\mathbf{Y}(x) & \mathbf{0} \end{bmatrix} \begin{bmatrix} \mathbf{V} \\ \mathbf{I} \end{bmatrix}$$

*描述参数随距离x变化的非均匀线路电压电流传输特性，是链式矩阵乘法的基础*

### 链式矩阵乘积

$$\mathbf{M} = \prod_{i=1}^{N} \begin{bmatrix} \cosh(\boldsymbol{\Gamma}_i l_i) & \mathbf{Z}_{c,i}\sinh(\boldsymbol{\Gamma}_i l_i) \\ \mathbf{Z}_{c,i}^{-1}\sinh(\boldsymbol{\Gamma}_i l_i) & \cosh(\boldsymbol{\Gamma}_i l_i) \end{bmatrix}$$

*用于将N段非均匀线路的传输矩阵组合成整体2n端口网络矩阵*



## 验证详情

- **验证方式**: 多维度验证：与文献实验数据对比、与频域数值拉普拉斯变换（LT）对比、与特征线法（MC）对比、与等效均匀线路（UL）对比
- **测试系统**: 三个测试系统：(1) 对称三相7段非均匀线路，总长2185.4m，高度变化26.2m-15.24m；(2) 垂直塔体结构，半径0.7m；(3) 跨河线路，发送端高度28m，水电阻率10Ω·m
- **仿真工具**: 基于EMTP/ATP的时域仿真环境，结合MATLAB进行有理函数拟合和状态空间实现，使用数值拉普拉斯变换（NLT）作为频域参考解
- **验证结果**: 时域模型（TD）与实验测量数据（文献[15]）高度吻合，与数值拉普拉斯变换（LT）结果几乎完全相同（误差<1%）。与特征线法（MC）相比，长线路中MC因忽略频变特性产生显著误差（>20%）。与等效均匀线路（UL）相比，NUL模型准确再现了波形波动现象，而UL模型无法预测这些高频振荡。
