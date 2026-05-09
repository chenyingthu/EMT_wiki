---
title: "直流断路器方法 (DCCB)"
type: method
tags: [dccb, dc-circuit-breaker, hvdc-protection, fault-isolation]
created: "2026-05-05"
updated: "2026-05-06"
---

# 直流断路器方法 (DCCB)

## 定义与边界

直流断路器（DC Circuit Breaker, DCCB）方法是指在直流故障发生后，通过机械开断、半导体换流、能量吸收和电压建立过程实现故障电流切除的建模与分析方法。它关注的是 DCCB 的类型、工作机理和与保护/网络的配合，而不是具体 HIL 实时仿真平台或某一个诺顿等效建模技巧本身。

## EMT 中的作用

在 EMT 仿真中，DCCB 方法主要用于：

- 表达故障电流上升、限流、换流和能量耗散过程；
- 研究 DCCB 动作时间与直流保护判据的配合；
- 比较机械式、混合式和全固态方案的建模边界；
- 分析 DCCB 对多端直流网络拓扑恢复和暂态稳定的影响。

## 常见类型

- 机械式 DCCB：损耗低，但开断速度较慢。
- 混合式 DCCB：机械支路与半导体支路配合，常用于兼顾速度与损耗。
- 固态 DCCB：动作快，但通态损耗和成本通常更高。

## 典型动作链

无论具体拓扑如何，DCCB 的 EMT 模型通常都要回答 4 个动作阶段：

1. 故障电流建立；
2. 电流转移或限流；
3. 主开断与能量吸收；
4. 隔离完成后的电压恢复。

不同类型的断路器，差异主要体现在“由谁承担电流转移”和“能量在哪里耗散”。

## 关键公式

DCCB 建模常围绕故障电流限制和能量吸收组织，例如：

$$
W_{abs} = \int v_{MOV}(t)\, i(t)\, dt
$$

该式表示故障切除过程中能量吸收器件承受的能量。对 EMT 研究而言，关键不是单一公式，而是 DCCB 动作序列、主支路/转移支路切换以及与网络电感电容的耦合。

## 与相关方法的关系

- [[dc-protection]]：决定何时启动 DCCB 动作。
- [[cl-dccb]]：电流限制型断路器是 DCCB 的一种特定路线。
- [[multi-terminal-dc]]：DCCB 在多端直流网络中承担选择性隔离作用。
- [[offshore-hvdc-hub]]：海上直流枢纽是 DCCB 需求较强的应用背景。
- [[cigre-b4-dc-grid]]：提供典型直流电网与保护测试场景入口。

## 适用边界与失败模式

- 适用于需要选择性切除直流故障的 HVDC 或 MTDC 场景。
- 若电流限制不足，故障电流上升过快会超出半导体或吸能器件能力。
- 若保护判据、动作时序和网络参数不匹配，可能导致误动、拒动或能量超限。
- 单一 DCCB 模型不能替代整个保护-控制-网络闭环验证。

## 代表性来源

- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]：说明 DCCB 与实际控制器、实时平台和直流电网闭环验证的场景。
- [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran]]：说明 DCCB 与行波保护/故障区段识别的相关背景。
- [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix]]：可作为国内直流断路与 EMT 装备发展背景来源。

## 证据边界

本页不写无来源开断时间、通态损耗或能量吸收极限。具体性能必须绑定断路器拓扑、网络参数和保护配合方案。

## 开放问题

- 当前页尚未把机械式、混合式和固态 DCCB 的验证指标拆开比较。
- 后续可继续补充 DCCB 与保护采样、站控和网络恢复的协同边界。
