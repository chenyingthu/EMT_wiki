---
title: "级联H桥型电力电子变压器的电磁暂态等效建模方法"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/丁江萍 等 - 2020 - 级联H桥型电力电子变压器的电磁暂态等效建模方法.pdf"]
---

# 级联H桥型电力电子变压器的电磁暂态等效建模方法

**作者**: CNKI
**年份**: 2022
**来源**: `16/丁江萍 等 - 2020 - 级联H桥型电力电子变压器的电磁暂态等效建模方法.pdf`

## 摘要

The power electronic transformer (PET) applied to the medium and high voltage distribution network widely adopts a two-stage cascade structure of a cascaded H-bridge rectifier and a dual-active bridge DC/DC converter. Aiming at the problem of extremely slow simulation speed in offline simulation platforms such as PSCAD/EMTDC and MATLAB, based on the Thévenin’s equivalent and nested fast simultaneous solving algorithm, an electromagnetic transient simulation accelerated model of cascaded H-bridge PET was proposed. Specifically, by arranging the decoupling companion network of the primary/secondary side of the high-frequency transformer flexibly, the cascaded sub-modules were divided into two single-port networks, and then the equivalent part of the Thévenin’s (Norton’s) equivalent parameter

## 核心贡献



- 提出基于戴维南/诺顿等效与嵌套快速同时求解算法的级联H桥型电力电子变压器电磁暂态仿真加速模型
- 通过构造高频变压器解耦伴随网络将级联子模块等效为仅含4个外部节点的单端口网络，使系统整体求解的计算复杂度几乎不随子模块数量增加

## 使用的方法


- [[network-equivalent]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]

## 相关主题


- [[network-equivalent]]
- [[transformer]]

## 主要发现



- 所提等效模型在PSCAD/EMTDC平台中能够精确复现级联H桥型电力电子变压器的暂态与稳态过程
- 模型外部等效节点数固定，计算复杂度不随子模块数量增长，相比详细模型具有极高的仿真加速比