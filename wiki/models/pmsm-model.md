---
title: "永磁同步电机 (PMSM)"
type: model
tags: [pmsm, synchronous-machine, permanent-magnet, motor, generator]
created: "2026-04-14"
---

# 永磁同步电机 (PMSM)

## 概述

永磁同步电机（Permanent Magnet Synchronous Machine, PMSM）是采用永磁体励磁的同步电机。相比电励磁同步电机，PMSM具有效率高、功率密度大、响应快等优点，广泛应用于风力发电、电动汽车和工业驱动领域。

## 主要特点

- 永磁体励磁，无需励磁绕组
- 高效率、高功率密度
-  dq轴电感不对称（凸极效应）
- 退磁风险（高温、大电流）
- 适用于变速恒频运行

## EMT建模方法

### 1. 传统dq0模型
- Park变换建立dq轴方程
- 适用于对称运行条件
- 计算效率高

### 2. 相域模型
- 直接在abc坐标系下建模
- 适用于不对称和故障条件
- 计算量大

### 3. 有限元耦合模型
- 基于FEA结果定义磁链
- 精确表征磁饱和和非线性
- 适用于高精度实时仿真

## 应用场景

- 直驱风力发电
- 电动汽车驱动
- 工业伺服系统
- 航空航天

## 相关方法
- [[state-space-method]]
- [[fixed-admittance]]

## 相关主题
- [[real-time-simulation]]
- [[frequency-dependent-modeling]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time]] | 2025 |
