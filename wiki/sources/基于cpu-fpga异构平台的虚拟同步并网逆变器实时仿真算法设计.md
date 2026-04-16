---
title: "基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/吴盼 等 - 2020 - 基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计.pdf"]
---

# 基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计

**作者**: CNKI
**年份**: 2023
**来源**: `32/吴盼 等 - 2020 - 基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计.pdf`

## 摘要

With the wide application of power electronic devices in power systems, the demand for small time-step (≤ 2μs) electromagnetic transient real-time simulation increases. While a CPU is unable to meet the demand alone, there is a trend to complement it with a Field Programmable Gate Array (FPGA). A CPU-FPGA heterogeneous computing platform available for real-time simulation of virtual synchronous grid-connected inverter system is built. Within it, the circuit part on the FPGA is implemented with an optimized Electro-Magnetic Transient Program (EMTP) algorithm. Constant admittance switch modeling, branch division with parallel processing and high efficiency matrix operation are used to improve real-time performance. The control part on the CPU adopts virtual synchronization control and design

## 核心贡献



- 构建了面向虚拟同步并网逆变器系统的CPU-FPGA异构实时仿真计算平台
- 提出了基于FPGA的优化EMTP算法，结合恒导纳开关建模、支路拆分并行处理与矩阵化高效运算，实现≤2μs小步长电磁暂态仿真

## 使用的方法


- [[fixed-admittance]]
- [[parallel]]
- [[nodal-analysis]]
- [[real-time]]

## 涉及的模型


- [[vsc-model]]

## 相关主题


- [[real-time]]
- [[co-simulation]]

## 主要发现



- CPU-FPGA异构架构结合优化EMTP算法可有效突破单一CPU的计算瓶颈，满足电力电子系统小步长实时仿真需求
- 所提平台的实时仿真波形与Simulink离线仿真结果高度吻合，验证了算法的准确性与FPGA资源利用的高效性