---
title: "A Multi-rate Co-simulation of Combined Phasor-Domain and Time-Domain Models for Large-scale Wind Farms"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2019.2936574"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Li 等 - 2020 - A Multi-Rate Co-Simulation of Combined Phasor-Domain and Time-Domain Models for Large-Scale Wind Far.pdf"]
---

# A Multi-rate Co-simulation of Combined Phasor-Domain and Time-Domain Models for Large-scale Wind Farms

**作者**: 
**年份**: 2019
**来源**: `02/Li 等 - 2020 - A Multi-Rate Co-Simulation of Combined Phasor-Domain and Time-Domain Models for Large-Scale Wind Far.pdf`

## 摘要

—In the year 2015-2018, there are many sub- and super-synchronous interaction (S2SI) events, happened in China. However, traditional transient stability models, electro-magnetic transient (EMT) models and hybrid TS and EMT simulation methods fail to capture the desired wide frequency band interac- tions between large-scale AC grids and wind farms. To accurately and efﬁciently capture wide frequency band interactions between AC grids and wind farms, a simulation method which can extend the time-step to 500µs and further adopt the multi-rate structure is highly required. For this objective, we propose a multi-rate co-simulation method, in which the target system is partitioned into electro-magnetic transient (EMT) and shifted frequency phasor (SFP) subsystems, represented by our proposed tra

## 核心贡献


- 提出基于旋转矩阵变换的移频相量模型，将大电网仿真步长扩展至500微秒
- 构建多速率多域传输线及频变接口，实现瞬时值与相量波形同步交互
- 建立相量域与时域结合的多速率联合仿真架构，精准复现次超同步振荡


## 使用的方法


- [[多速率联合仿真|多速率联合仿真]]
- [[移频相量法|移频相量法]]
- [[网络分区|网络分区]]
- [[多域传输线模型|多域传输线模型]]
- [[频变建模|频变建模]]
- [[梯形积分法|梯形积分法]]


## 涉及的模型


- [[大规模交流电网|大规模交流电网]]
- [[风电场|风电场]]
- [[双馈感应发电机|双馈感应发电机]]
- [[输电线路|输电线路]]
- [[移频相量模型|移频相量模型]]
- [[电磁暂态模型|电磁暂态模型]]


## 相关主题


- [[次超同步相互作用|次超同步相互作用]]
- [[宽频带交互分析|宽频带交互分析]]
- [[混合仿真|混合仿真]]
- [[风电场建模|风电场建模]]
- [[频率相关建模|频率相关建模]]
- [[网络分区|网络分区]]


## 主要发现


- 步长扩展至500微秒时，接口模型仍能有效捕捉1000赫兹内宽频交互动态
- 实际系统算例验证表明，该方法在保持高精度的同时显著降低了计算负担
- 成功复现含大规模风电场的交流电网次超同步振荡，验证了多速率架构有效性


