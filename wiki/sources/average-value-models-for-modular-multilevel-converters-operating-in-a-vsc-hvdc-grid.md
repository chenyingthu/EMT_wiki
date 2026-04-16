---
title: "Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid"
type: source
authors: ['未知']
year: 2014
journal: "IEEE Transactions on Power Delivery"
tags: ['mmc', 'vsc', 'average-value', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/TPWRD.2014.2332557.pdf-1.pdf"]
---

# Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid

**作者**: 未知
**年份**: 2014
**来源**: `37/TPWRD.2014.2332557.pdf-1.pdf`

## 摘要

This paper investigates the applicability of averaged-value models (AVMs) for modular multilevel converters (MMCs) operating in a voltage-sourced converter-based-high-voltage dc (VSC-HVDC) grid.

## 核心贡献


- 提出改进的MMC平均值模型拓扑，显著提升直流故障暂态仿真精度。
- 明确AVM适用边界，指出子模块电容电压恒定假设是模型有效的关键条件。
- 建立AVM与详细模型对比基准，为大规模直流电网系统级分析提供高效指南。


## 使用的方法


- [[average-value-model|平均值模型]]
- [[详细电磁暂态建模|详细电磁暂态建模]]
- [[最近电平控制-nlc|最近电平控制(NLC)]]
- [[载波移相spwm|载波移相SPWM]]
- [[功率平衡法|功率平衡法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[子模块-sm|子模块(SM)]]
- [[受控源等效电路|受控源等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[直流故障分析|直流故障分析]]
- [[模型降阶与等效|模型降阶与等效]]
- [[仿真加速|仿真加速]]
- [[vsc-model|VSC]]


## 主要发现


- 传统AVM仅在电容电压近似恒定时有效，直流故障下仿真精度显著下降。
- 改进拓扑后的AVM能准确复现直流故障暂态过程，且计算耗时大幅降低。
- AVM与详细模型在稳态及小扰动下波形高度一致，验证了系统级分析可行性。


