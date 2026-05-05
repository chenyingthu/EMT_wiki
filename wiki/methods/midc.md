---
title: "Midc"
type: method
tags: [midc]
created: "2026-05-05"
---

# Midc

## 定义与边界

模块化隔离型 DC/DC 变换器(modular isolated DC/DC converter，MIDC)作为光伏、风电等直流电源并网的重要方案，受到广泛关注。输入并联输出串联(input parallel output series，IPOS)型单有源桥(single active bridge，SAB)变换器是 MIDC 的常用拓扑之一，由于节点导纳矩阵阶数高、仿真步长小以及不控整流桥的存在，其电磁暂态仿真效率很低。文中提出一种基于电流过零点预计算的 SAB 变换器等效建模方法。首先，针对 SAB 变换器的拓扑结构和工作原理进行分析，求解不同模式下电感电流表达式。其次，计算电感电流过零...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，midc在EMT仿真中用于解决特定问题。

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

- [[equivalent-modelling-method-of-single-active-network-for-fast-electromagnetic-tr]]
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
