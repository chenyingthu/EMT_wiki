---
title: "Real-Time MPSoC-Based Electrothermal Transient Simulation of Fault Tolerant MMC Topology"
type: source
authors: ['未知']
year: 2019
journal: "2020 IEEE Power & Energy Society General Meeting (PESGM);2020; ; ;10.1109/PESGM41954.2020.9281694"
tags: ['mmc', 'real-time']
created: "2026-04-13"
sources: ["EMT_Doc/32/pesgm41954.2020.9281694.pdf.pdf"]
---

# Real-Time MPSoC-Based Electrothermal Transient Simulation of Fault Tolerant MMC Topology

**作者**: 
**年份**: 2019
**来源**: `32/pesgm41954.2020.9281694.pdf.pdf`

## 摘要

Real-Time MPSoC-Based Electrothermal Transient Simulation of Fault Tolerant MMC 1Electrical and Computer Engineering, University of Alberta, 2Electrical and Computer Engg., University of Alberta (MMC) submodule (SM) topologies, the clamp double submodule (CDSM) has the capability of dc fault current limiting and utilizes a relatively small number of switching devices. Since CDSM has

## 核心贡献


- 提出CDSM子模块器件级电热模型，精确计算开关损耗、结温及瞬态波形
- 融合系统等效电路与器件级模型，有效降低计算负担并保障实时仿真性能
- 基于Xilinx Zynq MPSoC平台完成多端直流系统实时硬件仿真部署


## 使用的方法


- [[等效电路法|等效电路法]]
- [[器件级建模|器件级建模]]
- [[电热耦合仿真|电热耦合仿真]]
- [[实时仿真|实时仿真]]
- [[mpsoc硬件加速|MPSoC硬件加速]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[cdsm|CDSM]]
- [[igbt|IGBT]]
- [[多端直流系统|多端直流系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电热暂态|电热暂态]]
- [[直流故障穿越|直流故障穿越]]
- [[mmc-model|MMC]]
- [[多端直流系统|多端直流系统]]
- [[硬件加速|硬件加速]]


## 主要发现


- 模型在直流故障清除期间精确复现IGBT功率损耗与结温的动态耦合过程
- 仿真波形与PSCAD及SaberRD结果高度一致，验证了模型精度与实时性
- MPSoC硬件实现成功满足复杂CDSM电热模型的计算需求，实测波形稳定


