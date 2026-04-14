---
title: "无源性强制 (Passivity Enforcement)"
type: method
tags: [passivity, stability, vector-fitting, frequency-domain]
created: "2026-04-13"
---

# 无源性强制 (Passivity Enforcement)

## 概述

无源性强制是确保频率相关模型（特别是矢量拟合得到的有理函数模型）满足无源性条件的关键技术。非无源模型在EMT仿真中可能导致数值不稳定，产生非物理的能量增长。

## 无源性条件

- 系统不产生净能量
- 频域条件：Re[H(jω)] ≥ 0
- 极点位于左半平面
- Hamiltonian矩阵无虚轴特征值

## 强制方法

### 残差摄动法
- 微调拟合参数
- 最小化修正量
- 保留原始拟合精度

### 全摄动形式
- 同时调整极点和留数
- 更灵活的修正
- 计算复杂度更高

### 在线无源性补偿
- 混合仿真中的局部补偿
- 双层网络等值
- 实时更新策略

## 应用场景

- 频变网络等值（FDNE）
- 输电线路宽频建模
- 变压器频响模型
- 电缆频变参数

## 相关方法
- [[vector-fitting]]
- [[state-space-method]]

## 相关主题
- [[frequency-dependent-modeling]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |