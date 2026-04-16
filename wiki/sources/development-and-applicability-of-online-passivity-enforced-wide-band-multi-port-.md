---
title: "Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port Equivalents For Hybrid Transient Simulation"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Systems; ;PP;99;10.1109/TPWRS.2018.2885240"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRS.2018.2885240.pdf.pdf"]
---

# Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port Equivalents For Hybrid Transient Simulation

**作者**: 
**年份**: 2018
**来源**: `13&14/files/TPWRS.2018.2885240.pdf.pdf`

## 摘要

—This paper presents a method for developing sin- gle and multi-port Frequency Dependent Network Equivalent (FDNE) based on a passivity enforced online recursive least squares (RLS) identiﬁcation algorithm which identiﬁes the input admittance matrix in z-domain. Further, with the proposed archi- tecture, a real-time hybrid model of the reduced power system is developed that integrate Transient Stability Analysis (TSA) and FDNE. Main advantages of the proposed architecture are, it identiﬁes the FDNE even with unknown network parameters in the frequency range of interest, and yet can be implemented directly due to discrete formulation while maintaining desired accuracy, stability and passivity conditions. The accuracy and characteristics of the proposed method are veriﬁed by imple- menting o

## 核心贡献


- 提出基于在线递推最小二乘的z域导纳辨识算法，实现无宽频参数下的多端口FDNE构建
- 设计离散域直接实现的FDNE架构，在线强制满足无源性与稳定性条件，便于实时接口
- 构建融合TSA低频机电与FDNE高频电磁特性的混合等值模型，兼顾精度与计算效率


## 使用的方法


- [[在线递推最小二乘辨识|在线递推最小二乘辨识]]
- [[矢量拟合|矢量拟合]]
- [[kron节点消去法|Kron节点消去法]]
- [[暂态稳定分析|暂态稳定分析]]
- [[离散域z变换建模|离散域z变换建模]]
- [[发电机相干性分组|发电机相干性分组]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[tsa等值模型|TSA等值模型]]
- [[同步发电机|同步发电机]]
- [[聚合发电机模型|聚合发电机模型]]
- [[多端口输电网络|多端口输电网络]]
- [[ieee-39-68节点系统|IEEE 39/68节点系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[网络等值|网络等值]]
- [[频率相关建模|频率相关建模]]
- [[无源性强制|无源性强制]]
- [[模型降阶|模型降阶]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 在IEEE标准节点系统验证中，所提FDNE在宽频范围内保持高精度与数值稳定性
- 混合架构有效保留高频电磁暂态与低频机电振荡特性，计算负担显著低于全EMT模型
- 在线辨识无需预知宽频导纳数据，离散域实现可直接嵌入实时仿真器且严格满足无源性


