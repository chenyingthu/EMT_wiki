---
title: "Development of phase domain frequency-dependent transmission line model on FPGA for real-time digital simulator"
type: source
authors: ['Jiadai Liu']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107305. doi:10.1016/j.epsr.2021.107305"
tags: ['real-time', 'fpga', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/J.EPSR.2021.107305.pdf-1.pdf"]
---

# Development of phase domain frequency-dependent transmission line model on FPGA for real-time digital simulator

**作者**: Jiadai Liu
**年份**: 2021
**来源**: `13&14/files/J.EPSR.2021.107305.pdf-1.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Development of phase domain frequency-dependent transmission line Jiadai Liu a,*, Yuan Chen a, Hui Ding a, Yi Zhang a a RTDS Technologies Inc., Winnipeg, MB, R3T 2E1, Canada The transmission line model is one of the most important components for the real-time digital simulator based on

## 核心贡献


- 提出基于FPGA的频变相域输电线路模型，避免模域变换矩阵误差
- 采用全流水线与并行硬件架构设计，显著降低仿真步长并提升实时性
- 设计48位自定义浮点数据格式，在硬件实现中兼顾计算精度与资源


## 使用的方法


- [[频变相域建模|频变相域建模]]
- [[并行计算|并行计算]]
- [[流水线技术|流水线技术]]
- [[诺顿等效|诺顿等效]]
- [[卷积运算|卷积运算]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变相域模型|频变相域模型]]
- [[通用线路模型|通用线路模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[频率相关建模|频率相关建模]]
- [[并行计算|并行计算]]
- [[电磁暂态分析|电磁暂态分析]]


## 主要发现


- 全流水线并行架构使模型实现微秒级仿真步长，满足高频暂态实时计算需求
- 48位自定义浮点格式有效平衡硬件资源与计算精度，确保模型数值稳定性
- 相域直接计算避免模域变换矩阵误差，显著提升不对称线路的仿真精度


