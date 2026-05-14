---
title: "动态相量法 (Dynamic Phasor Method)"
type: method
tags: [dynamic-phasor, frequency-shift, emt-simulation, phasor-domain, multiscale-modeling, shifted-frequency-analysis]
created: "2026-04-30"
updated: "2026-05-10"
---

# 动态相量法 (Dynamic Phasor Method)

## 1. 物理背景与工程需求

动态相量法（Dynamic Phasor, DP）将时域带通信号搬移至基带，使基波或指定谐波附近的动态以低频包络形式描述，从而在系统级仿真中允许比详�EMT更大的时间步长。它不是传统稳态相量，也不是完整开关级 EMT 的替代品——它在高频瞬时细节和计算效率之间选择了一条折中路径。

动态相量法在 EMT 中的工程需求包括：

1. **多时间尺度建模**：将工频附近的带通信号搬移到基带，使状态变量变化速度低于原始瞬时波形，允许更大时间步长（Parvari 2025）
2. **机电-电磁混合仿真**：DP 区域覆盖以基频动态为主的系统区域，EMT 区域保留局部电磁暂态细节，通过 MATE 框架耦合（Tarazona 2021）
3. **MMC 等换流器的扩展频率建模**：基频动态相量（BFDP）将 MMC 内部多谐波动态统一在基频参考坐标系下，避免多频网络重复求解（Rupasinghe 2018）
4. **多速率仿真**：DP 区域使用大步长、EMT 区域使用小步长，通过接口插值实现同步

## 2. 数学描述

### 2.1 动态相量定义

对时域信号 $x(t)$，第 $k$ 阶动态相量定义为滑动窗口内的傅里叶系数：

$$
\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jk\omega_s\tau} d\tau
$$

逆变换：

$$
x(t) = \sum_{k=-K}^{K} \langle x \rangle_k(t) e^{jk\omega_s t}
$$

其中 $T$ 是滑动窗口，$\omega_s$ 是参考角频率，$K$ 是保留的谐波阶数。该定义隐含了窗口宽度、中心频率和保留阶数——离开这些参数谈"精度"或"加速比"没有可审核意义。

### 2.2 广义积分因子框架

Parvari (2025) 将传统 DP 推广为积分因子变换：

$$
x(t) = \mu(t) \mathbf{X}(t), \quad \mu(t) = e^{\int_0^t s(\tau)d\tau}, \quad s(t) = \frac{\mu'(t)}{\mu(t)}
$$

该变换保持 KCL/KVL 不变，但改变动态元件的本构关系：

- **电阻**：$\mathbf{V} = R\mathbf{I}$（不变）
- **电感**：$\mathbf{V} = L\frac{d\mathbf{I}}{dt} + L s(t) \mathbf{I}$（同值电感串联频移阻抗）
- **电容**：$\mathbf{I} = C\frac{d\mathbf{V}}{dt} + C s(t) \mathbf{V}$（同值电容并联频移导纳）
- **独立源**：$\mathbf{E}(t) = e(t)/\mu(t)$（乘以积分因子倒数）

线性时不变且 $s(t) = j\omega_0$ 时退化为传统 DP。

### 2.3 DP 域状态空间与特征值平移

$$
\dot{\mathbf{X}} = (A - sI)\mathbf{X} + B\mathbf{U}
$$

$$
\lambda_{\mathrm{DP},k} = \lambda_k - s
$$

Parvari (2025) 的核心发现：**DP 并不消除系统固有暂态模态**，而是将所有特征值沿虚轴平移 $-\mathrm{Im}(s)$，**实部（衰减率）完全不变**。因此 DP 使用大步长能准确描述被频移到低频附近的稳态分量，但对由系统特征值决定的暂态衰减/振荡模态仍受数值积分步长限制。

### 2.4 移位频率分析（SFA）

Tarazona (2021) 的 SFA 将带通信号表示为同相和正交分量：

$$
u(t) = u_I(t)\cos\omega_0 t - u_Q(t)\sin\omega_0 t
$$

$$
U(t) = u_I(t) + j u_Q(t)
$$

解析信号：$z(t) = u(t) + j\mathcal{H}[u(t)] = U(t)e^{j\omega_0 t}$，其中 $\mathcal{H}$ 为 Hilbert 变换。SFA 变换将频谱左移 $\omega_0$，使基频分量移至零频附近。

### 2.5 MMC 基频动态相量（BFDP）

Rupasinghe (2018) 针对 MMC 提出 BFDP，将各次谐波统一映射至基频参考系：

$$
X_B(t) = \langle x \rangle_0(t) e^{-j\frac{2\pi}{T}(t-T+s)} + 2\sum_{k=1}^{+\infty} \langle x \rangle_k(t) e^{j(k-1)\frac{2\pi}{T}(t-T+s)}
$$

## 3. 计算模型与离散化

### 3.1 微分和乘积的 DP 域运算规则

**微分规则**：
$$
\langle \frac{dx}{dt} \rangle_k = \frac{d\langle x \rangle_k}{dt} + jk\omega_s \langle x \rangle_k
$$

**乘积规则**（卷积和）：
$$
\langle xy \rangle_k = \sum_{i=-K}^{K} \langle x \rangle_{k-i} \langle y \rangle_i
$$

**电感方程**：$\langle v_L \rangle_k = L\frac{d\langle i_L \rangle_k}{dt} + jk\omega_s L \langle i_L \rangle_k$

**电容方程**：$\langle i_C \rangle_k = C\frac{d\langle v_C \rangle_k}{dt} + jk\omega_s C \langle v_C \rangle_k$

### 3.2 DP 伴随电路离散化

Parvari (2025) 将 DP 域连续时间伴随电路用梯形积分离散：

$$
z_k = \frac{1 + \lambda_k \Delta t/2}{1 - \lambda_k \Delta t/2}
$$

当 $|\lambda \Delta t|$ 较大时，无论 EMT 还是 DP 都会产生模态幅值或相位误差——DP 将工频正弦量移至零频，因此稳态响应可用大步长；暂态衰减模态的 $\lambda$ 实部未改变，步长选择仍需尊重系统固有时间常数。

### 3.3 SFA-EMT 多速率接口（Tarazona 2021）

SFA-EMT 混合仿真在 MATE 框架下运行：

1. SFA 子系统用大步长求解复值低频包络
2. 并行运行实部 EMT 和虚部 EMT 仿真器跟踪SFA复解的实部和虚部
3. 接口处通过 Thévenin 等效交换端口量
4. 多速率同步/插值在 SFA 大步长和 EMT 小步长之间传递变量

$$
I_L = Z_T^{-1} E_L, \quad V_j = e_j - Y_j^{-1} C_j I_L
$$

### 3.4 BFDP 的离散化（Rupasinghe 2018）

MMC 的 BFDP 模型在每个步长内：

1. NLC 调制生成子模块投切状态
2. 桥臂变量和/差分解耦 → 分离共模/差模动态
3. BFDP 频移 → 单一基频复数状态空间方程
4. 离散化为受控源 + 并联导纳 → 直接注入全局节点导纳矩阵
5. 外部网络单频求解，反变换输出时域波形

步长从详细模型的 2--5 $\mu$s 放宽至 50 $\mu$s，效率提升 15--25 倍。

## 4. 实现方法与算法细节

### 4.1 DP 变体对比

| 变体 | 机制 | 适用场景 | 代价 |
|------|------|----------|------|
| 基波动态相量（$K=0$） | 仅保留基波复包络 | 机电-电磁接口、VSC/HVDC 慢动态 | 不保留谐波 |
| 多频动态相量（$K \geq 1$） | 保留多个 $k$ 阶分量 | 谐波耦合、MMC 环流 | 阶数越高复杂度越大 |
| 移位频率分析（SFA） | 解析信号 $z(t) = u + j\mathcal{H}[u]$ 频移至基带 | 混合 SFA-EMT 系统级仿真（Tarazona 2021） | 需双 EMT 副本跟踪复解 |
| 基频动态相量（BFDP） | 全谐波映射至基频参考系 | MMC 等多谐波换流器 EMT（Rupasinghe 2018） | 内部谐波建模精度受限 |
| 广义积分因子 DP | $x = \mu(t)X$ 任意频移函数（Parvari 2025） | 理论框架、特征值分析 | 通用性强但实现复杂 |

### 4.2 阶数选择准则

| 保留阶数 $K$ | 适用场景 | 计算复杂度 | 精度特点 |
|----------|----------|------------|----------|
| 0 | 系统级慢动态 | 最低 | 仅基波平均 |
| 1 | VSC/HVDC 基本动态 | 低 | 含主要谐波耦合 |
| 2--3 | MMC 环流、谐波耦合 | 中等 | 较好 |
| $\geq 5$ | 宽频振荡、详细分析 | 较高 | 接近全 EMT |

### 4.3 离散时间特征值约束

Parvari (2025) 强调：DP 大步长收益并非无条件。当使用梯形积分离散化时，系统特征值 $\lambda$ 与步长 $\Delta t$ 的乘积 $|\lambda \Delta t|$ 决定了数值精度。DP 将基频分量移至零频仅改善稳态表示——暂态模态的衰减率（$\mathrm{Re}(\lambda)$）不变，因此 DP 不能绕过系统固有暂态时间常数对步长的约束。

### 4.4 外部网络 BFDP 接口

Rupasinghe (2018) 的 BFDP 通过将 MMC 内部多谐波动态统一在基频参考系下，使外部网络只需一个基频导纳矩阵。相比传统多频 DP 方法，外部网络导纳矩阵维度降低为 $1/N$（$N$ 为保留谐波阶数），且矩阵求逆计算量减少约 90%。

## 5. 适用边界与失效模式

### 适用条件

- 信号能量集中在被保留的中心频率和选定谐波附近（Parvari 2025）
- 系统区域以基频附近机电动态为主，其他区域需详细 EMT（Tarazona 2021）
- MMC 等换流器的多谐波动态需在系统级 EMT 仿真中保留（Rupasinghe 2018）

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| 暂态阶段大步长误差 | DP 未改变 $\mathrm{Re}(\lambda)$，暂态模态仍受 $\Delta t$ 约束（Parvari 2025） | 暂态波形和衰减包络失真 |
| 阶数选择不足 | 截断频率包含显著能量 | 被截断谐波折叠为误差 |
| 参考频率失配 | PLL 失锁或多频电网使包络不再慢变 | DP 变量不再为低频 |
| 强非线性信号 | 铁磁饱和、电弧、限幅产生宽频分量 | DP 模型只能在分段假设下使用 |
| 开关频率附近谐波 | DP 保留阶数通常不及开关频率 | 开关纹波和载波边带丢失 |

### 关键约束

- Parvari (2025) 的结论在二阶 RLC 电路和 IEEE 9 节点系统中验证，不保证外推到高频开关场景
- Tarazona (2021) 的 SFA-EMT 混合协议在 IEEE 39 节点系统验证，原文未报告具体加速倍数或误差百分比
- Rupasinghe (2018) 的 BFDP 在 MMC 逆变器、背靠背 HVDC 和 12 节点系统中验证，结论绑定 PSCAD/EMTDC 平台和 50 $\mu$s 步长
- DP 与 EMT 混合仿真时，接口变量的形式（瞬时值、复包络、功率量）和同步方式需明确说明

## 6. 应用案例

### 案例 1：DP 大步长暂态精度分析（Parvari 2025）

场景：二阶 RLC 电路和 IEEE 9 节点系统。传统 DP 将基频正弦量移至零频，稳态响应可用毫秒级步长。但特征值分析显示 DP 域特征值 $λ_{\text{DP}} = λ - j\omega_0$，实部不变——暂态模态仍受 $|λ \Delta t|$ 约束。IEEE 9 节点系统在故障暂态阶段大步长 DP 精度显著受限。

### 案例 2：SFA-EMT 多速率混合仿真（Tarazona 2021）

场景：IEEE 39 节点系统中，部分区域用 SFA（大步长复包络），局部区域用 EMT（小步长瞬时值）。MATE 框架通过双 EMT 副本（实部 + 虚部）保持 SFA 复值解的解析性。SFA 区域步长可达毫秒级，EMT 区域保持微秒级。

### 案例 3：MMC 的 BFDP 扩展频率建模（Rupasinghe 2018）

场景：MMC 逆变器系统、背靠背 HVDC 和 12 节点交流系统。BFDP 将 MMC 内部多谐波动态统一至基频参考系，外部网络只需单频导纳矩阵。步长从 2--5 $\mu$s 放宽至 50 $\mu$s，效率提升 15--25 倍。基波及 2--7 次谐波幅值误差 $< 0.5\%$，相位偏差 $< 0.3^°$。

## 7. 延伸阅读

- [[average-value-model]]：平均值模型保留低频平均量；DP 可保留多个频率包络
- [[switching-function-method]]：开关函数可作为 DP 方程中的调制输入
- [[multirate-method]]：DP 子系统和 EMT 子系统的多速率耦合
- [[co-simulation]]：DP 作为混合仿真接口中的一种降阶表达
- [[state-space-method]]：DP 模型最终写成复数扩展的状态空间方程
- [[harmonic-analysis]]：谐波分析偏向诊断；DP 把谐波作为状态推进
- [[phase-locked-loop]]：PLL 的同步角在 SFA 中确定参考坐标系
- [[model-order-reduction]]：DP 可以看作频域模型降阶的一种形式

*页面基于 Parvari (2025)、Tarazona (2021) 和 Rupasinghe (2018) 的证据写作。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[dynamic-model-reduction-of-power-electronic-interfaced-generators-based-on-singu|Dynamic model reduction of power electronic interfaced gener]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[reduced-order-dynamic-model-of-modular|Reduced-Order Dynamic Model of Modular]] | 2019 |
| [[reduced-order-dynamic-model-of-modular|Reduced-Order Dynamic Model of Modular]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[dynamic-equivalence-method-of-ddpmsg-wind-farm-for-sub-synchronous-oscillation-a|Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synch]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[analytical-model-building-for-type-3-wind-farm-subsynchronous-oscillation-analys|Analytical model building for Type-3 wind farm subsynchronou]] | 2021 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[extending-the-frequency-bandwidth-of-transient-stability-simulation-using-dynami|Extending the Frequency Bandwidth of Transient Stability Sim]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size el]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[2728modeling|Modeling_of_LCC_HVDC_Systems_Using_Dynam]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[an-interface-method-for-co-simulation-of-emt-model-and-shifted-frequency-emt-mod|An Interface Method for Co-Simulation of EMT Model and Shift]] | 2025 |
| [[an-interface-method-for-co-simulation-of-emt-model-and-shifted-frequency-emt-mod|An Interface Method for Co-Simulation of EMT Model and Shift]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[improving-emt-simulations-using-frequency-shifted-rational-approximations|Improving EMT simulations using frequency-shifted rational a]] | 2025 |
| [[improving-emt-simulations-using-frequency-shifted-rational-approximations|Improving EMT simulations using frequency-shifted rational a]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[type-3-wind-turbine-generator-model-with-generic-high-level-control-for-electrom|Type-3 wind turbine generator model with generic high-level ]] | 2025 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[vsc-hvdc-系统的动态相量法建模仿真分析|VSC-HVDC 系统的动态相量法建模仿真分析]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
