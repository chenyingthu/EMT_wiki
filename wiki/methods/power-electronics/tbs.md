---
title: "晶闸管旁路开关方法入口 (TBS)"
type: method
tags: [tbs, thyristor-bypass-switch, bypass-protection, mmc-upfc, protection]
created: "2026-05-04"
updated: "2026-05-07"
---

# 晶闸管旁路开关方法入口 (TBS)


```mermaid
graph TD
    subgraph S0[晶闸管旁路开关方法入口 (TBS)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见场景]
        N3[形式化表达]
        N4[与相关页面的关系]
        N5[代表性来源]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

TBS 在当前 Wiki 语境中主要指 Thyristor Bypass Switch，即用于在故障或异常工况下快速旁路主换流器支路的晶闸管旁路开关方法入口。它常见于 MMC-UPFC、柔性补偿和快速保护切换场景。

本页讨论的是 TBS 作为旁路保护和设备保护手段的边界，不把一般输电线路模型或无关控制策略误写成 TBS 方法。

## EMT 中的作用

在 EMT 仿真中，TBS 方法主要用于：

- 在故障冲击或异常电流下快速旁路主换流器支路；
- 研究旁路动作时序与主电路保护协同；
- 分析主支路、旁路支路和故障电流之间的交互；
- 作为 MMC-UPFC 等装置保护与恢复场景的入口页。

## 常见场景

- MMC-UPFC 串联支路故障保护；
- 故障冲击电流的快速旁路与隔离；
- 主开关未完全承受故障应力前的保护切换；
- 与 DCCB、站级控制和保护逻辑协同动作。

## 形式化表达

TBS 的最小动作目标可抽象写为：

$$
i_{main} \rightarrow i_{bypass}
$$

即在满足触发条件后，把主支路电流尽快转移到旁路支路，以保护主换流器或串联装置。

## 与相关页面的关系

- [[dccb]]：故障开断与旁路动作的相关背景。
- [[dc-protection]]：保护判据与动作逻辑背景。
- [[mmc-upfc电磁-机电混合仿真技术研究]]：TBS 工程应用的直接来源背景。
- [[power-electronics-control]]：站级控制与动作协调背景。
- [[upfc-model]]：串并联柔性补偿装置背景。
- [[protection-system]]：保护系统上位背景。

## 代表性来源

- [[mmc-upfc电磁-机电混合仿真技术研究]]：TBS 在 MMC-UPFC 工程中的直接背景。
- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]]：旁路与混合仿真保护逻辑的相关背景。
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]：快速保护动作与电磁暂态验证背景。

## 证据边界

本页不写无来源的统一动作时间、保护成功率或适用于所有装置的旁路策略。具体结论必须绑定装置拓扑、保护逻辑和验证工况。

## 开放问题

- 当前页尚未继续细分 TBS 在 MMC-UPFC、STATCOM 或其他柔性装置中的不同作用。
- 旁路动作与主保护、站控之间的协调边界，后续仍需在相邻页面中继续细化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[mmc-upfc电磁-机电混合仿真技术研究|MMC-UPFC电磁-机电混合仿真技术研究]] | 2019 |
