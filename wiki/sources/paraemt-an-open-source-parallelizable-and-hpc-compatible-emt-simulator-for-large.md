---
title: "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Delivery;2024;39;2;10.1109/TPWRD.2023.3342715"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf"]
---

# ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids

**作者**: 
**年份**: 2024
**来源**: `30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation is an essential tool for studying power grids dominated by inverter-based resources (IBRs). However, due to small simulation time steps and increasing problem sizes, performing EMT simulations for large-scale power grids becomes computational-intensive, and of- ten impractical. To address this challenge, we developed ParaEMT, an open-source Python-based EMT simulator that is parallelizable and compatible with high-performance computing (HPC) systems for simulating large-scale power grids with a signiﬁcant presence of IBRs. Its key features include: 1) utilizing parallel computation for network solution by decomposing the network conductance matrix into the bordered block diagonal form; 2) enabling parallel updates of device states and network

## 核心贡献

- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[节点分析法|节点分析法]]
- [[并行计算|并行计算]]
- [[导纳矩阵加边块对角分解|导纳矩阵加边块对角分解]]
- [[历史电流并行更新|历史电流并行更新]]
- [[高性能计算-hpc-加速|高性能计算(HPC)加速]]

## 涉及的模型

- [[基于逆变器的资源-ibr|基于逆变器的资源(IBR)]]
- [[wecc-240节点系统|WECC 240节点系统]]
- [[10080节点合成系统|10080节点合成系统]]
- [[100-可再生能源电网|100%可再生能源电网]]

## 相关主题

- [[parallel-computing]]

## 主要发现

—The electromagnetic transient (EMT) simulation is an essential tool for studying power grids dominated by inverter-based resources (IBRs)
