---
title: "Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network partitioning"
type: source
authors: ['Jiale Yu']
year: 2024
journal: "International Journal of Electrical Power and Energy Systems, 162 (2024) 110297. doi:10.1016/j.ijepes.2024.110297"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Yu 等 - 2024 - Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network.pdf"]
---

# Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network partitioning

**作者**: Jiale Yu
**年份**: 2024
**来源**: `13&14/files/Yu 等 - 2024 - Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network.pdf`

## 摘要

International Journal of Electrical Power and Energy Systems Efficient electromagnetic transient simulation for DFIG-based wind farms Jiale Yu, Haoran Zhao ∗, Yibao Jiang ∗, Bing Li, Linghan Meng, Futao Yang School of Electrical Engineering, Shandong University, Jinan, 250061, China Electromagnetic transient (EMT) simulation plays a critical role in understanding the dynamic behavior

## 核心贡献


- 建立核心设备全电磁暂态高效模型，避免频繁矩阵求逆，提升单机计算效率
- 提出设备级细粒度网络解耦方法，降低导纳矩阵维度，突破亚微秒步长限制
- 构建基于OpenMP的可扩展并行框架，计算流程简洁，适应大规模风电场仿真


## 使用的方法


- [[节点分析法|节点分析法]]
- [[细粒度网络解耦|细粒度网络解耦]]
- [[多线程并行计算|多线程并行计算]]
- [[开关函数法|开关函数法]]
- [[集中参数模型|集中参数模型]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[vsc-model|VSC]]
- [[变压器|变压器]]
- [[lcl滤波器|LCL滤波器]]
- [[输电线路|输电线路]]
- [[风电场|风电场]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[风电场建模|风电场建模]]
- [[网络解耦|网络解耦]]
- [[大规模系统仿真|大规模系统仿真]]


## 主要发现


- 50台风机规模下仿真速度提升两个数量级，最大相对误差仅1.68%，兼顾高效与高精度
- 细粒度解耦有效降低导纳矩阵维度，避免亚微秒步长限制，显著提升大规模仿真效率
- 基于OpenMP的并行框架具备强扩展性，随规模扩大仍保持高计算效率与良好加速比


