---
title: "Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain"
type: source
authors: ['未知']
year: 2024
journal: "2024 IEEE Power & Energy Society General Meeting (PESGM);2024; ; ;10.1109/PESGM51994.2024.10688669"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain.pdf"]
---

# Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain

**作者**: 
**年份**: 2024
**来源**: `27&28/Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain.pdf`

## 摘要

—In this paper, a novel synchronous machine model is developed for the accurate and efﬁcient simulation of multi- scale transients. The machine stator equations are expressed with analytic signals in the phase domain, thus providing direct interface between machine model and external network model. Frequency shifting is applied to stator quantities to eliminate the ac carrier in the stator windings which enables the use of large time-step size. An artiﬁcial damper winding is introduced to eliminate the numerical saliency based on a pioneering tech- nique. The proposed machine model is represented as a Norton equivalent with constant conductance matrix. The analysis of test cases demonstrates the effectiveness of the proposed synchronous machine model in terms of accuracy and efﬁciency. Ind

## 核心贡献


- 提出基于频移概念的相域同步电机多尺度模型支持宽时间尺度暂态仿真
- 引入人工阻尼绕组消除数值凸极效应构建恒定导纳矩阵的诺顿等效模型
- 重构电机方程简化数学运算避免网络导纳矩阵每步更新显著提升计算效率


## 使用的方法


- [[频移技术|频移技术]]
- [[解析信号法|解析信号法]]
- [[隐式梯形积分法|隐式梯形积分法]]
- [[相域建模|相域建模]]
- [[诺顿等效|诺顿等效]]
- [[人工阻尼绕组技术|人工阻尼绕组技术]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[外部电网|外部电网]]


## 相关主题


- [[多尺度暂态仿真|多尺度暂态仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步长仿真|大时间步长仿真]]
- [[数值凸极效应消除|数值凸极效应消除]]
- [[电机网络直接接口|电机网络直接接口]]


## 主要发现


- 频移技术有效消除定子交流载波允许采用大时间步长且保持高精度
- 恒定导纳矩阵避免每步更新结合人工阻尼绕组参数新规则提升数值稳定性
- 算例验证表明该模型在宽时间尺度暂态仿真中兼具高计算精度与显著效率优势


