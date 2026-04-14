---
title: "电缆建模 (Cable Modeling)"
type: topic
tags: [cable, underground-cable, submarine-cable, skin-effect, frequency-dependent]
created: "2026-04-14"
---

# 电缆建模 (Cable Modeling)

## 概述

电缆（地下电缆和海底电缆）的EMT建模需要准确表征集肤效应、邻近效应、螺线管效应以及大地回路的频率相关特性。电缆建模与架空线路建模类似，但由于电缆结构的特殊性，其参数计算和建模方法有独特之处。

## 电缆结构特点

- 导体-绝缘-护套多层结构
- 三相电缆可能共用屏蔽层
- 海底电缆可能有铠装层
- 多层介质（XLPE、油纸等）

## 频率相关效应

### 集肤效应
- 高频下电流趋向导体表面
- 导体电阻随频率增加
- 内部电感随频率减小

### 邻近效应
- 相邻导体电流分布相互影响
- 三相电缆中尤为显著
- 增加有效电阻

### 螺线管效应（Solenoid Effect）
- 三芯统包电缆中铠装层的螺线管效应
- 产生附加损耗
- 影响正序和零序阻抗

## EMT建模方法

### 1. 频变参数模型
- 基于矢量拟合的频率相关阻抗
- 宽频阻抗建模
- 适用于暂态仿真

### 2. 恒定参数模型
- 在特定频率下的固定参数
- 适用于稳态和工频仿真
- 忽略频率相关特性

### 3. 多导体传输线模型
- 考虑导体间耦合
- 适用于多芯电缆
- 相域或模域求解

## 相关模型
- [[transmission-line-model]]
- [[fdne-model]]

## 相关方法
- [[vector-fitting]]
- [[frequency-dependent-modeling]]
- [[state-space-method]]

## 相关主题
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an undergr]] | 2005 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el|Modeling of cross-magnetization effects in saturated synchro]] | 2020 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-Delay Estimation Through All-Pass Functions for ULM Lin]] | 2025 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2026 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave function and multiscale modeling of MMC HVDC system for]] | 2026 |
| [[validation-of-frequency-dependent|Validation of frequency-dependent]] | 2026 |
