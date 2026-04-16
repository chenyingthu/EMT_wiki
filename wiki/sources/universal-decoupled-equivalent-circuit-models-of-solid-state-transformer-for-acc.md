---
title: "Universal Decoupled Equivalent Circuit Models of Solid-State Transformer for Accelerated EMT&#x2010;Type Simulation"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;5;10.1109/TPWRD.2025.3584585"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/39/Li 等 - 2025 - Universal Decoupled Equivalent Circuit Models of Solid-State Transformer for Accelerated EMT‐Type Si.pdf"]
---

# Universal Decoupled Equivalent Circuit Models of Solid-State Transformer for Accelerated EMT&#x2010;Type Simulation

**作者**: 
**年份**: 2025
**来源**: `39/Li 等 - 2025 - Universal Decoupled Equivalent Circuit Models of Solid-State Transformer for Accelerated EMT‐Type Si.pdf`

## 摘要

—Multilevel Multimodule Solid-State Transformer (SST) is emerging as a key technology interfacing MVAC and LVAC systems via chainlink AC-DC converter and Dual Active Bridge (DAB) DC-DC converters. The SST has the advantages of high modularity, bidirectional power transfer, galvanic isolation, and high-frequency power conversion. Fast control prototyping of the SST requires numerically efﬁcient and accurate equivalent circuit models for Electromagnetic Transient (EMT) simulation. This paper proposes universal decoupled equivalent circuit models using switching function to simplify the power converter circuits. Various types of power converters including full-bridge converter, DAB DC-DC converter, and three-phase 3-level converters can be universally modeled by the proposed equivalent circui

## 核心贡献



- 提出了一种基于开关函数的通用解耦等效电路模型，可统一适用于全桥、DAB及三电平等多种功率变换器的去闭锁与闭锁模式
- 采用直流链路解耦策略实现恒定导纳矩阵并显著减少系统节点数，结合开关插值技术在大步长下精确捕捉开关事件，大幅提升EMT仿真效率

## 使用的方法


- [[average-value-model]]
- [[interpolation]]
- [[fixed-admittance]]

## 涉及的模型


- [[transformer]]
- [[vsc-model]]

## 相关主题


- [[real-time]]
- [[numerical-integration]]
- [[nodal-analysis]]

## 主要发现



- 所提等效模型通过恒定导纳矩阵和节点缩减有效克服了传统详细模型因开关数量庞大导致的计算瓶颈
- 引入开关插值技术后，模型在采用较大仿真步长时仍能保持高精度，相比传统详细模型和变导纳矩阵等效模型显著提升了数值计算效率