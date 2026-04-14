---
title: "An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA"
type: source
authors: ['未知']
year: 2011
journal: "IEEE Transactions on Industrial Electronics;2011;58;6;10.1109/TIE.2010.2060461"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Chen and Dinavahi - 2011 - An iterative real-time nonlinear electromagnetic transient solver on FPGA.pdf"]
---

# An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA

**作者**: 
**年份**: 2011
**来源**: `07&08/Chen and Dinavahi - 2011 - An iterative real-time nonlinear electromagnetic transient solver on FPGA.pdf`

## 摘要

—A real-time transient simulation of nonlinear ele- ments in transmission networks requires signiﬁcant computational power. This paper proposes an iterative nonlinear transient solver on a ﬁeld-programmable gate array. The parallel solver, based on the compensation method and the Newton–Raphson algo- rithm (continuous and piecewise), is entirely implemented in Very high speed integrated circuit Hardware Description Language. It also involves sparsity techniques, deeply pipelined arithmetic ﬂoating-point processing, and parallel Gauss–Jordan elimination. To validate the new solver, two case studies are simulated in real time: surge arrester transients in a series-compensated line and ferroresonance transients in a transformer, with time steps of 5 and 3 μs, respectively. The captured real-t

## 核心贡献

- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[补偿法|补偿法]]
- [[牛顿-拉夫逊算法|牛顿-拉夫逊算法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]
- [[深度流水线浮点运算|深度流水线浮点运算]]
- [[并行高斯-约当消元法|并行高斯-约当消元法]]
- [[迭代求解|迭代求解]]

## 涉及的模型

- [[避雷器|避雷器]]
- [[串联补偿线路|串联补偿线路]]
- [[变压器|变压器]]
- [[非线性元件|非线性元件]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

—A real-time transient simulation of nonlinear ele- ments in transmission networks requires signiﬁcant computational power
