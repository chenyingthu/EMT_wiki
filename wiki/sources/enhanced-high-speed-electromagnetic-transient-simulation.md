---
title: "Enhanced high-speed electromagnetic transient simulation"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Xu 等 - 2016 - Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid-1.pdf"]
---

# Enhanced high-speed electromagnetic transient simulation

**作者**: 
**年份**: 2016
**来源**: `17/Xu 等 - 2016 - Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid-1.pdf`

## 摘要

Enhanced high-speed electromagnetic transient simulation Jianzhong Xu a,⇑, Hui Ding b, Shengtao Fan b, Aniruddha M. Gole b, Chengyong Zhao a a The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Manitoba, Canada This paper introduces a very fast electromagnetic transient (EMT) simulation model for the HVdc

## 核心贡献


- 提出基于后向欧拉法与理想开关零电导假设的MMC等效模型，大幅简化伴随电路计算
- 将高效排序算法嵌入戴维南等效电路，实现最近电平控制下电容电压平衡的线性计算
- 保持子模块个体身份的同时实现与平均值模型相当的仿真速度，适用于多端直流电网


## 使用的方法


- [[后向欧拉法|后向欧拉法]]
- [[戴维南等效|戴维南等效]]
- [[伴随电路模型|伴随电路模型]]
- [[理想开关模型|理想开关模型]]
- [[最近电平控制|最近电平控制]]
- [[高效排序算法|高效排序算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[半桥子模块|半桥子模块]]
- [[直流输电系统|直流输电系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高速仿真|高速仿真]]
- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[电容电压平衡|电容电压平衡]]


## 主要发现


- 相比传统详细模型新方法计算速度提升一至两个数量级，且仿真精度损失可忽略不计
- 结合最近电平控制与排序算法，仿真计算复杂度随系统规模呈线性增长，实现O(N)加速
- 模型在保持子模块独立电气特性的同时，仿真效率达到简化平均值模型水平


