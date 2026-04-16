---
title: "Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power Electronic Systems"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;6;10.1109/TPWRD.2023.3305035"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/Gao 等 - 2023 - Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power.pdf"]
---

# Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power Electronic Systems

**作者**: 
**年份**: 2023
**来源**: `31/Gao 等 - 2023 - Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power.pdf`

## 摘要

—Efﬁcient electromagnetic transient (EMT) simulation is crucial for addressing the challenges associated with the mod- ularity, cascading, and complex topologies of power electronics (PE) systems. This article introduces a novel portal analysis (PA) approach that adopts a unique “port-component” view, leveraging the characteristics of “ports”. Different from the classic nodal analysis (NA) method, the networks and the components are de- scribed based on the portal voltage equations with lower orders. Furthermore, a port tearing method is introduced to partition the circuit, resulting in a block-bordered-diagonal (BBD) matrix and a small number of boundary variables in the extended port equation. The parallel processing of the network solution is im- plemented by utilizing the BBD forms and

## 核心贡献


- 提出基于端口-元件视角的端口分析法，利用端口特性降低网络方程阶数
- 引入端口撕裂法构建块对角加边矩阵，减少边界变量并支持并行求解
- 设计灵活元件印记机制，避免内部支路重复更新并支持拓扑动态修改


## 使用的方法


- [[端口分析法|端口分析法]]
- [[端口撕裂法|端口撕裂法]]
- [[块对角加边矩阵分解|块对角加边矩阵分解]]
- [[并行计算|并行计算]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[dab变换器|DAB变换器]]
- [[chb-dab|CHB-DAB]]
- [[光伏系统|光伏系统]]
- [[储能系统|储能系统]]
- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[电力电子变压器|电力电子变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子系统建模|电力电子系统建模]]
- [[并行计算|并行计算]]
- [[电路网络划分|电路网络划分]]
- [[微电网仿真|微电网仿真]]


## 主要发现


- 硬件与微电网仿真验证表明，所提模型在各类暂态工况下最大相对误差小于2%
- 相比传统节点分析法，该方法计算速度提升一至两个数量级，显著降低耗时
- 端口撕裂结合BBD矩阵结构有效支持大规模电力电子网络的并行高效求解


