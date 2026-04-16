---
title: "Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit Model"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Electronics; ;PP;99;10.1109/TPEL.2026.3677417"
tags: ['adc']
created: "2026-04-13"
sources: ["EMT_Doc/09/Lai 等 - 2026 - Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit Model.pdf"]
---

# Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit Model

**作者**: 
**年份**: 2026
**来源**: `09/Lai 等 - 2026 - Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit Model.pdf`

## 摘要

— Gallium nitride high electron mobility transistors (GaN HEMTs) have been considered as potential power semicon- ductor devices in modern power electronics owing to their high switching speed and low conduction loss, which facilitate efficient and compact solutions in high-frequency applications. However, their fast-switching behavior introduces challenges like volt- age/current overshoot and parasitic sensitivity, necessitating accu- rate modeling for circuit optimization. This paper proposes an as- sociate discrete circuit (ADC) model for half-bridge leg inspired by the fixed-equivalent-admittance methodology in electromag- netic transient (EMT) simulations. Unlike traditional piece-wise linear state-space models that require switching between different equation sets, the proposed ADC-b

## 核心贡献


- 提出关联离散电路半桥统一模型，全模态节点导纳矩阵恒定，避免状态方程频繁重构
- 将非线性结电容等效为固定电容并联补偿电流源，实现导纳恒定与历史电流动态更新
- 建立覆盖ZVS与硬开关工况的完整解析模型，支持零初始条件直接启动且无需迭代


## 使用的方法


- [[关联离散电路模型|关联离散电路模型]]
- [[固定等效导纳法|固定等效导纳法]]
- [[梯形积分法|梯形积分法]]
- [[诺顿等效电路|诺顿等效电路]]
- [[解析建模|解析建模]]


## 涉及的模型


- [[gan-hemt|GaN HEMT]]
- [[半桥桥臂|半桥桥臂]]
- [[非线性结电容|非线性结电容]]
- [[pcb寄生参数|PCB寄生参数]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[开关瞬态建模|开关瞬态建模]]
- [[高频电力电子|高频电力电子]]
- [[非线性电容建模|非线性电容建模]]
- [[开关损耗评估|开关损耗评估]]


## 主要发现


- 仿真与实验验证表明，该模型能精确复现开关瞬态与稳态波形，误差极小
- 相比传统分段线性状态空间法，计算效率显著提升，适用于快速开关损耗评估
- 模型支持零初始条件直接启动，避免了传统周期性迭代不收敛或发散的问题


