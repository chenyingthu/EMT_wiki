---
title: "Mbsm"
type: method
tags: [mbsm]
created: "2026-05-05"
---

# Mbsm

## 定义与边界

本文提出一种结合详细等效模型（DEM）与广义开关函数平均值模型（GSFB-AVM）的统一MMC仿真框架。核心在于构建通用桥臂等效电路（UAM），利用反并联二极管自动识别桥臂电流方向，并通过受控电压源表征桥臂动态。GSFB-AVM基于桥臂等效电容与插入指数，推导适用于半桥、全桥、钳位双桥及混合桥等多种子模块拓扑的广义状态方程，精确计及闭锁/解锁模式下的电容充放电特性与半导体导通压降。DEM则保留各子模块独立电容电压与开关事件。两者通过历史电压数据交互机制实现动态仿真中的无缝平滑切换：GSFB-AVM转DEM时均分平均电压，DEM转GSFB-AVM时累加个体电压。此外，模型采用分段线性V-I特性计...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，mbsm在EMT仿真中用于解决特定问题。

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

- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-]]
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
