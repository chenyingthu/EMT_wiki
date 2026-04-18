---
title: "A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EMT-Type Programs"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;6;10.1109/TPWRD.2022.3157163"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/02/Pereira和Tavares - 2022 - A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EM.pdf"]
---

# A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EMT-Type Programs

**作者**: 
**年份**: 2022
**来源**: `02/Pereira和Tavares - 2022 - A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EM.pdf`

## 摘要

—This paper presents an accurate and efﬁcient model to represent the corona effect and frequency dependence of line parameters in electromagnetic transient simulations. The new method, named the voltage and frequency dependent line model (VFDLM), can be seen as a more general case of the well-known frequency-dependent (FD) or wideband (WB) line models, wherein the characteristic admittance and propagation function are con- sidered voltage- and frequency-dependent parameters. The time domain traveling wave equations are solved using recursive con- volutions and rational approximation through vector ﬁtting (VF). Since the model can be represented by Norton equivalents, it is to- tally compatible with EMT-type programs. The model is validated through comparisons with three ﬁeld measurement da

## 核心贡献


- 提出电压频率相关线路模型，将电晕效应与频变特性直接耦合于分布式参数中
- 将特征导纳与传播函数扩展为电压频率双重依赖参数，突破传统线性模型限制
- 基于诺顿等效与递归卷积构建算法，实现与现有EMT仿真程序的无缝兼容


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[递归卷积|递归卷积]]
- [[有理函数逼近|有理函数逼近]]
- [[诺顿等效|诺顿等效]]
- [[行波方程求解|行波方程求解]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变线路模型|频变线路模型]]
- [[宽带线路模型|宽带线路模型]]
- [[电晕模型|电晕模型]]


## 相关主题


- [[电晕效应|电晕效应]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[雷电过电压|雷电过电压]]


## 主要发现


- 与三组现场实测数据对比验证，模型在暂态过电压波形拟合上高度吻合
- 仿真验证表明该模型兼具数值稳定性、计算高效性与参数表征准确性
- 成功在EMT平台实现电晕非线性与线路频变特性的全分布式统一建模



## 方法细节

### 方法概述

提出电压与频率相关线路模型（VFDLM），将电晕效应与频变特性直接耦合于分布式参数中。该模型基于传输线行波理论，将特征导纳与传播函数扩展为电压与复频率的双重依赖函数。通过空间离散化将线路划分为短区段，利用矢量拟合对频域响应进行有理函数逼近，并结合递归卷积在时域求解。模型最终转化为诺顿等效形式，通过预计算不同电压采样点的时域实现参数，在仿真循环中根据实时电压动态更新等效导纳与历史电流源，实现与EMT程序的无缝兼容，彻底避免了传统集中参数电晕支路带来的物理不一致性问题。

### 数学公式


**公式1**: $$$Y(s, v) = G(v) + sC(v)$$$

*电压依赖的并联导纳表达式，其中电容C和电导G随导体电压v非线性变化*


**公式2**: $$$Y_c(s, v) = Z^{-1}(s) \sqrt{Z(s) Y(s, v)}$$$

*电压与频率相关的特征导纳定义式*


**公式3**: $$$H(s, v) = e^{-\sqrt{Y(s, v) Z(s)} l}$$$

*电压与频率相关的传播函数定义式，体现电晕对波速和衰减的影响*


**公式4**: $$$Y_c \approx d + \sum_{i=1}^{N_p^{Y_c}} \frac{r_i^{Y_c}}{s - p_i^{Y_c}}$$$

*特征导纳的有理函数逼近形式，用于递归卷积计算*


**公式5**: $$$[Y_{sh}(v(t-\Delta t))] \cdot [v(t)] = [i(t)] - [i_{hist}(v(t-\Delta t))]$$$

*基于上一时刻电压线性化的节点导纳方程，用于避免迭代求解*


### 算法步骤

1. 离线预计算阶段：在电晕起始电压$v_{crit}$至最大预期过电压$v_{max}$范围内线性选取$n$个电压采样点。对每个采样点计算对应的$Y_c(s,v_j)$和$H(s,v_j)$，利用矢量拟合技术提取极点、留数及时间延迟$\tau(v_j)$，生成时域实现参数集(TDIP)并存储至内存。

2. 缓冲区初始化：根据最大电压对应的时间延迟$\tau(v_{max})$计算历史电流缓冲区大小$BS = \tau(v_{max})/\Delta t + 1$，确保存储足够的历史样本。

3. 仿真循环电压检测：在每个时间步$t$，读取导体瞬时电压$v(t)$。若$v(t) > v_{crit}$，在内存中搜索最接近的预计算电压采样点$v_j$，并加载对应的TDIP参数。

4. 参数更新与插值处理：若当前时间延迟非时间步长的整数倍，采用线性插值计算历史项位置；根据加载的TDIP动态更新诺顿等效的非线性并联电导$G_s(v)$和电压相关历史电流源$i_{hist}(v)$。

5. 节点方程求解：采用上一时刻电压$v(t-\Delta t)$对应的导纳矩阵和历史电流源构建线性方程组，直接求解当前时刻节点电压$v(t)$，在保证精度的同时避免非线性迭代带来的计算负担。


### 关键参数

- **时间步长 $\Delta t$**: 10 ns

- **空间离散段长**: 50 m (EDF线) / 100 m (Tidd/Shiobara线)

- **电压采样点数 $n$**: 100

- **最大拟合阶数**: 8

- **拟合误差阈值**: < 0.02%

- **最大预期过电压 $v_{max}$**: 通常取 $4 \times v_{crit}$ 或 $5 \times v_{crit}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Tidd线路雷电过电压仿真 | VFDLM计算波形与现场实测数据高度吻合，准确复现了电晕引起的波形衰减与畸变特征。 | 传统宽带(WB)模型忽略电晕效应，导致过电压峰值高估约27% |

| EDF线路快速暂态仿真 | 模型在0.26 μs上升沿激励下表现稳定，计算波形紧密贴合实测记录。 | 传统宽带(WB)模型未考虑电晕非线性，过电压预测值偏高约49% |

| Shiobara线路暂态仿真 | VFDLM成功捕捉了长距离传播中的电晕损耗效应，波形匹配度优异。 | 传统宽带(WB)模型保守估计过电压，误差幅度达31% |



## 量化发现

- TDIP预计算耗时：< 0.6秒（100个电压采样点，Intel Core i7处理器环境）
- 传统宽带(WB)模型忽略电晕效应导致的过电压高估误差：Tidd线27%，EDF线49%，Shiobara线31%
- 矢量拟合最大允许误差：< 0.02%
- 传播函数与特征导纳拟合所需最大极点数量：8个
- 仿真固定时间步长：10 ns
- 电晕起始电压阈值：Tidd线470 kV，EDF线250 kV，Shiobara线303 kV


## 关键公式

### 电压频率相关特征导纳

$$$Y_c(s, v) = Z^{-1}(s) \sqrt{Z(s) Y(s, v)}$$$

*用于构建VFDLM核心频域响应，替代传统线性模型中的常数特征导纳*

### 电压频率相关传播函数

$$$H(s, v) = e^{-\sqrt{Y(s, v) Z(s)} l}$$$

*描述行波在电晕与频变耦合条件下的衰减与相移，其时间延迟随电压升高而增大*

### 线性化节点求解方程

$$$[Y_{sh}(v(t-\Delta t))] \cdot [v(t)] = [i(t)] - [i_{hist}(v(t-\Delta t))]$$$

*在EMT仿真循环中用于快速求解节点电压，利用上一时刻参数避免非线性迭代*



## 验证详情

- **验证方式**: 现场实测数据对比分析
- **测试系统**: Tidd线路、EDF线路、Shiobara线路（单相架空输电线路）
- **仿真工具**: MATLAB平台自主实现
- **验证结果**: VFDLM计算波形与三组现场实测数据高度吻合，准确捕捉了电晕引起的波形衰减与畸变；相比传统WB模型显著降低了过电压预测保守性（误差降低27%~49%），且预计算与在线更新机制保证了计算效率与数值稳定性，验证了模型在快速暂态仿真中的准确性与工程适用性。
