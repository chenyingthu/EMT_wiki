---
title: "Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics; ;PP;99;10.1109/JESTPE.2019.2947411"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/30/JESTPE.2019.2947411.pdf.pdf"]
---

# Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System

**作者**: 
**年份**: 2019
**来源**: `30/JESTPE.2019.2947411.pdf.pdf`

## 摘要

—The complexity in simulating power electron- ics like modular multilevel converters (MMCs) requires simulation algorithms to speed-up the process. Existing simulation algorithms exploit spatial parallelism to speed- up simulation. With rise in complexity of power electronics and presence of increased number of states within them, there are limits in the speed-up using spatial parallelism. In this paper, a temporal parallelism algorithm based on parallel-in-time methods is developed for simulation of power-electronics-systems. The temporal parallelism algorithm is based on computation of power-electronics- states on coarse and ﬁne time-steps using different models. The models of power-electronics-systems used in coarse and ﬁne time-steps are average-value and detailed models, respectively.

## 核心贡献

- 提出了一种改进的mmc建模方法，提高了EMT仿真效率和精度
- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[时间并行算法|时间并行算法]]
- [[粗细时间步计算|粗细时间步计算]]
- [[串行-并行混合计算|串行-并行混合计算]]
- [[状态转换方法|状态转换方法]]

## 涉及的模型

- [[mmc-model]]

## 相关主题

- [[parallel-computing]]

## 主要发现

—The complexity in simulating power electron- ics like modular multilevel converters (MMCs) requires simulation algorithms to speed-up the process
