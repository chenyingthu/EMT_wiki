---
title: "CIGRE 三端 MTDC 场景入口"
type: test-system
tags: [cigre-mtdc-three-terminal, mtdc, three-terminal, benchmark, hvdc]
created: "2026-05-04"
updated: "2026-05-06"
---

# CIGRE 三端 MTDC 场景入口

## 定义与边界

该入口用于承接 CIGRE 风格三端多端直流系统场景下的 EMT 建模、控制和保护研究。它不是变压器建模页，也不是 GPU 加速或频率控制页，而是一个场景/系统入口页。

## EMT 中的作用

在 EMT 知识网络中，这类三端 MTDC 场景常用于：

- 对比不同站级控制和功率分配策略；
- 研究直流故障传播和断路器配合；
- 说明多端拓扑比双端系统多出的协调复杂性；
- 作为更一般 [[multi-terminal-dc]] 方法页的案例背景。

## 常见研究对象

- 站间功率分配和直流电压下垂协调；
- 故障后区段隔离与断路器时序；
- 构网或跟网 VSC 在多端直流中的初始化与稳定性；
- 三端拓扑与更一般多端拓扑之间的可扩展性比较。

## 形式化表达

三端 MTDC 的最小系统级关系可抽象写为：

$$
\sum_{i=1}^{3} P_i = P_{loss}
$$

若使用电压下垂分担，则又可写为：

$$
P_i^\* = P_{i0} + k_{di}(V_{dc,0}-V_{dc,i})
$$

## 相关页面

- [[multi-terminal-dc]]：更一般的多端直流方法页。
- [[cigre-b4-dc-grid]]：更上位的 CIGRE 直流电网场景入口。
- [[dccb]] 和 [[dc-protection]]：故障隔离相关方法。
- [[mt-hvdc-test-system]]：主题层面的测试系统背景。

## 代表性来源

- [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15]]：说明多端直流系统建模背景。
- [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]]：说明多端直流场景中的 EMT 初始化问题。
- [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy]]：说明稳定性分析背景。

## 证据边界

本页不提供固定拓扑参数或统一结论，只作为三端 MTDC 场景入口使用。

## 开放问题

- 三端场景中的结论能否外推到更高端数拓扑，必须回到具体网络和控制结构验证。
- 当前页尚未继续拆分控制类、保护类和初始化类算例。
