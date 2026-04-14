---
title: "同步电机模型 (Synchronous Machine)"
type: model
tags: [synchronous-machine, generator, park, vbr, phase-domain]
created: "2026-04-13"
---

# 同步电机模型 (Synchronous Machine)

## 概述

同步电机是电力系统中最主要的发电设备，其EMT建模需要准确表征电磁暂态过程中的定子、转子绕组耦合关系以及磁路饱和特性。

## 主要模型类型

### 1. 经典模型
- Park变换（dq0轴）
- 恒定磁链假设
- 适用于机电暂态

### 2. 相域模型
- 直接在abc坐标系下建模
- 无需坐标变换
- 十二相同步电机相域模型
- 适合不对称工况

### 3. VBR模型（电压源后向转子）
- Voltage Behind Reactance
- 提高数值稳定性
- 适用于EMT-机电混合仿真

### 4. 交叉磁化模型
- 饱和交叉磁化效应
- d-q轴耦合
- 适用于饱和工况

### 5. 等值聚合模型
- 风电场同步机聚合
- 保留动态特性
- 大规模系统简化

## 关键技术

### 电磁暂态建模
- 定子绕组暂态
- 转子回路暂态
- 阻尼绕组效应

### 饱和处理
- 开路饱和曲线
- 负载饱和特性
- 交叉饱和效应

### 接口技术
- 与EMT仿真器的接口
- 混合仿真中的等值
- 可变步长适应性

## 应用场景

- 短路故障分析
- 励磁系统研究
- 稳定性分析
- 机电-电磁混合仿真
- 不对称运行分析

## 相关方法
- [[state-space-method]]
- [[nodal-analysis]]

## 相关主题
- [[co-simulation]]
- [[network-equivalent]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[re-examination-of-synchronous-machine|Re-examination of Synchronous Machine]] | 2007 |
| [[synchronous-machine-exciter-circuit-model-in-a|Synchronous Machine Exciter Circuit Model In A]] | 2013 |
| [[field-validated-generic-emt-type-model-of-a-full-converter-wind-turbine-based-on|Field Validated Generic EMT-Type Model of a Full Converter W]] | 2018 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm|An Efficient Phase Domain Synchronous Machine Model With Con]] | 2019 |
| [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation|Phase-domain model of twelve-phase synchronous machine for E]] | 2022 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy--16|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el|Modeling of cross-magnetization effects in saturated synchro]] | 2026 |