---
title: "Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power Systems"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Open Access Journal of Power and Energy;2020;7; ;10.1109/OAJPE.2020.3012636"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/oajpe.2020.3012636.pdf.pdf"]
---

# Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power Systems

**作者**: 
**年份**: 2020
**来源**: `30/oajpe.2020.3012636.pdf.pdf`

## 摘要

Parallel-in-time methods are emerging to accelerate the solution of time-consuming problems in different research ﬁelds. However, the complexity of power system component models brings challenges to realize the parallel-in-time power system electromagnetic transient (EMT) simulation, including the traveling wave transmission lines. This paper proposes a system-level parallel-in-time EMT simulation method based on traditional nodal analysis and the Parareal algorithm. A new interpretation scheme is proposed to solve the transmission line convergence problem. To integrate different kinds of traditional EMT models, a component- based EMT system solver architecture is proposed to address the increasing model complexity. An object- oriented C++ implementation is proposed to realize the parallel

## 核心贡献


- 提出基于节点分析与Parareal算法的系统级并行电磁暂态仿真方法
- 设计改进插值策略解决行波传输线模型在并行计算中的收敛难题
- 构建组件化面向对象求解器架构实现传统EMT模型灵活集成


## 使用的方法


- [[parareal算法|Parareal算法]]
- [[节点分析法|节点分析法]]
- [[面向对象编程|面向对象编程]]
- [[改进插值策略|改进插值策略]]
- [[多核并行计算|多核并行计算]]


## 涉及的模型


- [[行波传输线模型|行波传输线模型]]
- [[贝杰龙模型|贝杰龙模型]]
- [[微分代数方程系统|微分代数方程系统]]
- [[延迟微分方程模型|延迟微分方程模型]]


## 相关主题


- [[时间并行计算|时间并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[多核并行加速|多核并行加速]]
- [[延迟微分方程求解|延迟微分方程求解]]
- [[组件化建模|组件化建模]]


## 主要发现


- IEEE-118系统测试表明六线程下加速比达2.30倍且并行效率约40%
- 系统时域特性决定Parareal算法加速效果传输线延迟显著影响性能
- 改进插值策略有效解决传输线收敛问题保持与传统串行算法同等精度


