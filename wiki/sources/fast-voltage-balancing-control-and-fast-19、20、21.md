---
title: "Fast Voltage-Balancing Control and Fast"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/tpwrd.2014.2351397.pdf.pdf"]
---

# Fast Voltage-Balancing Control and Fast

**作者**: 
**年份**: 2014
**来源**: `19、20、21/EMT_task_19/tpwrd.2014.2351397.pdf.pdf`

## 摘要

—A methodology of fast voltage-balancing control based on average comparison and a fast numerical simulation model for the modular multilevel converter are proposed. In each control cycle, the average voltage of all the submodules (SMs) in an arm is calculated. The switching state of each SM will be determined by comparing the capacitor voltage of each SM with this average value. Little sorting of the capacitor voltages is required; therefore, the calculation burden on the controller is signiﬁcantly reduced. The previous switching state of each SM will be mostly retained. Two variables and are introduced to adjust the equivalent switching frequency of each SM. Simulation results veriﬁed the effectiveness of the proposed voltage-balancing control in normal and fault conditions. A fast numer

## 核心贡献


- 提出基于平均比较的快速电压均衡控制，大幅降低控制器排序计算负担
- 构建保留子模块动态特性的MMC快速数值仿真模型，支持PSCAD平台
- 开发混合仿真架构，兼顾关键子模块详细开关动态与系统级仿真速度


## 使用的方法


- [[平均比较法|平均比较法]]
- [[梯形积分法|梯形积分法]]
- [[最近电平控制|最近电平控制]]
- [[混合仿真建模|混合仿真建模]]
- [[开关线性化建模|开关线性化建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[详细开关模型|详细开关模型]]
- [[快速数值模型|快速数值模型]]
- [[混合仿真模型|混合仿真模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高压直流输电|高压直流输电]]
- [[电压均衡控制|电压均衡控制]]
- [[快速仿真|快速仿真]]
- [[pscad建模|PSCAD建模]]


## 主要发现


- 模型在正常与故障工况下均能精确复现详细开关模型的电磁暂态特性
- 仿真速度较详细开关模型提升约五千倍，极大缩短电磁暂态计算时间
- 平均比较策略有效维持电容电压均衡，显著降低控制器的实时计算负担


