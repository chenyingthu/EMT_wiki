---
title: "An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmission lines"
type: source
authors: ['H.M.J.', 'De', 'Silva']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109649. doi:10.1016/j.epsr.2023.109649"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/De Silva and Liu - 2023 - An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmission lines.pdf"]
---

# An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmission lines

**作者**: H.M.J., De, Silva
**年份**: 2023
**来源**: `07&08/De Silva and Liu - 2023 - An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmission lines.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. An Enhanced Method to Achieve Exact DC Values for Frequency-dependent This paper proposes an improved method to enhance the dc response of a frequency-dependent transmission line model used in EMT studies. A modification to the rational function approximation of propagation and charac­ teristic admittance matrices of a transmission line is introduced to enforce exact dc values at 0 Hz. Furthermore,

## 核心贡献


- 修改传播与导纳矩阵有理函数形式，强制0Hz精确直流值，无需额外优化算法
- 引入低频加权因子提升拟合精度，有效抑制时域直流响应过冲与数值振荡
- 重构低频传播函数并实施阶数缩减，显著降低有理函数阶数与整体计算负担


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[递归卷积|递归卷积]]
- [[最小二乘法|最小二乘法]]
- [[直流校正|直流校正]]
- [[加权拟合|加权拟合]]
- [[阶数缩减|阶数缩减]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[频率相关输电线路模型|频率相关输电线路模型]]
- [[地下电缆|地下电缆]]
- [[架空线路|架空线路]]
- [[高压直流输电线路|高压直流输电线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[曲线拟合|曲线拟合]]
- [[高压直流输电|高压直流输电]]
- [[时域仿真稳定性|时域仿真稳定性]]
- [[直流响应校正|直流响应校正]]


## 主要发现


- 新方法在时域仿真中实现精确直流响应，高频段无偏差且避免优化不收敛问题
- 低频加权拟合消除近似误差，彻底抑制直流响应中的人工过冲与数值振荡现象
- 阶数缩减策略降低计算量且保持精度，开短路测试验证了HVDC线路仿真准确性


