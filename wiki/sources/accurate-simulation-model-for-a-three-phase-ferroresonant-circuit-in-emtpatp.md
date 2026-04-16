---
title: "Accurate simulation model for a three-phase ferroresonant circuit in EMTP–ATP"
type: source
authors: ['Mi Zou']
year: 2018
journal: "Electrical Power and Energy Systems, 107 (2018) 68-77. doi:10.1016/j.ijepes.2018.11.016"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/05/j.ijepes.2018.11.016.pdf.pdf"]
---

# Accurate simulation model for a three-phase ferroresonant circuit in EMTP–ATP

**作者**: Mi Zou
**年份**: 2018
**来源**: `05/j.ijepes.2018.11.016.pdf.pdf`

## 摘要

Accurate simulation model for a three-phase ferroresonant circuit in College of Automation, Chongqing University of Posts and Telecommunications, Chongqing 400065, China Key Laboratory of Industrial Internet of Things and Networked Control, Ministry of Education, Chongqing University of Posts and Telecommunications, Chongqing 400065, This study presents a simulation model for a ferroresonant circuit. The proposed model includes a transformer model and a vacuum circuit breaker (VCB) model. Hyster

## 核心贡献


- 提出基于JA磁滞模型与磁电对偶变换的三相五柱变压器模型，精确刻画铁芯非线性
- 建立含截流、耐压与高频熄弧特性的真空断路器模型，提升开关暂态仿真精度
- 在EMTP-ATP中集成组件构建铁磁谐振仿真平台，实现多稳态振荡预测


## 使用的方法


- [[jiles-atherton磁滞模型|Jiles-Atherton磁滞模型]]
- [[磁电对偶变换|磁电对偶变换]]
- [[model语言与tacs开关|MODEL语言与TACS开关]]
- [[分岔分析|分岔分析]]
- [[相平面法|相平面法]]
- [[庞加莱映射|庞加莱映射]]


## 涉及的模型


- [[三相五柱变压器|三相五柱变压器]]
- [[真空断路器-vcb|真空断路器(VCB)]]
- [[ja磁滞电抗器|JA磁滞电抗器]]
- [[铁磁谐振电路|铁磁谐振电路]]
- [[绕组杂散电容模型|绕组杂散电容模型]]


## 相关主题


- [[铁磁谐振|铁磁谐振]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器非线性建模|变压器非线性建模]]
- [[开关暂态|开关暂态]]
- [[emtp-atp|EMTP-ATP]]


## 主要发现


- 基波与次谐波铁磁谐振实验验证表明，仿真与实测波形相似度均大于0.9
- 分岔图、相平面与庞加莱分析证实模型能准确复现铁磁谐振的多稳态特性
- 考虑截流与高频熄弧的断路器模型显著提升了开关暂态过电压的预测精度


