---
title: "Analyses of the modifications in the pi circuits for inclusion of frequency influence in transmission line representation"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Analyses of the modifications in the 蟺 circuits for inclusion of frequency influence in transmission line representation.pdf"]
---

# Analyses of the modifications in the pi circuits for inclusion of frequency influence in transmission line representation

**作者**: 
**年份**: 2011
**来源**: `07&08/Analyses of the modifications in the 蟺 circuits for inclusion of frequency influence in transmission line representation.pdf`

## 摘要

—In this article, it is represented by state variables phase a transmission line which parameters are considered frequency independently and frequency dependent. It is analyzed what is the reasonable number of π circuits and the number of blocks composed by parallel resistor and inductor in parallel for reduction of numerical oscillations. It is simulated the numerical routine with and without the effect of frequency in the longitudinal parameters. Initially, it is used state variables and π circuits representing the transmission line composing a linear system which is solved by numerical routines based on the trapezoidal rule. The effect of frequency on the line is synthesized by resistors and inductors in parallel and this representation is analyzed in details. It is described transmissi

## 核心贡献


- 提出在π型电路中并联RL支路以等效表征输电线路纵向参数的频率依赖性
- 构建基于状态变量与梯形积分法的数值求解算法实现频变线路电磁暂态仿真
- 系统分析并确定级联π电路与并联RL模块的最优数量以有效抑制数值振荡


## 使用的方法


- [[状态变量法|状态变量法]]
- [[梯形积分法|梯形积分法]]
- [[特征线法|特征线法]]
- [[π型电路级联|π型电路级联]]
- [[并联rl支路拟合|并联RL支路拟合]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变π型电路|频变π型电路]]
- [[并联rl等效模块|并联RL等效模块]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值振荡抑制|数值振荡抑制]]
- [[线路参数等值|线路参数等值]]
- [[emtp算法|EMTP算法]]


## 主要发现


- 合理配置π电路级联数与并联RL模块数可显著抑制梯形积分法引发的数值振荡
- 改进π电路模型在宽频范围内能高精度逼近真实频变输电线路的电磁暂态响应
- 状态变量结合梯形法则的算法在Matlab中验证可行满足暂态仿真精度要求



## 方法细节

### 方法概述

本文提出一种基于状态变量法与梯形积分法的频变输电线路电磁暂态仿真方法。将单相输电线路离散为n个级联π型电路，通过在纵向阻抗支路并联m个RL模块来等效拟合电阻与电感随频率变化的特性（集肤效应与大地回路效应）。基于基尔霍夫定律建立包含电容电压与电感电流的连续状态空间方程，利用梯形法则（Heun法）对微分方程进行离散化，推导出显式递推求解格式。通过系统分析π电路级联数量与并联RL模块数量的组合，确定抑制梯形积分法固有数值振荡的最优配置，从而在宽频范围内实现高精度、数值稳定的线路暂态响应计算。

### 数学公式


**公式1**: $$$$\dot{x} = [A]x + [B]u$$$$

*连续时间状态空间方程，描述线路电压与电流状态变量随时间的演化规律*


**公式2**: $$$$x[k+1] = x[k] + \frac{T}{2} \left( A x[k+1] + B u[k+1] + A x[k] + B u[k] \right)$$$$

*梯形积分法离散化公式，将连续微分方程转化为离散时间步长的代数方程*


**公式3**: $$$$x[k+1] = A'' x[k] + B' [u[k] + u[k+1]]$$$$

*递推求解核心公式，其中A''和B'为预计算的常数矩阵，用于高效时域迭代*


**公式4**: $$$$A_\pi = \begin{bmatrix} -\sum_{j=0}^{m}\frac{R_j}{L_0} & \frac{R_1}{L_0} & \cdots & \frac{R_m}{L_0} & -\frac{1}{L_0} \\ \frac{R_1}{L_1} & -\frac{R_1}{L_1} & 0 & 0 & 0 \\ \vdots & 0 & \ddots & 0 & 0 \\ \frac{R_m}{L_m} & 0 & 0 & -\frac{R_m}{L_m} & 0 \\ \frac{2}{C} & 0 & 0 & 0 & -\frac{G}{C} \end{bmatrix}$$$$

*单个改进π电路的状态矩阵，耦合了并联RL支路电流与节点电压的动态关系*


### 算法步骤

1. 1. 线路离散与参数初始化：设定输电线路总长度d，将其均匀划分为n个级联π电路。根据单位长度参数计算每个π电路的纵向电阻R、电感L及横向电导G、电容C。

2. 2. 频变特性综合建模：针对纵向参数，采用m个并联RL支路拟合频率依赖性。通过优化算法或查表法确定各支路电阻R_j与电感L_j的数值，使其等效阻抗在目标频段内逼近实际频变曲线。

3. 3. 构建全局状态矩阵：基于基尔霍夫电压/电流定律列写单个π电路的微分方程组，组装成(m+2)×(m+2)的局部矩阵A_π。将n个π电路级联，构建n(m+2)×n(m+2)的分块三对角全局系统矩阵[A]及输入矩阵[B]。

4. 4. 数值离散化与常数矩阵预计算：设定积分步长T，应用梯形积分法对状态方程进行离散。通过矩阵求逆与乘法运算，预先计算常数矩阵A'=[I-(T/2)A]^{-1}、A''=A'[I+(T/2)A]及B'=A'(T/2)B，避免迭代过程中的重复求逆。

5. 5. 时域步进迭代求解：初始化状态向量x[0]（通常为零初始条件）。在每个时间步k，读取输入激励u[k]与u[k+1]，利用递推公式x[k+1]=A''x[k]+B'[u[k]+u[k+1]]计算下一时刻状态。

6. 6. 结果提取与收敛性验证：从状态向量中提取沿线各节点电压与支路电流。对比不同n与m组合下的波形，评估数值振荡抑制效果与频变拟合精度，确定参数饱和极限。


### 关键参数

- **线路总长度**: 10 km

- **π电路级联数(n)**: 200

- **积分步长(T)**: 50 ns

- **仿真总时长**: 600 μs

- **并联RL模块数(m)**: 4 (理论最小有效值为2)

- **横向电导(G')**: 0.556 μS/km

- **横向电容(C')**: 11.11 nF/km

- **频变拟合频段**: 10 Hz ~ 10 kHz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 恒频参数线路合闸暂态仿真 | 末端开路，首端施加阶跃电压。末端电压呈现约33.3 μs的传播时延（对应波速），随后出现明显的行波反射振荡。末端电流波形因梯形积分法在无损/恒参模型中的数值不稳定性，产生高频非物理振荡。 | 作为基线对照，暴露了传统恒参π电路模型在梯形积分下固有的数值振荡缺陷，无法准确反映实际线路的频变衰减特性。 |

| 频变参数线路合闸暂态仿真（4个RL模块） | 在相同200级π电路与50 ns步长下，引入4个并联RL模块拟合频变特性。末端电压波形因高频损耗增加而呈现显著衰减，反射波幅值逐次降低。末端电流波形平滑，高频数值振荡被完全抑制，物理真实性大幅提升。 | 相较于恒频基线，频变模型消除了非物理数值振荡，电压衰减率与文献基准模型高度吻合，验证了RL并联结构在宽频暂态仿真中的有效性。 |



## 量化发现

- 采用200个π电路级联配合4个并联RL模块，可在10 Hz至10 kHz频段内实现满意的频变参数拟合精度与数值稳定性。
- 并联RL模块数量存在明确下限阈值：至少需要2个模块（分别针对低频与高频特征点）才能有效合成电阻与电感随频率变化的非线性特性，单模块无法覆盖宽频响应。
- 在50 ns积分步长与600 μs仿真周期内，改进模型未出现数值发散或累积误差放大，证明梯形积分法结合频变RL支路具备优异的长期数值稳定性。
- 频变模型的引入使末端电流的非物理振荡幅值降至可忽略水平，相较于恒频模型显著提升了暂态波形的工程适用精度。


## 关键公式

### 连续状态空间方程

$$$$\dot{x} = [A]x + [B]u$$$$

*用于建立包含线路分布参数与并联RL支路的连续时间动态模型*

### 梯形积分递推求解公式

$$$$x[k+1] = A'' x[k] + B' [u[k] + u[k+1]]$$$$

*电磁暂态时域仿真的核心迭代步骤，用于高效计算离散时间步的状态变量*

### 单π电路状态矩阵

$$$$A_\pi = \begin{bmatrix} -\sum_{j=0}^{m}\frac{R_j}{L_0} & \frac{R_1}{L_0} & \cdots & \frac{R_m}{L_0} & -\frac{1}{L_0} \\ \frac{R_1}{L_1} & -\frac{R_1}{L_1} & 0 & 0 & 0 \\ \vdots & 0 & \ddots & 0 & 0 \\ \frac{R_m}{L_m} & 0 & 0 & -\frac{R_m}{L_m} & 0 \\ \frac{2}{C} & 0 & 0 & 0 & -\frac{G}{C} \end{bmatrix}$$$$

*描述单个改进π电路内部各RL支路电流与节点电压的耦合微分关系*



## 验证详情

- **验证方式**: 数值仿真对比分析（恒频模型 vs 频变模型）
- **测试系统**: 10 km单相输电线路，末端开路，首端施加阶跃电压源合闸激励
- **仿真工具**: MATLAB (基于矩阵运算与自定义梯形积分算法)
- **验证结果**: 频变π电路模型成功抑制了梯形积分法在恒参线路中引发的数值振荡，准确复现了行波传播时延与频变衰减特性；验证了2个RL模块为有效拟合频变特性的最小配置，200级π电路配合4个RL模块在50 ns步长下具备优异的数值稳定性与工程适用精度，结果与现有文献基准模型一致。
