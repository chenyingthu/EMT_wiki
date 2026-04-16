---
title: "Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;5;10.1109/TPWRD.2023.3269143"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics.pdf"]
---

# Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics

**作者**: 
**年份**: 2023
**来源**: `27&28/Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics.pdf`

## 摘要

—The prediction of voltage stresses in transformer and machine windings requires the ability to calculate pulse propaga- tion effects on the feeding cable with sufﬁcient accuracy. The use of commonly available cable models in electromagnetic transient (EMT) programs can lead to voltage wave fronts with too weak damping at very high frequencies. This work shows a method for improving the accuracy of such models by usage of measured coaxial mode propagation characteristics. The information is in- troduced into a wide-band multi-conductor cable model at high frequencies by a merging procedure, with only a minor impact on the non-coaxial modes of propagation. The application of the developed model is demonstrated for cases where the metallic sheaths are grounded at one end only, or are cross-b

## 核心贡献


- 提出将实测同轴波特性融入多导体电缆模型的融合方法，提升高频阻尼精度
- 设计高频滤波合并策略，修正同轴模态同时保持非共轴模态与低频特性不变
- 构建兼容单端接地与交叉互联工况的通用频变行波模型，可直接用于EMT程序


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[模态分解|模态分解]]
- [[频变行波建模|频变行波建模]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[参数融合技术|参数融合技术]]


## 涉及的模型


- [[多导体电缆|多导体电缆]]
- [[同轴波传播模型|同轴波传播模型]]
- [[频变行波模型|频变行波模型]]
- [[交叉互联电缆|交叉互联电缆]]
- [[变压器-电机绕组|变压器/电机绕组]]


## 相关主题


- [[高频暂态建模|高频暂态建模]]
- [[脉冲传播分析|脉冲传播分析]]
- [[电缆频变建模|电缆频变建模]]
- [[极快速暂态仿真|极快速暂态仿真]]
- [[护套接地方式影响|护套接地方式影响]]


## 主要发现


- 融合模型显著增强高频电压波前阻尼，有效解决传统模型高频衰减过弱的问题
- 滤波合并策略使低频与非共轴模态响应与经典理论计算结果保持高度一致
- EMTP仿真证实该模型在多种护套接地方式下均能精确预测极快速暂态过程


