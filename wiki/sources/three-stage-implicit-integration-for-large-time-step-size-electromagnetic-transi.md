---
title: "Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling"
type: source
authors: ['Shilin Gao']
year: 2021
journal: "Electric Power Systems Research, 198 (2021) 107356. doi:10.1016/j.epsr.2021.107356"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/j.epsr.2021.107356.pdf.pdf"]
---

# Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling

**作者**: Shilin Gao
**年份**: 2021
**来源**: `37/j.epsr.2021.107356.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling Shilin Gao a,b,*, Ying Chen a,b, Yankan Song a,b, Shaowei Huang a,b a Department of Electrical Engineering, Tsinghua University, Beijing 100084, China

## 核心贡献



- 将三阶单对角隐式龙格-库塔法（3S-SDIRK）应用于基于移频的电磁暂态（SFEMT）仿真数值积分
- 解决了传统梯形法在大时间步长下引发的持续数值振荡问题，实现了高精度、无振荡且高效的电磁暂态仿真

## 使用的方法


- [[numerical-integration]]

## 涉及的模型


- [[移频等效模型|移频等效模型]]
- [[电磁暂态系统模型|电磁暂态系统模型]]

## 相关主题


- [[dynamic-phasor]]

## 主要发现



- 基于3S-SDIRK的SFEMT仿真能够有效消除梯形法引起的持续数值振荡
- 该方法在采用大时间步长时仍能保持较高的仿真精度，并显著提升了计算效率