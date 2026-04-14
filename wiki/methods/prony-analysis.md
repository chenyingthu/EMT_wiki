---
title: "Prony 分析 (Prony Analysis)"
type: method
tags: [prony, signal-processing, modal-analysis, system-identification]
created: "2026-04-14"
---

# Prony 分析 (Prony Analysis)

## 概述

Prony分析是一种基于指数信号分解的系统辨识方法，在电力系统EMT仿真中用于从暂态响应数据中提取模态参数（频率、阻尼、幅值）。与矢量拟合类似，Prony分析也是从时域或频域数据中提取系统模型的重要工具。

## 基本原理

- 将信号表示为复指数函数的线性组合
- 通过求解线性方程组提取极点和留数
- 适用于线性时不变系统辨识
- 可从EMT仿真结果中提取系统等效模型

## 应用场景

- 电力系统振荡模态分析
- 传输线参数辨识
- 同步电机参数估计
- 电力系统稳定性分析
- 暂态响应特征提取

## 与矢量拟合的比较

| 特性 | Prony分析 | 矢量拟合 |
|------|-----------|----------|
| 输入数据 | 时域响应 | 频域响应 |
| 应用领域 | 模态分析 | 频变网络等值 |
| 数值稳定性 | 中等 | 较高 |
| 适用频率 | 低频振荡 | 宽频范围 |

## 相关方法
- [[vector-fitting]]
- [[state-space-method]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[network-equivalent]]
