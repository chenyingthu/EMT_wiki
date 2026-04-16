---
title: "Interfacing Factor-Based White-Box Transformer Modeling Method"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/24/Gustavsen和Portillo - 2014 - Interfacing ${rm k}$-Factor Based White-Box Transformer Models With Electromagnetic Transients Prog.pdf"]
---

# Interfacing Factor-Based White-Box Transformer Modeling Method

**作者**: 
**年份**: 2014
**来源**: `24/Gustavsen和Portillo - 2014 - Interfacing ${rm k}$-Factor Based White-Box Transformer Models With Electromagnetic Transients Prog.pdf`

## 摘要

—White-box transformer models are used by trans- former manufacturers during the dielectric design of windings. The models are often based on constant parameters (RLCG ma- trices) with the high-frequency losses accounted for by a scaling of the dc resistance ( -Factor). We show an efﬁcient procedure for interfacing such models with Electromagnetic Transients Program (EMTP)-type circuit simulators via state equations and a Norton equivalent. The approach makes no approximations except for the discretization in the time domain. Diagonalization is utilized for achieving high computational efﬁciency. Proprietary information about internal voltages is optionally hidden from the user. Internal surge arresters are handled by the EMTP circuit solver by declaring their connection points as external

## 核心贡献


- 提出基于状态方程与诺顿等效的白盒变压器接口方法实现与EMTP求解器无缝对接
- 引入矩阵对角化技术提升计算效率并支持隐藏内部电压以保护制造商专有信息
- 实现工频稳态自动初始化并通过外部节点声明灵活处理内部避雷器接入


## 使用的方法


- [[状态方程法|状态方程法]]
- [[诺顿等效|诺顿等效]]
- [[矩阵对角化|矩阵对角化]]
- [[时域离散化|时域离散化]]
- [[集中参数建模|集中参数建模]]
- [[工频自动初始化|工频自动初始化]]


## 涉及的模型


- [[白盒变压器模型|白盒变压器模型]]
- [[集中参数变压器模型|集中参数变压器模型]]
- [[rlcg网络模型|RLCG网络模型]]
- [[cigre虚拟变压器|CIGRE虚拟变压器]]
- [[内部避雷器|内部避雷器]]


## 相关主题


- [[emtp接口技术|EMTP接口技术]]
- [[变压器内部过电压分析|变压器内部过电压分析]]
- [[高频损耗近似建模|高频损耗近似建模]]
- [[专有模型共享|专有模型共享]]
- [[绝缘配合仿真|绝缘配合仿真]]


## 主要发现


- 基于CIGRE虚拟变压器仿真验证表明该接口能精确复现端子与内部节点暂态响应
- 矩阵对角化处理在保持计算精度的同时显著降低求解耗时满足大规模网络仿真需求
- 工频自动初始化与内部避雷器外部节点声明机制均通过测试验证了接口的工程实用性


