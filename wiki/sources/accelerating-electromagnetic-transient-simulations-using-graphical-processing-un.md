---
title: "Accelerating electromagnetic transient simulations using graphical processing units"
type: source
authors: ['Devin Aluthge']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112314. doi:10.1016/j.epsr.2025.112314"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf"]
---

# Accelerating electromagnetic transient simulations using graphical processing units

**作者**: Devin Aluthge
**年份**: 2025
**来源**: `05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf`

## 摘要

Accelerating electromagnetic transient simulations using graphical b Manitoba Hydro International, Winnipeg, MB, Canada This paper explores and evaluates various approaches to accelerate Electromagnetic Transient (EMT) sim- ulations of power systems using Graphical Processing Units (GPUs). Existing EMT simulation methods face computational challenges in systems with extensive renewable energy sources due to the complexity

## 核心贡献


- 提出全GPU驻留的EMT网络求解架构，彻底消除主机与设备间通信开销。
- 系统评估KLU、Cholesky及Woodbury公式在GPU稀疏求解器上的适配性。
- 针对含高频开关的大规模电网，实现高效稀疏导纳矩阵并行求解算法。


## 使用的方法


- [[klu分解|KLU分解]]
- [[cholesky分解|Cholesky分解]]
- [[woodbury公式|Woodbury公式]]
- [[补偿法|补偿法]]
- [[gpu稀疏求解|GPU稀疏求解]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[ieee-39节点系统|IEEE 39节点系统]]
- [[变压器|变压器]]
- [[同步发电机|同步发电机]]
- [[π型输电线路|π型输电线路]]
- [[逆变器接口电源|逆变器接口电源]]
- [[电力电子换流器|电力电子换流器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行加速|GPU并行加速]]
- [[大规模电网仿真|大规模电网仿真]]
- [[高频开关动态|高频开关动态]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[新能源并网|新能源并网]]


## 主要发现


- cuDSS求解器在中小规模及万阶导纳矩阵测试中，计算耗时均显著低于CPU基准算法。
- GPU全驻留架构有效克服了频繁网络拓扑变化导致的矩阵重复分解瓶颈。
- 针对含大量电力电子设备的大规模系统，GPU方案可实现数量级的仿真提速。


