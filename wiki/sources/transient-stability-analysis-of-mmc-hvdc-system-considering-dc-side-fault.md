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

- 提出了一种改进的mmc建模方法，提高了EMT仿真效率和精度

## 使用的方法

- [[gpu加速计算|GPU加速计算]]
- [[二维并行矩阵向量乘法|二维并行矩阵向量乘法]]
- [[gpu专用稀疏矩阵技术|GPU专用稀疏矩阵技术]]
- [[并行化算法|并行化算法]]

## 涉及的模型

- [[mmc-model]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态(EMT)仿真]]
- [[并行计算|并行计算]]
- [[gpu高性能计算|GPU高性能计算]]
- [[仿真加速|仿真加速]]
- [[稀疏矩阵优化|稀疏矩阵优化]]

## 主要发现

—This paper presents a novel approach to speedup EMT simulation, using GPU-based computing
