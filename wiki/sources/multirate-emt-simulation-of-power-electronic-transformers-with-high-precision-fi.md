---
title: "Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2026.3656907"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals.pdf"]
---

# Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals

**作者**: 
**年份**: 2025
**来源**: `27&28/Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation of power electronic transformers (PETs) encounters significant computational challenges due to the high switching frequency nature imposing small simulation time step. This paper proposes a multirate simulation method incorporating high-precision firing signals, which enhances the simulation efficiency of PETs by reducing the number of numerical operations within specified simulation durations. Unlike the existing methods that utilize simplified models with unanimous simulation time step, the proposed approach leverages the inherent frequency disparities in multi-level conversion circuits of PETs to partition the entire system into distinct subsystems. They each are simulated with different time steps optimized for their specific frequencies 

## 核心贡献


- 提出多端口诺顿与电流源等效交互方法，避免子系统导纳矩阵频繁重构
- 设计交错等效多速率交互算法，消除数据延迟，实现器件级多速率仿真
- 构建基于改进节点分析的高精度触发DAB模型，扩大快子系统仿真步长


## 使用的方法


- [[多速率仿真|多速率仿真]]
- [[改进节点分析法|改进节点分析法]]
- [[多端口诺顿等效|多端口诺顿等效]]
- [[电流源等效|电流源等效]]
- [[交错等效交互算法|交错等效交互算法]]
- [[高精度触发信号技术|高精度触发信号技术]]


## 涉及的模型


- [[电力电子变压器|电力电子变压器]]
- [[级联h桥|级联H桥]]
- [[双有源桥|双有源桥]]
- [[高频隔离变压器|高频隔离变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[多速率仿真|多速率仿真]]
- [[电力电子变压器|电力电子变压器]]
- [[高频开关建模|高频开关建模]]
- [[仿真加速|仿真加速]]
- [[器件级划分|器件级划分]]


## 主要发现


- 多工况验证表明，该方法在保持单速率精度的同时显著降低了数值计算量
- 高精度触发信号使高频子系统步长大幅扩大，且完整保留了开关瞬态特征
- 交错等效机制有效消除了接口数据延迟，确保了多速率仿真的数值稳定性


