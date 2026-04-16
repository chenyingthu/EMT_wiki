---
title: "Improving numerical efficiency of frequency dependent transmission line models for EMT simulations"
type: source
authors: ['H.M.Jeewantha', 'De', 'Silva']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112328. doi:10.1016/j.epsr.2025.112328"
tags: ['frequency-dependent', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations-1.pdf"]
---

# Improving numerical efficiency of frequency dependent transmission line models for EMT simulations

**作者**: H.M.Jeewantha, De, Silva
**年份**: 2025
**来源**: `23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations-1.pdf`

## 摘要

Improving numerical efficiency of frequency dependent transmission line This paper compares two model order reduction techniques for frequency dependent transmission line models to enhance numerical performance for large cable or overhead line systems. The Modal Truncation and Balanced Truncation methods are applied to reduce the order of propagation matrix. The simulation examples involving underground cable systems are presented for comparison. Time domain simulation results with linear termi­

## 核心贡献


- 提出将模态截断与平衡截断算法应用于频变线路传播矩阵降阶提升仿真效率
- 首次将平衡截断法引入频变线路建模保证降阶模型稳定并提供先验误差界
- 设计迭代降阶流程保留关键模态极点有效降低递归卷积计算负担


## 使用的方法


- [[模型降阶|模型降阶]]
- [[模态截断|模态截断]]
- [[平衡截断|平衡截断]]
- [[矢量拟合|矢量拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[递归卷积|递归卷积]]


## 涉及的模型


- [[频变输电线路模型|频变输电线路模型]]
- [[通用线路模型|通用线路模型]]
- [[地下电缆|地下电缆]]
- [[多回电缆系统|多回电缆系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[模型降阶|模型降阶]]
- [[实时仿真|实时仿真]]
- [[数值效率优化|数值效率优化]]


## 主要发现


- 平衡截断法降阶后严格保证模型渐近稳定性且提供明确先验误差上界
- 模态截断法剔除小留数极点项显著降低传播矩阵阶数并缩短仿真耗时
- 两种方法在双回电缆算例中保持高精度有效缓解过拟合导致的无源性破坏


