---
title: "PV-STATCOM 方法入口"
type: method
tags: [pv-statcom, pv, statcom, reactive-support, inverter-control]
created: "2026-05-04"
updated: "2026-05-07"
---

# PV-STATCOM 方法入口


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 -->|Nf1| N1
    N2[常见场景]
    N1 -->|Nf2| N2
    N3[形式化表达]
    N2 -->|Nf3| N3
    N4[与相关页面的关系]
    N3 -->|Nf4| N4
    N5[代表性来源]
    N4 -->|Nf5| N5
```


## 定义与边界

PV-STATCOM 通常指光伏逆变器在低辐照或非发电时段提供 STATCOM 式无功支撑的控制与建模方法入口。它关注的是“利用光伏并网变流器承担静止无功补偿功能”的场景边界，而不是一般链式 STATCOM 等效建模页。

本页讨论的是 PV-STATCOM 的系统级方法边界，不把链式 STATCOM 快速等效模型或无关调制算法直接写成 PV-STATCOM 方法本身。

## EMT 中的作用

在 EMT 仿真中，PV-STATCOM 方法主要用于：

- 研究光伏逆变器在无功支撑模式下的动态行为；
- 分析并网点电压恢复、无功调节和故障穿越能力；
- 作为光伏并网控制与传统 STATCOM 功能融合的场景入口；
- 连接光伏、并网逆变器和无功补偿类页面。

## 常见场景

- 白天发电与无功支撑协同运行；
- 夜间或低辐照条件下的纯无功补偿运行；
- 电压支撑与故障穿越场景；
- 与传统 STATCOM、SVC 或场站级控制的对比场景。

## 形式化表达

PV-STATCOM 的最小控制目标可抽象为：

$$
Q_{ref} \rightarrow Q_{inj}
$$

其真正难点在于光伏逆变器有功/无功容量边界、并网电压支撑和控制模式切换如何共同作用，而不只是一个无功参考量本身。

## 与相关页面的关系

- [[power-electronics-control]]：控制总入口。
- [[grid-connected-inverter]]：并网逆变器背景。
- [[renewable-integration]]：新能源接入上位背景。
- [[frequency-control]]：若与并网支撑联动，可作为相关背景。
- [[reactive-compensation-device]]：无功补偿装置背景。
- [[facts]]：FACTS 与补偿装置的上位背景。

## 代表性来源

- [[大功率链式statcom电磁暂态快速等效建模和误差评估]]：STATCOM 快速等效的相关背景。
- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：光伏并网与无功支撑控制背景。
- [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb]]：多端口电力电子站控和无功支撑背景。

## 证据边界

本页不写无来源的容量利用率、统一无功极限或最优运行模式。具体结论必须绑定光伏逆变器容量、控制配置和验证工况。

## 开放问题

- 当前页尚未继续拆分纯 PV-STATCOM 模式与光储联合无功支撑模式的边界。
- 并网规范与装置额定值如何限制无功支撑能力，后续仍需回到具体 source 页细化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
