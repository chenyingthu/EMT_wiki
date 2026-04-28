---
title: "平均值模型"
type: method
tags: [average-value-model, avm, converter, emt]
created: "2026-04-13"
---

# 平均值模型

## 定义与概述

平均值模型（Average-Value Model, AVM）是一类用周期平均、开关函数平均或状态空间平均替代详细开关动作的 EMT 建模方法。它把变流器在一个开关周期内的高频通断细节压缩为连续控制量、受控源或等效电路，从而保留功率交换、控制响应和低频暂态，同时降低详细开关模型带来的计算负担。

AVM 常用于 [[models/vsc-model|VSC]]、[[models/mmc-model|MMC]]、LCC 换流器、风电变流器和系统级 HVDC 研究。它与详细 EMT 模型互补：详细模型用于开关应力、保护动作和高频谐波验证，平均值模型用于控制设计、系统级暂态、混合仿真和大规模参数扫描。

## 作用机制

平均值模型的核心是把离散开关变量替换为连续调制量或平均开关函数。例如换流器桥臂电压可由子模块开关状态求和得到，AVM 则用占空比、插入指数或调制函数近似桥臂平均电压。随后模型可表示为：

$$
\bar{v}_{\mathrm{arm}}(t)=m(t)V_{\mathrm{dc}},\qquad
\dot{x}=f(x,\bar{v}_{\mathrm{arm}},u)
$$

其中 $m(t)$ 是调制函数或插入指数，$\bar{v}_{\mathrm{arm}}$ 是开关周期平均桥臂电压，$x$ 可表示电容电压、环流、滤波器状态或控制状态。

- **受控源接口**：用受控电压源或电流源连接外部网络，计算简单，但可能引入接口延迟。
- **直接接口 AVM**：把平均模型方程嵌入节点导纳矩阵，与外部网络联立求解，减少间接接口延迟。
- **参数化 AVM（PAVM）**：用预先提取的参数或解析函数重构换流器在不平衡、换相失败或故障下的平均行为。
- **增强型 MMC AVM**：额外描述桥臂能量、环流、子模块电容电压纹波、闭锁/解锁状态或损耗。
- **混合模型切换**：在需要局部高保真时切换到详细等效模型，在系统级区段使用 AVM 提升效率。

## 适用边界

- 适合系统级暂态、控制器设计、机电-电磁混合仿真、VSC-HVDC 或 MMC-HVDC 大范围工况分析。
- 适合关注基波、低频控制动态、功率流和主要故障暂态，而不是逐个器件开关瞬态的任务。
- 对谐波、开关纹波、器件损耗、保护误动作和子模块电容局部不均衡敏感的研究，应使用增强 AVM、谐波保留 AVM 或详细模型复核。
- 传统受控源 AVM 在大步长或强耦合网络中可能出现接口延迟；直接接口模型更适合对数值稳定性要求高的节点法 EMT 求解器。
- 对直流故障、闭锁、换相失败和不平衡交流系统，必须确认模型是否显式覆盖相应运行模式，不能默认所有平均值模型都适用。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid]] | 2014 | 讨论 MMC 平均值模型在 VSC-HVDC 网格中的适用性和故障边界。 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 | 用动态平均值方法描述 AC-DC 换流器。 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation]] | 2018 | 增强 MMC AVM，关注闭锁和暂态初始条件。 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Converters]] | 2019 | 用阻塞模块统一处理多子模块拓扑和闭锁/解锁模式。 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model]] | 2020 | 讨论详细等效模型与开关函数 AVM 的动态切换。 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With Embedded Storage]] | 2021 | 面向带嵌入式储能 MMC 的平均值建模。 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Networks]] | 2021 | 将参数化 AVM 扩展到交流不平衡工况。 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC-DC Converters]] | 2022 | 讨论 PAVM 与节点方程的直接接口。 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMT]] | 2023 | 面向 VSC 的直接接口 AVM。 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal Analysis]] | 2024 | 将 VSC AVM 写成适合节点求解的扩展等效导纳形式。 |

## 相关页面

- [[models/vsc-model|VSC 模型]]
- [[models/mmc-model|MMC 模型]]
- [[topics/vsc-hvdc|VSC-HVDC]]
- [[state-space-method|状态空间法]]
- [[fixed-admittance|恒导纳模型]]
- [[topics/dynamic-phasor|动态相量]]
