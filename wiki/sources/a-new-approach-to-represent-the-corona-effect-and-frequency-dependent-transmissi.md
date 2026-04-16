---
title: "A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EMT-Type Programs"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;6;10.1109/TPWRD.2022.3157163"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/02/Pereira和Tavares - 2022 - A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EM.pdf"]
---

# A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EMT-Type Programs

**作者**: 
**年份**: 2022
**来源**: `02/Pereira和Tavares - 2022 - A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EM.pdf`

## 摘要

—This paper presents an accurate and efﬁcient model to represent the corona effect and frequency dependence of line parameters in electromagnetic transient simulations. The new method, named the voltage and frequency dependent line model (VFDLM), can be seen as a more general case of the well-known frequency-dependent (FD) or wideband (WB) line models, wherein the characteristic admittance and propagation function are con- sidered voltage- and frequency-dependent parameters. The time domain traveling wave equations are solved using recursive con- volutions and rational approximation through vector ﬁtting (VF). Since the model can be represented by Norton equivalents, it is to- tally compatible with EMT-type programs. The model is validated through comparisons with three ﬁeld measurement da

## 核心贡献


- 提出电压频率相关线路模型，将电晕效应与频变特性直接耦合于分布式参数中
- 将特征导纳与传播函数扩展为电压频率双重依赖参数，突破传统线性模型限制
- 基于诺顿等效与递归卷积构建算法，实现与现有EMT仿真程序的无缝兼容


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[递归卷积|递归卷积]]
- [[有理函数逼近|有理函数逼近]]
- [[诺顿等效|诺顿等效]]
- [[行波方程求解|行波方程求解]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变线路模型|频变线路模型]]
- [[宽带线路模型|宽带线路模型]]
- [[电晕模型|电晕模型]]


## 相关主题


- [[电晕效应|电晕效应]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[雷电过电压|雷电过电压]]


## 主要发现


- 与三组现场实测数据对比验证，模型在暂态过电压波形拟合上高度吻合
- 仿真验证表明该模型兼具数值稳定性、计算高效性与参数表征准确性
- 成功在EMT平台实现电晕非线性与线路频变特性的全分布式统一建模


