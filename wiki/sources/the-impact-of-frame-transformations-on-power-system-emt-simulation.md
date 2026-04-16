---
title: "The Impact of Frame Transformations on Power System EMT Simulation"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2024;39;1;10.1109/TPWRS.2023.3242823"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/Li 等 - 2024 - The Impact of Frame Transformations on Power System EMT Simulation.pdf"]
---

# The Impact of Frame Transformations on Power System EMT Simulation

**作者**: 
**年份**: 2023
**来源**: `37/Li 等 - 2024 - The Impact of Frame Transformations on Power System EMT Simulation.pdf`

## 摘要

—This article investigates the impact of frame trans- formations on the accuracy of numerical discretization in power system transient and stability studies. As analysed, frame transfor- mations inﬂuence the convergence of the numerical discretization. Speciﬁcally, for an explicit discretization method (e.g., forward Euler method), the stability of the original system is best preserved in the frame where the system eigenvalue is closer to the origin of the complex plane, e.g., in the stationary frame for inductors and capacitors, and in the synchronous frame for dq-frame controllers of inverters. Simulation results are given to validate the theoretical analysis. Index Terms—Power system stability, electromagnetic

## 核心贡献



- 揭示了参考系变换对电力系统EMT仿真中数值离散化收敛性与精度的影响机制
- 提出了基于系统特征值复平面位置选择最优参考系（静止系或同步旋转系）以最大化显式离散方法稳定性的理论准则

## 使用的方法


- [[numerical-integration]]
- [[real-time]]

## 涉及的模型


- [[vsc-model]]

## 相关主题


- [[state-space]]
- [[numerical-integration]]

## 主要发现



- 参考系变换会显著影响数值离散化方法的收敛性，系统特征值在复平面上越靠近原点，离散化稳定性越好
- 对于显式离散方法（如前向欧拉法），电感与电容在静止参考系下仿真最稳定，而逆变器的dq轴控制器在同步旋转参考系下仿真最稳定