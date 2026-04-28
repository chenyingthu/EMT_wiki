---
title: "数值积分"
type: method
tags: [numerical-integration, emt, trapezoidal, dirk]
created: "2026-04-13"
---

# 数值积分

## 定义与概述

数值积分是 EMT 仿真把连续时间微分代数方程离散成逐时步代数方程的核心方法。电感、电容、线路、变流器控制和等效网络都需要通过积分公式生成伴随电路、状态更新式或节点注入历史项。

在 EMTP 类求解器中，数值积分通常不是孤立算法，而是和 [[nodal-analysis|节点分析法]]、[[state-space-method|状态空间法]]、开关事件处理以及设备等效模型共同决定仿真精度、数值阻尼和计算成本。梯形法、后向欧拉法、DIRK/SDIRK、紧凑格式、频率匹配积分和混合积分策略分别面向不同的稳定性与效率需求。

## 作用机制

典型 EMT 离散化会把动态元件写成等效导纳加历史源：

$$
i(t_k)=G_{\mathrm{eq}}v(t_k)+I_{\mathrm{hist}}(t_{k-1})
$$

其中 $G_{\mathrm{eq}}$ 由积分公式、元件参数和步长决定，历史源汇总上一时刻的电压、电流或状态变量。这样可把含动态元件的网络并入同一个节点方程。

主要机制包括：

- **梯形法**：二阶精度、适合常规线性网络，但在开关突变或故障切换后可能保留高频数值振荡。
- **后向欧拉法**：数值阻尼强，常用于事件点、初始化、振荡抑制或刚性系统，但稳态精度通常低于梯形法。
- **DIRK/SDIRK 方法**：通过隐式多阶段计算提高稳定性，可在不依赖精确事件检测的情况下抑制突变后的伪振荡。
- **紧凑格式与多步法**：在精度、阻尼和单步求解成本之间折中，常用于非线性元件或大步长 EMT 场景。
- **频率匹配积分**：面向 [[topics/dynamic-phasor|动态相量]] 或窄频带模型，围绕目标频带优化离散化误差。
- **混合积分**：按元件类型、开关状态或时间段切换积分公式，例如在稳态采用低阻尼方法，在事件点采用强阻尼方法。

## 适用边界

- 需要逐时步保持电感、电容、频变网络和电力电子开关动态时，数值积分是基础求解环节。
- 含频繁开关、故障切换或非线性器件时，应关注积分公式的阻尼特性，避免把数值振荡误判为物理暂态。
- 梯形法适合大量常规 EMT 网络，但遇到不连续事件通常需要配合临界阻尼、后向欧拉过渡、插值或 L 稳定公式。
- DIRK/SDIRK 和紧凑格式适合对稳定性要求高的电力电子系统，但会增加每步或每阶段求解成本。
- 频率匹配方法适合目标频带明确的模型；若暂态频带很宽，应避免把窄带优化误用为通用 EMT 积分方案。
- 大步长积分能提高效率，但应由模型目标、控制带宽、开关频率和线路传播特性共同约束，不应脱离验证结果单独给出固定步长。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally]] | 2008 | 将 2S-DIRK 用于 EMT 离散化，讨论精度与振荡抑制。 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simulation of dynamic phasors]] | 2009 | 面向动态相量模型的频率匹配积分。 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact scheme for electromagnetic transients]] | 2023 | 用紧凑格式兼顾稳定性与突变处理。 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration]] | 2023 | 在 MMC 等效中结合混合积分、解耦和恒导纳思想。 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK based EMT simulations]] | 2024 | 讨论 2S-DIRK 在 EMT 应用中的补充处理。 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step-size electromagnetic transients]] | 2024 | 面向较大步长 EMT 的隐式积分。 |

## 相关页面

- [[nodal-analysis|节点分析法]]
- [[state-space-method|状态空间法]]
- [[fixed-admittance|恒导纳模型]]
- [[average-value-model|平均值模型]]
- [[topics/dynamic-phasor|动态相量]]
- [[topics/real-time-simulation|实时仿真]]
