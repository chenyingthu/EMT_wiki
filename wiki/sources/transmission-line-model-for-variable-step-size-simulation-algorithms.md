---
title: "Transmission line model for variable step size simulation algorithms"
type: source
authors: ['未知']
year: 1999
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/39/s0142-0615%2898%2900042-8.pdf.pdf"]
---

# Transmission line model for variable step size simulation algorithms

**作者**: 
**年份**: 1999
**来源**: `39/s0142-0615%2898%2900042-8.pdf.pdf`

## 摘要

In this paper, we describe a novel modeling approach for transmission lines that overcomes the maximum step size constraint of regular line models used in electromagnetic transients programs. The new model allows us to accurately simulate wave propagation phenomena as well as low network frequency variations with maximum efﬁciency, as the simulation step size is no longer restricted to model requirements, but can be adjusted according to the current transient state of the network. The model was tested with a CIGRE line energization case study which was performed utilizing a variable simulation step size algorithm for a combined study of electromagnetic transients and transient stability. q 1998 Elsevier Science Ltd. All rights reserved. Keywords: Transmission line modeling; Electromagnetic

## 核心贡献



- 提出了一种突破传统EMTP线路模型最大步长限制的新型输电线路建模方法
- 实现了基于网络暂态状态动态调整步长的仿真算法，兼顾电磁暂态波传播与低频机电暂态的精度与效率

## 使用的方法


- [[numerical-integration]]
- [[interpolation]]

## 涉及的模型


- [[transmission-line]]
- [[frequency-dependent]]

## 相关主题


- [[co-simulation]]
- [[network-equivalent]]

## 主要发现



- 新模型成功解除了传统线路模型对仿真步长必须小于等于最小波传播时间的严格约束
- CIGRE线路投切测试表明，变步长算法结合新模型能高效准确地同时捕捉电磁暂态波传播与低频网络频率变化