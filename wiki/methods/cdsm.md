---
title: "Cdsm"
type: method
tags: [cdsm]
created: "2026-05-05"
---

# Cdsm

## 定义与边界

本文提出了一种分层混合建模方法（Hierarchical Hybrid Modeling），将系统级等效电路模型（Equivalent Circuit Model, ECM）与CDSM（Clamp Double Submodule）的器件级电热模型（Device-Level Electrothermal Model, DLEM）相结合。在MPSoC的PL（Programmable Logic）侧实现并行电磁暂态求解，在PS（Processing System）侧实现热网络计算与参数管理。该方法通过动态切换机制，在保证系统级实时性的同时，对关键CDSM子模块进行器件级精细建模，实现IGBT开关瞬...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，cdsm在EMT仿真中用于解决特定问题。

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

- [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-]]
- [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法]]
- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
