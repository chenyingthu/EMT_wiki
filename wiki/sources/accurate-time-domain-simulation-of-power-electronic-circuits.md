---
title: "Accurate time-domain simulation of power electronic circuits✰"
type: source
authors: ['Willy Nzale']
year: 2021
journal: "Electric Power Systems Research, 195 (2021) 107156. doi:10.1016/j.epsr.2021.107156"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Nzale 等 - 2021 - Accurate time-domain simulation of power electronic circuits✰.pdf"]
---

# Accurate time-domain simulation of power electronic circuits✰

**作者**: Willy Nzale
**年份**: 2021
**来源**: `05/Nzale 等 - 2021 - Accurate time-domain simulation of power electronic circuits✰.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Accurate time-domain simulation of power electronic circuits✰ Willy Nzale a,*, Jean Mahseredjian a, Xiaopeng Fu b, Ilhan Kocar a, Christian Dufour c a Polytechnique Montr´eal, Montr´eal, QC H3T 1J4, Canada b Key Laboratory of Smart Grid of Ministry of Education, Tianjin, China

## 核心贡献


- 提出三种改进算法，有效抑制梯形积分在开关切换时引发的数值振荡问题
- 优化不连续点事件定位与状态重初始化机制，提升固定步长仿真精度
- 建立瞬时换相精确处理策略，消除多开关动作累积误差与非特征谐波


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[改进增广节点分析法|改进增广节点分析法]]
- [[线性-二次插值法|线性/二次插值法]]
- [[临界阻尼调整|临界阻尼调整]]
- [[固定步长仿真|固定步长仿真]]


## 涉及的模型


- [[理想开关模型|理想开关模型]]
- [[电力电子电路|电力电子电路]]
- [[rl支路|RL支路]]
- [[电感电容伴随模型|电感电容伴随模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值振荡抑制|数值振荡抑制]]
- [[不连续点处理|不连续点处理]]
- [[事件定位|事件定位]]
- [[状态重初始化|状态重初始化]]
- [[瞬时换相|瞬时换相]]


## 主要发现


- 梯形积分切换后向欧拉法时，若切换前电流非零仍会引发残余数值振荡
- 采用线性插值精确定位过零点可显著降低不连续点处的电压振荡幅值
- 传统重初始化方法在大步长下精度受限，需结合伴随模型历史项修正


