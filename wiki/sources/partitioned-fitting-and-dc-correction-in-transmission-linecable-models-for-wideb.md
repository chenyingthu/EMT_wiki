---
title: "Partitioned fitting and DC correction in transmission line/cable models for wideband EMT studies"
type: source
authors: ['Miguel Cervantes']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106809. doi:10.1016/j.epsr.2020.106809"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2020.106809.pdf.pdf"]
---

# Partitioned fitting and DC correction in transmission line/cable models for wideband EMT studies

**作者**: Miguel Cervantes
**年份**: 2020
**来源**: `31/j.epsr.2020.106809.pdf.pdf`

## 摘要

Partitioned ﬁtting and DC correction in transmission line/cable models for Miguel Cervantesa,⁎, Ilhan Kocara, Jean Mahseredjiana, Abner Ramirezb b CINVESTAV Campus Guadalajara, Guadalajara, Mexico This paper extends the applications of and provides further insights about partitioned ﬁtting procedure. At the ﬁrst stage of this procedure, the ﬁtting is performed at a high frequency band by excluding frequency samples close to DC. The second stage ﬁnds a correction term for those excluded samples.

## 核心贡献


- 提出分频段拟合与直流校正的两阶段方法，显著提升宽频带线路模型低频精度
- 消除传播函数拟合中的大留数极点比问题，有效解决时域仿真数值不稳定难题
- 给出完整的时域状态空间实现细节，并验证了不同积分与插值方案下的稳定性


## 使用的方法


- [[分频段拟合|分频段拟合]]
- [[直流校正|直流校正]]
- [[有理函数逼近|有理函数逼近]]
- [[模态分解|模态分解]]
- [[状态空间实现|状态空间实现]]
- [[时域卷积|时域卷积]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[通用线路模型|通用线路模型]]
- [[频率相关电缆模型|频率相关电缆模型]]
- [[高压直流输电线路|高压直流输电线路]]


## 相关主题


- [[宽频电磁暂态仿真|宽频电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[数值稳定性|数值稳定性]]
- [[高压直流输电|高压直流输电]]
- [[时域实现|时域实现]]


## 主要发现


- 两阶段拟合方法在保证高频精度的同时，实现了准确的直流稳态电压电流响应
- 有效避免了大留数极点比问题，相比传统通用线路模型显著提升了时域仿真稳定性
- 在不同积分与插值方案下均保持良好稳定性，验证了该模型在宽频暂态研究中的可靠性


