---
title: "Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number of Electromagnetic"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Chen 等 - 2020 - Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number of Electromagnetic.pdf"]
---

# Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number of Electromagnetic

**作者**: CNKI
**年份**: 2022
**来源**: `17/Chen 等 - 2020 - Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number of Electromagnetic.pdf`

## 摘要

1: With the rapid development of UHVDC and the step-by-step improvement of its transmission capacity, China's power grid has the characteristics of “Strong HVDC and weak AC system”. The coupling between the transmitting and receiving ends, AC and HVDC, and multiple HVDCs is getting closer and closer so that the operating characteristics of the power grid are becoming increasingly complex. In the simulation analysis of large-scale AC-DC power grids, the HVDC obtains accurate dynamic characteristics and the AC grids can improve its simulation efficiency via electromagnetic transient simulation. However, the hybrid simulation with multiple HVDC electromagnetic transient models

## 核心贡献


- 提出直流标准化建模与数据映射拼接技术，实现混合仿真数据自动建立。
- 提出基于内部潮流计算的电磁直流模型工况自动调整与微调方法。
- 提出接口电压箝位平稳启动策略，使混合仿真在0.6s内快速达到稳态。


## 使用的方法


- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[数据映射拼接|数据映射拼接]]
- [[内部潮流计算|内部潮流计算]]
- [[工况自动调整与微调|工况自动调整与微调]]
- [[接口电压箝位启动|接口电压箝位启动]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[换流变压器|换流变压器]]
- [[交流滤波器|交流滤波器]]
- [[六脉冲换流器|六脉冲换流器]]
- [[直流输电线路|直流输电线路]]
- [[频率相关线路模型|频率相关线路模型]]
- [[简化控制保护模型|简化控制保护模型]]


## 相关主题


- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[大规模交直流电网|大规模交直流电网]]
- [[特高压直流输电|特高压直流输电]]
- [[批量仿真计算|批量仿真计算]]
- [[运行工况初始化|运行工况初始化]]
- [[换相失败分析|换相失败分析]]


## 主要发现


- 自动化建模与数据拼接技术显著降低人工干预，提升大批量仿真效率。
- 内部潮流计算与工况自动微调使电磁模型初始状态与潮流数据高度一致。
- 接口箝位启动策略有效消除暂态冲击，混合仿真可在0.6s内快速达稳态。


