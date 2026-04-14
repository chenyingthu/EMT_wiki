---
title: "FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids With a Network-Decoupled Algorithm"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery;2020;35;2;10.1109/TPWRD.2019.2932993"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Xu 等 - 2020 - FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids with a Network-Decoupled Algori.pdf"]
---

# FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids With a Network-Decoupled Algorithm

**作者**: 
**年份**: 2020
**来源**: `19、20、21/EMT_task_20/Xu 等 - 2020 - FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids with a Network-Decoupled Algori.pdf`

## 摘要

—The real-time simulation based on the ﬁeld pro- grammable gate array (FPGA) is receiving more and more at- tention. However, up to now, the simulation scale for the power electronic system is not so satisfactory due to the real-time require- ment and the FPGA resource limitation. This paper proposes a sub-microsecond level real-time simulation method for microgrids. The power converters are modeled with ﬁxed-admittance models and simulated with a compact electromagnetic transients program (EMTP) algorithm. In the meanwhile, the distribution lines/cables are modeled with π-circuit models and simulated with a distributed circuit solution method, called the latency insertion method (LIM). As a result, the distribution generation (DG) systems are decoupled with each other and can be simulated

## 核心贡献

- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[固定导纳模型|固定导纳模型]]
- [[紧凑emtp算法|紧凑EMTP算法]]
- [[π型电路模型|π型电路模型]]
- [[延迟插入法-lim|延迟插入法(LIM)]]
- [[网络解耦算法|网络解耦算法]]
- [[并行仿真|并行仿真]]

## 涉及的模型

- [[电力电子变换器|电力电子变换器]]
- [[配电线路-电缆|配电线路/电缆]]
- [[分布式发电系统|分布式发电系统]]
- [[微电网|微电网]]
- [[三相变流器|三相变流器]]
- [[boost电路|Boost电路]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

—The real-time simulation based on the ﬁeld pro- grammable gate array (FPGA) is receiving more and more at- tention
