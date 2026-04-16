---
title: "Analytical model building for Type-3 wind farm subsynchronous oscillation analysis"
type: source
authors: ['Lingling Fan']
year: 2021
journal: "Electric Power Systems Research, 201 (2021) 107566. doi:10.1016/j.epsr.2021.107566"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Fan和Miao - 2021 - Analytical model building for Type-3 wind farm subsynchronous oscillation analysis.pdf"]
---

# Analytical model building for Type-3 wind farm subsynchronous oscillation analysis

**作者**: Lingling Fan
**年份**: 2021
**来源**: `09/Fan和Miao - 2021 - Analytical model building for Type-3 wind farm subsynchronous oscillation analysis.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Analytical model building for Type-3 wind farm subsynchronous Dept. of Electrical Engineering, University of South Florida, Tampa FL 33620 Many real-world scenarios confirmed insights developed based on the dq-frame nonlinear analytical model for doubly-fed induction generator (DFIG)-based type-3 wind subsynchronous resonance (SSR) study by the authors

## 核心贡献


- 提出包含锁相环动态的DFIG风电场dq坐标系非线性解析模型
- 构建模块化建模框架明确子系统接口与互联支持多种电网拓扑
- 模型兼具大信号时域仿真与小信号分析能力可复现低补偿度SSR


## 使用的方法


- [[dq坐标系解析建模|dq坐标系解析建模]]
- [[模块化建模|模块化建模]]
- [[状态空间法|状态空间法]]
- [[数值摄动线性化|数值摄动线性化]]
- [[小信号特征值分析|小信号特征值分析]]
- [[大信号时域仿真|大信号时域仿真]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[锁相环-pll|锁相环(PLL)]]
- [[转子侧变流器-rsc|转子侧变流器(RSC)]]
- [[网侧变流器-gsc|网侧变流器(GSC)]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[双质量轴系模型|双质量轴系模型]]


## 相关主题


- [[次同步谐振-ssr|次同步谐振(SSR)]]
- [[风电场建模|风电场建模]]
- [[动态建模|动态建模]]
- [[弱电网稳定性|弱电网稳定性]]
- [[变流器控制|变流器控制]]
- [[小信号稳定性分析|小信号稳定性分析]]


## 主要发现


- 引入PLL动态后成功复现低串补度下风电场次同步振荡现象
- PLL动态显著改变系统稳定裕度与振荡频率是SSR关键诱因
- 模块化模型可准确评估不同并网风机数量对系统SSR脆弱性影响


