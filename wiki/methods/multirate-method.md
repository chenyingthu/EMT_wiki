---
title: "多速率方法 (Multi-Rate Method)"
type: method
tags: [multirate, time-step, partitioning, interface]
created: "2026-04-13"
---

# 多速率方法 (Multi-Rate Method)

## 概述

多速率方法（Multi-Rate Method）在同一仿真框架内对不同子系统采用不同的时间步长，以兼顾计算效率和仿真精度。这是处理包含多种时间尺度电力系统的关键技术。

## 核心思想

- **快变子系统**（电力电子换流器）：小步长（μs级）
- **慢变子系统**（输电网、发电机）：大步长（ms级）
- 通过接口算法实现数据交换与同步

## 关键技术

### 系统拆分
- 按时间尺度分区
- 按物理特性分区
- 按仿真精度需求分区

### 接口技术
- 线性插值
- 多项式外推
- 动态相量接口
- 预测-校正方法

### 稳定性分析
- 接口延迟对稳定性的影响
- 步长比约束
- 数值振荡风险

## 应用场景

- MMC-MTDC系统仿真
- 机电-电磁混合仿真
- 含高比例新能源的电网
- 实时仿真加速
- SFA-EMT多速率仿真

## 相关方法
- [[co-simulation]]
- [[dynamic-phasor]]
- [[numerical-integration]]
- [[interpolation-method]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|27&28/Multi-rate real time hybrid simulation of controllable]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |