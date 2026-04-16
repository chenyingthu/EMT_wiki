---
title: "Improvement of Numerical Stability for the Computation of Transients in Lines and Cables"
type: source
authors: ['Ilhan Kocar', 'Jean Mahseredjian', 'Guy Olivier']
year: 2010
journal: "IEEE Transactions on Power Delivery;2010;25;2;10.1109/TPWRD.2009.2037633"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables.pdf"]
---

# Improvement of Numerical Stability for the Computation of Transients in Lines and Cables

**作者**: Ilhan Kocar, Jean Mahseredjian, Guy Olivier
**年份**: 2010
**来源**: `23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables.pdf`

## 摘要

—This paper discusses numerical stability problems of a frequency-dependent transmission-line and cable modeling ap- proach used for electromagnetic transient analysis. Time-domain numerical errors due to the discrete computation of convolution in- tegrals can be estimated in terms of transfer function parameters for a given line or cable model. Based on this estimation, a method- ology for the improvement of numerical stability is presented. The numerical advantages of the new method are supported by demon- strations and comparisons with existing models. The method pre- sented in this paper is applicable to power cables and transmission lines. Index Terms—Electromagnetic transients, Electromagnetic Transients Program (EMTP), ﬁtting, wideband line and cable

## 核心贡献


- 提出留极点比值约束的频域拟合方法，有效抑制时域卷积积分的数值误差
- 将相域传递函数辨识转化为约束最小二乘问题，提升宽频线路模型时域稳定性
- 建立时域离散误差与传递函数参数的定量关系，为模型稳定性提供理论依据


## 使用的方法


- [[部分分式展开|部分分式展开]]
- [[约束线性最小二乘法|约束线性最小二乘法]]
- [[特征线法|特征线法]]
- [[有理函数拟合|有理函数拟合]]
- [[卷积积分递归计算|卷积积分递归计算]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电力电缆|电力电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[宽频线路模型-wb|宽频线路模型(WB)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变线路建模|频变线路建模]]
- [[数值稳定性分析|数值稳定性分析]]
- [[宽频电缆模型|宽频电缆模型]]
- [[传递函数拟合|传递函数拟合]]


## 主要发现


- 宽频模型中延迟组留极点比过高会导致时域数值失稳，短电缆仿真中尤为显著
- 引入留极点比值约束后，新模型在保持频域拟合精度的同时彻底消除时域数值振荡
- 时域离散误差可通过传递函数参数精确预估，约束优化使误差严格控制在安全边界内


