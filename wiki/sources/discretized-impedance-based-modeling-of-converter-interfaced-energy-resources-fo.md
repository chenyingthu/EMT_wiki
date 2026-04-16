---
title: "Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Real-Time EMT Simulators"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Open Journal of Power Electronics;2025;6; ;10.1109/OJPEL.2024.3525019"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Vahabzadeh 等 - 2025 - Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Bas.pdf"]
---

# Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Real-Time EMT Simulators

**作者**: 
**年份**: 2025
**来源**: `13&14/files/Vahabzadeh 等 - 2025 - Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Bas.pdf`

## 摘要

Modern power systems are experiencing high penetration of voltage-source converter (VSC)- interfaced distributed energy resources and loads. Design, analysis, and reliable operation of such systems require extensive ofﬂine and real-time electromagnetic transient (EMT) simulations. This paper proposes discretized impedance-based modeling (DIBM) of VSCs for efﬁcient time-domain transient analysis in state-variable (SV)-based EMT simulators. Speciﬁcally, the VSC-based systems are ﬁrst represented as admittance-based models in Laplace domain, and then they are discretized and formulated to construct a Thévenin equivalent impedance matrix and history voltages that can be interfaced seamlessly with external systems in SV-based simulators. By replacing VSC subsystems with Thévenin equivalent circ

## 核心贡献


- 提出离散阻抗建模方法，将VSC导纳模型转化为离散戴维南等效电路以适配状态变量仿真器
- 消除接口步长延迟与虚拟缓冲电路，大幅降低系统状态变量数量并提升数值稳定性
- 实现VSC子系统与外部网络无缝接口，支持更大仿真步长且保持高瞬态分析精度


## 使用的方法


- [[离散阻抗建模|离散阻抗建模]]
- [[导纳建模|导纳建模]]
- [[戴维南等效电路|戴维南等效电路]]
- [[状态变量法|状态变量法]]
- [[数值离散化|数值离散化]]
- [[平均值模型|平均值模型]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[分布式能源|分布式能源]]
- [[并网滤波器|并网滤波器]]
- [[控制系统|控制系统]]
- [[七节点测试系统|七节点测试系统]]


## 相关主题


- [[实时电磁暂态仿真|实时电磁暂态仿真]]
- [[状态变量仿真|状态变量仿真]]
- [[换流器接口建模|换流器接口建模]]
- [[计算效率优化|计算效率优化]]
- [[数值稳定性|数值稳定性]]
- [[电力系统暂态分析|电力系统暂态分析]]


## 主要发现


- 经离线与实时平台验证，该方法在保持高波形精度的同时支持更大仿真步长
- 相比传统平均值模型，单步计算效率提升最高达四倍，显著降低实时仿真计算负担
- 成功消除接口延迟与虚拟缓冲电路，有效改善系统数值刚度并提升暂态仿真稳定性


