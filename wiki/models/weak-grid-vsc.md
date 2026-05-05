---
title: "Weak Grid Vsc"
type: model
tags: [weak-grid-vsc]
created: "2026-05-04"
---

# Weak Grid Vsc

## 定义与边界

本页面为自动创建的model类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

## 主要分支与机制

- 待补充

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

- [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]
- [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using]]
- [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s]]
- [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt]]
- [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea]]
