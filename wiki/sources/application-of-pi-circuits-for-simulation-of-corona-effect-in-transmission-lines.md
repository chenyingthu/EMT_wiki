---
title: "Application of pi circuits for simulation of corona effect in transmission lines"
type: source
authors: ['未知']
year: 2011
journal: "2012 IEEE Power and Energy Society General Meeting;2012; ; ;10.1109/PESGM.2012.6345558"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/09/Lessa 等 - 2012 - Application of π circuits for simulation of corona effect in transmission lines.pdf"]
---

# Application of pi circuits for simulation of corona effect in transmission lines

**作者**: 
**年份**: 2011
**来源**: `09/Lessa 等 - 2012 - Application of π circuits for simulation of corona effect in transmission lines.pdf`

## 摘要

—In this article, it is represented by state variables phase a transmission line which parameters are considered frequency independently and frequency dependent. Based on previous analyses, it is used the reasonable number of π circuits and the number of blocks composed by parallel resistor and inductor for reduction of numerical oscillations. It is analyzed the influence of the increase of the RL parallel blocks in the obtained results. The RL parallel blocks are used for inclusion of the frequency influence in the transmission line longitudinal parameter. It is a simple model that is been used by undergraduate students for simulation of traveling wave phenomena in transmission lines. Considering the model without frequency influence, it is included a representation of the corona effect. 

## 核心贡献


- 提出基于级联π型电路与并联RL支路的输电线路状态变量模型，有效抑制数值振荡
- 在频域无关模型中引入电晕效应局部表征方法，简化了暂态仿真建模流程
- 结合梯形积分法构建简化算法，突破传统EMTP程序对π电路数量的限制


## 使用的方法


- [[状态变量法|状态变量法]]
- [[梯形积分法|梯形积分法]]
- [[π型电路级联|π型电路级联]]
- [[并联rl支路频率拟合|并联RL支路频率拟合]]
- [[矩阵数值求解|矩阵数值求解]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[π型等效电路|π型等效电路]]
- [[电晕效应模型|电晕效应模型]]
- [[频变参数模型|频变参数模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[行波分析|行波分析]]
- [[频率相关建模|频率相关建模]]
- [[数值振荡抑制|数值振荡抑制]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 增加并联RL支路数量可显著降低仿真中的数值振荡，提升频变参数拟合精度
- 引入局部电晕效应模型后，线路暂态电压波形呈现明显衰减与非线性畸变特征
- 基于MATLAB的简化π电路算法在保持精度的同时，有效突破了传统EMTP的规模限制



## 方法细节

### 方法概述

本文提出一种基于状态变量法的单相等效输电线路电磁暂态仿真模型。该模型采用级联π型电路对线路进行空间离散化，并通过在纵向阻抗支路中并联多个RL模块来拟合参数的频率相关性（集肤效应与大地回路损耗）。数值求解采用梯形积分法（Heun法）将连续状态空间方程离散化，构建全局状态转移矩阵与输入矩阵。针对电晕效应，在频域无关模型基础上引入Gary经验公式，根据瞬时电压动态修正对地电容。整个算法在MATLAB中实现，利用矩阵运算突破传统EMTP程序对π电路数量的限制，适用于行波传播、数值振荡抑制及非线性暂态现象的教学与基础研究。

### 数学公式


**公式1**: $$$\dot{x} = [A]x + [B]u$$$

*连续时间状态空间方程，x为状态变量向量（沿线电压与电感电流），u为输入向量，A和B为系统矩阵。*


**公式2**: $$$x[k+1] = A''x[k] + B'[u[k] + u[k+1]]$$$

*基于梯形积分法离散化后的迭代求解公式，用于时域步进计算。*


**公式3**: $$$A' = \left[I - \frac{T}{2}A\right]^{-1}, \quad A'' = A'\left[I + \frac{T}{2}A\right], \quad B' = A'\frac{T}{2}B$$$

*离散化过程中的常数矩阵定义，T为积分步长，I为单位矩阵。*


**公式4**: $$$C_{CORONA} = C \cdot \eta \cdot \left(\frac{V}{V_{CORONA}}\right)^{\eta-1}, \quad \eta = 0.22 \cdot R_{COND} + 1.2$$$

*电晕效应非线性电容模型，根据瞬时电压V与起晕电压VCORONA的比值动态更新对地电容。*


### 算法步骤

1. 根据线路单位长度参数（R', L', G', C'）和总分段数n，计算单个π电路的分布参数。

2. 针对频率相关模型，在每个π电路纵向支路中串联指定数量的并联RL模块（本文采用4个），根据文献方法拟合目标频段（10Hz~10kHz）的阻抗特性。

3. 建立单π电路的状态空间矩阵$A_\pi$（维度$(m+2)\times(m+2)$，m为RL支路数）和输入矩阵$B$，推导包含所有支路电流与节点电压的微分方程组。

4. 将n个π电路级联，构建全局三对角块矩阵$[A]$（维度$n(m+2) \times n(m+2)$）和全局输入向量$[B]$，处理相邻π电路间的耦合关系。

5. 应用梯形积分法对全局状态方程进行离散化，预计算迭代矩阵$A''$和$B'$，避免每步重复求逆。

6. 设置初始条件（零状态）、时间步长$T=50\text{ns}$及首端阶跃激励$u(t)=1\text{kV}$，末端设为开路边界。

7. 按时间步迭代求解$x[k+1] = A''x[k] + B'[u[k] + u[k+1]]$，提取沿线电压与电流状态变量。

8. 若启用模块，在指定区段（如中间10个π电路）根据当前步电压$V$动态更新$C_{CORONA}$，修正对应行的矩阵元素后继续迭代。


### 关键参数

- **线路长度**: 10 km

- **π电路数量**: 200

- **时间步长**: 50 ns

- **仿真总时长**: 600 μs

- **激励源**: 1 kV阶跃电压

- **终端条件**: 末端开路

- **RL并联支路数**: 4个/π电路

- **频率拟合范围**: 10 Hz ~ 10 kHz

- **导体半径_RCOND**: 2.54 cm

- **频变纵向参数_R0_L0**: 0.026 Ω/km, 2.209 mH/km

- **频变纵向参数_R1_L1**: 1.470 Ω/km, 0.74 mH/km

- **频变纵向参数_R2_L2**: 2.354 Ω/km, 0.12 mH/km

- **频变纵向参数_R3_L3**: 20.149 Ω/km, 0.10 mH/km

- **频变纵向参数_R4_L4**: 111.111 Ω/km, 0.05 mH/km

- **横向参数_G_C**: 0.556 μS/km, 11.11 nF/km

- **频域无关简化参数**: R=0.05 Ω/km, L=1 mH/km



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 频域无关模型（200个π电路） | 末端电压波形呈现明显的数值振荡，无幅值衰减，行波传播延迟约33.3μs（对应10km线路波速），振荡频率与时间步长及离散化阶数直接相关。 | 作为基线对比，暴露了传统集中参数模型在高频暂态下的数值不稳定性。 |

| 频域相关模型（4个RL支路/π电路） | 末端电压波形平滑，高频数值振荡被完全抑制，幅值呈现自然衰减特征，准确反映了集肤效应与大地损耗对行波的滤波作用。 | 相比频域无关模型，波形畸变率降低>90%，完全消除虚假振荡，符合实际线路物理特性。 |

| 电晕效应仿真（VCORONA=0.35~0.9 pu） | 电晕区段作用于线路中段10个π电路（500m）。当起晕电压比降至0.35 pu时，末端电压峰值衰减约15%，波形上升沿明显展宽，呈现典型非线性电容充电特征。 | 与无电晕工况相比，暂态过电压幅值显著降低，验证了局部电晕对行波能量的吸收与波形平滑作用。 |



## 量化发现

- 至少需要2个并联RL支路才能准确合成线路纵向电阻的频率特性，采用4个支路可完整覆盖10Hz~10kHz频段。
- 使用200个π电路离散10km线路，配合50ns时间步长，可完全消除数值振荡，仿真结果满足工程教学精度要求。
- 电晕效应局部作用于线路中段500m（10个π电路），当起晕电压比$V_{CORONA}/V$降至0.35时，末端暂态电压峰值衰减约15%。
- MATLAB实现的矩阵迭代算法突破了传统EMTP对π电路数量的限制，支持大规模级联（n≥200）且保持数值稳定性。


## 关键公式

### 梯形积分离散迭代方程

$$$x[k+1] = A''x[k] + B'[u[k] + u[k+1]]$$$

*用于时域步进求解状态变量，是EMT仿真的核心数值推进公式。*

### Gary电晕非线性电容模型

$$$C_{CORONA} = C \cdot \eta \cdot \left(\frac{V}{V_{CORONA}}\right)^{\eta-1}$$$

*在频域无关模型中引入，用于动态修正对地电容以模拟电晕放电引起的非线性暂态响应。*

### 状态转移矩阵系数

$$$A' = \left[I - \frac{T}{2}A\right]^{-1}$$$

*梯形积分法离散化过程中用于构建隐式求解格式的关键矩阵，保证数值稳定性。*



## 验证详情

- **验证方式**: 数值仿真对比分析（频域无关 vs 频域相关，含/不含电晕效应）
- **测试系统**: 10km单相输电线路，末端开路，首端施加1kV阶跃电压源，线路中段500m设置电晕区段
- **仿真工具**: MATLAB (矩阵运算与梯形积分求解)
- **验证结果**: 模型在200个π电路级联下保持数值稳定，频变参数拟合精度满足要求，电晕模型成功复现电压衰减与波形畸变。算法有效抑制了传统集中参数模型的数值振荡，验证了其在行波传播分析与基础电磁暂态教学中的有效性与高精度。
