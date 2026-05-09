---
title: "动态相量法 (Dynamic Phasor Method)"
type: method
tags: [dynamic-phasor, frequency-shift, emt-simulation, phasor-domain, multiscale-modeling]
created: "2026-04-30"
---

# 动态相量法 (Dynamic Phasor Method)

## 定义与边界

动态相量法（Dynamic Phasor Method）把围绕一个或多个中心频率变化的电压、电流或状态量表示为缓慢变化的复包络。它不是传统稳态相量，也不是完整开关级 EMT 的替代品；它牺牲部分高频瞬时细节，换取对基波、低阶谐波或指定频带动态的低阶描述。

对时域信号 $x(t)$，第 $k$ 阶动态相量常写为 $\langle x\rangle_k(t)=\frac{1}{T}\int_{t-T}^{t}x(\tau)e^{-jk\omega_s\tau}d\tau$。其中 $T$ 是滑动窗口，$\omega_s$ 是参考角频率，$k$ 是保留的频率分量。该定义隐含了窗口、中心频率和保留阶数；离开这些设置谈“精度”或“加速比”没有可审核意义。

## EMT 中的作用

在 EMT 中，动态相量法主要用于多时间尺度建模：把工频附近的带通信号搬移到基带，使状态变量变化速度低于原始瞬时波形。典型对象包括 [[mmc-model]]、[[vsc-model]]、HVDC 外部等值、准稳态谐波传播和机电-电磁接口中的慢动态表达。

它适合回答“某些频带的包络如何变化”，不适合单独回答“开关沿、雷击陡波、保护动作瞬间的全频谱波形如何变化”。若研究目标是子模块器件应力、开关损耗或高频绝缘暂态，应优先使用详细开关模型、[[discretization-methods]] 和常规 [[nodal-analysis]]。

```mermaid
graph LR
    subgraph 时域
        xt["x(t)
原始信号"]
    end
    subgraph 频谱
        Xf["X(ω)
频谱"]
    end
    subgraph 动态相量
        Xk["⟨x⟩_k(t)
第k阶复包络"]
    end
    subgraph 移频分析
        Xs["x_e(t) = x_a·e^{-jω_c t}
移频包络"]
    end
    xt -->|Fourier变换| Xf
    xt -->|滑动窗+频移| Xk
    xt -->|Hilbert+频移| Xs
    Xf -->|带通滤波+下变频| Xk
    Xf -->|单边带搬移| Xs

    style xt fill:#e1f5fe
    style Xf fill:#fff3e0
    style Xk fill:#c8e6c9
    style Xs fill:#f3e5f5

## 核心机制

动态相量的核心是频谱搬移和截断。若信号可表示为 $x(t)\approx \sum_{k=-K}^{K}X_k(t)e^{jk\omega_s t}$，则 $X_k(t)$ 是慢变包络；微分和乘积在相量域中分别变为

- 微分：$\langle \dot{x}\rangle_k=\frac{d\langle x\rangle_k}{dt}+jk\omega_s\langle x\rangle_k$。
- 乘积：$\langle xy\rangle_k=\sum_i \langle x\rangle_{k-i}\langle y\rangle_i$。

因此，电感、电容、控制器和调制函数会从瞬时微分方程变成多个相量阶数之间的耦合方程。保留阶数越多，越能表达谐波耦合；阶数越少，计算越轻，但未保留频率会被截断或折叠为误差。

在移位相量实现中，也可先构造解析信号 $x_a(t)=x(t)+jx_q(t)$，再做 $x_e(t)=x_a(t)e^{-j\omega_c t}$。这里 $x_q(t)$ 可以由 Hilbert 变换、滤波器或近似正交生成方法得到；不同构造方式的误差应按论文或实现报告绑定，而不应写成通用优劣排序。

## 分类与变体

| 变体 | 输入与状态 | EMT 用途 | 边界 |
|------|------------|----------|------|
| 基波动态相量 | 基波复包络和低阶控制状态 | 机电-电磁接口、VSC/HVDC 慢动态 | 不保留开关纹波 |
| 多频动态相量 | 多个 $k$ 阶分量 | 谐波耦合、MMC 环流、低阶宽频振荡 | 阶数选择影响结果 |
| 移位相量模型 | 解析信号或正交分量 | FPGA/实时仿真中的带通信号降频 | 正交信号构造需验证 |
| 动态相量-节点混合 | 相量域设备接入节点网络 | 局部设备降阶、系统级 EMT | 接口变量和步长需一致 |

## 适用边界与失败模式

- 带宽边界：信号能量应主要集中在被保留的中心频率和谐波附近；故障陡波、雷电暂态和高频电缆振荡通常需要额外频段或全 EMT。
- 频率边界：参考频率偏移、PLL 失锁或多频率电网会使包络不再慢变。
- 非线性边界：铁磁饱和、电弧、限幅控制和开关死区会产生宽频分量，动态相量模型只能在明确工作点或分段假设下使用。
- 接口边界：与 [[co-simulation]]、[[multirate-method]] 或 RMS 侧耦合时，应说明接口变量是瞬时值、复包络还是功率量。
- 证据边界：原页面中”5-10 倍步长””误差 <1%””206 倍提速”等数字没有在本页绑定到测试系统、平台和论文表图，因此不作为通用结论保留。

### 阶数选择准则

| 保留阶数 | 适用场景 | 计算复杂度 | 精度 |
|----------|----------|------------|------|
| $K=0$（平均值） | 系统级慢动态 | 最低 | 仅基波 |
| $K=1$（基波+一阶谐波） | VSC/HVDC基本动态 | 低 | 含主要谐波 |
| $K=2\sim3$ | MMC环流、谐波耦合 | 中等 | 较好 |
| $K\geq5$ | 宽频振荡、详细分析 | 较高 | 接近全EMT |

```mermaid
flowchart LR
    subgraph 原始信号
        xt["x(t)
时域信号"]
    end
    subgraph 频谱搬移
        direction LR
        Xf["X(ω)
双边频谱"]
        Bp["带通滤波
保留kω₀附近"]
        Shift["频率搬移
乘以 e^{-jkω₀t}"]
        Lp["低通滤波
截取基带"]
    end
    subgraph 结果
        Xk["⟨x⟩_k(t)
k阶动态相量
慢变复包络"]
    end

    xt -->|傅里叶变换| Xf
    Xf --> Bp --> Shift --> Lp --> Xk

    style xt fill:#e1f5fe
    style Xf fill:#fff3e0
    style Bp fill:#f5f5f5
    style Shift fill:#f5f5f5
    style Lp fill:#f5f5f5
    style Xk fill:#c8e6c9
```

### 与其他方法的对比

| 特性 | 全EMT | 动态相量 | 平均值模型 |
|------|-------|----------|------------|
| 开关细节 | 完整 | 包络 | 平均 |
| 计算效率 | 低 | 中等 | 高 |
| 适用频段 | 全频带 | 选定频带 | 基波附近 |
| 谐波耦合 | 精确 | 截断阶数内 | 无 |
| 非线性处理 | 直接 | 近似 | 工作点线性化 |

## 代表性来源

| 来源 | 支撑内容 | 使用边界 |
|------|----------|----------|
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]] | 移位相量用于混合 MMC 子模块和桥臂等效，并在 FPGA 实时仿真平台验证 | 证据限于原文两端 LVDC/MMC 系统和给定硬件实现 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode]] | 动态相量、离散时间和频率扫描方法可用于 SSR 模态建模对比 | 不能外推为所有宽频振荡场景的优选 |
| [[dynamic-synchrophasor-estimator-based-on-multi-frequency-phasor-model]] | 多频相量模型可支撑动态同步相量估计 | 属于测量/估计场景，不等同于全 EMT 设备模型 |

## 形式化表达

### 动态相量系数求解

对于周期为 $T$ 的信号 $x(t)$，第 $k$ 阶动态相量系数：

$$\langle x \rangle_k(t) = \frac{1}{T}\int_{t-T}^{t} x(\tau) e^{-jk\omega_s\tau} d\tau$$

逆变换：
$$x(t) = \sum_{k=-K}^{K} \langle x \rangle_k(t) e^{jk\omega_s t}$$

### 微分和乘积运算规则

**微分规则**：
$$\langle \frac{dx}{dt} \rangle_k = \frac{d\langle x \rangle_k}{dt} + jk\omega_s \langle x \rangle_k$$

**乘积规则**（卷积和）：
$$\langle xy \rangle_k = \sum_{i=-K}^{K} \langle x \rangle_{k-i} \langle y \rangle_i$$

**电感方程**：
$$\langle v_L \rangle_k = L\frac{d\langle i_L \rangle_k}{dt} + jk\omega_s L \langle i_L \rangle_k$$

**电容方程**：
$$\langle i_C \rangle_k = C\frac{d\langle v_C \rangle_k}{dt} + jk\omega_s C \langle v_C \rangle_k$$

### 复数状态空间形式

将各阶动态相量组成状态向量 $\mathbf{X} = [\langle x \rangle_{-K}, ..., \langle x \rangle_0, ..., \langle x \rangle_K]^T$，可写成状态空间形式：

$$\dot{\mathbf{X}} = \mathbf{A}_{dp}\mathbf{X} + \mathbf{B}_{dp}\mathbf{U}$$

其中 $\mathbf{A}_{dp}$ 包含原系统矩阵和频率耦合项 $jk\omega_s$。

### 移位相量实现

构造解析信号：
$$x_a(t) = x(t) + j\mathcal{H}\{x(t)\}$$

其中 $\mathcal{H}$ 为Hilbert变换。移位到基带：
$$x_{dp}(t) = x_a(t)e^{-j\omega_c t}$$

## 与相关页面的关系

- [[average-value-model]]：平均值模型通常只保留低频平均量；动态相量可保留多个频率包络，边界更接近频谱截断。
- [[switching-function-method]]：开关函数可作为动态相量方程中的调制输入；若开关函数高频分量被截断，开关纹波不会被完整表达。
- [[harmonic-analysis]]：谐波分析偏向频谱诊断；动态相量把选定谐波作为状态随时间推进。
- [[state-space-method]]：动态相量模型常最终写成复数或实数扩展的状态空间方程。
- [[real-time-simulation]]：动态相量可降低实时计算压力，但是否满足实时 deadline 取决于硬件、步长、阶数和接口实现。

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
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size el]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[2728modeling|Modeling_of_LCC_HVDC_Systems_Using_Dynam]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
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
