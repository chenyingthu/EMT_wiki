---
title: "Electromagnetic disturbances in gas-insulated substations and VFT calculations"
type: source
authors: ['Akihiro Ametani']
year: 2018
journal: "Electric Power Systems Research, 160 (2018) 191-198. doi:10.1016/j.epsr.2018.02.014"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic disturbances in gas-insulated substations and VFT calculations_Ametani 等_2018.pdf"]
---

# Electromagnetic disturbances in gas-insulated substations and VFT calculations

**作者**: Akihiro Ametani
**年份**: 2018
**来源**: `15/Electromagnetic disturbances in gas-insulated substations and VFT calculations_Ametani 等_2018.pdf`

## 摘要

1. Introduction This paper is focused on VFTs from the viewpoint of electro- magnetic disturbances (EMDs). In Section 2, the voltage amplitudes It is well-known that lightning strikes to a transmission tower and oscillating frequencies of the VFTs are summarized based nearby a substation and swit...

## 核心贡献

- 系统总结了GIS中隔离开关和断路器操作产生的VFT幅值与振荡频率的现场与实验室测试数据
- 详细阐述了基于EMT类软件的GIS元件VFT仿真建模方法
- 对比验证了EMTP与FDTD两种数值计算方法在VFT仿真中的一致性

## 使用的方法

- [[emt型软件仿真-如emtp|EMT型软件仿真（如EMTP）]]
- [[时域有限差分法-fdtd|时域有限差分法（FDTD）]]
- [[传输线-tl-建模方法|传输线（TL）建模方法]]
- [[现场与实验室测试数据分析|现场与实验室测试数据分析]]

## 涉及的模型

- [[气体绝缘开关设备-gis|气体绝缘开关设备（GIS）]]
- [[隔离开关-ds-与断路器-cb|隔离开关（DS）与断路器（CB）]]
- [[高压主电路模型|高压主电路模型]]
- [[低压控制电路模型|低压控制电路模型]]
- [[金属外壳模型|金属外壳模型]]

## 相关主题

- [[极快速瞬态-vft-vfto|极快速瞬态（VFT/VFTO）]]
- [[电磁扰动-emd|电磁扰动（EMD）]]
- [[高频暂态分析|高频暂态分析]]
- [[gis电磁暂态仿真|GIS电磁暂态仿真]]
- [[数值计算方法对比|数值计算方法对比]]

## 主要发现

- GIS高压主电路与低压控制电路中的VFT振荡频率无显著差异
- 在采用合理建模方法的前提下，EMTP与FDTD的仿真结果具有良好的一致性
