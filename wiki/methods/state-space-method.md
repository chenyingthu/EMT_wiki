---
title: "状态空间法 (State-Space Method)"
type: method
tags: [state-space, matrix-exponential, eigenvalue, system-modeling]
created: "2026-04-13"
---

# 状态空间法 (State-Space Method)

## 概述

状态空间法将电力系统描述为一阶微分方程组 ẋ = Ax + Bu，通过矩阵运算和数值积分求解系统状态。这种方法特别适合电力电子系统和控制系统的建模与仿真。

## 核心优势

- 统一的数学框架
- 适用于线性与非线性系统
- 便于稳定性分析（特征值）
- 适合实时仿真（矩阵指数法）

## 关键技术

### 矩阵指数法
- 精确解：x(t) = e^(At)·x(0)
- 适用于线性时不变系统
- 可避免数值积分误差

### 状态空间保持法
- 开关状态变化时的状态连续性
- ADC（关联离散电路）模型
- 避免导纳矩阵重构

### 模型降阶
- 大规模系统状态缩减
- Krylov子空间方法
- 保留关键动态模式

## 应用场景

- MMC状态空间建模
- 电力电子变换器开关周期分析
- 系统稳定性评估
- 控制器设计与验证
- 实时仿真中的线性系统求解

## 相关方法
- [[nodal-analysis]]
- [[numerical-integration]]
- [[average-value-model]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations]] | 2021 |
| [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti|A Piecewise Generalized State Space Model of Power Converter]] | 2022 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transm]] | 2023 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Splitting State-Space Method for Converter-Integrated Power ]] | 2025 |