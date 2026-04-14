---
title: "双馈感应发电机 (DFIG)"
type: model
tags: [dfig, wind-turbine, induction-machine, renewable]
created: "2026-04-13"
---

# 双馈感应发电机 (DFIG)

## 概述

双馈感应发电机（Doubly-Fed Induction Generator, DFIG）是风力发电系统中广泛应用的发电机类型。其定子直接并网，转子通过背靠背换流器励磁，可实现变速恒频运行。

## 结构特点

- 绕线式感应电机
- 定子直接连接电网
- 转子通过部分容量换流器励磁
- 变速运行范围宽

## EMT建模方法

### 详细模型
- 完整的d-q轴模型
- 包含转子侧和网侧换流器
- 控制系统详细建模
- 适用于单机暂态分析

### 等值模型
- 风电场等值聚合
- 保留动态特性
- 大规模系统简化
- 机电-电磁混合仿真适用

### 高效实时模型
- 固定导纳建模
- FPGA实现
- 多台风电机组并行

## 控制特性

- 最大功率跟踪（MPPT）
- 有功/无功解耦控制
- 低电压穿越（LVRT）
- 转子侧换流器控制
- 网侧换流器控制

## 暂态特性

- 电网故障响应
-  Crowbar保护动作
- 直流母线电压波动
- 次同步振荡风险

## 相关方法
- [[state-space-method]]
- [[fixed-admittance]]

## 相关主题
- [[wind-farm-modeling]]
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co|Analysis of low frequency interactions of DFIG wind turbine ]] | 2020 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl|Electromechanical transient-electromagnetic transient hybrid]] | 2022 |
| [[structure-preserving-aggregation-method-for-doubly-fed-induction-generators-in-w|Structure Preserving Aggregation Method for Doubly-Fed Induc]] | 2022 |
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati|Equivalent grid-following inverter-based generator model for]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi|Improved methods for optimization of power systems with rene]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[inverter-based-resources-model-verification-using-electromagnetic-transient-play|Inverter-Based Resources Model Verification Using Electromag]] | 2024 |
| [[machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc|Machine-Learning-Reinforced Massively Parallel Transient Sim]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o|An enhanced K-means two-step clustering method for dynamic e]] | 2025 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Fine-grained hardware resource optimization and design for F]] | 2025 |
| [[huang-等-a-heterogeneous-multiscale-method-for-efficient-simulation-of-power-syst|Huang 等 | A Heterogeneous Multiscale Method for Efficient Si]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |