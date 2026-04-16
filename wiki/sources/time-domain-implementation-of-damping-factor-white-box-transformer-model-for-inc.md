---
title: "Time-Domain Implementation of Damping Factor White-Box Transformer Model for Inclusion in EMT Simulation Programs"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery;2020;35;2;10.1109/TPWRD.2019.2902447"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/38/Gustavsen 等 - 2020 - Time-Domain Implementation of Damping Factor White-Box Transformer Model for Inclusion in EMT Simula.pdf"]
---

# Time-Domain Implementation of Damping Factor White-Box Transformer Model for Inclusion in EMT Simulation Programs

**作者**: 
**年份**: 2020
**来源**: `38/Gustavsen 等 - 2020 - Time-Domain Implementation of Damping Factor White-Box Transformer Model for Inclusion in EMT Simula.pdf`

## 摘要

—White-box detailed transformer models are used by manufacturers for predicting internal overvoltages in transformer windings during the lightning impulse test. One such model is the d-factor model, which is based on a lumped-parameter description based on winding discretization with the inclusion of losses via an empirical, frequency-dependent damping factor. This paper shows a procedure for direct inclusion of the d-factor model in electro- magnetic transients simulation programs for use in general studies of network overvoltages. Proper utilization of the model’s diago- nal structure is utilized in combination with real-valued arithmetic for maximum speed in transient simulations, with optional initial- ization from sinusoidal steady-state conditions. The model can be used both as a ter

## 核心贡献



- 提出了一种将d因子白盒变压器模型直接集成到EMT仿真程序中的时域实现方法
- 利用模型的对角结构结合实数运算优化了瞬态仿真速度，并支持正弦稳态初始化
- 扩展了模型功能，使其既可作为端口等效模型，也可用于计算变压器内部节点电压

## 使用的方法


- [[state-space]]
- [[frequency-dependent]]
- [[numerical-integration]]

## 涉及的模型


- [[transformer]]
- [[network-equivalent]]

## 相关主题


- [[harmonic]]
- [[frequency-dependent]]

## 主要发现



- d因子模型的对角结构结合实数运算可显著提升EMT瞬态仿真的计算效率
- 该模型能够准确预测变压器绕组内部过电压，并适用于电网过电压的通用研究