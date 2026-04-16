---
title: "Switch-Averaged Frequency Domain Simulation of Photovoltaic Systems"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;2;10.1109/TPWRD.2022.3200011"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/Agudelo 等 - 2023 - Switch-Averaged Frequency Domain Simulation of Photovoltaic Systems.pdf"]
---

# Switch-Averaged Frequency Domain Simulation of Photovoltaic Systems

**作者**: 
**年份**: 2023
**来源**: `37/Agudelo 等 - 2023 - Switch-Averaged Frequency Domain Simulation of Photovoltaic Systems.pdf`

## 摘要

—This paper pushes forward frequency domain (FD) modeling of switched networks aimed at transient simulation, with particular interest in photovoltaic (PV) systems. The PV system simulation is performed via the numerical Laplace transform (NLT) in a sequential (partitioned-time) fashion by using a set of time-windows. The proposed technique enhances existing FD PV models by a) averaging switching functions and b) using sample overlapping to alleviate numerical oscillations due to rise-time phe- nomenon at time-window interfaces. The proposed enhancements provide a more efﬁcient dynamic simulation compared to both classical single-window full-sample NLT implementation and non- averaged FD PV models. Veriﬁcation is performed via prevalent electromagnetic transient (EMT) software tools. Index

## 核心贡献



- 提出基于数值拉普拉斯变换(NLT)的分时窗频域仿真框架，专用于光伏开关网络的暂态分析
- 引入开关函数平均与样本重叠技术，有效抑制时间窗接口处的上升沿数值振荡，显著提升动态仿真效率

## 使用的方法


- [[numerical-integration]]
- [[interpolation]]
- [[average-value-model]]

## 涉及的模型


- [[average-value-model]]
- [[network-equivalent]]

## 相关主题


- [[harmonic]]
- [[frequency-dependent]]

## 主要发现



- 开关平均与样本重叠策略能彻底消除传统分时窗NLT方法在接口处产生的数值振荡
- 所提方法在保持精度的前提下，计算效率显著优于经典单窗全采样NLT及非平均频域模型，且经主流EMT工具验证可靠