---
title: "The Reconﬁgurable-Hardware Real-Time and"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/37/tpwrd.2012.2229723.pdf.pdf"]
---

# The Reconﬁgurable-Hardware Real-Time and

**作者**: 
**年份**: 2012
**来源**: `37/tpwrd.2012.2229723.pdf.pdf`

## 摘要

—The reconﬁgurable-hardware real-time power system simulator (RH-RTS) is a ﬁeld-programmable gate-array (FPGA)-based real-time simulator that is developed based on the concept of simulators hardware reconﬁgurability (i.e., to change the underlying hardware architecture of the simulator to accommodate various power system topologies). The uniqueness of the RH-RTS is the underlying hardware architecture. The RH-RTS has a massively parallel customized hardware architec- ture that is tailored to the solution of the mathematical model of the power system under consideration. The RH-RTS enables the simulation of large power systems with a computation-time per simulation time-step in the range of tens of nanoseconds. Not only does the RH-RTS provide a means for real-time operation (e.g.,

## 核心贡献



- 提出基于FPGA的可重构硬件实时仿真器(RH-RTS)，实现底层硬件架构动态重构以适应不同电网拓扑
- 实现大规模电力系统电磁暂态仿真，单步计算时间低至24纳秒，支持实时与超实时双模式运行

## 使用的方法


- [[parallel]]
- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[network-equivalent]]

## 相关主题


- [[real-time]]
- [[co-simulation]]
- [[harmonic]]

## 主要发现



- RH-RTS单步计算时间可低至24纳秒，为目前技术文献报道的最低水平
- 该仿真器有效突破了传统实时仿真器在最小时间步长、频率带宽和模型精度上的限制，可高效支持硬件在环测试与统计开关研究