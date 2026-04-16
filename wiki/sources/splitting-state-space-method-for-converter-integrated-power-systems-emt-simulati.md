---
title: "Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;1;10.1109/TPWRD.2024.3514294"
tags: ['state-space']
created: "2026-04-13"
sources: ["EMT_Doc/35/Fu 等 - 2025 - Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations.pdf"]
---

# Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations

**作者**: 
**年份**: 2025
**来源**: `35/Fu 等 - 2025 - Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations.pdf`

## 摘要

—As the utilization of power electronic-based compo- nents in power systems continues to grow, a comprehensive un- derstanding of their dynamics becomes increasingly important for system design, control and protection analysis. To meet practi- cal needs, the high-ﬁdelity but time-consuming electromagnetic transient (EMT) simulations are often required. To improve the performance of these simulations, a highly efﬁcient splitting state- space method with numerical error control is proposed that reduces the computation workload. The method employs a generic decou- pling principle to split the state-space equations of the converter- integrated power system and introduces the exponential splitting formulas of multiple orders accuracy to solve and then compose the splitting state-space equations

## 核心贡献



- 提出了一种具有数值误差控制的高效分裂状态空间法，显著降低了含变流器电力系统EMT仿真的计算负担。
- 设计了基于状态矩阵时变部分分离的通用解耦原则，并引入多阶精度的指数分裂公式以加速矩阵指数计算。

## 使用的方法


- [[state-space]]
- [[numerical-integration]]

## 涉及的模型


- [[mmc-model]]
- [[wind-farm]]

## 相关主题


- [[real-time]]
- [[vsc]]

## 主要发现



- 该方法在含直流负载配电网、LLC变换器、大型风电场及MMC电路等多种测试案例中均验证了高保真度与计算准确性。
- 基于自动开关分组与相邻状态变量识别的解耦策略结合指数分裂方案，有效控制了数值误差并大幅提升了大规模电力电子系统EMT仿真的计算效率。