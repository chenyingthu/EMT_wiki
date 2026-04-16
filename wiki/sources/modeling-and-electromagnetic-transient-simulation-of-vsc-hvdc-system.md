---
title: "Modeling and electromagnetic transient simulation of VSC-HVDC system"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Zeng 等 - 2010 - Modeling and electromagnetic transient simulation of UHV autotransformer.pdf"]
---

# Modeling and electromagnetic transient simulation of VSC-HVDC system

**作者**: CNKI
**年份**: 2022
**来源**: `26/Zeng 等 - 2010 - Modeling and electromagnetic transient simulation of UHV autotransformer.pdf`

## 摘要

To correctly apply transformer differential protection in the environment of ultra high voltage (UHV), it is necessary to model the UHV power transformer reasonably and carry out the corresponding electro-magnetic transient simulations. According to the equivalent circuit of three winding autotransformer, we set up the three winding autotransformer model by means of unified magnetic equivalent circuit (UMEC) transformer model provided by EMTDC software. The parameters of UHV transformer are converted to those of the UMEC model. By this way, the UHV transformer model is built. Under the UHV environment, the excitation and internal fault current of UHV power transformer are simulated, and the simulated data are utilized to investigate the operation reliability of the well-applied differentia

## 核心贡献


- 基于UMEC模型构建特高压三绕组自耦变压器电磁暂态仿真模型
- 提出利用第四绕组模拟变压器内部匝间与匝地短路故障的建模方法
- 揭示特高压环境下励磁涌流与轻微故障电流的二次谐波分布特性


## 使用的方法


- [[统一电磁等效电路-umec|统一电磁等效电路(UMEC)]]
- [[参数折算|参数折算]]
- [[三端星型等值电路|三端星型等值电路]]
- [[分段线性插值法|分段线性插值法]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[特高压自耦变压器|特高压自耦变压器]]
- [[三绕组变压器|三绕组变压器]]
- [[umec变压器模型|UMEC变压器模型]]
- [[特高压输电线路|特高压输电线路]]
- [[高压并联电抗器|高压并联电抗器]]
- [[内部短路故障模型|内部短路故障模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器差动保护|变压器差动保护]]
- [[励磁涌流分析|励磁涌流分析]]
- [[内部故障建模|内部故障建模]]
- [[二次谐波制动|二次谐波制动]]
- [[特高压电网|特高压电网]]
- [[谐波分析|谐波分析]]


## 主要发现


- 特高压变压器三相励磁涌流二次谐波含量可低于10%易致差动保护误动
- 轻微内部故障初期故障电流二次谐波含量较高会导致保护装置短暂延时动作
- 传统15%至20%二次谐波制动门槛在特高压环境下无法可靠区分涌流与故障


