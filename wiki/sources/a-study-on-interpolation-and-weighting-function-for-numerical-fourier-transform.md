---
title: "A study on interpolation and weighting function for numerical Fourier transform"
type: source
authors: ['Xi Shi']
year: 2021
journal: "Electric Power Systems Research, 195 (2021) 107121. doi:10.1016/j.epsr.2021.107121"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/j.epsr.2021.107121.pdf.pdf"]
---

# A study on interpolation and weighting function for numerical Fourier transform

**作者**: Xi Shi
**年份**: 2021
**来源**: `04/j.epsr.2021.107121.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A study on interpolation and weighting function for numerical a Department of Electrical and Computer Engineering, University of Manitoba, MB R3T 2N2, Canada In order to mitigate the Gibbs oscillation, a very simple and effective linear mid-point interpolation method is proposed. The relationship between proposed linear mid-point interpolation in time domain and window

## 核心贡献


- 提出线性中点插值法，有效抑制数值傅里叶逆变换中的吉布斯振荡
- 严格证明时域线性中点插值与频域余弦窗函数在数学变换上完全等效
- 将插值法推广至整数加权阶数，揭示n次插值等效于频域余弦窗n次幂


## 使用的方法


- [[数值傅里叶变换|数值傅里叶变换]]
- [[线性中点插值法|线性中点插值法]]
- [[窗函数加权|窗函数加权]]
- [[σ近似法|σ近似法]]
- [[卷积分析|卷积分析]]


## 涉及的模型



- [[输电线路|输电线路]]
- [[开关过电压|开关过电压]]


## 相关主题


- [[吉布斯振荡抑制|吉布斯振荡抑制]]
- [[数值傅里叶逆变换|数值傅里叶逆变换]]
- [[开关过电压仿真|开关过电压仿真]]
- [[频域信号处理|频域信号处理]]


## 主要发现


- 线性中点插值法抑制振荡效果与sinc窗相当，但无需逐频点乘，计算效率显著提升
- n阶时域插值严格等效于频域余弦窗函数的n次幂加权，可灵活调节平滑程度
- 仿真步长小于振荡周期十分之一时振荡显著，采用该插值法可兼顾精度与波形平滑


