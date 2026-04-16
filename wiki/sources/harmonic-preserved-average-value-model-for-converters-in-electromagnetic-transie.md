---
title: "Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Delivery;2026;41;1;10.1109/TPWRD.2025.3645046"
tags: ['average-value', 'harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Cao 等 - 2026 - Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation.pdf"]
---

# Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation

**作者**: 
**年份**: 2026
**来源**: `19、20、21/EMT_task_21/Cao 等 - 2026 - Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transient Simulation.pdf`

## 摘要

—The increasing utilization of power electronic devices has heightened the impact of harmonics in modern power systems. However, compared with detailed models, conventional average- value models (AVMs) result in reduced accuracy due to the neglect of switching harmonics, making it challenging to meet the accuracy requirements when focusing on transient responses or harmonic dynamics. To address this limitation, this paper proposes a system- level converter model called the harmonic-preserved AVM (HP- AVM). This time-domain-based model integrates AVM computa- tion with harmonic component calculation into a uniﬁed simulation framework, enabling precision comparable to that of switching- function models (SFMs) for system-level simulation, while avoiding the high computational burden of detail

## 核心贡献


- 提出“平均值+谐波”统一时域框架，兼顾系统级仿真精度与计算效率
- 构建时域谐波模型与半载波周期占空比预测策略，突破频域阶数限制
- 提出谐波解耦策略，实现灵活稳定的解耦仿真并降低状态矩阵更新频率


## 使用的方法


- [[平均值模型|平均值模型]]
- [[开关函数模型|开关函数模型]]
- [[时域谐波计算|时域谐波计算]]
- [[谐波解耦策略|谐波解耦策略]]
- [[半载波周期占空比预测|半载波周期占空比预测]]
- [[状态空间法|状态空间法]]


## 涉及的模型


- [[变流器|变流器]]
- [[整流器|整流器]]
- [[逆变器|逆变器]]
- [[斩波器|斩波器]]
- [[n相桥式变流器|N相桥式变流器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变流器建模|变流器建模]]
- [[谐波分析|谐波分析]]
- [[系统级仿真|系统级仿真]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 仿真与实验验证表明，该模型精度媲美开关函数模型，且计算负担显著降低
- 模型在整流器、逆变器及斩波器等多种拓扑中均保持高精度与强适用性
- 半载波周期更新策略有效平衡计算开销与精度，提升大规模系统仿真效率


