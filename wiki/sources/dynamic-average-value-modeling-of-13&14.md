---
title: "Dynamic Average-Value Modeling of"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2014.2340870.pdf.pdf"]
---

# Dynamic Average-Value Modeling of

**作者**: 
**年份**: 2014
**来源**: `13&14/files/TPWRD.2014.2340870.pdf.pdf`

## 摘要

—High-voltage direct-current (HVDC) systems play an important role in modern energy grids, whereas efﬁcient and ac- curate models are often needed for system-level studies. Due to the inherent switching in HVDC converters, the detailed switch-level models are computationally expensive for the simulation of large-signal transients and hard to linearize for small-signal frequency-domain characterization. In this paper, a dynamic average-value model (AVM) of the ﬁrst CIGRE HVDC bench- mark system is developed in a state-variable-based simulator, such as Matlab/Simulink, and nodal-analysis-based electromag- netic transient program (EMTP), such as PSCAD/EMTDC. The 12-pulse converters in the HVDC system are modeled with a set of nonlinear algebraic functions that are extracted numerically. The r

## 核心贡献


- 提出基于参数化方法的HVDC动态平均值模型，消除开关细节提升系统级仿真效率
- 在状态变量与节点分析平台中实现十二脉冲换流器非线性代数函数数值提取与建模
- 构建连续型等效模型支持大信号暂态预测，并具备直接线性化用于频域分析的能力


## 使用的方法


- [[动态平均值建模|动态平均值建模]]
- [[参数化方法|参数化方法]]
- [[节点分析法|节点分析法]]
- [[状态变量法|状态变量法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[十二脉冲换流器|十二脉冲换流器]]
- [[换流变压器|换流变压器]]
- [[交流滤波器|交流滤波器]]
- [[直流输电线路|直流输电线路]]
- [[平波电抗器|平波电抗器]]
- [[弱交流电网|弱交流电网]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[大信号暂态分析|大信号暂态分析]]
- [[系统级仿真|系统级仿真]]
- [[动态等值|动态等值]]
- [[换流器控制|换流器控制]]


## 主要发现


- 平均值模型在大信号暂态下与详细开关模型波形高度吻合，验证了时域仿真精度
- 消除开关动作使计算步长显著增大，仿真速度提升数个数量级且大幅降低计算成本
- 模型为连续系统可直接用于小信号线性化分析，但无法捕捉换相失败等开关瞬态现象


