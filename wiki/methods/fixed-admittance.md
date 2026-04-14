---
title: "恒导纳模型 (Fixed Admittance / ADC Model)"
type: method
tags: [fixed-admittance, adc, real-time, companion-circuit]
created: "2026-04-13"
---

# 恒导纳模型 (Fixed Admittance / ADC Model)

## 概述

恒导纳模型（Fixed Admittance Model），也称关联离散电路模型（Associated Discrete Circuit, ADC），是一种保持导纳矩阵拓扑不变的建模方法。开关状态变化时仅改变伴随电流源，避免导纳矩阵重构，特别适合实时仿真。

## 核心原理

- 所有开关状态共享同一导纳矩阵
- 开关切换仅更新等效电流源
- 避免LU分解重复计算

## 优势

- 计算效率大幅提升
- 导纳矩阵只需分解一次
- 非常适合FPGA和实时仿真
- 数值稳定性好

## 应用场景

- MMC桥臂模块建模
- FPGA实时仿真
- 含大量开关的电力电子系统
- PMSM实时EMT仿真
- 变换器固定导纳ADC模型

## 相关方法
- [[nodal-analysis]]
- [[state-space-method]]
- [[average-value-model]]

## 相关主题
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul|A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Con]] | 2025 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等 | A fixed-admittance algorithm for the FPGA-based micro]] | 2025 |
| [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-|Analytical Modeling of the Half-Bridge Leg Using an Associat]] | 2026 |