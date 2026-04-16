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


- 提出基于FPGA的EMT-TS混合仿真架构，实现超实时动态推演
- 设计功率-电压接口实现电磁暂态与机电暂态模型的并行协同计算
- 利用光伏逆变器等效STATCOM，通过有功无功注入抑制次同步振荡


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[混合仿真|混合仿真]]
- [[fpga硬件仿真|FPGA硬件仿真]]
- [[并行计算|并行计算]]
- [[特征值分析|特征值分析]]
- [[功率-电压接口|功率-电压接口]]


## 涉及的模型


- [[光伏电站|光伏电站]]
- [[电压源换流器|电压源换流器]]
- [[交流电网|交流电网]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[pv-statcom|PV-STATCOM]]


## 相关主题


- [[次同步控制交互|次同步控制交互]]
- [[超实时仿真|超实时仿真]]
- [[硬件仿真|硬件仿真]]
- [[混合仿真|混合仿真]]
- [[弱电网稳定性|弱电网稳定性]]
- [[光伏并网|光伏并网]]
- [[并行计算|并行计算]]


## 主要发现


- 提出的FPGA硬件仿真平台实现了122倍超实时加速比，满足快速预测需求
- 通过有功无功功率控制策略有效阻尼了弱电网下光伏电站的次同步振荡
- 硬件仿真结果与Matlab及TSAT离线工具高度吻合，验证了模型准确性


