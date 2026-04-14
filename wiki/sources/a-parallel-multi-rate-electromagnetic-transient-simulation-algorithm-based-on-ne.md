---
title: "A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu"
type: source
year: 2023
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/Mu 等 - 2014 - A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu.pdf"]
---

# A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu

**年份**: 2023
**来源**: `03/Mu 等 - 2014 - A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了一种基于传输线分网的并行全隐式多速率电磁暂态仿真算法，显著提升了算法的并行化程度与计算效率
- 建立了全隐式多速率电磁暂态仿真的基本理论模型，并结合传输线方程实现了算法的并行化架构
- 提出了保证并行多速率算法稳定性的网络分网判据，并通过数学理论严格证明了其有效性

## 使用的方法

- [[全隐式多速率积分|全隐式多速率积分]]
- [[内插值法|内插值法]]
- [[传输线分网|传输线分网]]
- [[并行仿真算法|并行仿真算法]]
- [[后退欧拉法|后退欧拉法]]
- [[稳定判据分析|稳定判据分析]]
- [[全隐式积分法|全隐式积分法]]
- [[内插值同步技术|内插值同步技术]]
- [[后退欧拉离散化|后退欧拉离散化]]
- [[传输线分网技术|传输线分网技术]]
- [[基于范数理论的稳定性分析|基于范数理论的稳定性分析]]

## 涉及的模型

- [[vsc-model|VSC]]
- [[柔性交流输电系统-facts|柔性交流输电系统(FACTS)]]
- [[传输线模型|传输线模型]]
- [[大规模电力系统|大规模电力系统]]
- [[电压源型换流器-vsc-模型|电压源型换流器(VSC)模型]]
- [[柔性交流输电系统-facts-模型|柔性交流输电系统(FACTS)模型]]
- [[传输线等效电路模型|传输线等效电路模型]]
- [[电力系统状态空间模型|电力系统状态空间模型]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[多速率仿真|多速率仿真]]
- [[并行计算|并行计算]]
- [[网络划分|网络划分]]
- [[仿真稳定性|仿真稳定性]]
- [[电力电子暂态|电力电子暂态]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[多速率仿真|多速率仿真]]
- [[并行计算|并行计算]]
- [[网络分网策略|网络分网策略]]
- [[数值稳定性分析|数值稳定性分析]]

## 主要发现

- 基于传输线的并行全隐式多速率仿真算法在特定网络划分下可能出现数值失稳现象
- 采用所提稳定判据对网络分网进行优化调整后，可有效消除失稳问题，同时保持较高的并行计算效率
