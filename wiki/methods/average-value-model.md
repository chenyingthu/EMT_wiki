---
title: "平均值模型 (Average Value Model)"
type: method
tags: [avm, average-value, converter-modeling, simplification]
created: "2026-04-13"
---

# 平均值模型 (Average Value Model)

## 概述

平均值模型（Average Value Model, AVM）是一种简化电力电子换流器开关过程的建模方法。通过平均化开关周期内的高频纹波，AVM大幅减少了计算量，同时保留了换流器的低频动态特性。

## 核心思想

- 将开关周期内的脉冲波形替换为平均值
- 忽略开关纹波，保留基频和低频动态
- 可用连续函数替代离散的开关状态

## 在MMC中的应用

- MMC增强平均值模型
- MMC高效建模（嵌套快速求解）
- 适用于大规模MMC-MTDC系统仿真
- 计算复杂度降低1-2个数量级

## 优势与局限

### 优势
- 大幅减少计算量
- 允许更大仿真步长
- 适合系统级暂态分析

### 局限
- 丢失高频开关谐波
- 不适用于谐波共振分析
- 需要额外建模开关损耗

## 相关方法
- [[state-space-method]]
- [[multirate-method]]

## 相关模型
- [[mmc-model]]
- [[vsc-model]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With ]] | 2021 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters W]] | 2021 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems W]] | 2022 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
| [[harmonic-preserved-average-value-model-for-converters-in-electromagnetic-transie|Harmonic-Preserved Average-Value Model for Converters in Ele]] | 2026 |