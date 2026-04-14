---
title: "插值方法 (Interpolation Method)"
type: method
tags: [interpolation, numerical-method, time-step, multi-rate, accuracy]
created: "2026-04-14"
---

# 插值方法 (Interpolation Method)

## 概述

插值方法在EMT仿真中广泛应用于不同时间尺度系统之间的数据同步、变步长仿真的中间值计算以及多速率仿真的接口处理。插值精度直接影响仿真的数值稳定性和暂态响应的准确性。

## 主要应用场景

### 1. 多速率仿真
- 不同子系统采用不同时间步长
- 快系统和慢系统之间的数据交换
- 需要插值获取中间时刻的值

### 2. 变步长仿真
- 自适应步长调整
- 暂态期间小步长、稳态期间大步长
- 插值保证数值连续性

### 3. 混合仿真接口
- 电磁暂态与机电暂态混合仿真
- 实时仿真与离线仿真联合
- 接口数据同步

## 常用插值方法

### 1. 线性插值
- 最简单的插值方法
- 计算量小
- 精度有限

### 2. 多项式插值
- Lagrange插值
- Newton插值
- 精度较高

### 3. 样条插值
- 平滑性好
- 适用于高精度要求

### 4. Hermite插值
- 保持导数连续性
- 适用于电力系统暂态分析

## 数值稳定性

- 插值可能引入数值振荡
- 外推比插值更不稳定
- 需要评估插值对仿真精度的影响

## 相关方法
- [[multirate-method]]
- [[numerical-integration]]
- [[nodal-analysis]]

## 相关主题
- [[co-simulation]]
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable]] | 2026 |
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo|Interpolation for power electronic circuit simulation revisit]] | 2025 |
| [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da|Stability evaluation of interpolation, extrapolation and num]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Shifting frequency analysis based real-time simulation method]] | 2025 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|27&28/Multi-rate real time hybrid simulation of controllable]] | 2026 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK based EMT simulations]] | 2026 |
| [[基于rtds和fpga联合仿真平台的多速率实时仿真方法|基于RTDS和FPGA联合仿真平台的多速率实时仿真方法]] | 2026 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability assessment of multi-rate electromagnetic transient]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability improved network partition based on a small step s]] | 2026 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|Shu 2018 (多速率MMC)]] | 2018 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|Mu 2014 (多速率EMT)]] | 2014 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis EMTP multirate simulation of power]] | 2024 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|Shu 2018 (MMC多速率EMT)]] | 2018 |
