---
title: "Multi-scale Induction Machine Model in the Phase Domain with Constant Inner Impedance"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Systems; ;PP;99;10.1109/TPWRS.2019.2947535"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-Scale Induction Machine Model in the Phase Domain with Constant Inner Impedance.pdf"]
---

# Multi-scale Induction Machine Model in the Phase Domain with Constant Inner Impedance

**作者**: 
**年份**: 2019
**来源**: `27&28/Multi-Scale Induction Machine Model in the Phase Domain with Constant Inner Impedance.pdf`

## 摘要

—An efﬁcient and accurate multi-scale induction ma- chine model for simulating diverse transients in power systems is developed and validated. Voltages, currents, and ﬂux linkages are described through analytic signals that consist of real in-phase and imaginary quadrature components, covering only positive frequencies of the Fourier spectrum. The stator is modeled in the abc phase coordinates of an arbitrary reference frame whose rotating speed is adjusted by a simulation parameter called shift frequency. When the reference frame is stationary at a zero shift frequency, then the model processes instantaneous signals to yield natural waveforms. When the reference frame is set to rotate at the synchronous frequency of the electric network, then the Fourier spectra of the analytic signals ar

## 核心贡献


- 提出基于解析信号与可变偏移频率的感应电机多尺度相域模型，统一电磁与机电暂态仿真
- 推导恒定内导纳诺顿等效电路，消除转子位置与饱和影响，实现与相域网络直接接口
- 支持仿真中动态调整偏移频率，兼顾自然波形追踪与动态相量包络跟踪的计算效率


## 使用的方法


- [[解析信号法|解析信号法]]
- [[动态相量法|动态相量法]]
- [[相域建模|相域建模]]
- [[诺顿等效|诺顿等效]]
- [[希尔伯特变换|希尔伯特变换]]
- [[多尺度仿真|多尺度仿真]]


## 涉及的模型


- [[感应电机|感应电机]]
- [[电力系统网络|电力系统网络]]
- [[定转子绕组|定转子绕组]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[机电暂态|机电暂态]]
- [[多尺度仿真|多尺度仿真]]
- [[动态相量建模|动态相量建模]]
- [[频率自适应仿真|频率自适应仿真]]


## 主要发现


- 零偏移频率下精确追踪自然波形，同步频率下高效跟踪动态相量包络，验证多尺度适应性
- 恒定内导纳特性避免网络矩阵随转子位置更新，显著提升多机系统暂态仿真计算效率
- 跨时间尺度暂态测试表明，该模型在保持高精度的同时，大幅降低计算步长限制与耗时


