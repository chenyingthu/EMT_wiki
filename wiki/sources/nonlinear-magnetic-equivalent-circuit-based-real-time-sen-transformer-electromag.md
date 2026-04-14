---
title: "Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Model on FPGA for HIL Emulation"
type: source
authors: ['Jiadai Liu', 'Venkata Dinavahi']
year: 2016
journal: "IEEE Transactions on Power Delivery;2016;31;6;10.1109/TPWRD.2016.2518676"
tags: ['real-time', 'fpga', 'transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Mode.pdf"]
---

# Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Model on FPGA for HIL Emulation

**作者**: Jiadai Liu, Venkata Dinavahi
**年份**: 2016
**来源**: `27&28/Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Mode.pdf`

## 摘要

—Strategic power-ﬂow control using a Sen transformer (ST) can be a robust and cost-effective solution to relieve grid con- gestion due to increased installation of renewables. The ST con- sists of a multiwinding transformer and tap changer that can reg- ulate the power ﬂow through a transmission line by injecting a series-connected controllable voltage. This paper develops a real- time high-ﬁdelity magnetic equivalent circuit-based electromag- netic transient model for the ST on the ﬁeld-programmable gate array (FPGA) for hardware-in-the-loop applications. This geom- etry-based model was developed to depict the major ﬂux paths in the transformer core, and complex nonlinear phenomena, such as saturation, hysteresis, and eddy currents. The entire real-time ST model and other power system com

## 核心贡献

- 建立了更精确的transformer电磁暂态模型，考虑了频率相关特性和非线性效应
- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[磁等效电路法|磁等效电路法]]
- [[有限元法|有限元法]]
- [[硬件描述语言实现|硬件描述语言实现]]
- [[并行流水线架构|并行流水线架构]]
- [[32位浮点运算|32位浮点运算]]

## 涉及的模型

- [[transformer-model]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

—Strategic power-ﬂow control using a Sen transformer (ST) can be a robust and cost-effective solution to relieve grid con- gestion due to increased installation of renewables
