---
title: "Fast Realization of the Modal Vector Fitting"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/tpwrd.2008.2005462.pdf.pdf"]
---

# Fast Realization of the Modal Vector Fitting

**作者**: 
**年份**: 2009
**来源**: `19、20、21/EMT_task_19/tpwrd.2008.2005462.pdf.pdf`

## 摘要

—Admittance-based rational modeling of multiport systems is prone to error magniﬁcation in applications with high-impedance terminations. This problem is overcome by the modal vector ﬁtting method (MVF) which is formulated in terms of modal components with inverse least-squares weighting by the eigenvalue magnitude. A direct realization of MVF is very demanding in computation time and memory requirements. This paper overcomes the performance deﬁciency via three steps: 1) the required number of MVF iterations is reduced by precalculating an improved initial pole set via conventional vector ﬁtting with inverse magnitude weighting; 2) the pole identiﬁcation step is cal- culated in an efﬁcient manner by solving for only the few essential unknowns while exploiting the sparse matrix structure; a

## 核心贡献

- 应用矢量拟合算法实现频率响应的有理函数逼近

## 使用的方法

- [[vector-fitting]]

## 涉及的模型

- [[fdne-model|FDNE]]
- [[输电线路|输电线路]]
- [[多端口系统|多端口系统]]
- [[极点-留数模型|极点-留数模型]]
- [[状态空间模型|状态空间模型]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[有理建模|有理建模]]
- [[计算效率优化|计算效率优化]]
- [[高阻抗终端精度|高阻抗终端精度]]
- [[小特征值精确表示|小特征值精确表示]]

## 主要发现

—Admittance-based rational modeling of multiport systems is prone to error magniﬁcation in applications with high-impedance terminations
