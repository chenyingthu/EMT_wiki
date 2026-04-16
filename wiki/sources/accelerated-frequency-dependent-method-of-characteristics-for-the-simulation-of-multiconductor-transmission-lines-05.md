---
title: "Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain"
type: source
authors: ['Pablo Torrez Caballero', 'Sergio Kurokawa', 'Behzad Kordi']
year: 2018
journal: "Electric Power Systems Research"
tags: ['transmission-line', 'frequency-dependent']
created: "2026-04-13"
sources: ["EMT_Doc/05/j.epsr.2018.11.006.pdf.pdf"]
---

# Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain

**作者**: Pablo Torrez Caballero, Sergio Kurokawa, Behzad Kordi
**年份**: 2018
**来源**: `05/j.epsr.2018.11.006.pdf.pdf`

## 摘要

Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain. São Paulo State University – UNESP, Ilha Solteira, Brazil; University of Manitoba, Winnipeg, Manitoba, Canada.

## 核心贡献


- 利用电路拓扑结构缩减状态方程数量，结合稀疏矩阵技术加速常微分方程组求解
- 提出状态变量后处理技术降低内存占用，并修正行波传播时间离散化带来的误差
- 采用固定频率下模变换矩阵实部解耦多导体线路方程，兼顾计算效率与仿真精度


## 使用的方法


- [[特征线法|特征线法]]
- [[矢量拟合|矢量拟合]]
- [[模态分析|模态分析]]
- [[状态空间法|状态空间法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]
- [[时间离散化误差修正|时间离散化误差修正]]


## 涉及的模型


- [[多导体输电线路|多导体输电线路]]
- [[架空输电线路|架空输电线路]]
- [[频率相关等效电路|频率相关等效电路]]
- [[模态阻抗模型|模态阻抗模型]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[时域仿真|时域仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[计算加速|计算加速]]
- [[内存优化|内存优化]]


## 主要发现


- 所提方法在保持架空线路仿真精度的同时，显著降低了整体计算时间与内存消耗
- 固定频率模变换矩阵实部解耦策略在架空线路时域仿真中实现了高精度与高效率
- 状态变量后处理与稀疏求解技术有效减少了单步迭代的内存访问次数与计算量


