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


- 提出LIM与NAM混合的网络解耦算法，实现DG系统并行仿真
- 在单块FPGA上实现亚微秒级实时仿真，大幅降低硬件资源消耗
- 仿真步长不随系统规模增大而增加，满足高频开关精确模拟需求


## 使用的方法


- [[固定导纳模型|固定导纳模型]]
- [[节点分析法-nam|节点分析法(NAM)]]
- [[延迟插入法-lim|延迟插入法(LIM)]]
- [[leap-frog差分格式|Leap-frog差分格式]]
- [[网络解耦算法|网络解耦算法]]


## 涉及的模型


- [[电力电子变流器|电力电子变流器]]
- [[配电线路-电缆|配电线路/电缆]]
- [[π型等效电路|π型等效电路]]
- [[分布式电源-dg|分布式电源(DG)]]
- [[微电网|微电网]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga仿真|FPGA仿真]]
- [[网络解耦|网络解耦]]
- [[混合仿真|混合仿真]]
- [[亚微秒级仿真|亚微秒级仿真]]
- [[微电网建模|微电网建模]]


## 主要发现


- 在Kintex-7 FPGA上实现含21条线路微电网的380ns步长实时仿真
- 相比传统方法显著降低FPGA资源占用，且步长不随规模扩大而增加
- 验证了LIM-NAM混合解耦算法在亚微秒级仿真中的高精度与稳定性


