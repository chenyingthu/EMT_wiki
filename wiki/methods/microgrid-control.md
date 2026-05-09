---
title: "微电网控制 (Microgrid Control)"
type: method
tags: [microgrid-control, islanded-operation, grid-forming, secondary-control, coordination]
created: "2026-05-05"
updated: "2026-05-06"
---

# 微电网控制 (Microgrid Control)


```mermaid
graph TD
    N0[微电网控制 (Microgrid…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[常见控制层]
    N0 --> N3
    N4[关键公式]
    N0 --> N4
    N5[与相关方法的关系]
    N0 --> N5
    N6[适用边界与失败模式]
    N0 --> N6
    N7[代表性来源]
    N0 --> N7
    N8[证据边界]
    N0 --> N8
```


## 定义与边界

微电网控制是面向孤岛和并网运行的小型交直流系统控制方法集合，涉及电压频率建立、并联系统功率共享、储能协调、并网切换和二次恢复等问题。它通常由多个层级和多个设备控制器协同完成。

本页讨论的是微电网运行控制结构，不把多频潮流算法、版权残片或任意 AC/DC 联合求解器误写成微电网控制方法。

## EMT 中的作用

在 EMT 仿真中，微电网控制常用于：

- 研究孤岛建立、黑启动和并网/离网切换；
- 分析多台逆变器、储能和分布式电源的共享与恢复；
- 评估故障穿越、限流、通信延迟和负荷扰动对局部系统稳定性的影响；
- 检查控制层与主电路、保护和能量管理之间的耦合。

## 常见控制层

- 一次控制：[[droop-control]]、[[inertia-control]] 或构网型电压源控制。
- 二次控制：频率/电压恢复，常与 [[distributed-control]] 结合。
- 更慢层级：功率分配、能量管理和经济运行。

## 关键公式

微电网控制并没有唯一公式，但一次共享常从下垂关系出发：

$$
\omega = \omega_0 - m_p (P - P^\star), \qquad
V = V_0 - n_q (Q - Q^\star)
$$

若存在二次恢复，则恢复层通过较慢控制量修正一次层参考，而不是直接替代一次层。

## 与相关方法的关系

- [[droop-control]]：微电网并联系统的一次共享基础。
- [[hierarchical-control]]：说明一次、二次和能量管理层级。
- [[distributed-control]]：适用于多节点协同恢复。
- [[offshore-wind-integration]]：虽不是微电网控制本身，但可作为多装置协调背景对比。

## 适用边界与失败模式

- 适用于需要同时处理设备级动态和系统级运行模式切换的小型系统。
- 微电网控制高度依赖设备类型、通信结构和储能约束，不能简单照搬输电级控制。
- 仅有稳态潮流或平均值分析通常不足以解释 EMT 级故障和切换瞬态。
- 若未显式建模保护、限流和控制模式切换，可能误判系统可恢复性。

## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：可作为构网型逆变器、储能和黑启动微电网控制的直接背景来源。
- [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]]：说明微电网运行点和多频/混合系统建模背景，但不是控制方法本身。
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]：可作为微电网并网装置局部控制与阻尼设计的相关来源。

## 证据边界

本页不写无来源的切换时间、共享误差或恢复速度结论。具体控制效果必须绑定系统拓扑、储能规模、通信结构和测试工况。
