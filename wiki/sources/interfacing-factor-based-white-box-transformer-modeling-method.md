---
title: "Interfacing Factor-Based White-Box Transformer Modeling Method"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/24/Gustavsen和Portillo - 2014 - Interfacing ${rm k}$-Factor Based White-Box Transformer Models With Electromagnetic Transients Prog.pdf"]
---

# Interfacing Factor-Based White-Box Transformer Modeling Method

**作者**: 
**年份**: 2014
**来源**: `24/Gustavsen和Portillo - 2014 - Interfacing ${rm k}$-Factor Based White-Box Transformer Models With Electromagnetic Transients Prog.pdf`

## 摘要

—White-box transformer models are used by trans- former manufacturers during the dielectric design of windings. The models are often based on constant parameters (RLCG ma- trices) with the high-frequency losses accounted for by a scaling of the dc resistance ( -Factor). We show an efﬁcient procedure for interfacing such models with Electromagnetic Transients Program (EMTP)-type circuit simulators via state equations and a Norton equivalent. The approach makes no approximations except for the discretization in the time domain. Diagonalization is utilized for achieving high computational efﬁciency. Proprietary information about internal voltages is optionally hidden from the user. Internal surge arresters are handled by the EMTP circuit solver by declaring their connection points as external

## 核心贡献

- 建立了更精确的transformer电磁暂态模型，考虑了频率相关特性和非线性效应

## 使用的方法

- [[状态方程法|状态方程法]]
- [[诺顿等效|诺顿等效]]
- [[矩阵对角化|矩阵对角化]]
- [[时域离散化|时域离散化]]
- [[α因子缩放法|α因子缩放法]]
- [[模型接口技术|模型接口技术]]

## 涉及的模型

- [[transformer-model]]

## 相关主题

- [[电磁暂态仿真-emtp|电磁暂态仿真(EMTP)]]
- [[模型接口|模型接口]]
- [[高频损耗建模|高频损耗建模]]
- [[计算效率优化|计算效率优化]]
- [[模型保密|模型保密]]
- [[自动初始化|自动初始化]]

## 主要发现

—White-box transformer models are used by trans- former manufacturers during the dielectric design of windings
