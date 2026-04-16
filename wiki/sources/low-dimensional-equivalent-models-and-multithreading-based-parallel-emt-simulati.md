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


- 提出基于半隐式混合积分的VSC与电网解耦方法，实现内外节点并行求解
- 推导适配不同直流连接方式的多VSC低维等效电路，降低节点导纳矩阵维度
- 设计基于OpenMP的多线程并行算法，克服传统节点消元法的高串行缺陷


## 使用的方法


- [[半隐式混合积分|半隐式混合积分]]
- [[节点消元法|节点消元法]]
- [[等效电路综合|等效电路综合]]
- [[多线程并行计算|多线程并行计算]]
- [[openmp框架|OpenMP框架]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[vsc-model|VSC]]
- [[光伏电源单元|光伏电源单元]]
- [[滤波器|滤波器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[等效建模|等效建模]]
- [[新能源并网|新能源并网]]
- [[仿真加速|仿真加速]]


## 主要发现


- 在百兆瓦光伏电站串行仿真中，解耦与低维模型实现超八十倍计算加速
- 并行模式下获得两至三倍二次加速，且关键电气量仿真精度几乎无损失


