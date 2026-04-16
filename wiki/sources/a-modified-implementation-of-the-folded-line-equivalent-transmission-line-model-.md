---
title: "A modified implementation of the Folded Line Equivalent transmission line model in the Alternative Transient Program"
type: source
authors: ['Jaimis', 'S.L.', 'Colqui']
year: 2022
journal: "Electric Power Systems Research, 211 (2022) 108185. doi:10.1016/j.epsr.2022.108185"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/02/Colqui 等 - 2022 - A modified implementation of the Folded Line Equivalent transmission line model in the Alternative T.pdf"]
---

# A modified implementation of the Folded Line Equivalent transmission line model in the Alternative Transient Program

**作者**: Jaimis, S.L., Colqui
**年份**: 2022
**来源**: `02/Colqui 等 - 2022 - A modified implementation of the Folded Line Equivalent transmission line model in the Alternative T.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. A modified implementation of the Folded Line Equivalent transmission line Jaimis S.L. Colqui a,∗, Luis Carlos Timaná b, Pablo Torrez Caballero a,c, Sérgio Kurokawa d, José a School of Electrical and Computer Engineering, State University of Campinas - UNICAMP, Av. Albert Einstein 400, Campinas, Brazil b Department of Electronic and Telecommunications Engineering, Catholic University of Colombia, Av. Caracas 46 -13, Bogotá, Colombia

## 核心贡献


- 提出正交变换矩阵实现三相线路参数双向解耦，便于在ATP中用理想变压器搭建电路
- 改进折叠线等效模型将导纳矩阵分解为开路短路分量，结合矢量拟合确保无源性
- 突破特征线法限制允许步长大于传播延时，显著提升大型复杂网络仿真效率


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[折叠线等效模型|折叠线等效模型]]
- [[正交变换|正交变换]]
- [[clarke矩阵解耦|Clarke矩阵解耦]]
- [[节点导纳矩阵分解|节点导纳矩阵分解]]
- [[理想变压器电路实现|理想变压器电路实现]]


## 涉及的模型


- [[三相输电线路|三相输电线路]]
- [[改进折叠线等效模型-mfle|改进折叠线等效模型(MFLE)]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[jmarti模型|JMarti模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[频率相关建模|频率相关建模]]
- [[大型电网仿真|大型电网仿真]]
- [[仿真步长优化|仿真步长优化]]
- [[模态解耦|模态解耦]]


## 主要发现


- 在开路合闸及故障工况下，新模型精度与通用线路模型及JMarti模型高度一致
- 步长取传播延时百分之十至四百时仍保持高精度，有效缩短短线路仿真耗时
- 模型可直接输出模态电压电流，便于高频暂态分析且电路实现简单高效


