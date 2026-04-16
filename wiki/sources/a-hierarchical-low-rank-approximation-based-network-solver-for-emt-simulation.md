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


- 提出分层低秩近似算法求解网络方程，将单步计算复杂度降至O(N log N)。
- 建立算法的时间复杂度、内存占用与近似误差理论分析框架。
- 验证算法在保持精度的前提下，较稀疏LU分解求解器提速最高达2.8倍。


## 使用的方法


- [[分层低秩近似|分层低秩近似]]
- [[奇异值分解-svd|奇异值分解(SVD)]]
- [[快速矩阵向量乘法|快速矩阵向量乘法]]
- [[图划分网络分区|图划分网络分区]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[输电线路-π型等效|输电线路(π型等效)]]
- [[变压器-饱和模型|变压器(饱和模型)]]
- [[发电机-brandwajn模型|发电机(Brandwajn模型)]]
- [[负荷-恒定阻抗模型|负荷(恒定阻抗模型)]]
- [[网络导纳矩阵|网络导纳矩阵]]


## 相关主题


- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[网络方程求解|网络方程求解]]
- [[并行计算|并行计算]]
- [[大规模电力系统仿真|大规模电力系统仿真]]
- [[矩阵运算优化|矩阵运算优化]]


## 主要发现


- 在39节点与179节点系统中验证，求解速度较稀疏LU分解最高提升2.8倍。
- 仿真电压波形与商业软件EMTP-RV结果高度一致，未牺牲计算精度。
- 算法具备高度并行化特性，为后续多核或GPU硬件加速提供显著优化空间。


