---
title: "Transient Stability Analysis of MMC-HVDC System Considering DC-side Fault"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/tpwrd.2015.2492983.pdf.pdf"]
---

# Transient Stability Analysis of MMC-HVDC System Considering DC-side Fault

**作者**: 
**年份**: 2015
**来源**: `19、20、21/EMT_task_21/tpwrd.2015.2492983.pdf.pdf`

## 摘要

—This paper presents a novel approach to speedup EMT simulation, using GPU-based computing. This paper ex- tends earlier published works in the area, by exploiting additional parallelism inside EMT simulation. A 2D-parallel matrix-vector multiplication is used that is faster than previous 1D-methods. Also this paper implements a GPU-speciﬁc sparsity technique to further speed up the simulations, as the available CPU-based sparsity techniques are not suitable for GPUs. Additionally, as an extension to previous works, this paper demonstrates modelling of a power electronic subsystem. The efﬁcacy of the approach is demonstrated using two different scalable test systems. A low granularity system, i.e. one with a large cluster of busses connected to others with a few transmission lines is consi

## 核心贡献



- 提出基于GPU的电磁暂态仿真加速架构
- 实现2D并行矩阵向量乘法与GPU专用稀疏矩阵算法
- 在GPU平台上完成电力电子子系统及同步发电机的并行建模

## 使用的方法


- [[parallel]]
- [[nodal-analysis]]
- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]
- [[synchronous-machine]]
- [[mmc-model]]

## 相关主题


- [[real-time]]
- [[hvdc]]
- [[mmc]]

## 主要发现



- GPU稀疏技术仅能带来微小的仿真时间优化
- 系统粒度过高会显著降低GPU并行仿真效率
- 2D并行矩阵向量乘法在计算速度上优于传统1D方法