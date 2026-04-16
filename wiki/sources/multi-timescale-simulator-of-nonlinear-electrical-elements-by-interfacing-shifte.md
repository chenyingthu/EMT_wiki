---
title: "Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors and electromagnetic transient simulation"
type: source
authors: ['Zhen Gong']
year: 2022
journal: "Electric Power Systems Research, 208 (2022) 107856. doi:10.1016/j.epsr.2022.107856"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors.pdf"]
---

# Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors and electromagnetic transient simulation

**作者**: Zhen Gong
**年份**: 2022
**来源**: `27&28/Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Multi-timescale simulator of nonlinear electrical elements by interfacing shifted equivalent phasors and electromagnetic transient simulation School of Electrical Engineering and Automation, Wuhan University, Wuhan 430072, China This paper proposes a multi-timescale transient branch companion model for electrical elements with strong nonlinearity, which is suitable for electromagnetic

## 核心贡献


- 提出基于移位等效相量的多时间尺度支路伴随模型，适用于强非线性元件宽频带仿真
- 结合动态相量与包络跟踪技术，实现单次仿真中瞬时波形与包络波形的高效同步追踪
- 建立饱和SEP变压器模型，克服传统分段线性化在大步长下的数值过冲问题


## 使用的方法


- [[移位等效相量法-sep|移位等效相量法(SEP)]]
- [[动态相量法-dp|动态相量法(DP)]]
- [[牛顿-拉夫逊迭代|牛顿-拉夫逊迭代]]
- [[梯形积分法|梯形积分法]]
- [[伴随模型法|伴随模型法]]
- [[混合仿真接口|混合仿真接口]]


## 涉及的模型


- [[饱和变压器|饱和变压器]]
- [[vsc-model|VSC]]
- [[非线性电感|非线性电感]]
- [[磁链控制非线性支路|磁链控制非线性支路]]


## 相关主题


- [[多时间尺度仿真|多时间尺度仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[非线性元件建模|非线性元件建模]]
- [[包络跟踪|包络跟踪]]
- [[谐波分析|谐波分析]]
- [[大步长仿真|大步长仿真]]


## 主要发现


- SEP模型在大步长下有效抑制了传统分段线性化产生的励磁电流数值过冲现象
- 通过合理设置移频参数与步长，单次仿真即可同时精确追踪瞬时值与包络波形
- MATLAB与PSCAD验证表明，该模型在保持精度的同时显著提升非线性元件仿真效率


