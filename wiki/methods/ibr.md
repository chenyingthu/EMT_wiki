---
title: "Ibr"
type: method
tags: [ibr]
created: "2026-05-05"
---

# Ibr

## 定义与边界

基于Modelica语言的声明式电磁暂态仿真框架，采用方程导向（equation-based）而非赋值语句导向的建模范式。核心创新在于实现物理模型与数值求解器的完全解耦：用户仅需以隐式微分代数方程（DAE）形式描述元件物理行为（如$v = L rac{di}{dt}$），无需关心离散化方法或求解顺序。Modelica编译器通过自动结构分析、BLT（块下三角）排序和撕裂算法（Tearing），将高维稀疏DAE系统转化为高效的计算代码，最终链接至DASSL或IDA求解器进行变步长BDF积分。该方法支持刚性系统（stiff DAEs）求解和精确事件处理（开关操作不连续点），并可通过FMI标准与传统仿...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，ibr在EMT仿真中用于解决特定问题。

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

- [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]
- [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation]]
- [[data-driven-parameter-calibration-of-power-system-emt-model-based-on-sobol-sensi]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
