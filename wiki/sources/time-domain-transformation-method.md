---
title: "Time Domain Transformation Method"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/tpwrs.2012.2188913.pdf.pdf"]
---

# Time Domain Transformation Method

**作者**: 
**年份**: 2012
**来源**: `37/tpwrs.2012.2188913.pdf.pdf`

## 摘要

—Electromagnetic Transients Program (EMTP) is widely used in power system dynamics studies. However, in most cases EMTP is found inadequate for dealing with the realistic size power systems due to the small time step resulting in relatively slow simulation speeds. To accelerate the EMTP simulations of power system dynamics, a novel frequency-adaptive methodology is proposed. In this method, a new transformation is presented. The properties of the transformation and the numerical solutions based on the transformation are discussed. The component models obtained by discretizing the differential equations at the branch level are also given which are convenient for EMTP implementa- tion. The proposed method allows using large time steps without sacriﬁcing accuracy, which greatly improves the s

## 核心贡献



- 提出一种新型频域自适应时域变换方法以加速EMTP仿真
- 允许在不牺牲精度的情况下使用大时间步长，显著提升大规模电力系统动态仿真速度
- 提供支路级离散化的元件伴随模型，便于在EMTP中直接实现

## 使用的方法


- [[dynamic-phasor]]
- [[numerical-integration]]
- [[nodal-analysis]]
- [[co-simulation]]
- [[parallel]]

## 涉及的模型


- [[fdne]]
- [[network-equivalent]]

## 相关主题


- [[real-time]]
- [[harmonic]]
- [[frequency-dependent]]

## 主要发现



- 所提变换方法可在保持宽频动态特性精度的前提下显著增大仿真步长
- 该方法有效克服了传统EMTP因小步长导致的计算缓慢问题，大幅提升了仿真效率
- 支路级离散化模型具有良好的EMTP兼容性，并通过多种算例验证了其有效性与实用性