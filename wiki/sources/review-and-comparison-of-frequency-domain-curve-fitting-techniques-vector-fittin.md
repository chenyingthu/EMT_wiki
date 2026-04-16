---
title: "Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and loewner matrix"
type: source
authors: ['B. Salarieh']
year: 2021
journal: "Electric Power Systems Research, 196 (2021) 107254. doi:10.1016/j.epsr.2021.107254"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/Salarieh和De Silva - 2021 - Review and comparison of frequency-domain curve-fitting techniques Vector fitting, frequency-partit.pdf"]
---

# Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and loewner matrix

**作者**: B. Salarieh
**年份**: 2021
**来源**: `33/Salarieh和De Silva - 2021 - Review and comparison of frequency-domain curve-fitting techniques Vector fitting, frequency-partit.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and Manitoba Hydro International Ltd, Winnipeg, MB R3P 1A3, Canada It is a well-known practice to approximate the frequency-domain response of an electrical component or a

## 核心贡献



- 全面回顾并比较了四种主流频域曲线拟合技术（矢量拟合、频域分区拟合、矩阵束法与Loewner矩阵法）
- 通过案例研究系统评估了各方法的拟合精度与阶数需求
- 探讨了模型降阶（MOR）技术在拟合后处理中的应用效果

## 使用的方法


- [[vector-fitting]]
- [[frequency-dependent]]
- [[passivity]]
- [[state-space]]

## 涉及的模型


- [[fdne]]
- [[transformer]]
- [[transmission-line]]

## 相关主题


- [[frequency-dependent]]
- [[network-equivalent]]
- [[vector-fitting]]
- [[passivity]]
- [[state-space]]

## 主要发现



- 不同拟合方法在精度、计算速度与实现复杂度之间存在明显权衡，矩阵束法与Loewner矩阵法具备非迭代且无需初始极点的优势
- 模型降阶技术可在保持较高逼近精度的前提下显著降低状态空间模型阶数，提升EMT仿真效率
- 无源性约束是确保有理函数模型在时域仿真中稳定运行的关键后处理步骤