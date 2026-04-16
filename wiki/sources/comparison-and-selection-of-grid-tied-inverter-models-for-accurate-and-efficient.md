---
title: "Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Electronics;2022;37;3;10.1109/TPEL.2021.3117633"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Sano 等 - 2022 - Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations.pdf"]
---

# Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations

**作者**: 
**年份**: 2021
**来源**: `10/Sano 等 - 2022 - Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations.pdf`

## 摘要

—This article compares ﬁve modeling methods of grid- tied inverters for the electromagnetic transient simulation of power system, clariﬁes their differences, and discusses the suitable model for each simulation purpose. The comparison was made under the same conditions between the conventional switching model, and four simpliﬁed models—voltage interpolation, average-value, con- trolled current-injection, and simpliﬁed current-injection model. The comparison of the simulated waveforms clariﬁes the behaviors that can be simulated and cannot be simulated by each simpliﬁed model. The comparison of the computing time reveals the signiﬁ- cant decrease of the computing time by selecting the proper sim- pliﬁed modeling method. Based on these comparisons, this article discusses the selection of the

## 核心贡献


- 系统对比五种并网逆变器EMT模型，明确各模型适用场景与仿真边界
- 揭示简化模型在谐波与暂态响应仿真能力的差异，量化计算时间缩减效果
- 提出基于仿真目的的逆变器模型选型指南，实现精度与计算效率的平衡


## 使用的方法


- [[节点分析法|节点分析法]]
- [[固定步长仿真|固定步长仿真]]
- [[平均值建模|平均值建模]]
- [[电压插值法|电压插值法]]
- [[电流注入法|电流注入法]]
- [[状态空间平均法|状态空间平均法]]


## 涉及的模型


- [[并网逆变器|并网逆变器]]
- [[三相桥式逆变器|三相桥式逆变器]]
- [[开关模型|开关模型]]
- [[平均值模型|平均值模型]]
- [[电压插值模型|电压插值模型]]
- [[受控电流注入模型|受控电流注入模型]]
- [[简化电流注入模型|简化电流注入模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[模型对比与选型|模型对比与选型]]
- [[谐波分析|谐波分析]]
- [[暂态稳定性分析|暂态稳定性分析]]
- [[计算效率优化|计算效率优化]]
- [[新能源并网|新能源并网]]


## 主要发现


- 开关模型精度最高但耗时最长，电压插值模型可准确复现谐波且计算量显著降低
- 平均值与受控电流注入模型适用于系统级暂态分析，但无法捕捉高频开关谐波
- 简化电流注入模型计算最快，仅适用于大电网低频动态分析，高频暂态误差大


