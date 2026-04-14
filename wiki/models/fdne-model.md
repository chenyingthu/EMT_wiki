---
title: "频变网络等值 (FDNE)"
type: model
tags: [fdne, frequency-dependent, network-equivalent, multi-port, passivity]
created: "2026-04-13"
---

# 频变网络等值 (FDNE)

## 概述

频变网络等值（Frequency-Dependent Network Equivalent, FDNE）是将大规模电力系统的外部网络等效为多端口频率相关阻抗模型的技术。它保留了外部网络的宽频特性，同时大幅减少了仿真规模。

## 核心原理

- 从端口频率响应提取等值参数
- 矢量拟合获得有理函数模型
- 无源性强制确保稳定性
- 转换为状态空间或递归卷积形式

## 关键技术

### 参数辨识
- 频率扫描法
- Prony分析
- 最小二乘拟合
- 在线辨识

### 无源性保证
- 无源性检查算法
- 残差摄动修正
- 局部无源性补偿
- 双层网络等值

### 多端口扩展
- 多输入多输出系统
- 端口间耦合
- MIMO矢量拟合

## 应用场景

- 大电网边界简化
- 混合仿真接口模型
- 电磁-机电暂态混合仿真
- 外部系统宽频建模
- 实时仿真中的外部等值

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]
- [[prony-analysis]]

## 相关主题
- [[network-equivalent]]
- [[frequency-dependent-modeling]]
- [[co-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS V]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic Transient Analysis Using a Frequency Depende]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |