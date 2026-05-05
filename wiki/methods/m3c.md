---
title: "M3C"
type: method
tags: [m3c]
created: "2026-05-05"
---

# M3C

## 定义与边界

本文针对含模块化多电平矩阵换流器（M3C）的低频交流（LFAC）系统，提出了一套完整的机电暂态建模与仿真方法。首先，基于基尔霍夫电压定律建立M3C桥臂数学模型，并通过双重αβ0变换解耦得到输入/输出侧等效电路。其次，针对工频与低频混合电网特性，推导了考虑频率缩放的线路阻抗/导纳参数，并设计了适用于M3C-LFAC系统的迭代潮流计算算法，支持跟网型、构网型（含U-f与VSG控制）等多种运行模式。最后，基于正序基波相量法构建M3C机电动态模型，利用PSS/E的用户自定义模型（UDM）功能实现，并引入虚拟同步机（VSG）控制策略以支持去中心化构网运行。该方法在保证精度的前提下，大幅提升了大规模混合交...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，m3c在EMT仿真中用于解决特定问题。

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

- [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular]]
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
