---
title: "风电场-HVDC 接口场景入口"
type: test-system
tags: [wind-farm-hvdc, wind-farm, hvdc, offshore-wind, grid-integration]
created: "2026-05-04"
updated: "2026-05-07"
---

# 风电场-HVDC 接口场景入口

## 定义与边界

风电场-HVDC 接口场景入口用于承接风电场通过 HVDC 送出或与 HVDC 网络耦合时的建模、控制、保护和系统协调问题。它关注的是“风电场与 HVDC 接口”的系统级边界，而不是单篇关于接地系统、线路模型或局部算法的残片。

本页讨论的是风电场与 HVDC 之间的接口场景，不替代单机风机模型页或一般 HVDC 控制页。

## EMT 中的作用

在 EMT 仿真中，这类场景主要用于：

- 组织风电场、集电网络、送出换流站和主网接口的系统级模型；
- 分析海缆、升压站、送端控制和受端控制的耦合；
- 评估故障、弱网和送出系统约束下的动态响应；
- 作为海上风电并网和 MTDC 场景之间的中间入口。

## 常见场景

- 海上风电场经 VSC-HVDC 送出；
- 大规模风电场与直流枢纽或多端直流网连接；
- 风电场并网控制与 HVDC 站级控制联动；
- 风电场故障穿越与直流保护/恢复协同。

## 形式化表达

该场景的系统级最小关系可抽象写为：

$$
P_{farm} - P_{loss} = P_{dc}
$$

但对 EMT 来说，关键不只是功率平衡，而是风电场控制、集电网络和 HVDC 接口如何共同决定暂态响应。

## 与相关页面的关系

- [[offshore-wind-integration]]：海上风电并网上位背景。
- [[multi-terminal-dc]]：更一般的直流网场景背景。
- [[offshore-hvdc-hub]]：海上直流枢纽场景背景。
- [[wind-farm-hvdc]]：当前页自身聚焦风场与 HVDC 接口，而不是一般风场建模。
- [[dfig-offshore-wind-farm]]：风场内部建模背景。
- [[hvdc-control]]：送出换流站控制背景。

## 代表性来源

- [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag]]：风场与 HVDC/送出场景的相关背景。
- [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f]]：风场 EMT 建模背景。
- [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15]]：多端 HVDC 与风电场关联背景。

## 证据边界

本页不写无来源的风场规模、送出容量、统一故障性能或最优控制方案。具体结论必须绑定风机类型、送出拓扑和验证工况。

## 开放问题

- 当前页尚未继续拆分“海上风电经双端 HVDC 送出”和“风电场并入多端直流网”两类场景。
- 风场内部等值与送出接口等值的边界，后续仍需在测试系统页和风场页中继续细化。
