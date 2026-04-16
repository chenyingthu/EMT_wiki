---
title: "The fdLoad model for accurate frequency dynamics in the SFA-EMT simulator"
type: source
authors: ['Masoud', 'Hajiakbari', 'Fini']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112325. doi:10.1016/j.epsr.2025.112325"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/Fini 等 - 2026 - The fdLoad model for accurate frequency dynamics in the SFA-EMT simulator.pdf"]
---

# The fdLoad model for accurate frequency dynamics in the SFA-EMT simulator

**作者**: Masoud, Hajiakbari, Fini
**年份**: 2025
**来源**: `37/Fini 等 - 2026 - The fdLoad model for accurate frequency dynamics in the SFA-EMT simulator.pdf`

## 摘要

The fdLoad model for accurate frequency dynamics in the SFA-EMT a Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC, V6T 1Z4, Canada b Department of Civil Engineering, University of British Columbia, Vancouver, BC, V6T 1Z4, Canada Due to the reduction in the system’s total mechanical inertia, frequency swing deviations increase with the penetration of inverter-based resources (IBR). For frequency swings, transient stability programs usually model

## 核心贡献



- 提出fdLoad（频率相关负荷）合成模型并将其集成至SFA-EMT仿真器中
- 验证了SFA-EMT方法通过在每一步隐式求解频率，能够以相量域的计算成本实现高精度的频率动态仿真

## 使用的方法


- [[dynamic-phasor]]
- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[frequency-dependent]]

## 相关主题


- [[frequency-dependent]]
- [[dynamic-phasor]]

## 主要发现



- 在低惯量系统发生切负荷等扰动时，采用频率相关负荷模型会显著影响系统的最大频率偏差
- SFA-EMT结合fdLoad模型可在避免全系统EMT高昂计算成本的同时，准确捕捉负荷频率特性对暂态稳定性的影响