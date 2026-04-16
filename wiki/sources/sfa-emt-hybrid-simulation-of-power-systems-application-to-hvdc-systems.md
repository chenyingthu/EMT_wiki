---
title: "SFA-EMT hybrid simulation of power systems: Application to HVDC systems"
type: source
authors: ['Javier', 'O.', 'Tarazona']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112326. doi:10.1016/j.epsr.2025.112326"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/34/Tarazona 等 - 2026 - SFA-EMT hybrid simulation of power systems Application to HVDC systems.pdf"]
---

# SFA-EMT hybrid simulation of power systems: Application to HVDC systems

**作者**: Javier, O., Tarazona
**年份**: 2025
**来源**: `34/Tarazona 等 - 2026 - SFA-EMT hybrid simulation of power systems Application to HVDC systems.pdf`

## 摘要

SFA-EMT hybrid simulation of power systems: Application to a PSC North America, 155-4299 Canada Way, Burnaby, BC V5G4Y2, Canada b Department of Civil Engineering, University of British Columbia, Vancouver, BC V6T 1Z4, Canada c Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC V6T 1Z4, Canada This paper presents the application of a novel hybrid multirate protocol to interface a Shifted Frequency Analysis

## 核心贡献



- 提出基于MATE框架的新型混合多速率协议，实现SFA与EMT的直接接口，消除时间步延迟、迭代及传输线解耦需求
- 引入并行EMT解法跟踪复数实虚部，允许SFA采用大时间步且无需与EMT时间步成倍数关系，显著提升大规模系统仿真效率

## 使用的方法


- [[co-simulation]]
- [[multirate]]
- [[dynamic-phasor]]
- [[network-equivalent]]

## 涉及的模型


- [[hvdc]]

## 相关主题


- [[hvdc]]
- [[co-simulation]]
- [[multirate]]

## 主要发现



- 该协议成功应用于改进型CIGRE HVDC基准系统，验证了其在含电力电子设备子系统仿真中的有效性与高精度
- 相比纯EMT仿真，SFA-EMT混合多速率方法在频率偏移较小时计算效率显著提升，为大规模电力系统仿真提供了可行的加速方案