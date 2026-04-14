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

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[稀疏矩阵求解器-klu|稀疏矩阵求解器(KLU)]]
- [[自动并行化方法|自动并行化方法]]
- [[主元有效性测试与部分重分解|主元有效性测试与部分重分解]]
- [[非线性全迭代法|非线性全迭代法]]

## 涉及的模型

- [[电力电子变流器|电力电子变流器]]
- [[风力发电机|风力发电机]]
- [[非线性模型|非线性模型]]
- [[变拓扑网络|变拓扑网络]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[稀疏矩阵加速计算|稀疏矩阵加速计算]]
- [[自动并行化|自动并行化]]

## 主要发现

This paper is related to research on parallelization methods for the simulation of electro- magnetic transients (EMTs)
