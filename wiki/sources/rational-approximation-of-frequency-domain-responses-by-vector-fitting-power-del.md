---
title: "Rational approximation of frequency domain responses by vector fitting - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/VF_paper.pdf"]
---

# Rational approximation of frequency domain responses by vector fitting - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `32/VF_paper.pdf`

## 摘要

The paper describes a general methodology for the fitting of measured or calculated frequency domain responses with rational function approximations. This is achieved by replacing a set of Starting poles with an improved set of poles via a scaling procedure. A previous paper [5] has described the application of the method to smooth functions using real starting poles. This paper extends the method to functions with a high number of resonance peaks by allowing complex starting poles. Fundamental properties of the method are discussed and details of its practical imptementation are described. The method is demonstrated to be very suitable for fitting network equivalents and transformer responses. The computer code is in the public domain, available from the first author. 1 INTRODUCTION One o

## 核心贡献


- 提出采用复数起始极点的矢量拟合法，可精确拟合含多谐振峰频域响应
- 提出两阶段极点迁移与留数辨识算法，将非线性有理逼近转化为线性最小二乘求解
- 给出系统化的起始极点选取策略与迭代收敛机制，实现宽频带鲁棒拟合


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[极点迁移法|极点迁移法]]
- [[最小二乘法|最小二乘法]]
- [[部分分式展开|部分分式展开]]


## 涉及的模型


- [[变压器|变压器]]
- [[网络等值模型|网络等值模型]]
- [[输电线路|输电线路]]
- [[频变参数模型|频变参数模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[变压器建模|变压器建模]]
- [[频域响应拟合|频域响应拟合]]
- [[时域仿真|时域仿真]]


## 主要发现


- 复数起始极点有效克服病态问题，实现含高谐振峰响应的精确拟合
- 两阶段矢量拟合算法收敛迅速，生成的稳定有理模型适用于时域卷积计算
- 经人工数据、实测变压器及网络等值验证，方法具备高精度与强鲁棒性


