---
title: "Passivity Enforcement for Transmission Line Models"
type: source
authors: ['未知']
year: 2008
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2008.919034.pdf.pdf"]
---

# Passivity Enforcement for Transmission Line Models

**作者**: 
**年份**: 2008
**来源**: `31/TPWRD.2008.919034.pdf.pdf`

## 摘要

—The Universal Line Model (ULM) has been imple- mented in several EMT programs for simulation of electromag- netic transients. In some cases, instability problems have been encountered. This paper shows that the current approach for ra- tional function approximation adopted in ULM can lead to large out-of-band passivity violations, thereby causing an unstable sim- ulation. An approach is introduced which prevents the occurrence of large passivity violations. Low-frequency violations are avoided by adding an artiﬁcial shunt conductance to the diagonal elements of the shunt admittance matrix while high-frequency violations are avoided by introducing artiﬁcial attenuation using a low-pass ﬁlter. In addition, high-frequency asymptotic passivity is enforced for the characteristic admittance. An

## 核心贡献


- 提出在并联导纳矩阵对角线添加人工电导，消除低频无源性违规
- 引入低通滤波器与高频渐近无源性约束，抑制高频无源性违规
- 通过端口二阶校正项消除剩余违规，保障EMT仿真稳定性


## 使用的方法


- [[特征线法|特征线法]]
- [[矢量拟合|矢量拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[迹拟合|迹拟合]]
- [[低通滤波|低通滤波]]
- [[无源性强制|无源性强制]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[输电线路|输电线路]]
- [[电缆系统|电缆系统]]
- [[频变线路模型|频变线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[无源性强制|无源性强制]]
- [[频变建模|频变建模]]
- [[仿真稳定性|仿真稳定性]]
- [[有理逼近|有理逼近]]


## 主要发现


- 传统ULM有理逼近易引发带外无源性违规，导致仿真发散
- 所提方法有效消除电缆系统仿真中的数值不稳定现象
- 校正后模型在宽频带内保持高精度，未牺牲原有仿真质量


