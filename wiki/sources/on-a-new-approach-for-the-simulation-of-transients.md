---
title: "On a new approach for the simulation of transients"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/29/j.epsr.2006.08.027.pdf.pdf"]
---

# On a new approach for the simulation of transients

**作者**: 
**年份**: 2007
**来源**: `29/j.epsr.2006.08.027.pdf.pdf`

## 摘要

This paper presents a new simulation tool named EMTP-RV. EMTP-RV is a completely new program with a new graphical user interface and a new computational engine. The simulation uses a new matrix formulation for computing load-ﬂow, steady state and time-domain solutions. Theoretical advantages are emphasized and demonstrated through practical examples. An open-architecture graphical user interface (GUI) is developed to maximize ﬂexibility and allow creating and maintaining complex designs. © 2006 Elsevier B.V. All rights reserved. Keywords: Simulation tools; Numerical methods; EMTP 1. Introduction Since its initial concept presented in 1969 [1] the basic EMTP type simulation approach remained unchanged. It is used in var- ious commercial (DCG-EMTP Version 3, EMTP-V3 [2]) and non-commercial p

## 核心贡献


- 提出改进的增广节点分析法，统一处理理想开关与变压器，避免矩阵秩变问题
- 基于牛顿法构建雅可比矩阵，实现非线性设备与电机模型的真正同步迭代求解
- 重构底层计算引擎与开放式GUI架构，彻底摆脱传统Fortran代码限制


## 使用的方法


- [[增广节点分析法|增广节点分析法]]
- [[牛顿迭代法|牛顿迭代法]]
- [[梯形积分法|梯形积分法]]
- [[谐波稳态求解|谐波稳态求解]]
- [[潮流计算|潮流计算]]


## 涉及的模型


- [[理想电压源|理想电压源]]
- [[理想变压器|理想变压器]]
- [[理想开关|理想开关]]
- [[电机模型|电机模型]]
- [[非线性设备|非线性设备]]
- [[控制系统|控制系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值计算方法|数值计算方法]]
- [[仿真软件架构|仿真软件架构]]
- [[网络方程求解|网络方程求解]]
- [[稳态初始化|稳态初始化]]


## 主要发现


- 固定秩矩阵公式使开关切换无需重构网络，大幅降低高频开关场景的计算开销
- 雅可比求解法彻底消除控制反馈回路数值延迟，提升非线性暂态仿真精度
- 新架构成功实现潮流、稳态与时域求解的统一矩阵表达，验证了算法通用性


