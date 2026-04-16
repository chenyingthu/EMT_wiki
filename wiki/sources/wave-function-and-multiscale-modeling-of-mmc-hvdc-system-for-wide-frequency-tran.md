---
title: "Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics;2021;9;5;10.1109/JESTPE.2021.3051647"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/40/Ye 等 - 2021 - Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation.pdf"]
---

# Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation

**作者**: 
**年份**: 2021
**来源**: `40/Ye 等 - 2021 - Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation.pdf`

## 摘要

—The detailed modeling of power electronic (PE) devices poses challenging problems to an efﬁcient transient simulation of large-scale PE-dominated power systems. As PE paradigm, a multiscale modeling methodology of the modular multilevel converter (MMC) for simulating diverse transients from low-frequency oscillations up to high-frequency switching events in an MMC high-voltage direct current (HVdc) system is developed, implemented, and validated. The novelty lies in the creation of a wave propagation function (WPF) that describes the MMC submodule (SM) transient behavior, and then, the SM Fourier series-based shifted-frequency phasor (SFP) is developed to accelerate the computation speed of the system-level dynamics. These efforts serve as the basis for multiscale modeling of the MMC wher

## 核心贡献



- 提出基于波传播函数(WPF)的MMC子模块瞬态行为描述方法
- 开发基于傅里叶级数的移频相量(SFP)以加速系统级动态计算
- 构建适用于宽频带瞬态仿真的MMC多尺度建模框架并实现与控制系统的无缝接口

## 使用的方法


- [[dynamic-phasor]]
- [[numerical-integration]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-hvdc]]
- [[mmc]]

## 相关主题


- [[harmonic]]
- [[wind-farm]]

## 主要发现



- 所提多尺度模型在直流故障、内部故障及功率振荡等工况下，与全EMT模型相比具有极高的计算精度
- 基于移频相量与波传播函数的方法显著提升了宽频带瞬态仿真的计算效率，且能无缝对接控制系统