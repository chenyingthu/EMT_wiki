---
title: "An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients"
type: source
authors: ['N. Hooda']
year: 2017
journal: "Procedia Engineering, 186 (2017) 349-356. doi:10.1016/j.proeng.2017.03.211"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients.pdf"]
---

# An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients

**作者**: N. Hooda
**年份**: 2017
**来源**: `07&08/An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients.pdf`

## 摘要

Rural water networks in the developing world are typically branched networks with a single water source. The main design decision to be made for such networks is the choice of pipe diameters from a discrete set of commercially available pipe diameters. Larger the pipe diameters, better the service (pressure), but higher is the capital cost. In general, each link (connection between two nodes) in the network can consist of several pipe segments of differing diameters. For such networks, existing design tools solve the constrained-optimization problem heuristically [1] [2]. In [3], an ILP formulation is proposed for the special case of one pipe diameter per link. This means that currently one can either get an optimal solution for the special case of one piped segment per link or get a non-o

## 核心贡献


- 提出多管段管径线性规划模型，保持全局最优并显著提升求解效率
- 开发集成GIS的JalTantra系统，实现树状供水管网自动化优化设计


## 使用的方法


- [[线性规划-lp|线性规划(LP)]]
- [[整数线性规划-ilp|整数线性规划(ILP)]]
- [[hazen-williams水头损失公式|Hazen-Williams水头损失公式]]
- [[约束优化算法|约束优化算法]]


## 涉及的模型


- [[树状供水管网模型|树状供水管网模型]]
- [[单水源无环网络|单水源无环网络]]
- [[多管段组合模型|多管段组合模型]]
- [[jaltantra优化系统|JalTantra优化系统]]


## 相关主题


- [[供水管网优化设计|供水管网优化设计]]
- [[管径离散选择|管径离散选择]]
- [[压力约束优化|压力约束优化]]
- [[线性规划应用|线性规划应用]]
- [[gis集成设计|GIS集成设计]]


## 主要发现


- 不预设管段限制的LP模型运行更快，且自然收敛至最多两种相邻管径最优解
- 新模型在求解精度与计算耗时上均优于传统启发式算法及单管径整数规划方法


