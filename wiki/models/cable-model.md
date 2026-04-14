---
title: "电缆模型 (Cable)"
type: model
tags: [cable, underground, submarine, frequency-dependent, multi-core]
created: "2026-04-13"
---

# 电缆模型 (Cable)

## 概述

电力电缆（地下电缆、海底电缆）的EMT建模需要考虑集肤效应、邻近效应、绝缘层、护套接地等复杂因素。相比架空线路，电缆的电磁耦合更强，频率相关特性更显著。

## 主要特性

### 频率相关阻抗
- 导体集肤效应
- 邻近效应（多芯电缆）
- 护套涡流效应
- 螺线管效应（三芯铠装电缆）

### 导纳参数
- 绝缘层电容
- 护套接地
- 半导体层影响

### 暂态特性
- 行波传播
- 反射与折射
- 截断电荷
-  trapped charge放电

## 建模方法

### 相域模型
- 直接多导体建模
- 考虑相间耦合

### 模域模型
- 模态变换解耦
- 频率相关变换矩阵

### 频变模型
- 矢量拟合阻抗
- 无源性强制
- 递归卷积计算

## 特殊问题

- 海底电缆长距离暂态
- 多芯电缆螺线管效应
- 土壤电离化（接地故障）
- 混合架空线-电缆线路

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[transmission-line-model]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu|An Efficient and Accurate Calculation of Electric Field and ]] | 2016 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[effects-of-cable-insulations-physical-and-geometrical-parameters-on-sheath-trans|Effects of cable insulations’ physical and geometrical param]] | 2019 |
| [[analytical-study-of-the-frequencydependent-earth-conduction-effects-on-undergrou|Analytical study of the frequency‐dependent earth conduction]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable|Modal propagation characteristics and transient analysis of ]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[algorithm-for-fast-calculating-the-energization-overvoltages-along-a-power-cable|Algorithm for fast calculating the energization overvoltages]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[morales-等-a-new-tool-for-calculation-of-line-and-cable-parameters|Morales 等 | A new tool for calculation of line and cable par]] | 2023 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-Conductor Cable Modeling With Inclusion of Measured Co]] | 2023 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va|Frequency and transient responses of A 275 kV pressure oil-f]] | 2025 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |