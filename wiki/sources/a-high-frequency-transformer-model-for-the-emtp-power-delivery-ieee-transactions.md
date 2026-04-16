---
title: "A high frequency transformer model for the EMTP - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transformer', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/01/Morched 等 - 1993 - A High Frequency Transformer Model for the EMTP.pdf"]
---

# A high frequency transformer model for the EMTP - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `01/Morched 等 - 1993 - A High Frequency Transformer Model for the EMTP.pdf`

## 摘要

A model to simulate the high frequency behaviour of a power transformer is presented. This model is based on the frequency characteristics of the transformer admittance matrix between its tcnninals over a given range of frequencies. The transformer admittance characteristics can be obtained from measurements or from detailed internal models based on the physical layout of the transformer. The elements of the nodal admittance matrix are approximated with rational functions consisting of real as well as complex conjugate poles and zeroes. These approximations are nalized in the form of an RLC network in a format suitable for direct use with EMTP. The high frequency transformer model can be used as a stand-alone linear model or as an add-on module of a more comprehensive model where iron core

## 核心贡献


- 基于节点导纳矩阵有理函数逼近的变压器高频端口等效模型
- 将有理函数逼近结果综合为多端口π型RLC等效网络可直接嵌入EMTP
- 提出通过对角化与矩阵平均的稳健参数生成法保障等效网络数值稳定性


## 使用的方法


- [[有理函数逼近|有理函数逼近]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[多端口π型等效电路|多端口π型等效电路]]
- [[rlc网络综合|RLC网络综合]]
- [[模态分解|模态分解]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[多相多绕组变压器|多相多绕组变压器]]
- [[铁芯非线性模型|铁芯非线性模型]]
- [[内部绕组分布参数模型|内部绕组分布参数模型]]


## 相关主题


- [[高频建模|高频建模]]
- [[频率相关特性|频率相关特性]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器端口等效|变压器端口等效]]
- [[杂散电容与损耗建模|杂散电容与损耗建模]]


## 主要发现


- 模型能准确复现变压器从低频到高频的端口暂态响应有效捕捉串并联谐振特性
- 间接拟合非对角导纳元素结合矩阵平均法有效抑制测量噪声导致的数值不稳定
- RLCπ型等效结构成功表征集肤效应铁芯涡流损耗及绕组杂散电容的高频影响


