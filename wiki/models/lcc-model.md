---
title: "线路换相换流器 (LCC)"
type: model
tags: [lcc, hvdc, thyristor, line-commutated, converter]
created: "2026-04-14"
---

# 线路换相换流器 (LCC)

## 概述

线路换相换流器（Line-Commutated Converter, LCC）是传统高压直流输电（HVDC）的核心设备。与电压源换流器（VSC）不同，LCC使用晶闸管作为开关器件，依赖交流电网电压实现换相。

## 主要特点

- 晶闸管开关器件，不可控关断
- 依赖交流系统提供换相电压
- 换相失败是主要故障模式
- 只能向有源网络输电
- 大容量、远距离输电经济性好

## EMT建模方法

### 1. 详细换相模型
- 每个晶闸管单独建模
- 精确表征换相过程
- 适用于换相失败分析

### 2. 平均值模型
- 换相周期平均化
- 忽略开关细节
- 适用于系统级暂态仿真

### 3. 开关函数模型
- 使用开关函数表征换相
- 兼顾精度和效率
- 适用于混合仿真

## 主要故障模式

### 换相失败
- 交流电压跌落导致换相不成功
- 直流电压崩溃
- 无功功率突增
- 是LCC-HVDC最严重的故障

### 直流侧故障
- 直流线路短路
- 直流电流激增
- 需要快速保护动作

## 相关方法
- [[average-value-model]]
- [[nodal-analysis]]

## 相关主题
- [[co-simulation]]
- [[vsc-hvdc]]
- [[mmc-model]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne]] | 2021 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail]] | 2022 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulation for control desi]] | 2019 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algorithm for LCC-HVDC con]] | 2025 |
