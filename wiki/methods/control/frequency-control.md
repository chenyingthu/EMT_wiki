---
title: "频率控制 (Frequency Control)"
type: method
tags: [frequency-control, primary-frequency-control, secondary-control, grid-forming, converter-control]
created: "2026-05-05"
updated: "2026-05-06"
---

# 频率控制 (Frequency Control)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[主要机制]
    N1 --> N2
    N3[主要分支]
    N2 --> N3
    N4[关键公式]
    N3 --> N4
    N5[验证共识]
    N4 --> N5
    N6[量化线索]
    N5 --> N6
    N7[与相关方法的关系]
    N6 --> N7
```


## 定义与边界

频率控制是维持系统频率在扰动后可接受范围内，并在不同时间尺度上恢复频率偏差的控制方法总称。在 EMT Wiki 中，它既包括同步机和传统电网中的频率支撑，也包括逆变器主导系统中的构网、下垂、虚拟惯量和二次恢复机制。

本页讨论的是“频率作为控制对象”的方法，不把动态频率扫描或阻抗测量工具误写为频率控制方法。

## EMT 中的作用

在 EMT 仿真中，频率控制用于：

- 分析负荷突变、故障切除和孤岛切换后的频率响应；
- 研究一次控制、惯量支撑和二次恢复之间的耦合；
- 评估并网逆变器、储能和同步机混合系统的频率协调；
- 验证限流、饱和、PLL 或构网逻辑对频率支撑的影响。

## 主要机制

频率控制常按时间尺度划分：

- 一次频率控制：快速抑制频率偏差，常见于 [[droop-control]] 和 [[inertia-control]]。
- 二次频率控制：消除稳态频率偏差，常与 [[distributed-control]] 或集中调度配合。
- 更慢层级：与 [[economic-dispatch]]、[[optimal-power-flow]] 或能量管理相关。

## 主要分支

结合当前 Wiki 页面和来源，频率控制至少可分成 3 类：

1. 同步机式频率控制：以机械功率、阻尼和调速器为主。
2. 逆变器式频率控制：以构网、下垂、虚拟惯量和储能支撑为主。
3. 协调恢复式频率控制：以二次控制、分布式恢复或调度参考更新为主。

这 3 类分支共享“频率是被控对象”，但量测方式、内部状态和约束条件不同。

## 关键公式

最简单的一次频率支撑可抽象为：

$$
\Delta P = -K_f \Delta \omega
$$

若采用摆动型或虚拟同步机框架，则频率动态常写为：

$$
J \frac{d\Delta \omega}{dt} = P_m - P_e - D \Delta \omega
$$

这里 $K_f$、$J$、$D$ 可能来自同步机调速器、储能逆变器或构网控制器，但其物理含义和约束条件并不完全相同，不能直接混用。

## 验证共识

现有来源和相邻页面能稳定支持的共识包括：

- 频率控制在 EMT 中关注的是扰动后的瞬时支撑和恢复过程，而不是单纯稳态功率分配。
- 逆变器主导系统里，频率控制往往与构网策略、限流和同步方式强耦合。
- 二次频率恢复不能只看控制律本身，还要看通信和能量约束。
- 在混合系统中，同步机、储能和逆变器的频率控制参数不能直接视为同构对象。

## 量化线索

- 当前页明确区分 `3` 个时间层级和 `3` 类主要控制分支。
- 当前最小动力学表达至少包含 `3` 个关键参数：$K_f$、$J$、$D$。
- 当前相关页面已覆盖不少于 `4` 条直接关联链路：下垂、自适应下垂、惯量控制、分层控制。
- 这些数字足以说明本页是系统级频率控制入口，而不是某个频率扫描工具的误归类页。

## 与相关方法的关系

- [[droop-control]]：频率偏差到有功调整的静态一次控制关系。
- [[adaptive-droop]]：根据运行状态在线调整频率支撑系数。
- [[inertia-control]]：通过等效惯量改善频率暂态。
- [[hierarchical-control]]：说明一次/二次频率控制的层级组织。

## 适用边界与失败模式

- 适用于研究频率偏差、功率支撑和恢复过程的系统级动态问题。
- 若系统由强 PLL 跟网逆变器主导，频率概念与同步机系统并不完全等价。
- 储能功率和能量约束会限制频率支撑持续时间。
- 通信延迟、限流和模式切换会改变理想频率控制律的有效性。

## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：说明构网型逆变器在频率建立与恢复中的背景场景。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：说明逆变器储能系统的频率暂态支撑可以通过惯量/补偿控制增强。
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：提醒频率测量与同步环节本身也会影响频率控制表现。
- [[dynamic-performance-of-embedded-hvdc-with-13&14]]：说明频率控制也可作为嵌入式 HVDC 协调策略的一部分。

## 证据边界

本页不直接宣称某种频率控制更优或更稳。具体性能必须绑定被控对象、网络强度、储能约束、测量方式和测试工况。

## 开放问题

- 当前页尚未系统拆分同步机调速器、构网逆变器和 HVDC 协调频控的验证指标。
- 后续可继续补充频率控制与 PLL、限流、黑启动之间的交互失效模式。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat|Transient Electromagnetic Power Compensation‐Based Adaptive ]] | 2025 |