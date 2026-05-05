---
title: "Multi Terminal Dc"
type: method
tags: [multi-terminal-dc]
created: "2026-05-05"
---

# Multi Terminal Dc

## 定义与边界

本文提出一种适用于含直流故障的MMC-MTDC系统机电暂态建模方法。首先，基于基尔霍夫定律与能量守恒原理，严格推导MMC直流侧二阶等效电路，将传统仅含等效电容的一阶模型扩展为包含桥臂等效电感(2Larm/3)和电阻(2Rarm/3)的二阶动态模型，以准确捕捉故障期间的直流电流变化率。其次，构建基于关联矩阵T的广义MTDC网络模型，提出“预设故障信息法”。该方法在仿真前根据故障时间、类型和位置预先构建包含所有可能故障节点与支路的固定拓扑网络，仿真过程中仅通过动态修改支路参数（如将接地电阻从10^6Ω切换至故障电阻、按故障点位置分割π型线路参数）来模拟故障，避免了传统方法中因拓扑重构导致的雅可比矩...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，multi-terminal-dc在EMT仿真中用于解决特定问题。

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

- [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15]]
- [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w]]
- [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
