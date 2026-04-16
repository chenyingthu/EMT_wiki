---
title: "基于FPGA的变电站实时仿真培训系统"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/张炳达和王岚禹 - 2017 - 基于FPGA的变电站实时仿真培训系统.pdf"]
---

# 基于FPGA的变电站实时仿真培训系统

**作者**: 
**年份**: 2025
**来源**: `33/张炳达和王岚禹 - 2017 - 基于FPGA的变电站实时仿真培训系统.pdf`

## 摘要

Real-time simulation training system for substation based on field-programmable gate array (FPGA) is proposed in order to reduce the construction cost of substation simulation training system and enhance the quality of real-time digital simulation. A minimum degree maximum independent set method is adopted to arrange the sequence of nodes elimination and voltage computation, which has a good balance of computation burden and degree of parallelism. Fine granularity parallel computing is realized by adopting a multi-input and multi-output instruction stream arithmetic unit, therefore improving FPGA resource utilization. The simulation parameters are indirectly modified by the status word and effect word, thus reducing the simulation time and saving data memory space. Simulation example shows

## 核心贡献



- 提出基于FPGA的变电站实时仿真培训系统，采用最小度最大独立集法优化节点消去与电压计算顺序，有效平衡计算负载与并行度。
- 设计多输入多输出指令流运算器实现细粒度并行计算，并提出基于状态字和影响字的参数间接修改方法，显著提升FPGA资源利用率并降低存储与计算开销。

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]

## 相关主题


- [[real-time]]
- [[parallel]]

## 主要发现



- 所提架构可在单块EP4CGX150 FPGA芯片上以40 μs步长稳定运行542节点变电站模型。
- 细粒度并行计算与参数间接修改策略大幅提高了硬件资源利用率，同时有效减少了仿真计算时间与数据存储空间占用。