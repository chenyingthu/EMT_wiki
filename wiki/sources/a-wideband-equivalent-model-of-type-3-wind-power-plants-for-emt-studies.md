---
title: "A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies"
type: source
authors: ['未知']
year: 2016
journal: "IEEE Transactions on Power Delivery;2016;31;5;10.1109/TPWRD.2016.2551287"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Hussein 等 - 2016 - A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies.pdf"]
---

# A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies

**作者**: 
**年份**: 2016
**来源**: `05/Hussein 等 - 2016 - A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies.pdf`

## 摘要

—This paper presents the development and validation of an accurate and computationally efﬁcient wideband reduced-order dynamic equivalent model for the Type-3-based wind power plant (WPP). The proposed Type-3 WPP equivalent model reproduces the dynamic behavior of the WPP in response to an electromag- netic transient in the host power system and is composed of two parts: 1) a static frequency-dependent network equivalent model which represents the response of all passive components of the WPP in a wideband frequency range, and 2) a dynamic low-frequency equivalent model that represents the aggregated dynamic model of the doubly-fed asynchronous generator (which is also referred to as doubly-fed induction generator) wind turbine generators, their local controls, and the WPP supervisory cont

## 核心贡献


- 提出宽频降阶动态等值模型，结合频变网络与低频动态模块精准复现暂态响应
- 采用矢量拟合技术构建无源网络频响模型，结合伴随电路法实现高效时域接口
- 建立聚合双馈风机及控制系统的低频动态等值模块，显著降低仿真计算负担


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[频变网络等值|频变网络等值]]
- [[伴随电路法|伴随电路法]]
- [[动态低频等值|动态低频等值]]
- [[降阶建模|降阶建模]]
- [[双线性变换|双线性变换]]


## 涉及的模型


- [[type-3风电场|Type-3风电场]]
- [[双馈异步发电机|双馈异步发电机]]
- [[风力发电机组|风力发电机组]]
- [[集电网络|集电网络]]
- [[背靠背变流器|背靠背变流器]]
- [[风电场协调控制|风电场协调控制]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[宽频等值建模|宽频等值建模]]
- [[实时仿真|实时仿真]]
- [[故障穿越|故障穿越]]
- [[风电场降阶等值|风电场降阶等值]]
- [[频率相关建模|频率相关建模]]


## 主要发现


- 相比详细模型大幅降低计算负担，在PSCAD中验证保持高精度暂态响应
- 联合频变网络与低频动态模块，准确复现外部扰动下的端口响应与故障穿越特性
- 模型计算效率满足实际硬件资源限制，具备应用于大规模系统实时仿真的能力


