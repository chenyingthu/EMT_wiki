---
title: "Using TACS Functions Within EMPT To Teach Protective Relaying Fundamentals - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/39/59.574917.pdf.pdf"]
---

# Using TACS Functions Within EMPT To Teach Protective Relaying Fundamentals - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `39/59.574917.pdf.pdf`

## 摘要

The purpose of this discussion is to provide an educational tool for investigating relaying concepts by modeling digital relays using TACS functions within EM- in a closed- loop manner. Various elements of digital protection systems are identified and organized to generate an systematic approach to modeling the actual hardware of relay systems. Discussion is lim- ited to conventional relaying systems that monitor the vitality of the 60 Hz voltages and/or currents. TACS functions for transport delay and pulse generators are used to model dynamics associated with analog to digital conversion and sampling systems. DSP algorithms convert a sequence of sampled data into a sequence of values for magnitude and phase components. A simple example of a time overcurrent relay is developed to demonstr

## 核心贡献



- 提出基于EMTP/TACS闭环仿真的数字继电器教学建模框架
- 系统化整合TACS函数以复现继电器ADC采样、DSP算法及保护逻辑
- 开发定时限过流继电器实例以演示EMTP在继电保护教学中的应用

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]
- [[state-space]]

## 涉及的模型


- [[transmission-line]]
- [[transformer]]

## 相关主题

- [[继电保护教学|继电保护教学]]
- [[数字继电器建模|数字继电器建模]]
- [[电力系统仿真教育|电力系统仿真教育]]
- [[保护系统动态特性|保护系统动态特性]]

## 主要发现



- EMTP与TACS结合可有效模拟数字继电器的硬件动态与离散控制过程
- TACS传输延迟与脉冲发生器能准确表征模数转换与采样系统的时序特性
- 该闭环建模方法为继电保护原理教学提供了直观、可交互的仿真环境