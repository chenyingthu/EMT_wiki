---
title: "Spurious Power Losses in Modular Multilevel Converter Arm Equivalent Model"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2019.2911052"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/35/TPWRD.2019.2911052.pdf.pdf"]
---

# Spurious Power Losses in Modular Multilevel Converter Arm Equivalent Model

**作者**: 
**年份**: 2019
**来源**: `35/TPWRD.2019.2911052.pdf.pdf`

## 摘要

—This paper demonstrates the presence of spurious power losses or generation in the Arm Equivalent Model (AEM) of Modular Multilevel Converters. Such power losses can occur if model equations are not solved simultaneously with surrounding power circuit equations, which is the case when the AEM is implemented using control system blocks in an electromagnetic transient simulation software. Depending on operating conditions and simulation parameters, these additional losses can represent a significant part of the total converter station losses or even surpass them, thus making simulation results inaccurate. Analytical demonstration of the losses is presented, and several models that eliminate the losses are proposed. Based on simulation studies, only the variable resistance model and equivale

## 核心贡献



- 揭示了MMC桥臂等效模型（AEM）在EMT仿真中因未与主网络方程联立求解而产生的虚假功率损耗问题
- 提出了可变电阻模型与等效电压源模型，有效消除了虚假损耗并兼顾了仿真精度与计算效率

## 使用的方法


- [[nodal-analysis]]
- [[numerical-integration]]

## 涉及的模型


- [[mmc-model]]
- [[average-value-model]]

## 相关主题


- [[mmc]]
- [[vsc]]
- [[hvdc]]

## 主要发现



- 当AEM通过控制框实现而非与主网络方程联立求解时，会因单步延迟产生显著的虚假功率损耗或发电，导致仿真结果失真
- 可变电阻模型和等效电压源模型能够在不显著增加计算负担的前提下，准确消除虚假功率损耗并提供可靠的仿真结果