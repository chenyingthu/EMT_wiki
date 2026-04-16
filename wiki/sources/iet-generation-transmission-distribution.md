---
title: "IET Generation, Transmission & Distribution"
type: source
authors: ['未知']
year: 2020
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Ye 等 - 2020 - Large step size electromagnetic transient simulations by matrix transformation-based shifted-frequen.pdf"]
---

# IET Generation, Transmission & Distribution

**作者**: 
**年份**: 2020
**来源**: `25/Ye 等 - 2020 - Large step size electromagnetic transient simulations by matrix transformation-based shifted-frequen.pdf`

## 摘要

To evaluate and improve the performances of control and protection strategies for large-scale AC grids, simulation models that can adopt a much larger time-step, provide instantaneous and wide frequency-band phasor values simultaneously are desirable. However, the traditional electromagnetic transient (EMT) model is numerically expensive and the transient stability (TS) model only preserves low-frequency dynamics. To resolve these issues, the shifted frequency phasor (SFP) modelling is generalised based on specific matrix transformations and SFP models of typical components in large-scale AC grids are derived hereafter. Unlike traditional models, the SFP models can produce instantaneous and wide frequency-band phasor waveforms simultaneously, while the latter matches the envelopes of the f

## 核心贡献


- 提出基于矩阵变换的移频相量建模方法，统一推导大规模交流电网典型元件模型
- 实现瞬时值与宽频带相量同步输出，相量包络与瞬时值精确匹配，突破传统局限
- 支持采用更大仿真步长，显著降低大规模交流电网电磁暂态仿真的计算负担


## 使用的方法


- [[移频相量法-sfp|移频相量法(SFP)]]
- [[矩阵变换法|矩阵变换法]]
- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]


## 涉及的模型


- [[同步发电机|同步发电机]]
- [[输电线路|输电线路]]
- [[大规模交流电网|大规模交流电网]]
- [[传统emt模型|传统EMT模型]]
- [[暂态稳定模型|暂态稳定模型]]


## 相关主题


- [[大时间步长仿真|大时间步长仿真]]
- [[宽频带动态分析|宽频带动态分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[移频分析|移频分析]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 在2232节点实际电网中验证，SFP模型在保证精度的同时显著提升仿真效率
- 宽频带相量可精确捕捉高低频动态，其包络与瞬时值完全吻合，传统TS模型误差大
- 采用更大仿真步长后计算负担大幅降低，有效解决传统EMT模型计算耗时问题


