---
title: "Computation of the periodic steady state in systems with nonlinear components using a hybrid time and frequency domain methodology"
type: source
authors: ['A. Semlyen', 'A. Medina']
year: 2004
journal: "IEEE Transactions on Power Systems;1995;10;3;10.1109/59.466497"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Computation_of_the_periodic_steady_state_in_systems_with_nonlinear_components_using_a_hybrid_time_and_frequency_domain_methodology.pdf"]
---

# Computation of the periodic steady state in systems with nonlinear components using a hybrid time and frequency domain methodology

**作者**: A. Semlyen, A. Medina
**年份**: 2004
**来源**: `11/Computation_of_the_periodic_steady_state_in_systems_with_nonlinear_components_using_a_hybrid_time_and_frequency_domain_methodology.pdf`

## 摘要

The basic principles of an eficient new methodology for the calculation of the non-sinusoidal periodic steady state in system with nonlinear and timevarying components are described. All linear parts, including the network and part of he loads. are represented in the frequency domain, while nonlinear and time-varying components, mainly loads, are represented in the time domain. This hybrid procegp b iterative, with periodic, non-sinusoidal, bus voltages U inputs for both fiqumcy domain solutions and time domain simulations: a current mismatch is calculated at each bus and used to update the voltages until convergence is reached. Thus the process, but not the solution, is decoupled for the individual harmonics. Its efficiency is enhand by the use of Newton type algorithms for fast convergen

## 核心贡献


- 提出时频混合迭代架构，线性网络频域求解与非线性负载时域仿真结合实现谐波解耦
- 引入庞加莱映射与牛顿型算法加速时域周期稳态收敛，避免传统暂态积分耗时过长
- 构建基于电流失配量与近似导纳矩阵的节点电压更新机制，保障迭代过程全局收敛


## 使用的方法


- [[时频混合迭代法|时频混合迭代法]]
- [[牛顿型加速算法|牛顿型加速算法]]
- [[庞加莱映射|庞加莱映射]]
- [[谐波潮流计算|谐波潮流计算]]
- [[电流失配法|电流失配法]]
- [[变分方程线性化|变分方程线性化]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[非线性负载|非线性负载]]
- [[非线性电感|非线性电感]]
- [[线性网络|线性网络]]


## 相关主题


- [[周期稳态计算|周期稳态计算]]
- [[谐波分析|谐波分析]]
- [[电磁暂态初始化|电磁暂态初始化]]
- [[混合仿真|混合仿真]]
- [[非线性系统求解|非线性系统求解]]


## 主要发现


- 时频混合架构实现谐波解耦，显著降低非线性系统谐波潮流计算维度与内存需求
- 庞加莱映射结合牛顿法加速时域稳态收敛，克服轻阻尼电路传统仿真耗时难题
- 电流失配结合近似导纳矩阵更新电压，确保迭代收敛且兼容不可微非线性特性


