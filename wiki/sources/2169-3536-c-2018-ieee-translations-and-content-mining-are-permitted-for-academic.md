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

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[gpu并行计算|GPU并行计算]]
- [[面向线程的模型转换|面向线程的模型转换]]
- [[自动代码生成|自动代码生成]]
- [[simt分组处理|SIMT分组处理]]
- [[融合乘加运算|融合乘加运算]]
- [[线性方程组求解|线性方程组求解]]
- [[基于gpu的并行计算|基于GPU的并行计算]]
- [[面向线程的模型转换|面向线程的模型转换]]
- [[自动代码生成|自动代码生成]]
- [[simt并行架构|SIMT并行架构]]
- [[融合乘加运算|融合乘加运算]]
- [[线性方程组求解|线性方程组求解]]
- [[基于gpu的并行计算|基于GPU的并行计算]]
- [[面向线程的模型转换|面向线程的模型转换]]
- [[自动代码生成|自动代码生成]]
- [[simt并行处理|SIMT并行处理]]
- [[线性方程求解|线性方程求解]]
- [[gpu并行计算|GPU并行计算]]
- [[面向线程的模型转换|面向线程的模型转换]]
- [[自动代码生成|自动代码生成]]
- [[simt分组处理|SIMT分组处理]]
- [[线性方程组求解|线性方程组求解]]

## 涉及的模型

- [[ieee-33节点配电系统|IEEE 33节点配电系统]]
- [[分布式发电机|分布式发电机]]
- [[原始电气元件网络|原始电气元件网络]]
- [[分层有向无环图控制模型|分层有向无环图控制模型]]
- [[ieee-33节点配电系统|IEEE 33节点配电系统]]
- [[分布式电源|分布式电源]]
- [[基本电气元件|基本电气元件]]
- [[基本控制元件|基本控制元件]]
- [[ieee-33节点配电系统|IEEE 33节点配电系统]]
- [[分布式电源|分布式电源]]
- [[基本电气元件|基本电气元件]]
- [[基本控制元件|基本控制元件]]
- [[ieee-33节点配电系统|IEEE 33节点配电系统]]
- [[分布式发电机|分布式发电机]]
- [[原始电气元件网络|原始电气元件网络]]
- [[控制系统分层有向无环图模型|控制系统分层有向无环图模型]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[并行计算|并行计算]]
- [[gpu加速|GPU加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[并行计算|并行计算]]
- [[gpu加速|GPU加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[并行计算|并行计算]]
- [[gpu加速|GPU加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[实时仿真|实时仿真]]
- [[gpu加速|GPU加速]]

## 主要发现

Electromagnetic transients (EMT) simulation is the most accurate and intensive computation for power systems
