---
title: "晶闸管控制 (Thyristor Control)"
type: method
tags: [thyristor, control, firing-angle, tcr, tcsc, phase-control, scr, hvdc]
created: "2026-05-02"
---

# 晶闸管控制 (Thyristor Control)

## 概述

晶闸管控制（Thyristor Control）是通过同步触发脉冲决定晶闸管导通起点，从而控制整流、逆变、TCR/TSC、SVC、TCSC 或 LCC-HVDC 阀组等设备的等效电压、电流或阻抗的方法。晶闸管是半控器件：门极触发可以使其在正向偏置下导通，但导通后通常不能由门极直接关断，需要电流降至维持电流以下并建立足够恢复条件。

因此，晶闸管控制与 VSC 的 PWM 控制边界不同。[[models/vsc-model.md]] 依赖自关断器件和调制信号；[[models/lcc-model.md]] 依赖交流系统换相电压、触发角和关断角裕度。不能把 VSC 的 PLL/dq 电流控制结论写成晶闸管控制的通用规律。

## 输入与输出

| 项目 | 内容 |
|------|------|
| 输入 | 同步电压相位、触发角参考、阀状态、电流/电压反馈、保护闭锁信号 |
| 输出 | 门极触发脉冲、触发角 $\alpha$、必要时的超前触发角 $\beta$ 或电纳/阻抗参考 |
| 约束 | 正向电压、最小脉冲宽度、阀电流过零、恢复时间、触发脉冲排序 |
| EMT 结果 | 阀导通状态、换相过程、等效基波量、谐波和故障动态 |

触发角通常以交流同步参考为零点：

$$\alpha=\omega(t_{fire}-t_{ref})$$

其中 $t_{ref}$ 必须说明是电压过零、相电压参考、线电压参考还是特定阀组的换相参考。不同设备的触发角范围和物理含义不同，不能只给一个全局范围。

## 核心机制

晶闸管控制的 EMT 实现通常包括：

1. 从交流电压或 PLL/同步检测模块获得参考相位。
2. 根据外层控制器生成触发角、导纳、阻抗或直流电流参考。
3. 将参考量转换为各阀触发时刻，并按阀组顺序发出门极脉冲。
4. 在电路模型中判断正向电压、触发脉冲和阀电流条件，更新导通状态。
5. 在换相结束或电流过零后，判断是否具备关断恢复裕度。
6. 将阀状态反馈给网络方程、保护逻辑和下一步控制器。

在详细开关模型中，阀状态直接影响网络拓扑或等效支路；在平均值模型中，触发角通过参数化方程影响直流平均电压、交流电流和谐波分量。两者的证据边界不同：平均值模型通常不能替代阀级应力、触发失败或保护闭锁细节。

## LCC-HVDC 中的控制边界

LCC-HVDC 的晶闸管控制围绕直流电流、直流功率、触发角和 [[methods/extinction-angle-calculation.md]] 展开。逆变侧常需要保留关断角裕度，以降低换相失败风险；整流侧则常围绕直流电流或功率参考调节触发角。实际控制模式和限幅逻辑取决于工程控制系统，本页不新增未绑定来源的整定角度或最小裕度数字。

[[sources/average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail.md]] 支持这样一种边界化表述：在 LCC 逆变器平均值模型中，触发角、直流电流、换相电压和临界关断条件可用于识别换相失败。该来源不支持把 PAVM 结论外推到所有晶闸管装置。

[[sources/a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con.md]] 说明，若研究换相失败，模型应保留阀级离散开关状态或等效拓扑信息；仅用平滑控制方程可能不足以解释故障阀状态。

## FACTS 装置中的控制边界

在 [[models/svc-tcr-model.md]] 中，晶闸管触发角调节 TCR 的基波电纳，并伴随谐波产生。TSC 更接近投切控制，重点是选择合适投切时刻以限制涌流。[[models/tcsc-model.md]] 中，触发角改变串联支路的等效阻抗，但谐振区、保护旁路和次同步振荡风险需要单独建模。

这些 FACTS 装置的控制目标是无功、电压或串联补偿度，不等同于 LCC-HVDC 的换相角控制。相同的“触发角”术语在不同设备中代表不同输入输出关系。

## 适用边界

- 适用于晶闸管整流器、LCC-HVDC、TCR/TSC、SVC 和 TCSC 等半控器件场景。
- 不适用于 IGBT/MOSFET 的 PWM 自关断控制，也不适用于 VSC 的 dq 电流内环本身。
- 若研究换相失败，应结合阀状态、换相电压、直流电流和关断角，而不是只看触发角。
- 若研究谐波或次同步振荡，应保留触发角导致的非正弦电流和网络频率响应。
- 若研究保护动作，应显式写出闭锁、旁路、重触发和限幅逻辑，不能用常规稳态控制替代。

## 代表性证据

| 来源 | 证据用途 | 边界 |
|------|----------|------|
| [[sources/average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail.md]] | LCC 逆变器平均值模型中触发角、关断角和换相失败检测的关系 | 限于线换相逆变器 PAVM |
| [[sources/a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con.md]] | 晶闸管阀级离散状态对换相失败仿真的必要性 | 具体量化结论需回原文核对 |
| [[sources/hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model.md]] | SVC/TCR 可用动态相量或混合仿真方式表示晶闸管控制影响 | 面向 SVC，不代表 LCC-HVDC |

## 与相关页面的关系

- [[models/lcc-model.md]] 是晶闸管控制在 HVDC 中的主要设备页。
- [[methods/extinction-angle-calculation.md]] 是逆变侧换相裕度评估方法。
- [[methods/converter-station-inverter.md]] 说明控制方法在站级系统中的位置。
- [[models/svc-tcr-model.md]] 和 [[models/tcsc-model.md]] 是 FACTS 侧应用。

## 开放问题

晶闸管控制页面仍需要后续用具体来源补齐不同设备的触发同步、脉冲序列、保护闭锁和参数整定证据。当前修订优先建立术语边界，避免把 LCC、SVC/TCR、TCSC 和 VSC 控制混写。
