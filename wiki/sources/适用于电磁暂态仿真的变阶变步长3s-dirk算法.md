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

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[numerical-integration|数值积分]]
- [[变阶变步长积分|变阶变步长积分]]
- [[临界阻尼调整方法-cda|临界阻尼调整方法(CDA)]]
- [[算法切换策略|算法切换策略]]
- [[布彻矩阵分析|布彻矩阵分析]]

## 涉及的模型

- [[线性元件|线性元件]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值振荡抑制|数值振荡抑制]]
- [[数值积分算法|数值积分算法]]
- [[变步长仿真|变步长仿真]]

## 主要发现

When dealing with the numerical oscillation in electromagnetic transient simulation, a lower order numerical integration switched may lead to a larger numerical error
