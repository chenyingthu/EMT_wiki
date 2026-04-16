---
title: "Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phasor Models"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Access; ;PP;99;10.1109/ACCESS.2018.2884506"
tags: ['mmc', 'real-time']
created: "2026-04-13"
sources: ["EMT_Doc/32/ACCESS.2018.2884506.pdf.pdf"]
---

# Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phasor Models

**作者**: 
**年份**: 2018
**来源**: `32/ACCESS.2018.2884506.pdf.pdf`

## 摘要

The real-time simulation of modular multilevel converter (MMC) is essential to the evaluation and validation of its control and protection systems. Moreover, the dynamics at both sub-module level and system level are expected from the real-time simulations of MMCs. To achieve this objective, the paper proposes the shifted phasor modelling (SPM) of the MMC by representing each sub-module with a Thevenin equivalent circuit that is derived using shifted phasors with improved accuracy. The efﬁciency of the SPM is guaranteed by modelling each arm as a switch-dependent Thevenin equivalent circuit. The computational burden remains almost unchanged even when the number of sub-modules increases considerably. The proposed model are materialized using ﬁeld programmable gate array (FPGA). And thus the

## 核心贡献


- 提出移位相量建模法，以戴维南等效电路表征子模块，显著提升仿真精度。
- 将桥臂建模为开关依赖型戴维南等效电路，子模块增多时计算负担几乎不变。
- 基于FPGA实现电容电压并行更新，兼顾系统级与子模块级动态特性。


## 使用的方法


- [[移位相量法|移位相量法]]
- [[节点分析法|节点分析法]]
- [[戴维南等效电路|戴维南等效电路]]
- [[开关依赖建模|开关依赖建模]]
- [[并行计算|并行计算]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[双半桥子模块-dbsm|双半桥子模块(DBSM)]]
- [[交叉连接双半桥子模块-cc-dbsm|交叉连接双半桥子模块(CC-DBSM)]]
- [[低压直流系统|低压直流系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[直流故障闭锁|直流故障闭锁]]
- [[子模块级动态|子模块级动态]]


## 主要发现


- 验证表明模型可同时输出宽频带相量与瞬时值，精度显著优于传统平均值模型。
- 子模块数量大幅增加时计算负担几乎不变，FPGA实现完全满足实时性要求。
- 模型能准确捕捉混合MMC直流故障闭锁期间的桥臂电流与电容电压动态。


