---
title: "电力电子控制方法入口"
type: method
tags: [power-electronics-control, converter-control, control-loop, modulation, synchronization]
created: "2026-05-04"
updated: "2026-05-07"
---

# 电力电子控制方法入口

## 定义与边界

电力电子控制方法入口用于承接换流器、逆变器、整流器和高频 DC/DC 装置中的控制结构、控制层级和接口建模问题。它是控制类页面的上位入口，而不是某一篇关于惯量控制、线路建模或单一调制算法的专页。

本页讨论的是电力电子装置控制的总体方法边界，不把单个装置的专门控制页混写成通用结论。

## EMT 中的作用

在 EMT 仿真中，电力电子控制方法主要用于：

- 组织内环、电压/电流控制、外环功率控制和限流逻辑；
- 连接同步、调制、保护和主电路动态；
- 分析控制器参数、时延和采样对暂态响应与稳定性的影响；
- 作为设备级模型和系统级控制页之间的中间入口。

## 常见分支

- 内环控制：电流环、电压环和状态反馈控制。
- 外环控制：功率、直流电压、频率和无功控制。
- 同步与测量：PLL、观测器和滤波结构。
- 调制与执行：PWM、NLM、开关函数和触发策略。

## 形式化表达

电力电子控制的最小反馈结构可抽象写为：

$$
u(t)=\mathcal{K}\big(r(t),\,y(t),\,x(t)\big)
$$

其中 $r(t)$ 表示参考量，$y(t)$ 表示测量量，$x(t)$ 表示控制器内部状态，$u(t)$ 表示调制、触发或等效控制输入。具体控制性能取决于控制层级、采样时序和主电路对象。

## 与相关页面的关系

- [[phase-locked-loop]]：同步与测量背景。
- [[pll-design]]：同步环参数设计背景。
- [[pwm-modulation]]：调制与执行背景。
- [[frequency-control]]：系统级频率控制背景。
- [[grid-connected-inverter]]：典型并网设备控制背景。

## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：构网型控制背景。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：控制参数与频率响应背景。
- [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb]]：电力电子装置控制与平均值模型耦合背景。

## 证据边界

本页不写无来源的最优控制架构、统一参数范围或所有装置通用结论。具体能力必须绑定控制对象、网络环境和验证工况。

## 开放问题

- 当前页尚未继续拆分 GFL、GFM、HVDC、PET 和高频 DC/DC 装置控制之间的差异。
- 控制层级与同步/调制页之间的边界，后续仍需在相邻页面中继续细化。
