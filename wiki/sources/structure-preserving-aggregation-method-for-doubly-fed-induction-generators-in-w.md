---
title: "Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Energy Conversion;2022;37;2;10.1109/TEC.2021.3126571"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/36/Li 等 - 2022 - Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion.pdf"]
---

# Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion

**作者**: 
**年份**: 2022
**来源**: `36/Li 等 - 2022 - Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion.pdf`

## 摘要

—An aggregation method is proposed that transforms the multiple DFIGs into an equivalent DFIG model that retains the major collective dynamic characteristics of a group of DFIGs. It is intended for Electromagnetic Transients Simulation (EMT). The aggregated machine can take into account different speeds and parameters of each of the individual DFIGs and the connecting impedance of individual DFIGs. Starting with a State Variable (SV) modelofanindividualDFIG,aggregationiscarriedoutrecursively, by combining two DFIGs at a time and then reducing the order of the aggregate to match the state variable equations of a single DFIG so that the steady state performances are identical. Validation is carried out by comparing the detailed electromagnetic transient (EMT) simulation of the unreduced syst

## 核心贡献



- 提出一种保持结构的DFIG聚合方法，将多台DFIG等效为单台模型并保留群体动态特性
- 通过递归聚合与状态方程阶数匹配，显著降低风电场模型阶数以提升EMT仿真效率

## 使用的方法


- [[state-space]]
- [[network-equivalent]]

## 涉及的模型


- [[dfig-model]]

## 相关主题


- [[wind-farm]]
- [[dfig]]

## 主要发现



- 聚合模型在稳态性能上与详细未简化系统完全一致
- 聚合模型能准确复现系统主导暂态响应，同时大幅降低模型阶数并提高仿真效率