---
title: "Fast electromagnetic transient simulation of modular multilevel converter based on semi-implicit delay model"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Fan 等 - 2017 - Fast electromagnetic transient simulation for flexible DC Power Grid.pdf"]
---

# Fast electromagnetic transient simulation of modular multilevel converter based on semi-implicit delay model

**作者**: CNKI
**年份**: 2023
**来源**: `18/Fan 等 - 2017 - Fast electromagnetic transient simulation for flexible DC Power Grid.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了一种基于电容能量均分思想的MMC能量均分模型(EEM)，简化了子模块均压策略并准确保留桥臂闭锁与不闭锁时的外特性
- 针对级联全桥型直流断路器，提出了一种支路子模块串等值电路简化方法及快速仿真模型
- 在PSCAD/EMTDC平台中搭建并验证了所提模型，证明了其在大规模柔性直流电网仿真中的准确性与快速性

## 使用的方法

- [[电容能量均分思想|电容能量均分思想]]
- [[子模块串等值电路简化方法|子模块串等值电路简化方法]]
- [[电磁暂态仿真建模-pscad-emtdc|电磁暂态仿真建模(PSCAD/EMTDC)]]
- [[模型对比验证|模型对比验证]]

## 涉及的模型

- [[mmc详细模型-dm|MMC详细模型(DM)]]
- [[mmc详细等价模型-dem|MMC详细等价模型(DEM)]]
- [[mmc能量均分模型-eem|MMC能量均分模型(EEM)]]
- [[级联全桥型直流断路器详细模型|级联全桥型直流断路器详细模型]]
- [[直流断路器快速仿真模型|直流断路器快速仿真模型]]

## 相关主题

- [[柔性直流电网|柔性直流电网]]
- [[电磁暂态仿真-emt|电磁暂态仿真(EMT)]]
- [[模块化多电平换流器-mmc|模块化多电平换流器(MMC)]]
- [[直流断路器|直流断路器]]
- [[快速仿真与模型降阶|快速仿真与模型降阶]]
- [[电力系统仿真|电力系统仿真]]

## 主要发现

- 所提能量均分模型与断路器快速模型在保持高仿真精度的同时显著提升了计算效率
- 能量均分模型能够有效简化均压控制逻辑，且准确反映桥臂在正常与闭锁状态下的外部电气特性
- 快速仿真模型可有效解决含多换流站与断路器的大规模直流电网电磁暂态仿真速度缓慢的问题
