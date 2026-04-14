---
title: "节点分析与伴随电路 (Nodal Analysis / Companion Circuit)"
type: method
tags: [nodal-analysis, companion-circuit, emtp, admittance, conductance]
created: "2026-04-13"
---

# 节点分析与伴随电路 (Nodal Analysis / Companion Circuit)

## 概述

节点分析法（Nodal Analysis）是EMTP类仿真器的核心求解方法。通过将电路中每个元件替换为其伴随电路（Companion Circuit）模型，形成节点导纳矩阵，求解节点电压。

## 核心原理

### 伴随电路模型
- 电阻：导纳 G = 1/R
- 电感：伴随电流源 + 等效电导（梯形积分）
- 电容：伴随电流源 + 等效电导
- 传输线：Bergeron模型（行波等值）

### 求解流程
1. 每个元件转换为伴随电路
2. 组装节点导纳矩阵 G·v = i
3. 求解线性方程组得到节点电压
4. 由电压计算支路电流和元件状态

## 数值积分

- **梯形法**：最常用，A稳定但有数值振荡
- **后向Euler**：强阻尼，抑制振荡但精度低
- **Gear法**：多步法，高阶精度
- **2S-DIRK**：对角隐式Runge-Kutta

## 稀疏矩阵求解

- 大型导纳矩阵通常是稀疏的
- 稀疏LU分解（KLU算法）
- 迭代法（共轭梯度）
- GPU加速稀疏求解

## 在EMT中的地位

- EMTP、PSCAD/EMTDC、ATP的标准求解框架
- 所有设备模型最终接入节点方程
- 接口技术的基础（混合仿真、多速率）

## 相关方法
- [[numerical-integration]]
- [[state-space-method]]
- [[fixed-admittance]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|A combined state-space nodal method for the simulation of po]] | 2011 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations]] | 2021 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-|An Automatable Approach for Small-Signal Stability Analysis ]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us|Inaccuracies due to the frequency warping in simulation of e]] | 2023 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |