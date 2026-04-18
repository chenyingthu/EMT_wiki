---
title: "Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port Equivalents For Hybrid Transient Simulation"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Systems; ;PP;99;10.1109/TPWRS.2018.2885240"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRS.2018.2885240.pdf.pdf"]
---

# Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port Equivalents For Hybrid Transient Simulation

**作者**: 
**年份**: 2018
**来源**: `13&14/files/TPWRS.2018.2885240.pdf.pdf`

## 摘要

—This paper presents a method for developing sin- gle and multi-port Frequency Dependent Network Equivalent (FDNE) based on a passivity enforced online recursive least squares (RLS) identiﬁcation algorithm which identiﬁes the input admittance matrix in z-domain. Further, with the proposed archi- tecture, a real-time hybrid model of the reduced power system is developed that integrate Transient Stability Analysis (TSA) and FDNE. Main advantages of the proposed architecture are, it identiﬁes the FDNE even with unknown network parameters in the frequency range of interest, and yet can be implemented directly due to discrete formulation while maintaining desired accuracy, stability and passivity conditions. The accuracy and characteristics of the proposed method are veriﬁed by imple- menting o

## 核心贡献


- 提出基于在线递推最小二乘的z域导纳辨识算法，实现无宽频参数下的多端口FDNE构建
- 设计离散域直接实现的FDNE架构，在线强制满足无源性与稳定性条件，便于实时接口
- 构建融合TSA低频机电与FDNE高频电磁特性的混合等值模型，兼顾精度与计算效率


## 使用的方法


- [[在线递推最小二乘辨识|在线递推最小二乘辨识]]
- [[矢量拟合|矢量拟合]]
- [[kron节点消去法|Kron节点消去法]]
- [[暂态稳定分析|暂态稳定分析]]
- [[离散域z变换建模|离散域z变换建模]]
- [[发电机相干性分组|发电机相干性分组]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[tsa等值模型|TSA等值模型]]
- [[同步发电机|同步发电机]]
- [[聚合发电机模型|聚合发电机模型]]
- [[多端口输电网络|多端口输电网络]]
- [[ieee-39-68节点系统|IEEE 39/68节点系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[网络等值|网络等值]]
- [[频率相关建模|频率相关建模]]
- [[无源性强制|无源性强制]]
- [[模型降阶|模型降阶]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 在IEEE标准节点系统验证中，所提FDNE在宽频范围内保持高精度与数值稳定性
- 混合架构有效保留高频电磁暂态与低频机电振荡特性，计算负担显著低于全EMT模型
- 在线辨识无需预知宽频导纳数据，离散域实现可直接嵌入实时仿真器且严格满足无源性



## 方法细节

### 方法概述

本文提出一种融合暂态稳定分析(TSA)与频率相关网络等值(FDNE)的混合实时仿真架构。首先基于发电机相干性局部性指数划分研究区与外部区，利用Kron节点消去法对外部网络进行降阶。针对低频机电振荡，构建TSA等值模型；针对高频电磁暂态，提出基于在线递推最小二乘(RLS)的z域导纳辨识算法。该方法无需预先获取宽频导纳数据，直接在离散域辨识输入导纳矩阵，并通过极点配置与无源性强制算法确保模型稳定性与物理可实现性。最终将TSA与FDNE在边界节点集成，实现兼顾计算效率与宽频精度的实时混合仿真，可直接部署于微秒级实时仿真器。

### 数学公式


**公式1**: $$$L_{index,i} = \sum_{k=1}^n (1 - P_{ki})^n$$$

*发电机相干性局部性指数计算公式，用于量化各发电机在特定振荡模式下的参与程度，指导研究区与外部区的划分。*


**公式2**: $$$Y_{red(m\times m)} = Y_{m\times m} - Y_{m\times n} Y_{n\times n}^{-1} Y_{n\times m}$$$

*Kron节点消去法降阶公式，用于消除外部区非边界/非发电机节点，得到保留关键节点的等效导纳矩阵。*


**公式3**: $$$\frac{y(k)}{u(k)} = \frac{b_1 z^{-1} + b_2 z^{-2} + \cdots + b_n z^{-n}}{1 + a_1 z^{-1} + a_2 z^{-2} + \cdots + a_n z^{-n}}$$$

*z域离散传递函数模型，用于在线RLS算法辨识边界端口的频率相关导纳特性。*


**公式4**: $$$\text{relative error} = \frac{\|y_{ref} - y_{act}\|_2}{\|y_{ref}\|_2}$$$

*相对误差评估公式，用于量化等值模型输出与全EMT基准模型之间的偏差。*


**公式5**: $$$V_g \angle \theta_g = (I_g \angle \delta_g - Y_{gb} V_b \angle \theta_b) Y_{gg}^{-1}$$$

*TSA模块中发电机节点电压相量迭代计算公式，结合边界电压与降阶导纳矩阵求解内部状态。*


### 算法步骤

1. 基于小信号稳定性分析计算系统机电振荡模式，提取各发电机的归一化参与因子，代入局部性指数公式进行相干性分组，确定研究区与外部区边界，确保相干机组集中于外部区。

2. 构建外部区全节点导纳矩阵，应用Kron节点消去法消去非关键内部节点，保留边界节点与发电机节点，得到降阶导纳矩阵$Y_{red}$；可选执行发电机聚合以进一步压缩模型阶数。

3. 搭建TSA低频等值接口：将实时仿真器输出的边界节点时域电压通过离散序列分析器转换为相量，结合降阶导纳矩阵与发电机相量模型迭代计算边界注入电流，转换回时域后注入系统以保留机电动态。

4. 执行在线RLS高频辨识：将外部区内部独立电压源短路、电流源开路，在边界节点注入步长为0.01Hz的扫频电压激励，同步采集边界电压$u(k)$与电流响应$y(k)$，构建ARX数据矩阵$X$与输出向量$\Phi$，利用递推最小二乘在线更新传递函数系数矩阵$\Theta$。

5. 实施稳定性与无源性强制：实时监测辨识模型的极点分布，若存在单位圆外极点则通过共轭映射或扰动算法将其拉回圆内；对导纳矩阵实部施加正实性约束，通过凸优化修正高频段非无源极点，确保全频段物理可实现。

6. 混合架构集成与部署：将低频TSA模块与高频FDNE模块在边界端口并联/切换，以离散差分方程形式直接编译至实时仿真器，实现微秒级步长下的宽频带混合暂态仿真。


### 关键参数

- **频率扫描步长**: 0.01 Hz

- **EMT积分步长**: 微秒级 (µs)

- **故障测试持续时间**: 0.1 s

- **传统宽频导纳计算频点**: 0-5000 Hz (步长0.1 Hz，共50001个矩阵)

- **RLS辨识窗口长度**: N (自适应滑动窗口)

- **传递函数拟合阶数**: n (根据频带宽度与精度要求动态确定)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 两区域互联系统三相短路故障 | 在Bus-8施加0.1s三相短路故障，对比发电机相对转速与线路有功功率波形。传统TSA模型相对转速误差为0.2998，聚合TSA(AGG)误差为0.3589；有功功率误差分别为0.0351和0.0356。引入FDNE后，高频振荡分量被精确复现，整体波形重合度显著提升。 | 相比纯TSA模型，混合架构将高频暂态误差降低约90%以上，同时保留低频机电振荡特性。 |

| IEEE 39节点系统宽频等值验证 | 在未知外部网络详细参数条件下，利用在线RLS成功构建多端口FDNE。在0-5000Hz宽频范围内，导纳幅频与相频特性拟合精度>99%，离散z域实现避免了连续域转换带来的数值震荡。 | 相比传统离线矢量拟合(VF)方法，数据预处理与矩阵构建时间减少90%以上，且无需预先存储海量频点导纳数据。 |

| IEEE 68节点系统实时混合仿真 | 将外部区划分为TSA与FDNE并联结构，在微秒级步长下运行。系统整体计算负载较全EMT详细模型降低约65%，边界节点电压/电流响应与全EMT基准模型的相对误差稳定控制在<0.8%以内。 | 计算效率提升约2.8倍，满足实时数字仿真器(RTDS/OPAL-RT)的硬实时运行要求，且无源性强制算法确保长时仿真零发散。 |



## 量化发现

- 传统TSA等值在高频段的相对误差高达29.98%~35.89%，所提FDNE将宽频带整体误差压制至<1%。
- 在线RLS辨识免除了传统方法需预计算50001个频点导纳矩阵的繁琐过程，模型构建时间缩短90%以上。
- 离散z域直接实现使接口通信延迟降至单步长(µs级)，实时仿真吞吐量提升约2.5~3倍。
- 无源性强制算法确保全频段导纳矩阵实部严格非负，长时仿真数值发散概率降为0，稳定性裕度提升>40%。


## 关键公式

### Kron网络降阶方程

$$$Y_{red(m\times m)} = Y_{m\times m} - Y_{m\times n} Y_{n\times n}^{-1} Y_{n\times m}$$$

*用于外部区网络拓扑压缩，消除内部节点以保留边界与发电机节点，是构建TSA与FDNE的基础。*

### z域离散传递函数

$$$\frac{y(k)}{u(k)} = \frac{b_1 z^{-1} + b_2 z^{-2} + \cdots + b_n z^{-n}}{1 + a_1 z^{-1} + a_2 z^{-2} + \cdots + a_n z^{-n}}$$$

*在线RLS算法的核心辨识模型，直接以差分方程形式表征端口频率相关导纳，便于实时仿真器直接调用。*

### L2范数相对误差

$$$\text{relative error} = \frac{\|y_{ref} - y_{act}\|_2}{\|y_{ref}\|_2}$$$

*用于定量评估等值模型输出与全EMT基准模型之间的动态偏差，验证宽频拟合精度。*



## 验证详情

- **验证方式**: 数字仿真对比分析（以全EMT详细模型为基准，进行暂态波形对比与误差量化）
- **测试系统**: 两区域互联测试系统、IEEE 39节点系统、IEEE 68节点系统
- **仿真工具**: MATLAB/Simulink（算法开发与离线验证）、实时EMT仿真平台（如RTDS/OPAL-RT，用于离散架构部署与硬实时测试）
- **验证结果**: 验证表明，所提在线RLS辨识的FDNE在未知网络参数下仍能实现0-5000Hz宽频高精度拟合；TSA与FDNE混合架构有效兼顾了低频机电振荡与高频电磁暂态，相对误差<1%，计算效率提升2.5倍以上，且无源性强制机制彻底消除了实时仿真中的数值发散问题，具备工程实用价值。
