---
title: "Robust Passivity Enforcement Scheme for"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/34/tpwrd.2009.2035916.pdf.pdf"]
---

# Robust Passivity Enforcement Scheme for

**作者**: 
**年份**: 2010
**来源**: `34/tpwrd.2009.2035916.pdf.pdf`

## 摘要

—This paper proposes an algorithm to enforce passivity on the time-domain simulation model for a multi-conductor cable or transmission line. The model is ﬁrst reformulated in a form which reduces the severity of passivity violations. The frequency sweep method is then used to identify any remaining passivity violating regions of the model’s frequency response. These small passivity violations are then removed using a linear constrained least squares algorithm to perturb the diagonal elements of propagation matrix. The passivity enforcement algorithm is ap- plied to the Universal Line Model (ULM), a widely used robust phase domain formulation implemented in many commercial electromagnetic transients simulation programs. Two examples of multi-conductor underground cable systems, one for ac a

## 核心贡献



- 提出了一种针对多导体电缆与输电线路时域仿真模型的鲁棒无源性强制算法
- 通过线性约束最小二乘法扰动传播矩阵对角元素，有效消除曲线拟合模型中的无源性违规，并成功集成于通用线路模型(ULM)

## 使用的方法


- [[passivity]]
- [[vector-fitting]]
- [[frequency-dependent]]

## 涉及的模型


- [[transmission-line]]
- [[cable]]

## 相关主题


- [[hvdc]]
- [[passivity]]

## 主要发现



- 所提算法能有效识别并消除多导体线路时域模型中的无源性违规，避免非物理能量生成导致的仿真数值不稳定
- 在交流与高压直流(HVDC)地下电缆系统中的应用验证表明，该方法在保证计算效率的同时显著提升了电磁暂态仿真的鲁棒性与准确性