---
title: "下垂控制 (Droop Control)"
type: method
tags: [droop-control, grid-forming, power-sharing, frequency-control, voltage-control]
created: "2026-05-05"
updated: "2026-05-06"
---

# 下垂控制 (Droop Control)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[主要分支]
    N1 --> N2
    N3[关键公式]
    N2 --> N3
    N4[验证共识]
    N3 --> N4
    N5[量化线索]
    N4 --> N5
    N6[与相关方法的关系]
    N5 --> N6
    N7[适用边界与失败模式]
    N6 --> N7
```


## 定义与边界

下垂控制是在不依赖高速通信的条件下，通过频率-有功和电压-无功静态关系实现并联系统功率共享的控制方法。它是微电网、储能并网、构网型逆变器和多变流器并联系统中的常见一次控制结构。

本页讨论的是控制律和共享机制本身，不把黑启动、电池能量管理、CPU-FPGA 实时仿真框架或频率扫描工具混写为“下垂控制”。

## EMT 中的作用

在 EMT 仿真里，下垂控制常用于：

- 分析并联逆变器之间的有功/无功分配；
- 研究孤岛运行和黑启动过程中的频率、电压建立；
- 评估弱网、线路阻抗和滤波器参数对功率共享误差的影响；
- 与二次控制配合，分析稳态偏差恢复与暂态性能折中。

## 主要分支

在当前 Wiki 语境中，下垂控制至少有 3 个常见分支：

1. 有功-频率/无功-电压基本下垂：最传统的共享形式。
2. 构网型逆变器下垂：强调黑启动、孤岛供电和弱网支撑。
3. 与二次恢复或能量管理耦合的层级下垂：强调恢复稳态偏差和运行约束。

这些分支共享静态下垂关系，但控制对象、实现设备和约束条件并不相同。

## 关键公式

标准有功-频率与无功-电压下垂关系常写为：

$$
\omega = \omega_0 - m_p (P - P^\star)
$$

$$
V = V_0 - n_q (Q - Q^\star)
$$

其中 $\omega_0$、$V_0$ 为额定频率和电压参考，$m_p$、$n_q$ 为下垂系数。下垂系数越大，控制器对功率偏差越敏感，但系统频率/电压偏移也可能更明显。

若采用二次恢复控制，常把恢复环作为较慢层级叠加在下垂外环上，而不是取消下垂本身。

## 验证共识

现有来源和相邻页面能稳定支持的共识包括：

- 下垂控制的核心价值是无高速通信条件下的近似共享，而不是严格最优分配。
- 频率共享与无功共享常受线路阻抗、滤波器和测量位置影响。
- 构网型逆变器场景把下垂控制看成一次控制骨架，而不是全部控制逻辑。
- 一旦进入限流、保护或模式切换工况，理想下垂关系往往会被覆盖。

## 量化线索

- 当前页面至少覆盖 `3` 个控制分支。
- 基本控制律至少由 `2` 条核心关系构成：$P$-$\omega$ 和 $Q$-$V$。
- 当前交叉引用已连接不少于 `6` 个相关控制/设备页面，说明它是一个骨架型入口页。
- 这些数字足以支撑“下垂控制是一次共享总入口”的页面定位。

## 与相关方法的关系

- [[adaptive-droop]]：讨论下垂系数的在线调整。
- [[hierarchical-control]]：说明一次下垂、二次恢复和能量管理的层级关系。
- [[inertia-control]]：关注虚拟惯量注入，不等同于静态下垂律。
- [[microgrid-control]]：给出微电网场景中的控制组合。
- [[grid-forming-inverter]]：给出下垂控制常见的设备级实现背景。
- [[frequency-control]]：说明下垂在系统频率支撑链条中的位置。

## 适用边界与失败模式

- 适用于希望在无高速通信条件下获得近似功率共享的并联系统。
- 线路阻抗不一致、$R/X$ 比显著、滤波器差异或测量偏差会导致共享误差。
- 单纯下垂控制会带来稳态频率或电压偏差，需要更慢层级恢复。
- 在强限流、保护动作或故障穿越场景中，下垂关系可能被电流限制或模式切换覆盖。

## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：说明构网型逆变器黑启动和下垂控制的应用背景。
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]：提醒外环共享与内环阻尼设计之间可能存在耦合。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：可作为与惯量增强控制对比的相关来源，但不应混写为同一种方法。
- [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]]：提供 coordinated droop 和多微电网初始化背景。

## 证据边界

当前页面只说明控制结构和适用边界，不宣称某组下垂参数“最优”或某场景必然稳定。所有性能结论都必须绑定网络阻抗、设备额定值、限流逻辑和具体算例。

## 开放问题

- 当前页尚未系统整理阻抗匹配、虚拟阻抗和功率解耦设计在下垂控制中的角色。
- 后续可继续补充“何时下垂足够、何时必须引入更高层恢复控制”的工程判断。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Control and Simulation of a Grid-Forming Inverter for Hybrid]] | 2021 |
| [[advancing-grid-forming-inverter-technology-comprehensive-pq-capability-and-perfo|Advancing Grid-Forming Inverter Technology: Comprehensive PQ]] | 2025 |
