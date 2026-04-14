---
title: "Supplementary techniques for 2S-DIRK-based EMT simulations"
type: source
authors: ['T. Noda']
year: 2014
journal: "Electric Power Systems Research, Corrected proof. doi:10.1016/j.epsr.2014.04.011"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/36/j.epsr.2014.04.011.pdf.pdf"]
---

# Supplementary techniques for 2S-DIRK-based EMT simulations

**作者**: T. Noda
**年份**: 2014
**来源**: `36/j.epsr.2014.04.011.pdf.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了适用于2S-DIRK方法的补充数值技术，以充分发挥其固有的无振荡特性
- 详细阐述了电压源、电流源及开关器件在2S-DIRK框架下的精确数值表示方法
- 通过数值算例验证了补充技术在消除虚假数值振荡和提升EMT仿真精度方面的有效性

## 使用的方法

- [[两阶段对角隐式runge-kutta方法-2s-dirk|两阶段对角隐式Runge-Kutta方法 (2S-DIRK)]]
- [[梯形积分法-trapezoidal-method|梯形积分法 (Trapezoidal method)]]
- [[临界阻尼调整法-cda|临界阻尼调整法 (CDA)]]
- [[针对电源与开关的补充数值离散技术|针对电源与开关的补充数值离散技术]]

## 涉及的模型

- [[电压源|电压源]]
- [[电流源|电流源]]
- [[开关器件|开关器件]]
- [[电感与电容元件|电感与电容元件]]
- [[电力电子变流器|电力电子变流器]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态(EMT)仿真]]
- [[数值积分算法|数值积分算法]]
- [[数值振荡抑制|数值振荡抑制]]
- [[开关暂态建模|开关暂态建模]]
- [[电力系统数字仿真|电力系统数字仿真]]

## 主要发现

- 传统梯形积分法在电感电流或电容电压突变时会产生虚假的持续数值振荡，严重影响含开关及非线性元件的仿真
- 2S-DIRK方法本身具备固有的无振荡特性，但需配合特定的补充技术才能完全发挥其高精度优势
- 所提出的针对电压源、电流源和开关的补充数值技术能有效消除数值振荡，显著提升仿真的稳定性与准确性
