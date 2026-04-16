---
title: "Benchmark High-Fidelity EMT Models for Power"
type: source
authors: ['未知']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Marthi 等 - 2024 - Benchmark High-Fidelity EMT Models for Power Grid with PV Plants.pdf"]
---

# Benchmark High-Fidelity EMT Models for Power

**作者**: 
**年份**: 2023
**来源**: `10/Marthi 等 - 2024 - Benchmark High-Fidelity EMT Models for Power Grid with PV Plants.pdf`

## 摘要

—In recent times electromagnetic transient (EMT) modeling tools have been identiﬁed as one of the most important requirements in replicating, analyzing, and investigating the dynamics of the power grid with photovoltaic (PV) plants. However, there are no benchmark models for power grid with PVs to investigate emerging challenges with higher penetration of PVs (like trips and momentary cessations during faults from a region faraway). To this end, in this paper, benchmark high- ﬁdelity EMT dynamic models of power grid with large-scale PV plants are presented. The models are developed in PSCAD and PSCAD/Fortran. Simulation results for different use cases (events) and scenarios are presented. Index Terms—PV plant, EMT simulation, PV inverter. I. INTRODUCTION The penetration of large-scale inve

## 核心贡献


- 提出含多光伏电站的IEEE-39节点系统高保真EMT基准模型并开源
- 采用Kron降阶与多阶离散化技术显著提升大规模光伏阵列仿真计算速度
- 构建匹配实际硬件时序的多速率分层控制架构实现控制器协同仿真


## 使用的方法


- [[微分代数方程|微分代数方程]]
- [[二阶梯形积分|二阶梯形积分]]
- [[kron降阶法|Kron降阶法]]
- [[dae聚类与聚合|DAE聚类与聚合]]
- [[多阶离散化|多阶离散化]]
- [[混合离散化|混合离散化]]
- [[多速率仿真|多速率仿真]]
- [[lu分解|LU分解]]


## 涉及的模型


- [[光伏电站|光伏电站]]
- [[光伏逆变器|光伏逆变器]]
- [[电站级控制器|电站级控制器]]
- [[变压器|变压器]]
- [[架空输电线路|架空输电线路]]
- [[地下电缆|地下电缆]]
- [[并联电容器|并联电容器]]
- [[ieee-39节点系统|IEEE-39节点系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高比例光伏并网|高比例光伏并网]]
- [[逆变器并网资源建模|逆变器并网资源建模]]
- [[故障扰动分析|故障扰动分析]]
- [[多速率控制|多速率控制]]
- [[仿真加速技术|仿真加速技术]]
- [[基准模型开发|基准模型开发]]


## 主要发现


- 模型在多种故障与短路比场景下准确复现高渗透率光伏集群的部分功率损失动态
- Kron降阶与混合离散化有效缩减矩阵规模显著提升大规模光伏EMT仿真速度
- 多速率控制架构匹配实际硬件时序成功验证逆变器保护与电站级控制的协同仿真


