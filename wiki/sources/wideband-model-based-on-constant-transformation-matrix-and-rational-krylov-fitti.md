---
title: "Wideband model based on constant transformation matrix and rational Krylov fitting"
type: source
authors: ['Emmanuel Francois']
year: 2023
journal: "Electric Power Systems Research, 220 (2023) 109295. doi:10.1016/j.epsr.2023.109295"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/Francois 等 - 2023 - Wideband model based on constant transformation matrix and rational Krylov fitting.pdf"]
---

# Wideband model based on constant transformation matrix and rational Krylov fitting

**作者**: Emmanuel Francois
**年份**: 2023
**来源**: `40/Francois 等 - 2023 - Wideband model based on constant transformation matrix and rational Krylov fitting.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Wideband model based on constant transformation matrix and rational Emmanuel Francois a, Ilhan Kocar b,*, Jean Mahseredjian a a Department of Electrical Engineering, Polytechnique Montreal, Montreal, H3T 1J4, QC Canada b Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong SAR

## 核心贡献



- 首次证明使用恒定变换矩阵会因频率点选择不同而内在破坏输电线路系统的无源性
- 提出并评估了基于有理Krylov拟合的新策略，证明其相比向量拟合能生成更精确且低阶的模型

## 使用的方法


- [[vector-fitting]]

## 涉及的模型


- [[transmission-line]]
- [[cable]]

## 相关主题


- [[passivity]]
- [[frequency-dependent]]

## 主要发现



- 恒定变换矩阵的引入会导致最终有理模型在特定频段违反无源性
- 有理Krylov拟合在模型精度和阶数控制上均优于传统的向量拟合算法
- 基于Bode拟合的传统恒定T模型在相域拟合精度较差，直接导致其时域仿真结果不准确

## 方法细节

### 方法概述

本文提出基于恒定变换矩阵(Constant T)的宽带模型(CTWB)，通过模态分解将传播函数$H$分解为模态形式，使用有理Krylov拟合(RKF)或向量拟合(VF)在模域进行拟合，再利用恒定的实变换矩阵$T_{const}$将结果转换回相域。该方法允许处理多导体传输线，同时研究了恒定$T$对系统无源性的影响，并首次证明恒定$T$的选择会内在地导致特定频段的无源性违反。

### 数学公式


**公式1**: $$$Y_c = \Gamma Z^{-1}$, where $\Gamma = \sqrt{YZ}$$$

*特性导纳矩阵定义，其中$Y$和$Z$分别为单位长度并联导纳和串联阻抗矩阵*


**公式2**: $$$H = e^{-\Gamma L}$$$

*传播矩阵定义，$L$为线路长度*


**公式3**: $$$H = T H_m T^{-1}$$$

*传播矩阵的模态分解，$T$为特征向量矩阵，$H_m$为对角模态传播矩阵*


**公式4**: $$$H_m = \text{diag}[e^{\lambda_1}, e^{\lambda_2}, \cdots, e^{\lambda_N}]$$$

*模态传播函数对角矩阵，$\lambda_i$为$-\sqrt{YZ}L$的特征值*


**公式5**: $$$\hat{H}_i = \sum_{k=1}^{M_i} \frac{r_k}{s - p_{i,k}} e^{-s\tau_i} \cong H_i$$$

*第$i$个模态的有理函数拟合形式，$M_i$为极点数，$\tau_i$为时延*


**公式6**: $$$H_{fit} = T_{const} H_{modefit} T_{const}^{-1}$$$

*使用恒定变换矩阵将拟合后的模态函数转换回相域*


**公式7**: $$$I_0 - Y_c V_0 = -H(I_L + Y_c V_L)$$$

*线路首端电流电压关系（相域）*


**公式8**: $$$e = \|H - T_{const} H_{modefit} T_{const}^{-1}\|_2$$$

*恒定$T$拟合误差计算，用于选择最优的常数变换矩阵*


### 算法步骤

1. 计算频域样本：在所需频带内计算多导体线路的单位长度参数矩阵$Y$和$Z$，进而计算特性导纳$Y_c$和传播矩阵$H$的频域样本

2. 模态分解：对每个频率样本计算传播矩阵$H$的特征值分解，得到模态传播矩阵$H_m = \text{diag}[e^{\lambda_1},...,e^{\lambda_N}]$和变换矩阵$T$

3. 选择恒定变换矩阵：在$N_\omega$个频率样本中选择特定频率点（如1000 Hz）处的变换矩阵$T_i$，取其实部并旋转以最小化虚部，得到$T_{const}$

4. 提取模态函数：从$H_m$中提取各模态传播函数$H_i = e^{\lambda_i}$，并优化时延$\tau_i$以减少拟合误差

5. 有理函数拟合：使用RKF或VF算法将每个模态函数$H_i$拟合为部分分式展开形式$\sum_{k=1}^{M_i} \frac{r_k}{s-p_{i,k}}e^{-s\tau_i}$

6. 相域重构：利用$T_{const}$构建对角矩阵$H_{modefit} = \text{diag}[\hat{H}_1,...,\hat{H}_N]$，计算相域传播矩阵$H_{fit} = T_{const} H_{modefit} T_{const}^{-1}$

7. 无源性验证：检查由$H_{fit}$和$Y_c$构建的节点导纳矩阵特征值，验证在特定频段是否存在负特征值（无源性违反）

8. 时域离散化：将有理近似转换为离散状态空间形式，采用分段线性输入假设的精确解，应用两步插值最小化积分误差，可选进行DC校正


### 关键参数

- **T_const_selection_frequency**: 1000 Hz（默认），用户可手动设置或选择使误差$e$最小的频率点

- **ground_wire_radius**: 4.75 mm

- **ground_wire_DC_resistance**: 3.75 Ohm/km

- **bundle_radius**: 230.09 mm

- **bundle_angle**: 0°

- **conductor_radius**: 15.29 mm

- **conductor_DC_resistance**: 0.0701 Ohm/km

- **number_of_conductors**: 3（三导体束）

- **fitting_order_VF**: 各模态极点数$M_i$的总和（具体数值依案例而定）

- **fitting_order_RKF**: 各模态极点数$M_i$的总和（显著低于VF）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case-1三导体束传输线 | 对比RKF与VF在CTWB中的拟合性能。RKF生成的模型极点数显著少于VF，同时保持相当的精度。在时域开关瞬态仿真中，CTWB能够精确生成电压波形 | RKF比VF生成更低阶的模型（less order），具体阶数比未明确给出但描述为'remarkably less poles'；传统FD模型（基于Bode拟合）在相域表现出较差的拟合精度 |

| 无源性验证测试 | 验证恒定$T$对系统无源性的影响。当选择特定频率点（如1000Hz）作为$T_{const}$时，重构的相域传播函数在某些频段导致节点导纳矩阵出现负特征值 | 使用恒定$T$内在地违反系统无源性，而非常规WB模型（ULM/FDCM）在相域直接拟合可避免此问题 |



## 量化发现

- 恒定变换矩阵$T_{const}$的选择频率默认为1000 Hz，此时在特定测试案例中观察到无源性违反
- RKF算法生成的有理模型阶数（极点总数）显著低于VF算法，在保持相同精度的前提下实现模型降阶
- 传统FD模型基于Bode拟合在相域的拟合误差显著大于现代方法（VF/RKF），这直接解释了其时域仿真的不准确性
- 三导体束案例中的导体直流电阻为0.0701 Ohm/km，地线直流电阻为3.75 Ohm/km
- 模态分解中，各模态$H_i$的拟合采用部分分式展开，极点数$M_i$取决于所选算法（RKF通常需要更少的极点）
- 无源性违反的程度和频段取决于$T_{const}$所选取的具体频率点，并非所有频率选择都会导致无源性丧失


## 关键公式

### 模态分解方程

$$$H = T H_m T^{-1}$$$

*将相域传播矩阵分解为模态形式，是恒定T方法的基础*

### 恒定T相域重构方程

$$$H_{fit} = T_{const} H_{modefit} T_{const}^{-1}$$$

*使用恒定实变换矩阵将拟合后的模态函数转换回相域，此步骤可能引入无源性违反*

### 模态有理拟合方程

$$$\hat{H}_i = \sum_{k=1}^{M_i} \frac{r_k}{s - p_{i,k}} e^{-s\tau_i}$$$

*使用RKF或VF对每个传播模态进行有理函数拟合的标准形式*



## 验证详情

- **验证方式**: 数值仿真对比与理论分析
- **测试系统**: 三导体束架空传输线（Three-conductor bundle），包含地线，具体参数包括：地线半径4.75mm、电阻3.75Ohm/km；导体半径15.29mm、电阻0.0701Ohm/km；束半径230.09mm
- **仿真工具**: 基于EMT仿真原理的数值实现（文中提及ULM和FDCM的实现框架，使用精确状态空间离散化和两步插值方法）
- **验证结果**: RKF在CTWB框架下比VF生成更低阶且精确的模型；恒定T方法因频率点选择不同会导致无源性违反，而传统基于Bode拟合的FD模型在相域精度显著低于现代部分分式展开方法（VF/RKF），这解释了FD模型在时域的不准确性
