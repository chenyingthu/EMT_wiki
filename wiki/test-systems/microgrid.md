---
title: "微电网场景入口"
type: test-system
tags: [microgrid, scenario-entry, test-system, distributed-energy]
created: "2026-05-05"
updated: "2026-05-06"
---

# 微电网场景入口


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 -->|Nf1| N1
    N2[主要场景分支]
    N1 -->|Nf2| N2
    N3[形式化表达]
    N2 -->|Nf3| N3
    N4[验证共识]
    N3 -->|Nf4| N4
    N5[相关页面]
    N4 -->|Nf5| N5
```


## 定义与边界

微电网在本 Wiki 中更适合作为系统场景入口，而不是单一方法页。它通常涉及孤岛/并网运行、分布式电源、储能、控制层级和保护协同。本页用于承接围绕微电网场景展开的 EMT 研究，而不重复正式控制方法页内容。

## EMT 中的作用

该入口常用于：

- 组织微电网运行模式切换和控制研究；
- 连接储能、逆变器、微电网控制和测试系统页面；
- 作为微电网 benchmark 或案例场景入口。

## 主要场景分支

在本 Wiki 的证据范围内，微电网至少可以分成 3 类常见 EMT 场景：

1. 交流微电网：关注下垂控制、同步、保护和孤岛切换。
2. 直流微电网：关注变流器、高频器件、HIL 和实时仿真。
3. 混合 AC/DC 微电网：关注互联变流器、不同频率子网和统一初始化。

这 3 类场景共用“分布式电源聚合、小范围供电网络、可孤岛运行”这些属性，但模型边界、状态变量和验证工具明显不同，因此本页只做场景汇总，不替代具体控制或测试系统页。

## 形式化表达

把微电网作为 EMT 场景时，其最小抽象可以写成一个带运行模式的局部网络：

$$
\mathcal{M}=\big(\mathcal{N},\,\mathcal{S},\,\mathcal{C},\,m\big)
$$

其中 $\mathcal{N}$ 表示网络和负荷，$\mathcal{S}$ 表示分布式电源与储能，$\mathcal{C}$ 表示控制和保护层，$m\in\{\text{grid-connected},\ \text{islanded}\}$ 表示运行模式。对 EMT 来说，关键不在于“微电网”这个名字，而在于模式切换、接口变流器和局部控制如何改变瞬时电压、电流和能量交换。

## 验证共识

现有来源能稳定支持的共识包括：

- 微电网经常被作为 EMT 详细仿真对象，而不是仅用相量模型处理。
- FPGA、HIL 和 faster-than-real-time 平台是微电网研究中的高频验证环境。
- 混合 AC/DC 多微电网的初始化问题需要统一潮流或 MANA 类框架，而不仅是普通单频潮流。
- 具体结论必须绑定场景，例如 DC railway microgrid、multi-microgrid 或三变流器实验微电网，不能直接横向泛化。

## 相关页面

- [[microgrid-control]]：正式控制方法页。
- [[microgrid-test-system]]：测试系统背景。
- [[distributed-control]]：多节点协调背景。
- [[droop-control]]：一次共享控制背景。
- [[hardware-in-loop]]：微电网常见验证方式。
- [[hybrid-simulation]]：交流主网与微电网分区仿真背景。
- [[grid-forming-inverter]]：构网型设备背景。
- [[energy-storage-system]]：储能在微电网中的角色背景。

## 代表性来源

- [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]]：微电网系统建模背景。
- [[fpga-based-sub-microsecond-level-real-time-simulation-for-microgrids-with-a-netw]]：微电网实时仿真背景。
- [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode]]：微电网/直流微网 HIL 背景。
- [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of]]：多微电网与 faster-than-real-time 场景背景。

## 量化线索

- 当前代表性来源覆盖至少 3 类验证环境：潮流初始化、FPGA 实时仿真、HIL/FTRT 仿真。
- 当前引用的代表性来源中，可明确识别的微电网系统规模至少包括 `2` 个 ACMG、`1` 个 DCMG 和 `2` 个互联变流器的多微电网算例。
- 实时仿真证据中可直接见到的时间尺度包括 `380 ns` 级子微秒步长和 `1 ns` 级器件特征重构步长。
- 这些数字说明微电网场景横跨从系统级初始化到器件级超快暂态，不应由单一方法页覆盖。

## 证据边界

本页不写统一控制策略或参数结论，只作为微电网场景入口。

## 开放问题

- 微电网入口后续是否应拆成“交流微电网”“直流微电网”“多微电网”三个子入口页？
- 当前入口页尚未系统汇总保护、能量管理和模式切换验证指标，后续可沿来源继续补齐。
