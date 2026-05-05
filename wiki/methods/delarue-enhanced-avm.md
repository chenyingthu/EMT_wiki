---
title: "Delarue Enhanced Avm"
type: method
tags: [delarue-enhanced-avm]
created: "2026-05-05"
---

# Delarue Enhanced Avm

## 定义与边界

本文提出一种增强型MMC平均值模型（EAVM），旨在解决传统基于控制信号的AVM在换流器闭锁工况下因初始条件缺失导致的直流电流不连续问题。该方法在现有带桥臂阻抗闭锁模块（AIBM）的改进型AVM（MAVM-AIBM）基础上，于六个桥臂电感两端并联受控电流源。在检测到直流故障并触发闭锁指令的瞬间，利用闭锁前流经直流侧等效阻抗的故障电流值，按三分之一比例分配至各桥臂，通过受控电流源强制初始化桥臂电感电流。该策略无需修改底层求解器即可在EMT软件中实现，既保留了控制信号型AVM结构简单、计算高效的优势，又精准复现了闭锁后二极管续流阶段的暂态电气特性，有效消除了传统模型在模式切换时的数值振荡与电流阶跃...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，delarue-enhanced-avm在EMT仿真中用于解决特定问题。

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

- [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep]]
- [[enhanced-high-speed-electromagnetic-transient-simulation-17]]
- [[enhanced-high-speed-electromagnetic-transient-simulation]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
