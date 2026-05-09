---
title: "惯量控制 (Inertia Control)"
type: method
tags: [inertia-control, virtual-inertia, vsg, frequency-support, grid-forming]
created: "2026-05-05"
updated: "2026-05-06"
---

# 惯量控制 (Inertia Control)

## 定义与边界

惯量控制是通过控制器人为引入等效转动惯量、阻尼或暂态功率补偿，使电力电子接口在频率扰动下表现出类似同步机惯性响应的控制方法。它常出现在虚拟同步机、构网型逆变器和储能变流器中。

本页讨论的是频率支撑意义上的“虚拟惯量注入”，不把一般下垂控制、频率扫描工具或任意小信号模型都归为惯量控制。

## EMT 中的作用

在 EMT 仿真中，惯量控制主要用于：

- 研究逆变器主导系统中的频率最低点、RoCoF 和功率振荡；
- 分析虚拟惯量与阻尼参数对频率响应和稳定性的影响；
- 评估储能功率约束、测量延迟和限流逻辑对惯量支撑效果的影响；
- 与 [[droop-control]]、[[adaptive-droop]] 和 [[hierarchical-control]] 配合分析多层频率支撑。

## 关键公式

等效摆动关系常写为：

$$
J \frac{d\Delta \omega}{dt} = P_m - P_e - D \Delta \omega
$$

其中 $J$ 为等效惯量，$D$ 为等效阻尼，$P_m$ 为控制器注入的机械功率等效量，$P_e$ 为电气输出功率。若引入补偿项，也可写成：

$$
P_m = P^\star + K_\omega (\omega_0 - \omega) + P_{comp}
$$

自适应惯量控制进一步使 $J$、$D$ 或 $P_{comp}$ 随状态变化，但那属于本页的扩展分支，不应与固定惯量模型混写。

## 与相关方法的关系

- [[droop-control]]：提供静态共享关系，但不直接等同于惯量注入。
- [[adaptive-droop]]：调整下垂系数，与调整等效惯量是不同手段。
- [[hierarchical-control]]：惯量控制常属于一次频率支撑层。
- [[virtual-synchronous-generator]]：更完整的同步机型构网控制背景。

## 适用边界与失败模式

- 适用于需要改善频率暂态响应的逆变器主导系统和储能支撑场景。
- 虚拟惯量过大可能导致功率超调、控制振荡或能量约束冲突。
- 储能容量和功率限制会直接约束可实现的惯量支撑。
- 测量延迟、频率估计误差和限流逻辑会削弱理想惯量模型的解释力。

## 代表性来源

- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：直接支撑自适应惯量与暂态补偿控制的场景。
- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：说明构网型逆变器与储能在频率支撑场景中的应用背景。
- [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-]]：可作为新能源并网和频率响应复杂性的背景来源。

## 证据边界

本页只说明惯量控制的结构和边界，不新增无来源的最优惯量、最优阻尼、频率最低点改善百分比或稳定裕度结论。具体效果必须绑定系统规模、储能约束和测试工况。
