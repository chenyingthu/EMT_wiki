---
title: "Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery;2020;35;2;10.1109/TPWRD.2019.2934099"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/38/Gunawardana和Kordi - 2020 - Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory.pdf"]
---

# Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory

**作者**: 
**年份**: 2020
**来源**: `38/Gunawardana和Kordi - 2020 - Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory.pdf`

## 摘要

—Classical multiconductor transmission line (MTL) theory, which is employed in electromagnetic transient (EMT) simulators, is built on the assumptions that the wire structure is inﬁnitely long and has a uniform cross-section. Therefore, non- uniformities which occur in physical power systems, such as trans- mission line crossings, are not represented in classical MTL models. A new transmission line model has been developed to calculate space varying per unit length (PUL) parameter matrices near a conductor crossing using electromagnetic scattering theory. The proposed scattered ﬁeld transmission line (SFTL) model has been implemented for lossless, frequency-independent conductors, that cross each other at a variable crossing angle. A single dimensional ﬁnite difference time domain (1D-FDTD

## 核心贡献



- 提出基于电磁散射理论的散射场输电线路(SFTL)模型，用于计算导体交叉点附近空间变化的单位长度(PUL)参数矩阵
- 开发一维时域有限差分(1D-FDTD)算法实现该模型的时域求解
- 通过与三维全波电磁求解器对比，验证了模型在变交叉角无损导体场景下的准确性

## 使用的方法


- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]

## 相关主题


- [[transmission-line]]

## 主要发现



- 经典多导体传输线(MTL)理论因假设导线无限长且截面均匀，无法准确表征输电线路交叉等非均匀结构
- 所提SFTL模型结合1D-FDTD算法能有效计算交叉区域的空间变化参数，时域仿真结果与三维全波求解器高度吻合
- 该模型为EMT仿真中精确建模线路交叉引起的电磁干扰和暂态过电压提供了新途径