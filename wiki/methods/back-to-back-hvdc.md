---
title: "Back To Back Hvdc"
type: method
tags: [back-to-back-hvdc]
created: "2026-05-04"
---

# Back To Back Hvdc

## 定义与边界

Back-to-back HVDC 是两端换流器位于同一站点或短距离直流侧相连、用于异步交流系统互联或功率可控交换的 HVDC 结构。它可以采用 LCC、VSC 或 MMC 换流技术；关键特征是直流侧不承担长距离输电线路功能，而主要作为两个交流系统之间的可控电力电子接口。

本页作为简洁方法入口，收敛原先由批量模板混入的 Nelson River HIL、多速率仿真和 LCC 片段。具体拓扑、额定值、控制方式和验证指标必须回到对应来源或测试系统页。

## 核心机制

Back-to-back HVDC 的核心功能是实现两个异步交流系统之间的可控有功功率交换。忽略换流器损耗时，功率传输关系可简化为：

$$
P = V_{dc} I_{dc}, \quad Q_1 = f(V_1, \delta_1, \text{modulation}), \quad Q_2 = f(V_2, \delta_2, \text{modulation})
$$

其中 $P$ 为直流传输有功功率，$V_{dc}$ 和 $I_{dc}$ 为直流侧电压电流，$Q_1, Q_2$ 为两端换流站与交流系统交换的无功功率。实际控制中，有功由整流侧定电流或定功率控制决定，无功由两端换流器分别独立调节；$P$ 的稳态值受换流器容量和直流侧电压运行范围约束。

## 概念边界

- 与 [[hvdc-control]] 的关系：back-to-back HVDC 是系统结构；HVDC 控制是站级控制方法集合。
- 与 [[vsc-hvdc]] 的关系：VSC-HVDC 可包含点对点、多端或背靠背结构，本页只讨论背靠背结构语义。
- 与 [[multi-terminal-dc]] 的关系：MTDC 强调三个及以上换流站的直流网络协调；back-to-back 通常是两端接口。
- 与 [[mmc-21-level-hvdc]] 的关系：该测试系统可包含背靠背结构，但测试系统参数不应自动外推为本页通用参数。

## 链接用法

当句子强调“异步交流系统通过短直流环节互联”时，可链接本页。若讨论控制律、换流器模型、直流保护或多端直流网络，应直接链接 [[hvdc-control]]、[[converter-station-inverter]]、[[dc-protection]] 或 [[multi-terminal-dc]]。

## 代表性来源

- [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems]]：可作为 HVDC/FACTS 暂态分析背景来源。
- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]：可作为 VSC-HVDC/MMC 建模背景来源；其结论不等同于所有背靠背站。
- [[mmc-21-level-hvdc]]：说明 MMC-HVDC 测试系统中可出现背靠背运行结构。

## 证据边界

当前页不保留无来源的精度、实时性、固定电压等级或统一 LCC 表达。LCC 与 VSC/MMC 背靠背站的主电路、控制和故障行为差异较大，任何性能判断都必须绑定具体换流器类型和算例。
