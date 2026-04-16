---
title: "Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation"
type: source
authors: ['Shilin Gao']
year: 2022
journal: "International Journal of Electrical Power and Energy Systems, 143 (2022) 108459. doi:10.1016/j.ijepes.2022.108459"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/31/Gao 等 - 2022 - Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation.pdf"]
---

# Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation

**作者**: Shilin Gao
**年份**: 2022
**来源**: `31/Gao 等 - 2022 - Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation.pdf`

## 摘要

Electrical Power and Energy Systems 143 (2022) 108459 0142-0615/© 2022 Elsevier Ltd. All rights reserved. International Journal of Electrical Power and Energy Systems Phase-domain model of twelve-phase synchronous machine for EMTP-type Shilin Gao a, Zhendong Tan b, Yankan Song b,∗, Ying Chen a,b, Chen Shen a,b, Zhitong Yu b

## 核心贡献


- 首次建立十二相同步电机相域模型，填补EMTP类仿真中多相电机建模空白
- 提出恒定电导相域模型，避免网络导纳矩阵每步重分解，显著提升仿真效率
- 设计嵌入式小步长算法，有效改善大时间步长下相域模型的数值计算精度


## 使用的方法


- [[相域建模|相域建模]]
- [[恒定电导模型|恒定电导模型]]
- [[节点分析法|节点分析法]]
- [[梯形积分离散化|梯形积分离散化]]
- [[嵌入式小步长算法|嵌入式小步长算法]]


## 涉及的模型


- [[十二相同步电机|十二相同步电机]]
- [[同步电机相域模型|同步电机相域模型]]
- [[恒定电导模型|恒定电导模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[emtp类仿真|EMTP类仿真]]
- [[综合电力系统|综合电力系统]]
- [[实时仿真|实时仿真]]
- [[多相电机建模|多相电机建模]]


## 主要发现


- 相域模型彻底消除qd0模型接口误差，在大步长下仍保持优异数值稳定性
- 恒定电导模型避免导纳矩阵重复分解，计算耗时大幅降低，满足实时仿真需求
- 嵌入式小步长算法有效抑制大时间步长数值振荡，显著提升瞬态响应精度


