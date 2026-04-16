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


- 提出基于FPGA的交流电机纳秒级步长并行实时仿真方法，消除预测校正环节
- 采用单步延迟接口解耦电机与网络，实现dq0定子电流解耦与机电并行求解
- 设计面向交流电机的大规模并行定制硬件架构，单步计算耗时仅44纳秒


## 使用的方法


- [[dq0变换模型|dq0变换模型]]
- [[单步延迟接口法|单步延迟接口法]]
- [[并行计算|并行计算]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[常数电感矩阵离散化|常数电感矩阵离散化]]


## 涉及的模型


- [[pmsm-model|PMSM]]
- [[感应电机|感应电机]]
- [[同步电机|同步电机]]
- [[双馈异步电机|双馈异步电机]]
- [[机电耦合模型|机电耦合模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[并行计算|并行计算]]
- [[fpga仿真|FPGA仿真]]
- [[电磁暂态|电磁暂态]]
- [[模型解耦|模型解耦]]


## 主要发现


- FPGA单步计算时间仅44纳秒，成功实现纳秒级步长下的交流电机实时仿真
- 单步延迟接口结合极小步长有效抑制数值振荡，无需预测校正仍保高精度
- PMSM与感应电机驱动系统仿真结果验证了该并行架构的精度与实时性


