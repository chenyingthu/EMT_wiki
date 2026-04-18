---
title: "Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Equivalent Circuits"
type: source
authors: ['Claudio Saldaña']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108432. doi:10.1016/j.epsr.2022.108432"
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient implementation of multi-port frequency dependent network equivalents for electromagnetic t_Saldaña和Calzolari_2022.pdf"]
---

# Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Equivalent Circuits

**作者**: Claudio Saldaña
**年份**: 2022
**来源**: `15/Efficient implementation of multi-port frequency dependent network equivalents for electromagnetic t_Saldaña和Calzolari_2022.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Power system electromagnetic transient studies require that a small part of the electrical network be modelled in detail. The rest of the system is represented by a network equivalent taking into account the frequency depen­

## 核心贡献


- 提出基于诺顿等效电路的高阶有理模型实现方法，显著减少导纳支路数量
- 开发动态更新JMARTI线路模型模态变换矩阵的频率扫描方法，消除近似误差
- 将有理函数部分分式直接转化为时域微分方程并梯形积分，避免复极点特殊处理


## 使用的方法


- [[矩阵拟合-矢量拟合|矩阵拟合/矢量拟合]]
- [[诺顿等效电路|诺顿等效电路]]
- [[梯形积分法|梯形积分法]]
- [[谐波频率扫描-hfs|谐波频率扫描(HFS)]]
- [[有理函数极点-留数逼近|有理函数极点-留数逼近]]
- [[多端π型等值电路综合|多端π型等值电路综合]]


## 涉及的模型


- [[同步发电机次暂态阻抗模型|同步发电机次暂态阻抗模型]]
- [[变压器漏抗模型|变压器漏抗模型]]
- [[r-l串联负荷模型|R-L串联负荷模型]]
- [[jmarti频变输电线路模型|JMARTI频变输电线路模型]]
- [[fdne-model|FDNE]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变网络等值|频变网络等值]]
- [[频率相关建模|频率相关建模]]
- [[网络等值与降阶|网络等值与降阶]]
- [[开关暂态分析|开关暂态分析]]
- [[emtp程序二次开发|EMTP程序二次开发]]


## 主要发现


- 在500kV系统开关暂态仿真中，该等值模型能高精度复现外部网络动态响应
- 相比完整系统模型与传统电路拟合方法，该实现方案显著降低了计算处理时间
- 无需特殊处理复极点即可保证模型无源性，简化了EMTP程序实现流程



## 方法细节

### 方法概述

本文提出一种基于诺顿等效电路的高阶有理函数实现方法，用于构建多端口频变网络等值(FDNE)。首先通过EMTP-ATP的谐波频率扫描(HFS)获取外部系统的频域导纳矩阵$Y(\omega)$，并创新性地动态更新JMARTI线路模型的模态变换矩阵参数(FREQTRAN)以消除固定频率近似误差。随后利用矢量拟合(Matrix Fitting Toolbox)将$Y(\omega)$各元素拟合为极点-留数形式的有理函数并强制保证无源性。基于导纳矩阵的对称性将其综合为多端$\pi$型等值电路，将每个支路的有理函数部分分式直接转换为时域微分方程。应用梯形积分法则离散化，得到并联电导与历史电流源组合的诺顿等效电路。该方法通过引入辅助状态变量将复极点对应的二阶微分方程降阶为一阶系统，无需对复极点进行特殊处理，显著减少了导纳支路数量，并通过MODELS本地模型、TACS Type-69设备及MODELS外部子模型三种方式在EMTP-ATP中实现自动化代码生成与集成。

### 数学公式


**公式1**: $$$y_{ii,\pi} = \sum_{j=1}^N Y_{ij,fit}, \quad y_{ij,\pi} = -Y_{ij,fit}$$$

*多端$\pi$型等值电路支路导纳计算公式，利用拟合后的导纳矩阵元素合成自导纳与互导纳*


**公式2**: $$$I(s) = \left( \sum_k \frac{a_k}{s - c_k} \right) V(s)$$$

*频域中支路电流与电压的极点-留数有理函数关系式*


**公式3**: $$$I_i(t) = \text{hist}_i(t-\Delta t) + G_i V(t)$$$

*实极点部分分式经梯形积分离散化后的时域诺顿等效形式*


**公式4**: $$$\frac{d^2 I_j(t)}{dt^2} + P\frac{dI_j(t)}{dt} + QI_j(t) = M\frac{dV(t)}{dt} + NV(t)$$$

*共轭复极点对应的二阶时域微分方程*


**公式5**: $$$I_j(t) = \text{hist}_j(t-\Delta t) + G_j V(t)$$$

*复极点降阶为一阶系统后离散化的诺顿等效形式，包含历史项与等效电导*


### 算法步骤

1. 1. 频域导纳矩阵获取：利用EMTP-ATP的HFS模块，在边界母线逐相注入1V单相电压源，其余相接地，逐列计算外部系统的频域导纳矩阵$Y(\omega)$。

2. 2. JMARTI模型动态更新：编写Fortran 2003程序，在频率扫描过程中动态修改JMARTI SETUP的FREQTRAN参数，使模态变换矩阵在每个扫描频率点重新计算，消除固定模态矩阵引入的近似误差。

3. 3. 矢量拟合与无源性处理：调用MATLAB Matrix Fitting Toolbox的VFdriver.m和RPdriver.m，将$Y(\omega)$各元素拟合为极点-留数形式，并通过无源性校正算法确保拟合矩阵$Y_{fit}(\omega)$物理可实现。

4. 4. $\pi$型电路综合：利用导纳矩阵对称性，根据公式$y_{ii,\pi} = \sum Y_{ij,fit}$和$y_{ij,\pi} = -Y_{ij,fit}$将矩阵元素映射为多端$\pi$型等值电路的各支路导纳。

5. 5. 时域微分方程转换：将每个支路导纳的部分分式转换为拉普拉斯域表达式，实极点直接对应一阶ODE；共轭复极点合并为二阶ODE，并引入辅助变量$X_j(t)$将其降阶为一阶状态方程组。

6. 6. 梯形积分离散化：对一阶ODE应用梯形积分法则($h=\Delta t/2$)，推导出各极点对应的并联等效电导$G$和历史电流源$\text{hist}(t-\Delta t)$的递推计算公式。

7. 7. 诺顿等效合成与代码生成：将所有实极点和复极点的电导与历史项分别求和，得到支路总诺顿等效$I(t) = \text{hist}_T(t-\Delta t) + G_T V(t)$。编写Fortran程序自动生成MODELS语言或Type-69 Fortran代码，并输出符合EMTP-ATP格式的导纳数据文件。

8. 8. EMTP-ATP集成：通过$INCLUDE命令将生成的模型代码和电导参数嵌入仿真算例，在INIT阶段初始化状态变量，在EXEC阶段每个时间步更新历史电流源并输出至Type-60受控源。


### 关键参数

- **frequency_range**: [5.0, 5000.0] Hz

- **poles_per_element**: 4个实极点 + 102对共轭复极点

- **time_step**: 1.0 μs

- **simulation_duration_line**: 300 ms

- **simulation_duration_transformer**: 1.0 s

- **boundary_bus_dimension**: 三相母线，6×6导纳矩阵

- **integration_method**: 梯形积分法 (Trapezoidal Rule)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 500 kV输电线路空载合闸 | 线路长123.9 km，末端接50 MVAr并联电抗器。三相断路器按相电压峰值时刻依次闭合。FDNE三种实现方式计算的末端C相电压暂态波形与完整系统模型(FSR)高度重合，最大幅值偏差可忽略。 | Type-69设备实现耗时仅为FSR的38%，外部子模型为45.7%，而MODELS本地模型耗时为FSR的56倍。 |

| 425/425/140 MVA单相变压器组励磁涌流 | 考虑铁芯磁滞特性(Type-96非线性元件)及±100%、0%剩磁。A相电压过零时刻三相同时合闸。FDNE计算的A相涌流波形与FSR一致，但因FDNE准确计及了线路模态矩阵的频变特性，涌流衰减速度略快于使用固定模态矩阵的FSR。 | Type-69设备实现耗时仅为FSR的29%，外部子模型为35.4%，MODELS本地模型耗时为FSR的54倍。 |



## 量化发现

- 导纳矩阵拟合最大绝对误差为$8.805 \times 10^{-5}$ mho，在5~5000 Hz频段内实现极高精度逼近。
- Type-69设备实现方案在变压器合闸仿真中计算耗时仅为完整系统模型(FSR)的29%，计算效率提升约3.45倍。
- 外部子模型(Foreign Submodel)实现方案在线路合闸仿真中计算耗时为FSR的45.7%，效率提升约2.19倍。
- MODELS本地模型因解释型执行开销，计算耗时高达FSR的54~56倍，不适用于大规模极点模型。
- 离散换位线路模型与连续换位模型对比表明，全对称假设会导致高频段导纳矩阵响应失真，必须采用相坐标逐列扫描。
- FDNE实现无需特殊处理复极点，通过状态变量降阶将二阶ODE转化为一阶系统，单支路仅需计算1个等效电导，大幅降低节点导纳矩阵规模。


## 关键公式

### 支路总诺顿等效时域方程

$$$I(t) = \text{hist}_T(t-\Delta t) + G_T V(t)$$$

*用于EMTP-ATP每个时间步的节点电压求解，将频变导纳转化为固定电导与历史电流源的并联组合*

### 实极点离散化参数计算

$$$G_i = \frac{h a_i}{1 - h c_i}, \quad \text{hist}_i(t-\Delta t) = \frac{(1+h c_i)I_i(t-\Delta t) + h a_i V(t-\Delta t)}{1 - h c_i}$$$

*梯形积分离散化后，用于更新实极点对应的并联电导和历史电流源递推值*

### 复极点降阶离散化参数计算

$$$G_j = \frac{h(M+\beta_3)}{1-h\beta_2}, \quad \beta_1 = \frac{1-hP}{1+hP}, \beta_2 = \frac{-hQ}{1+hP}, \beta_3 = \frac{h(N-MP)}{1+hP}$$$

*处理共轭复极点时，通过引入辅助状态变量避免复数运算，直接计算实数电导与历史项系数*



## 验证详情

- **验证方式**: 全系统详细模型(FSR)与三种FDNE实现方案的时域波形对比分析，包含电压暂态、励磁涌流及CPU运行时间统计
- **测试系统**: 乌拉圭国家电网500 kV辐射状输电系统，以BUS5为边界节点，外部区域包含水电厂、火电厂、多组自耦变压器及长距离换位线路
- **仿真工具**: EMTP-ATP (HFS模块、MODELS语言、TACS Type-69设备)、MATLAB (Matrix Fitting Toolbox)、Fortran 2003/77 (自动化代码生成)
- **验证结果**: FDNE在5~5000 Hz频段内导纳拟合误差低于$10^{-4}$ mho，时域暂态波形与完整系统高度一致。Type-69与外部子模型实现方案在保证精度的前提下，将计算时间压缩至完整系统的29%~46%，验证了基于诺顿等效的高阶有理函数实现方法在工程级EMT仿真中的高效性与实用性。
