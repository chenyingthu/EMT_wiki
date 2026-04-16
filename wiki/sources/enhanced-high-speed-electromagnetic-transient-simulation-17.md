---
title: "Enhanced high-speed electromagnetic transient simulation"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Xu 等 - 2016 - Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid.pdf"]
---

# Enhanced high-speed electromagnetic transient simulation

**作者**: 
**年份**: 2016
**来源**: `17/Xu 等 - 2016 - Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid.pdf`

## 摘要

Enhanced high-speed electromagnetic transient simulation Jianzhong Xu a,⇑, Hui Ding b, Shengtao Fan b, Aniruddha M. Gole b, Chengyong Zhao a a The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Manitoba, Canada This paper introduces a very fast electromagnetic transient (EMT) simulation model for the HVdc

## 核心贡献


- 提出基于后向欧拉法与理想开关零电导假设的MMC伴随模型，大幅简化等效电路计算
- 将高效排序算法嵌入戴维南等效电路，实现电容电压平衡的线性复杂度计算
- 构建保留子模块身份的高速MMC模型，计算速度逼近平均值模型且精度无损


## 使用的方法


- [[后向欧拉法|后向欧拉法]]
- [[戴维南等效|戴维南等效]]
- [[伴随模型|伴随模型]]
- [[理想开关模型|理想开关模型]]
- [[最近电平控制|最近电平控制]]
- [[电容电压平衡排序算法|电容电压平衡排序算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[子模块|子模块]]
- [[igbt半桥|IGBT半桥]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高速仿真|高速仿真]]
- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[电容电压平衡|电容电压平衡]]
- [[计算加速|计算加速]]


## 主要发现


- 相比传统详细模型，所提方法计算速度提升一至两个数量级，且仿真精度几乎无损失
- 结合高效排序算法后，系统规模增大时计算耗时呈线性增长，实现O(N)加速
- 模型在保留子模块独立电气特征的同时，计算效率可媲美高度简化的平均值模型


