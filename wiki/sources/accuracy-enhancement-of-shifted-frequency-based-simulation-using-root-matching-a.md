---
title: "Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-Step"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;4;10.1109/TPWRS.2022.3207283"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Gao 等 - 2023 - Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-St.pdf"]
---

# Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-Step

**作者**: 
**年份**: 2023
**来源**: `05/Gao 等 - 2023 - Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-St.pdf`

## 摘要

—Electromagnetic transients (EMT) simulation is fun- damental in power system design and operation. To improve the computational efﬁciency of EMT simulation, the shifted frequency- based EMT (SFEMT) simulation with large time-steps has been proposed in the literature recently. Nevertheless, the existing SFEMT simulation methods with a large time-step have accuracy issues when there is a sudden change in the power system. In this paper, the causes of the poor accuracy of traditional SFEMT simu- lation in sudden-change scenarios are ﬁrst analyzed. Then, it pro- poses a highly accurate SFEMT simulation algorithm based on the root matching (RM) and embedded small-step (ESS) techniques. Next, the RM-based SFEMT (RM-SFEMT) models of the power system components are derived and the ﬂowchart of RM-

## 核心贡献


- 理论揭示大时间步移频仿真在系统突变时的误差形成机制与频谱混叠原因
- 提出基于根匹配的移频建模算法，精确模拟载频与零频附近的高频分量
- 设计嵌入式小步长积分方案，有效消除大时间步下非状态变量的积分丢失


## 使用的方法


- [[移频电磁暂态仿真|移频电磁暂态仿真]]
- [[根匹配法|根匹配法]]
- [[嵌入式小步长|嵌入式小步长]]
- [[希尔伯特变换|希尔伯特变换]]
- [[梯形积分法|梯形积分法]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[感应电机|感应电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[风电机组|风电机组]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步仿真|大时间步仿真]]
- [[移频技术|移频技术]]
- [[突变场景精度分析|突变场景精度分析]]
- [[数值积分误差|数值积分误差]]


## 主要发现


- 在三种不同规模电力系统中验证，所提算法显著提升了突变工况下的仿真精度
- 根匹配技术有效抑制了梯形积分在大时间步下的截断误差，保持计算效率
- 嵌入式小步长方案彻底消除了非状态变量积分丢失问题，波形拟合更精确


