---
title: "Modeling for large-scale offshore wind farm using multi-thread parallel computing"
type: source
authors: ['Ming Zou']
year: 2023
journal: "International Journal of Electrical Power and Energy Systems, 148 (2023) 108928. doi:10.1016/j.ijepes.2022.108928"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Zou 等 - 2023 - Modeling for large-scale offshore wind farm using multi-thread parallel computing.pdf"]
---

# Modeling for large-scale offshore wind farm using multi-thread parallel computing

**作者**: Ming Zou
**年份**: 2023
**来源**: `26/Zou 等 - 2023 - Modeling for large-scale offshore wind farm using multi-thread parallel computing.pdf`

## 摘要

Electrical Power and Energy Systems 148 (2023) 108928 0142-0615/© 2022 Elsevier Ltd. All rights reserved. Modeling for large-scale offshore wind farm using multi-thread State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University (NCEPU), 102206 Beijing, China Large-scale Offshore Wind Farms (OWFs) face difficulty when carrying out microsecond-level Electro-Magnetic

## 核心贡献


- 提出基于内部节点消元的单机集成等值建模方法，有效降低导纳矩阵阶数
- 设计相间解耦算法消除三相互阻抗，满足风机与集电线路并联等值条件
- 将OpenMP多线程并行技术融入全场求解流程，实现大规模风电场仿真加速


## 使用的方法


- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[内部节点消元|内部节点消元]]
- [[相间解耦|相间解耦]]
- [[多线程并行计算|多线程并行计算]]
- [[诺顿等值|诺顿等值]]


## 涉及的模型


- [[pmsg|PMSG]]
- [[全功率变流器|全功率变流器]]
- [[lc滤波器|LC滤波器]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[风力发电机|风力发电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[并行计算|并行计算]]
- [[网络等值|网络等值]]
- [[海上风电|海上风电]]


## 主要发现


- 所提等值模型相比详细模型最大相对误差低于0.96%，保持高精度动态特性
- 多线程并行计算大幅提升大规模海上风电场仿真速度，获得显著加速比
- 该方法克服短集电线路自然解耦限制，实现微秒级高效电磁暂态仿真


