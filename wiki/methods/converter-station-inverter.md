---
title: "换流站-逆变器 (Converter Station - Inverter)"
type: method
tags: [converter, inverter, hvdc, station, lcc, vsc]
created: "2026-05-02"
---

# 换流站-逆变器 (Converter Station - Inverter)

## 概述

换流站-逆变器页面说明 HVDC 换流站在逆变运行时如何把直流侧功率送入交流系统，以及 EMT 建模中需要保留哪些主电路、控制和网络接口。这里的“逆变器”不是单一拓扑：LCC 逆变器依赖交流系统换相和晶闸管触发；VSC 逆变器依赖自关断器件、调制和闭环控制；MMC 是工程 VSC-HVDC 中常见的多电平实现。

因此，本页是方法页而非设备参数手册。它不列无来源的容量、损耗、占地或固定角度范围，只说明建模流程、拓扑边界和证据使用方式。

## 建模对象与边界

| 类别 | LCC 逆变站 | VSC/MMC 逆变站 |
|------|------------|----------------|
| 功率器件 | 晶闸管 | IGBT/IGCT 或子模块开关 |
| 换相方式 | 依赖交流换相电压 | 自换相 |
| 关键控制量 | 触发角、直流电流、关断角 | dq 电流、功率/电压外环、调制信号 |
| 主要风险 | 换相失败、无功需求、交流故障敏感 | 直流故障、控制饱和、宽频振荡、保护闭锁 |
| 关联页面 | [[lcc-model]]、[[thyristor-control]]、[[extinction-angle-calculation]] | [[vsc-model]]、[[mmc-model]]、[[dual-loop-pi-controller]]、[[pll-model]] |

如果研究对象是普通光伏或储能并网逆变器，应优先查看 [[inverter-model]] 和 [[vsc-model]]。如果研究对象是 LCC-HVDC 受端换相失败，应优先查看 [[lcc-model]] 和 [[extinction-angle-calculation]]。

## EMT 建模流程

换流站逆变器的 EMT 建模一般包括：

1. 选择设备层级：详细开关、平均值模型、动态相量、端口等值或混合模型。
2. 建立交流侧接口：换流变压器、滤波器、交流网络等值、测量和同步信号。
3. 建立直流侧接口：直流线路、电抗器、电容、直流电压控制或直流电流约束。
4. 写清控制层：站控/极控、换流器控制、阀控、保护闭锁和限幅逻辑。
5. 明确网络耦合：节点导纳矩阵、受控源接口、固定导纳或拓扑分解。
6. 用目标工况验证：稳态、交流故障、直流故障、换相失败、闭锁/解锁或控制模式切换。

不同模型层级服务不同问题。详细开关模型适合阀级过程、保护动作和高频暂态；平均值模型适合系统级控制和多场景扫描；动态相量或混合仿真适合多时间尺度研究。任何“更快”“更准”的比较都必须绑定具体来源、测试系统、步长和对比基线。

## 关键公式

换流站逆变器在 EMT 网络中通常体现为端口电流、端口电压、控制状态和开关/调制状态之间的耦合关系。为了避免把具体工程控制器写成通用模型，本页只给出用于组织页面证据的抽象形式：

- 网络接口可写为 $\mathbf{Y}_{ac}\mathbf{v}_{ac}=\mathbf{i}_{net}+\mathbf{i}_{conv}$，其中 $\mathbf{v}_{ac}$ 是交流侧节点电压，$\mathbf{i}_{conv}$ 是换流器注入网络的等效电流。
- 直流侧功率平衡可用 $p_{ac}\approx v_{dc}i_{dc}-p_{loss}$ 表示，其中 $p_{loss}$ 只应在来源给出损耗模型或参数时展开。
- VSC/MMC 控制常写成 $\dot{\mathbf{x}}_c=f_c(\mathbf{x}_c,\mathbf{v}_{ac},v_{dc},\mathbf{r},\mathbf{m})$、$\mathbf{i}_{conv}=g_c(\mathbf{x}_c,\mathbf{v}_{ac},v_{dc},\mathbf{m})$，其中 $\mathbf{x}_c$ 是控制状态，$\mathbf{r}$ 是功率、电压或电流参考，$\mathbf{m}$ 是调制或开关状态。
- LCC 逆变侧还需要跟踪触发角 $\alpha$、关断角 $\gamma$、直流电流 $i_{dc}$ 和阀导通状态 $s_k$；换相失败分析不能只保留平滑功率方程。

这些表达用于说明变量接口和模型边界，不表示所有换流站都共享同一控制器、损耗模型或保护逻辑。若页面引用具体角度、限幅、功率额定值或阀级参数，必须回到对应 source 页或工程资料。

## LCC 逆变站

LCC 逆变站的核心机制是用晶闸管阀组在交流电压帮助下完成换相，控制目标通常围绕直流电流、直流功率和关断角裕度。逆变侧关断角不足时可能发生换相失败，表现为阀电流不能按预期转移、直流电压跌落和功率传输受扰。

[[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] 支持将 LCC 逆变器换相失败放入参数化平均值模型中处理，并使用自动故障检测识别故障开关。该证据说明平均值模型可以被扩展到部分换相失败研究，但不等于详细阀级保护或器件应力都可由平均值模型替代。

[[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con]] 支持另一类思路：保留晶闸管离散阀状态，通过拓扑分解减少求解开销。它适合说明 LCC 换相失败研究为什么不能只保留平滑功率方程。

## VSC/MMC 逆变站

VSC 或 MMC 逆变站通过自关断器件和调制策略生成交流电压，控制系统通常包含 [[pll-model]]、内环电流控制、外环功率/电压控制、直流电压控制、限流和保护。VSC 可以在一定范围内独立调节有功和无功，但该能力受额定容量、直流电压、交流电压、调制限制和控制模式影响。

[[a-vsc-hvdc-model-with-reduced-computational-intensity]] 将 VSC-HVDC 表示为受控源型动态平均值模型，用于降低系统级 EMT 仿真负担。[[dynamic-performance-of-embedded-hvdc-with-13&14]] 则在嵌入式 VSC-HVDC 场景中保留常规 dq 双环控制，并在有功参考层叠加频率相关补偿。后者的稳定性结论只支撑该 PSCAD 算例和嵌入式 HVDC 条件，不应写成所有 VSC-HVDC 的通用控制效果。

## 适用边界与失败模式

- LCC 逆变站需要足够交流换相电压和无功支撑；交流故障、谐波和弱系统会影响关断角。
- VSC/MMC 逆变站不发生 LCC 意义下的换相失败，但可能出现控制饱和、直流故障电流、闭锁、宽频振荡或 PLL 失稳。
- 平均值模型会削弱或删除开关谐波和阀级事件；用于保护或高频研究时必须说明缺失内容。
- 详细开关模型更接近阀级过程，但计算成本和步长约束较强。
- 多端或多馈入系统必须说明站间控制、通信、交流耦合网络和故障隔离策略。

## 代表性证据

| 来源 | 证据用途 | 边界 |
|------|----------|------|
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] | LCC 逆变器 PAVM 和换相失败检测 | 限于线换相逆变器平均值模型 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con]] | LCC 阀级拓扑状态与结构稳定求解 | 当前页面不复用未核验量化数字 |
| [[a-vsc-hvdc-model-with-reduced-computational-intensity]] | VSC-HVDC 受控源型动态平均值模型 | 限于论文中的 VSC、SPWM 和对比算例 |
| [[dynamic-performance-of-embedded-hvdc-with-13&14]] | 嵌入式 VSC-HVDC 的 dq 双环控制与附加频率控制 | 不外推到异步互联、多端或弱网电压稳定问题 |

## 与相关页面的关系

- [[thyristor-control]] 和 [[extinction-angle-calculation]] 支撑 LCC 逆变站。
- [[dual-loop-pi-controller]]、[[vector-control-model]] 和 [[pll-model]] 支撑 VSC/MMC 控制。
- [[converter-transformer-model]]、[[transmission-line-model]] 和 [[network-equivalent]] 决定站级接口。
- [[vsc-hvdc]] 是系统级主题页，讨论多站直流网络和应用边界。

## 开放问题

换流站逆变器页面后续需要按工程或论文来源补齐具体控制模式、保护闭锁、滤波器、无功补偿和测试系统参数。没有官方工程资料或论文表图时，不应新增设备容量、损耗、角度整定或滤波器阶次等精确数值。
