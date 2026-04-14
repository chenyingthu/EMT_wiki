---
title: "FPGA-Based Real-Time EMTP"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['real-time', 'fpga', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/TPWRD.2008.923392.pdf.pdf"]
---

# FPGA-Based Real-Time EMTP

**作者**: 
**年份**: 2009
**来源**: `19、20、21/EMT_task_19/TPWRD.2008.923392.pdf.pdf`

## 摘要

—Real-time transient simulation of large transmis- sion networks requires signiﬁcant computational power. This paper proposes a ﬁeld-programmable gate array (FPGA)-based real-time electromagnetic transient simulator. Taking advantage of the inherent parallel architecture, high density, and high clock speed, the real-time Electromagnetic Transients Program (EMTP) is implemented on a single FPGA chip. It is based on a paralleled algorithm that is deeply pipelined, and uses a ﬂoating-point arithmetic calculation to achieve high accuracy for simulating fast electromagnetic transients. To validate the new simulator, a sample system with 15 transmission lines using full frequency-de- pendent modeling is simulated in real time. A timestep of 12 s has been achieved based on a 12.5-ns clock period 

## 核心贡献

- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[fpga硬件实现|FPGA硬件实现]]
- [[并行算法|并行算法]]
- [[深度流水线技术|深度流水线技术]]
- [[浮点运算|浮点运算]]
- [[全频变建模|全频变建模]]

## 涉及的模型

- [[输电线路|输电线路]]
- [[全频变线路模型|全频变线路模型]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

—Real-time transient simulation of large transmis- sion networks requires signiﬁcant computational power
