---
title: "并行计算 (Parallel Computing)"
type: topic
tags: [parallel, gpu, multicore, hpc, acceleration]
created: "2026-04-13"
---

# 并行计算 (Parallel Computing)

## 概述

并行计算是解决大规模EMT仿真计算瓶颈的关键技术。通过将系统分解为多个子问题并行求解，可以显著加速仿真过程，尤其在大规模电网和含大量电力电子设备的系统中效果显著。

## 并行策略

### 1. 空间分解（网络拆分）
- 将大规模电网拆分为多个子网络
- 各子网络独立求解，通过边界变量协调
- 拆分算法需最小化跨分区通信

### 2. 时间并行
- 并行-in-time算法
- 多时间点同时计算
- Waveform松弛方法

### 3. 设备级并行
- GPU大规模线程并行
- 多核CPU共享内存架构
- FPGA硬件并行

### 4. 多线程/共享内存
- 基于OpenMP的共享内存并行
- 任务级并行调度
- 缓存优化

## 关键技术挑战

- **通信开销**：子区域间数据交换
- **负载平衡**：各并行单元计算量均衡
- **数值稳定性**：并行分解对精度的影响
- **可扩展性**：并行度随系统规模的扩展

## 典型实现

- ParaEMT：开源可并行EMT仿真器
- GPU加速的电磁暂态并行仿真
- 大规模电池储能系统并行建模
- 多区域Thevenin等值并行计算

## 相关方法
- [[network-equivalent]]
- [[state-space-method]]
- [[nodal-analysis]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[independent-power-producer-parallel-operation-modeling-in-transient-network-anal|Independent power producer parallel operation modeling in tr]] | 2009 |
| [[chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas|Chen 等 | A hybrid parallel computation algorithm and its app]] | 2010 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[modal-domain-based-modeling-of-parallel-transmission-lines|Modal Domain Based Modeling of Parallel Transmission Lines]] | 2012 |
| [[parallel-massive-thread-electromagnetic-transient-simulation-on-gpu|Parallel Massive-Thread Electromagnetic Transient Simulation]] | 2014 |
| [[a-parallel-multi-modal-optimization-algorithm-for-simulation-based-design-of-pow|A Parallel Multi-Modal Optimization Algorithm for Simulation]] | 2015 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio|Functional Mock-up Interface Based Approach for Parallel and]] | 2018 |
| [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-|The diode-clamped half-bridge MMC structure with internal sp]] | 2018 |
| [[面向指数积分方法的电磁暂态仿真gpu并行算法|面向指数积分方法的电磁暂态仿真GPU并行算法]] | 2018 |
| [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre|Functional Mock-Up Interface Based Parallel Multistep Approa]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|A Novel Linking-Domain Extraction Decomposition Method for P]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[parallel-in-time-object-oriented-electromagnetic-transient-simulation-of-power-s|Parallel-in-Time Object-Oriented Electromagnetic Transient S]] | 2020 |
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Use of efficient task allocation algorithm for parallel real]] | 2020 |
| [[a-parallelization-in-time-approach-for-accelerating-emt-simulations|A parallelization-in-time approach for accelerating EMT simu]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[evaluation-of-the-extended-modal-domain-model-in-the-calculation-of-lightning-in|Evaluation of the extended modal-domain model in the calcula]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[analysis-on-non-characteristic-harmonic-circulating-current-in-parallel-inverter|Analysis on non-characteristic harmonic circulating current ]] | 2022 |
| [[coupling-model-for-time-domain-analysis-of-nonparallel-overhead-wires-and-buried|Coupling model for time-domain analysis of nonparallel overh]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized-03|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[locating-arc-faults-on-coupling-two-parallel-transmission-lines-using-the-novel-|Locating arc faults on coupling two parallel transmission li]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn|Performance evaluation of communication fabrics for offline ]] | 2023 |
| [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Sparse solver application for parallel real-time electromagn]] | 2023 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc|Machine-Learning-Reinforced Massively Parallel Transient Sim]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel|Double-Ended Fault-Locating Method for Parallel Lines Withou]] | 2025 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[low-dimensional-equivalent-models-and-multithreading-based-parallel-emt-simulati|Low-Dimensional Equivalent Models and Multithreading-Based P]] | 2025 |
| [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat|Transient Electromagnetic Power Compensation‐Based Adaptive ]] | 2025 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[gpu-parallel-rate-exponential-integrator-algorithm-for-efficient-simulation-of-p|GPU Parallel-Rate Exponential Integrator Algorithm for Effic]] | 2026 |