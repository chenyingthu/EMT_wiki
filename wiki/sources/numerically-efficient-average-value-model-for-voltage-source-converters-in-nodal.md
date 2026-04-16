---
title: "Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Open Journal of Power Electronics;2024;5; ;10.1109/OJPEL.2023.3337888"
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf"]
---

# Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs

**作者**: 
**年份**: 2024
**来源**: `29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf`

## 摘要

Discrete detailed models of high-frequency switching voltage source converters (VSCs) are accurate but computationally expensive in simulations of large power-electronics-based systems. For fast/efﬁcient studies, the average-value models (AVMs) of VSCs have proven indispensable, which conven- tionally utilize controlled voltage/current sources to interface with external circuits. In nodal-analysis-based electromagnetic transient (EMT) simulation programs with a non-iterative solution, the interfacing variables are computed based on the values of input voltages/currents calculated at the previous time step. This delay may cause numerical inaccuracy and/or instability at large simulation time steps. Recently, a so-called directly-interfaced AVM (DI-AVM) has been developed for VSCs that avoid

## 核心贡献


- 提出广义直接接口平均值模型，消除传统受控源接口的一步计算延迟
- 构建悬浮节点假设下的扩展等效电导矩阵，实现与外部网络方程同步求解
- 解除传统模型对交直流侧接地的结构限制，支持任意拓扑与多换流器配置


## 使用的方法


- [[节点分析法|节点分析法]]
- [[平均值建模|平均值建模]]
- [[直接接口技术|直接接口技术]]
- [[电导矩阵法|电导矩阵法]]
- [[非迭代求解|非迭代求解]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[详细开关模型|详细开关模型]]
- [[传统受控源平均值模型|传统受控源平均值模型]]
- [[直流侧电容|直流侧电容]]
- [[戴维南等效电网|戴维南等效电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步长仿真|大时间步长仿真]]
- [[数值稳定性|数值稳定性]]
- [[电力电子系统建模|电力电子系统建模]]
- [[节点接口技术|节点接口技术]]


## 主要发现


- 在平衡与不平衡工况下，新模型在大时间步长下仍保持高精度与数值稳定性
- 相比传统接口模型，消除单步延迟导致的数值误差，显著提升仿真计算效率
- 模型无需交直流侧接地假设，可灵活适配任意换流器拓扑及多机并联系统


