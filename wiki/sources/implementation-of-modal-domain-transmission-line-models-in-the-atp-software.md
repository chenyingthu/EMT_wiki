---
title: "Implementation of Modal Domain Transmission Line Models in the ATP Software"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Access;2022;10; ;10.1109/ACCESS.2022.3146880"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/23/Colqui 等 - 2022 - Implementation of Modal Domain Transmission Line Models in the ATP Software.pdf"]
---

# Implementation of Modal Domain Transmission Line Models in the ATP Software

**作者**: 
**年份**: 2022
**来源**: `23/Colqui 等 - 2022 - Implementation of Modal Domain Transmission Line Models in the ATP Software.pdf`

## 摘要

Electromagnetic Transients Program make extensive use of transmission line models for the simulation of electromagnetic transients. This paper proposes a circuit representation of the modal transformation, more speciﬁcally Clarke’s matrix. The arrangement of ideal transformers we propose allows modal transformation to be directly implemented in software such as Alternative Transient Program - Electromagnetic Transients Program. We combined the proposed circuit with single-phase transmission line models that consider frequency independent and frequency dependent parameters to represent transposed three-phase transmission lines. The main advantage of the proposed approach is that it allows the implementation of new transmission line models without depending on models provided in applications

## 核心贡献


- 提出基于理想变压器阵列的Clarke模态变换电路，实现三相线路精确解耦
- 结合单相线路模型构建多导体线路，支持在ATP中灵活开发新型频变模型
- 实现土壤参数频变特性直接嵌入仿真，突破商用软件内置模型参数限制


## 使用的方法


- [[clarke模态变换|Clarke模态变换]]
- [[理想变压器等效电路|理想变压器等效电路]]
- [[transmission-line-model|Bergeron线路模型]]
- [[jmarti模型|JMarti模型]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[频域扫描|频域扫描]]


## 涉及的模型


- [[换位三相输电线路|换位三相输电线路]]
- [[单相输电线路模型|单相输电线路模型]]
- [[transmission-line-model|Bergeron线路模型]]
- [[jmarti模型|JMarti模型]]
- [[折叠线等效模型|折叠线等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变参数建模|频变参数建模]]
- [[模态域解耦|模态域解耦]]
- [[atp-emtp模型实现|ATP-EMTP模型实现]]
- [[土壤频变特性|土壤频变特性]]


## 主要发现


- 频域扫描与时域仿真结果均验证了所提模态变换电路的高精度特性
- 结合Bergeron与JMarti模型的仿真结果与ATP内置模型高度一致
- 成功实现土壤参数频变特性嵌入，验证了模型自定义参数的灵活性与准确性


