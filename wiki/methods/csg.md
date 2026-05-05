---
title: "Csg"
type: method
tags: [csg]
created: "2026-05-05"
---

# Csg

## 定义与边界

本文提出一种适用于交流电网不平衡工况的电网换相换流器（LCC）扩展参数化平均值模型（PAVM）。该方法首先将不平衡交流电源电压分解为正序与负序分量，并引入不平衡度因子与相位偏移进行量化。通过Park变换将交流侧电压/电流映射至多个以n倍同步速正/反向旋转的dq参考坐标系中，利用周期平均技术分离出各次谐波的直流分量。模型核心在于构建三维参数化查找表，将交流侧正负序谐波幅值/相位、直流侧平均量及h次纹波分量与系统运行工况建立非线性映射。同时，模型提供动态微分方程与代数相量两种数学表征形式，前者用于精确捕捉暂态过程，后者用于降低计算负担。该PAVM在EMT仿真中可替代详细开关模型，支持大时间步长计算...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，csg在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$-\frac{dV(x,s)}{dx}=Z(s)I(x,s),\qquad -\frac{dI(x,s)}{dx}=Y(s)V(x,s)$$

$$Z(s)=Z_C(s)+Z_E(s)+Z_G(s)$$

$$Z_G(s)=sL_0$$

$$Y(s)=sC_0$$

$$-\frac{dV(x,s)}{dx}=\left(R'(s)+L_0s\right)I(x,s)$$





## 适用边界与失败模式


基于证据边界的分析：




**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
