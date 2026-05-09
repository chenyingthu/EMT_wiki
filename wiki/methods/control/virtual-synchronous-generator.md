---
title: "虚拟同步发电机方法 (VSG)"
type: method
tags: [virtual-synchronous-generator, vsg, grid-forming, inertia-control, synchronization]
created: "2026-05-04"
updated: "2026-05-07"
---

# 虚拟同步发电机方法 (VSG)


```mermaid
graph TD
    subgraph S0[虚拟同步发电机方法 (VSG)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见分支]
        N3[关键公式]
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

虚拟同步发电机（Virtual Synchronous Generator, VSG）是构网型变流器中常见的一类控制方法，通过模拟同步发电机的惯量、阻尼和频率调节特性来提供电压与频率支撑。

本页讨论的是 VSG 作为构网控制方法的边界，不把光伏模型、一般频率控制页或无关线路公式误写成 VSG 方法页。

## EMT 中的作用

在 EMT 仿真中，VSG 方法主要用于：

- 表达构网型变流器的惯量、阻尼和同步支撑行为；
- 研究多 VSG 并联时的频率同步和功率振荡问题；
- 分析弱网、扰动和非理想通信条件下的构网稳定性；
- 作为 GFM 控制、惯量控制和频率控制页的核心设备级入口。

## 常见分支

- 单机 VSG：关注单台构网装置的惯量和阻尼特性；
- 多机并联 VSG：关注功率振荡、互阻尼和协同控制；
- 带一致性或自适应机制的 VSG：关注并联系统中的同步和鲁棒性；
- 与 RMS/相量适用性分析耦合的 VSG：关注模型层级边界。

## 关键公式

VSG 的最小摆动关系可抽象写为：

$$
J\frac{d\omega}{dt}=P_m-P_e-D(\omega-\omega_0)
$$

其中 $J$ 表示等效惯量，$D$ 表示阻尼，$P_m$ 与 $P_e$ 分别表示机械等效输入和电磁等效输出。VSG 的关键不在单个公式，而在于这些量如何通过变流器控制器被实现。

## 与相关页面的关系

- [[frequency-control]]：系统级频率控制背景。
- [[inertia-control]]：惯量支撑背景。
- [[grid-forming-converters-sufficient-conditions-for-rms-modeling]]：VSG 与模型层级边界相关背景。
- [[power-electronics-control]]：控制总入口。
- [[phase-locked-loop]]：VSG 与基于 PLL 的跟网同步形成对照。

## 代表性来源

- [[基于一致性算法的多虚拟同步机功率振荡协调抑制]]：多 VSG 并联协调的直接背景。
- [[grid-forming-converters-sufficient-conditions-for-rms-modeling]]：VSG 与 RMS/EMT 边界背景。
- [[改善暂态稳定性的多构网型变换器频率同步协同控制]]：多构网型频率同步与协同控制背景。

## 证据边界

本页不写无来源的最优惯量、统一阻尼参数或所有弱网场景下的稳定性结论。具体能力必须绑定控制结构、网络强度和验证工况。

## 开放问题

- 当前页尚未继续拆分单机 VSG、多机并联 VSG 和带一致性协调 VSG 的细边界。
- VSG 与其他 GFM 路线的适用性差异，后续仍需在相邻页面中继续细化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
| [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat|Transient Electromagnetic Power Compensation‐Based Adaptive ]] | 2025 |
