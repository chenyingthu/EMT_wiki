---
title: "A full frequency dependent line model based on folded line equivalencing and latency exploitation"
type: source
authors: ['Felipe Camara']
year: 2017
journal: "Electric Power Systems Research, 154 (2018) 352-360. doi:10.1016/j.epsr.2017.08.018"
tags: ['frequency-dependent']
created: "2026-04-13"
sources: ["EMT_Doc/01/Camara 等 - 2018 - A full frequency dependent line model based on folded line equivalencing and latency exploitation.pdf"]
---

# A full frequency dependent line model based on folded line equivalencing and latency exploitation

**作者**: Felipe Camara
**年份**: 2017
**来源**: `01/Camara 等 - 2018 - A full frequency dependent line model based on folded line equivalencing and latency exploitation.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出基于延迟利用的全频变输电线路有理逼近模型，提升时域仿真数值效率
- 开发多伴随网络(MCN)技术以有效分离系统动态中的快慢极点
- 实现基于极点特性的多时间步长仿真策略，优化计算资源分配

## 使用的方法

- [[延迟利用-latency-exploitation-与多时间步长策略|延迟利用(Latency exploitation)与多时间步长策略]]
- [[多伴随网络-multiple-companion-networks-mcn-技术|多伴随网络(Multiple Companion Networks, MCN)技术]]
- [[节点导纳矩阵的极点-留数表示法|节点导纳矩阵的极点-留数表示法]]
- [[有理逼近方法-如向量拟合|有理逼近方法(如向量拟合)]]

## 涉及的模型

- [[全频变输电线路模型|全频变输电线路模型]]
- [[频变网络等值模型|频变网络等值模型]]
- [[基于极点-留数形式的节点导纳矩阵模型|基于极点-留数形式的节点导纳矩阵模型]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态(EMT)仿真]]
- [[架空线路建模|架空线路建模]]
- [[网络综合与有理逼近|网络综合与有理逼近]]
- [[时域多速率仿真|时域多速率仿真]]

## 主要发现

- 通过为快慢极点分配不同时间步长可显著提升全频变线路时域仿真的计算效率
- 所提多时间步长策略在大幅减少计算量的同时未对仿真精度造成负面影响
