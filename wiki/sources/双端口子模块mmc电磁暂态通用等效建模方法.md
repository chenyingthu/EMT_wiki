---
title: "双端口子模块MMC电磁暂态通用等效建模方法"
type: source
authors: ['徐义良']
year: 2018
journal: "中国电机工程学报"
tags: ['mmc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/徐义良 等 - 2018 - 双端口子模块MMC电磁暂态通用等效建模方法.pdf"]
---

# 双端口子模块MMC电磁暂态通用等效建模方法

**作者**: 徐义良
**年份**: 2018
**来源**: `40/徐义良 等 - 2018 - 双端口子模块MMC电磁暂态通用等效建模方法.pdf`

## 摘要

This paper proposed an accurate and high-speed electromagnetic transient (EMT) equivalent modeling method for arbitrary novel two-port MMC by using paralleled full bridge sub-module (SMs) modular multilevel converter topology.

## 核心贡献



- 提出适用于任意双端口MMC的电磁暂态通用等效建模方法
- 设计递归节点消去算法，将桥臂等效为4个外部节点并完整保留内部动态信息
- 在PSCAD/EMTDC环境中验证了所提模型的高精度与显著加速效果

## 使用的方法


- [[nodal-analysis]]
- [[network-equivalent]]

## 涉及的模型


- [[mmc-model]]

## 相关主题


- [[mmc]]
- [[hvdc]]
- [[vsc-hvdc]]

## 主要发现



- 递归消去算法能在大幅降低计算复杂度的同时精确复现系统内外动态特性
- 所提等效模型相比传统详细模型显著提升了电磁暂态仿真速度
- 该方法克服了传统单端口等效算法的局限，可通用化应用于各类双端口子模块拓扑