---
title: "Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients"
type: source
authors: ['未知']
year: 2019
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Abusalah 等 - 2020 - Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients.pdf"]
---

# Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients

**作者**: 
**年份**: 2019
**来源**: `05/Abusalah 等 - 2020 - Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients.pdf`

## 摘要

This paper is related to research on parallelization methods for the simulation of electro- magnetic transients (EMTs). It presents an automatic parallelization approach based on the solution of sparse matrices resulting from the formulation of network equations. Modiﬁed-augmented-nodal analysis is used to formulate network equations. The selected sparse matrix solver is parallelized and adapted to improve performance by pivot validity testing and partial refactorization. Refactorization is needed when dealing with varying topology networks and nonlinear models. The EMT solver employs a fully iterative method for nonlinear functions. Conventional computer CPU-based parallelization is achieved and does not require any user intervention for given arbitrary network topologies. The presented a

## 核心贡献


- 提出基于KLU的自动并行方法，利用块三角分解实现任意拓扑网络无干预并行计算
- 引入主元检验与部分重分解技术，显著降低变拓扑与非线性迭代时的矩阵更新耗时
- 实现多线程分布式内存架构，无缝衔接潮流计算与时域电磁暂态全迭代求解


## 使用的方法


- [[修正增广节点分析法|修正增广节点分析法]]
- [[块三角分解|块三角分解]]
- [[klu稀疏矩阵求解|KLU稀疏矩阵求解]]
- [[部分重分解|部分重分解]]
- [[主元有效性检验|主元有效性检验]]
- [[全迭代牛顿法|全迭代牛顿法]]
- [[cpu多线程并行|CPU多线程并行]]


## 涉及的模型


- [[非线性模型|非线性模型]]
- [[时变开关模型|时变开关模型]]
- [[变压器分接头模型|变压器分接头模型]]
- [[电力电子换流器|电力电子换流器]]
- [[风电机组模型|风电机组模型]]
- [[分布参数输电线路|分布参数输电线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[自动网络分解|自动网络分解]]
- [[离线仿真加速|离线仿真加速]]
- [[非线性迭代求解|非线性迭代求解]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 所提算法在含电力电子与风电的大规模真实电网中显著缩短电磁暂态仿真时间
- 部分重分解策略有效减少非线性迭代过程中的完整矩阵分解次数，提升计算效率
- 自动块三角分解成功识别分布参数线路解耦子网，实现多核CPU负载均衡加速


