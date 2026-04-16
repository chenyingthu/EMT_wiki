---
title: "2169-3536 (c) 2018 IEEE. Translations and content mining are permitted for academic research only. Personal use is also "
type: source
authors: ['未知']
year: 2018
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient GPU-based electromagnetic transient simulation for power systems with thread-oriented tran_Song 等_2018.pdf"]
---

# 2169-3536 (c) 2018 IEEE. Translations and content mining are permitted for academic research only. Personal use is also 

**作者**: 
**年份**: 2018
**来源**: `15/Efficient GPU-based electromagnetic transient simulation for power systems with thread-oriented tran_Song 等_2018.pdf`

## 摘要

Electromagnetic transients (EMT) simulation is the most accurate and intensive computation for power systems. Past research has shown the potential of accelerating such simulations using graphics processing units (GPUs). In this paper, an efﬁcient GPU-based parallel EMT simulator is designed. Thread- oriented model transformations are ﬁrst proposed for the electrical and control systems. Following the transformations, the electrical system is represented by connected networks of massive primitive electrical elements, the computations of which can be constructed as massive fused multiply-add operations and solutions to a linear equation. The control systems are represented by a layered directed acyclic graph with primitive control elements that can be dealt with using SIMT groups. Finally, 

## 核心贡献





- 提出面向线程的电气归一化变换，将网络转为基本元件连接，计算统一为FMA操作
- 构建控制系统分层有向无环图，利用SIMT线程组并行处理，突破复杂控制计算瓶颈
- 开发运行时自动代码生成工具，大幅减少GPU寻址与访存，提升内核效率与算法通用性


## 使用的方法





- [[节点分析法|节点分析法]]
- [[gpu并行计算|GPU并行计算]]
- [[面向线程的模型变换|面向线程的模型变换]]
- [[自动代码生成|自动代码生成]]
- [[融合乘加运算|融合乘加运算]]
- [[分层有向无环图建模|分层有向无环图建模]]
- [[simt并行架构|SIMT并行架构]]


## 涉及的模型





- [[ieee-33节点配电系统|IEEE 33节点配电系统]]
- [[分布式电源|分布式电源]]
- [[电力电子变换器|电力电子变换器]]
- [[基本电气元件|基本电气元件]]
- [[交直流混合电网|交直流混合电网]]


## 相关主题





- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行加速|GPU并行加速]]
- [[实时仿真|实时仿真]]
- [[自动代码生成|自动代码生成]]
- [[大规模配电网仿真|大规模配电网仿真]]
- [[异构计算|异构计算]]


## 主要发现





- 在NVIDIA K20x与P100上测试，该方法相比CPU程序显著加速了电磁暂态仿真
- 自动代码生成工具有效降低访存开销，使GPU内核计算效率与线程负载均衡性大幅提升
- 针对含分布式电源的扩展配电系统，该方法在特定规模下成功实现了电磁暂态实时仿真


