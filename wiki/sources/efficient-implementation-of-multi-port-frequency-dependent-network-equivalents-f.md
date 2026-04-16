---
title: "Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Equivalent Circuits"
type: source
authors: ['Claudio Saldaña']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108432. doi:10.1016/j.epsr.2022.108432"
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient implementation of multi-port frequency dependent network equivalents for electromagnetic t_Saldaña和Calzolari_2022.pdf"]
---

# Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Equivalent Circuits

**作者**: Claudio Saldaña
**年份**: 2022
**来源**: `15/Efficient implementation of multi-port frequency dependent network equivalents for electromagnetic t_Saldaña和Calzolari_2022.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Power system electromagnetic transient studies require that a small part of the electrical network be modelled in detail. The rest of the system is represented by a network equivalent taking into account the frequency depen­

## 核心贡献


- 提出基于诺顿等效电路的高阶有理模型实现方法，显著减少导纳支路数量
- 开发动态更新JMARTI线路模型模态变换矩阵的频率扫描方法，消除近似误差
- 将有理函数部分分式直接转化为时域微分方程并梯形积分，避免复极点特殊处理


## 使用的方法


- [[矩阵拟合-矢量拟合|矩阵拟合/矢量拟合]]
- [[诺顿等效电路|诺顿等效电路]]
- [[梯形积分法|梯形积分法]]
- [[谐波频率扫描-hfs|谐波频率扫描(HFS)]]
- [[有理函数极点-留数逼近|有理函数极点-留数逼近]]
- [[多端π型等值电路综合|多端π型等值电路综合]]


## 涉及的模型


- [[同步发电机次暂态阻抗模型|同步发电机次暂态阻抗模型]]
- [[变压器漏抗模型|变压器漏抗模型]]
- [[r-l串联负荷模型|R-L串联负荷模型]]
- [[jmarti频变输电线路模型|JMARTI频变输电线路模型]]
- [[fdne-model|FDNE]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变网络等值|频变网络等值]]
- [[频率相关建模|频率相关建模]]
- [[网络等值与降阶|网络等值与降阶]]
- [[开关暂态分析|开关暂态分析]]
- [[emtp程序二次开发|EMTP程序二次开发]]


## 主要发现


- 在500kV系统开关暂态仿真中，该等值模型能高精度复现外部网络动态响应
- 相比完整系统模型与传统电路拟合方法，该实现方案显著降低了计算处理时间
- 无需特殊处理复极点即可保证模型无源性，简化了EMTP程序实现流程


