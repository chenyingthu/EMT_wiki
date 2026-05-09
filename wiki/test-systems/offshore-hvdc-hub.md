---
title: "海上 HVDC 枢纽场景入口 (Offshore HVDC Hub)"
type: test-system
tags: [offshore-hvdc-hub, offshore-hvdc, dc-grid, offshore-wind, hub]
created: "2026-05-05"
updated: "2026-05-06"
---

# 海上 HVDC 枢纽场景入口 (Offshore HVDC Hub)


```mermaid
graph TD
    subgraph S0[海上 HVDC 枢纽场景入口 (Offshore HVD…]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见研究对象]
        N3[关键关系]
        N4[关键公式]
        N5[适用边界与失败模式]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

海上 HVDC 枢纽场景入口是指围绕海上多风场汇集、海上换流站互联和海上直流网络协调建立的系统级场景。它关注的是“枢纽化海上直流送出系统”的拓扑、控制、保护和接口组织，而不是某一篇关于高频振荡或时滞稳定裕度的特定分析方法。

## EMT 中的作用

在 EMT 仿真中，海上 HVDC 枢纽方法主要用于：

- 组织多个海上风场、海上站和陆上站之间的系统级模型；
- 研究海上汇集、站间控制和故障隔离的相互作用；
- 分析海缆、电压支撑、海上弱网和多端直流网络的动态耦合；
- 为海上风电大规模送出和海上直流电网扩展提供测试系统背景。

## 常见研究对象

- 多海上风场到海上换流站的汇集结构；
- 海上站与陆上站之间的控制协调；
- 海缆、直流网络与弱网接口的耦合；
- 故障后区段隔离、重构与恢复。

## 关键关系

- [[offshore-wind-integration]]：风场并网与集电网络背景。
- [[multi-terminal-dc]]：海上 HVDC 枢纽常是 MTDC 的具体应用形态。
- [[hvdc-control]]：对应海上/陆上换流站控制结构。
- [[dc-protection]] 与 [[dccb]]：对应故障隔离和恢复问题。

## 关键公式

海上 HVDC 枢纽没有统一单一公式，但系统级功率平衡仍可抽象写为：

$$
\sum P_{wind} - P_{loss} = \sum P_{onshore}
$$

其难点通常不在静态平衡本身，而在多站控制、故障切换和网络耦合如何在 EMT 中被同时解释。

## 适用边界与失败模式

- 适用于研究多风场汇集和海上多站直流送出场景。
- 海缆参数、海上站控制、弱网和直流故障会显著影响系统动态。
- 单篇关于时滞、高频振荡或某一种控制器的结果不能直接概括整个海上枢纽方法。

## 代表性来源

- [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15]]：说明海上多端直流背景中的系统级建模问题。
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]：说明海上/长距离 HVDC 场景中高频稳定问题的相关背景。
- [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40]]：说明海上送出相关多尺度建模背景。

## 证据边界

本页不写无来源枢纽容量、海缆长度上限或统一控制方案。具体结论必须绑定拓扑、风场规模和控制配置。

## 开放问题

- 当前页尚未继续拆分海上枢纽中的控制、保护和网络规划三类方法边界。
- 海上多站扩展后的结论能否外推到更一般 MTDC 场景，仍需结合具体 benchmark 判断。
