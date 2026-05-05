---
title: "Inertia Control"
type: method
tags: [inertia-control]
created: "2026-05-05"
---

# Inertia Control

## 定义与边界

本文针对并联VSC-ESS（电压源变换器储能系统）在频率调节过程中的有功功率振荡和超调问题，提出了一种基于暂态电磁功率补偿的自适应惯量控制策略。首先建立并联VSC-ESS的完整数学模型，包括基于虚拟同步机（VSG）理论的有功-频率控制和无功-电压控制。通过推导小信号状态空间方程和传递函数，分析虚拟惯量、虚拟阻尼、补偿系数和时间常数等关键参数对系统稳定性和频率响应特性的影响。基于幅频特性曲线和极点轨迹分析不同VSC-ESS单元间参数的交互作用及其对系统频率响应的影响。进而设计暂态电磁功率补偿控制策略以抑制频率响应过程中的超调和振荡，并提出自适应惯量控制方法，通过设计自适应系数在频率响应过程中动态...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

#.

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

- 待补充


### 核心数学表达

从相关研究提取的关键公式：

$$J_i\frac{d\Delta\omega_i}{dt}=\frac{P_{mi}}{\omega_0}-\frac{P_{0i}}{\omega_0}-D_i(\omega_i-\omega_0),\qquad P_{mi}=P_{refi}+k_{\omega i}(\omega_0-\omega)$$

$$E_i=\frac{1}{K_{qi}s}\left[Q_{refi}-Q_{0i}+D_{qi}(U_{cni}-U_c)\right]$$

$$P_{0i}=\frac{3U_{ci}U_g\sin\delta_i}{2\omega_0L_i}\approx\frac{3U_{ci}U_g}{2X_i}\delta_i\approx K_i\delta_i,\qquad \delta_i=\int(\omega_i-\omega_{bus})dt$$

$$\frac{\Delta\omega_i(s)}{\Delta\omega_{bus}(s)}=\frac{K_i}{J_i\omega_0s^2+(D_i\omega_0+k_{\omega i})s+K_i}$$



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

- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]
- [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve]]
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
