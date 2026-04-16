---
title: "Magnetically Saturable Voltage Behind Reactance Model for Induction Machines"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Wang和Jatskevich - 2011 - Magnetically-saturable voltage-behind-reactance synchronous machine model for EMTP-type solution.pdf"]
---

# Magnetically Saturable Voltage Behind Reactance Model for Induction Machines

**作者**: 
**年份**: 2011
**来源**: `25/Wang和Jatskevich - 2011 - Magnetically-saturable voltage-behind-reactance synchronous machine model for EMTP-type solution.pdf`

## 摘要

—A so-called voltage-behind-reactance (VBR) machine model has recently been proposed for the electro-magnetic tran- sient programs (EMTP) as an advantageous alternative to the conventional and phase-domain models. This paper extends the previous research and proposes a magnetically saturable VBR synchronous machine model for EMTP-type solutions. The proposed saturable VBR model utilizes the saliency factor approach to represent main-ﬂux saturation for the salient-pole synchronous machines with the axes static and dynamic cross saturation included. An efﬁcient piecewise-linear method is used for representing the nonlinear saturation characteristic within the discretized EMTP solution. Case studies verify that the new model maintains the improved numerical accuracy in steady state and transi

## 核心贡献


- 提出凸极同步机电压后电抗模型，基于凸极系数法实现主磁通饱和及交轴交叉饱和精确表征
- 采用分段线性化方法处理非线性饱和特性，适配离散化EMTP求解器实现非迭代高效计算
- 建立可直接与外部网络接口耦合的VBR饱和模型，显著提升大时间步长下的暂态数值精度


## 使用的方法


- [[电压后电抗法-vbr|电压后电抗法(VBR)]]
- [[凸极系数法|凸极系数法]]
- [[分段线性化方法|分段线性化方法]]
- [[离散化节点分析|离散化节点分析]]
- [[增量电感近似|增量电感近似]]


## 涉及的模型


- [[凸极同步电机|凸极同步电机]]
- [[隐极同步电机|隐极同步电机]]
- [[电压后电抗模型|电压后电抗模型]]
- [[相域模型|相域模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[磁饱和建模|磁饱和建模]]
- [[交叉饱和效应|交叉饱和效应]]
- [[大时间步长仿真|大时间步长仿真]]
- [[机电网络接口|机电网络接口]]


## 主要发现


- 新模型在稳态与暂态中精确计及交轴交叉饱和，数值精度显著优于传统相域模型
- 分段线性化使模型在大时间步长下保持高数值稳定性与计算效率，避免非线性迭代
- 仿真验证表明该VBR模型可直接耦合外部网络，有效消除传统模型的大步长累积误差


