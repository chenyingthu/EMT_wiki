---
title: "开关暂态 (Switching Transient)"
type: topic
tags: [switching, circuit-breaker, transient, trapped-charge, re-strike, pre-insertion]
created: "2026-05-01"
---

# 开关暂态 (Switching Transient)

## 定义与边界

开关暂态（Switching Transient）是断路器、隔离开关、负荷开关、电力电子器件或直流断路器改变网络连接状态时产生的电压电流暂态。它包括合闸过电压、分闸过电压、预击穿、重燃、截流、暂态恢复电压和残余电荷释放等现象。

本页讨论由开关事件触发的 EMT 现象。它不等同于全部 [[electromagnetic-transient]]，也不替代 [[circuit-breaker-model]] 或 [[detailed-switch-model]] 的设备模型细节。若开关只被表示为预定时刻的理想拓扑变化，页面结论应限于网络波形，不应外推为真实断路器灭弧能力或寿命结论。

## EMT 中的作用

开关暂态是 EMT 仿真的经典入口，因为事件时刻会直接改变节点导纳矩阵、历史源和元件状态。它常用于绝缘配合、断路器应力、并联电抗器和电容器投切、长电缆合分闸、直流故障开断、电力电子开关波形和控制保护验证。

对第 $n$ 个时步，可把开关状态写为 $s_n\in\{0,1\}$，网络方程写成

$$
\mathbf{Y}(s_n)\mathbf{v}_n=\mathbf{i}^{\mathrm{hist}}_n+\mathbf{i}^{\mathrm{src}}_n.
$$

若需要表示电弧或重燃，开关不再只是 $s_n$，而是带状态的非线性端口 $i_{\mathrm{arc}}=f(v_{\mathrm{arc}},x_{\mathrm{arc}},t)$。这一区分决定了模型能否讨论开断失败、热击穿和介质恢复。

## 主要分支与机制

- 合闸暂态：合闸相角、残余电荷、线路或电缆端接阻抗决定入射波和反射波，常与 [[transmission-line-model]]、[[cable-model]] 衔接。
- 分闸暂态：电感或电容储能在电流过零附近释放，可能形成暂态恢复电压和高频振荡。
- 重燃与预击穿：触头间介质强度和恢复电压相互竞争，简单理想开关无法给出可信失败机理。
- 截流和电弧：小感性电流开断、并联电抗器投切和真空/SF6 断路器研究需要动态电弧或经验开断模型。
- 直流开断：直流电流没有自然过零，混合式、谐振式或限流式拓扑需要同时表示电流转移、能量吸收和控制时序。
- 数值事件处理：开关事件通常落在离散步之间，[[interpolation-method]] 和 [[voltage-interpolation]] 决定事件时刻误差和数值振荡风险。

## 适用边界与失败模式

- 合闸电阻、同步合闸、重燃概率和过电压倍数必须绑定电压等级、线路长度、负荷状态、残余电荷、断路器模型和统计口径。
- 动态断路器模型需要实测或厂家参数。没有电弧参数时，只能讨论建模方法，不能判断真实开断成功率。
- 理想开关适合拓扑事件和控制逻辑初筛，不适合研究电弧能量、热失败、介质击穿或多次重燃。
- 直流断路器论文中的开断时间、电流和能量结果通常是特定拓扑和测试系统结论，不能泛化为所有 HVDC 开断。
- 开关插值方法若只在某个电力电子算例中验证，应写为“作者在该算例中报告”，不能写成所有开关暂态都消除数值振荡。

## 代表性来源

- [[modelling-of-circuit-breakers-in-the-electromagnetic-transients-program-power-sy]] 支撑动态断路器模型与 EMTP 补偿法的讨论；其证据边界提醒不要把单个电弧模型写成所有失效模式都可覆盖。
- [[potential-risk-of-failures-in-switching-ehv-shunt-reactors]] 可作为并联电抗器开断、电弧-电路相互作用和频率相关参数影响的个案来源。
- [[a-new-model-of-trapped-charge-sources-in-switching-transient-studies-in-the-pres]] 支撑残余电荷源在开关暂态研究中的建模入口。
- [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu]] 可用于说明开关器件插值和事件时刻误差处理；具体精度应绑定原文算例。
- [[a-new-topology-for-current-limiting-hvdc-circuit-breaker]] 与 [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea]] 可作为直流断路器拓扑和谐振开断建模的来源入口。

## 与相关页面的关系

- [[electromagnetic-transient]] 给出暂态现象总边界；本页聚焦开关事件。
- [[ideal-switch-model]]、[[detailed-switch-model]] 和 [[circuit-breaker-model]] 分别承载开关模型层级。
- [[state-space-method]] 和 [[nodal-admittance-matrix]] 解释拓扑切换后网络方程如何求解。
- [[interpolation-method]] 与 [[voltage-interpolation]] 处理离散步长内的事件时刻。
- [[vsc-hvdc]]、[[mmc-model]] 和 [[power-electronics]] 涉及高频器件开关，但器件调制问题不等同于高压断路器开断。

## 开放问题

- 如何在公开 EMT 模型中记录断路器电弧参数、介质恢复和厂家数据的证据等级。
- 如何把开关统计分散性、残余电荷和保护动作组织成可复现的绝缘配合算例。
- 如何为直流断路器建立跨拓扑、跨平台且不过度外推的验证基准。
- 如何区分物理重燃、数值振荡和插值误差在波形中的表现。
