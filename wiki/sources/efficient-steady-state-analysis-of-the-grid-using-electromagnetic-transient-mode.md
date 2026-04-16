---
title: "Efficient steady state analysis of the grid using electromagnetic transient models"
type: source
authors: ['Aayushya Agarwal']
year: 2022
journal: "Electric Power Systems Research, 213 (2022) 108408. doi:10.1016/j.epsr.2022.108408"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient steady state analysis of the grid using electromagnetic transient models_Agarwal和Pileggi_2022.pdf"]
---

# Efficient steady state analysis of the grid using electromagnetic transient models

**作者**: Aayushya Agarwal
**年份**: 2022
**来源**: `15/Efficient steady state analysis of the grid using electromagnetic transient models_Agarwal和Pileggi_2022.pdf`

## 摘要

Efficient steady state analysis of the grid using electromagnetic Electrical and Computer Engineering Department, Carnegie Mellon University, Pittsburgh, United States of America Modern grids contain an increasing number of non-linear grid devices that are accurately modeled only in the time domain. Performing an accurate steady-state analysis with such models requires a transient simulation to infinite (sufficiently long) time, which can be computationally prohibitive. Power flow provides an ef

## 核心贡献


- 提出基于完整波形迭代的时域稳态分析方法，避免离散时间步长，实现快速收敛
- 利用替代定理解耦线性输电网与非线性设备，避免大规模雅可比矩阵求逆运算
- 通过分离线性与非线性子系统支持并行计算，大幅提升电磁暂态稳态仿真效率


## 使用的方法


- [[谐波平衡法|谐波平衡法]]
- [[波形松弛法|波形松弛法]]
- [[替代定理|替代定理]]
- [[网络解耦|网络解耦]]
- [[时域波形迭代|时域波形迭代]]
- [[线性n端口建模|线性N端口建模]]


## 涉及的模型


- [[线性输电网络|线性输电网络]]
- [[非线性源|非线性源]]
- [[同步调相机|同步调相机]]
- [[非线性负荷|非线性负荷]]
- [[发电机|发电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[14节点测试系统|14节点测试系统]]


## 相关主题


- [[稳态分析|稳态分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[潮流计算对比|潮流计算对比]]
- [[网络解耦|网络解耦]]
- [[并行计算|并行计算]]
- [[时域建模|时域建模]]


## 主要发现


- 所提时域稳态方法比传统电磁暂态逐步积分收敛更快，有效突破大规模系统计算瓶颈
- 潮流计算因单频与平衡假设，其稳态结果与真实电磁暂态模型存在显著偏差
- 线性与非线性子系统解耦可直接支持并行计算，在保持模型精度的同时提升求解速度


