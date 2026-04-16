---
title: "Multi-scale formulation of admittance-based modeling of cables"
type: source
authors: ['Felipe Camara']
year: 2021
journal: "Electric Power Systems Research, 195 (2021) 107120. doi:10.1016/j.epsr.2021.107120"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-scale formulation of admittance-based modeling of cables.pdf"]
---

# Multi-scale formulation of admittance-based modeling of cables

**作者**: Felipe Camara
**年份**: 2021
**来源**: `27&28/Multi-scale formulation of admittance-based modeling of cables.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Multi-scale formulation of admittance-based modeling of cables Felipe Camara a, Antonio C.S. Lima *,b, Kai Strunz c a Furnas Centrais El´etricas, Dept. Electrical Studies and Operation Planning, RJ, Brazil b Federal University of Rio de Janeiro, COPPE/UFRJ, RJ, Brazil

## 核心贡献


- 提出基于节点导纳矩阵的多尺度电缆模型，摆脱特征线法对最小步长的限制
- 引入折叠线等效变换解决导纳矩阵有理拟合精度问题，提升宽频建模准确性
- 设计基于解析信号的变步长算法，实现电磁与机电暂态在同一环境下的平滑过渡


## 使用的方法


- [[节点导纳矩阵建模|节点导纳矩阵建模]]
- [[动态相量法|动态相量法]]
- [[频率自适应暂态仿真-fast|频率自适应暂态仿真(FAST)]]
- [[折叠线等效变换|折叠线等效变换]]
- [[变步长算法|变步长算法]]
- [[解析信号|解析信号]]


## 涉及的模型


- [[电缆|电缆]]
- [[输电线路|输电线路]]
- [[频变线路模型|频变线路模型]]
- [[节点导纳模型|节点导纳模型]]


## 相关主题


- [[多尺度仿真|多尺度仿真]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态联合仿真|机电暂态联合仿真]]
- [[变步长仿真|变步长仿真]]


## 主要发现


- 导纳模型无需步长小于最快模态行波时间，显著放宽了短电缆仿真步长限制
- 变步长算法在切换时波形平滑无畸变，整体计算速度显著提升且精度保持良好
- 基于解析信号的FAST框架成功实现电磁与机电暂态在同一数学模型下的统一求解


