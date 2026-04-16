---
title: "A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM"
type: source
year: 2019
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Shu 等 - 2019 - A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM.pdf"]
---

# A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM

**年份**: 2019
**来源**: `02/Shu 等 - 2019 - A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM.pdf`

## 摘要

— To accurately capture the dynamics of a large-scale AC/DC system as a whole and the interactions between its individual components, a simulation method with high precision and efficiency is in great demand. For this purpose, we develop a multi-domain co-simulation method, in which the target system is partitioned into multiple DC and AC subsystems, represented by our proposed shifted frequency phasor (SFP) models }and the traditional EMT models, respectively. SFP models can be simulated with a much larger time step, leading to a significant improvement in simulation efficiency under a given requirement of precision. Further, a new interface model, namely, hybrid multi-domain transmission-line model (HMD-TLM), is developed to reflect the interactions between SFP models and EMT models, wit

## 核心贡献


- 提出直流移频相量模型支持更大仿真步长显著提升大规模系统计算效率
- 开发混合多域传输线接口实现移频相量与电磁暂态域交互及波形同步输出
- 设计多域协同仿真时序架构实现交直流子系统分区高效高精度联合仿真


## 使用的方法


- [[移频相量法|移频相量法]]
- [[多域协同仿真|多域协同仿真]]
- [[混合多域传输线模型接口|混合多域传输线模型接口]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统分区解耦|系统分区解耦]]


## 涉及的模型


- [[sfp模型|SFP模型]]
- [[emt模型|EMT模型]]
- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[交流电网|交流电网]]
- [[cigre交直流测试系统|CIGRE交直流测试系统]]


## 相关主题


- [[交直流混合系统仿真|交直流混合系统仿真]]
- [[多域协同仿真|多域协同仿真]]
- [[高效仿真|高效仿真]]
- [[接口建模|接口建模]]
- [[大规模电网动态分析|大规模电网动态分析]]


## 主要发现


- 在CIGRE及实际MMC系统中验证该方法在保持精度的同时显著提升仿真效率
- 新接口模型能准确传递交直流交互动态并同步输出瞬时值与相量波形
- 移频相量模型允许采用更大仿真步长有效降低大规模交直流系统计算负担


