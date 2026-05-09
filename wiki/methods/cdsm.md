---
title: "双钳位子模块方法 (CDSM)"
type: method
tags: [cdsm, clamp-double-submodule, mmc, fault-tolerant, electrothermal]
created: "2026-05-05"
updated: "2026-05-06"
---

# 双钳位子模块方法 (CDSM)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[常见关注点]
    N1 --> N2
    N3[关键公式]
    N2 --> N3
    N4[与相关方法的关系]
    N3 --> N4
    N5[适用边界与失败模式]
    N4 --> N5
    N6[代表性来源]
    N5 --> N6
    N7[证据边界]
    N6 --> N7
```


## 定义与边界

CDSM（Clamp Double Submodule）通常指 MMC 或相关多电平换流器中的双钳位子模块结构及其建模方法。它常与故障容错、器件级热应力和桥臂控制相关。对应的方法问题是如何在 EMT 中表示该类子模块的电气状态、热状态和与系统级模型的耦合。

本页讨论的是 CDSM 子模块及其建模边界，不把 MPSoC 电热实时仿真框架本身当成“CDSM 方法”的全部内容。

## EMT 中的作用

在 EMT 仿真中，CDSM 方法主要用于：

- 表达故障容错型子模块的多状态行为；
- 研究电气动态和器件热应力的耦合；
- 支撑从系统级平均值到器件级电热模型的分层分析；
- 比较不同子模块拓扑在桥臂控制和故障场景中的表现。

## 常见关注点

- 子模块可输出状态和故障后电流路径；
- 器件损耗到结温的电热映射；
- 与桥臂排序、均压和容错控制的耦合；
- 从详细开关到等效模型的层级切换。

## 关键公式

CDSM 的具体方程依赖拓扑，但其电热耦合通常可抽象为：

$$
C_{th}\frac{dT_j}{dt} = P_{loss} - \frac{T_j - T_{amb}}{R_{th}}
$$

其中 $T_j$ 为结温，$P_{loss}$ 为器件损耗。这个表达说明 CDSM 研究往往不仅关注桥臂电压电流，还关注器件热状态。

## 与相关方法的关系

- [[half-bridge-submodule]]、[[fbsm]]：作为其他子模块拓扑的对照背景。
- [[mbsm]]：统一子模块表示框架的相关背景。
- [[mmc-model]]：整机层应用背景。
- [[real-time-simulation]]：器件级电热耦合在实时验证中的相关背景。

## 适用边界与失败模式

- 适用于需要研究子模块拓扑细节和热应力问题的场景。
- 若只保留系统级等效，可能无法解释器件热失衡和容错行为。
- 具体 CDSM 拓扑差异较大，不能泛化为单一标准结构。

## 代表性来源

- [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-]]：说明 CDSM 电热耦合与实时背景。
- [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法]]：说明双钳位子模块 EMT 建模背景。
- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-]]：说明详细与平均值耦合背景。

## 证据边界

本页不写无来源热阻参数、损耗极限或实时性能结论。具体结果必须绑定子模块结构和测试工况。

## 开放问题

- 当前页尚未细分不同 CDSM 拓扑之间的输出状态和控制自由度差异。
- 电热耦合模型应做到多细，仍需结合目标场景和计算预算判断。
