---
title: "VSC-HVDC"
type: topic
tags: [vsc-hvdc, hvdc, flexible-dc-transmission, voltage-source-converter]
created: "2026-04-14"
---

# VSC-HVDC（柔性直流输电）

## 概述

VSC-HVDC（Voltage Source Converter High Voltage Direct Current）是基于电压源换流器的高压直流输电技术。相比传统的LCC-HVDC，VSC-HVDC具有可向无源网络供电、可控性强、谐波小等优势，是新能源并网和柔性直流输电的核心技术。

## 主要特点

- 可独立控制有功和无功功率
- 可向无源网络（孤岛）供电
- 不需要无功补偿设备
- 占地面积小，适合城市供电
- 多端直流系统灵活组网

## 主要拓扑

### 1. 两电平VSC
- 最简单的VSC拓扑
- 适用于中低压应用

### 2. 三电平NPC-VSC
- 中点箝位拓扑
- 改善谐波特性
- 适用于风电并网

### 3. MMC-VSC
- 模块化多电平换流器
- 目前VSC-HVDC主流拓扑
- 低开关频率、高质量输出波形

## EMT仿真挑战

- 大量电力电子开关器件
- 多时间尺度动态过程
- 控制系统与一次系统耦合
- 平均值模型和详细模型的选择
- 实时仿真对硬件要求高

## 相关模型
- [[vsc-model]]
- [[mmc-model]]
- [[lcc-model]]

## 相关方法
- [[average-value-model]]
- [[fixed-admittance]]
- [[state-space-method]]

## 相关主题
- [[real-time-simulation]]
- [[co-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVD]] | 2022 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
