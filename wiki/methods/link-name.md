---
title: "Link Name"
type: method
tags: [link-name]
created: "2026-05-05"
---

# Link Name

## 定义与边界

本文提出一种基于频域平衡实现（FDBR）的双频段模型降阶方法，专用于含电力电子换流器的电力系统电磁暂态仿真。传统全频段降阶难以兼顾电网低频机电振荡与换流器高频开关动态。该方法首先利用矢量拟合技术获取线性电网的宽频带全阶状态空间模型。随后，针对低频（Hz级）和高频（kHz级）独立频带，分别计算频域受限的可控性与可观性格拉姆矩阵，并通过求解李雅普诺夫方程量化各频带能量分布。将双频带格拉姆矩阵叠加后，经特征值分解求取相似变换矩阵，将原系统转换为内部平衡形式。最后，依据汉克尔奇异值阈值直接截断弱动态模态，生成低阶模型。该模型与详细开关网络耦合，在大幅降低ODE数量的同时，精准保留目标频带内的主导动态特...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，link-name在EMT仿真中用于解决特定问题。

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

- [[dual-band-reduced-order-model-of-an-hvdc-link-embedded-into-a-power-network-for-]]
- [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne]]
- [[a-link-between-emtp-rv-and-flux3d-for-transformer-energization-studies]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
