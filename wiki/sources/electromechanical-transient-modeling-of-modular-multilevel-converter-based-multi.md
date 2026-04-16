---
title: "Electromechanical Transient Modeling of Modular Multilevel Converter Based Multi-Terminal HVDC Systems"
type: source
authors: ['未知']
year: 2013
journal: "IEEE Transactions on Power Systems;2014;29;1;10.1109/TPWRS.2013.2278402"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/17/Liu 等 - 2014 - Electromechanical transient modeling of modular multilevel converter based multi-terminal hvdc syste.pdf"]
---

# Electromechanical Transient Modeling of Modular Multilevel Converter Based Multi-Terminal HVDC Systems

**作者**: 
**年份**: 2013
**来源**: `17/Liu 等 - 2014 - Electromechanical transient modeling of modular multilevel converter based multi-terminal hvdc syste.pdf`

## 摘要

—This paper studies the techniques for modeling mod- ular multilevel converter (MMC) based multi-terminal HVDC (MTDC) systems in the electromechanical transient mode. Firstly, the mathematical model of the MMC and its corresponding equivalent circuit are established, which are similar to those of the two level converters. Then, a power ﬂow calculation method for AC/DC systems containing MMC-MTDC systems is developed. Two dynamic models for MMC-MTDC systems are developed in the paper. One is the detailed model, taking into account of the AC side circuit, the inner controllers, the modulation strategies, the outer controllers and the MTDC circuit. The other is the simpliﬁed model, which only reserves the outer controllers and partial dynamics of the MTDC circuit based on a quantitative analy

## 核心贡献


- 提出适用于机电暂态仿真的MMC-MTDC详细与简化动态模型，支持大步长计算
- 建立含MMC-MTDC交直流系统的潮流计算方法，实现换流器节点等效处理
- 推导MMC交流侧等效电路模型，将桥臂串联电感等效为相电感以简化分析


## 使用的方法


- [[机电暂态建模|机电暂态建模]]
- [[潮流计算|潮流计算]]
- [[等效电路法|等效电路法]]
- [[动态过程定量分析|动态过程定量分析]]
- [[节点分析|节点分析]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mtdc|MTDC]]
- [[vsc-model|VSC]]
- [[换流变压器|换流变压器]]
- [[同步发电机|同步发电机]]
- [[交直流电网|交直流电网]]


## 相关主题


- [[机电暂态仿真|机电暂态仿真]]
- [[多端直流输电|多端直流输电]]
- [[电力系统稳定性|电力系统稳定性]]
- [[交直流潮流|交直流潮流]]
- [[故障隔离|故障隔离]]
- [[模型降阶|模型降阶]]


## 主要发现


- 详细与简化模型在PSS/E中实现，与PSCAD电磁暂态模型对比验证了精度
- 简化模型通过忽略快速动态过程，可在机电暂态仿真中采用更大步长且保持精度
- 异步联网的MMC-MTDC系统能有效隔离交流侧故障，提升大电网暂态稳定性


