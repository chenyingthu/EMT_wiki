---
title: "27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmission Lines"
type: source
authors: ['未知']
year: 2017
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmission Lines.pdf"]
---

# 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmission Lines

**作者**: 
**年份**: 2017
**来源**: `27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmission Lines.pdf`

## 摘要

—A frequency-dependent transmission line model for multi-scale simulation of diverse transients over a wide range of frequencies is developed, implemented, and validated. It makes use of the concept of frequency-adaptive simulation of transients in which the Fourier spectra are adaptively shifted in the frequency domain to reduce the discretization time-steps in the time domain. The transients are modeled through dynamic phasors comprising the real and imaginary parts of analytic signals to facilitate the frequency-shifting. In the proposed line model, all mathematical operations such as numerical recursive convolutions are therefore expressed in terms of analytic signals. A modal decomposition is performed to attain decoupled modes for the multi-phase case. The transition from the represe

## 核心贡献




- 提出基于可平移解析信号的递归卷积算法，实现频变线路高效时域计算
- 构建多尺度频变多相线路模型，通过自动插入π型支路实现暂态无缝切换
- 完成模型算法实现，并通过涵盖线路投切与恢复电压的现场试验验证精度


## 使用的方法




- [[动态相量法|动态相量法]]
- [[解析信号|解析信号]]
- [[频移技术|频移技术]]
- [[模态分解|模态分解]]
- [[部分分式展开|部分分式展开]]
- [[数值递归卷积|数值递归卷积]]
- [[多尺度仿真|多尺度仿真]]


## 涉及的模型




- [[输电线路|输电线路]]
- [[频变线路模型|频变线路模型]]
- [[π型等值电路|π型等值电路]]
- [[多相线路|多相线路]]


## 相关主题




- [[多尺度建模|多尺度建模]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态|电磁暂态]]
- [[机电暂态|机电暂态]]
- [[实时仿真|实时仿真]]


## 主要发现




- 模型在单次仿真中实现了电磁与机电暂态的高精度与高效率统一计算
- 现场试验验证表明，模型在线路投切、暂态恢复电压及稳态工况下精度优异
- 自动插入π型支路策略有效实现了跨时间尺度暂态过程的平滑无缝过渡


