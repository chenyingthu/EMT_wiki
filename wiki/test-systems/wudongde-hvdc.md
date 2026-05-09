---
title: "乌东德 HVDC 场景入口"
type: test-system
tags: [wudongde-hvdc, hvdc, benchmark, china, large-scale-system]
created: "2026-05-04"
updated: "2026-05-07"
---

# 乌东德 HVDC 场景入口

## 定义与边界

乌东德 HVDC 场景入口用于承接围绕乌东德特高压混合直流工程展开的系统建模、控制、保护和暂态分析问题。它是工程/benchmark 场景入口，不是某一篇变压器暂态实验或单一直流故障算法页。

本页讨论的是乌东德工程作为 HVDC 场景的边界，不替代一般 HVDC 控制页或直流保护页。

## EMT 中的作用

在 EMT 仿真中，这类工程场景主要用于：

- 作为大型混合直流工程的 benchmark 或案例背景；
- 对比控制、故障和暂态分析方法在实际工程约束下的表现；
- 连接工程级参数、控制结构和测试系统页面；
- 为中国大型直流工程与张北、鲁西等项目形成对照背景。

## 常见用途

- 作为混合直流工程案例背景；
- 作为控制器、故障恢复和工程参数验证背景；
- 作为大型交直流系统暂态仿真和对照 benchmark。

## 形式化表达

作为工程场景入口，其最小系统级关系可抽象为：

$$
P_{send} - P_{loss} = P_{receive}
$$

但实际工程研究还需要补充换流站控制、故障工况和系统级边界条件。

## 与相关页面的关系

- [[hvdc-control]]：HVDC 控制背景。
- [[dc-protection]]：直流故障与保护背景。
- [[model-verification-benchmark]]：工程 benchmark 使用边界。
- [[large-scale-power-system]]：大规模系统背景。
- [[zhangbei-dc-grid]]：另一类国内直流工程场景对照。

## 代表性来源

- [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc]]：国内大型直流工程控制背景。
- [[a-method-to-calculate-short-circuit-faults-in-high-voltage-dc-grids]]：直流故障与工程保护背景。
- [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]]：大型直流工程高频稳定背景。

## 证据边界

本页不写无来源的工程参数、统一稳定性结论或最优控制方案。具体结论必须绑定工程配置和验证工况。

## 开放问题

- 当前页尚未继续区分乌东德工程中的控制、保护和系统级验证分支。
- 工程级参数与公开论文中的简化模型之间的映射，后续仍需在测试系统页细化。
