---
title: "An improved low-frequency transformer model for use in GIC studies"
type: source
authors: ['未知']
year: 2004
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An improved low-frequency transformer model for use in GIC studies.pdf"]
---

# An improved low-frequency transformer model for use in GIC studies

**作者**: 
**年份**: 2004
**来源**: `07&08/An improved low-frequency transformer model for use in GIC studies.pdf`

## 摘要

—A hysteresis model based on the Jiles–Atherton theory is incorporated into a power transformer model in an electromagnetic transient program (EMTP)-type program. The eddy current effects are also included in the same model. Com- parisons are made between recorded and simulated waveforms using a single-phase distribution transformer. A good agreement is achieved between recorded and simulated data. Index Terms—Eddy currents, hysteresis, losses, power trans- formers, simulation. I. INTRODUCTION G EOMAGNETICALLY induced currents (GICs) are the ground effect of a complicated space weather chain that originates in the sun. The flow of GIC through power trans- formers has been the root cause of operational and equipment problems in power systems during a geomagnetic disturbance

## 核心贡献


- 引入Jiles-Atherton磁滞理论替代分段线性模型，实现铁芯剩磁自动初始化与精确追踪
- 集成经典涡流与异常损耗效应，提升低频地磁感应电流工况下的变压器仿真精度
- 基于磁等效电路推导动态电感矩阵，支持多绕组多铁芯结构的通用化磁滞特性建模


## 使用的方法


- [[jiles-atherton磁滞模型|Jiles-Atherton磁滞模型]]
- [[磁等效电路法|磁等效电路法]]
- [[电感矩阵推导|电感矩阵推导]]
- [[电磁暂态仿真-emtdc|电磁暂态仿真(EMTDC)]]
- [[涡流损耗建模|涡流损耗建模]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[单相配电变压器|单相配电变压器]]
- [[变压器铁芯磁路模型|变压器铁芯磁路模型]]


## 相关主题


- [[地磁感应电流-gic-分析|地磁感应电流(GIC)分析]]
- [[铁磁半周饱和|铁磁半周饱和]]
- [[磁滞与涡流建模|磁滞与涡流建模]]
- [[低频电磁暂态仿真|低频电磁暂态仿真]]
- [[谐波与无功特性分析|谐波与无功特性分析]]


## 主要发现


- 仿真波形与实测数据高度吻合，验证了JA磁滞模型在低频GIC工况下的准确性
- 新模型能自动处理铁芯剩磁与反冲环，克服了传统分段线性模型长时仿真磁通衰减缺陷
- 准确捕捉了半周饱和引发的非对称励磁电流、无功激增及显著谐波电流现象


