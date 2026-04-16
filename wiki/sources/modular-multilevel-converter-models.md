---
title: "Modular Multilevel Converter Models"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modular Multilevel Converter Models for Electromagnetic Transients.pdf"]
---

# Modular Multilevel Converter Models

**作者**: 
**年份**: 2013
**来源**: `27&28/Modular Multilevel Converter Models for Electromagnetic Transients.pdf`

## 摘要

—Modular multilevel converters (MMCs) may contain numerous insulated-gate bipolar transistors. The modeling of such converters for electromagnetic transient-type (EMT-type) simula- tions is complex. Detailed models used in MMC-HVDC simula- tions may require very large computing times. Simpliﬁed and av- eraged models have been proposed in the past to overcome this problem. In this paper, existing averaged and simpliﬁed models are improved in order to increase their range of applications. The models are compared and analyzed for different transient events on an MMC-HVDC system. Index Terms—Average-value model (AVM), EMT-type pro- grams, HVDC transmission, modular multilevel

## 核心贡献


- 提出基于开关函数原理的MMC桥臂等效模型，显著提升仿真效率。
- 改进等效电路模型，引入迭代算法精确处理子模块闭锁状态。
- 设计梯形积分与后向欧拉法切换策略，有效消除状态突变振荡。


## 使用的方法


- [[平均值模型|平均值模型]]
- [[开关函数法|开关函数法]]
- [[等效电路法|等效电路法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[迭代求解算法|迭代求解算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[半桥子模块|半桥子模块]]
- [[igbt开关模型|IGBT开关模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[mmc-model|MMC]]
- [[模型简化与等效|模型简化与等效]]
- [[数值振荡抑制|数值振荡抑制]]
- [[暂态事件分析|暂态事件分析]]


## 主要发现


- 改进模型在401电平MMC仿真中平均仅需少于3次迭代即可收敛。
- 迭代算法结合后向欧拉法切换，有效消除闭锁状态切换引发的振荡。
- 简化模型在多种暂态工况下保持较高精度，并大幅降低计算时间。


