---
title: "DFIG 海上风电场建模方法"
type: method
tags: [dfig-offshore-wind-farm, dfig, offshore-wind, wind-farm, model]
created: "2026-05-05"
updated: "2026-05-06"
---

# DFIG 海上风电场建模方法


```mermaid
graph TD
    subgraph S0[DFIG 海上风电场建模方法]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见组成]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[代表性来源]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

该方法页用于描述以双馈感应发电机（DFIG）为核心的海上风电场 EMT 建模路线。它关注风机、电气集电系统、并网换流器和控制器在海上风电场场景中的组合，而不是一般海上风电并网入口。

## EMT 中的作用

在 EMT 仿真中，DFIG 海上风电场建模常用于：

- 研究风机群、集电网络和并网点之间的动态耦合；
- 分析 DFIG 控制、转差和直流侧接口对风电场响应的影响；
- 为海上风电场大规模并行 EMT 研究提供对象边界。

## 常见组成

- DFIG 风机及其转子侧/网侧控制器；
- 场内集电网络与海缆送出链路；
- 升压站、并网点及必要时的 HVDC 送出接口；
- 场站级有功、无功和故障穿越协调逻辑。

## 关键公式

DFIG 的转差关系常写为：

$$
s = \frac{\omega_s - \omega_r}{\omega_s}
$$

其有功/转子侧功率关系在不同等效层级下会有不同写法，但 EMT 研究通常更关心控制器与并网接口的动态耦合，而不仅是单个功率公式。

## 与相关方法的关系

- [[offshore-wind-integration]]：更上位的海上风电并网场景页。
- [[ibr]]：逆变器型资源建模背景。
- [[wind-farm-hvdc]]：若采用 HVDC 送出，可作为相关背景。
- [[lvrt-control]]：风电并网故障穿越背景。
- [[microgrid-control]]：多设备协调控制的相关背景。
- [[dfig-model]]：设备级 DFIG 模型背景。

## 代表性来源

- [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin]]：大规模海上风电场建模和并行 EMT 背景。
- [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f]]：DFIG 风电场 EMT 建模背景。
- [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag]]：高效/实时背景来源。

## 证据边界

本页不写无来源功率等级、集电规模或稳定裕度结论，必须绑定具体风电场场景。

## 开放问题

- DFIG 场站与全功率变流器场站的 EMT 建模边界仍需在相邻页面中继续明确。
- 当前页尚未展开海缆、升压站和送出方式变化对模型层级选择的影响。
