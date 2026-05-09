---
title: "Dc Pfc"
type: method
tags: [dc-pfc]
created: "2026-05-04"
---

# DC-PFC


```mermaid
graph LR
    N0[定义与边界]
    N1[概念边界]
    N0 -->|Nf1| N1
    N2[核心机制]
    N1 -->|Nf2| N2
    N3[链接用法]
    N2 -->|Nf3| N3
    N4[代表性来源]
    N3 -->|Nf4| N4
    N5[证据边界]
    N4 -->|Nf5| N5
```


## 定义与边界

DC-PFC 是一个需要消歧的缩写入口。在现有来源中，它一方面可能作为直流电网中的 DC power flow controller / 直流潮流控制设备出现，另一方面也容易被误混入 AC/DC 功率因数校正 PFC。当前页面只作为受控入口，避免把这两类对象扩展成同一篇完整方法页。

## 概念边界

- 若语境是直流电网设备或国产 EMT 平台的模块化电力电子装备清单，DC-PFC 应理解为直流潮流控制相关设备，并与 [[mtdc-model]]、[[dc-protection]] 和 [[dc-fcl]] 区分。
- 若语境是交错图腾柱 PFC、Boost PFC 或车载充电器，应链接具体来源页，而不是把它写成直流潮流控制器。
- 若语境是 FACTS 或 UPFC 的交流潮流控制，应转向 [[facts]]、[[upfc-model]] 或相关来源，不应使用 DC-PFC 缩写。
- 本页不保留旧页面中线路电报方程、通用 EMT 作用、泛化未来方向和无来源量化说法。

## 核心机制

DC 潮流控制器的核心功能是在直流网络中调节线路功率分配。以串联型 DC-PFC 为例，其注入电压 $\Delta V$ 与线路功率 $P_{ij}$ 的关系为：

$$
P_{ij} = rac{V_i(V_j + \Delta V - V_i)}{R_{ij}}
$$

其中 $V_i, V_j$ 为节点 $i, j$ 的直流电压，$R_{ij}$ 为线路电阻，$\Delta V$ 为 PFC 注入的串联电压。当 $\Delta V$ 可正可负时，线路功率可在正常运行范围外双向调节，实现对多端直流网络潮流的主动控制。

## 链接用法

只有在原文或页面确实使用 `DC-PFC` 缩写且需要英文锚点时链接 [[dc-pfc]]。讨论单相或图腾柱功率因数校正时，优先链接 [[a-bidirectional-interleaved-totem-pole-pfc-based-integrated-on-board-charger-for]] 或 [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct]]。讨论 MMC-UPFC 或交流潮流控制时，使用 [[mmc-upfc电磁-机电混合仿真技术研究]] 或 [[upfc-model]]。

## 代表性来源

- [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix]]：在平台综述中把 DC-PFC 与 DCCB、DC-FCL 并列为模块化电力电子装备；该来源不提供 DC-PFC 单独性能验证。
- [[a-bidirectional-interleaved-totem-pole-pfc-based-integrated-on-board-charger-for]]：代表 AC/DC 功率因数校正语境，应避免被误归入直流潮流控制设备。
- [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct]]：代表 Boost PFC 动态相量建模语境，适合 PFC 控制和建模说明。
- [[mmc-upfc电磁-机电混合仿真技术研究]]：代表交流潮流控制和 UPFC 混合仿真语境，不应与 DC-PFC 缩写混写。

## 证据边界

当前 Wiki 证据不足以把 DC-PFC 写成一个已充分定义的独立方法页。使用本入口时必须说明缩写指向、设备对象和来源语境；不得把 AC/DC 功率因数校正、直流潮流控制和 UPFC 控制指标混用。
