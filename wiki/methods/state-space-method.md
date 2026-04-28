---
title: "状态空间法"
type: method
tags: [state-space, emt, model-reduction, matrix-exponential]
created: "2026-04-13"
---

# 状态空间法

## 定义与概述

状态空间法把 EMT 网络中的电感、电容、电机、电力电子子模块、线路等效或多端口网络写成一组一阶动态方程，再通过数值积分、矩阵指数或分裂公式推进状态。它与传统 [[nodal-analysis|节点分析法]] 的区别在于：节点分析法优先形成每个时步的代数导纳方程，而状态空间法优先保留系统状态变量 $x$ 的演化关系。

对于开关电路、[[models/mmc-model|MMC]]、[[topics/vsc-hvdc|HVDC 系统]]、频变线路和多端口等效网络，状态空间表达能清楚描述“拓扑如何影响动态”，也便于做降阶、解耦、并行和解析求解。

## 作用机制

连续系统通常写成：

$$
\dot{x}(t)=Ax(t)+Bu(t), \qquad y(t)=Cx(t)+Du(t)
$$

其中 $x$ 是储能元件或等效内部变量，$u$ 是端口电压、电流、控制量或等效源，$y$ 是端口响应或内部观测量。EMT 仿真中的关键步骤是把连续方程离散化：

$$
x_{k+1}=\Phi x_k+\Gamma u_k
$$

$\Phi$ 和 $\Gamma$ 可由矩阵指数、梯形法、后向欧拉法、指数积分或分裂公式得到。当开关状态变化时，$A,B,C,D$ 可能随拓扑改变；高效算法的核心是减少矩阵重建、分解或指数运算成本。

典型用法包括：

- **直接状态求解**：把设备或简化系统整体写成状态方程，适合 HVDC 暂态简化模型、同步机和电力电子平均模型。
- **状态空间-节点混合**：设备内部用状态空间表示，外部网络仍用节点方程求解，适合 MMC、SST 和 N 端口等效模型。
- **描述符状态空间（DSE）**：保留代数约束，减少对电感割集、电容回路等特殊拓扑的手工处理。
- **分段/广义状态空间平均**：合并开关周期内相似时间段，降低变流器多时间尺度仿真成本。
- **状态分裂与降阶**：按子电路、开关状态或时间尺度拆分大矩阵，用低阶等效或分裂公式加速。
- **频变模型状态实现**：把有理拟合的频变线路、[[models/fdne-model|频变网络等值]] 或多端口网络转换为时域递推状态。

## 适用边界

- 适合内部动态强、外部端口有限、需要保留状态变量含义的设备级建模，例如 MMC、[[average-value-model|平均值模型]] 和频变网络等值。
- 对纯线性大网络，直接节点分析和稀疏矩阵求解往往更简单；状态空间法的收益通常来自内部消元、降阶或并行。
- 当开关频繁改变拓扑时，需要预计算、分组或快速更新状态矩阵，否则矩阵重建会抵消效率优势。
- 平均或降阶状态空间模型应明确是否仍能捕捉子模块电容电压、换相失败、故障电流高频分量等 EMT 细节。
- 描述符或高阶状态空间模型在接入节点求解器前，应检查稳定性、无源性和端口变量定义，避免接口不一致。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 | 用状态方程处理线性开关电路 EMT。 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 | 基于状态空间的 HVDC 暂态简化解析算法。 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 | 变流器分段广义状态空间平均模型。 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits]] | 2021 | 比较描述符状态空间和伴随电路 EMT 建模。 |
| [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti|A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transients]] | 2022 | 分段 GSSA 在变流器 EMT 中的应用。 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transmission line parameters]] | 2023 | 用状态空间实现频变输电线路时域仿真。 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular multilevel converters]] | 2025 | 面向 MMC 的状态矩阵降维和加速仿真。 |
| [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulation]] | 2025 | 变流器集成电力系统的分裂状态空间求解。 |

## 相关页面

- [[nodal-analysis|节点分析法]]
- [[numerical-integration|数值积分]]
- [[average-value-model|平均值模型]]
- [[fixed-admittance|恒导纳模型]]
- [[models/mmc-model|MMC 模型]]
- [[models/fdne-model|频变网络等值]]
- [[topics/vsc-hvdc|VSC-HVDC]]
- [[topics/frequency-dependent-modeling|频率相关建模]]
