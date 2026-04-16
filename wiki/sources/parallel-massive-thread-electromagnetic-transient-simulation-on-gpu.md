---
title: "Parallel Massive-Thread Electromagnetic Transient Simulation on GPU"
type: source
authors: ['未知']
year: 2014
journal: "IEEE Transactions on Power Delivery;2014;29;3;10.1109/TPWRD.2013.2297119"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/Zhou和Dinavahi - 2014 - Parallel Massive-Thread Electromagnetic Transient Simulation on GPU.pdf"]
---

# Parallel Massive-Thread Electromagnetic Transient Simulation on GPU

**作者**: 
**年份**: 2014
**来源**: `30/Zhou和Dinavahi - 2014 - Parallel Massive-Thread Electromagnetic Transient Simulation on GPU.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation of a large-scale power system consumes so much computational power that parallel programming techniques are urgently needed in this area. For example, realistic-sized power systems include thousands of buses, generators, and transmission lines. Massive-thread com- puting is one of the key developments that can increase the EMT computational capabilities substantially when the processing unit has enough hardware cores. Compared to the traditional CPU, the graphic-processing unit (GPU) has many more cores with dis- tributed memory which can offer higher data throughput. This paper proposes a massive-thread EMT program (MT-EMTP) and develops massive-thread parallel modules for linear passive ele- ments, the universal line model, and the universa

## 核心贡献


- 提出基于GPU的EMT仿真程序，实现线性元件、通用线路与电机模型的并行计算。
- 设计节点映射与分块调整方法，将导纳矩阵转为块对角稀疏格式以适配GPU架构。


## 使用的方法


- [[节点分析法|节点分析法]]
- [[cuda并行编程|CUDA并行编程]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[分块节点调整|分块节点调整]]
- [[通用线路模型算法|通用线路模型算法]]


## 涉及的模型


- [[线性无源元件|线性无源元件]]
- [[通用线路模型|通用线路模型]]
- [[通用同步电机模型|通用同步电机模型]]
- [[输电线路|输电线路]]
- [[同步电机|同步电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行计算|GPU并行计算]]
- [[大规模电网建模|大规模电网建模]]
- [[离线仿真|离线仿真]]
- [[稀疏网络求解|稀疏网络求解]]


## 主要发现


- 在2458节点三相系统中验证，仿真精度与EMTP-RV相当，计算速度显著提升。
- 块对角稀疏导纳矩阵结构有效降低GPU内存访问冲突，大幅提升众核数据吞吐率。
- 并行模块在大规模测试系统中展现出良好的可扩展性，满足高数据吞吐量需求。


