---
title: "Assessment of dynamic phasor extraction methods for power system co-simulation applications"
type: source
authors: ['Janesh Rupasinghe']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107319. doi:10.1016/j.epsr.2021.107319"
tags: ['cosimulation', 'dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/09/Rupasinghe 等 - 2021 - Assessment of dynamic phasor extraction methods for power system co-simulation applications.pdf"]
---

# Assessment of dynamic phasor extraction methods for power system co-simulation applications

**作者**: Janesh Rupasinghe
**年份**: 2021
**来源**: `09/Rupasinghe 等 - 2021 - Assessment of dynamic phasor extraction methods for power system co-simulation applications.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Assessment of dynamic phasor extraction methods for power system Janesh Rupasinghe a, Shaahin Filizadeh *,a, Kai Strunz b a Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Canada The paper examines a number of methods for extracting dynamic phasors from samples of natural waveforms

## 核心贡献


- 系统评估多种动态相量提取方法的理论基础与数值实现流程
- 深入分析含振荡、直流、谐波及不平衡信号下提取相量的特性与局限
- 构建EMT-动态相量联合仿真算例，验证不同提取方法的适用性


## 使用的方法


- [[动态相量提取|动态相量提取]]
- [[广义平均法|广义平均法]]
- [[移频分析法|移频分析法]]
- [[快速时变相量变换|快速时变相量变换]]


## 涉及的模型


- [[三相交流线性电路模型|三相交流线性电路模型]]
- [[动态相量数学模型|动态相量数学模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[联合仿真|联合仿真]]
- [[动态相量提取|动态相量提取]]
- [[谐波分析|谐波分析]]
- [[频域建模|频域建模]]


## 主要发现


- 广义平均法可灵活选择谐波分量，但多谐波计算时计算负担显著增加
- 快速时变相量法仅适用于平衡三相系统，处理零序分量时复杂度剧增
- 不同提取方法在应对直流偏置与任意暂态时表现出显著的频谱精度差异



## 方法细节

### 方法概述

本文系统评估了四种动态相量提取方法：快速时变相量法(FTVP)、广义平均法(GAM)、移频分析法(SFA)和基频动态相量法(BFDP)。研究从数学理论出发，推导各方法将EMT时域自然波形转换为频域低通动态相量的变换算子与数值离散流程。重点分析了各方法在机电振荡、直流偏置、谐波、频率漂移及三相不平衡等典型电力系统暂态信号下的频谱搬移特性、计算复杂度与适用边界。通过构建统一的测试信号模型，对比各方法提取相量的包络波形与频谱分布，并探讨其在EMT-动态相量联合仿真接口中的工程适用性。

### 数学公式


**公式1**: $$$\langle x \rangle_k(t) = \frac{1}{T} \int_0^T x(t-T+s)e^{-jk\omega_0(t-T+s)} ds$$$

*GAM连续域定义式，通过滑动窗口傅里叶积分提取k次谐波动态相量*


**公式2**: $$$\langle x \rangle_k(t) = \langle x \rangle_k(t-\Delta t) + \frac{1}{N}[x(t)e^{-jk\omega_0 t} - x(t-N\Delta t)e^{-jk\omega_0(t-N\Delta t)}]$$$

*GAM离散递归更新公式，利用窗口重叠特性大幅降低计算量*


**公式3**: $$$z_{abc} = \hat{I} + j \frac{1}{\sqrt{3}} M x_{abc}$$$

*SFA三相解析信号近似矩阵表达式，用于从三相瞬时值直接构造解析信号*


**公式4**: $$$\langle X \rangle_B(t) = 2\langle x \rangle_1(t) + X_h(t)$$$

*BFDP方法II合成公式，将基频分量与剩余高频/直流分量合并下变频*


### 算法步骤

1. GAM递归提取流程：初始化积分窗口长度T与采样点数N，计算初始时刻k次谐波相量⟨x⟩_k(t-Δt)；当仿真步进至t时，利用前后窗口重叠特性执行递归更新：⟨x⟩_k(t) = ⟨x⟩_k(t-Δt) + (1/N)[x(t)e^{-jkω0t} - x(t-NΔt)e^{-jkω0(t-NΔt)}]，该步骤仅需2次加法与2次乘法；沿时间轴滑动窗口重复计算，直至获取全时段动态相量序列。

2. BFDP方法II提取流程：首先调用GAM递归算法计算基频正序分量⟨x⟩_1(t)；构造基频复指数项2⟨x⟩_1(t)e^{jω0(t-T+s)}并从原始时域信号x(t)中减去，得到包含直流与高次谐波的剩余信号X_h(t)；将X_h(t)与基频项在频域合并，并统一乘以e^{-jω0(t-T+s)}下变频至基频参考系，最终输出基频动态相量⟨X⟩_B(t) = 2⟨x⟩_1(t) + X_h(t)。


### 关键参数

- **T**: 积分窗口长度，通常取系统基频周期(如20ms)

- **N**: 单窗口内离散采样点数

- **k**: 目标谐波阶数(整数，k=0为直流，k=1为基频)

- **ω0**: 系统额定基频角频率(如2π×50或2π×60 rad/s)

- **fe**: 机电振荡频率，测试案例中设定为3Hz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 机电振荡工况 | 测试信号含基频幅值20、衰减振荡幅值15、振荡频率3Hz。所有方法均能准确提取包络，原始频谱f0±fe被成功搬移至0±fe低频带。 | GAM需计算多个冗余谐波系数，计算开销比SFA/BFDP高约3-5倍，但包络精度一致。 |

| 直流偏置与二次谐波工况 | 直流偏置a0=5(t∈[0,0.1]s)，二次谐波ah=10(t∈[0.15,0.25]s)。FTVP完全忽略零序/直流分量；GAM通过k=0准确捕获直流；SFA与BFDP将直流搬移至-f0，导致相量包络出现基频振荡。 | FTVP对直流分量提取误差为100%；GAM直流提取误差<0.1%；SFA/BFDP包络振荡幅值等于直流偏置值5。 |

| 频率斜坡暂态工况 | 频率变化率m=-0.5π(t∈[0.2,0.4]s)。各方法相量幅值保持恒定，实部与虚部相位角按Δωt规律平滑变化，验证了频偏跟踪能力。 | 各方法相位跟踪误差均<0.5%，幅值波动<0.2%，满足宽频暂态接口要求。 |



## 量化发现

- GAM离散递归算法将单步计算复杂度从直接积分的2N次运算降至4次运算(2加2乘)，在典型N=100时计算效率提升约50倍。
- FTVP仅适用于正序平衡系统，对零序/直流分量提取误差为100%，无法用于含不对称故障或电力电子直流注入的联合仿真。
- BFDP方法I仅使用正频系数，频谱搬移后无负频分量，包络为纯低通信号，适用于大时间步长(>1ms)仿真；方法II因Xh(t)下变频会在包络中引入3次谐波振荡分量，需额外滤波。
- 测试信号参数明确量化：基频幅值20，机电振荡幅值15/频率3Hz，直流偏置5，二次谐波幅值10，频率斜坡斜率-0.5π，为算法边界测试提供标准化基准。


## 关键公式

### GAM递归更新方程

$$$\langle x \rangle_k(t) = \langle x \rangle_k(t-\Delta t) + \frac{1}{N}[x(t)e^{-jk\omega_0 t} - x(t-N\Delta t)e^{-jk\omega_0(t-N\Delta t)}]$$$

*用于EMT仿真中实时、低延迟地提取任意次谐波动态相量，是联合仿真接口的核心数值实现*

### 三相解析信号构造矩阵

$$$z_{abc} = \hat{I} + j \frac{1}{\sqrt{3}} M x_{abc}$$$

*SFA框架下从三相瞬时值直接近似解析信号，避免全时域Hilbert变换，适用于三相不平衡系统*

### 基频动态相量合成方程

$$$\langle X \rangle_B(t) = 2\langle x \rangle_1(t) + X_h(t)$$$

*BFDP方法II核心公式，将全频谱信息压缩至单一基频参考系，大幅降低网络建模阶数*



## 验证详情

- **验证方式**: 数值仿真与理论频谱对比分析
- **测试系统**: 自定义多频带暂态测试信号模型(含基频、机电振荡、直流偏置、高次谐波、频率斜坡及三相不平衡分量)
- **仿真工具**: 基于MATLAB/自定义数值计算环境实现离散相量提取算法、FFT频谱分析与包络波形对比
- **验证结果**: 验证了各方法在不同暂态工况下的频谱搬移特性与计算边界。明确了GAM适用于多谐波精确建模但计算量大；SFA/BFDP适用于宽带信号降频处理；BFDP方法I在兼顾精度、负频抑制与计算效率方面最具EMT-动态相量联合仿真接口应用潜力，为大规模电力系统混合仿真提供了方法选型依据。
