---
title: "Development of a Voltage-Dependent Line Model to Represent the Corona Effect in Electromagnetic Transient Program"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2990968"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2020.2990968.pdf.pdf"]
---

# Development of a Voltage-Dependent Line Model to Represent the Corona Effect in Electromagnetic Transient Program

**作者**: 
**年份**: 2020
**来源**: `13&14/files/TPWRD.2020.2990968.pdf.pdf`

## 摘要

This paper describes a new method to represent single-phase overhead transmission lines (TL) under corona effect in electromagnetic transient simulation program. Based on Bergeron model and the scheme proposed by Dommel to represent transmission lines in Electromagnetic Transients Programs (EMT), a voltage-dependent line model (VDLM) was developed. This model can be represented through of an equivalent impedance network and easily combined with other components of the electric power system. To solve the nodal equations of the network a simple technique is proposed, which is suitable to calculate lightning overvoltages transients and avoids the necessity of iterative methods, increasing the efficiency of the algorithm. The proposed method was implemented in Matlab software, and the simulati

## 核心贡献


- 提出基于Bergeron模型的电压相关线路模型，将电晕直接嵌入分布参数
- 将单位长度并联电容设为电压函数，实现电晕非线性与分布特性的直接表征
- 提出无迭代节点电压求解技术，避免传统迭代计算，显著提升雷击过电压仿真效率


## 使用的方法


- [[transmission-line-model|Bergeron线路模型]]
- [[空间离散化|空间离散化]]
- [[等效阻抗网络|等效阻抗网络]]
- [[节点分析法|节点分析法]]
- [[非迭代求解技术|非迭代求解技术]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[电压相关线路模型-vdlm|电压相关线路模型(VDLM)]]
- [[电晕模型|电晕模型]]
- [[传统线性电晕模型|传统线性电晕模型]]


## 相关主题


- [[电晕效应|电晕效应]]
- [[雷击过电压|雷击过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[绝缘配合|绝缘配合]]


## 主要发现


- 模型仿真结果与现场实测数据高度吻合，验证了VDLM在雷击过电压计算中的准确性
- 与传统线性电晕模型对比结果一致，证明该模型能有效捕捉电晕衰减与波速降低特性
- 非迭代求解算法大幅降低计算耗时，满足电磁暂态程序对雷击暂态快速仿真的需求


