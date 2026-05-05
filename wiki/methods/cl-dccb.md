---
title: "Cl Dccb"
type: method
tags: [cl-dccb]
created: "2026-05-05"
---

# Cl Dccb

## 定义与边界

本文提出了一种基于诺顿等效和分段线性化的混合式高压直流断路器(HHB)实时仿真建模方法。针对实时计算约束，将详细的非线性半导体模型（IGBT/二极管）简化为双值电阻模型，将金属氧化物避雷器(MOV)简化为多段分段线性电阻。通过预计算各主支路单元的等效电阻和诺顿等效电流源，将原本复杂的非线性电路求解转化为线性代数方程求解，满足实时仿真的计算时序要求。同时构建了包含物理MMC控制器和12个DCCB控制器的三端直流电网硬件在环(HIL)测试平台，实现了控制器硬件与实时仿真器的闭环交互。...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，cl-dccb在EMT仿真中用于解决特定问题。

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

- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]
- [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran]]
- [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
