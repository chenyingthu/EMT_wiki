---
title: "Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precision Calculations"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;4;10.1109/TPWRS.2022.3199181"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/32/Ma 等 - 2023 - Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precisi.pdf"]
---

# Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precision Calculations

**作者**: 
**年份**: 2023
**来源**: `32/Ma 等 - 2023 - Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precisi.pdf`

## 摘要

—The massive integration of renewable energy sources and power electronics into the power grid leads to the strong need of real-time Electromagnetic Transients (EMT) simulation of power system using ﬁeld-programmable gate array (FPGA) platform due to its high efﬁciency and superior performance. FPGA based EMT simulations – A key for Digital Twin were mainly based on Single-Precision calculations, but ignored potential accumulation displacement. To address this problem, this paper proposes full Double-Precision and Mixed-Precision Floating-Point schemes to achieve optimal balance between numerical accuracy and com- putational resource cost in FPGA-based EMT simulation even for long duration simulations. Furthermore, adjustable pipeline, address dynamic access and sequence controller techniq

## 核心贡献

- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[自适应混合精度计算|自适应混合精度计算]]
- [[全双精度浮点方案|全双精度浮点方案]]
- [[全单精度浮点方案|全单精度浮点方案]]
- [[可调流水线技术|可调流水线技术]]
- [[地址动态访问技术|地址动态访问技术]]
- [[序列控制器技术|序列控制器技术]]
- [[单精度迭代法|单精度迭代法]]
- [[组件级灵敏度分析|组件级灵敏度分析]]

## 涉及的模型

- [[同步发电机-sg|同步发电机(SG)]]
- [[mmc-model|MMC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[输电线路|输电线路]]
- [[kundur测试系统|Kundur测试系统]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

—The massive integration of renewable energy sources and power electronics into the power grid leads to the strong need of real-time Electromagnetic Transients (EMT) simulation of power system using ﬁ
