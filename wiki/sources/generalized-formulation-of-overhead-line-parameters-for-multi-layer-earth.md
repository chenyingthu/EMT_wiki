---
title: "Generalized Formulation of Overhead Line Parameters for Multi-Layer Earth"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2021.3049595"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/tpwrd.2021.3049595.pdf-1.pdf"]
---

# Generalized Formulation of Overhead Line Parameters for Multi-Layer Earth

**作者**: 
**年份**: 2021
**来源**: `19、20、21/EMT_task_20/tpwrd.2021.3049595.pdf-1.pdf`

## 摘要

—A generalized formulation of earth-return impedance and admittance for overhead lines above a multi-layer earth is derived. An equivalent homogeneous earth method (EHEM) and a Method of Moments - Surface Admittance Operator (MoM-SO) method with modified earth-return Green function considering an N-layer earth are also proposed. The frequency responses of wave propagation characteristics are evaluated by the newly proposed formulas and compared to those found from existing formulas in software used for the simulation of electromagnetic transients. Transient simulations performed in an electromagnetic transient (EMT) type simulation tool are also presented. It is shown that the proposed generalized formulas, the

## 核心贡献


- 推导了架空线路在四层大地下的精确大地返回阻抗与导纳广义公式
- 提出改进的等效均匀大地法，引入介电常数与导纳，突破卡森假设限制
- 推导适用于N层大地的修正MoM-SO格林函数，消除高频数值不稳定性


## 使用的方法


- [[精确解析法|精确解析法]]
- [[等效均匀大地法-ehem|等效均匀大地法(EHEM)]]
- [[矩量法-表面导纳算子-mom-so|矩量法-表面导纳算子(MoM-SO)]]
- [[修正格林函数法|修正格林函数法]]
- [[emtp暂态仿真|EMTP暂态仿真]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[多层大地模型|多层大地模型]]
- [[大地返回阻抗-导纳模型|大地返回阻抗/导纳模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[架空线路参数计算|架空线路参数计算]]
- [[多层大地建模|多层大地建模]]
- [[波传播特性分析|波传播特性分析]]
- [[过电压-浪涌分析|过电压/浪涌分析]]
- [[频率相关建模|频率相关建模]]


## 主要发现


- 新公式、改进EHEM与修正MoM-SO在宽频带内结果高度一致，验证了理论正确性
- 改进EHEM能准确反映大地介电常数影响，显著提升高频段波传播计算精度
- EMTP暂态仿真表明新方法计算效率高，适用于电力系统过电压与浪涌分析


