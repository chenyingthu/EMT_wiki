---
title: "双闭环Pi控制器"
type: method
tags: [双闭环pi控制器]
created: "2026-05-05"
---

# 双闭环Pi控制器

## 定义与边界

基于模块化多电平换流器的高压直流输电（MMC-HVDC）的长链路延时引发的高频振荡严重威胁了电力系统的安全稳定运行。采用时滞稳定裕度衡量 MMC-HVDC 系统的高频稳定性，建立了 MMC-HVDC 时滞系统的高阶状态空间模型，应用基于广义特征根的时滞系统稳定性分析方法直接求解 MMC-HVDC 系统的时滞稳定裕度，并分析了控制器参数对系统高频稳定性的影响。将 MMC-HVDC 系统链路延时对系统高频稳定性的影响等效为外部干扰，通过混合灵敏度优化设计了基于 鲁棒控制的 MMC-HVDC 系统高频振荡抑制策略。通过 MMC-HVDC 电磁暂态仿真，验证了基于广义特征根的时滞系统稳定性分析方法求解...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，双闭环pi控制器在EMT仿真中用于解决特定问题。

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

- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
