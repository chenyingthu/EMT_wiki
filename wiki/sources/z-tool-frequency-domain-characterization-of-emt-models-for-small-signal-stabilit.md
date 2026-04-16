---
title: "Z-Tool: Frequency-domain characterization of EMT models for small-signal stability analysis"
type: source
authors: ['Francisco', 'Javier', 'Cifuentes', 'Garcia']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112405. doi:10.1016/j.epsr.2025.112405"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/Cifuentes Garcia和Beerten - 2026 - Z-Tool Frequency-domain characterization of EMT models for small-signal stability analysis.pdf"]
---

# Z-Tool: Frequency-domain characterization of EMT models for small-signal stability analysis

**作者**: Francisco, Javier, Cifuentes 等
**年份**: 2025
**来源**: `40/Cifuentes Garcia和Beerten - 2026 - Z-Tool Frequency-domain characterization of EMT models for small-signal stability analysis.pdf`

## 摘要

Z-Tool: Frequency-domain characterization of EMT models for small-signal a Department of Electrical Engineering (ESAT-ELECTA), KU Leuven, 3000, Leuven, Belgium This paper presents a novel frequency-domain identiﬁcation tool based on Electromagnetic Transient (EMT) simulations: Z-tool. This is the ﬁrst open source program oﬀering a versatile automated scan and state-of-the- art small-signal analysis of multi-terminal AC, DC and AC/DC power systems. The approach is introduced with

## 核心贡献



- 开发了首个开源的基于EMT仿真的频域识别工具Z-Tool，支持多端交直流系统的自动化扫描与小信号稳定性分析
- 提出了多频激励与对称性利用等优化策略，显著降低计算耗时，并量化了时间步长依赖下的精度与效率权衡

## 使用的方法


- [[numerical-integration]]
- [[state-space]]
- [[frequency-dependent]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-hvdc]]
- [[hvdc]]

## 相关主题


- [[harmonic]]
- [[passivity]]
- [[network-equivalent]]

## 主要发现



- 基于EMT的频域识别误差具有时间步长依赖性，需在计算效率与模型精度之间进行合理权衡
- 采用多频激励与对称性优化可大幅缩短扫描时间，同时保持对次同步振荡等小信号稳定性评估的准确性