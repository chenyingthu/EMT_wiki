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

- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[最小度最大独立集法|最小度最大独立集法]]
- [[细粒度并行计算|细粒度并行计算]]
- [[多输入多输出指令流运算器|多输入多输出指令流运算器]]
- [[状态字与影响字间接修改法|状态字与影响字间接修改法]]
- [[梯形积分法-差分化|梯形积分法（差分化）]]
- [[节点消去法|节点消去法]]

## 涉及的模型

- [[变电站一次系统|变电站一次系统]]
- [[隔离开关|隔离开关]]
- [[挂地线点|挂地线点]]
- [[故障设置点|故障设置点]]
- [[继电保护装置|继电保护装置]]
- [[自动控制装置|自动控制装置]]
- [[磁饱和元件|磁饱和元件]]
- [[伴随电路模型|伴随电路模型]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

Real-time simulation training system for substation based on field-programmable gate array (FPGA) is proposed in order to reduce the construction cost of substation simulation training system and enha
