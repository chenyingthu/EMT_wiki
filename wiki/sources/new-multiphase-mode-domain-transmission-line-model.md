---
title: "New multiphase mode domain transmission line model"
type: source
authors: ['未知']
year: 1999
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/New multiphase mode domain transmission line model.pdf"]
---

# New multiphase mode domain transmission line model

**作者**: 
**年份**: 1999
**来源**: `27&28/New multiphase mode domain transmission line model.pdf`

## 摘要

This article presents a new model to represent transmission lines including the frequency dependence of longitudinal parameters. The model uses exact modes, for ideally transposed lines, and “quasi-modes” for non-transposed lines. The line is represented through a cascade of p-circuits, with one p-circuit for each mode. The transformation matrix used is real and it is modeled with ideal transformers. The model is described for three-phase lines, dc lines, double three-phase lines and six-phase lines. An ATP-EMTP implementation of a 440 kV three- phase transmission line is performed to illustrate the model and a comparison with two frequency dependent ATP line models are made, the Semlyen and JMarti ones. q 1999 Elsevier Science Ltd. All rights reserved. Keywords: Transmission line model; F

## 核心贡献


- 提出基于精确模与拟模的多相线路模型，有效表征纵向参数频变特性
- 采用实数且频不变的Clarke变换矩阵，通过理想变压器实现相模转换
- 构建各模态级联p型电路结构，支持三相至六相线路的时域仿真实现


## 使用的方法


- [[模域变换|模域变换]]
- [[clarke变换|Clarke变换]]
- [[p型电路级联|p型电路级联]]
- [[频变参数综合|频变参数综合]]
- [[理想变压器建模|理想变压器建模]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[三相线路|三相线路]]
- [[直流线路|直流线路]]
- [[双三相线路|双三相线路]]
- [[六相线路|六相线路]]
- [[p型等效电路|p型等效电路]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[模域分析|模域分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[线路合闸暂态|线路合闸暂态]]
- [[多相线路建模|多相线路建模]]


## 主要发现


- 拟模法对非换位线路近似精度高，误差小且满足多数工程暂态分析需求
- 440kV线路合闸与频扫验证表明，模型精度与Semlyen等经典模型相当
- 实数变换矩阵结合理想变压器实现，显著简化了频变线路的时域程序实现


