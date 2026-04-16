---
title: "Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/Xu 等 - 2025 - Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En.pdf"]
---

# Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En

**作者**: 
**年份**: 2025
**来源**: `35/Xu 等 - 2025 - Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En.pdf`

## 摘要

—Due to the advanced features of multidirectional power transfer and fast smoothing of the power ﬂuctuation in renewable energy systems, the multiple-active-bridge based power-electronic-transformer (MAB-PET) with integrated energy storage units is becoming popular. However, the accurate elec- tromagnetic transient simulation of the MAB-PETs is extremely time-consuming due to the large number of circuit nodes and small time-step. This paper proposes a simpliﬁed EMT modeling approach for the MAB-PETs by employing the generalized state- space averaging method. First, the switching function method and Dommel algorithm are used to build the equivalent model of each power module. Further, the PET equivalent model is presented in a multi-port PM polymerization mode. The system is simpliﬁed by ap

## 核心贡献



- 提出基于广义状态空间平均法的MAB-PET简化电磁暂态（EMT）建模方法
- 构建多端口功率模块聚合等效模型，通过傅里叶分解忽略高次谐波，导出四端口等效电压源电路

## 使用的方法


- [[state-space]]
- [[average-value-model]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]
- [[mmc-model]]

## 相关主题


- [[harmonic]]
- [[network-equivalent]]
- [[dynamic-phasor]]

## 主要发现



- 所提简化等效模型在PSCAD/EMTDC中与详细模型对比具有极高的仿真精度
- 该模型通过状态平均与谐波忽略策略，使仿真速度比详细模型快2至3个数量级，有效克服了MAB-PET节点多、步长小导致的计算瓶颈