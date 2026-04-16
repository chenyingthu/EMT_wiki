---
title: "混合型MMC全状态高效电磁暂态仿真方法研究"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/连攀杰 等 - 2021 - 混合型MMC全状态高效电磁暂态仿真方法研究.pdf"]
---

# 混合型MMC全状态高效电磁暂态仿真方法研究

**作者**: CNKI
**年份**: 2022
**来源**: `33/连攀杰 等 - 2021 - 混合型MMC全状态高效电磁暂态仿真方法研究.pdf`

## 摘要

The hybrid modular multilevel converter (MMC), which composed of half-bridge sub-modules and full-bridge sub-modules, takes into account the DC fault ride-through capability and economy, with broad engineering application prospects. For the problems of complex equivalent, multiple internal nodes and low computational efficiency in the electromagnetic transient simulation model of the hybrid MMC, this paper analyzed the working state of the hybrid MMC in the unlocked and locked modes, and proposed a “efficient electromagnetic transient simulation method for hybrid MMC

## 核心贡献



- 提出混合型MMC闭锁模式的高效等效仿真方法
- 提出改进的灵活堆排序电容电压排序算法以提升解锁模式仿真效率

## 使用的方法


- [[nodal-analysis]]
- [[numerical-integration]]
- [[network-equivalent]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-model]]

## 相关主题


- [[mmc]]
- [[hvdc]]
- [[real-time]]

## 主要发现



- 闭锁等效方法有效减少了模型内部节点数量，显著提升了闭锁状态下的仿真计算效率
- 灵活堆排序算法优化了电容电压排序过程，在保证模型精度的同时大幅提高了解锁状态下的仿真速度