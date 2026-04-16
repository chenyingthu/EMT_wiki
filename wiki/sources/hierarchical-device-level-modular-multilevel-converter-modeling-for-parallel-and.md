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


- 提出多层级MMC建模方法，结合拓扑重构与网络等值，降低高阶IGBT计算负担
- 设计CPU/GPU异构协同架构，利用多速率仿真分离非线性器件，实现高效并行求解
- 基于GPU单指令多线程架构，将相同电路单元映射至并行内核，提升换流器仿真速度


## 使用的方法


- [[拓扑重构|拓扑重构]]
- [[网络等值|网络等值]]
- [[多速率仿真|多速率仿真]]
- [[cpu-gpu异构计算|CPU/GPU异构计算]]
- [[节点分析法|节点分析法]]
- [[伴随电路离散化|伴随电路离散化]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[igbt|IGBT]]
- [[续流二极管|续流二极管]]
- [[vsc-hvdc|VSC-HVDC]]
- [[子模块|子模块]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[异构计算|异构计算]]
- [[器件级建模|器件级建模]]
- [[高性能计算|高性能计算]]
- [[vsc-hvdc|VSC-HVDC]]


## 主要发现


- 混合CPU/GPU平台相比传统CPU实现超50倍加速，大幅缩短大规模系统仿真时间
- 方法经ANSYS/Simplorer与PSCAD/EMTDC验证，波形与精度高度吻合
- 拓扑重构与网络等值有效降低导纳矩阵维度，避免数值发散并提升电路求解效率


