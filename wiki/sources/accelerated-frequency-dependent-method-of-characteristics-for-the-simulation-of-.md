---
title: "Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain"
type: source
authors: ['Pablo', 'Torrez', 'Caballero']
year: 2019
journal: "Electric Power Systems Research, 168 (2019) 55-66. doi:10.1016/j.epsr.2018.11.006"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/05/1-s2.0-S0378779618303675-main.pdf"]
---

# Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain

**作者**: Pablo, Torrez, Caballero
**年份**: 2019
**来源**: `05/1-s2.0-S0378779618303675-main.pdf`

## 摘要

Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain☆ Pablo Torrez Caballeroa, Sergio Kurokawaa, Behzad Kordib,⁎ a São Paulo State University – UNESP, Ilha Solteira, Brazil b University of Manitoba, Winnipeg, Manitoba, Canada R3T 5V6

## 核心贡献


- 利用电路拓扑特性减少状态方程数量，结合稀疏矩阵技术加速常微分方程求解
- 提出状态变量后处理技术，显著降低迭代过程中的内存占用与访问次数
- 采用固定频率模变换矩阵实部解耦多导体线路，并校正行波时间离散化误差


## 使用的方法


- [[特征线法|特征线法]]
- [[矢量拟合|矢量拟合]]
- [[模态分析|模态分析]]
- [[状态空间法|状态空间法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]


## 涉及的模型


- [[多导体输电线路|多导体输电线路]]
- [[架空输电线路|架空输电线路]]
- [[频变等效电路模型|频变等效电路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[频率相关建模|频率相关建模]]
- [[加速仿真|加速仿真]]


## 主要发现


- 该方法在架空线路仿真中保持高精度，同时显著降低整体计算时间与内存消耗
- 状态变量后处理与稀疏矩阵技术有效减少了内存访问次数，大幅提升了求解速度
- 固定频率模变换实部解耦法在工程精度范围内可行，有效避免了频变矩阵求逆难题


