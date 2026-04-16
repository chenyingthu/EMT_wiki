---
title: "Compact Matrix Formulation for Calculating Lightning-Induced Voltages on Electromagnetic Transient Simulators"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Delivery;2021;36;4;10.1109/TPWRD.2020.3017149"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Leal和De Conti - 2021 - Compact Matrix Formulation for Calculating Lightning-Induced Voltages on Electromagnetic Transient S.pdf"]
---

# Compact Matrix Formulation for Calculating Lightning-Induced Voltages on Electromagnetic Transient Simulators

**作者**: 
**年份**: 2021
**来源**: `10/Leal和De Conti - 2021 - Compact Matrix Formulation for Calculating Lightning-Induced Voltages on Electromagnetic Transient S.pdf`

## 摘要

—In this paper, a compact matrix formulation that sim- pliﬁes the calculation of the lumped sources necessary to estimate lightning-induced effects using transmission line models available in electromagnetic transient programs is proposed. As opposed to an existing solution strategy that requires the sequential calculation of the convolution integrals involving the horizontal component of the incident electric ﬁeld along multiple segments along the line, the proposed matrix solution allows such convolutions to be performed at once. This not only increases the model efﬁciency, but also simpliﬁes the assembly of the solution in matrix-oriented simulation tools. The equations are described in both phase and modal domains, with formulations that are compatible with the universal line model and

## 核心贡献


- 提出紧凑矩阵公式将沿线多段电场卷积积分一次性求解替代顺序计算
- 推导相域与模域矩阵解法分别兼容通用线路模型与Marti频变模型
- 优化集中源组装流程显著提升电磁暂态程序中雷击感应电压计算效率


## 使用的方法


- [[紧凑矩阵运算|紧凑矩阵运算]]
- [[卷积积分|卷积积分]]
- [[指数项拟合|指数项拟合]]
- [[数值积分法|数值积分法]]
- [[相模变换|相模变换]]
- [[集中源等效|集中源等效]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[marti频变模型|Marti频变模型]]
- [[架空线路|架空线路]]


## 相关主题


- [[雷击感应电压|雷击感应电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变线路建模|频变线路建模]]
- [[数值分析|数值分析]]


## 主要发现


- 矩阵公式可一次性完成多段卷积计算效率显著优于传统顺序递归算法
- 相域与模域解法均能精确计算架空线路雷击感应电压验证了模型准确性
- 新公式易于在面向矩阵的仿真工具中集成简化了集中源组装与代码实现


