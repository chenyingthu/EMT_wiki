---
title: "Development of phase domain frequency-dependent transmission line model on FPGA for real-time digital simulator"
type: source
authors: ['Jiadai Liu']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107305. doi:10.1016/j.epsr.2021.107305"
tags: ['real-time', 'fpga', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/J.EPSR.2021.107305.pdf.pdf"]
---

# Development of phase domain frequency-dependent transmission line model on FPGA for real-time digital simulator

**作者**: Jiadai Liu
**年份**: 2021
**来源**: `13&14/files/J.EPSR.2021.107305.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Development of phase domain frequency-dependent transmission line Jiadai Liu a,*, Yuan Chen a, Hui Ding a, Yi Zhang a a RTDS Technologies Inc., Winnipeg, MB, R3T 2E1, Canada The transmission line model is one of the most important components for the real-time digital simulator based on

## 核心贡献


- 提出基于FPGA的频变相域线路模型，采用全流水线并行架构实现最小仿真步长。
- 设计自定义48位浮点运算单元与VHDL硬件逻辑，显著提升模型数值计算精度。
- 直接在相域执行递归卷积运算，消除模域变换矩阵误差，适配非对称线路仿真。


## 使用的方法


- [[相域频变建模|相域频变建模]]
- [[递归卷积计算|递归卷积计算]]
- [[全流水线并行架构|全流水线并行架构]]
- [[自定义48位浮点运算|自定义48位浮点运算]]
- [[诺顿等效电路法|诺顿等效电路法]]


## 涉及的模型


- [[频变相域输电线路模型|频变相域输电线路模型]]
- [[多相输电线路|多相输电线路]]


## 相关主题


- [[实时数字仿真|实时数字仿真]]
- [[电磁暂态分析|电磁暂态分析]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[频率相关建模|频率相关建模]]
- [[并行计算|并行计算]]
- [[硬件在环测试|硬件在环测试]]


## 主要发现


- 硬件全流水线设计使仿真步长降至微秒级，满足电力电子高频暂态实时计算需求。
- 48位浮点格式有效抑制硬件量化误差，模型在宽频带内的数值精度显著提升。
- 模型成功与外部网络求解器接口，验证了其在大规模实时数字仿真系统中的兼容性。


