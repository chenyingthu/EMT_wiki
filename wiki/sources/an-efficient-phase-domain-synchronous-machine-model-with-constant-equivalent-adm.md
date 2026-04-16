---
title: "An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery;2019;34;3;10.1109/TPWRD.2019.2897612"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Xia et al. - 2019 - An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix.pdf"]
---

# An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix

**作者**: 
**年份**: 2019
**来源**: `07&08/Xia et al. - 2019 - An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix.pdf`

## 摘要

—In this paper, a new synchronous machine model is de- veloped for electromagnetic transients program type simulations. The stator circuit is expressed in the abc phase domain. The ma- chine model is represented as a Norton equivalent with a current source in parallel with a constant Norton admittance. The ma- chine equations are reformulated so that the computational effort required for the modeling of the machine is reduced. Test stud- ies demonstrate the accuracy of the proposed synchronous ma- chine model and show that the proposed model is computationally more efﬁcient than the existing constant conductance phase domain model and voltage-behind-reactance model. Index Terms—Constant admittance matrix, direct interface, electromagnetic transients program (EMTP), phase domain (PD) model,

## 核心贡献


- 提出相域同步电机诺顿等效模型，实现等效导纳矩阵恒定，避免网络矩阵频繁修改
- 重构电机状态方程并简化受控电流源表达式，显著降低单步仿真计算量与耗时


## 使用的方法


- [[节点分析法|节点分析法]]
- [[相域建模|相域建模]]
- [[诺顿等效|诺顿等效]]
- [[直接接口法|直接接口法]]
- [[状态方程重构|状态方程重构]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[abc相域模型|abc相域模型]]
- [[cc-pd模型|CC-PD模型]]
- [[vbr模型|VBR模型]]
- [[qd0模型|qd0模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[同步电机建模|同步电机建模]]
- [[恒定导纳矩阵|恒定导纳矩阵]]
- [[相域模型|相域模型]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 仿真验证表明该模型精度与现有相域模型相当，且计算效率显著优于CC-PD与VBR模型
- 恒定导纳矩阵特性有效避免了转子位置变化导致的网络导纳矩阵重复求逆与更新


