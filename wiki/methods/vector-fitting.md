---
title: "矢量拟合"
type: method
tags: []
created: "2026-04-13"
---

# 矢量拟合

## 定义与边界

矢量拟合（Vector Fitting, VF）是一种频域有理函数逼近方法，用迭代极点重定位把离散频率响应拟合为极点-留数模型。常见目标形式为 $H(s)\approx\sum_{m=1}^{M}\frac{R_m}{s-p_m}+D+sE$；多端口导纳可写为 $\mathbf{Y}(s)\approx\sum_m\frac{\mathbf{R}_m}{s-p_m}+\mathbf{D}+s\mathbf{E}$。

VF 解决的是“由频域采样得到可时域实现的有理模型”。它不直接保证模型接入 EMT 后无源、稳定或实时可运行；这些需要 [[passivity-enforcement]]、[[state-space-method]]、离散化和时域验证。它也不负责给出物理材料参数，除非拟合模型与物理参数之间有额外映射。

## EMT 中的作用

VF 是 [[frequency-dependent-modeling]] 和 [[fdne-model]] 的关键工具。线路、电缆、变压器、外部网络和黑箱设备的阻抗/导纳频率响应经过 VF 后，可转为递推卷积、状态空间模型或等效 RLC 网络，从而进入 EMT 时间步进。

VF 的价值在于把宽频响应压缩为有限阶模型。模型阶数、频率范围、采样密度、权重和初始极点决定拟合结果；离开这些条件谈“高精度”“最优”或“实时”都不够严谨。

```mermaid
graph TD
    subgraph 初始设置
        A[频域采样数据 H(s_j)]
        B[设置起始极点 ā₁,...,āₚ]
    end
    subgraph 迭代求解
        C[Step 1: 求解线性LS问题]
        D[提取σ(s)的零点作为新极点]
        E{极点收敛?}
        C --> D --> E
        E -->|否| C
    end
    subgraph 最终求解
        F[Step 2: 固定极点求留数]
        G[检查无源性 passivity]
        F --> G
    end
    subgraph 输出
        H[有理函数模型]
        I[状态空间实现 / FDNE / RLC网络]
        H --> I
    end
    A --> C
    B --> C
    E -->|是| F

    style A fill:#e3f2fd
    style B fill:#e3f2fd
    style C fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#e8f5e9
    style G fill:#e8f5e9
    style H fill:#f3e5f5
    style I fill:#f3e5f5
```

## 核心机制

标准 VF 通过辅助函数 $\\sigma(s)$ 把同时优化极点和留数的非线性问题拆成线性最小二乘问题。给定起始极点 $\bar{p}_m$，先拟合 $\sigma(s)H(s)$ 与 $\sigma(s)$，再把 $\sigma(s)$ 的零点作为更新极点。极点收敛后，固定极点重新求留数、直接项和高频项。

对多端口系统，常采用公共极点策略：所有矩阵元素共享同一组极点，但留数为矩阵。这样有利于统一状态空间实现，却可能增加阶数。若导纳矩阵小特征值很重要，普通元素级误差可能不足以控制高阻抗端接下的响应误差，需要模态加权或模态 VF。

## 分类与变体

| 变体 | 机制 | EMT 用途 | 边界 |
|------|------|----------|------|
| 标准 VF | 两阶段极点重定位和留数识别 | 单端口或矩阵元素频响拟合 | 对初始极点、权重和频段敏感 |
| 复数 VF | 允许独立复极点或复数域响应 | 基带、非对称或变换域模型 | 实值时域实现需额外处理 |
| 模态 VF | 在模态分量上加权拟合 | 多端口 FDNE、小特征值保护 | 依赖模态变换和矩阵对称性 |
| 快速/并行 VF | 利用稀疏结构、QR 和底层线性代数 | 大规模端口或高采样数拟合 | 加速量绑定实现平台 |
| VF + 降阶 | 拟合后截断弱状态或做 MOR | 实时仿真和 HIL | 降阶后需重新检查误差和无源性 |

## 适用边界与失败模式

- 采样边界：采样点应覆盖 DC 或最低关注频率至最高关注频率；谐振峰附近需要更密集采样。
- 初始极点边界：起始极点不足或分布不当会导致局部拟合差、冗余阶数或不稳定极点。
- 权重边界：幅值很小的通道、小特征值和高阻抗端接需要相对误差控制，不能只看绝对 RMS。
- 无源性边界：拟合曲线匹配不代表 $\mathbf{Y}(j\omega)$ 正实；非无源模型可能在 EMT 中发散。
- 非线性边界：VF 拟合线性频响；饱和、开关限幅和控制模式切换只能通过分段或多工作点处理。
- 证据边界：原页面中的“首次”“最优”“机器精度”“20-25 倍”等强结论只在对应论文和算例中成立，本页改为论文级证据，不写成领域共识。

## 代表性来源

| 来源 | 支撑内容 | 使用边界 |
|------|----------|----------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] | 复数起始极点扩展 VF，用于含谐振峰的频域响应有理逼近 | 原始抽取中未完整给出所有算例表图；数值精度需回原文核对 |
| [[fast-realization-of-the-modal-vector-fitting]] | 快速模态 VF 面向多端口导纳矩阵和小特征值模态 | 加速和误差结论依赖原文 FDNE 算例与实现 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin]] | 比较 VF、矩阵束、Loewner 等曲线拟合/降阶方法 | 选型结论应限于其测试算例 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-]] | VF 用于多相线路和频变土壤参数相关暂态建模 | 证据限于原文线路、土壤和频率设置 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend]] | 并行/底层实现可改善 FDNE 有理逼近计算性能 | 不能外推为所有端口规模和硬件平台 |

## 与相关页面的关系

- [[parameter-identification]]：VF 是频域参数辨识的一种特化形式。
- [[prony-analysis]]：Prony 从时域响应拟合指数模态；VF 从频域响应拟合有理函数。
- [[passivity-enforcement]]：VF 后处理常需要无源性检测和修正，尤其是多端口导纳。
- [[state-space-method]]：极点-留数结果常转换为状态空间参与 EMT 步进。
- [[model-order-reduction]]：VF 模型阶数偏高时，可进一步降阶，但需重新验证频域和时域误差。
- [[wideband-modeling]]：VF 是宽频模型的常用实现路径，但不是唯一选择。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS V]] | 2004 |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP - Power Deli]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[fast-realization-of-the-modal-vector-fitting|Fast Realization of the Modal Vector Fitting]] | 2009 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[parametric-study-of-transient-electromagnetic-fields|Parametric Study of Transient Electromagnetic Fields]] | 2011 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri|Proposal of an alternative transmission line model for symme]] | 2011 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[published-in-iet-generation-transmission-distribution-27&28|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2013 |
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model|Fitting the frequency-dependent parameters in the Bergeron l]] | 2014 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method|Frequency-dependent multiconductor line model based on the B]] | 2015 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method|Frequency-dependent multiconductor line model based on the B]] | 2015 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies|A Wideband Equivalent Model of Type-3 Wind Power Plants for ]] | 2016 |
| [[extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe|Extension of a modal-domain transmission line model for incl]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[an-electromagnetic-model-for-the-calculation-of-tower-surge-impedance-based-on-t|An Electromagnetic Model for the Calculation of Tower Surge ]] | 2020 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[lightning-induced-voltage-analysis-on-a-three-phase-compact-distribution-line-co|Lightning-induced voltage analysis on a three-phase compact ]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[evaluation-of-the-extended-modal-domain-model-in-the-calculation-of-lightning-in|Evaluation of the extended modal-domain model in the calcula]] | 2021 |
| [[expanding-the-measuring-range-via-s-parameters-in-a-ehv-voltage-transformer-mode|Expanding the measuring range via S-parameters in a EHV volt]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[implementation-of-the-universal-line-model-in-the-alternative-transients-program|Implementation of the universal line model in the alternativ]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-|A Thévenin-Type Version of the Extended Modal-Domain Model f]] | 2023 |
| [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-|A Thévenin-Type Version of the Extended Modal-Domain Model f]] | 2023 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient|Comparison of soil modeling concerning physical factors: App]] | 2023 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-Conductor Cable Modeling With Inclusion of Measured Co]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-|Calculation of lightning-induced voltages on a large-scale d]] | 2025 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[improving-emt-simulations-using-frequency-shifted-rational-approximations|Improving EMT simulations using frequency-shifted rational a]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |
