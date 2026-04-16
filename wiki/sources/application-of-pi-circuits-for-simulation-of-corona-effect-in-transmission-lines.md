---
title: "Application of pi circuits for simulation of corona effect in transmission lines"
type: source
authors: ['未知']
year: 2011
journal: "2012 IEEE Power and Energy Society General Meeting;2012; ; ;10.1109/PESGM.2012.6345558"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/09/Lessa 等 - 2012 - Application of π circuits for simulation of corona effect in transmission lines.pdf"]
---

# Application of pi circuits for simulation of corona effect in transmission lines

**作者**: 
**年份**: 2011
**来源**: `09/Lessa 等 - 2012 - Application of π circuits for simulation of corona effect in transmission lines.pdf`

## 摘要

—In this article, it is represented by state variables phase a transmission line which parameters are considered frequency independently and frequency dependent. Based on previous analyses, it is used the reasonable number of π circuits and the number of blocks composed by parallel resistor and inductor for reduction of numerical oscillations. It is analyzed the influence of the increase of the RL parallel blocks in the obtained results. The RL parallel blocks are used for inclusion of the frequency influence in the transmission line longitudinal parameter. It is a simple model that is been used by undergraduate students for simulation of traveling wave phenomena in transmission lines. Considering the model without frequency influence, it is included a representation of the corona effect. 

## 核心贡献


- 提出基于级联π型电路与并联RL支路的输电线路状态变量模型，有效抑制数值振荡
- 在频域无关模型中引入电晕效应局部表征方法，简化了暂态仿真建模流程
- 结合梯形积分法构建简化算法，突破传统EMTP程序对π电路数量的限制


## 使用的方法


- [[状态变量法|状态变量法]]
- [[梯形积分法|梯形积分法]]
- [[π型电路级联|π型电路级联]]
- [[并联rl支路频率拟合|并联RL支路频率拟合]]
- [[矩阵数值求解|矩阵数值求解]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[π型等效电路|π型等效电路]]
- [[电晕效应模型|电晕效应模型]]
- [[频变参数模型|频变参数模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[行波分析|行波分析]]
- [[频率相关建模|频率相关建模]]
- [[数值振荡抑制|数值振荡抑制]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 增加并联RL支路数量可显著降低仿真中的数值振荡，提升频变参数拟合精度
- 引入局部电晕效应模型后，线路暂态电压波形呈现明显衰减与非线性畸变特征
- 基于MATLAB的简化π电路算法在保持精度的同时，有效突破了传统EMTP的规模限制


