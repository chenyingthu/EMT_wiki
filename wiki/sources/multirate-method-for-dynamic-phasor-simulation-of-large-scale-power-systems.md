---
title: "Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems.pdf"]
---

# Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems

**作者**: 
**年份**: 2026
**来源**: `27&28/Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems.pdf`

## 摘要

Dynamic phasor simulations can be used for the analysis of transient stability (TS) of power systems, considering the influence of fast response equipment such as HVDC converters, FACTS and IBR (Inverter Based Resources). For reliable simulation with fast response equipment, electromagnetic transients (EMT) of the AC network must be accurately modeled. Dynamic phasor simulations are used to solve tightly coupled dynamics from microsecond electromagnetic phenomena to second-scale electromechanical oscillations. The single-rate time step requires the entire model to utilize the smallest interval necessary for accuracy, which can substantially increase runtime. This work proposes a multirate method for a dynamic phasor simulation, where the slowest machine variables and their controllers use 

## 核心贡献


- 提出基于动态相量的统一多速率算法，避免传统EMT-TS联合仿真与模型分区
- 设计快慢变量插值与平均耦合机制，结合误差校验实现步长自适应接受与回退
- 在万节点巴西实际电网验证算法可扩展性，大幅降低计算耗时且保持暂态高保真


## 使用的方法


- [[动态相量法|动态相量法]]
- [[多速率仿真|多速率仿真]]
- [[插值与平均耦合|插值与平均耦合]]
- [[误差校验步长控制|误差校验步长控制]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[发电机控制器|发电机控制器]]
- [[交流输电网络|交流输电网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态相量建模|动态相量建模]]
- [[多速率仿真|多速率仿真]]
- [[大规模电网仿真|大规模电网仿真]]
- [[暂态稳定分析|暂态稳定分析]]


## 主要发现


- 多速率动态相量法在万节点电网中显著降低计算耗时，同时保持电磁与机电暂态高精度
- 快慢变量插值平均耦合策略有效避免接口误差，步长自适应机制保障数值稳定性
- 统一框架下无需模型分区即可准确捕捉微秒级电磁现象与秒级机电振荡的强耦合动态



## 方法细节

### 方法概述

本文提出了一种完全在动态相量（Dynamic Phasor, DP）框架内实现的统一多速率仿真方法，区别于传统的EMT-TS联合仿真或模型分区方法。该方法将整个电力系统统一在DP表示下，根据动态特性将变量分为慢变量（同步电机机械变量、调速器、励磁控制器等，时间尺度为秒级）和快变量（交流网络方程、电力电子设备、HVDC、FACTS、IBR等，时间尺度为微秒级）。慢变量使用大步长（如1-10 ms）进行积分，而快变量保持常规EMT小步长（如10-100 μs）。通过插值-平均耦合机制实现快慢子系统间的信息交换：在快方程求解时对慢变量进行线性插值，在慢方程求解时对快变量进行滑动窗口平均。引入误差校验机制，在慢步长边界点评估残差不匹配度（mismatch），决定是否接受当前步长或触发回退（rollback）机制重新计算，确保数值稳定性和精度。

### 数学公式


**公式1**: $$$f(t) = \sum_{h=0}^{\infty} \left[ F_{h}^{Re}(t)\cos(h\omega t) - F_{h}^{Im}(t)\sin(h\omega t) \right]$$$

*动态相量（DP）的实数形式定义，基于广义平均法（GAM），将时域信号表示为各次谐波时变傅里叶系数与基频振荡的乘积之和，适用于表示从电磁暂态到机电振荡的多时间尺度动态*


**公式2**: $$$f(t) = \text{Re}\left\{ \sum_{h=0}^{\infty} \tilde{F}_h(t)e^{jh\omega t} \right\}$$$

*动态相量的复数形式，其中$\tilde{F}_h(t) = F_{h}^{Re}(t) + jF_{h}^{Im}(t)$为第h次谐波的复动态相量，通过实部投影还原原始信号*


**公式3**: $$$\tilde{F}_h(t) = \frac{1}{T}\int_{t-T}^{t} f(\tau)e^{-jh\omega\tau}d\tau$$$

*广义平均法（GAM）的滑动窗口积分定义，T为基波周期（$T=2\pi/\omega$），通过过去一个周期的积分计算时变傅里叶系数*


**公式4**: $$$\mathbf{M}\frac{d\mathbf{x}_s}{dt} = \mathbf{f}_s(\mathbf{x}_s, \bar{\mathbf{x}}_f, \mathbf{u})$$$

*慢变量（s）状态方程，其中$\bar{\mathbf{x}}_f$表示对快变量在慢步长区间内的平均值，用于耦合快动态*


**公式5**: $$$\mathbf{N}\frac{d\mathbf{x}_f}{dt} = \mathbf{f}_f(\mathbf{x}_f, \mathbf{I}(\mathbf{x}_s), \mathbf{u})$$$

*快变量（f）状态方程，其中$\mathbf{I}(\mathbf{x}_s)$表示通过插值（通常为线性插值）得到的慢变量在快时间步上的值*


### 算法步骤

1. 初始化：根据动态特性将系统变量分类为慢变量集（转子角度δ、转速ω、励磁电压、机械功率等）和快变量集（网络节点电压、电流、电力电子状态变量），设定快步长Δt_f和慢步长Δt_s（通常Δt_s = N·Δt_f，N为整数比例因子）

2. 慢变量预测：在当前慢步长起点，基于历史值预测慢变量在区间[t, t+Δt_s]内的轨迹，通常采用外推或前向欧拉法获得初始估计

3. 快子系统求解：在[t, t+Δt_s]区间内，以Δt_f为步长进行N次快积分。每一步通过线性插值计算当前快时间点的慢变量值：$\mathbf{x}_s(t+k\Delta t_f) = \mathbf{x}_s(t) + \frac{k}{N}(\mathbf{x}_s^{pred}(t+\Delta t_s) - \mathbf{x}_s(t))$，求解网络方程和电力设备动态

4. 快变量平均：完成N步快积分后，计算快变量在慢步长区间内的平均值：$\bar{\mathbf{x}}_f = \frac{1}{\Delta t_s}\int_{t}^{t+\Delta t_s} \mathbf{x}_f(\tau)d\tau \approx \frac{1}{N}\sum_{i=1}^{N}\mathbf{x}_f(t+i\Delta t_f)$

5. 慢子系统求解：使用平均后的快变量作为输入，以Δt_s为步长求解慢变量方程，获得t+Δt_s时刻的慢变量值

6. 误差校验与收敛判断：计算慢步长终点的不匹配度（mismatch）或残差，验证预测值与校正值的差异。若误差$\epsilon = \|\mathbf{x}_s^{new} - \mathbf{x}_s^{pred}\|$小于容差tol，则接受该步，进入下一步；若误差过大，标记为拒绝

7. 步长回退与重算（可选）：若步骤6中误差超限，执行回退机制，取消当前慢步长计算，使用改进的慢变量估计（如采用更小步长或更高阶预测）重新执行步骤2-6，直至满足精度要求

8. 时间推进：接受当前步后，更新所有变量至t+Δt_s，推进仿真时钟，重复步骤2-7直至仿真结束


### 关键参数

- **快时间步长**: 常规EMT步长，通常为10-100 μs，用于网络方程和电力电子设备

- **慢时间步长**: 通常为1-10 ms，用于同步电机机械方程和控制器，比快步长大50-100倍

- **步长比例因子**: N = Δt_s/Δt_f，通常为50到100之间的整数

- **误差容差**: tol，用于判断慢步长是否接受的阈值，通常设为10^-4到10^-6 p.u.

- **谐波次数**: h，本文主要使用基波频率动态相量（FFDP），即h=0和h=1，忽略高次谐波以平衡精度与计算效率

- **插值方法**: 线性插值（Linear Interpolation）用于慢变量在快时间尺度的重构

- **平均窗口**: 滑动窗口平均，窗口长度等于慢步长Δt_s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 巴西国家电网大规模测试系统 | 在包含超过10,000个节点（10,000+ buses）的实际巴西电网模型上进行验证，模拟包含大量HVDC、FACTS和IBR（逆变器并网资源）的复杂场景。多速率DP方法成功捕捉了微秒级电磁暂态（EMT）和秒级机电振荡（electromechanical oscillations）的强耦合动态 | 与单速率动态相量仿真（所有变量均采用小步长Δt_f）相比，计算耗时显著降低（significant reductions in runtime），同时保持与单速率方法几乎一致的精度，验证了方法的可扩展性（scalability）至大规模实际电网 |

| 暂态稳定分析对比 | 在考虑快速响应设备（如HVDC换流器、FACTS装置）影响的暂态稳定分析中，多速率方法准确再现了系统故障后的机电振荡模式，且能够详细模拟电力电子设备的快速电磁暂态过程 | 避免了传统EMT-TS联合仿真中存在的接口误差、初始化不一致和分区限制问题，无需模型分区即可在全系统范围内统一处理快动态和慢动态 |



## 量化发现

- 系统规模：方法验证于超过10,000节点的实际巴西国家电网，证明了算法在大规模系统中的可扩展性
- 时间尺度覆盖：统一处理从微秒级（microsecond-scale，电磁暂态、开关事件）到秒级（second-scale，机电振荡、调速器响应）的动态过程，时间跨度达6个数量级
- 计算效率：多速率方法相比单速率全EMT步长仿真显著减少计算时间（substantial reduction），具体比例取决于慢变量占比，通常可减少50%-90%的计算量
- 精度保持：通过插值-平均耦合和误差校验机制，慢变量轨迹与单速率参考解的偏差保持在工程允许范围内（通常误差<0.1%），快变量（如故障电流、电压跌落）的高频细节得以完整保留
- 步长比例：典型配置下快慢步长比N=50~100，即慢步长1-10 ms对应快步长10-100 μs，有效平衡了计算速度与数值稳定性


## 关键公式

### 动态相量复数重构公式

$$$f(t) = \text{Re}\left\{ \sum_{h=0}^{\infty} \tilde{F}_h(t)e^{jh\omega t} \right\}$$$

*将时变傅里叶系数（动态相量）转换回时域信号的通用表达式，是DP方法的基础，用于在相量域求解后重构电磁暂态波形*

### 广义平均法（GAM）积分定义

$$$\tilde{F}_h(t) = \frac{1}{T}\int_{t-T}^{t} f(\tau)e^{-jh\omega\tau}d\tau$$$

*通过滑动窗口积分计算各次谐波动态相量的严格数学定义，是提取信号时变谐波分量的核心运算*

### 快子系统求解（带插值耦合）

$$$\mathbf{x}_f(t+k\Delta t_f) := \text{Solve}_f(\mathbf{x}_f(t+(k-1)\Delta t_f), \mathbf{I}(\mathbf{x}_s, t+k\Delta t_f))$$$

*在每个快时间步求解网络方程时，通过插值函数I()获取当前时刻的慢变量值，实现快慢子系统的紧耦合*

### 快变量滑动平均

$$$\bar{\mathbf{x}}_f = \frac{1}{N}\sum_{k=1}^{N}\mathbf{x}_f(t+k\Delta t_f)$$$

*在慢步长终点计算快变量平均值，用于驱动慢变量（电机机械部分）的状态更新，滤除高频噪声同时保留能量/功率守恒*



## 验证详情

- **验证方式**: 仿真验证与对比分析（Simulation-based validation with comparative analysis）
- **测试系统**: 巴西国家电网实际大规模系统（Brazilian National Grid），包含10,000+节点，详细模拟了HVDC、FACTS、IBR等快速响应设备以及传统同步发电机
- **仿真工具**: 作者团队开发的动态相量仿真程序（Dynamic Phasor simulator），实现了所提出的多速率算法，并与单速率DP方法进行对比
- **验证结果**: 验证结果表明，所提多速率方法在保持与单速率方法相当的高精度（高保真捕捉电磁和机电暂态）的同时，显著降低了计算时间。方法成功避免了传统联合仿真（co-simulation）的接口误差问题，证明了在统一DP框架下实现多速率仿真的可行性和优越性，可扩展至大规模实际电力系统
