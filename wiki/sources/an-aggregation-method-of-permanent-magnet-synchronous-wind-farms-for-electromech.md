---
title: "An aggregation method of permanent magnet synchronous wind farms for electromechanical transient stability analysis"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Yang 等 - 2011 - An aggregation method of permanent magnet synchronous generators wind farm model for electromagnetic.pdf"]
---

# An aggregation method of permanent magnet synchronous wind farms for electromechanical transient stability analysis

**作者**: CNKI
**年份**: 2023
**来源**: `06/Yang 等 - 2011 - An aggregation method of permanent magnet synchronous generators wind farm model for electromagnetic.pdf`

## 摘要

An aggregation method to build the model of large-scale wind farm utilizing permanent magnet synchronous generators (PMSG), which is used in the electromagnetic transient analysis of the wind farm, is presented. A simplified transient model of PMSG-based wind farm is built and the simulation results from the simplified transient model and those from corresponding detailed electromagnetic transient simulation model are compared and verified. The response characteristics of PMSG unit under various power grid faults are analyzed; on this basis two kinds of wind farm simulation models, namely a detailed model of wind farm, which consists of forty PMSGs and the capacity of each PMSG is 5MW, and an equivalent aggregation model with the capacity of 200MW for the very wind farm, are built. The agg

## 核心贡献


- 提出基于功率等效原则的PMSG风电场聚合建模方法，适用于大规模电磁暂态仿真。
- 建立保留变流器d-q轴电流控制的PMSG简化模型，忽略机械动态以降低计算量。
- 推导集电网络与升压变压器等值参数计算方法，实现百兆瓦级风场快速等效建模。


## 使用的方法


- [[聚合等值方法|聚合等值方法]]
- [[简化电磁暂态建模|简化电磁暂态建模]]
- [[d-q坐标系pi控制|d-q坐标系PI控制]]
- [[π型等值电路|π型等值电路]]
- [[功率等效原则|功率等效原则]]


## 涉及的模型


- [[pmsg|PMSG]]
- [[全功率变流器|全功率变流器]]
- [[升压变压器|升压变压器]]
- [[集电线路|集电线路]]
- [[风电场详细模型|风电场详细模型]]
- [[风电场聚合模型|风电场聚合模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[模型聚合|模型聚合]]
- [[电网故障响应|电网故障响应]]
- [[电压跌落分析|电压跌落分析]]


## 主要发现


- 聚合模型与详细模型在电压跌落故障下的动态响应高度一致，验证了方法有效性。
- 升压变压器参数对聚合模型精度影响显著，必须在等值过程中予以保留和精确建模。
- 集电线路对百兆瓦级风场聚合模型仿真结果影响较小，在常规精度要求下可忽略不计。


