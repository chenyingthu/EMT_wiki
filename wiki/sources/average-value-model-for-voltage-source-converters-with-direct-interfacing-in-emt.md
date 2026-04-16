---
title: "Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Energy Conversion;2023;38;3;10.1109/TEC.2022.3220085"
tags: ['average-value', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/09/Ebrahimi和Jatskevich - 2023 - Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution.pdf"]
---

# Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution

**作者**: 
**年份**: 2023
**来源**: `09/Ebrahimi和Jatskevich - 2023 - Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution.pdf`

## 摘要

—Average-value models (AVMs) of high-frequency switching voltage-source converters (VSCs) are indispensable for fast/efﬁcient simulation of VSC-based power systems. However, in EMT/EMTP-type programs large simulation time-steps cannot be utilized with conventional non-iterative interfacings of AVMs due to numerical inaccuracy/instability as a result of a one-time-step interfacing delay. In this letter, a directly-interfaced AVM has been developed for the VSCs which eliminates the interfacing delay and allows large time-steps. This is achieved by formulating the AVM in the nodal form that is solved simultaneously with the overall network nodal equations. The new proposed model is demonstrated to outperform the existing AVMs of VSCs in terms of accuracy at fairly large time steps. Index Term

## 核心贡献


- 提出VSC平均值模型直接接口方法，消除传统间接接口的一步延迟
- 将AVM重构为节点导纳形式，与外部网络节点方程联立同步求解
- 突破大仿真步长下的数值不稳定瓶颈，显著提升系统级仿真效率


## 使用的方法


- [[平均值建模|平均值建模]]
- [[直接接口技术|直接接口技术]]
- [[节点分析法|节点分析法]]
- [[dq坐标变换|dq坐标变换]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[交直流系统|交直流系统]]
- [[戴维南等效电路|戴维南等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步长仿真|大时间步长仿真]]
- [[vsc-model|VSC]]
- [[数值稳定性|数值稳定性]]


## 主要发现


- 消除接口延迟后，仿真步长可显著增大且保持数值稳定与高精度
- 在大时间步长下，新模型精度优于传统间接接口平均值模型
- 节点联立求解有效避免了传统方法因单步延迟引发的数值发散问题


