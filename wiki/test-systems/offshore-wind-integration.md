---
title: "海上风电并网场景入口 (Offshore Wind Integration)"
type: test-system
tags: [offshore-wind-integration, wind-farm, hvdc, grid-integration, renewable]
created: "2026-05-05"
updated: "2026-05-06"
---

# 海上风电并网场景入口 (Offshore Wind Integration)

## 定义与边界

海上风电并网场景入口是指围绕海上风电场集电网络、风机接口、升压与送出系统、HVDC/交流并网方式以及控制协调建立的系统级场景。它关注的是“海上风电接入电网的系统级组织与接口问题”，而不是任意数值积分算法或通用 EMT 求解器。

## EMT 中的作用

在 EMT 仿真中，海上风电并网方法主要用于：

- 研究大规模风机并联、集电网络和送出系统的暂态响应；
- 分析海缆、升压平台、并网换流器和陆上电网之间的接口耦合；
- 评估故障、弱网、电压恢复和控制交互风险；
- 支撑海上风电场与 VSC-HVDC、储能或构网控制的联合建模。

## 主要环节

- 风机与变流器模型选择；
- 集电网络与海缆建模；
- 升压和送出系统建模；
- 并网控制、故障穿越和站级协调。

## 常见场景

- 交流集电加交流送出；
- 交流集电加 VSC-HVDC 送出；
- 含储能或构网控制的海上风电场；
- 多风场汇集到海上直流枢纽的扩展场景。

## 关键公式

海上风电并网并没有单一公式，但在系统层面，常需要把并网点功率、风机侧控制和送出网络耦合起来：

$$
P_{farm} = \sum_{i=1}^{N} P_i - P_{loss}
$$

若经 HVDC 送出，风电场并网动态还需通过送端/受端控制和海缆/直流网络模型共同解释，不能只看单台风机或单个控制器。

## 与相关方法的关系

- [[wind-farm-hvdc]]：关注风电场与 HVDC 接口的特定场景。
- [[lvrt-control]]：海上风机并网控制中的故障穿越问题。
- [[hvdc-control]]：HVDC 送出场景下的站级控制框架。
- [[microgrid-control]]：虽然规模和目标不同，但可作为多装置协调控制的对比背景。
- [[power-system-network]]：海缆、集电网络和陆上接入系统的网络边界。
- [[renewable-energy-integration]]：提供更上位的新能源系统接入背景。

## 适用边界与失败模式

- 适用于研究风机群、集电系统和送出系统之间的动态耦合。
- 单台风机结果不能直接外推到大规模海上风电场。
- 海缆频变参数、集电拓扑和并网方式对 EMT 结果影响很大。
- 若忽略站级控制、并网规范或送出系统约束，可能高估风场支撑能力。

## 代表性来源

- [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin]]：说明大规模海上风电场 EMT 建模和并行求解背景。
- [[type-3-wind-turbine-generator-model-with-generic-high-level-control-for-electrom]]：说明风机接口和高层控制建模背景。
- [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources]]：说明大规模并网资源接入时的 EMT 计算组织问题。

## 证据边界

本页不写无来源的风场容量、可接入规模、暂态稳定裕度或最优送出方案。具体结论必须绑定风机类型、并网方式、海缆参数和测试工况。

## 开放问题

- 当前页尚未继续拆分海上风电并网中的“风机层”“场站层”“送出层”场景边界。
- 不同送出方式下的 EMT 建模层级选择，后续仍需结合具体 source 页细化。
