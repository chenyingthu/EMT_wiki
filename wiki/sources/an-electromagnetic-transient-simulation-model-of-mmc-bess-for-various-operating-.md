---
title: "An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;5;10.1109/TPWRD.2025.3599870"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions.pdf"]
---

# An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions

**作者**: 
**年份**: 2025
**来源**: `07&08/An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions.pdf`

## 摘要

—Existing electromagnetic transient (EMT) simulation models of the modular multilevel converter with an embedded battery energy storage system (MMC-BESS) often suffer from computational inefﬁciencies and difﬁculties in accurately simulat- ing fault behaviors. To address these issues, this paper proposes an efﬁcient EMT model for the MMC-BESS. The proposed model im- proves the detailed equivalent model (DEM) by accounting for the complex scenarios where both switches in the same leg are simul- taneously turned off. The converter blocked state is simulated by incorporating auxiliary PSCAD switches and leveraging its built-in interpolation algorithms, while the battery disconnection is simu- lated by using supplementary decision formulas. Furthermore, a speedup calculation method is introduce

## 核心贡献


- 提出改进详细等效模型，解决同桥臂双开关同时关断时的建模失效问题
- 结合辅助开关与插值算法实现闭锁仿真，引入决策公式处理电池断开工况
- 提出基于工况简化的加速计算方法，大幅减少运算量并显著提升仿真效率


## 使用的方法


- [[详细等效模型-dem|详细等效模型(DEM)]]
- [[pscad辅助开关与插值算法|PSCAD辅助开关与插值算法]]
- [[补充决策公式|补充决策公式]]
- [[加速计算方法|加速计算方法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[子模块-sm|子模块(SM)]]
- [[buck-boost变换器|Buck-Boost变换器]]
- [[详细开关模型-dsm|详细开关模型(DSM)]]
- [[average-value-model|平均值模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[换流器闭锁状态|换流器闭锁状态]]
- [[电池断开仿真|电池断开仿真]]
- [[交直流故障分析|交直流故障分析]]
- [[仿真加速优化|仿真加速优化]]


## 主要发现


- 模型在交直流故障及电池断开工况下，仿真波形与详细开关模型高度吻合
- 加速算法有效降低计算复杂度，在保持高精度的同时显著提升暂态仿真速度


