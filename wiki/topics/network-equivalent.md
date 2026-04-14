---
title: "网络等值 (Network Equivalent)"
type: topic
tags: [network-equivalent, thevenin, ward, fdne, reduction]
created: "2026-04-13"
---

# 网络等值 (Network Equivalent)

## 概述

网络等值技术将大规模电力系统简化为等效模型，在保持端口特性不变的前提下大幅减少仿真规模。这是混合仿真、并行计算和大电网仿真的基础技术。

## 等值类型

### 1. 稳态等值
- Ward等值
- REI等值
- 适用于潮流和机电暂态

### 2. 频变等值 (FDNE)
- 考虑频率相关特性的宽频等值
- 多端口Thevenin等值
- 矢量拟合实现

### 3. 动态等值
- 保留关键动态特性
- 同步机等值聚合
- 新能源场站等值

### 4. 多层等值
- 双层网络等值（局部+全局）
- 多区域Thevenin等值
- 混合仿真中的接口等值

## 关键技术

- 参数辨识（Prony分析、最小二乘）
- 无源性补偿
- 在线更新策略
- 等值误差评估

## 相关方法
- [[vector-fitting]]
- [[prony-analysis]]
- [[passivity-enforcement]]

## 相关模型
- [[fdne-model]]
- [[synchronous-machine-model]]
