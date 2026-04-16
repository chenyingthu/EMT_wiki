---
title: "Modelica-based simulation of electromagnetic transients using Dynaωo: Current status and perspectives"
type: source
authors: ['A. Masoom']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107340. doi:10.1016/j.epsr.2021.107340"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Masoom 等 - 2021 - Modelica-based simulation of electromagnetic transients using Dynaωo Current status and perspective.pdf"]
---

# Modelica-based simulation of electromagnetic transients using Dynaωo: Current status and perspectives

**作者**: A. Masoom
**年份**: 2021
**来源**: `26/Masoom 等 - 2021 - Modelica-based simulation of electromagnetic transients using Dynaωo Current status and perspective.pdf`

## 摘要

ion levels than with classical simulation tools whose codes are based on imperative languages, e.g. Fortran or C++. Modelica has begun to gain interest in the power system community with two European projects: PEGASE [4] and iTesla [5]. These projects, alongside other national or international initiatives coming both from the power system and the Modelica communities, have ended up in the development of several libraries: iPSL [6], OpenIPSL [7], or PowerGrids [8] for phasor-domain simulation. Regarding EMT-type simulations, the first effort in this direction has been done in [9], where Constant Parameter (CP) and Wideband (WB) transmission line models have been implemented and validated against EMTP [10]. The precision obtained with Modelica models and tools is perfect, but the simulation 

## 核心贡献


- 提出C++与Modelica混合架构，实现模型求解器解耦以提升大规模EMT仿真效率
- 设计虚拟方程预编译策略，实现组件独立编译与运行时高效实例化复用
- 集成变步长BDF积分算法，验证混合框架在电磁暂态仿真中的精度与性能优势


## 使用的方法


- [[混合c-modelica建模|混合C++/Modelica建模]]
- [[非因果方程建模|非因果方程建模]]
- [[模型与求解器解耦|模型与求解器解耦]]
- [[变步长变阶bdf积分法|变步长变阶BDF积分法]]
- [[隐式欧拉法|隐式欧拉法]]
- [[稀疏lu分解-klu-nicslu|稀疏LU分解(KLU/NICSLU)]]
- [[虚拟方程预编译技术|虚拟方程预编译技术]]


## 涉及的模型


- [[输电线路-cp-wb模型|输电线路(CP/WB模型)]]
- [[同步电机|同步电机]]
- [[电力变压器|电力变压器]]
- [[避雷器|避雷器]]
- [[电力控制器|电力控制器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[modelica建模|Modelica建模]]
- [[混合仿真架构|混合仿真架构]]
- [[大规模系统仿真|大规模系统仿真]]
- [[数值求解器集成|数值求解器集成]]
- [[仿真性能优化|仿真性能优化]]
- [[非因果建模|非因果建模]]


## 主要发现


- 混合架构显著缩短仿真耗时，在保持建模精度的同时满足工业级计算性能需求
- 解耦设计支持算法灵活替换且免重复编译，大幅降低大规模系统开发调试成本
- IDA求解器结合稀疏矩阵分解在测试案例中验证了数值稳定性与高计算精度


