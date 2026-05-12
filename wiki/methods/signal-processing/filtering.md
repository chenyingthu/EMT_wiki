---
title: "滤波方法 (Filtering in EMT)"
type: method
tags: [filtering, signal-processing, low-pass-filter, measurement, harmonic-extraction]
created: "2026-05-05"
updated: "2026-05-11"
---

# 滤波方法 (Filtering in EMT)

## 物理背景与工程需求

在电磁暂态（EMT）仿真中，电压和电流波形包含从直流到数十千赫兹的宽频信息。滤波技术的工程需求来自以下几个层面：
- **测量信号处理**：保护和控制算法需要从含噪声和高频暂态的 EMT 波形中提取稳定的基波或低频信息。
- **抗混叠**：数字控制系统采样前需要低通滤波以防止高频分量折叠到控制频带。
- **谐波/间谐波分离**：在电能质量和谐振分析中需要将特定频段分量从宽频谱中分离。
- **同步信号提取**：PLL 等同步环节需要在电压畸变或不平衡条件下提取基波正序分量。

滤波方法在 EMT 中不是独立算法，而是嵌入在测量链、控制回路、保护判据和混合仿真接口中的基础环节。其带宽、阶数和实现方式直接影响 EMT 仿真结果的可用性。

## 数学描述

### 一阶低通滤波器

一阶低通滤波器（LPF）在连续域的传递函数为：

$$H(s) = \frac{\omega_c}{s + \omega_c}$$

其中 $\omega_c = 2\pi f_c$ 为截止角频率。一阶 LPF 的阶跃响应上升时间 $t_r \approx 0.35/f_c$，这意味着滤波器的截止频率越低，引入的测量延迟越大。

### 二阶低通滤波器

二阶 LPF 提供更陡的阻带衰减：

$$H(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

其中 $\omega_n$ 为自然角频率，$\zeta$ 为阻尼系数。二阶滤波器在 $\zeta = 0.707$ 时获得最平坦的通带响应（Butterworth 配置）。

### 滑动平均滤波器

滑动平均滤波器是最简单的 FIR 低通实现，在时域为：

$$y[k] = \frac{1}{N}\sum_{i=0}^{N-1} x[k-i]$$

其幅频响应在 $f = k \cdot f_s/N$（$k = 1,2,\dots$）处具有陷波特性，可用于抑制特定谐波。

## 计算模型与离散化

### 一阶 LPF 的离散化

使用后向欧拉法离散一阶 LPF：

$$y[k] = \frac{T_s \omega_c}{1 + T_s \omega_c} x[k] + \frac{1}{1 + T_s \omega_c} y[k-1]$$

使用梯形法（Tustin）离散一阶 LPF：

$$y[k] = \frac{T_s \omega_c}{2 + T_s \omega_c} (x[k] + x[k-1]) + \frac{2 - T_s \omega_c}{2 + T_s \omega_c} y[k-1]$$

### 双二阶滤波器结构

DSOGI（双二阶广义积分器）是一种频率自适应的带通滤波器，其传递函数为：

$$D(s) = \frac{k\omega' s}{s^2 + k\omega' s + \omega'^2}, \quad Q(s) = \frac{k\omega'^2}{s^2 + k\omega' s + \omega'^2}$$

其中 $D(s)$ 为带通输出，$Q(s)$ 为低通输出（正交信号），$\omega'$ 为自适应中心频率，$k$ 为阻尼系数。[[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]（Ranasinghe 等，2024）采用此结构作为 PLL 的前端滤波器，在不对称故障下将调节时间从 0.040 s 缩短至 0.016 s（缩短 60%），频率跟踪 RMSE 从 2.16 Hz 降至 0.001 Hz（降幅 99.95%）。

## 实现方法与算法细节

### 测量链中的滤波

在 EMT 程序中，电压和电流测量信号在进入控制算法之前通常先经过模拟抗混叠滤波器（建模为一阶或二阶 LPF）和数字滤波器。测量链的总延迟是滤波器阶数、截止频率和采样周期的函数，需要在控制设计时计入。

### PLL 中的滤波

SRF-PLL 通常使用 LPF 滤波 d 轴电压以提取频率误差信号。[[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]]（Luchini 等，2023）在 ATP/ATPDraw 中实现了两种 PLL 方案：LPF-PLL（传统低通滤波+PLL）和 DSOGI-PLL（双二阶广义积分器正交信号发生器+正序分量计算），其中 DSOGI 结构在电网电压畸变条件下可有效抑制谐波干扰，故障条件下平均误差约 2.33%。

### 基于滤波器组的并行 EMT 计算

[[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks]]（Zuluaga，2021）将长卷积计算拆分为多相 QMF（正交镜像滤波器）滤波器组的并行子运算。该方法在 17 母线网络算例中实现了超过 100 倍实时的仿真速度，与 PSCAD/EMTDC 结果一致，适用于统计性绝缘配合等需要大量重复仿真的场景。

### H∞ 混合灵敏度滤波

[[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]（Zhang 等，2022）将 MMC-HVDC 链路延时对高频稳定性的影响等效为外部干扰，通过混合灵敏度 H∞ 优化设计抑制滤波器，将 1 kHz-1.5 kHz 频段的相位裕度提升约 25°，抑制带宽扩大 1.8 倍，优于经验试凑的低通滤波器方案。

## 适用边界与失效模式

### valid_when
- 信号的频带与被提取目标频带可分离（如基波与高次谐波、低频振荡与高频噪声）
- 滤波器引入的相移和群延迟在控制或保护允许的延时范围内
- 截止频率远高于控制闭环带宽（通常 > 5-10 倍）以避免滤波器动态影响控制稳定性
- 用于动态相量提取时，滤波器带宽需覆盖预期的机电振荡频率范围（通常 0.1-3 Hz）

### invalid_when
- 信号与噪声频带重叠时，线性滤波无法同时满足衰减和保真度
- 保护和快速控制场景下，过度平滑可能遮蔽真实暂态信息导致判据延迟或误动
- 滤波器群延迟在闭环控制系统中可能引入额外的相位裕度损失
- 宽频 EMT 研究中，单一截止频率的 LPF 无法同时保留高频暂态和抑制数值噪声

### assumptions
- 滤波对象为线性时不变系统（LTI），滤波器设计与信号统计特性无关（据方法推断）
- 数字滤波器的采样率满足奈奎斯特准则（据方法推断）
- 滤波器离散化方法的稳定性和精度在目标频带内可接受（据方法推断）

### evidence_gaps
- 不同滤波器类型（Butterworth、Chebyshev、Elliptic）在 EMT 暂态响应中的具体差异，原文未提供跨场景的系统对比
- DSOGI 自适应频率跟踪在极弱电网（SCR < 1.5）下的滤波性能边界，原文未报告可核验的数值结果
- QMF 滤波器组方法在包含详细电力电子和快速控制闭环的 EMT 系统中的适用性，原文未验证

## 应用案例

### DSOGI-PLL 滤波在弱电网同步中的应用

[[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]（Ranasinghe 等，2024）在 PSCAD/EMTDC 中实现了改进型 DSOGI-PLL，DSOGI 作为前端带通滤波器提取基波正序分量。在替换同步发电机的 IEEE 9 节点系统（SCR ≈ 1.8）中，改进 DSOGI-PLL 在不对称故障下调节时间缩短 60%，超调量降低 58.5%。

### QMF 滤波器组并行 EMT 仿真

[[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks]]（Zuluaga，2021）利用多相 QMF 滤波器组将长卷积分解为并行子运算，在 FPGA 上实现了开关暂态 EMT 的 >100 倍实时仿真速度，验证系统为 17 节点配电网络，与 PSCAD/EMTDC 对比验证了波形一致性。

### 动态相量提取中的滤波

[[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a]]（Rupasinghe，2021）评估了广义平均法（GAM）从 EMT 自然波形中提取低通动态相量的滤波特性。GAM 的离散递归算法将单步计算复杂度从 2N 次运算降至 4 次运算，当窗口长度 N=100 时计算效率提升约 50 倍。该方法适用于 EMT-动态相量联合仿真接口中的相量提取。

## 延伸阅读

- [[fourier-filtering]]：基于傅里叶变换的频谱滤波方法。
- [[fft]]：频域分量提取基础。
- [[phasor-measurement-unit]]：测量链中的动态滤波和相量估计。
- [[signal-processing]]：更上位的信号处理方法入口。
- [[dsogi-pll]]：DSOGI 滤波在 PLL 同步环节中的应用。
- [[harmonic-analysis-methods]]：谐波分析和滤波相关的频域方法。
- [[passivity-enforcement]]：滤波器设计中的无源性强制方法。
- [[average-value-model]]：滤波与平均化的区别和联系。
