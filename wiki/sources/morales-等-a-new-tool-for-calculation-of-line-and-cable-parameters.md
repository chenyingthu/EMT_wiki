---
title: "Morales 等 | A new tool for calculation of line and cable parameters"
type: source
authors: ['54']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf"]
---

# Morales 等 | A new tool for calculation of line and cable parameters

**作者**: 54
**年份**: 2023
**来源**: `02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf`

## 摘要

−This paper presents a new tool for the computation of per-unit-length parameters for transmission line and cable models used for simulating electromagnetic transients (EMT). The proposed methodology is based on the MoM-SO theory and state-of-the-art formulations for the computation of the series impedance and shunt admittance parameters. The new tool has major advantages compared to traditional approaches available in EMT-type software. These advantages include accurate skin and proximity effect modeling, above-ground cable modeling, modeling of stranded wires in cables, representation of multilayer soil, coupled overhead lines and underground cables, etc. This paper presents the

## 核心贡献


- 提出基于矩量法与表面导纳算子的新工具，实现线路电缆单位长度参数高精度计算
- 突破传统程序局限，精确计及集肤与邻近效应、多层土壤及架空地下混合线路耦合建模
- 将新算法完整集成至EMTP平台，并通过实际暂态仿真案例验证其工程适用性


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[表面导纳算子-so|表面导纳算子(SO)]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[等效原理|等效原理]]
- [[电场积分方程|电场积分方程]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[架空线路|架空线路]]
- [[地下电缆|地下电缆]]
- [[架空电缆|架空电缆]]
- [[绞线导体|绞线导体]]
- [[多层土壤模型|多层土壤模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[单位长度参数计算|单位长度参数计算]]
- [[频率相关建模|频率相关建模]]
- [[集肤与邻近效应|集肤与邻近效应]]
- [[线路与电缆常数计算|线路与电缆常数计算]]
- [[emtp集成|EMTP集成]]


## 主要发现


- 新工具计算精度媲美有限元法，但计算负担显著降低，满足电磁暂态仿真效率需求
- 成功实现架空与地下混合线路及多层土壤耦合建模，突破传统程序的应用局限
- 暂态仿真案例验证了该工具在复杂线路配置下的参数计算准确性与工程实用性


