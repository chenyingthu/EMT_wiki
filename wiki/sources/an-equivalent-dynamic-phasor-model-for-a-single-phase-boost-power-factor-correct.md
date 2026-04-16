---
title: "An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Open Journal of Power Electronics;2025;6; ;10.1109/OJPEL.2025.3560554"
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter.pdf"]
---

# An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter

**作者**: 
**年份**: 2025
**来源**: `07&08/An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter.pdf`

## 摘要

To mitigate harmonic current ﬂow in distribution systems, single-phase diode-bridge rectiﬁers (DBRs) are commonly equipped with active power factor correction (PFC) controllers. Achieving high power quality and dynamic performance in PFC controller design demands a precise understanding of PFC converter behavior. While detailed electromagnetic transient (EMT) simulations provide accurate insights, they are time-consuming. To address this, the dynamic phasor (DP) method offers a more efﬁcient modeling approach for power converters. This paper introduces and explores the DP model of a single-phase boost PFC converter, along with guidelines to integrate it with existing simulation platforms. To overcome challenges arising from differing driving frequencies (line frequency for the DBR and swit

## 核心贡献


- 提出基于符号函数变换的等效动态相量模型，解决多频激励下的PFC建模难题。
- 推导动态相量小信号模型，保留宽频谐波动态特性，适用于谐振补偿器设计。
- 建立系统化控制设计流程，利用DP模型精确整定开关模型与硬件原型控制参数。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[符号函数变换|符号函数变换]]
- [[小信号分析|小信号分析]]
- [[等效建模|等效建模]]
- [[线性化分析|线性化分析]]


## 涉及的模型


- [[单相boost-pfc变换器|单相Boost PFC变换器]]
- [[二极管整流桥|二极管整流桥]]
- [[等效有源整流器|等效有源整流器]]
- [[动态相量模型|动态相量模型]]
- [[小信号模型|小信号模型]]


## 相关主题


- [[动态相量建模|动态相量建模]]
- [[功率因数校正|功率因数校正]]
- [[控制器参数整定|控制器参数整定]]
- [[谐波分析|谐波分析]]
- [[仿真加速|仿真加速]]
- [[电力电子变换器|电力电子变换器]]


## 主要发现


- DP模型与详细EMT仿真结果高度吻合，且大幅缩短数值计算时间。
- DP小信号模型准确捕捉二次谐波与电感电流动态，验证了控制设计有效性。
- 硬件实验证实该模型可直接用于实际PFC变换器控制系统的参数整定与优化。


