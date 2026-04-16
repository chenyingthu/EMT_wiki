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


- 提出基于时间并行(MGRIT)的电磁暂态仿真算法，突破空间并行加速瓶颈
- 构建粗/细时间步状态转换方法，实现平均值与详细开关模型间的初值精确映射
- 设计双层迭代框架，粗步串行推进与细步并行计算结合，提升多状态系统仿真效率


## 使用的方法


- [[时间并行算法|时间并行算法]]
- [[多重网格时间缩减法-mgrit|多重网格时间缩减法(MGRIT)]]
- [[parareal算法|Parareal算法]]
- [[平均值模型|平均值模型]]
- [[详细开关模型|详细开关模型]]
- [[多时间步长迭代|多时间步长迭代]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mmc-model|MMC]]
- [[电力电子系统|电力电子系统]]
- [[子模块-sm|子模块(SM)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[时间并行仿真|时间并行仿真]]
- [[电力电子系统加速|电力电子系统加速]]
- [[多电平换流器建模|多电平换流器建模]]


## 主要发现


- 算法在5核并行下实现最高3.47倍加速，有效突破传统空间并行计算的性能瓶颈
- 所提状态转换方法能精确映射模型初值，仿真结果与详细参考模型高度吻合
- 时间并行框架显著降低含大量子模块MMC的电磁暂态仿真计算负担，保持数值稳定


