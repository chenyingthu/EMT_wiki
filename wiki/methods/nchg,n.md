---
title: "Nchg,N"
type: method
tags: [nchg,n]
created: "2026-05-05"
---

# Nchg,N

## 定义与边界

本文提出了一种基于路径的部分重分解（Path-based Partial Refactorization）技术，用于加速电磁暂态（EMT）仿真中的网络方程求解。该方法针对使用KLU求解器的左视LU分解（Left-looking LU factorization），通过识别矩阵变化元素的最小依赖列集，避免对整个矩阵进行完全重分解。核心思想是利用消去图（Elimination Graph）理论，通过深度优先搜索（DFS）计算因子化路径（Factorization Path），仅重分解受影响的列。此外，结合分块三角分解（BTF）技术，将大型稀疏矩阵分解为多个独立或弱耦合的子矩阵，仅对发生变化的子矩阵...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，nchg,n在EMT仿真中用于解决特定问题。

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

- [[partial-refactorization-techniques-for-electromagnetic-transient-simulations]]
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
