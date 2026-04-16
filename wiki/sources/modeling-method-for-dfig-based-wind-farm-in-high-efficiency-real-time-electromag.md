---
title: "Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromagnetic Transient (EMT) Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Electronics;2025;40;9;10.1109/TPEL.2025.3567136"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/26/Liu 等 - 2025 - Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromagnetic Transient (EMT.pdf"]
---

# Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromagnetic Transient (EMT) Simulations

**作者**: 
**年份**: 2025
**来源**: `26/Liu 等 - 2025 - Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromagnetic Transient (EMT.pdf`

## 摘要

—With the increasing integration of renewable energy into power systems, electromagnetic transient simulation has be- comeindispensableforaccuratesystemanalysis.However,thecom- plexity of wind turbine modeling, characterized by a large number of electrical nodes, poses signiﬁcant challenges and necessitates substantial real-time simulation hardware. Existing methods for reducing circuit complexity improve simulation efﬁciency, but are each associated with inherent limitations. Aggregation methods sacriﬁce considerable internal station information, while existing decoupling techniques are constrained by speciﬁc requirements. This article proposes a real-time simulation model for a doubly fed induction generator-based wind farm (WF) using latency de- coupling and a multilevel nested fast and

## 核心贡献


- 提出基于离散化与延迟解耦的DFIG节点模型，实现定转子独立接口连接
- 将风机核心设备解耦为四部分，实现子网络独立求解，大幅降低矩阵维度
- 提出多级嵌套快速同步求解法，以多次低阶求解替代高阶求解，有效缩减节点


## 使用的方法


- [[延迟解耦法|延迟解耦法]]
- [[多级嵌套快速同步求解-m-nfss|多级嵌套快速同步求解(M-NFSS)]]
- [[节点分析法|节点分析法]]
- [[开关函数模型|开关函数模型]]
- [[离散化建模|离散化建模]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[风力发电机|风力发电机]]
- [[背靠背变流器|背靠背变流器]]
- [[变压器|变压器]]
- [[滤波器|滤波器]]
- [[风电场|风电场]]


## 相关主题


- [[实时电磁暂态仿真|实时电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[电路复杂度降低|电路复杂度降低]]
- [[硬件资源优化|硬件资源优化]]
- [[阻抗特性分析|阻抗特性分析]]


## 主要发现


- 模型仅需传统详细模型33.3%的硬件资源，显著降低实时仿真算力需求
- 风机对外接口节点由24个降至3个，保留内部细节的同时大幅提升求解效率
- RTDS验证表明模型阻抗特性与时域波形精度高，满足大规模风电场仿真要求


