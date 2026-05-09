---
title: "单机 PMSG 建模方法"
type: method
tags: [pmsg-single-unit, pmsg, wind-turbine, generator-modeling, converter-interface]
created: "2026-05-04"
updated: "2026-05-07"
---

# 单机 PMSG 建模方法

## 定义与边界

单机 PMSG 建模方法指围绕单台永磁同步发电机（PMSG）及其全功率变流器、滤波器和并网接口建立的 EMT 或机电暂态模型。它常作为风电机组、海上风电场或并网资源等值的基础单元。

本页讨论的是单机 PMSG 的建模边界，不把风电场级等值、海上集电网络或无关线路模型误写成单机 PMSG 方法。

## EMT 中的作用

在 EMT 仿真中，单机 PMSG 建模主要用于：

- 表达永磁同步发电机与背靠背变流器的接口动态；
- 分析并网、电压跌落和控制切换下的机组响应；
- 为风电场多机等值、实时仿真或并行 EMT 提供单机模块基础；
- 作为 PMSG 场站、海上风电场和并网资源研究的设备级入口。

## 常见模型层级

- 详细 EMT 模型：保留发电机、变流器、滤波器和控制器细节。
- 恒导纳或快速等效模型：面向实时仿真和大规模并行场景。
- 机电暂态模型：保留慢变量和关键能量通道，弱化高频开关细节。

## 关键公式

PMSG 的典型转矩和转速关系可围绕 d-q 轴模型组织，其最小抽象可写为：

$$
s = \frac{\omega_s - \omega_r}{\omega_s}
$$

但在单机 PMSG 场景中，真正重要的不只是发电机方程本身，而是其与全功率变流器、直流母线和并网控制的耦合。

## 与相关页面的关系

- [[dfig-offshore-wind-farm]]：说明 PMSG 与 DFIG 风场建模的边界。
- [[offshore-wind-integration]]：说明单机模型如何进入海上风电场场景。
- [[grid-connected-inverter]]：并网变流器接口背景。
- [[renewable-energy-integration]]：新能源接入的上位背景。
- [[power-electronics-control]]：单机 PMSG 与变流器控制耦合背景。
- [[lvrt-control]]：故障穿越与并网控制背景。

## 代表性来源

- [[fixed-admittance-modeling-method-of-pmsg-based-on-compensation-of-impedance-基于虚拟]]：PMSG 恒导纳 EMT 建模背景。
- [[直驱式风电机组机电暂态建模及仿真]]：直驱 PMSG 机电暂态建模背景。
- [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin]]：PMSG 单机模块进入大规模海上风电场的背景。

## 证据边界

本页不写无来源的最优控制参数、风机容量或统一稳定性结论。具体能力必须绑定机组结构、控制策略和验证工况。

## 开放问题

- 当前页尚未继续细分直驱 PMSG 与其他永磁机组接口结构的边界。
- 单机 PMSG 模型应保留到什么层级，后续仍需结合风电场研究目标判断。
