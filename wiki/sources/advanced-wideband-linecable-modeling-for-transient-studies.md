---
title: "Advanced Wideband Line/Cable Modeling for Transient Studies"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Delivery;2024;39;5;10.1109/TPWRD.2024.3449868"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Ramirez 等 - 2024 - Advanced Wideband LineCable Modeling for Transient Studies.pdf"]
---

# Advanced Wideband Line/Cable Modeling for Transient Studies

**作者**: 
**年份**: 2024
**来源**: `06/Ramirez 等 - 2024 - Advanced Wideband LineCable Modeling for Transient Studies.pdf`

## 摘要

—The grouping of propagation modes in line/cable sys- tems involving a large number of conductors has been central in recent research regarding the stability of simulations for elec- tromagnetic transient (EMT) studies. This article presents three improvements to the existing wideband line/cable modeling tech- niques for EMT analysis. The ﬁrst improvement consists of cal- culating optimum time delays such that the oscillations in the phase angle of the propagation function are reduced. The second is a novel strategy for grouping propagation modes. As a third improvement, the maximum ﬁtting frequency of a rapidly decaying mode is limited when its magnitude is below a threshold value. It is demonstrated that these modiﬁcations improve the stability characteristics oftime-domainsimulation,com

## 核心贡献


- 提出基于最小相位函数的最优时延计算方法有效降低传播函数相位角振荡
- 设计基于时延相近性的自适应传播模式分组策略显著降低残差与极点比值
- 引入快速衰减模式最大拟合频率阈值限制机制提升高频段拟合精度与稳定性


## 使用的方法


- [[极点-留数拟合|极点-留数拟合]]
- [[最小相位函数分析|最小相位函数分析]]
- [[布伦特优化算法|布伦特优化算法]]
- [[自适应模式分组|自适应模式分组]]
- [[频域综合|频域综合]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[输电线路|输电线路]]
- [[地下电缆|地下电缆]]
- [[频变电缆模型-fdcm|频变电缆模型(FDCM)]]
- [[多导体电缆系统|多导体电缆系统]]


## 相关主题


- [[宽频线路电缆建模|宽频线路电缆建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性|数值稳定性]]
- [[无源性违规|无源性违规]]
- [[频率相关参数|频率相关参数]]
- [[时域仿真|时域仿真]]


## 主要发现


- 改进方法显著降低残差极点比与无源性违规解决传统ULM短电缆系统失稳
- 在含九十六根电缆与双回架空线复杂系统中验证时域仿真稳定性与精度均提升
- 最优时延与频率阈值限制有效减少传播函数高频相位振荡降低有理逼近阶数


