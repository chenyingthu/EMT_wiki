---
title: "Compacting and partitioning‐based simulation solution for frequency‐dependent network equivalents in real‐time digital simulator"
type: source
authors: ['未知']
year: 2020
journal: "IET Generation Trans & Dist 2015.9:2526-2533"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/10/Hu 等 - 2015 - Compacting and partitioning-based simulation solution for frequency-dependent network equivalents in.pdf"]
---

# Compacting and partitioning‐based simulation solution for frequency‐dependent network equivalents in real‐time digital simulator

**作者**: 
**年份**: 2020
**来源**: `10/Hu 等 - 2015 - Compacting and partitioning-based simulation solution for frequency-dependent network equivalents in.pdf`

## 摘要

Rational models of frequency-dependent network equivalents (FDNEs) have been used in real-time digital simulator (RTDS) for power-system simulation. However, this can lead to a computational burden issue; the application of FDNEs may result in a loss of real-time simulation features because the computational cost of the FDNE component exceeds the limits of RTDS. The authors describe a solution that combines compacting and partitioning of the FDNEs, whereby the former reduces the redundancy in the mathematical model and the latter allows us to exploit parallel computer architectures. Then they describe the results of numerical simulations that demonstrate the effectiveness of the approach. Moreover, the proposed simulation solution is not limited to the applications of FDNEs in RTDS, it sol

## 核心贡献


- 提出基于奇异值分解的模型压缩方法，消除状态变量冗余以降低计算量
- 设计FDNE模块划分策略，拆分等效网络以适配RTDS并行计算架构
- 融合压缩与划分技术，解决大规模频变网络等值实时仿真算力瓶颈


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[奇异值分解|奇异值分解]]
- [[状态空间实现|状态空间实现]]
- [[梯形积分法|梯形积分法]]
- [[并行计算|并行计算]]
- [[模型压缩|模型压缩]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[有理函数模型|有理函数模型]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[并行计算|并行计算]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[计算加速|计算加速]]


## 主要发现


- 计算量公式证明瓶颈源于端口与极点数，压缩法有效消除冗余状态变量
- 划分策略将计算负载分散至多处理器，成功恢复系统实时仿真运行能力
- 数值实验验证组合方案大幅降低单步耗时，彻底解决RTDS局部过载问题


