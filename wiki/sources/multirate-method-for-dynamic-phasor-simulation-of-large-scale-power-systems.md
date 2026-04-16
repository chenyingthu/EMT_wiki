---
title: "Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems.pdf"]
---

# Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems

**作者**: 
**年份**: 2026
**来源**: `27&28/Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems.pdf`

## 摘要

Dynamic phasor simulations can be used for the analysis of transient stability (TS) of power systems, considering the influence of fast response equipment such as HVDC converters, FACTS and IBR (Inverter Based Resources). For reliable simulation with fast response equipment, electromagnetic transients (EMT) of the AC network must be accurately modeled. Dynamic phasor simulations are used to solve tightly coupled dynamics from microsecond electromagnetic phenomena to second-scale electromechanical oscillations. The single-rate time step requires the entire model to utilize the smallest interval necessary for accuracy, which can substantially increase runtime. This work proposes a multirate method for a dynamic phasor simulation, where the slowest machine variables and their controllers use 

## 核心贡献


- 提出基于动态相量的统一多速率算法，避免传统EMT-TS联合仿真与模型分区
- 设计快慢变量插值与平均耦合机制，结合误差校验实现步长自适应接受与回退
- 在万节点巴西实际电网验证算法可扩展性，大幅降低计算耗时且保持暂态高保真


## 使用的方法


- [[动态相量法|动态相量法]]
- [[多速率仿真|多速率仿真]]
- [[插值与平均耦合|插值与平均耦合]]
- [[误差校验步长控制|误差校验步长控制]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[发电机控制器|发电机控制器]]
- [[交流输电网络|交流输电网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态相量建模|动态相量建模]]
- [[多速率仿真|多速率仿真]]
- [[大规模电网仿真|大规模电网仿真]]
- [[暂态稳定分析|暂态稳定分析]]


## 主要发现


- 多速率动态相量法在万节点电网中显著降低计算耗时，同时保持电磁与机电暂态高精度
- 快慢变量插值平均耦合策略有效避免接口误差，步长自适应机制保障数值稳定性
- 统一框架下无需模型分区即可准确捕捉微秒级电磁现象与秒级机电振荡的强耦合动态


