---
title: "Passivity Enforcement for Transmission Line Models"
type: source
authors: ['未知']
year: 2008
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2008.919034.pdf.pdf"]
---

# Passivity Enforcement for Transmission Line Models

**作者**: 
**年份**: 2008
**来源**: `31/TPWRD.2008.919034.pdf.pdf`

## 摘要

—The Universal Line Model (ULM) has been imple- mented in several EMT programs for simulation of electromag- netic transients. In some cases, instability problems have been encountered. This paper shows that the current approach for ra- tional function approximation adopted in ULM can lead to large out-of-band passivity violations, thereby causing an unstable sim- ulation. An approach is introduced which prevents the occurrence of large passivity violations. Low-frequency violations are avoided by adding an artiﬁcial shunt conductance to the diagonal elements of the shunt admittance matrix while high-frequency violations are avoided by introducing artiﬁcial attenuation using a low-pass ﬁlter. In addition, high-frequency asymptotic passivity is enforced for the characteristic admittance. An

## 核心贡献

- 建立了考虑频率相关特性的transmission-line模型，提高了暂态仿真精度
- 提出无源性强制校正方法，确保频率相关模型的数值稳定性

## 使用的方法

- [[passivity-enforcement]]

## 涉及的模型

- [[transmission-line-model]]

## 相关主题

（待进一步分析）

## 主要发现

—The Universal Line Model (ULM) has been imple- mented in several EMT programs for simulation of electromag- netic transients
