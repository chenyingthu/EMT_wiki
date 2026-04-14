---
title: "Massively Parallel Implementation of AC Machine Modeling for Real-Time Simulation"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Matar和Iravani - 2011 - Massively parallel implementation of AC machine models for FPGA-based real-time simulation of electr.pdf"]
---

# Massively Parallel Implementation of AC Machine Modeling for Real-Time Simulation

**作者**: 
**年份**: 2011
**来源**: `25/Matar和Iravani - 2011 - Massively parallel implementation of AC machine models for FPGA-based real-time simulation of electr.pdf`

## 摘要

—This paper presents a generalized, parallel imple- mentation methodology for real-time simulation of ac machine transients in an FPGA-based real-time simulator. The proposed method adopts nanosecond range simulation time-step and exploits the large response time of a rotating machine to: 1) eliminate the need for predictive-corrective action for the machine electrical and mechanical variables, 2) decouple the solution of the dq0 stator currents, and 3) enable the use of one-time-step delayed interface between the machine and the rest of the system which decouples the machine solution from that of the rest of the system. The proposed method simpliﬁes the solution of the machine model without compromising accuracy or numerical stability of the simulation. This paper also presents a massivel

## 核心贡献

- 设计了并行计算策略，加速大规模电网EMT仿真
- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[大规模并行计算|大规模并行计算]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[纳秒级仿真步长|纳秒级仿真步长]]
- [[dq0轴电流解耦|dq0轴电流解耦]]
- [[单步延迟接口技术|单步延迟接口技术]]

## 涉及的模型

- [[交流电机|交流电机]]
- [[永磁同步电机|永磁同步电机]]
- [[感应电机|感应电机]]
- [[交流驱动系统|交流驱动系统]]

## 相关主题

- [[parallel-computing]]
- [[real-time-simulation]]

## 主要发现

—This paper presents a generalized, parallel imple- mentation methodology for real-time simulation of ac machine transients in an FPGA-based real-time simulator
