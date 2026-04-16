---
title: "Multi-layer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2019.2930406"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multilayer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations.pdf"]
---

# Multi-layer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations

**作者**: 
**年份**: 2019
**来源**: `27&28/Multilayer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations.pdf`

## 摘要

—This paper proposes a technique to approximate a multi-layer earth structure by a homogeneous conductivity soil in ground return impedance calculations. An equivalent real- valued conductivity parameter is obtained, which can be used with reasonable accuracy in a simpler expression or in commonly available EMTP software, such as the Line Constants routine of the Alternative Transients Program (ATP). Several actual soil models are evaluated at frequencies ranging from from 1 Hz to 2 MHz. Results show that the proposed method is accurate for modeling most power system problems, from steady-state conditions to transients commonly veriﬁed in electrical systems. The proposed expression is easy to use and introduces a con- siderable performance gain in terms of ﬂoating-point operations, compare

## 核心贡献


- 提出等效均匀电导率参数，实现N层土壤结构向均匀介质的精确近似
- 基于电流穿透系数构建自底向上逐层等效算法，简化多层土壤建模
- 推导兼容ATP等主流EMTP软件的简化公式，提升地回路阻抗计算效率


## 使用的方法


- [[卡森公式|卡森公式]]
- [[等效均匀介质近似|等效均匀介质近似]]
- [[逐层等效算法|逐层等效算法]]
- [[频率扫描分析|频率扫描分析]]


## 涉及的模型


- [[多层土壤模型|多层土壤模型]]
- [[架空导线|架空导线]]
- [[地回路阻抗模型|地回路阻抗模型]]
- [[输电线路参数|输电线路参数]]


## 相关主题


- [[地回路阻抗计算|地回路阻抗计算]]
- [[频率相关建模|频率相关建模]]
- [[土壤电导率建模|土壤电导率建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路参数计算|输电线路参数计算]]


## 主要发现


- 在电力系统频段内，等效模型与精确N层解析解相比相对误差仅约1%
- 在1Hz至2MHz宽频带内保持高精度，可准确覆盖稳态至电磁暂态工况
- 大幅减少浮点运算量，相比复杂多层解析公式具有显著的计算性能优势


