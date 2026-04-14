---
title: "A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2978128"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Zhang 等 - 2021 - A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation.pdf"]
---

# A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation

**作者**: 
**年份**: 2020
**来源**: `01/Zhang 等 - 2021 - A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation.pdf`

## 摘要

—In electromagnetic transient (EMT) simulation, 80- 97% of the computational time is devoted to solving the network equations. A key observation is that the sub-matrix representing the interaction between two far-away groups of buses is usually sparse and can be approximated by a low-rank matrix. Based on this observation, we propose a novel low-rank approximation method which permits O(N log N)-time matrix-vector multi- plication for each network solution time step. Comprehensive numerical studies are conducted on a 39-bus system and a 179- bus system from the literature, and large cases created from the two systems. The results demonstrate that the proposed approach is up to 2.8× faster than the state-of-the-art sparse LU factorization based network solution, without compromising simulat

## 核心贡献

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[分层低秩近似|分层低秩近似]]
- [[图划分|图划分]]
- [[稀疏lu分解|稀疏LU分解]]
- [[并行计算|并行计算]]
- [[分层低秩近似|分层低秩近似]]
- [[稀疏lu分解|稀疏LU分解]]
- [[图划分|图划分]]
- [[矩阵向量乘法|矩阵向量乘法]]

## 涉及的模型

- [[电力系统网络模型|电力系统网络模型]]
- [[39节点系统|39节点系统]]
- [[179节点系统|179节点系统]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络求解|网络求解]]
- [[并行计算|并行计算]]
- [[大规模系统仿真|大规模系统仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络求解|网络求解]]
- [[并行计算|并行计算]]
- [[大规模系统仿真|大规模系统仿真]]

## 主要发现

—In electromagnetic transient (EMT) simulation, 80- 97% of the computational time is devoted to solving the network equations
