---
title: "风电场建模 (Wind Farm Modeling)"
type: topic
tags: [wind-farm, dfig, pmsg, wind-turbine, aggregation, equivalent-model]
created: "2026-04-14"
---

# 风电场建模 (Wind Farm Modeling)

## 概述

风电场建模是新能源并网EMT仿真的重要方向。大规模风电场的详细建模面临计算量大的挑战，需要发展等值聚合方法和高效仿真策略。

## 主要风机类型

### 1. DFIG（双馈感应发电机）
- 转子侧变频器控制
- 变速恒频运行
- 广泛应用于陆上和海上风电
- EMT建模需考虑转子动态和控制器

### 2. PMSG（永磁同步发电机）
- 全功率变频器
- 无齿轮箱（直驱）
- 效率高、可靠性好
- 海上风电主流选择

### 3. 异步风力发电机
- 固定转速
- 结构简单
- 早期风电场主要类型

## 等值聚合方法

### 1. 单机等值
- 将整个风电场等值为单台风机
- 适用于电网级仿真
- 忽略场内差异

### 2. 多机等值
- 基于风速分布和机组特性分组
- 多机等值模型
- 兼顾精度和效率

### 3. 通用等值模型
- 基于单机模型扩展
- 适用于不同风机类型
- 保持外特性一致

## EMT仿真挑战

- 大量风机机组的并行仿真
- 风速随机性和波动性
- 多时间尺度动态（电气、机械、控制）
- 故障穿越特性
- 大规模风电场的暂态稳定性

## 相关模型
- [[dfig-model]]
- [[pmsm-model]]
- [[synchronous-machine-model]]

## 相关方法
- [[state-space-method]]
- [[average-value-model]]
- [[fixed-admittance]]

## 相关主题
- [[co-simulation]]
- [[real-time-simulation]]
- [[parallel-computing]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-type-4-wind-power-plant-equivalent-model|Hussein 2013 (4型风电等值)]] | 2013 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech|Yang 2011 (永磁风机群等值聚合)]] | 2011 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[基于单机模型扩展的直驱风电场通用等值模型构建方法|基于单机模型扩展的直驱风电场通用等值模型构建方法]] | 2026 |
