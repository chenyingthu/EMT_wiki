---
title: "Damping of Subsynchronous Control Interactions in Large-Scale PV Installations Through Faster-Than-Real-Time Dynamic Emulation"
type: source
authors: ['未知']
year: 2021
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/12/Damping_of_Subsynchronous_Control_Interactions_in_Large-Scale_PV_Installations_Through_Faster-Than-Real-Time_Dynamic_Emulation.pdf"]
---

# Damping of Subsynchronous Control Interactions in Large-Scale PV Installations Through Faster-Than-Real-Time Dynamic Emulation

**作者**: 
**年份**: 2021
**来源**: `12/Damping_of_Subsynchronous_Control_Interactions_in_Large-Scale_PV_Installations_Through_Faster-Than-Real-Time_Dynamic_Emulation.pdf`

## 摘要

Large-scale photovoltaic (PV) power plant has witnessed a dramatic increase in the integration into transmission and distribution network, manifesting subsynchronous control interaction (SSCI) when the host grid is weak. In this work, the oscillation modes of a typical PV network are analyzed, and a faster-than- real-time (FTRT) emulation is proposed for predicting the SSCI and consequently mitigating its impacts on AC grid by taking the effective active/reactive power control action. The electromagnetic transient (EMT) simulation is utilized to model the PV panels and converter stations to reﬂect the actual dynamic process. Meanwhile, the AC grid undergoes transient stability (TS) simulation to obtain a high speed up over real-time, and consequently, a power-voltage interface is adopted f

## 核心贡献

- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[超实时-ftrt-仿真|超实时(FTRT)仿真]]
- [[电磁暂态-emt-仿真|电磁暂态(EMT)仿真]]
- [[暂态稳定-ts-仿真|暂态稳定(TS)仿真]]
- [[emt-ts混合仿真|EMT-TS混合仿真]]
- [[fpga硬件并行仿真|FPGA硬件并行仿真]]
- [[功率-电压接口技术|功率-电压接口技术]]
- [[预测控制|预测控制]]
- [[振荡模式分析|振荡模式分析]]

## 涉及的模型

- [[大型光伏电站|大型光伏电站]]
- [[光伏阵列|光伏阵列]]
- [[变流器|变流器]]
- [[交流电网|交流电网]]
- [[串联补偿输电线路|串联补偿输电线路]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

Large-scale photovoltaic (PV) power plant has witnessed a dramatic increase in the integration into transmission and distribution network, manifesting subsynchronous control interaction (SSCI) when th
