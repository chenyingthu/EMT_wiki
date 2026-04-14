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

- 应用动态相量法进行宽频暂态分析，兼顾计算效率和精度

## 使用的方法

- [[联合仿真|联合仿真]]
- [[松弛迭代法|松弛迭代法]]
- [[多端口等效技术|多端口等效技术]]
- [[相量插值与提取|相量插值与提取]]
- [[戴维南阻抗频率更新|戴维南阻抗频率更新]]
- [[边界变量时间预测|边界变量时间预测]]

## 涉及的模型

- [[电磁暂态-emt-模型|电磁暂态(EMT)模型]]
- [[相量-pm-模型|相量(PM)模型]]
- [[多端口等效模型|多端口等效模型]]
- [[戴维南等效模型|戴维南等效模型]]
- [[74节点23机测试系统|74节点23机测试系统]]

## 相关主题

- [[co-simulation]]
- [[dynamic-phasor]]

## 主要发现

—Co-simulation opens new opportunities to combine mature ElectroMagnetic Transients (EMT) and Phasor-Mode (PM) solvers, and take advantage of their respective high ac- curacy and execution speed
