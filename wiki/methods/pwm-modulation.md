---
title: "PWM 调制方法"
type: method
tags: [pwm-modulation, pwm, modulation, converter-control, switching]
created: "2026-05-04"
updated: "2026-05-07"
---

# PWM 调制方法

## 定义与边界

PWM（Pulse Width Modulation）调制方法是通过控制开关器件导通占空比或触发时刻来合成目标电压/电流波形的基本方法。它常出现在逆变器、整流器、DC/DC 变换器和多电平换流器控制中。

本页讨论的是 PWM 作为调制与执行方法的边界，不把时域变换算法、无关网络模型或某篇线路求解论文误写成 PWM 方法页。

## EMT 中的作用

在 EMT 仿真中，PWM 调制主要用于：

- 生成开关器件的触发与导通时序；
- 连接控制器输出与主电路开关状态；
- 分析开关频率、占空比和载波策略对波形与暂态的影响；
- 为详细开关模型、平均值模型和实时等效模型提供调制背景。

## 常见分支

- 正弦 PWM（SPWM）；
- 载波移相 PWM（CPS-SPWM）；
- 空间矢量 PWM（SVPWM）；
- 面向多电平或高频链的专用 PWM 变体。

## 关键公式

PWM 的最小占空比关系可抽象写为：

$$
d(t)=\frac{t_{on}}{T_s}
$$

其中 $t_{on}$ 为开关导通时间，$T_s$ 为开关周期。对 EMT 来说，关键不只是占空比值，而是触发时刻、采样方式和主电路动态如何共同决定开关事件。

## 与相关页面的关系

- [[power-electronics-control]]：控制总入口。
- [[phase-locked-loop]]：并网同步背景会影响调制参考量。
- [[nearest-level-modulation]]：多电平离散电平调制的相关背景。
- [[dual-active-bridge]]：高频 DC/DC 装置中的调制背景。
- [[grid-connected-inverter]]：典型并网 PWM 应用背景。

## 代表性来源

- [[modulation-index-dependent-thevenin-equivalent-circuit-model-of-vsc-and-apdr]]：调制指数与等效模型背景。
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：调制与同步链路的相关背景。
- [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver]]：控制参数与调制执行背景。

## 证据边界

本页不写无来源的最优调制方式、统一谐波性能或固定开关频率结论。具体效果必须绑定装置拓扑、载波策略和验证工况。

## 开放问题

- 当前页尚未继续拆分两电平、多电平和高频链装置中 PWM 的建模边界。
- 调制层与平均值模型、开关函数模型之间的衔接，后续仍需在相邻页面中细化。
