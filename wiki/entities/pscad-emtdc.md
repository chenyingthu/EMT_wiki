---
title: "PSCAD/EMTDC"
type: entity
entity_type: tool
tags: [pscad, emtdc, manitoba, simulation-tool]
created: "2026-04-13"
---

# PSCAD/EMTDC

## 概述

PSCAD/EMTDC 是由加拿大曼尼托巴大学（University of Manitoba）和曼尼托巴水电国际公司（Manitoba Hydro International）开发的电力系统电磁暂态仿真软件。

## 核心原理详解

PSCAD 是图形化建模环境，EMTDC 是时域 EMT 求解引擎。其基本计算仍可概括为：把网络元件离散为伴随电路，形成节点导纳矩阵，在每个微秒级时间步求解瞬时电压和电流。

$$
G_{\mathrm{eq},L}=\frac{\Delta t}{2L}, \qquad
G_{\mathrm{eq},C}=\frac{2C}{\Delta t}
$$

这些等效导纳和历史源使电感、电容、变压器、线路和电力电子开关可以统一进入节点方程。PSCAD/EMTDC 在 EMT Wiki 中的意义不是单一算法，而是大量论文用来提供“可信详细模型基准”的工具：新方法经常通过与 PSCAD 波形对比来证明精度。

## 特点

- 图形化建模界面（PSCAD）
- EMTDC求解引擎
- 广泛应用于工业界和学术界
- 支持用户自定义模型

## 关键技术

- 节点分析法（Nodal Analysis）
- 伴随电路模型
- 梯形积分法
- 稀疏矩阵求解

## 关键技术详解

| 技术面 | 作用 | Wiki 关联 |
|-------|------|-----------|
| 详细电力电子建模 | 保留开关、控制、保护和高频暂态，是平均模型和等效模型的常用基准 | [[average-value-model]], [[mmc-model]] |
| 自定义组件 | 支持用户实现新控制器、新接口模型和实验算法 | [[co-simulation]], [[dynamic-phasor]] |
| 线路/电缆模型 | 支持行波、频率相关参数和宽频暂态分析 | [[cable-modeling]], [[transmission-line-model]] |
| 混合仿真接口 | 常与 PSS/E、E-TRAN、RTDS 或自定义接口用于 EMT/TS 联合仿真 | [[co-simulation]] |

## 代表性用途

| 用途 | PSCAD/EMTDC 在论文中的角色 | 审核重点 |
|------|-----------------------------|----------|
| 新型换流器或 MMC 模型验证 | 作为详细开关级或详细等效模型基准 | 是否说明子模块数量、控制采样、死区、时间步长 |
| HVDC/FACTS 控制策略 | 承载主电路、控制器和故障工况 | 是否有对比控制策略和扰动设置 |
| EMT/TS 混合仿真 | 作为 EMT 子系统与机电暂态工具交换边界变量 | 接口量、同步方式和延迟补偿是否清楚 |
| 保护与行波暂态 | 产生高频故障波形和测量信号 | 线路模型、采样率和故障位置决定结论可信度 |

## 代表性页面

- [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map]]：使用 PSCAD/EMTDC 对比详细模型、状态空间模型和等效模型，适合检查“波形精度+计算效率”的证据链。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：把 PSCAD/EMTDC 用作并联 VSC-ESS 频率控制策略的 EMT 验证环境。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：体现 PSCAD/EMTDC 与实时或混合仿真基准之间的关系。

## 证据使用规则

- “PSCAD 仿真验证”只能说明在给定模型和工况下通过了数值实验；若没有基准、参数表或误差指标，不应扩写为工程已验证。
- 对电力电子模型，必须看是否包含死区、采样、PWM、限幅和保护逻辑；缺少这些细节时，PSCAD 波形仍可能过于理想化。
- 对混合仿真论文，PSCAD 侧的 EMT 精度不是唯一问题，边界等值、通信步长和插值策略同样会决定稳定性。

## 适用边界与注意事项

- PSCAD/EMTDC 适合高保真离线 EMT 和工程模型验证，但详细开关模型在大规模系统中计算成本高；这也是 [[average-value-model|平均值模型]]、[[state-space-method|状态空间等效]]、[[co-simulation|混合仿真]] 持续发展的原因。
- 论文中“与 PSCAD 一致”通常只能说明相同工况下波形接近；还需要关注时间步长、控制采样、开关插值、初值和故障位置是否一致。
- 当模型用于 HIL 或实时验证时，PSCAD 离线模型常需要转换到 [[rtds|RTDS]]、OPAL-RT 或 FPGA/GPU 平台，转换过程可能引入模型简化和接口延迟。

## 开放问题

- 大规模新能源场站和多端 HVDC 系统如何在 PSCAD 详细模型、实时模型和机电暂态模型之间保持一致性。
- 自定义组件如何形成可复用、可审计的模型库，而不是停留在单个工程项目脚本中。

## 相关实体
- [[university-manitoba]]
- [[manitoba-hydro]]
- [[emtp]]
- [[rtds]]
- [[atp-emtp]]
- [[mmc-model]]
