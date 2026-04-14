---
title: "矢量拟合 (Vector Fitting)"
type: method
tags: [vector-fitting, rational-approximation, curve-fitting, frequency-domain]
created: "2026-04-13"
---

# 矢量拟合 (Vector Fitting)

## 概述

矢量拟合（Vector Fitting, VF）是一种用于频率响应有理函数逼近的经典算法。在EMT仿真中，VF广泛用于频率相关参数的建模，将频域测量或计算数据转换为时域可用的状态空间模型。

## 算法原理

1. **初始极点选择**：设置一组不稳定的初始极点
2. **迭代优化**：通过最小二乘拟合调整极点位置
3. **留数计算**：确定最优留数以匹配频率响应
4. **无源性检查**：验证拟合模型的无源性

## 关键特性

- 鲁棒性好，对噪声数据有较强的适应性
- 收敛速度快，通常3-5次迭代即可收敛
- 支持多输入多输出（MIMO）系统
- 可扩展到宽频带拟合

## 在EMT中的应用

- 输电线路频变参数拟合
- 电缆频变阻抗拟合
- 频变网络等值（FDNE）建模
- 变压器宽频建模
- 接地系统频响拟合

## 相关方法
- [[passivity-enforcement]]：无源性强制
- [[numerical-integration]]：数值积分（时域实现）

## 相关主题
- [[frequency-dependent-modeling]]
- [[network-equivalent]]
- [[cable-modeling]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[fast-realization-of-the-modal-vector-fitting|Fast Realization of the Modal Vector Fitting]] | 2009 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |