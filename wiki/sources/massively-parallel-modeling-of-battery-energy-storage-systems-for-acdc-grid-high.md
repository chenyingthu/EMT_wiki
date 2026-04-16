---
title: "Massively Parallel Modeling of Battery Energy Storage Systems for AC/DC Grid High-Performance Transient Simulation"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;3;10.1109/TPWRS.2022.3196286"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Lin 等 - 2023 - Massively Parallel Modeling of Battery Energy Storage Systems for ACDC Grid High-Performance Transi.pdf"]
---

# Massively Parallel Modeling of Battery Energy Storage Systems for AC/DC Grid High-Performance Transient Simulation

**作者**: 
**年份**: 2023
**来源**: `25/Lin 等 - 2023 - Massively Parallel Modeling of Battery Energy Storage Systems for ACDC Grid High-Performance Transi.pdf`

## 摘要

—Extensive integration of power electronics appara- tuses complicates the modern power grid and consequently necessi- tates time-domain transients study for its planning and operation. In this work, a heterogeneous computing architecture utilizing the CPU and graphics processing unit (GPU) is proposed for the efﬁcient study of interactions between a power grid network and massive utility-scale battery energy storage systems (BESSs). The device-level electromagnetic transient (EMT) simulation aiming at enhanced ﬁdelity of the BESS is conducted simultaneously with electro-mechanical transient stability (TS) simulation which suf- ﬁces system-level dynamic security assessment. Since the reser- vation of a large amount of energy storage units is computation- ally intensive for the CPU, the conc

## 核心贡献


- 提出CPU-GPU异构架构实现EMT-TS联合仿真，兼顾设备级高精度与系统级动态评估
- 构建向量化电池与TLL变流器模型，将储能异构性转为同构性以实现GPU细粒度并行
- 引入多流异步处理与多速率机制，优化异构资源调度与跨步长数据交互效率


## 使用的方法


- [[emt-ts联合仿真|EMT-TS联合仿真]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]
- [[多速率仿真|多速率仿真]]
- [[多流异步处理|多流异步处理]]
- [[向量化建模|向量化建模]]
- [[传输线链接-tll-模型|传输线链接(TLL)模型]]
- [[状态空间法|状态空间法]]
- [[后向欧拉离散|后向欧拉离散]]


## 涉及的模型


- [[电池储能系统-bess|电池储能系统(BESS)]]
- [[电力电子变流器|电力电子变流器]]
- [[戴维南等效电池模型|戴维南等效电池模型]]
- [[交直流电网|交直流电网]]
- [[ieee-118节点系统|IEEE 118节点系统]]


## 相关主题


- [[高性能计算|高性能计算]]
- [[并行计算|并行计算]]
- [[混合仿真|混合仿真]]
- [[电磁暂态|电磁暂态]]
- [[暂态稳定|暂态稳定]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 异构架构在含大规模储能的IEEE 118节点系统中实现超200倍仿真加速
- 设备级精度经MATLAB/Simulink验证，系统级精度经DSATools验证
- 多速率与向量化模型有效降低计算负担，保障跨时间尺度数据交互实时性


