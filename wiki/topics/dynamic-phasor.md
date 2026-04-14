---
title: "动态相量法 (Dynamic Phasor Method)"
type: topic
tags: [dynamic-phasor, sfa, shifted-frequency, frequency-domain]
created: "2026-04-13"
---

# 动态相量法 (Dynamic Phasor Method)

## 概述

动态相量法（Dynamic Phasor Method）是一种扩展频率范围的相量域建模方法。传统相量法仅适用于基频稳态分析，而动态相量法通过引入时变傅里叶系数，能够捕捉宽频暂态过程，在仿真效率和精度之间取得良好平衡。

## 核心原理

- 将时域信号展开为时变傅里叶级数
- 每个傅里叶系数作为状态变量进行微分方程求解
- 可选择保留的谐波次数，灵活控制精度与效率
- 移位频率分析（SFA）进一步扩展了频率覆盖范围

## 主要优势

1. **大时间步长**：相比EMT可使用更大步长
2. **宽频覆盖**：能捕捉谐波和次同步振荡
3. **混合仿真接口**：天然适配电机暂态模型
4. **多速率兼容**：与其他仿真方法良好结合

## 关键技术

### 动态相量提取
- 滑动窗口傅里叶分析
- 递归最小二乘法
- 卡尔曼滤波方法

### 移位频率分析 (SFA)
- 将信号频谱搬移至参考频率附近
- 减少所需保留的谐波数量
- 适用于窄带信号分析

### 接口模型
- EMT与动态相量的接口技术
- 多域联合仿真（EMT+DP+相量域）
- 接口延迟补偿

## 应用场景

- MMC-MTDC系统多尺度暂态仿真
- VSC-HVDC系统谐波分析
- 次同步控制互动（SSCI）研究
- 混合仿真中的接口模型
- 半波长输电系统暂态稳定

## 相关方法
- [[multirate-method]]
- [[co-simulation]]
- [[harmonic-analysis]]

## 相关模型
- [[mmc-model]]
- [[vsc-model]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-22|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-|Advanced EMT and Phasor-Domain Hybrid Simulation With Simula]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2019 |
| [[shu-等-a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-ph|Shu 等 | A Multi-Domain Co-Simulation Method for Comprehensiv]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a|Assessment of dynamic phasor extraction methods for power sy]] | 2021 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[extending-the-frequency-bandwidth-of-transient-stability-simulation-using-dynami|Extending the Frequency Bandwidth of Transient Stability Sim]] | 2021 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|Half-wavelength System Transients Stability Simulation Using]] | 2021 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size el]] | 2021 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte|Multi-timescale simulator of nonlinear electrical elements b]] | 2022 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[dynamic-synchrophasor-estimator-based-on-multi-frequency-phasor-model|Dynamic Synchrophasor Estimator Based on Multi-frequency Pha]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[an-interface-method-for-co-simulation-of-emt-model-and-shifted-frequency-emt-mod|An Interface Method for Co-Simulation of EMT Model and Shift]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |