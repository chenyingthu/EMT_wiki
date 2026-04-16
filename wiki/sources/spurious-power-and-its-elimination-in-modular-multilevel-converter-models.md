---
title: "Spurious power and its elimination in modular multilevel converter models"
type: source
authors: ['Anton Stepanov']
year: 2020
journal: "Electric Power Systems Research, 190 (2021) 106704. doi:10.1016/j.epsr.2020.106704"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/35/j.epsr.2020.106704.pdf.pdf"]
---

# Spurious power and its elimination in modular multilevel converter models

**作者**: Anton Stepanov
**年份**: 2020
**来源**: `35/j.epsr.2020.106704.pdf.pdf`

## 摘要

Spurious power and its elimination in modular multilevel converter models Anton Stepanova,⁎, Hani Saadb, Ulas Karaagacc, Jean Mahseredjiana c Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong This paper demonstrates the presence of spurious power generation or losses in two commonly used Modular Multilevel Converter (MMC) models: the Arm Equivalent Model (AEM) and the Average Value Model (AVM).

## 核心贡献



- 揭示了MMC的AEM和AVM模型中因控制框实现导致的一步延迟会产生非物理虚假功率
- 提出了消除AEM和AVM模型中虚假功率的改进方案，并在MMC-HVDC系统中验证了其有效性

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]
- [[state-space]]

## 涉及的模型


- [[mmc-model]]
- [[average-value-model]]
- [[vsc-model]]

## 相关主题


- [[mmc]]
- [[vsc-hvdc]]
- [[hvdc]]

## 主要发现



- 当模型方程未与主网络方程联立求解（如使用控制框实现）时，数值效应会导致AEM和AVM模型产生虚假功率
- 虚假功率可能显著影响甚至超过换流站实际损耗，导致仿真结果失真；联立求解或特定修正可有效消除该现象