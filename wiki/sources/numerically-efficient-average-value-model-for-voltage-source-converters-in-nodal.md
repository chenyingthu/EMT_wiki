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

- 采用平均值模型简化换流器开关过程，大幅提升计算效率
- 基于节点分析和伴随电路法建立EMT求解框架

## 使用的方法

- [[average-value-model]]
- [[nodal-analysis]]

## 涉及的模型

- [[vsc-model|VSC]]
- [[详细开关模型|详细开关模型]]
- [[受控电压-电流源模型|受控电压/电流源模型]]
- [[average-value-model|平均值模型]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值效率|数值效率]]
- [[接口技术|接口技术]]
- [[大时间步长仿真|大时间步长仿真]]
- [[数值稳定性与精度|数值稳定性与精度]]

## 主要发现

Discrete detailed models of high-frequency switching voltage source converters (VSCs) are accurate but computationally expensive in simulations of large power-electronics-based systems
