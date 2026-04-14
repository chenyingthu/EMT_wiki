---
title: "数值积分 (Numerical Integration)"
type: method
tags: [numerical-integration, trapezoidal, gear, dirk, stability]
created: "2026-04-13"
---

# 数值积分 (Numerical Integration)

## 概述

数值积分是EMT仿真中求解微分方程的核心技术。电力系统中的电感、电容等储能元件通过微分方程描述，需要数值方法离散化求解。

## 常用方法

### 梯形法 (Trapezoidal)
- EMT仿真默认方法
- A稳定，二阶精度
- 问题：可能产生数值振荡

### 后向Euler (Backward Euler)
- 强数值阻尼
- 一阶精度
- 抑制数值振荡但引入幅值误差

### Gear法
- 多步法，可变阶数
- 更高的精度和稳定性
- 需要历史数据

### 2S-DIRK (双阶段对角隐式Runge-Kutta)
- 适用于 stiff 系统
- 良好的数值稳定性
- 在EMT中逐渐应用

## 关键问题

### 数值振荡
- 开关操作触发的数值振荡
- 阻尼方法：混合Euler-梯形
- 数值振荡抑制技术

### 步长选择
- 固定步长 vs 可变步长
- 稳定性约束
- 精度-效率权衡

### 多速率积分
- 不同子系统不同步长
- 插值/外推处理数据同步
- 数值稳定性分析

## 相关方法
- [[nodal-analysis]]
- [[state-space-method]]
- [[multirate-method]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally]] | 2008 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[field-validated-generic-emt-type-model-of-a-full-converter-wind-turbine-based-on|Field Validated Generic EMT-Type Model of a Full Converter W]] | 2018 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact sc]] | 2023 |