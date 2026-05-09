---
title: "分层控制 (Hierarchical Control)"
type: method
tags: [hierarchical-control, primary-control, secondary-control, tertiary-control, coordination]
created: "2026-05-05"
updated: "2026-05-06"
---

# 分层控制 (Hierarchical Control)


```mermaid
graph TD
    subgraph S0[分层控制 (Hierarchical Control)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见层级]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[适用边界与失败模式]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

分层控制是把控制任务按时间尺度和职责分成一次、二次、三次或更高层级的组织方法。它广泛用于微电网、储能系统、多变流器并联系统和多端直流网络中，用来协调快速稳定、稳态恢复和更慢的调度优化任务。

本页讨论的是控制分层逻辑，不把 CPU-FPGA 实时仿真分区、硬件资源分配或主电路模型切换误写成“分层控制”。

## EMT 中的作用

在 EMT 仿真中，分层控制用于：

- 区分一次支撑、二次恢复和更慢能量管理的动态作用；
- 研究层间带宽分离不充分时的相互作用；
- 分析通信延迟、模式切换和功率限值如何跨层传播；
- 为多装置协调提供结构化解释框架。

## 常见层级

- 一次控制：快速局部支撑，例如 [[droop-control]]、[[inertia-control]] 或限流控制。
- 二次控制：恢复频率、电压或功率共享偏差，常与 [[distributed-control]] 结合。
- 三次控制：更慢的调度、经济优化或运行方式管理，可与 [[economic-dispatch]]、[[optimal-power-flow]] 关联。

## 关键公式

分层控制本身不是单一方程，但可抽象为快慢参考的级联更新：

$$
r_1 = f_1(y), \qquad
r_2 = f_2(y, \bar{y}), \qquad
r_3 = f_3(\mathcal{O}, \mathcal{C})
$$

其中 $r_1,r_2,r_3$ 分别表示不同层级输出的参考量，$y$ 为局部测量，$\bar{y}$ 为协调或邻居信息，$\mathcal{O},\mathcal{C}$ 为更慢层面的运行目标和约束。关键不在公式形式，而在不同层级的时间尺度和职责边界。

## 与相关方法的关系

- [[droop-control]]：常见一次控制层。
- [[distributed-control]]：常见二次协调层。
- [[adaptive-droop]]：可看作一次层参数自适应的扩展。
- [[microgrid-control]] 和 [[multi-terminal-dc]]：是分层控制的典型应用场景。

## 适用边界与失败模式

- 适用于多目标、不同时间尺度同时存在的控制场景。
- 若层间带宽分离不足，可能出现相互抢占、振荡或恢复缓慢。
- 若上层参考更新过慢或通信不可靠，下层可能长期运行在偏差状态。
- 若能量管理与保护约束不一致，层级设计可能在故障下失效。

## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：说明一次下垂和更慢恢复/管理层级在构网型场景中的组织。
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]：说明多层控制与保护在实时闭环中的协调问题。
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]：可作为多环控制和局部阻尼层与外层目标耦合的相关来源。

## 证据边界

本页强调的是层级组织，不给出无来源的固定带宽比例、恢复时间或“最优分层架构”。具体实现必须回到应用系统和对应来源。
