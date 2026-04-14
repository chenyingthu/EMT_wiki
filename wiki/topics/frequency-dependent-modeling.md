---
title: "频率相关建模 (Frequency-Dependent Modeling)"
type: topic
tags: [frequency-dependent, vector-fitting, fdne, wideband]
created: "2026-04-13"
---

# 频率相关建模 (Frequency-Dependent Modeling)

## 概述

频率相关建模是EMT仿真中的核心技术，用于准确表征电力设备（输电线路、电缆、变压器、电网等值）参数随频率变化的特性。在宽频暂态分析中，忽略频率相关性会导致显著的仿真误差。

## 核心问题

- **集肤效应**：导体电阻和电感随频率变化
- **大地回路**：土壤电阻率的频率特性
- **磁芯损耗**：变压器铁芯的频响特性
- **电网等值**：外部系统的宽频阻抗特性

## 主要方法

### 矢量拟合 (Vector Fitting)
- 将频率响应拟合为有理函数
- 保证无源性（Passivity）
- 转换为状态空间或递归卷积形式

### 频变网络等值 (FDNE)
- 多端口频率相关等值
- 宽频阻抗拟合
- 局部无源性补偿

### 频变线路模型
- Bergeron模型的频率扩展
- 模域变换方法
- 行波卷积计算

## 关键技术

- [[vector-fitting]]：有理函数拟合算法
- [[passivity-enforcement]]：无源性强制校正
- [[fdne-model]]：频变网络等值
- [[transmission-line-model]]：频变线路建模

## 应用场景

- 雷击过电压计算（高频分量）
- 开关操作暂态分析
- 谐波共振研究
- 电缆暂态分析
- 混合仿真中的边界等值

## 来源论文

| 论文 | 年份 |
|------|------|
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-voltage-transformer-13&14|Digital Time-Domain Investigation of Transient Behavior of C]] | 1998 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies|A Wideband Equivalent Model of Type-3 Wind Power Plants for ]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|27&28/Multi-Scale and Frequency-Dependent Modeling of Electr]] | 2017 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-multiconductor-transmission-lines-05|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2019 |
| [[development-of-high-frequency-supraharmonic-models-of-small-scale-amplt5kw-singl|Development of high frequency (Supraharmonic) models of smal]] | 2019 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo|An Inverter Model Simulating Accurate Harmonics with Low Com]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga--13&14|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[analysis-on-induced-voltages-in-wind-farms-close-to-distribution-lines-on-freque|Analysis on Induced Voltages in Wind Farms Close to Distribu]] | 2022 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[analytical-and-measurement-based-wideband-two-port-modeling-of-dc-dc-converters-|Analytical and measurement-based wideband two-port modeling ]] | 2023 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-|Harmonics Interaction Mechanism and Impact on Extinction Ang]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic Transient Analysis Using a Frequency Depende]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[harmonic-preserved-average-value-model-for-converters-in-electromagnetic-transie|Harmonic-Preserved Average-Value Model for Converters in Ele]] | 2026 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |