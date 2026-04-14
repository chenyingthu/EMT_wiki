---
title: "Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet"
type: source
authors: ['Jurij']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Wang - 2010 - Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet.pdf"]
---

# Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet

**作者**: Jurij
**年份**: 2010
**来源**: `26/Wang - 2010 - Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了用于EMTP仿真的同步电机与感应电机电压-电抗（VBR）新模型
- 将磁饱和特性成功融入VBR模型，并开发了适用于状态变量仿真语言的全阶VBR感应电机模型
- 提出了近似VBR感应电机模型，实现恒定等效导纳矩阵以避免网络矩阵的重复分解

## 使用的方法

- [[电压-电抗-vbr-建模公式|电压-电抗（VBR）建模公式]]
- [[直接机网接口技术|直接机网接口技术]]
- [[特征值缩放优化|特征值缩放优化]]
- [[磁饱和非线性建模|磁饱和非线性建模]]
- [[离散化emtp求解与恒定导纳矩阵技术|离散化EMTP求解与恒定导纳矩阵技术]]

## 涉及的模型

- [[同步电机vbr模型|同步电机VBR模型]]
- [[感应电机vbr模型|感应电机VBR模型]]
- [[含磁饱和的vbr模型|含磁饱和的VBR模型]]
- [[全阶vbr感应电机模型|全阶VBR感应电机模型]]
- [[近似vbr感应电机模型|近似VBR感应电机模型]]
- [[传统qd轴参考系模型与相域-pd-模型|传统qd轴参考系模型与相域(PD)模型]]

## 相关主题

- [[电磁暂态仿真-emtp|电磁暂态仿真(EMTP)]]
- [[交流电机建模|交流电机建模]]
- [[电力系统暂态分析|电力系统暂态分析]]
- [[数值计算效率与精度优化|数值计算效率与精度优化]]
- [[磁饱和效应处理|磁饱和效应处理]]

## 主要发现

- VBR模型相比传统qd和PD模型显著提升了数值精度与计算效率，单步计算仅需约240次（同步电机）和108次（感应电机）浮点运算，大幅降低CPU耗时
- 含磁饱和的VBR模型在大步长下仍保持高精度与稳定性；全阶模型计算效率较传统耦合电路模型提升740%；近似模型通过恒定导纳矩阵避免了每步网络矩阵重分解，进一步优化了机网联合求解效率
