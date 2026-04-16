---
title: "Modeling and simulation of VSC-HVDC with dynamic phasors"
type: source
authors: ['未知']
year: 2023
journal: ""
tags: ['vsc', 'dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/26/Yao 等 - 2008 - Modeling and simulation of VSC-HVDC with dynamic phasors.pdf"]
---

# Modeling and simulation of VSC-HVDC with dynamic phasors

**作者**: 
**年份**: 2023
**来源**: `26/Yao 等 - 2008 - Modeling and simulation of VSC-HVDC with dynamic phasors.pdf`

## 摘要

：To meet the needs of rapid accurate simulation and analysis of the power systema newly developed meth- od-dynamic phasors method is applied to a model voltage sources converter based HVDC（VSC-HVDC）transmission system．T his method is based on the time-varying Fourier coefficients series of the system variablesand focuses on the dynamics behavior of the Fourier coefficients．By truncating unimportant higher order series and keep only those significant seriesthis method can catch the dynamic behavior of the original detail model．T he complexity of dy- namic phasors model can be adjusted according to different application requirements．T hereforeit can significantly improve computational efficiency and maintain a good engineering precision when it is used for transient simulation． Followed 

## 核心贡献


- 首次将动态相量法应用于VSC-HVDC建模，完整推导系统动态相量方程
- 基于开关函数保留直流与基频分量，有效简化高频开关过程并降低模型阶数
- 构建复杂度可调的VSC-HVDC动态相量模型，兼顾暂态仿真精度与计算效率


## 使用的方法


- [[动态相量法|动态相量法]]
- [[时变傅里叶级数|时变傅里叶级数]]
- [[开关函数法|开关函数法]]
- [[平均值近似|平均值近似]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[电压源型换流器|电压源型换流器]]
- [[直流输电线路|直流输电线路]]
- [[直流电容|直流电容]]
- [[换流电抗|换流电抗]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态相量建模|动态相量建模]]
- [[暂态过程分析|暂态过程分析]]
- [[模型降阶|模型降阶]]
- [[高频开关简化|高频开关简化]]


## 主要发现


- 动态相量模型能精确复现VSC-HVDC系统的暂态变化过程与稳态运行特性
- 相比详细电磁暂态模型，该方法大幅缩短仿真耗时且维持良好的工程计算精度
- 仅保留直流与基频分量即可准确捕捉系统主导动态，验证了模型降阶的有效性


