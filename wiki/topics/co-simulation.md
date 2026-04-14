---
title: "混合仿真 (Co-Simulation / Hybrid Simulation)"
type: topic
tags: [cosimulation, hybrid, emt, transient-stability, interface]
created: "2026-04-13"
---

# 混合仿真 (Co-Simulation / Hybrid Simulation)

## 概述

混合仿真（Co-Simulation / Hybrid Simulation）是EMT领域最重要的研究方向之一，核心思想是将不同时间尺度、不同建模精度的仿真方法结合起来，在保证关键区域仿真精度的同时，大幅提升大规模系统的仿真效率。

## 主要类型

### 1. 机电-电磁暂态混合仿真

将电磁暂态（EMT）仿真与机电暂态（Transient Stability / RMS）仿真相结合：
- **EMT侧**：关注局部关键区域（如换流站、新能源场站）的毫秒级电磁暂态过程
- **机电侧**：关注大范围电网的秒级机电暂态过程
- **接口技术**：是混合仿真的核心挑战，包括边界解耦、数据同步、接口模型设计

### 2. 多速率混合仿真

在同一仿真框架内对不同子系统采用不同时间步长：
- 快速子系统（电力电子换流器）：微秒级步长
- 慢速子系统（输电网、发电机）：毫秒级步长
- 通过多速率接口实现数据交换

### 3. 数模混合仿真

将数字仿真（离线EMT程序）与模拟仿真（实时硬件在环）结合：
- RTDS + FPGA联合仿真
- 硬件在环（HIL）测试
- 数字孪生应用

### 4. 频域-时域联合仿真

将相量域（动态相量、移位频率分析）与时域EMT仿真结合：
- 动态相量接口模型
- 移位频率EMT（SFA-EMT）
- 谐波相量域联合仿真

## 关键技术挑战

### 接口算法
- 边界变量选择与同步
- 接口延迟补偿
- 接口稳定性分析
- 接口位移与映射等价

### 仿真模式切换
- EMT与机电暂态模型的在线切换
- 故障触发式切换策略
- 平滑过渡算法

### 频率相关网络等值
- 在混合仿真中保持频率相关特性
- 局部无源性补偿
- 多端口Thevenin等值

## 典型应用场景

- 大规模交直流电网仿真（MMC-MTDC系统）
- 高比例新能源并网仿真
- VSC-HVDC系统多尺度暂态分析
- 牵引供电系统与主网交互影响
- 次同步振荡分析

## 相关方法
- [[dynamic-phasor]]
- [[multirate-method]]
- [[network-equivalent]]
- [[nodal-analysis]]

## 相关模型
- [[mmc-model]]
- [[vsc-model]]
- [[synchronous-machine-model]]
- [[fdne-model]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Comparison between electromechanical transient model and ele]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g|Comparative study on electromechanical and electromagnetic t]] | 2014 |
| [[基于adpss的电力系统和牵引供电系统机电电磁暂态混合仿真|基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真]] | 2014 |
| [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution|A Hybrid Simulation Tool for the Study of PV Integration Imp]] | 2016 |
| [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t|Application of Electromagnetic Transient-Transient Stability]] | 2016 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a|A Novel Interfacing Technique for Distributed Hybrid Simulat]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[a-rotary-frequency-converter-model-for-electromechanical-transient-studies|A rotary frequency converter model for electromechanical tra]] | 2018 |
| [[a-rotary-frequency-converter-model-for-electromechanical-transient-studies-of-16|A rotary frequency converter model for electromechanical tra]] | 2018 |
| [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-|Advanced EMT and Phasor-Domain Hybrid Simulation With Simula]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[shu-等-a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-ph|Shu 等 | A Multi-Domain Co-Simulation Method for Comprehensiv]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a|Assessment of dynamic phasor extraction methods for power sy]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[co-simulation-applied-to-power-systems-with-high-penetration-of-distributed-ener|Co-simulation applied to power systems with high penetration]] | 2022 |
| [[electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl|Electromechanical transient-electromagnetic transient hybrid]] | 2022 |
| [[electromechanical-electromagnetic-hybrid-simulation-technology-with-large-number|Electromechanical-electromagnetic Hybrid Simulation Technolo]] | 2022 |
| [[electromechanical-electromagnetic-transient-hybrid-simulation-of-an-acdc-hybrid-|Electromechanical-electromagnetic transient hybrid simulatio]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech|An aggregation method of permanent magnet synchronous wind f]] | 2023 |
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[an-interface-method-for-co-simulation-of-emt-model-and-shifted-frequency-emt-mod|An Interface Method for Co-Simulation of EMT Model and Shift]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[design-and-implementation-of-scalable-communication-interfaces-for-reliable-and-|Design and Implementation of Scalable Communication Interfac]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|27&28/Multi-rate real time hybrid simulation of controllable]] | 2026 |
| [[electromagnetic-transient-emt-and-quasi-static-time-series-qsts-co-simulation-fo|Electromagnetic transient (EMT) and quasi static time series]] | 2026 |
| [[electromechanical-transientelectromagnetic-transient-hybrid-simulation-method-co|Electromechanical transientelectromagnetic transient hybrid ]] | 2026 |