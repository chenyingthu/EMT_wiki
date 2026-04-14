---
title: "电压源换流器 (VSC)"
type: model
tags: [vsc, hvdc, two-level, three-level, pwm]
created: "2026-04-13"
---

# 电压源换流器 (VSC)

## 概述

电压源换流器（Voltage Source Converter, VSC）是柔性直流输电和新能源并网的核心设备。相比传统的线路换相换流器（LCC），VSC具有可控性强、谐波小、可向无源网络供电等优势。

## 主要拓扑

### 1. 两电平VSC
- 最基本的VSC拓扑
- 6个IGBT/IGCT开关
- PWM调制
- 适用于中小容量应用

### 2. 三电平VSC（NPC）
- 中点箝位拓扑
- 减少开关应力
- 改善谐波特性
- 适用于风电并网

### 3. 多电平VSC
- 级联H桥
- 飞跨电容
- 接近正弦波输出

## EMT建模方法

### 详细开关模型
- 每个开关器件单独建模
- 精确表征开关动态
- 计算量大

### 平均值模型
- 开关周期平均化
- 保留基频动态
- 系统级仿真适用

### 固定导纳模型
- ADC建模
- 实时仿真适用

### 动态相量模型
- 频域VSC建模
- 混合仿真适用

## 控制系统

- 内外环控制器
- 锁相环（PLL）
- 直流电压控制
- 无功功率控制
- 故障穿越控制

## 相关方法
- [[average-value-model]]
- [[fixed-admittance]]
- [[dynamic-phasor]]

## 相关主题
- [[vsc-hvdc]]
- [[mmc-model]]
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s|Modeling Synchronous Voltage Source Converters in Transmissi]] | 2004 |
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[modulation-index-dependent-thevenin-equivalent-circuit-model-of-vsc-and-apdr|Modulation Index Dependent Thévenin Equivalent Circuit Model]] | 2015 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr|A Novel Ultra-High-Speed Traveling-Wave Protection Principle]] | 2019 |
| [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea|Modeling a voltage source converter assisted resonant curren]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-|A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro]] | 2020 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using|Fast Simulation Model of Voltage Source Converters With Arbi]] | 2022 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVD]] | 2022 |
| [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour|Fast Electromagnetic Transient Modeling Method for Half-brid]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat|Transient Electromagnetic Power Compensation‐Based Adaptive ]] | 2025 |