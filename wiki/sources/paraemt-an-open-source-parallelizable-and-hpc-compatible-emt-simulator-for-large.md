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


- 提出基于加边块对角矩阵分解的网络导纳矩阵并行求解算法
- 实现设备状态变量与网络历史电流的解耦并行更新机制
- 开发适配高性能计算集群的开源Python电磁暂态仿真平台


## 使用的方法


- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[伴随电路法|伴随电路法]]
- [[加边块对角矩阵分解|加边块对角矩阵分解]]
- [[并行计算|并行计算]]


## 涉及的模型


- [[逆变器接口电源-ibr|逆变器接口电源(IBR)]]
- [[通用ibr模型|通用IBR模型]]
- [[r-l-c网络元件|R-L-C网络元件]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[高性能计算|高性能计算]]
- [[大规模电网仿真|大规模电网仿真]]
- [[高比例新能源电网|高比例新能源电网]]


## 主要发现


- 在240节点WECC系统中验证了与PSCAD一致的电磁暂态动态精度
- 在万节点级合成电网中利用HPC集群实现约25至36倍的仿真加速比
- 成功构建100%可再生能源区域案例，验证了大规模IBR交互仿真能力


