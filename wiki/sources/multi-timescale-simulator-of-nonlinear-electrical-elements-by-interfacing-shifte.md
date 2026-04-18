---
title: "Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors and electromagnetic transient simulation"
type: source
authors: ['Zhen Gong']
year: 2022
journal: "Electric Power Systems Research, 208 (2022) 107856. doi:10.1016/j.epsr.2022.107856"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors.pdf"]
---

# Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors and electromagnetic transient simulation

**作者**: Zhen Gong
**年份**: 2022
**来源**: `27&28/Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors and electromagnetic transient simulation School of Electrical Engineering and Automation, Wuhan University, Wuhan 430072, China This paper proposes a multi-timescale transient branch companion model for electrical elements with strong nonlinearity, which is suitable for electromagnetic

## 核心贡献


- 提出基于移位等效相量的多时间尺度支路伴随模型，适用于强非线性元件宽频带仿真
- 结合动态相量与包络跟踪技术，实现单次仿真中瞬时波形与包络波形的高效同步追踪
- 建立饱和SEP变压器模型，克服传统分段线性化在大步长下的数值过冲问题


## 使用的方法


- [[移位等效相量法-sep|移位等效相量法(SEP)]]
- [[动态相量法-dp|动态相量法(DP)]]
- [[牛顿-拉夫逊迭代|牛顿-拉夫逊迭代]]
- [[梯形积分法|梯形积分法]]
- [[伴随模型法|伴随模型法]]
- [[混合仿真接口|混合仿真接口]]


## 涉及的模型


- [[饱和变压器|饱和变压器]]
- [[vsc-model|VSC]]
- [[非线性电感|非线性电感]]
- [[磁链控制非线性支路|磁链控制非线性支路]]


## 相关主题


- [[多时间尺度仿真|多时间尺度仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[非线性元件建模|非线性元件建模]]
- [[包络跟踪|包络跟踪]]
- [[谐波分析|谐波分析]]
- [[大步长仿真|大步长仿真]]


## 主要发现


- SEP模型在大步长下有效抑制了传统分段线性化产生的励磁电流数值过冲现象
- 通过合理设置移频参数与步长，单次仿真即可同时精确追踪瞬时值与包络波形
- MATLAB与PSCAD验证表明，该模型在保持精度的同时显著提升非线性元件仿真效率



## 方法细节

### 方法概述

本文提出了一种基于移位等效相量（Shifted Equivalent Phasor, SEP）与电磁暂态（EMT）仿真相接口的多时间尺度瞬态支路伴随模型。该方法通过动态相量（Dynamic Phasor, DP）理论对宽频带信号进行谐波分解，利用等效相量移位算子将高频分量搬移至低频区域形成慢变包络，从而允许在关注包络动态时使用大步长积分以提高效率；同时，通过乘回移位算子可在同一仿真进程中恢复瞬时波形 details。针对非线性元件（如饱和变压器），采用牛顿-拉夫逊迭代结合梯形积分法构建离散伴随模型，将非线性电感转化为等效电导与历史电流源并联的诺顿等效电路，解决了传统分段线性化在大步长下的数值过冲问题。

### 数学公式


**公式1**: $$$\psi_{n+1} - \psi_n = \frac{\tau}{2}(V_{n+1} + V_n)$$$

*梯形积分法离散化的磁链-电压关系，用于将连续时间微分方程$d\psi/dt = V(t)$转换为离散代数方程，其中$\tau$为时间步长，$n$为时间步计数器*


**公式2**: $$$i_{n+1}^{(j+1)} = G_L^{(j)} V_{n+1}^{(j+1)} + I_{Lh}^{(j)}$$$

*非线性电感的伴随模型方程，通过牛顿-拉夫逊迭代线性化得到，$G_L^{(j)}$为第$j$次迭代的等效电导，$I_{Lh}^{(j)}$为历史电流源，将非线性支路转化为线性等效电路便于EMT求解*


**公式3**: $$$\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jk\omega_s \tau} d\tau$$$

*动态相量（DP）定义式，表示信号$x(\tau)$在第$k$次谐波处的时变傅里叶系数，$T$为滑动窗口周期，$\omega_s=2\pi/T$为基波频率，用于提取各次谐波的复包络*


**公式4**: $$$\langle x(t) \cdot y(t) \rangle_k = \sum_{i=-\infty}^{\infty} \langle x(t) \rangle_{k-i} \langle y(t) \rangle_i$$$

*动态相量的乘积性质（卷积性质），用于处理非线性元件中电压与电感（或电流与电阻）的乘积，将时域非线性乘积转换为相量域的离散卷积和*


**公式5**: $$$\frac{d}{dt}\langle x(t) \rangle_k(t) = \left\langle \frac{dx(t)}{dt} \right\rangle_k - jk\omega\langle x \rangle_k(t)$$$

*动态相量的微分性质，用于将时域微分方程转换到相量域，其中$\omega=2\pi/T$，右侧第二项体现频率移位效应，是构建DP域伴随模型的基础*


**公式6**: $$$S(t-T+s) = \langle x(t) \rangle_0(t) + \sum_{k=1}^{\infty} (2\langle x(t) \rangle_k(t)e^{jk\omega_s(t-T+s)})$$$

*移位等效相量（SEP）信号重构公式，$\hat{S}(t) = \langle x \rangle_0 + \sum_{k=1}^{\infty} 2\langle x \rangle_k$为慢变复包络，乘以$e^{jk\omega_s(t-T+s)}$（SEP算子）后恢复原始高频信号，实现包络与瞬时值的统一表示*


**公式7**: $$$G_L^{(j)} = \frac{\Gamma^{(j)}\tau}{2}, \quad \Gamma^{(j)} = \left.\frac{di}{d\psi}\right|_{\psi_{n+1}^{(j)}}$$$

*伴随模型中等效电导的计算公式，$\Gamma^{(j)}$为非线性特性$i=g(\psi)$在当前迭代工作点处的斜率（增量电导倒数），$\tau$为积分步长*


### 算法步骤

1. 对磁链控制型非线性电感（如变压器铁芯）建立微分方程$d\psi/dt = V(t)$和代数方程$i=g(\psi)$，采用梯形积分法进行离散化，得到$\psi_{n+1} - \psi_n = \frac{\tau}{2}(V_{n+1} + V_n)$

2. 在当前时间步$n+1$和第$j$次牛顿-拉夫逊迭代点$\psi_{n+1}^{(j)}$处，对非线性函数$i=g(\psi)$进行一阶泰勒展开线性化，计算增量电导$\Gamma^{(j)} = dg/d\psi$和等效电导$G_L^{(j)} = \Gamma^{(j)}\tau/2$

3. 构建离散伴随模型，将非线性支路转换为诺顿等效电路：等效电导$G_L^{(j)}$与历史电流源$I_{Lh}^{(j)} = g(\psi_{n+1}^{(j)}) - \Gamma^{(j)}(\psi_{n+1}^{(j)} - \psi_n) + G_L^{(j)}V_n$并联

4. 对网络中的电压、电流信号$x(t)$应用滑动窗口离散傅里叶变换（RDFT），提取各次谐波的动态相量$\langle x \rangle_k(t)$，构建复包络$\hat{S}(t) = \sum_{k} 2\langle x \rangle_k$（$k=0$时为直流分量）

5. 通过引入移位等效相量算子$e^{jk\omega_s(t-T+s)}$，将DP域的复包络信号搬移至低频区域（若$\omega_s$设为载波频率，则包络频谱集中在零频附近），此时可采用大步长$\Delta t$进行积分以加速仿真

6. 根据仿真需求进行模式选择：若关注包络动态，直接对$\hat{S}(t)$使用大步长（如100$\mu$s或更大）进行仿真；若关注瞬时波形，将SEP算子乘回复包络$\hat{S}(t)$重构原始信号$S(t-T+s)$，恢复高频细节

7. 在每个时间步内执行牛顿-拉夫逊迭代求解网络方程，更新非线性元件工作点直至收敛（通常一次迭代即可满足精度），实现瞬时波形与包络波形在单次仿真中的同步追踪


### 关键参数

- **time_step_size**: $\tau$（或$\Delta t$），梯形积分步长，传统方法需较小（如10$\mu$s），SEP方法可采用大步长（如100$\mu$s或更大）

- **shifting_frequency**: $\omega_s = 2\pi/T$，移位等效相量频率，通常设为基波或载波频率，决定频谱搬移的中心频率

- **harmonic_order**: $k$，动态相量分析的谐波次数，理论上$k \in (-\infty, \infty)$，实际取有限项（如$k=0, \pm1, \pm2...$）

- **newton_tolerance**: 牛顿-拉夫逊迭代收敛判据（文中未明确具体数值，但指出通常一次迭代即可收敛）

- **window_period**: $T = 2\pi/\omega_s$，滑动窗口周期，通常取基波周期



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 饱和变压器励磁涌流仿真 | 在变压器空载合闸或故障恢复场景中，对比传统分段线性化与SEP模型的励磁电流波形。传统方法在大步长（如100$\mu$s）下出现显著的数值过冲（overshoot），导致励磁电流峰值计算错误；SEP模型在同等大步长下完全抑制过冲，波形平滑且与理论饱和特性一致 | 相比传统分段线性化方法，SEP模型在大步长条件下消除了数值过冲现象，允许使用比传统EMT大一个数量级的时间步长（如从10$\mu$s提升至100$\mu$s以上）而保持精度 |

| 电压源变换器（VSC）多时间尺度仿真 | 建立VSC模型验证SEP方法在电力电子器件中的适用性。通过设置不同的移频参数$\omega_s$和步长$\tau$，同时追踪VSC交流侧电压/电流的瞬时高频波形（含开关谐波）和慢变包络（基波分量） | 单次仿真即可同时获得精确的瞬时波形（通过SEP算子恢复）和包络动态（大步长积分），无需像传统DP-EMT联合仿真那样在不同时间尺度间切换或牺牲高频精度 |



## 量化发现

- 传统分段线性化方法在步长为100$\mu$s时产生严重的励磁电流数值过冲（overshoot），而SEP模型在同等步长下完全抑制该现象
- 传统DP-EMT联合仿真在步长比为100$\mu$s:10$\mu$s时会产生较大误差，而SEP方法通过频谱搬移允许使用大步长（如毫秒级或百微秒级）而保持数值稳定性
- 通过合理设置移频参数$\omega_s$（设为载波频率）和时间步长$\tau$，可将原高频信号频谱集中在零频附近，实现包络跟踪，计算效率显著提升（具体加速比取决于所取步长与谐波次数，理论上与步长增大倍数成正比）
- 牛顿-拉夫逊迭代求解非线性伴随模型时，无论初始点如何选择，通常仅需一次迭代即可收敛到函数根（参考ATP中的补偿法理论）
- SEP模型在保持与详细EMT模型相当精度的同时，通过动态相量识别不同谐波分量，避免了FAST（自适应频率暂态仿真）方法仅适用于线性元件的局限性


## 关键公式

### 非线性电感离散伴随模型

$$$i_{n+1}^{(j+1)} = G_L^{(j)} V_{n+1}^{(j+1)} + I_{Lh}^{(j)}$$$

*用于将磁链控制型非线性电感（变压器铁芯）在EMT仿真中转换为等效线性电路，结合牛顿-拉夫逊迭代在每个时间步更新等效电导和历史电流源*

### 动态相量（DP）定义

$$$\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jk\omega_s \tau} d\tau$$$

*用于提取信号第$k$次谐波的时变复包络，是SEP方法的基础，通过滑动窗口傅里叶变换将时域信号分解为各次谐波的慢变相量*

### 移位等效相量（SEP）信号重构

$$$S(t-T+s) = \langle x(t) \rangle_0(t) + \sum_{k=1}^{\infty} 2\langle x(t) \rangle_k(t)e^{jk\omega_s(t-T+s)}$$$

*实现多时间尺度仿真的核心公式，通过移位算子$e^{jk\omega_s(t-T+s)}$将DP域的复包络$\hat{S}(t)$恢复为时域瞬时信号，或反之将高频信号搬移至低频包络*



## 验证详情

- **验证方式**: 数值仿真对比验证（与基线方法对比）
- **测试系统**: 包含饱和变压器的励磁涌流测试系统和电压源变换器（VSC）测试系统（具体拓扑未在提供的摘录中详述，但包含强非线性元件和电力电子器件）
- **仿真工具**: MATLAB（用于SEP算法实现）和 PSCAD/EMTDC（用于传统电磁暂态仿真对比验证）
- **验证结果**: SEP模型在大步长（如100$\mu$s）下有效抑制了传统分段线性化产生的励磁电流数值过冲现象，验证了模型的数值稳定性；通过合理设置移频参数与步长，单次仿真即可同时精确追踪瞬时值与包络波形，证明了该方法在保持精度的同时显著提升非线性元件仿真效率，适用于宽频带多时间尺度的电磁暂态分析
