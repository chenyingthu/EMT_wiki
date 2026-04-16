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


- 提出基于逆幅值加权常规矢量拟合的改进初始极点集预计算方法，显著减少迭代次数。
- 利用稀疏矩阵结构仅求解关键未知数，实现极点识别步骤的高效计算。
- 设计利用矩阵对称性的逐行求解策略，大幅提升残差识别步骤的计算效率。


## 使用的方法


- [[模态矢量拟合|模态矢量拟合]]
- [[矢量拟合|矢量拟合]]
- [[有理拟合|有理拟合]]
- [[极点-留数建模|极点-留数建模]]
- [[最小二乘优化|最小二乘优化]]
- [[特征值分解|特征值分解]]


## 涉及的模型


- [[频率相关网络等值|频率相关网络等值]]
- [[多端口系统|多端口系统]]
- [[极点-留数模型|极点-留数模型]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[宽频带建模|宽频带建模]]
- [[高阻抗终端误差抑制|高阻抗终端误差抑制]]


## 主要发现


- 改进算法在FDNE建模中大幅降低计算时间与内存需求，同时保持模型高精度。
- 逆幅值加权初始极点集有效减少迭代次数，彻底避免小特征值拟合误差放大。
- 稀疏矩阵与对称性优化使极点与残差识别效率显著提升，适用于大规模多端口系统。


