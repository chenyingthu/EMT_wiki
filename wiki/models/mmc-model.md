---
title: "模块化多电平换流器 (MMC)"
type: model
tags: [mmc, hvdc, converter, sub-module, arm]
created: "2026-04-13"
---

# 模块化多电平换流器 (MMC)

## 概述

模块化多电平换流器（Modular Multilevel Converter, MMC）是当前高压直流输电（HVDC）和柔性交流输电系统的主流拓扑。由多个子模块（SM）级联构成桥臂，具有模块化、可扩展、低谐波等优势。

## 结构特点

- **桥臂结构**：三相六桥臂，每桥臂含N个子模块
- **子模块类型**：半桥（HBSM）、全桥（FBSM）、箝位双子模块等
- **电容电压平衡**：需要复杂的排序和均压算法
- ** circulating current**：桥臂内存在环流

## EMT建模方法

### 1. 详细模型
- 每个子模块单独建模
- 包含开关动态和电容电压
- 计算量极大，适用于少量SM

### 2. 平均值模型 (AVM)
- 桥臂平均化处理
- 忽略开关纹波，保留低频动态
- 计算效率提升1-2个数量级
- 增强平均值模型（考虑环流）

### 3. 等效模型
- Thevenin等效桥臂
- 嵌套快速求解方法
- 任意多端口子模块结构

### 4. 固定导纳模型
- ADC建模，避免矩阵重构
- 适用于实时仿真
- FPGA硬件实现

### 5. 动态相量模型
- 频域MMC建模
- 适用于混合仿真
- 宽频暂态分析

## 关键技术挑战

- 子模块电容电压平衡
- 环流抑制控制
- 直流故障穿越
- 损耗建模（虚假功率问题）
- 大规模MMC-MTDC系统仿真

## 相关方法
- [[average-value-model]]
- [[fixed-admittance]]
- [[state-space-method]]
- [[dynamic-phasor]]

## 相关主题
- [[vsc-hvdc]]
- [[real-time-simulation]]
- [[co-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-22|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Efﬁcient Modeling of Modular Multilevel HVDC]] | 2010 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[ahmed-等-a-computationally-efficient-continuous-model-for-the-modular-multilevel-|Ahmed 等 | A Computationally Efficient Continuous Model for t]] | 2014 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[current-source-modular-multilevel-converter-modeling-and-control|Current Source Modular Multilevel Converter Modeling and Con]] | 2016 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Modeling of Modular Multilevel Converters with Different Lev]] | 2017 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us|High-Speed EMT Modeling of MMCs With Arbitrary Multiport Sub]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-|The diode-clamped half-bridge MMC structure with internal sp]] | 2018 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified High-Speed EMT Equivalent and Implementation Method ]] | 2018 |
| [[双端口子模块mmc电磁暂态通用等效建模方法|双端口子模块MMC电磁暂态通用等效建模方法]] | 2018 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[mmc-upfc电磁-机电混合仿真技术研究|MMC-UPFC电磁-机电混合仿真技术研究]] | 2019 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Spurious Power Losses in Modular Multilevel Converter Arm Eq]] | 2019 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With ]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co|An Equivalent Hybrid Model for a Large-Scale Modular Multile]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[混合型mmc全状态高效电磁暂态仿真方法研究|混合型MMC全状态高效电磁暂态仿真方法研究]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
| [[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-|Equivalent model of nearest level modulation for fast electr]] | 2023 |
| [[fast-electromagnetic-transient-simulation-method-for-mmc-hvdc-system|Fast electromagnetic transient simulation method for MMC-HVD]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-|Generalized Electromagnetic Transient Equivalent Modeling an]] | 2023 |
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|Modeling of MMC-based STATCOM with embedded energy storage f]] | 2023 |
| [[多样性子模块混合型mmc统一外特性高效电磁暂态模型|多样性子模块混合型MMC统一外特性高效电磁暂态模型]] | 2023 |
| [[多类型子模块mmc电磁暂态通用建模和实现方法|多类型子模块MMC电磁暂态通用建模和实现方法]] | 2023 |
| [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu|An ultra-fast MMC-HVDC fault location algorithm based on tra]] | 2024 |
| [[基于mmc平均值仿真模型的损耗快速评估方法|Fast Loss Evaluation Method Based on MMC Average Simulation ]] | 2024 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2024 |
| [[a-computationally-efficient-approach-for-power-semiconductor-loss-estimation-of-|A computationally efficient approach for power semiconductor]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|An Electromagnetic Transient Simulation Model of MMC-BESS fo]] | 2025 |
| [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map|Dead-time effect modeling for hybrid modular multilevel conv]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[equivalent-modeling-of-electromagnetic-transient-for-mmc-hvdc-based-on-semi-impl|Equivalent modeling of electromagnetic transient for MMC-HVD]] | 2026 |
| [[fast-electromagnetic-transient-simulation-models-of-modular-multilevel-converter|Fast electromagnetic transient simulation models of modular ]] | 2026 |
| [[适用于实时仿真的mmc子模块电容电压优化均衡方法|适用于实时仿真的MMC子模块电容电压优化均衡方法]] | 2026 |