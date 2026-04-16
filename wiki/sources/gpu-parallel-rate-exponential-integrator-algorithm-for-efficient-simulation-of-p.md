---
title: "GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of Power Electronic Systems"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Open Access Journal of Power and Energy;2026;13; ;10.1109/OAJPE.2026.3659790"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Paull 等 - 2026 - GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of Power Electronic Syst.pdf"]
---

# GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of Power Electronic Systems

**作者**: 
**年份**: 2026
**来源**: `19、20、21/EMT_task_21/Paull 等 - 2026 - GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of Power Electronic Syst.pdf`

## 摘要

Electromagnetic transient (EMT) simulation of power electronic converters is critical for analysis, design, and fast control prototyping of power and energy systems. This paper proposes a multi- granular GPU parallel-rate exponential integrator (EI) algorithm for fast oﬄine EMT simulation of power electronic systems. The proposed parallel-rate EI algorithm utilizes the massively parallel GPU architecture to compute multiple discretization steps in parallel. The matrix-vector computations of the EI algorithm within each time step are also parallelized. Additionally, a novel GPU-based framework is proposed for numerically eﬃcient precomputation of matrix exponentials before a simulation loop starts. The high degree of parallelism leads to large simulation speedups compared to single-thread C

## 核心贡献


- 提出多粒度GPU并行率指数积分算法，实现多时间步与步内矩阵运算的细粒度并行加速
- 设计GPU端矩阵指数高效预计算框架，通过单次矩阵乘法大幅降低离线计算负载
- 基于密集并行输出点实现无源开关事件精准检测，消除传统过零点迭代求解过程


## 使用的方法


- [[指数积分法|指数积分法]]
- [[gpu并行计算|GPU并行计算]]
- [[多粒度并行仿真|多粒度并行仿真]]
- [[矩阵指数预计算|矩阵指数预计算]]
- [[离散开关事件驱动|离散开关事件驱动]]


## 涉及的模型


- [[电力电子变换器|电力电子变换器]]
- [[二极管-无源开关|二极管/无源开关]]
- [[开关级状态空间模型|开关级状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行加速|GPU并行加速]]
- [[大时间步长积分|大时间步长积分]]
- [[开关事件检测|开关事件检测]]
- [[离线仿真|离线仿真]]


## 主要发现


- 高阶指数积分算法具备L稳定性，大时间步下无虚假数值振荡且精度优于梯形法
- GPU多粒度并行架构相比单线程CPU实现显著加速，有效克服小系统并行延迟瓶颈
- 密集并行输出点可精准捕捉二极管电压电流过零点，避免传统迭代求解带来的误差


