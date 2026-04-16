---
title: "Simulation of electromagnetic transients with a family of implicit multi-step oscillation-free formulas"
type: source
authors: ['Enrique Melgoza-Vázquez']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112402. doi:10.1016/j.epsr.2025.112402"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/Melgoza-Vázquez - 2026 - Simulation of electromagnetic transients with a family of implicit multi-step oscillation-free formu.pdf"]
---

# Simulation of electromagnetic transients with a family of implicit multi-step oscillation-free formulas

**作者**: Enrique Melgoza-Vázquez
**年份**: 2025
**来源**: `35/Melgoza-Vázquez - 2026 - Simulation of electromagnetic transients with a family of implicit multi-step oscillation-free formu.pdf`

## 摘要

Simulation of electromagnetic transients with a family of implicit Tecnológico Nacional de México / I. T. Morelia, Av. Tecnológico 1500, Morelia, Mich, C P 58120, México The backward diﬀerentiation formulas are a family of implicit integration rules which generalize the backward Euler ﬁnite diﬀerence formula and may be used for electromagnetic transient simulation. These multi-step for- mulas require a number of history terms, improving the precision as the order increases. This approach was

## 核心贡献



- 提出并应用一族隐式多步后向微分公式（BDF）进行电磁暂态仿真，克服了传统梯形法的数值振荡缺陷
- 基于改进节点分析法构建可灵活切换积分阶数的计算框架，历史项仅影响右端向量，易于集成至现有EMT程序

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型

- [[电力系统|电力系统]]
- [[感性支路|感性支路]]

## 相关主题


- [[numerical-integration]]
- [[harmonic]]

## 主要发现



- 1至5阶BDF公式在保持绝对稳定性的同时显著提升了计算精度，且完全消除了开关操作引起的数值振荡
- 该算法额外内存需求极小，无需特殊控制或额外校验即可支持固定或可变步长仿真，具备极高的工程实用性