---
title: "Study of a numerical integration method using the compact scheme for electromagnetic transient simulations"
type: source
authors: ['Yohei Tanaka']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109666. doi:10.1016/j.epsr.2023.109666"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/36/Tanaka和Baba - 2023 - Study of a numerical integration method using the compact scheme for electromagnetic transient simul.pdf"]
---

# Study of a numerical integration method using the compact scheme for electromagnetic transient simulations

**作者**: Yohei Tanaka
**年份**: 2023
**来源**: `36/Tanaka和Baba - 2023 - Study of a numerical integration method using the compact scheme for electromagnetic transient simul.pdf`

## 摘要

0378-7796/© 2023 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Study of a numerical integration method using the compact scheme for a Grid and Communication Technology Division, Grid Innovation Research Laboratory, Central Research Institute of Electric Power Industry, Kanagawa 240-0196, Japan b Graduate School of Science and Engineering, Doshisha University, Kyotanabe, Kyoto 610-0394, Japan This pape

## 核心贡献



- 提出基于紧致格式的单阶段无振荡数值积分方法
- 该方法在电路突变为刚性系统时具备L稳定性，可自动抑制虚假数值振荡与非线性元件引起的虚假尖峰

## 使用的方法


- [[numerical-integration]]
- [[interpolation]]

## 涉及的模型


- [[电磁暂态-emt-仿真模型|电磁暂态(EMT)仿真模型]]
- [[电力系统网络模型|电力系统网络模型]]

## 相关主题


- [[numerical-integration]]

## 主要发现



- 紧致格式在系统刚度突变时自动呈现L稳定性，无需依赖事件检测即可有效抑制数值振荡
- 作为单阶段方法，该格式避免了多阶段隐式方法在处理非线性元件时产生的虚假电压/电流尖峰
- 与梯形法、2S-DIRK及TR-BDF2相比，该方法在保持二阶精度的同时彻底消除了虚假振荡与尖峰