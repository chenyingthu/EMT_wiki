---
title: "Current Source Modular Multilevel Converter Modeling and Control"
type: source
authors: ['未知']
year: 2016
journal: "IEEE Transactions on Power Delivery"
tags: ['mmc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/29/TPWRD.2016.2590569.pdf-1.pdf"]
---

# Current Source Modular Multilevel Converter Modeling and Control

**作者**: 未知
**年份**: 2016
**来源**: `29/TPWRD.2016.2590569.pdf-1.pdf`

## 摘要

Current source modular multilevel converter (CSMMC) is a good alternative for high-power applications with medium-voltage and high-current requirements. To obtain the multilevel output current, the submodule capacitors are designed to maintain constant voltages.

## 核心贡献


- 提出CSMMC桥臂诺顿等效两节点模型，消除内部中间节点，大幅降低电磁暂态仿真计算负担
- 构建支持冗余子模块故障安全研究的混合模型，兼顾子模块级动态特性与仿真效率
- 在PSCAD中通过FORTRAN实现等效模型，验证其在背靠背系统动态研究中的高精度


## 使用的方法


- [[诺顿等效建模|诺顿等效建模]]
- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[混合建模|混合建模]]
- [[自定义fortran模块|自定义FORTRAN模块]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[背靠背变流器系统|背靠背变流器系统]]
- [[传统详细模型|传统详细模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[等效建模|等效建模]]
- [[动态特性研究|动态特性研究]]
- [[背靠背变流器|背靠背变流器]]
- [[电流平衡控制|电流平衡控制]]


## 主要发现


- 等效模型仿真结果与传统详细模型高度吻合，在保持精度的同时显著缩短计算时间
- 混合模型可准确复现冗余子模块故障安全功能及电流平衡控制器的动态交互特性
- 背靠背系统动态仿真验证表明，该模型适用于中高压大功率场景的系统级暂态分析


