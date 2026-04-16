---
title: "Passivity enforcement of wideband line model through coupled perturbation of residues and poles"
type: source
authors: ['Juan Becerra']
year: 2020
journal: "Electric Power Systems Research, 190 (2021) 106798. doi:10.1016/j.epsr.2020.106798"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2020.106798.pdf.pdf"]
---

# Passivity enforcement of wideband line model through coupled perturbation of residues and poles

**作者**: Juan Becerra
**年份**: 2020
**来源**: `31/j.epsr.2020.106798.pdf.pdf`

## 摘要

Passivity enforcement of wideband line model through coupled perturbation Juan Becerra⁎, Ilhan Kocar, Keyhan Sheshyekani, Jean Mahseredjian Department of Electrical Engineering, Ecole Polytechnique de Montreal, Montreal, Canada Ensuring stability in transient simulations of power systems requires that intrinsically passive components of the network should be represented with passive models, including transmission lines and cables. Existing research

## 核心贡献


- 提出同时扰动特征导纳留数、极点与常数项的无源性强制方法
- 引入基于相对误差与状态空间Frobenius距离的偏差度量以保持精度
- 建立线性化凸优化框架实现宽频线路模型无源性校正与精度保持联合求解


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[无源性强制|无源性强制]]
- [[凸优化|凸优化]]
- [[频率扫描法|频率扫描法]]
- [[状态空间建模|状态空间建模]]
- [[frobenius范数|Frobenius范数]]


## 涉及的模型


- [[宽频线路模型-ulm|宽频线路模型(ULM)]]
- [[频变电缆模型-fdcm|频变电缆模型(FDCM)]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[特征导纳有理模型|特征导纳有理模型]]


## 相关主题


- [[无源性强制|无源性强制]]
- [[宽频建模|宽频建模]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真稳定性|电磁暂态仿真稳定性]]
- [[有理函数逼近|有理函数逼近]]


## 主要发现


- 联合扰动极点与留数可显著降低校正引起的频响偏差，精度优于传统方法
- 所提偏差度量指标能有效控制模型失真，确保电磁暂态仿真数值稳定性
- 针对近直流频段大幅违规需结合直流校正预处理，以保证线性化算法收敛


