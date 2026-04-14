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

- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[异构计算|异构计算]]
- [[emt-ts联合仿真|EMT-TS联合仿真]]
- [[gpu多流多线程并行|GPU多流多线程并行]]
- [[异步串行-并行处理|异步串行-并行处理]]
- [[多速率仿真|多速率仿真]]
- [[设备级电磁暂态仿真|设备级电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]

## 涉及的模型

- [[电池储能系统-bess|电池储能系统(BESS)]]
- [[交直流电网|交直流电网]]
- [[ieee-118节点系统|IEEE 118节点系统]]
- [[电力电子装置|电力电子装置]]

## 相关主题

- [[parallel-computing]]

## 主要发现

—Extensive integration of power electronics appara- tuses complicates the modern power grid and consequently necessi- tates time-domain transients study for its planning and operation
