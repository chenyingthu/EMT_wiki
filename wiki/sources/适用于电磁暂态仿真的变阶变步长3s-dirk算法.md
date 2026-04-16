---
title: "适用于电磁暂态仿真的变阶变步长3S-DIRK算法"
type: source
authors: ['叶小晖']
year: 2020
journal: "电力系统自动化"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/叶小晖 等 - 2020 - 适用于电磁暂态仿真的变阶变步长3S-DIRK算法.pdf"]
---

# 适用于电磁暂态仿真的变阶变步长3S-DIRK算法

**作者**: 叶小晖
**年份**: 2020
**来源**: `40/叶小晖 等 - 2020 - 适用于电磁暂态仿真的变阶变步长3S-DIRK算法.pdf`

## 摘要

When dealing with the numerical oscillation in electromagnetic transient simulation, a lower order numerical integration switched may lead to a larger numerical error. Based on the butcher tableau, variable order and variable step 3S-DIRK algorithm is proposed.

## 核心贡献



- 提出适用于电磁暂态仿真的变阶变步长3S-DIRK算法
- 设计基于4种分算法的切换策略，保证切换时等值导纳不变且全程计算精度不低于2阶
- 利用算法的L稳定特性消除数值振荡，并支持变步长计算以提升仿真效率

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]
- [[state-space]]
- [[fixed-admittance]]

## 涉及的模型


- [[network-equivalent]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值振荡抑制|数值振荡抑制]]
- [[数值积分算法|数值积分算法]]
- [[变步长仿真|变步长仿真]]

## 主要发现



- 3S-DIRK算法在整个仿真过程中可保持不低于2阶的计算精度
- 算法的L稳定性能够有效消除电磁暂态计算中的数值振荡现象
- 算法切换策略可在不同工况下保持元件等值导纳恒定，避免切换引入的误差
- 变步长机制结合多分算法切换显著提升了复杂暂态过程的仿真效率与稳定性