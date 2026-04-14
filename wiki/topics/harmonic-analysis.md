---
title: "谐波分析 (Harmonic Analysis)"
type: topic
tags: [harmonic, harmonic-analysis, frequency-domain, power-quality, resonance]
created: "2026-04-14"
---

# 谐波分析 (Harmonic Analysis)

## 概述

谐波分析是电力系统EMT仿真中的重要应用方向。随着电力电子设备的广泛应用，电力系统中的谐波问题日益突出。谐波分析包括谐波潮流计算、谐振频率分析、谐波阻抗扫描等。

## 谐波来源

- 换流器（LCC、VSC、MMC）
- 非线性负载
- 变压器饱和
- 电力电子变流器的开关频率谐波
- 新能源并网逆变器

## 分析方法

### 1. 频域分析
- 谐波潮流计算
- 阻抗-频率扫描
- 谐振频率识别
- 频率耦合分析

### 2. 时域仿真
- EMT仿真中的谐波提取
- FFT分析
- 动态相量法
- 宽频暂态分析

### 3. 混合方法
- 频域-时域联合仿真
- 谐波相量域与EMT域耦合
- 适用于多频率系统

## 在EMT仿真中的挑战

- 需要宽频模型（频率相关参数）
- 大量谐波频率点
- 长时间仿真收敛性
- 谐波谐振风险评估
- 无源性要求（稳定性）

## 相关方法
- [[vector-fitting]]
- [[dynamic-phasor]]
- [[nodal-analysis]]

## 相关模型
- [[vsc-model]]
- [[mmc-model]]
- [[transmission-line-model]]
- [[transformer-model]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[co-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The FDLOAD model for accurate frequency dynamics in the SFA-]] | 2024 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[基于c型滤波器的mmc高频振荡抑制及参数设计方法|基于C型滤波器的MMC高频振荡抑制及参数设计方法]] | 2026 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
