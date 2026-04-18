---
title: "Shifted frequency analysis-EMTP multirate simulation of power systems"
type: source
authors: ['J.O. Tarazona']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107292. doi:10.1016/j.epsr.2021.107292"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/34/j.epsr.2021.107292.pdf.pdf"]
---

# Shifted frequency analysis-EMTP multirate simulation of power systems

**作者**: J.O. Tarazona
**年份**: 2021
**来源**: `34/j.epsr.2021.107292.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Shifted frequency analysis-EMTP multirate simulation of power systems J.O. Tarazona a,*, A.T.J. Martí a, J.R. Martí a, F.A. Moreira b a Electrical and Computer Engineering Department, University of British Columbia, Vancouver, British Columbia V6T 1Z4, Canada b Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, Bahia 40210-630, Brazil

## 核心贡献

- 采用多速率方法对不同子系统采用不同时间步长，提高仿真效率
- 应用动态相量法进行宽频暂态分析，兼顾计算效率和精度

## 使用的方法

- [[multirate-method]]

## 涉及的模型

- [[ieee-39节点系统|IEEE 39节点系统]]

## 相关主题

- [[dynamic-phasor]]

## 主要发现

0378-7796/© 2021 Elsevier B

## 方法细节

### 方法概述

本文提出了一种基于多区域戴维南等效（MATE）概念框架的新型混合多速率协议，用于接口移频分析（SFA）仿真器和电磁暂态（EMT）仿真器。核心创新在于使用第二个并行的EMT仿真器（虚部EMT）来跟踪SFA仿真器复值解的虚部，与实部EMT仿真器并行运行。这种双EMT结构（Real-Part EMT和Imaginary-Part EMT）保持了SFA/EMT混合仿真器的解析性和同步性，使SFA解能够使用大时间步长捕捉基频（50/60Hz）周围的机电暂态包络，而EMT解使用小时间步长处理快速暂态。通过SFA变换可直接从EMT解中提取基频相量，避免了传统混合仿真中的延迟问题。

### 数学公式


**公式1**: $$$u(t) = u_I(t)\cos\omega_0 t - u_Q(t)\sin\omega_0 t$$$

*带通信号表示，将系统信号分解为同相分量u_I(t)和正交分量u_Q(t)，中心频率为系统基频ω0*


**公式2**: $$$U(t) = u_I(t) + ju_Q(t)$$$

*动态相量（时变相量）定义，为复值低通信号，表示原信号的复包络*


**公式3**: $$$z(t) = u(t) + jH[u(t)]$$$

*解析信号定义，通过Hilbert变换H[·]构造，用于建立与动态相量的关系*


**公式4**: $$$z(t) = U(t)e^{j\omega_0 t}$$$

*解析信号与动态相量的转换关系，表明动态相量是解析信号乘以e^{-jω0t}的结果*


**公式5**: $$$z_m(t) = e^{-j\omega_0 t}z(t) = T^{-1}z(t)$$$

*SFA变换公式，将频谱左移ω0，使基频分量移至零频，允许使用大步长仿真*


**公式6**: $$$I_L = Z_T^{-1}E_L$$$

*MATE框架中的支路电流求解，基于各子系统的戴维南等效电压E_L和等效阻抗矩阵Z_T*


**公式7**: $$$V_j = e_j - Y_j^{-1}C_jI_L$$$

*MATE框架中的子系统节点电压求解，e_j为子系统戴维南电压，Y_j为节点导纳矩阵，C_j为连接矩阵*


### 算法步骤

1. 对每个子系统计算其戴维南等效电压e_j和等效阻抗，建立多端口戴维南等效电路

2. 求解连接各子系统的支路（link）电流：利用所有子系统的戴维南电压计算支路电流I_L = Z_T^{-1}E_L，其中Z_T为整个系统的戴维南阻抗矩阵

3. 将求得的支路电流I_L注入各子系统，求解各子系统的节点电压：V_j = e_j - Y_j^{-1}C_jI_L，其中C_j为描述支路与子系统连接关系的关联矩阵

4. 在每个EMT时间步内，通过插值获取SFA解的值，实现无延迟的直接耦合，保证数值稳定性

5. 并行运行实部EMT仿真和虚部EMT仿真，分别跟踪SFA复值解的实部和虚部，保持复数解的解析性

6. 通过SFA逆变换将复值解转换回时域实信号，提取实部作为最终输出


### 关键参数

- **ω0**: 系统基频（50/60 Hz），SFA变换的中心频率

- **Δt_SFA**: SFA仿真器使用的大时间步长，适用于捕捉机电暂态（通常毫秒级）

- **Δt_EMT**: EMT仿真器使用的小时间步长，适用于快速电磁暂态（通常微秒级）

- **U(t)**: 复值动态相量，包含时变幅值和相角信息

- **Z_T**: MATE框架中的多端口戴维南等效阻抗矩阵

- **E_L**: 连接支路两端的戴维南电压差向量



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统机电暂态仿真 | 在IEEE 39节点系统上验证SFA-EMT混合仿真器的准确性，SFA部分捕捉机电暂态（摇摆曲线），EMT部分提供详细的电磁暂态精度。结果显示SFA仿真器能准确捕捉机电暂态，EMT仿真器能达到与纯EMT相当的精度。 | 相比全EMT解，所提出的混合仿真器在保持EMT级精度的同时实现了相当大的计算节省（considerable savings），允许SFA和EMT使用显著不同的时间步长 |

| 基频相量提取验证 | 通过SFA变换直接从EMT解中提取基频相量，无需传统的傅里叶变换或锁相环，验证了在存在谐波和次谐波谐振情况下仍能准确提取基频分量 | 与传统TS-EMT混合方法相比，避免了TS时间步延迟导致的精度问题，无需迭代即可实现同步 |



## 量化发现

- SFA变换将信号频谱移动ω0（50/60 Hz），使基频分量移至零频，从而允许使用比传统EMT大得多的时间步长（从微秒级提升到毫秒级）
- 混合仿真器支持SFA和EMT使用显著不同的时间步长（significantly different solution steps），实现多速率仿真
- 通过MATE框架，SFA子系统表示为多端口戴维南等效，可捕捉由SFA时间步决定的频率范围内的频率响应
- 采用固定时间步长的梯形法或后向欧拉法离散化，保证绝对数值稳定性
- 虚部EMT仿真器与实部EMT仿真器并行运行，维持复值解的解析性（analyticity）


## 关键公式

### SFA变换（移频变换）

$$$z_m(t) = e^{-j\omega_0 t}z(t)$$$

*将时域实信号转换为复值低通信号，使基频分量移至零频，允许使用大步长仿真机电暂态*

### 动态相量定义

$$$U(t) = u_I(t) + ju_Q(t)$$$

*表示信号的复包络，包含时变幅值和相角，是SFA域的求解变量*

### MATE支路电流求解

$$$I_L = Z_T^{-1}E_L$$$

*在接口算法中用于求解连接SFA和EMT子系统的边界电流，实现子系统间的高效解耦和并行求解*



## 验证详情

- **验证方式**: 仿真验证与对比分析
- **测试系统**: IEEE 39节点标准测试系统（New England Test System），包含39个母线、10台发电机和19个负荷
- **仿真工具**: 基于EMTP原理的SFA仿真器和EMT仿真器，使用复数运算和MATE（Multi-Area Thévenin Equivalent）求解框架
- **验证结果**: 在IEEE 39节点系统上的验证表明，所提出的协议在捕捉机电暂态方面具有很高的精度，在EMT仿真中达到了与纯EMT相当的精度。通过使用显著不同的时间步长，相比全EMT解实现了相当大的计算节省，特别适用于需要详细建模部分设备的暂态稳定性研究。
