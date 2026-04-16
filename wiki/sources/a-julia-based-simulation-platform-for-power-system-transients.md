---
title: "A Julia-based simulation platform for power system transients"
type: source
authors: ['A. Alsabbagh']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112307. doi:10.1016/j.epsr.2025.112307"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Naidjate 等 - 2025 - A Julia-Based Simulation Platform for Power System Transients.pdf"]
---

# A Julia-based simulation platform for power system transients

**作者**: A. Alsabbagh
**年份**: 2025
**来源**: `02/Naidjate 等 - 2025 - A Julia-Based Simulation Platform for Power System Transients.pdf`

## 摘要

A Julia-based simulation platform for power system transients Polytechnique Montr´eal, Department of Electrical Engineering, Montr´eal-QC, H3T 1J4, Canada This paper implements and tests an EMT-type simulator, using Julia, a high-level and high-performance pro­ gramming language. The designed simulator is compared with EMTP® in terms of accuracy and performance. Several developments are applied to enhance the performance of the designed Julia simulator. The presented

## 核心贡献


- 开发基于Julia的EMT仿真平台JSEMT，兼顾高级语言灵活性与高性能计算。
- 采用MANA节点分析法构建网络方程，显式处理开关状态，支持任意拓扑。
- 引入KLU稀疏矩阵求解、重因式分解优化及CPU并行技术，显著提升仿真速度。


## 使用的方法


- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[梯形积分法|梯形积分法]]
- [[牛顿迭代法|牛顿迭代法]]
- [[分段线性化|分段线性化]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[并行计算|并行计算]]
- [[符号分解优化|符号分解优化]]


## 涉及的模型


- [[rlc支路|RLC支路]]
- [[理想变压器|理想变压器]]
- [[非线性电感|非线性电感]]
- [[非线性电阻|非线性电阻]]
- [[输电线路|输电线路]]
- [[同步电机|同步电机]]
- [[同步电机控制系统|同步电机控制系统]]
- [[开关|开关]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高性能计算|高性能计算]]
- [[并行计算|并行计算]]
- [[网络方程求解|网络方程求解]]
- [[电力系统暂态分析|电力系统暂态分析]]


## 主要发现


- JSEMT在IEEE 39节点系统测试中，仿真精度与商业软件EMTP高度一致。
- 引入KLU求解器与重因式分解优化后，矩阵求解效率显著提升，缩短计算时间。
- CPU并行化技术有效加速大规模网络暂态仿真，验证了Julia平台的高性能潜力。


