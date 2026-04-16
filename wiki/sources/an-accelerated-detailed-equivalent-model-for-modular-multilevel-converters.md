---
title: "An accelerated detailed equivalent model for modular multilevel converters"
type: source
authors: ['Ramin Parvari']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109648. doi:10.1016/j.epsr.2023.109648"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/06/Parvari 等 - 2023 - An accelerated detailed equivalent model for modular multilevel converters.pdf"]
---

# An accelerated detailed equivalent model for modular multilevel converters

**作者**: Ramin Parvari
**年份**: 2023
**来源**: `06/Parvari 等 - 2023 - An accelerated detailed equivalent model for modular multilevel converters.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. An accelerated detailed equivalent model for modular multilevel converters✩ Ramin Parvari a, Shaahin Filizadeh a,∗, Dharshana Muthumuni b a University of Manitoba, Winnipeg, MB R3T 5V6, Canada b Manitoba Hydro International, Winnipeg, MB R3P 1A3, Canada

## 核心贡献


- 提出恒定导纳矩阵策略，仅在闭锁时重求逆，消除正常运行时的频繁矩阵更新
- 构建兼容半桥与全桥子模块的加速详细等效模型，实现正常与故障工况高精度仿真


## 使用的方法


- [[戴维南等效电路|戴维南等效电路]]
- [[梯形积分法|梯形积分法]]
- [[节点导纳矩阵优化|节点导纳矩阵优化]]
- [[电磁暂态离散化|电磁暂态离散化]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块-hbsm|半桥子模块(HBSM)]]
- [[全桥子模块-fbsm|全桥子模块(FBSM)]]
- [[详细等效模型-dem|详细等效模型(DEM)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[mmc-model|MMC]]
- [[计算加速|计算加速]]
- [[直流故障闭锁|直流故障闭锁]]
- [[vsc-hvdc|VSC-HVDC]]


## 主要发现


- 半桥与全桥MMC模型仿真速度较传统DEM分别提升30%与60%，显著降低计算负担
- 模型在正常运行与直流故障闭锁工况下均保持与详细开关模型一致的电压电流精度


