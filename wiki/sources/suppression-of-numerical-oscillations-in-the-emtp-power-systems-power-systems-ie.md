---
title: "Suppression of numerical oscillations in the EMTP power systems - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/36/59.193849.pdf.pdf"]
---

# Suppression of numerical oscillations in the EMTP power systems - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `36/59.193849.pdf.pdf`

## 摘要

The integration scheme i n  the EJectromagnetic Transients Program EMTP has been modified t o  solve the problem of sustained numerical oscillations that. can occur when the trapezoidal rule has t o  a c t  as a differentiator. These oscillations appear, f o r  instance, on the volt.ae;e across an inductance a f t e r current interruption. The technique presented in t h i s  paper prevents these oscillations by providing critical damping of the discontinuity within one

## 核心贡献



- 提出临界阻尼调整（CDA）算法，通过在间断点执行两个半步长的后向欧拉积分，彻底消除梯形积分法引发的数值振荡
- 使EMTP能够全程使用梯形积分法而无需切换或添加人工阻尼，在抑制振荡的同时避免了相位误差与正常响应失真

## 使用的方法


- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]
- [[frequency-dependent]]

## 相关主题


- [[numerical-integration]]
- [[interpolation]]

## 主要发现



- 后向欧拉积分法具备在两个半步长内对间断点提供完全临界阻尼的特性，可有效抑制梯形法在电流开断等场景下的数值振荡
- CDA方法实现简单且通用性强，可直接应用于电感、电容及频变传输线等复杂非线性模型，且不影响系统其余部分的仿真精度