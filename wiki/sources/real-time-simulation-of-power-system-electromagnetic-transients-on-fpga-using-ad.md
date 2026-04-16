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



- 提出全双精度与混合精度浮点计算方案，以在FPGA电磁暂态仿真中实现数值精度与计算资源成本的最佳平衡
- 开发可调流水线、动态地址访问与序列控制器技术，优化高扇出与长数据路径的硬件实现资源与时序约束
- 基于元件级灵敏度分析提出系统级混合精度方案，在保持接近全双精度精度的同时平均减少20%的FPGA资源占用

## 使用的方法


- [[real-time]]
- [[parallel]]
- [[numerical-integration]]

## 涉及的模型


- [[synchronous-machine]]
- [[mmc-model]]
- [[transmission-line]]

## 相关主题


- [[real-time]]
- [[hvdc]]
- [[synchronous-machine]]

## 主要发现



- 对于非旋转元件，全双精度与全单精度计算均表现出优异的收敛性
- 针对具有强非线性的旋转元件（同步电机），仅全双精度计算能够有效避免相位偏移问题
- 系统级混合精度方案在Kundur测试系统中实现了与全双精度方案相近的仿真精度，并平均降低了20%的硬件资源消耗