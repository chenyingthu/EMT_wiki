---
title: "Flexible extended harmonic domain approach for transient state analysis of switched systems"
type: source
authors: ['Uriel Vargas']
year: 2017
journal: "Electric Power Systems Research, 155 (2018) 40-47. doi:10.1016/j.epsr.2017.09.030"
tags: ['harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/j.epsr.2017.09.030.pdf.pdf"]
---

# Flexible extended harmonic domain approach for transient state analysis of switched systems

**作者**: Uriel Vargas
**年份**: 2017
**来源**: `19、20、21/EMT_task_19/j.epsr.2017.09.030.pdf.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出灵活扩展谐波域（FEHD）方法，允许为系统中每个状态变量独立配置任意数量（非连续）的谐波成分
- 有效解决传统EHD模型在分析高频电力电子开关系统时面临的维度爆炸问题，实现模型降阶
- 在保留高频纹波特性的前提下显著提升计算效率，精度优于传统EHD模型与平均值模型

## 使用的方法

- [[灵活扩展谐波域-fehd-建模技术|灵活扩展谐波域（FEHD）建模技术]]
- [[基于状态变量谐波特征差异的非连续谐波选择策略|基于状态变量谐波特征差异的非连续谐波选择策略]]
- [[降阶状态空间模型构建|降阶状态空间模型构建]]
- [[与pscad-emtdc时域仿真工具的对比验证|与PSCAD/EMTDC时域仿真工具的对比验证]]

## 涉及的模型

- [[三相光伏并网系统-闭环运行|三相光伏并网系统（闭环运行）]]
- [[含电力电子开关的电力系统|含电力电子开关的电力系统]]
- [[传统扩展谐波域-ehd-模型|传统扩展谐波域（EHD）模型]]
- [[平均值模型-averaged-value-models|平均值模型（Averaged-value models）]]
- [[pscad-emtdc电磁暂态仿真模型|PSCAD/EMTDC电磁暂态仿真模型]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态（EMT）仿真]]
- [[扩展谐波域分析|扩展谐波域分析]]
- [[开关系统暂态分析|开关系统暂态分析]]
- [[电能质量与谐波动态|电能质量与谐波动态]]
- [[模型降阶与计算优化|模型降阶与计算优化]]
- [[新能源并网系统建模|新能源并网系统建模]]

## 主要发现

- FEHD方法能够以非连续谐波配置精准捕捉各状态变量的高频动态与纹波信息
- 相比传统EHD和平均值模型，FEHD在保证仿真精度的同时大幅降低计算维度与时间成本
- 根据网络拓扑和开关/滤波器配置差异化分配谐波成分，是实现高效暂态分析的关键
