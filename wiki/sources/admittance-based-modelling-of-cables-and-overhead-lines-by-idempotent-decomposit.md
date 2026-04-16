---
title: "Admittance-based modelling of cables and overhead lines by idempotent decomposition"
type: source
authors: ['Felipe Camara']
year: 2023
journal: "Electric Power Systems Research, 224 (2023) 109596. doi:10.1016/j.epsr.2023.109596"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Camara 等 - 2023 - Admittance-based modelling of cables and overhead lines by idempotent decomposition.pdf"]
---

# Admittance-based modelling of cables and overhead lines by idempotent decomposition

**作者**: Felipe Camara
**年份**: 2023
**来源**: `06/Camara 等 - 2023 - Admittance-based modelling of cables and overhead lines by idempotent decomposition.pdf`

## 摘要

Admittance-based modelling of cables and overhead lines by idempotent Felipe Camara a,∗, Antonio C.S. Lima b, Maria Teresa Correia de Barros c, Filipe Faria da Silva a, This paper presents a new modelling approach based on idempotent decomposition of the nodal admittance matrix for representation of cables and overhead lines (OHL). By subjecting the idempotent matrices rather than the nodal admittance matrix to rational fitting, the poor observability of the smallest eigenvalues in the

## 核心贡献


- 提出基于节点导纳矩阵幂等分解的线路建模方法，避免传统模态变换带来的耦合问题
- 对幂等矩阵进行矢量拟合，有效克服低频段最小特征值可观测性差的数值难题
- 构建全耦合相域导纳模型，保留频率相关性，适用于长短线路且无需极小仿真步长


## 使用的方法


- [[幂等分解|幂等分解]]
- [[节点导纳矩阵建模|节点导纳矩阵建模]]
- [[矢量拟合|矢量拟合]]
- [[有理逼近|有理逼近]]
- [[相域建模|相域建模]]


## 涉及的模型


- [[电缆|电缆]]
- [[架空输电线路|架空输电线路]]
- [[节点导纳矩阵模型|节点导纳矩阵模型]]
- [[全耦合相域模型|全耦合相域模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[宽带线路建模|宽带线路建模]]
- [[多尺度仿真|多尺度仿真]]


## 主要发现


- 幂等分解拟合显著提升低频小特征值辨识精度，彻底解决直接拟合导致的数值不稳定
- 全耦合相域模型统一处理长短线路，验证了避免极小时间步长下的仿真准确性
- 对比标准时域仿真表明，该模型在保留参数频率依赖性的同时具备高精度与计算效率


