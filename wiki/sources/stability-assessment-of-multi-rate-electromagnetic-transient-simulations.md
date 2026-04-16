---
title: "Stability Assessment of Multi-Rate Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;6;10.1109/TPWRD.2025.3590630"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/Sinkar 等 - 2025 - Stability Assessment of Multi-Rate Electromagnetic Transient Simulations.pdf"]
---

# Stability Assessment of Multi-Rate Electromagnetic Transient Simulations

**作者**: 
**年份**: 2025
**来源**: `35/Sinkar 等 - 2025 - Stability Assessment of Multi-Rate Electromagnetic Transient Simulations.pdf`

## 摘要

—Multi-rate Electromagnetic Transient (EMT) simu- lations use smaller time-steps for parts of the network requiring greater accuracy, and larger time-steps for the rest of the network. This paper presents an analytical approach for evaluating the stability of multi-rate EMT simulations of linear time-invariant (LTI) networks. It is shown that their resulting discrete time sys- tem is inherently time-periodic. Leveraging this characteristic, a sampled-data time-invariant representation of the simulated net- work is derived. The overall simulation’s numerical stability can then be assessed through eigenvalue analysis. The paper shows that contrary to popular belief, a multi-rate EMT simulation may become unstable even if the well-known A-stable trapezoidal rule is used. The proposed approach

## 核心贡献



- 提出了一种评估线性时不变（LTI）网络多速率电磁暂态（EMT）仿真稳定性的解析方法
- 推导了多速率仿真网络的采样数据时不变表示，并建立了基于特征值分析的数值稳定性评估框架

## 使用的方法


- [[multirate]]
- [[numerical-integration]]
- [[state-space]]
- [[interpolation]]

## 涉及的模型


- [[network-equivalent]]

## 相关主题


- [[multirate]]
- [[numerical-integration]]

## 主要发现



- 多速率EMT仿真生成的离散时间系统本质上是时间周期性的
- 即使采用A稳定的梯形积分法则，多速率EMT仿真仍可能出现数值不稳定现象
- 通过特征值分析采样数据时不变模型可准确预测和评估整体仿真的数值稳定性