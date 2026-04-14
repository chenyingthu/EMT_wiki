---
title: "Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive AC/DC Grids"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Energy Conversion;2021;36;3;10.1109/TEC.2020.3043307"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Lin 等 - 2021 - Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive ACDC Grids.pdf"]
---

# Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive AC/DC Grids

**作者**: 
**年份**: 2021
**来源**: `05/Lin 等 - 2021 - Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive ACDC Grids.pdf`

## 摘要

—The increasingly complex AC/DC network as a result of the massive integration of wind farms manifests the signiﬁcance of a comprehensive transient study. In this work, the wind turbine (WT) and the DC grid are modeled in detail for the electromagnetic transient (EMT) simulation to maximize its ﬁdelity, whilst the AC grid transient stability is analyzed by dynamic simulation (DS). An interactive EMT-DS interface is thus introduced to enable their concurrency and subsequently form a co-simulation. The CPU which is dominant in system study faces a tremendous challenge in handling a great number of components albeit they exhibit homogeneity. The many-core graphics processing unit (GPU) fea- turing massive parallelism is therefore exploited and following the deﬁnition of an adaptive computing 

## 核心贡献

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[emt-ds协同仿真|EMT-DS协同仿真]]
- [[gpu并行计算|GPU并行计算]]
- [[异构顺序-并行处理架构|异构顺序-并行处理架构]]
- [[自适应计算边界划分|自适应计算边界划分]]
- [[拓扑重构|拓扑重构]]
- [[simt计算范式|SIMT计算范式]]

## 涉及的模型

- [[dfig-model|DFIG]]
- [[风力发电机-wt|风力发电机(WT)]]
- [[多端直流电网|多端直流电网]]
- [[交流电网|交流电网]]
- [[换流器系统|换流器系统]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态仿真|动态仿真]]
- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[暂态稳定分析|暂态稳定分析]]
- [[风电场并网|风电场并网]]
- [[自适应计算|自适应计算]]

## 主要发现

—The increasingly complex AC/DC network as a result of the massive integration of wind farms manifests the signiﬁcance of a comprehensive transient study
