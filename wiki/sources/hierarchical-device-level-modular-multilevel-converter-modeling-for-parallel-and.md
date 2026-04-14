---
title: "Hierarchical Device-Level Modular Multilevel Converter Modeling for Parallel and Heterogeneous Transient Simulation of HVDC Systems"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Open Journal of Power Electronics;2020;1; ;10.1109/OJPEL.2020.3016296"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/OJPEL.2020.3016296.pdf.pdf"]
---

# Hierarchical Device-Level Modular Multilevel Converter Modeling for Parallel and Heterogeneous Transient Simulation of HVDC Systems

**作者**: 
**年份**: 2020
**来源**: `19、20、21/EMT_task_21/OJPEL.2020.3016296.pdf.pdf`

## 摘要

System-level electromagnetic transient (EMT) simulation of large-scale power converters with high-order nonlinear semiconductor switch models remains a challenge albeit it is essential for design pre- view. In this work, a multi-layer hierarchical modeling methodology is proposed for high-performance com- puting of the modular multilevel converter involving device-level IGBT/diode models. The computational burden induced by converter scale and model complexity is dramatically alleviated following the proposal of topological reconﬁguration and network equivalence, which create a substantial number of identical circuit units that facilitate massively parallel processing on the graphics processing unit (GPU), using the kernel-based single-instruction multi-threading computing architecture. As

## 核心贡献

- 提出了一种改进的mmc建模方法，提高了EMT仿真效率和精度
- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[多层级建模|多层级建模]]
- [[拓扑重构|拓扑重构]]
- [[网络等效|网络等效]]
- [[gpu并行计算|GPU并行计算]]
- [[单指令多线程-simt-架构|单指令多线程(SIMT)架构]]
- [[cpu-gpu异构计算|CPU/GPU异构计算]]
- [[多速率仿真|多速率仿真]]
- [[非线性模型分离|非线性模型分离]]

## 涉及的模型

- [[mmc-model]]

## 相关主题

- [[parallel-computing]]

## 主要发现

System-level electromagnetic transient (EMT) simulation of large-scale power converters with high-order nonlinear semiconductor switch models remains a challenge albeit it is essential for design pre-
