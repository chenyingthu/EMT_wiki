---
title: "Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immersed Transformers"
type: source
authors: ['CNKI']
year: 2024
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Liu 等 - 2024 - Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immers.pdf"]
---

# Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immersed Transformers

**作者**: CNKI
**年份**: 2024
**来源**: `05/Liu 等 - 2024 - Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immers.pdf`

## 摘要

In response to the problem of low efficiency in calculating transient temperature rise of oil immersed power transformers, this paper proposes POD-αATS reduced order adaptive variable step size transient calculation method. First, the article briefly derives the finite element discrete equation for calculating the transient temperature rise of transformer windings. Next, the proper orthogonal decomposition (POD) order reduction algorithm is adopted to improve the problems of excessive number of conditions and equation orders in traditional transient calculations. Meanwhile, for the time step selection problem in transient calculations, this paper proposes a method suitable for nonlinear problems α ATS (adaptive time stepping based on α factor, αATS) variable step size strategy. Then, in or

## 核心贡献


- 提出POD降阶算法，有效降低有限元方程阶数与条件数，提升单步求解效率。
- 提出αATS自适应变步长策略，结合收敛速率因子动态优化非线性瞬态步长。
- 构建POD-αATS耦合计算方法，实现流热耦合场高精度快速瞬态求解。


## 使用的方法


- [[有限元法|有限元法]]
- [[本征正交分解-pod|本征正交分解(POD)]]
- [[降阶建模|降阶建模]]
- [[αats自适应变步长算法|αATS自适应变步长算法]]
- [[奇异值分解|奇异值分解]]
- [[流热耦合计算|流热耦合计算]]


## 涉及的模型


- [[油浸式电力变压器|油浸式电力变压器]]
- [[变压器绕组|变压器绕组]]
- [[二维八分区流热耦合模型|二维八分区流热耦合模型]]
- [[有限元离散模型|有限元离散模型]]


## 相关主题


- [[瞬态温升计算|瞬态温升计算]]
- [[降阶算法|降阶算法]]
- [[自适应时间步长|自适应时间步长]]
- [[流热耦合仿真|流热耦合仿真]]
- [[热点温度预测|热点温度预测]]
- [[快速数值计算|快速数值计算]]


## 主要发现


- 算法精度与全阶定步长法一致，流场计算效率提升约45倍，大幅缩短耗时。
- 温度场计算效率提升约38倍，有效克服传统变步长法在非线性问题中的不稳定性。
- 温升实验验证了该方法的准确性与高效性，证明其具备工程实际应用价值。


