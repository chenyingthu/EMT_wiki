---
title: "Analyses of the modifications in the pi circuits for inclusion of frequency influence in transmission line representation"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Analyses of the modifications in the 蟺 circuits for inclusion of frequency influence in transmission line representation.pdf"]
---

# Analyses of the modifications in the pi circuits for inclusion of frequency influence in transmission line representation

**作者**: 
**年份**: 2011
**来源**: `07&08/Analyses of the modifications in the 蟺 circuits for inclusion of frequency influence in transmission line representation.pdf`

## 摘要

—In this article, it is represented by state variables phase a transmission line which parameters are considered frequency independently and frequency dependent. It is analyzed what is the reasonable number of π circuits and the number of blocks composed by parallel resistor and inductor in parallel for reduction of numerical oscillations. It is simulated the numerical routine with and without the effect of frequency in the longitudinal parameters. Initially, it is used state variables and π circuits representing the transmission line composing a linear system which is solved by numerical routines based on the trapezoidal rule. The effect of frequency on the line is synthesized by resistors and inductors in parallel and this representation is analyzed in details. It is described transmissi

## 核心贡献


- 提出在π型电路中并联RL支路以等效表征输电线路纵向参数的频率依赖性
- 构建基于状态变量与梯形积分法的数值求解算法实现频变线路电磁暂态仿真
- 系统分析并确定级联π电路与并联RL模块的最优数量以有效抑制数值振荡


## 使用的方法


- [[状态变量法|状态变量法]]
- [[梯形积分法|梯形积分法]]
- [[特征线法|特征线法]]
- [[π型电路级联|π型电路级联]]
- [[并联rl支路拟合|并联RL支路拟合]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变π型电路|频变π型电路]]
- [[并联rl等效模块|并联RL等效模块]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值振荡抑制|数值振荡抑制]]
- [[线路参数等值|线路参数等值]]
- [[emtp算法|EMTP算法]]


## 主要发现


- 合理配置π电路级联数与并联RL模块数可显著抑制梯形积分法引发的数值振荡
- 改进π电路模型在宽频范围内能高精度逼近真实频变输电线路的电磁暂态响应
- 状态变量结合梯形法则的算法在Matlab中验证可行满足暂态仿真精度要求


