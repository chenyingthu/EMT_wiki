---
title: "Dc Protection"
type: method
tags: [dc-protection]
created: "2026-05-05"
---

# Dc Protection

## 定义与边界

本文提出在EMTP中集成保护系统的完整框架，包括电流互感器(CT)和电容式电压互感器(CVT)的暂态模型、FORTRAN用户子程序接口以及闭环交互机制。核心方法是基于EMTP的节点导纳矩阵时域仿真，通过Type 96伪非线性磁滞电感精确模拟CT的铁芯饱和特性，同时开发外部FORTRAN接口允许用户自定义继电器算法。仿真采用时步迭代法，每个时间步内依次求解电力系统暂态、互感器动态响应、继电器算法处理，并将保护决策（断路器跳闸/重合闸）实时反馈至电力系统，实现真正意义上的闭环保护系统仿真。...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，dc-protection在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

- 待补充



## 适用边界与失败模式

- 待补充

**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[protection-system-representation-in-the-electromagnetic-transients-program-power]]
- [[application-of-wavelet-singular-entropy-theory-in-transient-protection-and-accel]]
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
