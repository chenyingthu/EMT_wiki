---
title: "Validation of Frequency-Dependent"
type: source
authors: ['未知']
year: 2005
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/tpwrd.2004.837676.pdf.pdf"]
---

# Validation of Frequency-Dependent

**作者**: 
**年份**: 2005
**来源**: `40/tpwrd.2004.837676.pdf.pdf`

## 摘要

—The accuracy of a transmission line model can be veriﬁed by comparing its response to that by an alternative method of indisputable accuracy. This paper shows a procedure for validation which is based on the inverse Fourier transform. Desired test responses are calculated in the frequency domain using an admittance representation of the line and its terminal conditions. Time-domain step responses are calculated using the inverse Fourier transform, with semianalytic integration between sample points to permit calculation at arbitrarily large time values. The required number of frequency samples is greatly reduced by adaptively calculating the samples while considering the frequency-domain behavior of the integrand. Responses from arbitrary excitations are calculated by superposition of wei

## 核心贡献



- 提出了一种基于逆傅里叶变换的频变输电线路模型验证流程
- 引入自适应非等距频率采样策略，结合被积函数频域特性大幅减少所需采样点数量
- 采用采样点间的半解析积分技术，支持在任意大时间值下精确计算时域阶跃响应
- 通过加权与时延阶跃响应的叠加，实现任意激励下系统响应的快速求解

## 使用的方法


- [[frequency-dependent]]
- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[transmission-line]]
- [[cable]]

## 相关主题


- [[frequency-dependent]]
- [[transmission-line]]
- [[cable]]

## 主要发现



- 自适应非等距采样策略能显著降低逆傅里叶变换的计算负担，同时保持频域响应分辨率
- 半解析积分方法有效克服了传统离散傅里叶变换在长时域仿真中的精度衰减与吉布斯现象
- 该验证流程在架空线路与地下电缆系统中的测试结果与高精度相域模型（ULM）高度吻合，证明了其可靠性与工程实用性