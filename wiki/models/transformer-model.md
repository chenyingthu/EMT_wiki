---
title: "变压器模型 (Transformer)"
type: model
tags: [transformer, hysteresis, saturation, frequency-dependent, white-box]
created: "2026-04-13"
---

# 变压器模型 (Transformer)

## 概述

变压器是电力系统中最关键的设备之一，其EMT建模需要准确表征磁路饱和、磁滞、频率特性和绕组间耦合等非线性特性。

## 主要模型类型

### 1. 经典模型
- 线性互感模型
- 饱和励磁支路
- 适用于稳态和小信号分析

### 2. 磁滞模型
- Jiles-Atherton磁滞公式
- Preisach模型
- 现场磁滞曲线测量
- 适用于铁磁谐振研究

### 3. 白盒模型
- 基于详细设计参数
- 高频白盒变压器模型
- 接口因子法
- 阻尼因子模型

### 4. 对偶电路模型
- 磁路-电路对偶建模
- 多芯变压器对偶电路
- UMEC（统一磁电耦合）模型
- Sen变压器模型

### 5. 频变模型
- 高频响应建模
- 绕组间电容
- 雷电冲击响应
- 宽频阻抗拟合

## 特殊效应

### 磁饱和
- 励磁电流畸变
- 铁芯饱和曲线
- 直流偏磁效应

### 磁滞
- 剩磁效应
- 励磁涌流
- 铁磁谐振

### 集肤效应和涡流
- 绕组频变电阻
- 铁芯涡流损耗
- 螺线管效应（三芯电缆）

## 应用场景

- 励磁涌流分析
- 铁磁谐振研究
- 雷电冲击响应
- 直流偏磁（GIC）
- 高频暂态分析

## 相关方法
- [[nodal-analysis]]
- [[vector-fitting]]
- [[state-space-method]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[ferroresonance]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-voltage-transformer-13&14|Digital Time-Domain Investigation of Transient Behavior of C]] | 1998 |
| [[电磁暂态计算中新的变压器模型|电磁暂态计算中新的变压器模型]] | 1999 |
| [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-|A Z-transform model of transformers for the study of electro]] | 2004 |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP - Power Deli]] | 2004 |
| [[a-transformer-model-for-winding-fault-studies-power-delivery-ieee-transactions-o|A transformer model for winding fault studies - Power Delive]] | 2004 |
| [[an-improved-low-frequency-transformer-model-for-use-in-gic-studies|An improved low-frequency transformer model for use in GIC s]] | 2004 |
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo|Digital Time-Domain Investigation of Transient Behavior of C]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[a-link-between-emtp-rv-and-flux3d-for-transformer-energization-studies|A link between EMTP-RV and FLUX3D for transformer energizati]] | 2009 |
| [[dual-reversible-transformer-model-for-the-13&14|Dual Reversible Transformer Model for the]] | 2013 |
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio|EMTP model of a bidirectional multilevel solid state transfo]] | 2014 |
| [[interfacing-factor-based-white-box-transformer-modeling-method|Interfacing Factor-Based White-Box Transformer Modeling Meth]] | 2014 |
| [[analysing-a-power-transformers-internal-response-to-system-transients-using-a-hy|Analysing a power transformer⠒s internal response to system ]] | 2015 |
| [[duality-based-transformer-model-including-13&14|Duality-Based Transformer Model Including]] | 2015 |
| [[duality-based-transformer-modeling-for-low-frequency-transients|Duality-Based Transformer Modeling for Low-Frequency Transie]] | 2016 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[an-improved-high-frequency-white-box-lossy-transformer-model-for-the-calculation|An improved high frequency white-box lossy transformer model]] | 2017 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[application-of-duality-based-equivalent-circuits-for-modeling-multilimb-transfor|Application of Duality-Based Equivalent Circuits for Modelin]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[determination-of-the-saturation-curve-of-power-transformers-by-processing-transi|Determination of the saturation curve of power transformers ]] | 2021 |
| [[expanding-the-measuring-range-via-s-parameters-in-a-ehv-voltage-transformer-mode|Expanding the measuring range via S-parameters in a EHV volt]] | 2021 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[级联h桥型电力电子变压器的闭锁状态等效建模方法-33|级联H桥型电力电子变压器的闭锁状态等效建模方法]] | 2021 |
| [[级联h桥型电力电子变压器的闭锁状态等效建模方法-40|级联H桥型电力电子变压器的闭锁状态等效建模方法]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien|A Transformer Model With Hysteresis Characteristics for Elec]] | 2022 |
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Accelerated Electromagnetic Transient (EMT) Equivalent Model]] | 2022 |
| [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based|Electromagnetic Modeling of Transformers in EMT-Type Softwar]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized-03|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[on-site-measurement-of-the-hysteresis-curve-for-improved-modelling-of-transforme|On-site measurement of the hysteresis curve for improved mod]] | 2023 |
| [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e|Optimized high-frequency white-box transformer model for imp]] | 2023 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[adaptive-variable-step-size-calculation-method-for-transient-temperature-rise-and-fall|Adaptive Variable Step Size Calculation Method for Transient]] | 2024 |
| [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w|Enhancements to Terminal Duality-based models for three-phas]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
| [[experimental-research-on-high-voltage-transformer-transient-characteristics|Experimental research on high-voltage transformer transient ]] | 2026 |