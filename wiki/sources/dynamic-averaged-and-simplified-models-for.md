---
title: "Dynamic Averaged and Simplified Models for"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2013.2251912.pdf.pdf"]
---

# Dynamic Averaged and Simplified Models for

**作者**: 
**年份**: 2013
**来源**: `13&14/files/TPWRD.2013.2251912.pdf.pdf`

## 摘要

—Voltage-source converter (VSC) technologies are rapidly evolving and increasing the range of applications in a variety of ﬁelds within the power industry. Existing two- and three-level VSC technologies are being superseded by the new modular multilevel converter (MMC) technology for HVDC applications. The computational burden caused by detailed mod- eling of MMC–HVDC systems in electromagnetic transient-type (EMT-type) programs complicates the simulation of transients when such systems are integrated into large networks. This paper develops and compares different types of models for efﬁcient and accurate representation of MMC–HVDC systems. The results show that the use of a speciﬁc type of model will depend on the conducted analysis and required accuracy. Index Terms—Average-value model

## 核心贡献


- 提出并对比多种MMC-HVDC电磁暂态简化与平均值模型，显著降低计算负担
- 建立动态平均值建模指南，明确不同模型在精度与效率间的适用场景与选择依据
- 在点对点直流输电系统中验证各模型的动态响应特性与计算性能差异


## 使用的方法


- [[动态平均值建模|动态平均值建模]]
- [[详细非线性开关模型|详细非线性开关模型]]
- [[最近电平逼近调制|最近电平逼近调制]]
- [[环流抑制控制|环流抑制控制]]
- [[电容电压均衡控制|电容电压均衡控制]]
- [[dq矢量控制|dq矢量控制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[半桥子模块|半桥子模块]]
- [[igbt阀|IGBT阀]]
- [[桥臂电抗器|桥臂电抗器]]
- [[平均值模型|平均值模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态平均值建模|动态平均值建模]]
- [[mmc-model|MMC]]
- [[计算效率优化|计算效率优化]]
- [[降阶模型|降阶模型]]
- [[大电网暂态分析|大电网暂态分析]]


## 主要发现


- 平均值模型可大幅增大积分步长并降低计算资源消耗，适用于大系统暂态分析
- 模型选择需权衡分析目标与精度需求，简化模型能有效复现开关动态响应
- 详细模型虽精度高但计算负担重，仅适用于局部器件级精细仿真场景


