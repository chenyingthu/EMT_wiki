---
title: "晶闸管投切电容方法入口 (TSC)"
type: method
tags: [tsc, thyristor-switched-capacitor, reactive-compensation, facts, switching]
created: "2026-05-04"
updated: "2026-05-07"
---

# 晶闸管投切电容方法入口 (TSC)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[常见场景]
    N1 --> N2
    N3[形式化表达]
    N2 --> N3
    N4[与相关页面的关系]
    N3 --> N4
    N5[代表性来源]
    N4 --> N5
    N6[证据边界]
    N5 --> N6
    N7[开放问题]
    N6 --> N7
```


## 定义与边界

TSC 通常指 Thyristor Switched Capacitor，即通过晶闸管投切电容支路实现无功补偿的装置或方法入口。它常作为 SVC 或其他 FACTS 装置中的组成单元出现。

本页讨论的是 TSC 作为投切无功补偿支路的边界，不把一般线路模型或无关混合仿真框架误写成 TSC 方法页。

## EMT 中的作用

在 EMT 仿真中，TSC 方法主要用于：

- 表达晶闸管投切电容支路的投切时序和暂态响应；
- 研究无功补偿、电压支撑和投切过渡过程；
- 作为 SVC、FACTS 和并网补偿场景中的基本支路模型；
- 分析投切时刻、电压波形和系统振荡之间的耦合。

## 常见场景

- SVC 中的分级无功投切；
- 并网点电压支撑和无功补偿；
- 投切电容引发的暂态波形与过渡过程；
- 与其他 FACTS 支路联合作用的系统级补偿场景。

## 形式化表达

TSC 的最小无功补偿关系可抽象写为：

$$
Q_c = \omega C V^2
$$

在 EMT 中，真正重要的是晶闸管投切时刻和电容支路如何进入电磁暂态过程，而不只是稳态无功公式本身。

## 与相关页面的关系

- [[facts]]：FACTS 装置总入口。
- [[reactive-compensation-device]]：无功补偿装置背景。
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]]：SVC/TSC 场景相关背景。
- [[power-electronics-control]]：投切与控制协调背景。
- [[svc-model]]：SVC 装置模型背景。
- [[power-system-network]]：补偿支路与系统网络耦合背景。

## 代表性来源

- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]]：SVC/TSC 动态建模背景。
- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]]：TSC 与混合硬件在环背景。
- [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc]]：无功控制与系统动态背景。

## 证据边界

本页不写无来源的统一补偿容量、最优投切策略或所有工况通用的暂态结论。具体结论必须绑定支路参数、控制逻辑和验证工况。

## 开放问题

- 当前页尚未继续拆分 TSC 单支路与 SVC 组合系统中的边界。
- 投切时序、谐波和过电压风险如何统一建模，后续仍需在相邻页面中细化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
