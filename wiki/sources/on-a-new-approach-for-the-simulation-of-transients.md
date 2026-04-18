---
title: "On a new approach for the simulation of transients"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/29/j.epsr.2006.08.027.pdf.pdf"]
---

# On a new approach for the simulation of transients

**作者**: 
**年份**: 2007
**来源**: `29/j.epsr.2006.08.027.pdf.pdf`

## 摘要

This paper presents a new simulation tool named EMTP-RV. EMTP-RV is a completely new program with a new graphical user interface and a new computational engine. The simulation uses a new matrix formulation for computing load-ﬂow, steady state and time-domain solutions. Theoretical advantages are emphasized and demonstrated through practical examples. An open-architecture graphical user interface (GUI) is developed to maximize ﬂexibility and allow creating and maintaining complex designs. © 2006 Elsevier B.V. All rights reserved. Keywords: Simulation tools; Numerical methods; EMTP 1. Introduction Since its initial concept presented in 1969 [1] the basic EMTP type simulation approach remained unchanged. It is used in var- ious commercial (DCG-EMTP Version 3, EMTP-V3 [2]) and non-commercial p

## 核心贡献


- 提出改进的增广节点分析法，统一处理理想开关与变压器，避免矩阵秩变问题
- 基于牛顿法构建雅可比矩阵，实现非线性设备与电机模型的真正同步迭代求解
- 重构底层计算引擎与开放式GUI架构，彻底摆脱传统Fortran代码限制


## 使用的方法


- [[增广节点分析法|增广节点分析法]]
- [[牛顿迭代法|牛顿迭代法]]
- [[梯形积分法|梯形积分法]]
- [[谐波稳态求解|谐波稳态求解]]
- [[潮流计算|潮流计算]]


## 涉及的模型


- [[理想电压源|理想电压源]]
- [[理想变压器|理想变压器]]
- [[理想开关|理想开关]]
- [[电机模型|电机模型]]
- [[非线性设备|非线性设备]]
- [[控制系统|控制系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值计算方法|数值计算方法]]
- [[仿真软件架构|仿真软件架构]]
- [[网络方程求解|网络方程求解]]
- [[稳态初始化|稳态初始化]]


## 主要发现


- 固定秩矩阵公式使开关切换无需重构网络，大幅降低高频开关场景的计算开销
- 雅可比求解法彻底消除控制反馈回路数值延迟，提升非线性暂态仿真精度
- 新架构成功实现潮流、稳态与时域求解的统一矩阵表达，验证了算法通用性



## 方法细节

### 方法概述

本文提出基于改进增广节点分析法（Modified-Augmented-Nodal Analysis, MANA）的统一仿真框架，彻底重构EMTP类仿真引擎。核心创新包括：(1)采用固定秩（fixed-rank）矩阵 formulation，通过增广矩阵统一处理理想电压源、理想变压器和理想开关，避免传统节点分析法中开关操作导致的矩阵维度变化和重构；(2)基于牛顿-拉夫逊迭代法构建雅可比矩阵，实现非线性设备与电机模型的真正同步（simultaneous）迭代求解，消除伪非线性近似；(3)将潮流计算、谐波稳态求解和时域暂态求解整合为统一的矩阵方程体系，通过复数变量转换实现不同求解模式的兼容；(4)采用面向对象编程范式（Fortran-95/C++），实现自动内存管理和设备模型封装。

### 数学公式


**公式1**: $$$Yv = i$$$

*传统标准节点分析方程，其中Y为导纳矩阵，v为未知电压向量，i为电流源与历史电流源组合向量。局限性在于要求所有元件必须具有导纳矩阵模型，无法直接处理理想变压器和未接地电压源。*


**公式2**: $$$\begin{bmatrix} Y_n & V_c & D_c & S_c \\ V_r & V_d & D_{DV} & S_{VS} \\ D_r & D_{DV}^T & D_d & S_{DS} \\ S_r & S_{SV} & S_{SD} & S_d \end{bmatrix} \begin{bmatrix} v_n \\ i_V \\ i_D \\ i_S \end{bmatrix} = \begin{bmatrix} i_n \\ v_b \\ d_b \\ s_b \end{bmatrix}$$$

*改进的增广节点分析方程（公式2）。子矩阵含义：Yn为网络导纳子矩阵；Vc/Vr处理电压源（vk-vm=vbkm）；Dc/Dr处理理想变压器（vk-vm-gvi+gvj=0）；Sc/Sr处理理想开关（闭合时vk-vm=0，开路时电流为零）；Vd/Dd/Sd为对应约束的对角子矩阵。该矩阵保持固定秩，开关状态变化仅需修改对应元素而无需重构矩阵。*


**公式3**: $$$\begin{bmatrix} A & A_I \\ L_{LA} & L_d \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta x_{LF} \end{bmatrix} = F = 0$$$

*统一潮流求解方程（公式3）。A为线性网络矩阵（即公式2的左侧矩阵），AI为负荷潮流设备连接矩阵，LLA和Ld提供负荷潮流约束方程。未知向量Δx包含网络变量[Δvn ΔiV ΔiD ΔiS]^T，ΔxLF包含负荷电流和内部电压[I_L I_PQ I_PV I_SL E_PQ E_PV E_SL]^T。该 formulation 自动包含频变传输线等非经典潮流设备，无需单独的雅可比矩阵推导。*


**公式4**: $$$v_k - v_m - g v_i + g v_j = 0$$$

*理想变压器方程，变比为g，一次侧节点为i-j，二次侧节点为k-m。通过子矩阵Dr和Dc直接嵌入主系统，无需引入泄漏电抗或理想化近似。*


**公式5**: $$$v_k - v_m - R i_{km} = v_{dc}$$$

*带电阻和固定压降的开关模型（如二极管），其中R为导通电阻，vdc为阈值电压。通过子矩阵Sr、Sd和sb实现。*


### 算法步骤

1. 构建固定秩增广节点矩阵A：根据网络拓扑，将导纳矩阵Yn、电压源约束(Vc,Vr)、变压器约束(Dc,Dr)和开关约束(Sc,Sr)按公式2的分块结构组装，保持矩阵维度在整个仿真过程中恒定。

2. 非线性设备线性化：在每个时间步长或迭代步骤，对非线性设备（如电机、饱和变压器）在当前工作点进行线性化，将结果贡献到矩阵A的相应位置，使A成为牛顿-拉夫逊迭代的雅可比矩阵。

3. 开关状态处理：当理想开关状态改变时，仅修改子矩阵Sd的对角元素（开路时设为1强制电流为零）或Sr/Sc的约束行（闭合时强制电压差为零），保持矩阵稀疏结构和维度不变，避免LU分解符号重分析。

4. 同步迭代求解：对于含控制系统的非线性网络，采用牛顿法同步求解网络方程与控制系统方程（通过雅可比矩阵扩展），消除传统方法中控制回路的数值延迟（numerical delays）。

5. 稳态初始化：将时域方程转换为复数频域形式，所有变量变为相量，设备提供频域等效模型，使用相同的增广矩阵结构求解谐波稳态。

6. 潮流初始化：追加负荷潮流约束方程（PQ、PV、松弛节点），形成扩展方程组（公式3），通过牛顿法求解得到精确初始条件，为时域仿真提供零自然响应启动。

7. 面向对象数据管理：通过封装设备对象管理数据和求解方法，实现自动内存分配和基于Web页面的数据输入，支持JavaScript脚本化设备建模和绘图。


### 关键参数

- **矩阵秩特性**: 固定秩（Fixed rank），与开关状态无关

- **求解器类型**: 牛顿-拉夫逊迭代（Newton-Raphson）用于非线性系统

- **积分方法**: 梯形积分法（Trapezoidal integration）用于历史电流源计算

- **编程语言**: Fortran-95（计算核心），C/C++（GUI），JavaScript（脚本）

- **开关模型**: 理想开关（R=0闭合，R=∞开路）或带电阻/压降的实用开关模型

- **变压器模型**: 理想变压器（无漏抗，无损耗）通过代数约束方程实现



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 高频开关操作场景（理论分析） | 在包含大量电力电子开关的系统中，传统EMTP方法因开关操作导致矩阵秩变化（variable rank），需频繁进行符号LU分解。本文方法保持矩阵固定秩，开关状态变化仅需修改矩阵元素值而非结构。 | 计算复杂度从传统方法的O(n³)（每次开关动作需重新符号分解）降为O(n)或O(n²)（仅需数值更新和迭代求解），特别适用于开关频率高的场景。 |

| 非线性控制系统仿真 | 采用雅可比矩阵统一求解网络和控制系统方程，消除了传统块迭代方法中控制信号通过非线性反馈回路时的数值延迟。 | 实现了真正的同步（simultaneous）解，相比传统补偿法（compensation method）的伪非线性近似，精度显著提升，且不受拓扑限制。 |

| 变电站和风电场可视化设计 | 通过EMTPWorks GUI构建包含多级子电路（subcircuits）的变电站模型和风电场模型，使用符号编辑器（Symbol Editor）创建与实际变电站外观一致的图形组件。 | 支持无层级限制的子电路嵌套和JavaScript脚本自动绘图，相比传统EMTP-V3的固定图形界面，复杂系统设计效率显著提升。 |



## 量化发现

- 矩阵维度恒定性：采用增广节点分析法后，系统矩阵秩在开关开合过程中保持不变（fixed rank），避免了传统方法中关闭开关导致矩阵列和行被消除、打开开关需恢复矩阵结构的计算开销。
- 非线性求解精度：通过将矩阵A作为雅可比矩阵进行牛顿迭代，实现了非线性设备（包括电机模型）的真正同步求解，消除了传统补偿法（compensation method）的拓扑限制和精度损失。
- 计算内存管理：基于Fortran-95的面向对象设计实现自动内存分配（automatic memory allocation），支持极大规模算例和极小步长（very small time-steps）的传输线模型仿真，克服了Fortran-77的静态内存限制。
- 潮流求解通用性：扩展的雅可比矩阵 formulation（公式3）可自动容纳频变传输线（frequency-dependent transmission lines）等非经典潮流设备，无需像传统方法[9]那样为网络模型进行繁琐的雅可比矩阵推导。
- 控制回路延迟消除：通过雅可比矩阵 formulation 求解控制系统方程，完全消除了非线性反馈回路中的数值延迟（numerical delays），实现了控制与网络方程的严格同步求解。


## 关键公式

### 改进增广节点分析方程（MANA）

$$$\begin{bmatrix} Y_n & V_c & D_c & S_c \\ V_r & V_d & D_{DV} & S_{VS} \\ D_r & D_{DV}^T & D_d & S_{DS} \\ S_r & S_{SV} & S_{SD} & S_d \end{bmatrix} \begin{bmatrix} v_n \\ i_V \\ i_D \\ i_S \end{bmatrix} = \begin{bmatrix} i_n \\ v_b \\ d_b \\ s_b \end{bmatrix}$$$

*用于时域暂态仿真、稳态初始化和谐波分析的统一网络求解，支持理想变压器、理想开关和电压源的直接建模而无需等效电路近似。*

### 统一潮流求解方程

$$$\begin{bmatrix} A & A_I \\ L_{LA} & L_d \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta x_{LF} \end{bmatrix} = F = 0$$$

*用于多相潮流计算，将负荷潮流约束方程（PQ、PV、松弛节点）与网络方程联立求解，提供精确的时域仿真初始条件。*



## 验证详情

- **验证方式**: 理论优势通过实际算例演示（demonstrated through practical examples），包括变电站详细模型和风电场研究。
- **测试系统**: (1) 包含理想变压器和复杂开关配置的变电站系统（使用Symbol Editor创建自定义图形）；(2) 风电场研究案例，包含风力发电机控制电路、风效应模型、静止补偿器（Statcom）和负荷的多级子电路（multilevel subcircuits）封装。
- **仿真工具**: EMTP-RV（本文提出的新仿真工具，完全重新编写，无EMTP-V3遗留代码），图形界面为EMTPWorks（基于Microsoft Foundation Class库和C/C++开发）。
- **验证结果**: 验证了固定秩矩阵formulation在处理理想开关和变压器时的理论优势，证实了非线性设备同步求解消除了数值延迟，展示了开放式GUI在处理极大规模网络和复杂分层设计中的灵活性。未提供与传统工具（如EMTP-V3或PSCAD/EMTDC）的定量速度或精度对比数据。
