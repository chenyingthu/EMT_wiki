---
title: "输电线路模型 (Transmission Line)"
type: model
tags: [transmission-line, bergeron, frequency-dependent, traveling-wave]
created: "2026-04-13"
---

# 输电线路模型 (Transmission Line)

## 概述

输电线路是电力系统中分布范围最广的元件，其电磁暂态特性对系统仿真精度有重要影响。准确的线路模型需要考虑频率相关参数、分布参数特性和行波传播效应。

## 主要模型类型

### 1. Bergeron模型
- 恒定参数的行波模型
- 无损耗线路假设
- 计算简单，EMTP标准模型
- 忽略频率相关性

### 2. 频变线路模型
- 考虑集肤效应和大地回路
- 参数随频率变化
- 模域变换解耦
- 矢量拟合实现

### 3. π型等值电路
- 集中参数近似
- 适用于短时线路
- 精确等值π电路
- 可变步长仿真算法

### 4. 多导体线路
- 三相耦合线路
- 非平行多导体
- 模态分解方法
- 交叉换位效应

## 频率相关特性

### 集肤效应
- 导线电阻随频率增加
- 内部电感减小

### 大地回路
- Carson公式
- 土壤电阻率影响
- 频率相关大地返回阻抗

### 模态变换
- 相域→模域解耦
- 频率相关变换矩阵
- 常数变换矩阵近似

## 特殊问题

- 截断电荷效应（线路开断）
- 电晕效应（高压线路）
- 半波长线路暂态
- 混合线路（架空线+电缆）

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]
- [[numerical-integration]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[cable-modeling]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[耦合长线电磁暂态分析的扩展bergeron模型|耦合长线电磁暂态分析的扩展Bergeron模型]] | 1996 |
| [[new-multiphase-mode-domain-transmission-line-model|New multiphase mode domain transmission line model]] | 1999 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[a-wavelet-transform-based-method-for-improved-modeling-of-transmission-lines-pow|A wavelet transform-based method for improved modeling of tr]] | 2001 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[mode-domain-multiphase-transmission-line-model-use-in-transient-studies-power-de|Mode domain multiphase transmission line model - use in tran]] | 2004 |
| [[modelling-of-single-phase-nonuniform-transmission-lines-in-electromagnetic-trans|Modelling of Single-Phase Nonuniform Transmission Lines in E]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri|Proposal of an alternative transmission line model for symme]] | 2011 |
| [[modal-domain-based-modeling-of-parallel-transmission-lines|Modal Domain Based Modeling of Parallel Transmission Lines]] | 2012 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|27&28/Multi-Scale and Frequency-Dependent Modeling of Electr]] | 2017 |
| [[modal-decoupling-of-overhead-transmission-lines-using-real-and-constant-matrices|Modal decoupling of overhead transmission lines using real a]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-multiconductor-transmission-lines-05|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2019 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[time-domain-modeling-of-transmission-line-crossing-using-electromagnetic-scatter|Time-Domain Modeling of Transmission Line Crossing Using Ele]] | 2020 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga--13&14|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio|Influence of a lossy ground on the lightning performance of ]] | 2022 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transm]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[locating-arc-faults-on-coupling-two-parallel-transmission-lines-using-the-novel-|Locating arc faults on coupling two parallel transmission li]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga|A waveform-dependence lightning impulse corona model in PSCA]] | 2024 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
| [[electromagnetic-transient-model-reconstruction-of-generalized-power-transmission|Electromagnetic Transient Model Reconstruction of Generalize]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss|Influence of approximate internal impedance formula on half-]] | 2025 |