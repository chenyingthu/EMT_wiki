---
title: "Cigre Mtdc Three Terminal"
type: method
tags: [cigre-mtdc-three-terminal]
created: "2026-05-04"
---

# Cigre Mtdc Three Terminal

## 定义与边界

本页面为自动创建的method类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

## 主要分支与机制

- 待补充


## 验证与测试

基于相关研究的验证证据：

- **数值结果**: 0%, 0Hz


## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$\begin{cases}J\frac{d\omega}{dt}=\frac{P_m}{\omega_0}-\frac{P_e}{\omega_0}-D(\omega-\omega_0)\\\frac{d\theta}{dt}=\omega\end{cases}$$

$$P_m=P_{ref}+K_f(\omega_n-\omega)$$

$$

*有功功率参考值生成式，体现一次调频下垂特性。*

**公式3**: $$

$$\begin{cases}Q_m=Q_{ref}+K_v(U_n-U)\\e_d=\frac{K}{s}(Q_m-Q_e)\end{cases}$$

$$

*无功-电压积分下垂控制方程，用于模拟同步机励磁调节特性。*

**公式4**: $$



## 适用边界与失败模式

- 待补充

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w]]
- [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]]
- [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d]]
- [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15]]
- [[neutral-conductor-current-in-three-phase-networks-with-compact-fluorescent-lamps]]
