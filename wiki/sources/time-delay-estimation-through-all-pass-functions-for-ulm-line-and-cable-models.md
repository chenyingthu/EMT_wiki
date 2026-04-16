---
title: "Time-delay estimation through all-pass functions for ULM line and cable models"
type: source
authors: ['S. Loaiza-Elejalde']
year: 2026
journal: "Electric Power Systems Research, 252 (2026) 112414. doi:10.1016/j.epsr.2025.112414"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/38/Loaiza-Elejalde 等 - 2026 - Time-delay estimation through all-pass functions for ULM line and cable models.pdf"]
---

# Time-delay estimation through all-pass functions for ULM line and cable models

**作者**: S. Loaiza-Elejalde
**年份**: 2026
**来源**: `38/Loaiza-Elejalde 等 - 2026 - Time-delay estimation through all-pass functions for ULM line and cable models.pdf`

## 摘要

Time-delay estimation through all-pass functions for ULM line and , J.L. Naredo a, Martin G. Vega-Grijalva b, O. Ramos-Lea˜nos c Traveling-wave line models, such as the ULM, are widely used in time-domain EMT simulations for power systems. These models require the rational approximation of both the characteristic admittance matrix Yc, and the propagation matrix H. Rational fitting of H is challenging due to the inclusion of a mix of modal delays in all

## 核心贡献



- 提出了一种基于全通函数与延迟均衡的迭代时延估计方法，用于改进ULM线路与电缆模型的传播矩阵有理拟合
- 该方法在拟合过程中严格保证了合成模型的因果性与最小相位特性，且相比传统均方根误差最小化方法具有更高的计算效率

## 使用的方法


- [[vector-fitting]]

## 涉及的模型


- [[transmission-line]]
- [[cable]]

## 相关主题


- [[frequency-dependent]]
- [[passivity]]

## 主要发现



- 所提方法通过全通滤波器提取模态时延，成功解决了传统Bode积分法在截止频率选取上的局限性，确保了有理近似的因果性
- 在合成传递函数、地下电缆系统及架空线路EMT响应测试中，新方法在保持拟合精度与现有方法相当的前提下，显著降低了迭代次数