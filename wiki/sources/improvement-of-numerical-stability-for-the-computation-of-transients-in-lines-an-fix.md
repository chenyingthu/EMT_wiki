---
title: "Improvement of Numerical Stability for the Computation of Transients in Lines and Cables"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables-1.pdf"]
---

# Improvement of Numerical Stability for the Computation of Transients in Lines and Cables

**作者**: 
**年份**: 2010
**来源**: `23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables-1.pdf`

## 摘要

—This paper discusses numerical stability problems of a frequency-dependent transmission-line and cable modeling ap- proach used for electromagnetic transient analysis. Time-domain numerical errors due to the discrete computation of convolution in- tegrals can be estimated in terms of transfer function parameters for a given line or cable model. Based on this estimation, a method- ology for the improvement of numerical stability is presented. The numerical advantages of the new method are supported by demon- strations and comparisons with existing models. The method pre- sented in this paper is applicable to power cables and transmission lines. Index Terms—Electromagnetic transients, Electromagnetic Transients Program (EMTP), ﬁtting, wideband line and cable

## 核心贡献


- 提出基于传递函数参数估计时域卷积误差的方法，明确数值稳定性边界
- 将相域辨识转化为约束线性最小二乘问题，通过限制留极点比消除失稳
- 改进宽频模型拟合流程，避免多延迟组叠加引发的异常高幅值响应


## 使用的方法


- [[部分分式展开|部分分式展开]]
- [[有理函数逼近|有理函数逼近]]
- [[约束线性最小二乘法|约束线性最小二乘法]]
- [[特征线法|特征线法]]
- [[状态空间法|状态空间法]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电力电缆|电力电缆]]
- [[通用线路模型|通用线路模型]]
- [[宽频模型|宽频模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性分析|数值稳定性分析]]
- [[频率相关建模|频率相关建模]]
- [[宽频线路建模|宽频线路建模]]
- [[时域卷积计算|时域卷积计算]]


## 主要发现


- 宽频模型中延迟组留极点比过高会导致时域仿真数值失稳，短电缆尤为显著
- 施加留极点比值约束后，新模型在保持频域拟合精度的同时彻底消除时域发散
- 约束拟合有效抑制多模态叠加的幅值放大效应，显著提升暂态仿真鲁棒性


