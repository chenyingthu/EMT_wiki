---
title: "Cigre B4"
type: method
tags: [cigre-b4]
created: "2026-05-05"
---

# Cigre B4

## 定义与边界

为满足对交直流系统电磁–机电暂态特性准确、快速和灵活仿真的需要，提出基于移频分析等方法的含柔性高压直流(voltage source converter-based high voltage direct current，VSC-HVDC)输电交直流电力系统多尺度暂态模型。移频分析法采用希尔伯特变换，通过移除或保留交流信号基频载波实现慢–快变化暂态的模拟。该文建立了 VSC 移频相量模型，推导出 VSC 移频域与其控制系统 域的转换关系，选择性插入 模型获得直流输电线多尺度暂态模型，进而构建了全系统多尺度暂态模型。该模型通过设置仿真参数(如时间步长)能够满足不同时间、不同电网位置电磁或机电暂态...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，cigre-b4在EMT仿真中用于解决特定问题。

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

- [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40]]
- [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat]]
- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
