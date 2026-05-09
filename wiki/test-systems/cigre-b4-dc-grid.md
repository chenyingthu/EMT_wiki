---
title: "CIGRE B4 直流电网场景入口"
type: test-system
tags: [cigre-b4-dc-grid, cigre-b4, dc-grid, benchmark, mtdc]
created: "2026-05-05"
updated: "2026-05-06"
---

# CIGRE B4 直流电网场景入口


```mermaid
graph TD
    subgraph S0[CIGRE B4 直流电网场景入口]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[形式化表达]
        N3[关键关系]
        N4[代表性来源]
        N5[证据边界]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

CIGRE B4 直流电网通常指 CIGRE B4 工作组提出或沿用的多端直流系统参考拓扑、设备配置和研究场景。在 EMT Wiki 中，本页作为方法/案例入口，用于承接围绕该类参考直流电网展开的建模、初始化和保护研究。

本页不是单篇论文摘要，也不是通用 MTDC 控制方法页。它更接近“参考直流电网场景入口”，用于把多篇相关工作组织到同一个可比较的系统背景下。旧有的 `cigre-b4` 和 `cigre-b4-57` 方法页均已并入本页；后续遇到 CIGRE B4、B4-57、BM4 等名称时，应优先回到具体来源核对拓扑和参数，不再在 `methods/` 下维护并列入口。

## EMT 中的作用

该入口常用于：

- 统一描述多端直流系统测试拓扑；
- 比较不同控制、初始化和保护方法在同类直流网中的表现；
- 说明 grid-forming VSC、故障隔离和直流网络初始化问题的共同背景；
- 为 [[multi-terminal-dc]]、[[dc-protection]] 和 [[hvdc-control]] 提供系统级案例入口。

## 形式化表达

作为参考直流电网场景入口，其最核心的形式化关系通常不是某一设备公式，而是多站直流网络的测试约束，例如：

$$
\mathbf{Y}_{dc}\mathbf{v}_{dc} = \mathbf{i}_{inj}
$$

该表达强调 CIGRE B4 直流电网研究通常围绕多端网络、站间注入和控制/保护场景组织，而不是围绕单一设备局部方程组织。

## 关键关系

- [[multi-terminal-dc]]：描述多端直流网络的一般方法边界。
- [[hvdc-control]]：描述站级控制结构。
- [[dc-protection]] 和 [[dccb]]：描述故障检测与开断路径。
- [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]]：说明相关初始化问题的代表来源。
- [[cigre-hvdc-benchmark]]：LCC-HVDC benchmark 页面；不要与本页的多端直流/VSC-HVDC 场景混同。

## 代表性来源

- [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]]：说明 MTDC 系统中构网型 VSC 的 EMT 初始化背景。
- [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient]]：提供并网变流器模型选择与系统级表现的相关背景。
- [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran]]：提供直流电网故障与保护背景。
- [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte]]：页面证据中出现 CIGRE B4-57 四端 MMC-HVDC 系统验证语境。

## 证据边界

本页只作为 CIGRE B4 直流电网场景入口，不写固定参数、节点数或统一测试标准，除非具体来源已明确给出。
