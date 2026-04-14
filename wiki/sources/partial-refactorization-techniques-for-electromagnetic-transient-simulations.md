---
title: "Partial Refactorization Techniques for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;4;10.1109/TPWRD.2025.3574482"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/Bruned 等 - 2025 - Partial Refactorization Techniques for Electromagnetic Transient Simulations.pdf"]
---

# Partial Refactorization Techniques for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2025
**来源**: `31/Bruned 等 - 2025 - Partial Refactorization Techniques for Electromagnetic Transient Simulations.pdf`

## 摘要

—This paper explores partial refactorization techniques to accelerate the simulation of Electromagnetic Transients (EMTs) in power systems. Direct sparse left-looking LU factorization from the KLU solver is used to solve network equations. The refactoriza- tionstepcanbetime-consumingifthefactorizedmatrixvariesoften as the simulation involves power electronics switching or nonlinear devices. A path-based partial refactorization technique is proposed to accelerate the re-computation of LU factors. In the left-looking algorithm, only a subset of columns that belong to the computed factorization path are refactorized. In addition, Block Triangular Factorization (BTF) is enhanced through partial refactorization, which further accelerates computation through smaller, evolving submatrices. The ne

## 核心贡献

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[直接稀疏左视lu分解|直接稀疏左视LU分解]]
- [[klu求解器|KLU求解器]]
- [[基于路径的部分重分解技术|基于路径的部分重分解技术]]
- [[块三角分解-btf|块三角分解(BTF)]]
- [[gilbert-peierls分解算法|Gilbert-Peierls分解算法]]

## 涉及的模型

- [[电力电子开关|电力电子开关]]
- [[非线性设备|非线性设备]]
- [[电网网络模型|电网网络模型]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真加速|仿真加速]]
- [[稀疏线性方程组求解|稀疏线性方程组求解]]
- [[矩阵重分解优化|矩阵重分解优化]]

## 主要发现

—This paper explores partial refactorization techniques to accelerate the simulation of Electromagnetic Transients (EMTs) in power systems
