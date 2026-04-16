---
title: "Generalized Formulation of Overhead Line Parameters for Multi-Layer Earth"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2021.3049595"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/tpwrd.2021.3049595.pdf.pdf"]
---

# Generalized Formulation of Overhead Line Parameters for Multi-Layer Earth

**作者**: 
**年份**: 2021
**来源**: `19、20、21/EMT_task_20/tpwrd.2021.3049595.pdf.pdf`

## 摘要

—A generalized formulation of earth-return impedance and admittance for overhead lines above a multi-layer earth is derived. An equivalent homogeneous earth method (EHEM) and a Method of Moments - Surface Admittance Operator (MoM-SO) method with modified earth-return Green function considering an N-layer earth are also proposed. The frequency responses of wave propagation characteristics are evaluated by the newly proposed formulas and compared to those found from existing formulas in software used for the simulation of electromagnetic transients. Transient simulations performed in an electromagnetic transient (EMT) type simulation tool are also presented. It is shown that the proposed generalized formulas, the

## 核心贡献


- 推导多层大地架空线大地返回阻抗与导纳广义精确公式突破Carson假设限制
- 提出引入等效传播常数的改进EHEM方法实现N层大地宽频参数高效计算
- 推导适用于N层大地的修正MoM-SO格林函数消除高频数值不稳定性


## 使用的方法


- [[精确公式推导|精确公式推导]]
- [[等效均匀大地法-ehem|等效均匀大地法(EHEM)]]
- [[矩量法-表面导纳算子-mom-so|矩量法-表面导纳算子(MoM-SO)]]
- [[修正格林函数法|修正格林函数法]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[多层大地模型|多层大地模型]]
- [[大地返回阻抗与导纳模型|大地返回阻抗与导纳模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[浪涌分析|浪涌分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[波传播特性|波传播特性]]
- [[大地返回参数计算|大地返回参数计算]]


## 主要发现


- 改进EHEM与精确公式及修正MoM-SO结果高度一致验证宽频计算精度
- 新公式在EMTP暂态仿真中准确复现多层大地波传播特性适用于高频浪涌分析
- 修正MoM-SO方法有效克服高频数值振荡提升多层大地线路参数计算稳定性


