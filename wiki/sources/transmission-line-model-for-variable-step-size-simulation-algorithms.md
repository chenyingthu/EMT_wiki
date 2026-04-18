---
title: "Transmission line model for variable step size simulation algorithms"
type: source
authors: ['未知']
year: 1999
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/39/s0142-0615%2898%2900042-8.pdf.pdf"]
---

# Transmission line model for variable step size simulation algorithms

**作者**: 
**年份**: 1999
**来源**: `39/s0142-0615%2898%2900042-8.pdf.pdf`

## 摘要

In this paper, we describe a novel modeling approach for transmission lines that overcomes the maximum step size constraint of regular line models used in electromagnetic transients programs. The new model allows us to accurately simulate wave propagation phenomena as well as low network frequency variations with maximum efﬁciency, as the simulation step size is no longer restricted to model requirements, but can be adjusted according to the current transient state of the network. The model was tested with a CIGRE line energization case study which was performed utilizing a variable simulation step size algorithm for a combined study of electromagnetic transients and transient stability. q 1998 Elsevier Science Ltd. All rights reserved. Keywords: Transmission line modeling; Electromagnetic

## 核心贡献



- 提出了一种突破传统EMTP线路模型最大步长限制的新型输电线路建模方法
- 实现了基于网络暂态状态动态调整步长的仿真算法，兼顾电磁暂态波传播与低频机电暂态的精度与效率

## 使用的方法


- [[numerical-integration]]
- [[interpolation]]

## 涉及的模型


- [[transmission-line]]
- [[frequency-dependent]]

## 相关主题


- [[co-simulation]]
- [[network-equivalent]]

## 主要发现



- 新模型成功解除了传统线路模型对仿真步长必须小于等于最小波传播时间的严格约束
- CIGRE线路投切测试表明，变步长算法结合新模型能高效准确地同时捕捉电磁暂态波传播与低频网络频率变化

## 方法细节

### 方法概述

本文提出了一种基于插值技术的变步长输电线路建模方法，突破了传统EMTP线路模型要求仿真步长必须小于最小波传播时间（Δt ≤ τ_min）的限制。该方法包含三个层次：1）当Δt ≤ τ时，使用传统Bergeron无损线模型，保持线路两端电气隔离；2）当Δt > τ时，采用线性插值技术估算τ时刻前的历史值，将线路模型转换为具有非零非对角元素的导纳矩阵形式，此时电气隔离消失但计算精度得以保持；3）对于机电暂态仿真（大步长40-60ms），引入动态相量（Dynamic Phasor）概念，通过复数插值处理带额定频率旋转分量的变量，实现电磁暂态与机电暂态的联合仿真。该方法适用于恒定参数线路模型，并可扩展至频变线路模型。

### 数学公式


**公式1**: $$$$\begin{bmatrix} \bar{i}_k(t) \\ \bar{i}_m(t) \end{bmatrix} = \begin{bmatrix} G_c & 0 \\ 0 & G_c \end{bmatrix} \begin{bmatrix} \bar{v}_k(t) \\ \bar{v}_m(t) \end{bmatrix} + \begin{bmatrix} \bar{h}_k(t) \\ \bar{h}_m(t) \end{bmatrix}$$$$

*传统Bergeron无损线模型（Δt ≤ τ），k和m为线路两端，Gc为特性电导，电气隔离（对角矩阵）*


**公式2**: $$$$\begin{bmatrix} \bar{h}_k(t) \\ \bar{h}_m(t) \end{bmatrix} = -\begin{bmatrix} G_c & 0 \\ 0 & G_c \end{bmatrix} \begin{bmatrix} \bar{v}_k(t-\tau) \\ \bar{v}_m(t-\tau) \end{bmatrix} - \begin{bmatrix} \bar{i}_k(t-\tau) \\ \bar{i}_m(t-\tau) \end{bmatrix}$$$$

*历史项计算，取决于τ时刻前的电压电流值，τ为波传播时间*


**公式3**: $$$$\bar{x}(t-\tau) = a\bar{x}(t) + b\bar{x}(t-\Delta t), \quad a=\frac{\Delta t-\tau}{\Delta t}, \quad b=\frac{\tau}{\Delta t}$$$$

*线性插值公式（Δt ≥ τ），用于估算τ时刻前的状态变量值*


**公式4**: $$$$\begin{bmatrix} \bar{i}_k(t) \\ \bar{i}_m(t) \end{bmatrix} = G_c \begin{bmatrix} 1+a^2 & -2a \\ -2a & 1+a^2 \end{bmatrix} \begin{bmatrix} \bar{v}_k(t) \\ \bar{v}_m(t) \end{bmatrix} + \begin{bmatrix} \bar{h}_k(t) \\ \bar{h}_m(t) \end{bmatrix}$$$$

*扩展线路模型（Δt ≥ τ），导纳矩阵出现非对角元素-2a·Gc，电气隔离消失*


**公式5**: $$$$\bar{X}(t) = \bar{x}(t)e^{-j\omega_0 t}$$$$

*动态相量（复数域）定义，ω₀为额定角频率（2π×50或60 Hz），用于稳定性研究的大步长仿真*


**公式6**: $$$$\bar{x}(t-\tau) = p\bar{x}(t) + q\bar{x}(t-\Delta t), \quad p=\frac{\Delta t-\tau}{\Delta t}e^{-j\omega_0 \tau}, \quad q=\frac{\tau}{\Delta t}e^{j\omega_0(\Delta t-\tau)}$$$$

*复数插值公式（大步长），插值系数p和q包含频率旋转因子*


**公式7**: $$$$\begin{bmatrix} \bar{i}_k(t) \\ \bar{i}_m(t) \end{bmatrix} = G_c \begin{bmatrix} 1+p^2 & -2p \\ -2p & 1+p^2 \end{bmatrix} \begin{bmatrix} \bar{v}_k(t) \\ \bar{v}_m(t) \end{bmatrix} + \begin{bmatrix} \bar{h}_k(t) \\ \bar{h}_m(t) \end{bmatrix}$$$$

*复数域线路模型，导纳矩阵变为复数矩阵，适用于Δt=40-60ms的机电暂态仿真*


### 算法步骤

1. 初始化：设定线路参数（波传播时间τ，特性电导Gc），选择初始仿真步长Δt

2. 步长判断：比较当前步长Δt与最小波传播时间τ_min（τ_min = min[τ_i], i=1,...,n，n为模态数）

3. 小步长模式（Δt ≤ τ_min）：使用传统Bergeron模型（公式1-2），从历史存储中提取τ时刻前的值，保持两端电气隔离（解耦计算）

4. 中步长模式（τ_min < Δt < 1ms）：启用实数线性插值，计算系数a=(Δt-τ)/Δt和b=τ/Δt，利用公式4插值得到τ时刻前的等效值

5. 构建实数域扩展模型：根据公式5-6构建包含非对角元素的实导纳矩阵和历史项，此时线路两端在电气上耦合

6. 大步长模式（Δt ≥ 1ms，稳定性研究）：执行频率变换，将时域变量x(t)转换为动态相量X(t)=x(t)e^(-jω₀t)

7. 复数插值计算：计算复数插值系数p和q（含频率旋转因子），利用公式8在复数域进行插值

8. 构建复数域模型：根据公式9-10构建复导纳矩阵和复历史项，求解复数域网络方程

9. 变量反变换：将复数域结果转换回时域，更新历史项（仅需存储前一步的值）

10. 动态步长调整：根据网络暂态状态（电磁暂态或机电暂态）自动调整下一步的Δt（1ms至60ms范围），重复步骤2-9


### 关键参数

- **τ_min**: 最小波传播时间（s），决定传统模型的最大允许步长

- **Δt**: 仿真步长（s），可变范围从微秒级到40-60ms

- **G_c**: 特性电导（S），无损线特征阻抗的倒数（G_c = 1/R_c）

- **a, b**: 实数插值系数，a=(Δt-τ)/Δt, b=τ/Δt，满足a+b=1

- **p, q**: 复数插值系数，包含额定频率相位偏移，p=((Δt-τ)/Δt)e^(-jω₀τ), q=(τ/Δt)e^(jω₀(Δt-τ))

- **ω₀**: 额定角频率（rad/s），ω₀=2πf₀，f₀=50或60Hz

- **d**: 传统模型历史内存需求，d=ceil(τ/Δt)，新模型仅需1个存储位置



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| CIGRE 1971年线路投切案例（三相输电线路空载合闸） | 使用变步长算法模拟线路 energization 过程，初始阶段使用小步长（<1ms）捕捉高频电磁暂态（波传播现象），随后自动增大步长至40-60ms模拟低频机电暂态和稳态行为。与MICROTRAN（使用极小固定步长）的参考解对比，波形吻合良好。 | 相比传统固定小步长EMTP仿真，计算效率显著提高（步长扩大40-60倍），内存需求从d=ceil(τ/Δt)个存储位置（典型值20个）减少至仅需1个历史向量 |



## 量化发现

- 传统EMTP线路模型限制：仿真步长必须满足Δt ≤ τ_min，对于50/60Hz系统通常要求Δt ≤ 1ms以保证正弦波形的分段线性近似精度
- 新模型步长范围：可扩展至40-60ms（机电暂态研究典型步长），相比传统方法扩大40-60倍
- 内存需求减少：传统模型需要存储d=ceil(τ/Δt)个历史值（例如τ=1ms，Δt=50μs时需存储20个值），新模型仅需存储前一步的1个历史向量
- 波传播时间τ：典型架空线路的模态传播时间通常在微秒至毫秒级（如100-1000μs），是限制传统模型步长的关键参数
- 复数插值精度：通过动态相量变换e^(-jω₀t)处理额定频率分量，允许在保持低频动态精度的同时忽略高频电磁暂态细节


## 关键公式

### 复数域动态相量插值公式

$$$$\bar{x}(t-\tau) = p\bar{x}(t) + q\bar{x}(t-\Delta t), \quad p=\frac{\Delta t-\tau}{\Delta t}e^{-j\omega_0 \tau}, \quad q=\frac{\tau}{\Delta t}e^{j\omega_0(\Delta t-\tau)}$$$$

*当仿真步长超过波传播时间（Δt > τ）且进入机电暂态时间尺度（Δt ≈ 40-60ms）时使用，通过额定频率旋转因子e^(-jω₀τ)实现大步长下的精确相量仿真*

### 扩展线路导纳模型（实数域）

$$$$\begin{bmatrix} \bar{i}_k(t) \\ \bar{i}_m(t) \end{bmatrix} = G_c \begin{bmatrix} 1+a^2 & -2a \\ -2a & 1+a^2 \end{bmatrix} \begin{bmatrix} \bar{v}_k(t) \\ \bar{v}_m(t) \end{bmatrix} + \begin{bmatrix} \bar{h}_k(t) \\ \bar{h}_m(t) \end{bmatrix}$$$$

*当Δt > τ时替代传统Bergeron模型，非对角元素-2a·Gc（a=(Δt-τ)/Δt）反映了两端电气耦合，允许大步长仿真同时保持波传播的历史效应*



## 验证详情

- **验证方式**: 对比验证（与参考解对比）
- **测试系统**: CIGRE 1971年标准线路投切测试系统（三相输电线路 energization 案例）
- **仿真工具**: UBC开发的MICROTRAN（固定极小步长的EMTP版本，作为参考解）和正在开发的变步长仿真程序
- **验证结果**: 变步长算法结合新线路模型在CIGRE测试案例中表现良好，初始小步长阶段准确捕捉波传播和电磁暂态，后续大步长阶段（40-60ms）准确跟踪低频网络频率变化，与MICROTRAN参考解一致，验证了模型在变步长条件下的准确性和效率
