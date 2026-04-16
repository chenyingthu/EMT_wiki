---
title: "Duality-Based Transformer Model Including"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2015.2424223.pdf.pdf"]
---

# Duality-Based Transformer Model Including

**作者**: 
**年份**: 2015
**来源**: `13&14/files/TPWRD.2015.2424223.pdf.pdf`

## 摘要

—This paper presents a general method for building equivalent electric circuits of power transformers, including eddy current effects in windings and core. A high-frequency equiva- lent dual model for single- and three-phase transformers with two multilayer windings is derived from the application of the principle of duality. The model is built from elements available in circuit simulation programs, such as Electromagnetic Transients Program (EMTP)–Alternative Transients Program, EMTP-RV, PSCAD, and PSpice. The parameters of the frequency-dependent leakage inductance and winding resistance are computed with analytical formulae obtained from the solution of Maxwell’s equations that are based on the geometrical dimensions and material information. Ideal transformers are utilized to isolate t

## 核心贡献


- 提出基于对偶原理的双侧Cauer等效电路，实现绕组涡流效应的高频精确建模
- 推导基于麦克斯韦方程的解析公式，直接由几何尺寸计算频变漏感与电阻参数
- 利用理想变压器隔离电磁元件并明确物理连接点，模型可直接部署于EMTP等软件


## 使用的方法


- [[对偶原理|对偶原理]]
- [[cauer等效电路|Cauer等效电路]]
- [[解析参数计算|解析参数计算]]
- [[有限元验证|有限元验证]]
- [[理想变压器隔离法|理想变压器隔离法]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[单相变压器|单相变压器]]
- [[三相变压器|三相变压器]]
- [[多层绕组|多层绕组]]
- [[频变漏感模型|频变漏感模型]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[频率相关建模|频率相关建模]]
- [[涡流效应|涡流效应]]
- [[变压器高频建模|变压器高频建模]]
- [[电路等效|电路等效]]


## 主要发现


- 双侧Cauer模型与单侧模型在宽频范围内电阻与电感特性完全等效，且便于接入电容
- 解析公式计算的频变参数与有限元仿真及实验室实测数据高度吻合，验证了模型精度
- 模型通过理想变压器实现电磁解耦，可直接在EMTP/PSCAD中搭建并高效运行


