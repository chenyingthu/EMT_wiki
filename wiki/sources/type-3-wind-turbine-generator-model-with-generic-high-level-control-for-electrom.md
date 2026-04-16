---
title: "Type-3 wind turbine generator model with generic high-level control for electromagnetic transient simulations"
type: source
authors: ['Anton Stepanov']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112205. doi:10.1016/j.epsr.2025.112205"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/39/Stepanov 等 - 2026 - Type-3 wind turbine generator model with generic high-level control for electromagnetic transient si.pdf"]
---

# Type-3 wind turbine generator model with generic high-level control for electromagnetic transient simulations

**作者**: Anton Stepanov
**年份**: 2025
**来源**: `39/Stepanov 等 - 2026 - Type-3 wind turbine generator model with generic high-level control for electromagnetic transient si.pdf`

## 摘要

Type-3 wind turbine generator model with generic high-level control for Electromagnetic transient (EMT) simulations are instrumental in providing researchers and engineers with detailed data about the dynamic behavior of power grids, necessary for analysis, planning, and risk mitigation. Such simulation studies become even more relevant with the increased number of inverter-based resources in­ tegrated into the grid. To achieve reliable simulation results, accurate and accessible models are need

## 核心贡献



- 提出了一种用于电磁暂态(EMT)仿真的三型风力发电机(DFIG)模型
- 将WECC通用高层控制系统与详细的DFIG电气模型相结合，实现控制参数无缝复用
- 显著提升了平衡与不对称故障等快速暂态工况下的仿真精度

## 使用的方法


- [[state-space]]
- [[numerical-integration]]

## 涉及的模型


- [[dfig]]
- [[dfig-model]]

## 相关主题


- [[wind-farm]]
- [[dynamic-phasor]]

## 主要发现



- 所提模型在保留WECC通用控制架构优势的同时，通过详细电气建模克服了传统相量域模型在快速暂态中精度不足的问题
- 模型可直接继承现有WECC模型的控制参数设置，无需在EMT环境中重新整定，大幅提高了工程应用效率
- 在对称与不对称故障等极端暂态条件下，该模型能够提供比简化通用模型更准确的动态响应数据