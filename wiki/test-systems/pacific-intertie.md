---
title: "Pacific Intertie 场景入口"
type: test-system
tags: [pacific-intertie, hvdc, benchmark, interconnection, long-distance-transmission]
created: "2026-05-04"
updated: "2026-05-07"
---

# Pacific Intertie 场景入口

## 定义与边界

Pacific Intertie 通常指北美西部经典的长距离交直流互联系统场景，常被用作 HVDC、长距离输电和大系统稳定研究的 benchmark 或工程背景入口。在本 Wiki 中，本页作为场景入口，用于承接围绕该互联系统展开的控制、稳定性、保护和 EMT 扩展研究。

本页不是频变输电线路建模页，也不是任意大系统控制方法页。

## EMT 中的作用

该入口常用于：

- 说明长距离 HVDC/AC 互联系统如何被纳入 EMT 或混合仿真研究；
- 对比站级控制、故障恢复和系统稳定性分析方法在经典互联系统中的适用边界；
- 为 benchmark、HVDC 控制和大系统验证页提供工程背景。

## 常见用途

- 作为长距离 HVDC 互联系统 benchmark；
- 作为控制器、阻尼策略和故障恢复研究的工程背景；
- 作为与 Nelson River、Nordic 等其他大型系统场景的对照对象。

## 形式化表达

作为系统入口，其最小功率平衡关系可抽象为：

$$
P_{send} - P_{loss} = P_{receive}
$$

实际 EMT 研究通常还需要补充换流站控制、线路模型、保护和扰动脚本。

## 相关页面

- [[hvdc-control]]：站级和系统级控制背景。
- [[multi-terminal-dc]]：交直流互联系统与更一般直流网场景的对照背景。
- [[transient-stability-analysis]]：稳定性研究背景。
- [[model-verification-benchmark]]：benchmark 使用边界。
- [[large-scale-power-system]]：大规模系统主题背景。
- [[power-system-network]]：长距离互联系统的网络背景。

## 代表性来源

- [[published-in-iet-generation-transmission-distribution-27&28]]：经典互联系统相关背景。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：大型 HVDC benchmark 对照背景。
- [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc]]：长距离交直流互联系统控制研究背景。

## 证据边界

本页不写具体线路参数、功率等级或统一稳定性结论，只作为 Pacific Intertie 场景入口。

## 开放问题

- 当前页尚未区分“历史工程场景”与“论文中改造后的 benchmark 场景”之间的边界。
- 不同文献如何对 Pacific Intertie 进行 EMT 局部细化，后续应在测试系统页继续拆开。
