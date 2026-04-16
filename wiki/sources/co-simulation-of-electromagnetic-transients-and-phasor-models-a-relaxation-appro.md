---
title: "Co-Simulation of electromagnetic transients and Phasor models: A relaxation approach"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Plumier 等 - 2016 - Co-Simulation of electromagnetic transients and Phasor models A relaxation approach.pdf"]
---

# Co-Simulation of electromagnetic transients and Phasor models: A relaxation approach

**作者**: 
**年份**: 2016
**来源**: `10/Plumier 等 - 2016 - Co-Simulation of electromagnetic transients and Phasor models A relaxation approach.pdf`

## 摘要

—Co-simulation opens new opportunities to combine mature ElectroMagnetic Transients (EMT) and Phasor-Mode (PM) solvers, and take advantage of their respective high ac- curacy and execution speed. In this paper, a relaxation approach is presented, iterating between an EMT and a PM solver. This entails interpolating over time the phasors of the PM simula- tion, extracting phasors from the time evolutions of the EMT simulation, and representing each sub-system by a proper multi- port equivalent when simulating the other sub-system. Various equivalents are reviewed and compared in terms of convergence of the PM-EMT iterations. The paper also considers the update with frequency of the Thévenin impedances involved in the EMT simulation, the possibility to compute the EMT solution only once per t

## 核心贡献


- 提出基于松弛迭代的EMT与相量模式联合仿真框架，采用多端口等效实现边界耦合。
- 引入戴维南阻抗频率更新与边界预测机制，加速迭代收敛并减少EMT计算次数。
- 对比多种边界等效模型收敛特性，在74节点多接口大系统中验证算法有效性。


## 使用的方法


- [[松弛迭代法|松弛迭代法]]
- [[多速率仿真|多速率仿真]]
- [[时间插值|时间插值]]
- [[相量提取|相量提取]]
- [[多端口戴维南等效|多端口戴维南等效]]
- [[边界变量预测|边界变量预测]]


## 涉及的模型


- [[相量模式模型|相量模式模型]]
- [[电磁暂态模型|电磁暂态模型]]
- [[频率相关网络等效|频率相关网络等效]]
- [[戴维南等效网络|戴维南等效网络]]
- [[同步电机|同步电机]]
- [[输电网络|输电网络]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[联合仿真|联合仿真]]
- [[网络等值|网络等值]]
- [[多速率仿真|多速率仿真]]
- [[边界条件处理|边界条件处理]]
- [[迭代收敛加速|迭代收敛加速]]


## 主要发现


- 多端口戴维南等效有效计及接口耦合，显著提升松弛迭代收敛速度与精度。
- 戴维南阻抗频率更新与边界预测策略可减少EMT单步计算量，保持仿真稳定。
- 74节点系统验证表明该方法支持多接口划分，且能准确复现系统暂态过程。


