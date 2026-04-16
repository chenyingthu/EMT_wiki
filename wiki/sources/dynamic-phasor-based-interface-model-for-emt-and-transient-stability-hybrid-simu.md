---
title: "Dynamic Phasor Based Interface Model for EMT and Transient Stability Hybrid Simulations"
type: source
authors: ['未知']
year: 2017
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRS.2017.2766269.pdf.pdf"]
---

# Dynamic Phasor Based Interface Model for EMT and Transient Stability Hybrid Simulations

**作者**: 
**年份**: 2017
**来源**: `13&14/files/TPWRS.2017.2766269.pdf.pdf`

## 摘要

—Electromagnetic transient (EMT) and transient sta- bility hybrid simulations are predominantly used to analyze the interactions between HVDC systems and the AC grids. However, the dynamics of the converters will be greatly affected by the waveforms of adjacent AC systems. Waveform distortion as well as time delay caused by interfacing can signiﬁcantly increase interface errors, resulting in the decrease of the overall accuracy of the simulations. To solve such problems, a dynamic phasor based interface model (DPIM) is proposed in this paper to im- prove the accuracy of interfaces, especially when the fault occurs near the converters. In doing so, the whole system is partitioned into three parts: the transient stability (TS) subsystem, the EMT subsystem, and the DPIM. During each iteration

## 核心贡献


- 提出基于动态相量的接口模型，有效抑制混合仿真接口波形畸变与采样延迟误差。
- 采用动态相量形式的诺顿与戴维南等效，实现暂态稳定与电磁暂态子系统双向交互。
- 克服传统曲线拟合与FFT计算量大缺陷，显著提升接口精度与整体仿真效率。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[诺顿等效|诺顿等效]]
- [[戴维南等效|戴维南等效]]
- [[系统分区法|系统分区法]]
- [[时变傅里叶级数|时变傅里叶级数]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[输电线路|输电线路]]
- [[换流器|换流器]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[接口模型|接口模型]]
- [[交直流系统交互|交直流系统交互]]
- [[换流器近区故障|换流器近区故障]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 实际HVDC工程仿真验证表明，该模型显著降低了接口波形畸变与时间延迟误差。
- 换流器近区故障工况下，模型相比传统方法大幅提升了混合仿真精度与计算效率。
- 动态相量等效接口有效消除采样延迟影响，保证了交直流系统交互仿真的数值稳定。


