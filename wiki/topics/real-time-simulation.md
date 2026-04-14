---
title: "实时仿真 (Real-Time Simulation)"
type: topic
tags: [real-time, fpga, rtds, hardware, hil]
created: "2026-04-13"
---

# 实时仿真 (Real-Time Simulation)

## 概述

实时仿真是EMT领域的核心技术方向，要求在严格的时间约束内完成每个仿真步长的计算。这对于硬件在环（HIL）测试、保护装置验证、控制系统开发等应用至关重要。

## 硬件平台

### RTDS (Real-Time Digital Simulator)
- 商业实时数字仿真器，广泛用于电力系统HIL测试
- 支持大规模电网的并行仿真
- 与外部控制器接口（如PSCAD/GTNET）

### FPGA加速
- 利用FPGA的并行性实现微秒级仿真
- 适用于电力电子换流器的详细开关仿真
- 挑战：资源受限、编程复杂

### GPU并行计算
- 大规模线程并行处理
- 适用于大规模电网电磁暂态并行仿真
- 与CPU异构计算

## 实时仿真建模挑战

### 计算效率 vs 精度
- 详细模型计算量大，难以满足实时性要求
- 需要简化模型（平均值模型、等效模型）
- 恒导纳模型（Fixed Admittance Model）是关键技术

### 时间步长约束
- 实时仿真通常要求50-100μs步长
- 多速率方法：不同子系统不同步长
- 外推/插值处理步长不匹配

### 数值稳定性
- 实时约束下无法使用迭代求解
- 需要无条件稳定的数值积分方法
- 数值振荡抑制

## 关键技术

- [[fixed-admittance]]：恒导纳建模，避免拓扑变化
- [[state-space-method]]：状态空间保持法
- [[average-value-model]]：平均值模型，减少开关细节
- [[multirate-method]]：多速率方法
- [[parallel-computing]]：并行计算

## 典型应用

- 保护装置硬件在环测试
- 换流器控制器（CCP/VCP）验证
- 新能源场站并网测试
- 数字孪生系统

## 相关实体
- [[rtds]]
- [[pscad-emtdc]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow|Multiprocessor based generator module for a real-time power ]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[the-computer-simulation-and-real-time-stabilization-control-for-the-inverted-pen|The Computer Simulation and Real-Time Stabilization Control ]] | 2009 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[real-time-fpga-rtds-co-simulator-for-power-systems|Real-Time FPGA-RTDS Co-Simulator for Power Systems]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea|Modeling a voltage source converter assisted resonant curren]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[fpga-based-sub-microsecond-level-real-time-simulation-for-microgrids-with-a-netw|FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Mi]] | 2020 |
| [[high-performance-computing-engines-for-the-fpga-based-simulation-of-the-ulm|High performance computing engines for the FPGA-based simula]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Use of efficient task allocation algorithm for parallel real]] | 2020 |
| [[an-fpga-based-electromagnetic-transient-analysis-of-power-distribution-network|An FPGA based electromagnetic transient analysis of power di]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga--13&14|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg|Interfacing real-time and offline power system simulation to]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[digital-twins-of-multiple-energy-networks-based-on-real-time-simulation-using-ho|Digital twins of multiple energy networks based on real-time]] | 2023 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Lessons learned in porting offline large-scale power system ]] | 2023 |
| [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Real-Time HIL Emulation of DRM With Machine Learning Acceler]] | 2023 |
| [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad|Real-Time Simulation of Power System Electromagnetic Transie]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Sparse solver application for parallel real-time electromagn]] | 2023 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[high-efficiency-modeling-of-multi-layer-cascaded-dual-active-bridge-dab-units-on|High Efficiency Modeling of Multi-Layer Cascaded Dual-Active]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time]] | 2025 |
| [[design-and-implementation-of-scalable-communication-interfaces-for-reliable-and-|Design and Implementation of Scalable Communication Interfac]] | 2025 |
| [[discretized-impedance-based-modeling-of-converter-interfaced-energy-resources-fo|Discretized Impedance-Based Modeling of Converter-Interfaced]] | 2025 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Fine-grained hardware resource optimization and design for F]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等 | A fixed-admittance algorithm for the FPGA-based micro]] | 2025 |
| [[基于fpga的变电站实时仿真培训系统|基于FPGA的变电站实时仿真培训系统]] | 2025 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|27&28/Multi-rate real time hybrid simulation of controllable]] | 2026 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |