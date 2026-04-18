---
title: "Time Domain Transformation Method"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/tpwrs.2012.2188913.pdf.pdf"]
---

# Time Domain Transformation Method

**作者**: 
**年份**: 2012
**来源**: `37/tpwrs.2012.2188913.pdf.pdf`

## 摘要

—Electromagnetic Transients Program (EMTP) is widely used in power system dynamics studies. However, in most cases EMTP is found inadequate for dealing with the realistic size power systems due to the small time step resulting in relatively slow simulation speeds. To accelerate the EMTP simulations of power system dynamics, a novel frequency-adaptive methodology is proposed. In this method, a new transformation is presented. The properties of the transformation and the numerical solutions based on the transformation are discussed. The component models obtained by discretizing the differential equations at the branch level are also given which are convenient for EMTP implementa- tion. The proposed method allows using large time steps without sacriﬁcing accuracy, which greatly improves the s

## 核心贡献



- 提出一种新型频域自适应时域变换方法以加速EMTP仿真
- 允许在不牺牲精度的情况下使用大时间步长，显著提升大规模电力系统动态仿真速度
- 提供支路级离散化的元件伴随模型，便于在EMTP中直接实现

## 使用的方法


- [[dynamic-phasor]]
- [[numerical-integration]]
- [[nodal-analysis]]
- [[co-simulation]]
- [[parallel]]

## 涉及的模型


- [[fdne]]
- [[network-equivalent]]

## 相关主题


- [[real-time]]
- [[harmonic]]
- [[frequency-dependent]]

## 主要发现



- 所提变换方法可在保持宽频动态特性精度的前提下显著增大仿真步长
- 该方法有效克服了传统EMTP因小步长导致的计算缓慢问题，大幅提升了仿真效率
- 支路级离散化模型具有良好的EMTP兼容性，并通过多种算例验证了其有效性与实用性

## 方法细节

### 方法概述

本文提出了一种频域自适应的时域变换方法（Time Domain Transformation Method），通过引入旋转变换将原系统中的高频交流载波信号转换为低频慢变信号，从而允许在EMTP仿真中使用更大的时间步长。该方法首先定义了一个从原始x-y坐标系到变换后u-v坐标系的旋转变换，其中变换矩阵随时间以系统基频旋转。在变换后的坐标系中，原本围绕基频变化的信号转换为围绕直流（0 Hz）变化的慢信号。基于此，构建了"微分扩展网络"（Differentially Extended Network）的概念，即将原始网络与其微分网络并联，通过在支路级别离散化微分方程，得到适用于EMTP的伴随模型。数值积分采用梯形法（Trapezoidal Rule, TR）在变换域进行，再通过逆变换得到原始时域的瞬时波形。

### 数学公式


**公式1**: $$$\begin{bmatrix} u \\ v \end{bmatrix} = T \begin{bmatrix} x \\ y \end{bmatrix}$$$

*核心时域变换公式，将原始信号(x,y)通过旋转矩阵T变换为慢变信号(u,v)，降低信号变化速率*


**公式2**: $$$T = \begin{bmatrix} \cos(\omega_s t) & -\sin(\omega_s t) \\ \sin(\omega_s t) & \cos(\omega_s t) \end{bmatrix}$$$

*旋转变换矩阵，其中$\omega_s$为移频参数（通常等于基频），实现坐标系的旋转以消除基频分量*


**公式3**: $$$\begin{bmatrix} \dot{u} \\ \dot{v} \end{bmatrix} = \omega_s \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix} + T \begin{bmatrix} \dot{x} \\ \dot{y} \end{bmatrix}$$$

*变换后变量(u,v)与原变量(x,y)微分关系，用于构建微分扩展网络的支路方程*


**公式4**: $$$\begin{bmatrix} x(t) \\ y(t) \end{bmatrix} = \frac{2}{h} T^{-1}(t) \left( \begin{bmatrix} u(t) \\ v(t) \end{bmatrix} - \begin{bmatrix} u(t-h) \\ v(t-h) \end{bmatrix} \right) - T^{-1}(t) \begin{bmatrix} u(t-h) \\ v(t-h) \end{bmatrix}$$$

*基于梯形法的离散化公式，h为时间步长，实现从变换域到原时域的数值求解*


**公式5**: $$$G_{eq} = \frac{2}{h} L^{-1}, \quad R_{eq} = R - \omega_s L$$$

*等效电路参数，其中电导$G_{eq}$和等效电阻$R_{eq}$考虑了变换引入的耦合项和离散化效应*


**公式6**: $$$I_{h}(t) = I_{h}(t-h) + \frac{2}{h} L^{-1} [u(t-h), v(t-h)]^T$$$

*电感支路的历史电流更新公式，用于伴随模型中的历史电流源计算*


### 算法步骤

1. 初始化：设定移频参数$\omega_s$（通常取基频50/60 Hz），设定大步长h（可比传统EMTP大数十至数千倍），构建原始网络的节点导纳矩阵

2. 构建微分扩展网络：对原始网络中的每个支路（R、L、C）构建对应的微分网络，其中微分网络的参数与原网络相同，形成并联结构

3. 坐标变换：在每个时间步长，根据当前时刻t计算变换矩阵$T(t)$和$T^{-1}(t)$，将上一时刻的解从x-y坐标系变换到u-v坐标系

4. 离散化求解：在u-v坐标系中，使用梯形法(TR)对支路微分方程进行离散化，计算等效电导$G_{eq}$和历史电流源$I_h$，形成节点电压方程$Y_{bus}V = I$

5. 求解节点电压：求解变换域中的节点电压$[u(t), v(t)]^T$，得到当前时刻变换域的解

6. 反变换：通过逆变换矩阵$T^{-1}(t)$将解从u-v坐标系转换回x-y坐标系，得到原始时域的瞬时电压和电流值$[x(t), y(t)]^T$

7. 更新历史项：根据当前解更新各支路的历史电流源，准备下一时间步长的计算

8. 输出与存储：记录原始时域的瞬时波形（EMT结果）和变换域的慢变包络（相量信息），推进时间步长并重复步骤3-8直至仿真结束


### 关键参数

- **$\omega_s$**: 移频参数（Shift Frequency），通常设置为系统基频（50 Hz或60 Hz），决定坐标系旋转速度

- **$h$**: 仿真时间步长，可比传统EMTP方法增大数十倍、数百倍甚至数千倍而不损失精度

- **$T$**: 时变旋转变换矩阵，元素为$\cos(\omega_s t)$和$\sin(\omega_s t)$，实现Park变换类似的坐标旋转

- **$u, v$**: 变换域中的慢变信号（d-q轴类似量），变化速率远低于原始信号

- **$x, y$**: 原始时域中的瞬时量（类似$\alpha-\beta$坐标系或三相瞬时值的分量）

- **$G_{eq}$**: 离散化后的等效电导，值为$2L/h$（电感支路）或$h/2C$（电容支路）

- **$R_{eq}$**: 等效电阻，原电阻R减去耦合项$\omega_s L$（感性支路）或加上$\omega_s L$（容性支路）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| RLC串联电路暂态仿真 | 对图3所示RLC串联电路进行仿真，自然角频率$\omega_0$由电路参数决定。该方法使用大步长成功捕捉了指数衰减的正弦信号，与理论解对比显示良好的一致性 | 相比传统EMTP需要极小步长（通常<100 μs）来捕捉基频（50/60 Hz）波形，所提方法允许使用毫秒级步长，仿真速度提升数十至数百倍，同时保持幅值和相位精度 |

| 大规模电力系统动态仿真 | 开发了通用仿真程序对实际规模电力系统进行验证，系统包含FACTS和HVDC等电力电子设备，仿真了机电暂态过程 | 实现了与暂态稳定（TS）程序相当的计算速度，同时保留了EMTP程序的详细设备级建模能力，克服了传统EMTP因小步长导致的计算缓慢问题 |



## 量化发现

- 时间步长可增大数十倍、数百倍甚至数千倍（tens, hundreds, or even thousands times）而不牺牲精度
- 方法同时提供EMT仿真器的瞬时波形信息和TS仿真器的相量信息
- 通过支路级离散化得到的伴随模型可直接集成到现有EMTP框架中，保持良好的兼容性
- 变换后的信号u和v为慢变信号，其变化速率远低于原始信号x和y，使得数值积分允许使用大步长
- 等效电路参数中，电感支路的等效电阻$R_{eq} = R - \omega_s L$体现了移频引入的耦合效应补偿


## 关键公式

### 时域旋转变换（Time Domain Transformation）

$$$\begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} \cos(\omega_s t) & -\sin(\omega_s t) \\ \sin(\omega_s t) & \cos(\omega_s t) \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$$

*将原始时域信号(x,y)变换为慢变信号(u,v)，是方法的核心数学基础，允许后续使用大步长积分*

### 梯形法离散化逆变换公式

$$$\begin{bmatrix} x(t) \\ y(t) \end{bmatrix} = \frac{2}{h} T^{-1}(t) \left( \begin{bmatrix} u(t) \\ v(t) \end{bmatrix} - \begin{bmatrix} u(t-h) \\ v(t-h) \end{bmatrix} \right) - T^{-1}(t) \begin{bmatrix} u(t-h) \\ v(t-h) \end{bmatrix}$$$

*在变换域使用梯形法积分后，通过此公式将结果转换回原时域，用于EMTP实现*

### 支路伴随模型（电感支路）

$$$G_{eq} = \frac{2}{h}L^{-1}, \quad I_h(t) = I_h(t-h) + \frac{2}{h}L^{-1}\begin{bmatrix} u(t-h) \\ v(t-h) \end{bmatrix}$$$

*用于构建微分扩展网络的等效电路，其中历史电流源$I_h$体现了梯形法的记忆效应*



## 验证详情

- **验证方式**: 通过开发通用仿真程序进行数值验证，并与理论解析解及传统EMTP仿真结果对比分析
- **测试系统**: 包括RLC串联电路（Fig. 3）和含FACTS、HVDC设备的大规模实际电力系统，具体节点数在提供的文本片段中未明确但提及为"realistic size power systems"
- **仿真工具**: 自主开发的通用仿真程序（general program），基于所提时域变换方法实现，兼容EMTP的支路级建模框架
- **验证结果**: 各种案例研究（various case studies）证实了该方法允许使用大步长而不牺牲精度，显著提升了大规模电力系统动态仿真的计算速度，同时能够同时提供瞬时波形和相量信息，验证了方法的有效性和实用性
