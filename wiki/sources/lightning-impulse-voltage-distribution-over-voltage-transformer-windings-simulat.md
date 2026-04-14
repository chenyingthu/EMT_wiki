---
title: "Lightning impulse voltage distribution over voltage transformer windings — Simulation and measurement"
type: source
authors: ['Bojan Trkulja']
year: 2017
journal: "Electric Power Systems Research, 147 (2017) 185-191. doi:10.1016/j.epsr.2017.02.024"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/25/Trkulja 等 - 2017 - Lightning impulse voltage distribution over voltage transformer windings — Simulation and measuremen.pdf"]
---

# Lightning impulse voltage distribution over voltage transformer windings — Simulation and measurement

**作者**: Bojan Trkulja
**年份**: 2017
**来源**: `25/Trkulja 等 - 2017 - Lightning impulse voltage distribution over voltage transformer windings — Simulation and measuremen.pdf`

## 摘要

1. Introduction culated using simple analytical formulas [1–3] or ﬁnite element method (FEM) based calculations [4–7]. Calculation of lumped cir- Voltage transformers in a power system are designed to trans- cuit parameters can be performed using genetic algorithm [8]. form voltages from high vol...

## 核心贡献

- 提出了一种快速且精确计算电压互感器绕组内部电压暂态分布的方法
- 开发了基于边界元法与积分方程的自研求解器，用于计算绕组集总电路参数
- 构建了带有多测量点的电压互感器物理测试模型，并通过实验验证了仿真精度

## 使用的方法

- [[边界元法-bem|边界元法（BEM）]]
- [[积分方程法|积分方程法]]
- [[时域集总参数等效电路求解|时域集总参数等效电路求解]]
- [[基于dommel方法的电磁暂态-emt-数值算法|基于Dommel方法的电磁暂态（EMT）数值算法]]

## 涉及的模型

- [[电压互感器绕组|电压互感器绕组]]
- [[高频集总参数等效电路模型|高频集总参数等效电路模型]]
- [[带内部测量点的物理测试样机|带内部测量点的物理测试样机]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态（EMT）仿真]]
- [[雷电冲击电压分布|雷电冲击电压分布]]
- [[内部过电压与绝缘应力分析|内部过电压与绝缘应力分析]]
- [[电压互感器暂态特性|电压互感器暂态特性]]
- [[数值仿真与实验测量对比|数值仿真与实验测量对比]]

## 主要发现

- 仿真计算得到的绕组内部暂态电压分布与实测数据高度吻合，验证了方法的准确性
- 所提方法能够高效处理复杂几何结构下的参数计算，适用于雷电冲击下的绕组绝缘设计与评估
