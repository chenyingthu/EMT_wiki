---
title: "Dual-Band Reduced-Order Model of an HVDC Link Embedded into a Power Network for EMT Studies"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2019.2935892"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TEC.2019.2935892.pdf.pdf"]
---

# Dual-Band Reduced-Order Model of an HVDC Link Embedded into a Power Network for EMT Studies

**作者**: 
**年份**: 2019
**来源**: `13&14/files/TEC.2019.2935892.pdf.pdf`

## 摘要

—This paper presents an approach to obtain reduced- order models for power networks involving power electronic converters (PEC) via the frequency-domain balanced realizations (FDBR) technique. PECs play an essential role in power processing and energy conversion in modern electrical networks, such as the interconnection of renewable generators, HVDC links, and active filters. Integration of PECs into dynamic equivalents needs model-order reduction (MOR) in both low- and high- frequency ranges to account for both slow and fast dynamics due to the network and switching natures. The objective of the FDBR technique is to obtain an internally balanced system, i.e., an equally controllable/observable system, that can be reduced according to its dominant dynamics within the limited frequency band

## 核心贡献


- 提出基于频域平衡实现的双频段降阶方法，兼顾电网低频与换流器高频开关动态。
- 将FDBR技术应用于含换流器电网，实现特定频带内的局部状态空间降阶拟合。
- 双频段局部拟合相比全频段降阶，在维持仿真精度的同时显著降低计算复杂度。


## 使用的方法


- [[频域平衡实现法-fdbr|频域平衡实现法(FDBR)]]
- [[模型降阶-mor|模型降阶(MOR)]]
- [[李雅普诺夫方程求解|李雅普诺夫方程求解]]
- [[状态空间直接截断|状态空间直接截断]]
- [[双频段拟合技术|双频段拟合技术]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[电力电子换流器-pec|电力电子换流器(PEC)]]
- [[交流电网等效模型|交流电网等效模型]]
- [[线性时不变状态空间模型|线性时不变状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[模型降阶|模型降阶]]
- [[频域分析|频域分析]]
- [[电力系统动态等值|电力系统动态等值]]
- [[开关频率动态|开关频率动态]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 双频段降阶模型在保持时域精度的同时，显著提升了仿真速度并降低了计算资源消耗。
- 相比全频段降阶，双频段拟合能更精准捕捉换流器开关频率附近的电磁暂态特性。
- 频域平衡实现法有效兼顾了电网低频机电振荡与电力电子高频开关动态的仿真需求。


