---
title: "电缆建模 (Cable Modeling)"
type: topic
tags: [cable, underground-cable, submarine-cable, skin-effect, frequency-dependent]
created: "2026-04-14"
---

# 电缆建模 (Cable Modeling)

## 定义与概述

电缆建模研究地下电缆、海底电缆和混合架空-电缆线路在 EMT 仿真中的参数计算、频率相关效应和时域实现。与架空线路相比，电缆具有导体、绝缘、屏蔽、护套、铠装和土壤/海水回路等多层结构，集肤效应、邻近效应、护套回流和介质损耗会显著影响暂态传播。

在 EMT 语境下，电缆模型通常需要在宽频精度、数值稳定性和计算成本之间折中。工频或慢暂态可使用固定参数模型；雷电、开关冲击、直流故障行波和 VSC-HVDC 宽频振荡则需要频率相关模型。

## 作用机制

电缆模型通常先在频域获得单位长度阻抗矩阵和导纳矩阵：

$$
Z(s)=R(s)+sL(s), \qquad Y(s)=G(s)+sC(s)
$$

随后再转换为适合时域 EMT 的形式。常见机制包括：

- **频变参数计算**：考虑导体集肤效应、邻近效应、护套/铠装回流、大地或海水返回路径。
- **多导体传输线模型**：在相域或模域处理芯线、护套和铠装之间的耦合。
- **矢量拟合与有理逼近**：把频域阻抗、导纳或传播函数拟合为可在时域递推的有理函数。
- **状态空间实现**：将拟合结果写成状态方程，便于和 [[state-space-method|状态空间法]] 或 [[models/fdne-model|频变网络等值]] 接口。
- **宽频/ULM 类模型**：在传播时延、模态变换和无源性之间做平衡，适用于长电缆和混合线路。
- **测量融合**：当几何参数不足以解释高频传播时，可用阻抗测量、S 参数或时域反射数据修正模型。

## 适用边界

- 固定参数电缆模型适合工频、准稳态和低频控制研究，但不应直接用于快速暂态或行波保护精度判断。
- 频率相关模型适合雷电冲击、开关暂态、VSC-HVDC 宽频相互作用和长距离电缆传播问题。
- 三芯、铠装、交叉互联或共沟敷设电缆需要显式考虑导体间耦合；单芯简化模型不一定适用。
- 频域拟合模型必须检查稳定性和无源性，否则在闭环 HIL 或长时域仿真中可能出现非物理发散。
- 电缆参数依赖几何、材料、敷设方式和环境；缺少证据时应避免给出固定的宽频误差或通用参数。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an underground transmission cable]] | 2005 | 讨论地下电缆快速暂态中的邻近效应。 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2009 | 线路与电缆参数计算工具。 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-conductor cable modeling with inclusion of measured coaxial wave propagation]] | 2022 | 将测量传播特性纳入多导体电缆模型。 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core armoured cables]] | 2023 | 关注三芯铠装电缆的螺线管效应。 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 | 海底埋设电缆的时域建模。 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-Delay Estimation Through All-Pass Functions for ULM Line and Cable Models]] | 2025 | ULM 线路/电缆模型的时延估计。 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and rational Krylov fitting]] | 2026 | 宽频电缆/线路模型的降阶拟合。 |
| [[validation-of-frequency-dependent|Validation of frequency-dependent]] | 2026 | 频率相关模型验证。 |

## 相关页面

- [[models/cable-model|电缆模型]]
- [[models/transmission-line-model|传输线模型]]
- [[models/fdne-model|频变网络等值]]
- [[methods/vector-fitting|矢量拟合]]
- [[topics/frequency-dependent-modeling|频率相关建模]]
- [[methods/state-space-method|状态空间法]]
- [[topics/real-time-simulation|实时仿真]]
