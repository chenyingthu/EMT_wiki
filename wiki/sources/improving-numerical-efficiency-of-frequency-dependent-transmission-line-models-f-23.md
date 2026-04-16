---
title: "Improving numerical efficiency of frequency dependent transmission line models for EMT simulations"
type: source
authors: ['H.M.Jeewantha', 'De', 'Silva']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112328. doi:10.1016/j.epsr.2025.112328"
tags: ['frequency-dependent', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations.pdf"]
---

# Improving numerical efficiency of frequency dependent transmission line models for EMT simulations

**作者**: H.M.Jeewantha, De, Silva
**年份**: 2025
**来源**: `23/De Silva和Zhang - 2026 - Improving numerical efficiency of frequency dependent transmission line models for EMT simulations.pdf`

## 摘要

Improving numerical efficiency of frequency dependent transmission line This paper compares two model order reduction techniques for frequency dependent transmission line models to enhance numerical performance for large cable or overhead line systems. The Modal Truncation and Balanced Truncation methods are applied to reduce the order of propagation matrix. The simulation examples involving underground cable systems are presented for comparison. Time domain simulation results with linear termi­

## 核心贡献


- 提出将模态截断与平衡截断技术应用于频变线路传播矩阵降阶
- 设计基于残差极点比与汉克尔特征值的迭代筛选流程降低计算负担
- 验证平衡截断法在保障系统渐近稳定与提供先验误差界方面的优势


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[模态截断|模态截断]]
- [[平衡截断|平衡截断]]
- [[模型降阶|模型降阶]]
- [[有理函数逼近|有理函数逼近]]
- [[递归卷积|递归卷积]]


## 涉及的模型


- [[频变输电线路模型|频变输电线路模型]]
- [[通用线路模型|通用线路模型]]
- [[地下电缆|地下电缆]]
- [[多回路电缆系统|多回路电缆系统]]
- [[传播矩阵|传播矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[模型降阶|模型降阶]]
- [[实时仿真|实时仿真]]
- [[广域建模|广域建模]]
- [[数值效率优化|数值效率优化]]


## 主要发现


- 模态截断法直接应用效果不佳需结合残差极点比迭代筛选满足精度
- 平衡截断法能有效降低传播矩阵阶数同时严格保证降阶模型稳定性
- 降阶后的频变线路模型在多回路电缆时域仿真中显著提升计算效率


