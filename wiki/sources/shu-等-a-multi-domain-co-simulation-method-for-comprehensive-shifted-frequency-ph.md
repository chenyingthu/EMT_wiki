---
title: "Shu 等 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM"
type: source
authors: ['未知']
year: 2019
journal: ""
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Shu 等 - 2019 - A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM.pdf"]
---

# Shu 等 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM

**作者**: 
**年份**: 2019
**来源**: `02/Shu 等 - 2019 - A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM.pdf`

## 摘要

— To accurately capture the dynamics of a large-scale AC/DC system as a whole and the interactions between its individual components, a simulation method with high precision and efficiency is in great demand. For this purpose, we develop a multi-domain co-simulation method, in which the target system is partitioned into multiple DC and AC subsystems, represented by our proposed shifted frequency phasor (SFP) models }and the traditional EMT models, respectively. SFP models can be simulated with a much larger time step, leading to a significant improvement in simulation efficiency under a given requirement of precision. Further, a new interface model, namely, hybrid multi-domain transmission-line model (HMD-TLM), is developed to reflect the interactions between SFP models and EMT models, wit

## 核心贡献



- 提出了一种多域协同仿真方法，将交直流系统划分为采用移频相量(SFP)模型的直流子系统和采用传统EMT模型的交流子系统
- 开发了混合多域传输线模型(HMD-TLM)作为接口，有效耦合SFP与EMT模型，实现瞬时值与相量波形的同步输出

## 使用的方法


- [[co-simulation]]
- [[dynamic-phasor]]
- [[multirate]]
- [[transmission-line]]

## 涉及的模型


- [[mmc-model]]
- [[transmission-line]]

## 相关主题


- [[hvdc]]
- [[vsc-hvdc]]
- [[co-simulation]]
- [[dynamic-phasor]]

## 主要发现



- SFP模型允许采用比传统EMT大得多的时间步长，在满足精度要求的前提下显著提升了大规模交直流系统的仿真效率
- 所提HMD-TLM接口模型能够准确反映SFP域与EMT域之间的动态交互，在CIGRE标准系统及实际MMC多端直流电网中验证了方法的高精度与高效性