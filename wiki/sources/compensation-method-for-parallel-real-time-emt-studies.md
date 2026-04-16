---
title: "Compensation method for parallel real-time EMT studies✰"
type: source
authors: ['B. Bruned']
year: 2021
journal: "Electric Power Systems Research, 198 (2021) 107341. doi:10.1016/j.epsr.2021.107341"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/11/Bruned 等 - 2021 - Compensation method for parallel real-time EMT studies✰.pdf"]
---

# Compensation method for parallel real-time EMT studies✰

**作者**: B. Bruned
**年份**: 2021
**来源**: `11/Bruned 等 - 2021 - Compensation method for parallel real-time EMT studies✰.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Compensation method for parallel real-time EMT studies✰ B. Bruned a,*, S. Denneti`ere a, J. Michel a, M. Schudel a, J. Mahseredjian b, N. Bracikowski c The classical solution for computing electromagnetic transients (EMTs) in parallel relies on the propagation delay of transmission lines. The lines are used as decoupling elements to split the network into different tasks. When

## 核心贡献


- 提出基于补偿法的网络解耦策略，解决无自然传播延迟时的并行仿真难题
- 详细设计补偿法在实时EMT环境中的并行实现架构与线程屏障同步机制
- 结合节点导纳矩阵与戴维南等效，实现含开关动作子网的动态阻抗更新


## 使用的方法


- [[补偿法|补偿法]]
- [[节点分析|节点分析]]
- [[戴维南等效|戴维南等效]]
- [[稀疏lu分解|稀疏LU分解]]
- [[并行计算|并行计算]]
- [[网络解耦|网络解耦]]


## 涉及的模型


- [[配电网|配电网]]
- [[r-l线路模型|R-L线路模型]]
- [[动态负荷模型|动态负荷模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[电力电子开关|电力电子开关]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[并行仿真|并行仿真]]
- [[硬件在环|硬件在环]]
- [[网络解耦|网络解耦]]
- [[开关暂态分析|开关暂态分析]]


## 主要发现


- 在600节点配电网测试中，补偿法有效突破线路延迟限制，显著提升并行加速比
- 实时HIL验证表明该方法能准确处理HVDC换流器开关动作，保持数值稳定性
- 补偿任务与子网任务通过屏障机制同步，在离线与实时环境中均实现高效计算


