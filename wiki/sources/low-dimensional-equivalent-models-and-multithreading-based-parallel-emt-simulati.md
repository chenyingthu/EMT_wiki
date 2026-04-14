---
title: "Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-Converter Systems"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Energy Conversion;2025;40;1;10.1109/TEC.2024.3422080"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Xu 等 - 2025 - Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-.pdf"]
---

# Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-Converter Systems

**作者**: 
**年份**: 2025
**来源**: `25/Xu 等 - 2025 - Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-.pdf`

## 摘要

—As the proportion of renewable energy generation in the grid increases, the number of voltage source converters (VSCs) has grown signiﬁcantly. It is therefore of great importance to study the multi-VSC systems using electromagnetic transient (EMT) simulation. This paper presents a novel approach to modeling multi-VSC circuits, comprising EMT low-dimensional equivalent models and a multithreading-based parallel simulation method. The decoupling between the VSC from the AC grid is initially achieved through the adoption of semi-implicit hybrid integration. This is followed by the synthesis of the equivalent circuit for each phase,whichresultsinthederivationoflow-dimensionalequivalent models of multi-VSC circuits. In addition, a parallel simulation algorithm for the VSC is proposed, which en

## 核心贡献

- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[半隐式混合积分法|半隐式混合积分法]]
- [[等效电路综合|等效电路综合]]
- [[低维等效建模|低维等效建模]]
- [[多线程并行仿真|多线程并行仿真]]
- [[openmp并行计算框架|OpenMP并行计算框架]]
- [[交直流解耦技术|交直流解耦技术]]

## 涉及的模型

- [[vsc-model|VSC]]
- [[多换流器系统|多换流器系统]]
- [[光伏电源单元-pvpu|光伏电源单元(PVPU)]]
- [[光伏电站|光伏电站]]
- [[背靠背柔性直流输电系统|背靠背柔性直流输电系统]]
- [[交流电网|交流电网]]

## 相关主题

- [[parallel-computing]]

## 主要发现

—As the proportion of renewable energy generation in the grid increases, the number of voltage source converters (VSCs) has grown signiﬁcantly
