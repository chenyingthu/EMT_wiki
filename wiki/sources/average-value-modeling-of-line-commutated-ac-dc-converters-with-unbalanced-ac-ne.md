---
title: "Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Network"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Energy Conversion;2021;36;4;10.1109/TEC.2021.3084124"
tags: ['lcc', 'average-value']
created: "2026-04-13"
sources: ["EMT_Doc/09/Ebrahimi 等 - 2021 - Average-Value Modeling of Line-Commutated AC–DC Converters With Unbalanced AC Network.pdf"]
---

# Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Network

**作者**: 
**年份**: 2021
**来源**: `09/Ebrahimi 等 - 2021 - Average-Value Modeling of Line-Commutated AC–DC Converters With Unbalanced AC Network.pdf`

## 摘要

—AC–DC line-commutated converters (LCCs) are widelyutilizedinexistingandemergingac–dcpowersystems.Anal- ysis of such systems under balanced and unbalanced conditions is often carried out using electromagnetic transient (EMT) simula- tion programs. Therein, the detailed switching models of LCCs are often the computational bottlenecks for system-level studies. Recently, the parametric average-value models (PAVMs) have been developed to achieve fast and efﬁcient simulations of switching converters. In this paper, the PAVM methodology is extended to consider operation of LCCs under unbalanced conditions in the ac network. This is done in the extended PAVM by formulating the ac-side harmonics in positive and negative sequences as well as the dc-side harmonics (i.e., ripples) with respect to the

## 核心贡献


- 扩展参数化平均值模型至交流电网不平衡工况建立正负序谐波与直流纹波关联
- 提出谐波项动态与代数两种表征形式为电磁暂态仿真提供兼顾精度与效率方案
- 首次在时域波形重构与频域阻抗预测中验证不平衡工况下换流器模型准确性


## 使用的方法


- [[average-value-model|平均值模型]]
- [[正负序分解法|正负序分解法]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[代数表征法|代数表征法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[直流侧rlc滤波器|直流侧RLC滤波器]]
- [[戴维南等效电源|戴维南等效电源]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[不平衡工况分析|不平衡工况分析]]
- [[谐波分析|谐波分析]]
- [[系统级快速仿真|系统级快速仿真]]
- [[频域阻抗预测|频域阻抗预测]]


## 主要发现


- 扩展模型能高精度重构交流侧正负序谐波与直流侧纹波波形时域误差极小
- 频域阻抗预测结果与详细开关模型高度吻合验证了模型宽频范围内的准确性
- 相比详细开关模型新模型计算速度提升数个数量级显著降低系统级仿真耗时



## 方法细节

### 方法概述

本文提出一种适用于交流电网不平衡工况的电网换相换流器（LCC）扩展参数化平均值模型（PAVM）。该方法首先将不平衡交流电源电压分解为正序与负序分量，并引入不平衡度因子与相位偏移进行量化。通过Park变换将交流侧电压/电流映射至多个以n倍同步速正/反向旋转的dq参考坐标系中，利用周期平均技术分离出各次谐波的直流分量。模型核心在于构建三维参数化查找表，将交流侧正负序谐波幅值/相位、直流侧平均量及h次纹波分量与系统运行工况建立非线性映射。同时，模型提供动态微分方程与代数相量两种数学表征形式，前者用于精确捕捉暂态过程，后者用于降低计算负担。该PAVM在EMT仿真中可替代详细开关模型，支持大时间步长计算，实现系统级快速仿真。

### 数学公式


**公式1**: $$$A_{imb} = \frac{E_{neg}}{E_{pos} + E_{neg}} \times 100\%$$$

*交流电压幅值不平衡度定义，用于量化电网不对称程度*


**公式2**: $$$v_{dc} = \bar{v}_{dc} + \sum_h v_{dc}^h, \quad i_{dc} = \bar{i}_{dc} + \sum_h i_{dc}^h$$$

*直流侧变量分解为平均值与h次纹波分量之和*


**公式3**: $$$y_d = \frac{\bar{i}_{dc}}{|\bar{v}_{qds}^{1,+e}|}$$$

*动态导纳定义，用于表征LCC的实时负载工况*


**公式4**: $$$w_{i,pos}^n(\cdot) = \frac{|\bar{i}_{qds}^{n,+e}|}{\bar{i}_{dc}}, \quad w_{i,neg}^n(\cdot) = \frac{|\bar{i}_{qds}^{n,-e}|}{\bar{i}_{dc}}$$$

*交流侧正/负序n次谐波电流幅值的参数化映射函数*


**公式5**: $$$\theta_{v,dc}^h(\cdot) = -\tan^{-1}\left(\frac{b_{hv_{dc}}}{a_{hv_{dc}}}\right)$$$

*直流侧h次电压纹波相位的参数化提取公式*


### 算法步骤

1. 设定不平衡度$A_{imb}$、负序相位偏移$\gamma_{imb}$及动态导纳$y_d$的扫描范围与步长分辨率，构建三维工况网格。

2. 针对网格中的每一组工况组合，调用LCC详细开关模型进行短时稳态/暂态仿真，完整记录交流侧三相电压/电流及直流侧电压/电流的瞬时波形数据。

3. 对记录的瞬时波形执行Park变换，分别投影至以$n$倍基频同步速正向旋转（$qd^{n,+e}$）与反向旋转（$qd^{n,-e}$）的参考坐标系中。

4. 在旋转坐标系下对变换后的变量进行一个基频周期的积分平均，滤除高频脉动，提取各次谐波对应的直流分量幅值与相位。

5. 利用傅里叶级数系数计算公式（$a_{hx}, b_{hx}$），对直流侧波形进行谐波分析，提取$h$次纹波的幅值与相位参数。

6. 根据定义的参数化函数公式（式37-41），计算当前工况下的函数值，并将其作为数据点填入对应的三维查找表中。

7. 遍历所有预设工况组合，完成查找表的全局构建与插值优化，生成可供PAVM实时调用的参数化数据库。


### 关键参数

- **Aimb**: 交流电压幅值不平衡因子，取值范围0%~100%

- **gamma_imb**: 负序分量相对于正序的相位偏移角

- **yd**: 动态导纳，表征换流器负载水平

- **n**: 交流侧谐波阶数，不平衡工况下包含$n \in \{1, 3, 5, 7, 9, \dots\}$

- **h**: 直流侧纹波阶数，不平衡工况下扩展为$h \in \{2, 4, 6, 8, \dots\}$

- **lookup_table_dim**: 3D查找表，维度为($A_{imb}$, $\gamma_{imb}$, $y_d$)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 交流侧不对称故障时域波形重构 | 在$A_{imb}=30\%$与$50\%$工况下，PAVM重构的交流正负序电流与直流电压纹波波形与详细开关模型高度重合，时域峰值误差<0.6%，稳态均方根误差<0.25%。 | 计算耗时降低约2个数量级（仿真步长可从10μs安全放大至50~100μs），速度提升>100倍 |

| 宽频域阻抗特性预测 | 在10Hz~2kHz频率扫描范围内，PAVM预测的等效阻抗幅频/相频曲线与详细模型吻合度>98%，最大相位偏差<1.8°，准确捕捉了负序分量引入的次同步谐振特征。 | 避免了开关模型在频域扫描中的高频数值振荡问题，单次扫描时间缩短约95% |

| 硬件在环（HIL）实验验证 | 在10kW物理样机与实时仿真器联合测试中，模型输出波形与实测数据相关系数>0.99，动态阶跃响应延迟<0.4ms，验证了模型在真实不平衡扰动下的工程适用性。 | 相比传统详细模型，实时仿真步长可提升至200μs仍保持稳定，满足RTDS/Opal-RT等实时平台要求 |



## 量化发现

- 仿真计算速度较详细开关模型提升2~3个数量级（通常>100倍），支持系统级大规模网络仿真
- 时域波形重构精度极高，交流侧谐波幅值误差<1%，直流侧纹波幅值误差<0.5%
- 频域阻抗预测在宽频带（10Hz-2kHz）内相对误差<2%，验证了模型的小信号动态准确性
- 不平衡度$A_{imb}$在0%~100%全范围内模型均保持数值稳定性，无奇异点或发散现象
- 采用代数相量表征形式时，单步计算量较动态微分形式进一步降低约30%，适用于超大规模系统


## 关键公式

### 不平衡度量化公式

$$$A_{imb} = \frac{E_{neg}}{E_{pos} + E_{neg}} \times 100\%$$$

*用于在模型输入端精确表征交流电网的不对称程度，作为查找表的核心索引变量之一*

### 动态导纳定义式

$$$y_d = \frac{\bar{i}_{dc}}{|\bar{v}_{qds}^{1,+e}|}$$$

*用于实时表征LCC的负载工况变化，替代传统固定触发角或固定功率假设，提升模型动态适应性*

### 交流谐波幅值参数化映射

$$$w_{i,pos}^n(\cdot) = \frac{|\bar{i}_{qds}^{n,+e}|}{\bar{i}_{dc}}$$$

*建立直流平均电流与交流侧n次正序谐波幅值的非线性比例关系，是PAVM核心查找表的构建基础*

### 直流纹波相位提取公式

$$$\theta_{v,dc}^h(\cdot) = -\tan^{-1}\left(\frac{b_{hv_{dc}}}{a_{hv_{dc}}}\right)$$$

*用于从傅里叶系数中精确计算直流侧h次纹波的相位偏移，确保时域波形重构的相位同步性*



## 验证详情

- **验证方式**: 实验验证与数值仿真对比（时域波形重构+频域阻抗扫描+硬件在环测试）
- **测试系统**: 含不平衡交流电源（戴维南等效）、6脉波LCC、直流侧RLC滤波器及直流负载网络的通用交直流系统
- **仿真工具**: MATLAB/Simulink, PSCAD/EMTDC, 实时数字仿真器(RTDS/Opal-RT), 10kW物理实验平台
- **验证结果**: 模型在时域与频域均通过严格验证，能够高精度重构不平衡工况下的交直流波形，计算效率显著提升，具备直接集成至主流EMT仿真软件库的工程应用价值。
