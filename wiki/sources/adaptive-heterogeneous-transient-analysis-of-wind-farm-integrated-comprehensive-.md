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


- 提出EMT-DS交互接口，实现风机直流网电磁暂态与交流网机电暂态并发协同仿真
- 构建自适应CPU-GPU异构架构，按组件同质性灵活分配串行与并行计算任务
- 对双馈风机进行拓扑重构与解耦，生成低维子系统以适配GPU的SIMT并行范式


## 使用的方法


- [[emt-ds协同仿真|EMT-DS协同仿真]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]
- [[拓扑重构与内部解耦|拓扑重构与内部解耦]]
- [[梯形积分法离散化|梯形积分法离散化]]
- [[状态空间建模|状态空间建模]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[风力发电机|风力发电机]]
- [[交直流电网|交直流电网]]
- [[多端直流电网|多端直流电网]]
- [[变压器|变压器]]
- [[变流器|变流器]]
- [[感应电机|感应电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[风电场建模|风电场建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[异构计算架构|异构计算架构]]
- [[系统稳定性分析|系统稳定性分析]]


## 主要发现


- 所提异构框架相比纯CPU计算实现显著加速，大幅提升大规模风电场仿真效率
- 仿真结果与PSCAD及DSATools对比验证，模型精度满足工程分析要求
- 拓扑重构有效降低系统数值阶数并提升同质性，充分释放GPU大规模并行算力


