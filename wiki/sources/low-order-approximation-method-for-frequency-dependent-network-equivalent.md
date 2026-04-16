---
title: "Low-order approximation method for frequency-dependent network equivalent"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Liu 等 - 2017 - Low-order approximation method for frequency-dependenttransmission line model.pdf"]
---

# Low-order approximation method for frequency-dependent network equivalent

**作者**: 
**年份**: 2026
**来源**: `25/Liu 等 - 2017 - Low-order approximation method for frequency-dependenttransmission line model.pdf`

## 摘要

Rational function approximations of characteristic impedance and propagation coefficient are crucial in modeling of frequency-dependent transmission line. Traditional Bode asymptotic method produces lots of pole-zeros. Some of them have no contribution to fitting accuracy and cause unnecessary calculation in electromagnetic transient simulation. To avoid appearance of redundant pole-zeros, a low-order approximation method of

## 核心贡献


- 提出频变线路低阶有理函数拟合方法，消除传统Bode法产生的冗余零极点
- 基于单调区间划分与分段误差区间实现零极点初始低阶定位
- 引入非线性最小二乘法优化零极点位置，实现降阶与高精度拟合的统一


## 使用的方法


- [[有理函数拟合|有理函数拟合]]
- [[bode渐近线法|Bode渐近线法]]
- [[非线性最小二乘法|非线性最小二乘法]]
- [[递归卷积|递归卷积]]
- [[相模变换|相模变换]]


## 涉及的模型


- [[频变输电线路模型|频变输电线路模型]]
- [[j-r-marti模型|J.R. Marti模型]]
- [[分布参数线路模型|分布参数线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[网络等值|网络等值]]


## 主要发现


- 相比传统Bode法，新方法在显著降低有理函数阶数的同时提升了拟合精度
- 消除冗余零极点有效减少递归卷积计算量，大幅加速电磁暂态仿真过程
- 分段误差与最小二乘优化结合，克服了零极点密集导致的实际拟合偏差


