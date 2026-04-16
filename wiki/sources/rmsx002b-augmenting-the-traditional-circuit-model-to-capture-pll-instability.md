---
title: "RMS&#x002B;: Augmenting the Traditional Circuit Model to Capture PLL Instability"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Delivery;2026;41;1;10.1109/TPWRD.2025.3646818"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/34/Carreño 等 - 2026 - RMS+ Augmenting the Traditional Circuit Model to Capture PLL Instability.pdf"]
---

# RMS&#x002B;: Augmenting the Traditional Circuit Model to Capture PLL Instability

**作者**: 
**年份**: 2026
**来源**: `34/Carreño 等 - 2026 - RMS+ Augmenting the Traditional Circuit Model to Capture PLL Instability.pdf`

## 摘要

—Electrical circuits are modelled with a constant ad- mittance matrix for steady-state studies and for dynamic stud- ies involving synchronous machines. It is widely considered that this model, called RMS model, is also suitable for capturing low- frequencyoscillationsinnetworkswithinverters;however,thisidea has been challenged by recent research of the Phase-Locked Loop. TheEMTmodel,incontrast,accountsforthedynamicsofallcircuit components, but its high computational cost limits its application in the analysis of bulk power systems. This paper introduces RMS+, a new circuit model constructed from the raw data of the system, that captures the PLL interactions with the network while reducing the number of state variables. The theoretical framework includes the theory of dynamical systems, pa

## 核心贡献



- 提出RMS+增强型电路模型，在保留网络与PLL交互动态的同时有效减少系统状态变量
- 基于慢快系统理论建立分析框架，利用电磁暂态与PLL动态的时间尺度分离特性提升大电网同步稳定性分析效率

## 使用的方法


- [[state-space]]
- [[nodal-analysis]]
- [[fixed-admittance]]

## 涉及的模型


- [[vsc-model]]
- [[synchronous-machine]]

## 相关主题


- [[vsc]]
- [[synchronous-machine]]

## 主要发现



- 传统RMS模型的恒定导纳矩阵无法准确捕捉跟网型VSC中PLL与网络的交互动态及小信号失稳机制
- 电感“di/dt”效应是引发PLL相关小信号失稳的关键物理机制
- RMS+模型通过引入慢快系统理论成功分离时间尺度，在大幅降低计算维度的同时实现了对PLL同步稳定性的精确评估