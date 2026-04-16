---
title: "Efﬁcient Modeling of Modular Multilevel HVDC"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient modeling of modular multilevel HVDC converters (MMC) on electromagnetic transient simulati_Gnanarathna 等_2011.pdf"]
---

# Efﬁcient Modeling of Modular Multilevel HVDC

**作者**: 
**年份**: 2010
**来源**: `15/Efficient modeling of modular multilevel HVDC converters (MMC) on electromagnetic transient simulati_Gnanarathna 等_2011.pdf`

## 摘要

—The number of semiconductor switches in a modular multilevel converter (MMC) for HVDC transmission is typically two orders of magnitudes larger than that in a two or three level voltage-sourced converter (VSC). The large number of devices creates a computational challenge for electromagnetic transient simulation programs, as it can signiﬁcantly increase the simula- tion time. The paper presents a method based on partitioning the system’s admittance matrix and deriving an efﬁcient time-varying Thévenin’s equivalent for the converter part. The proposed method does not make use of approximate interfaced models, and mathematically, is exactly equivalent to modelling the entire network (converter and external system) as one large network. It is shown to drastically reduce the computational tim

## 核心贡献


- 提出基于导纳矩阵分割的MMC建模方法，推导高效时变戴维南等效电路
- 采用嵌套快速同步求解技术解耦MMC与外网，实现数学精确等效
- 避免近似接口模型，在保留全网络精度的同时大幅降低EMT仿真耗时


## 使用的方法


- [[导纳矩阵分割|导纳矩阵分割]]
- [[时变戴维南等效|时变戴维南等效]]
- [[嵌套快速同步求解|嵌套快速同步求解]]
- [[节点分析法|节点分析法]]
- [[电容电压平衡控制|电容电压平衡控制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[功率子模块|功率子模块]]
- [[igbt-二极管开关|IGBT/二极管开关]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[网络等值|网络等值]]
- [[计算效率优化|计算效率优化]]
- [[换流器建模|换流器建模]]


## 主要发现


- 所提方法在数学上与传统全网络建模完全等效，未牺牲任何仿真精度
- 仿真验证表明该方法大幅降低计算时间，有效解决频繁开关导致的矩阵求逆瓶颈
- 成功应用于点对点VSC-MMC直流系统，验证了模型在暂态过程中的有效性


