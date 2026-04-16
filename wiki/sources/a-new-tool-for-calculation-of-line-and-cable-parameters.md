---
title: "A new tool for calculation of line and cable parameters"
type: source
year: 2023
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf"]
---

# A new tool for calculation of line and cable parameters

**年份**: 2023
**来源**: `02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf`

## 摘要

−This paper presents a new tool for the computation of per-unit-length parameters for transmission line and cable models used for simulating electromagnetic transients (EMT). The proposed methodology is based on the MoM-SO theory and state-of-the-art formulations for the computation of the series impedance and shunt admittance parameters. The new tool has major advantages compared to traditional approaches available in EMT-type software. These advantages include accurate skin and proximity effect modeling, above-ground cable modeling, modeling of stranded wires in cables, representation of multilayer soil, coupled overhead lines and underground cables, etc. This paper presents the

## 核心贡献


- 提出基于MoM-SO理论的新型参数计算工具，实现高精度单位长度参数求解
- 突破传统程序局限，精确计及集肤与邻近效应、多层土壤及混合线路耦合
- 将先进算法集成至EMTP平台，支持传统方法无法实现的复杂暂态仿真


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[表面导纳算子-so|表面导纳算子(SO)]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[等效定理|等效定理]]
- [[电场积分方程|电场积分方程]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[架空线路|架空线路]]
- [[地下电缆|地下电缆]]
- [[多绞线电缆|多绞线电缆]]
- [[多层土壤模型|多层土壤模型]]
- [[架空-地下混合线路|架空-地下混合线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[单位长度参数计算|单位长度参数计算]]
- [[集肤与邻近效应|集肤与邻近效应]]
- [[线路-电缆参数计算|线路/电缆参数计算]]
- [[emtp集成|EMTP集成]]


## 主要发现


- 新工具计算精度媲美有限元法，且计算效率显著优于传统有限元技术
- 成功实现架空与地下混合线路及多层土壤耦合暂态仿真，验证模型有效性
- 精确计及集肤与邻近效应，解决传统程序在复杂电缆建模中的精度不足问题


