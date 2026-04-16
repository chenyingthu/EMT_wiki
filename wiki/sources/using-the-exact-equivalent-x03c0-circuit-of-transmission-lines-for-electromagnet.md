---
title: "Using the Exact Equivalent &#x03C0;-Circuit of Transmission Lines for Electromagnetic Transient Simulations in the Time Domain"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Access;2022;10; ;10.1109/ACCESS.2022.3201503"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/39/Juan Robles Balestero 等 - 2022 - Using the Exact Equivalent π-Circuit of Transmission Lines for Electromagnetic Transient Simulations.pdf"]
---

# Using the Exact Equivalent &#x03C0;-Circuit of Transmission Lines for Electromagnetic Transient Simulations in the Time Domain

**作者**: 
**年份**: 2022
**来源**: `39/Juan Robles Balestero 等 - 2022 - Using the Exact Equivalent π-Circuit of Transmission Lines for Electromagnetic Transient Simulations.pdf`

## 摘要

This work presents a transmission line model for simulating electromagnetic transients directly in the time domain. For this purpose, the exact equivalent π-circuit is used, which represents the line taking into account its distributed and frequency-dependent parameters. The admittances that constitute the exact equivalent π-circuit are approximated by rational functions using the vector ﬁtting technique. Then, for each admittance, an electrical circuit is synthesized, consisting of an association of discrete elements (resistors, inductors, and capacitors) aiming at modeling the transmission line, thus allowing its use in any circuit simulation software and the eventual connection of nonlinear elements. From the simulation results, it is reasonable to state that the proposed model is a fea

## 核心贡献



- 提出了一种基于精确等效π型电路的输电线路时域电磁暂态仿真模型
- 利用矢量拟合技术将频变导纳近似为有理函数并综合为离散RLC电路，避免了卷积与频域变换，可直接用于通用电路仿真软件

## 使用的方法


- [[vector-fitting]]
- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]
- [[network-equivalent]]

## 相关主题


- [[frequency-dependent]]
- [[harmonic]]

## 主要发现



- 该模型在时域中完整保留了精确等效π型电路的特性，在稳态和电磁暂态过程中均具有高精度
- 模型通过离散无源元件综合实现，无需卷积或拉普拉斯/傅里叶逆变换，且支持非线性元件的直接接入