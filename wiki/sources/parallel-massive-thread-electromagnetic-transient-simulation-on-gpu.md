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

- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[并行计算|并行计算]]
- [[gpu加速|GPU加速]]
- [[节点分析法|节点分析法]]
- [[块节点对角稀疏格式映射|块节点对角稀疏格式映射]]
- [[多线程编程|多线程编程]]

## 涉及的模型

- [[线性无源元件|线性无源元件]]
- [[通用线路模型|通用线路模型]]
- [[通用电机模型|通用电机模型]]
- [[输电线路|输电线路]]
- [[发电机|发电机]]
- [[电力系统节点|电力系统节点]]

## 相关主题

- [[parallel-computing]]

## 主要发现

—The electromagnetic transient (EMT) simulation of a large-scale power system consumes so much computational power that parallel programming techniques are urgently needed in this area
