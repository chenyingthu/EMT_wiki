---
title: "An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2024;39;1;10.1109/TPWRS.2023.3262584"
tags: ['mmc', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration.pdf"]
---

# An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration

**作者**: 
**年份**: 2023
**来源**: `07&08/An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration.pdf`

## 摘要

—Electromagnetic transient (EMT) simulation is criti- cal and fundamental in the design and operation of the modular multilevel converter (MMC). This article proposes a highly efﬁ- cient EMT simulation model for MMC based on hybrid numerical integration. The topology and operational principle of MMC are elaborated ﬁrst. Based on this, an efﬁcient simulation model for MMC is proposed. Each arm of the MMC is reduced to a two-node Norton equivalent circuit in the main network simulation. The computation of the capacitor dynamic equations is decoupled from that of the arm inductor dynamic equation. They are computed in a leapfrog manner. This makes the equivalent conductance of the MMC arm constant and greatly improves the simulation efﬁciency. Moreover, the dynamic equations of the capacitors

## 核心贡献


- 提出基于中点法与梯形法混合积分的MMC模型，实现桥臂等效电导恒定
- 将桥臂电感与子模块电容动态方程解耦并采用蛙跳法计算，降低矩阵维度
- 将LIM思想融入EMTP求解框架并引入临界阻尼调整，兼顾精度与效率


## 使用的方法


- [[混合数值积分|混合数值积分]]
- [[中点法|中点法]]
- [[梯形法|梯形法]]
- [[节点分析法|节点分析法]]
- [[诺顿等效|诺顿等效]]
- [[临界阻尼调整|临界阻尼调整]]
- [[延迟插入法|延迟插入法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[桥臂电感|桥臂电感]]
- [[子模块电容|子模块电容]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[恒定电导建模|恒定电导建模]]
- [[模型解耦|模型解耦]]
- [[大规模电力系统仿真|大规模电力系统仿真]]
- [[emtp型求解|EMTP型求解]]


## 主要发现


- 桥臂等效电导恒定避免了频繁LU分解，显著提升大规模系统仿真效率
- 多工况仿真验证表明，该模型在保持高精度的同时大幅缩短计算时间
- 子模块电容方程相互解耦，有效降低了节点方程维度与内存占用


