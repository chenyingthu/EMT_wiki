---
title: "Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators"
type: source
authors: ['K. Mudunkotuwa']
year: 2018
journal: "Electric Power Systems Research, 163 (2018) 423-429. doi:10.1016/j.epsr.2018.06.010"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Mudunkotuwa和Filizadeh - 2018 - Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators.pdf"]
---

# Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators

**作者**: K. Mudunkotuwa
**年份**: 2018
**来源**: `10/Mudunkotuwa和Filizadeh - 2018 - Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators.pdf`

## 摘要

Co-simulation of electrical networks by interfacing EMT and dynamic- b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada The paper presents a hybrid co-simulator comprising EMT and dynamic phasor-based simulators. The EMT simulator models portion(s) of the network wherein fast transients are prevalent and detailed modeling is ne- cessary. The dynamic phasor solver models the rest of the network using extended-frequency Fourier compo-

## 核心贡献


- 提出EMT与动态相量混合协同架构，实现网络分区高效求解
- 开发瞬时EMT与动态相量样本精确映射算法，保障接口数据传递精度
- 解决多速率时间步长接口问题，确保大范围谐波仿真下的数值稳定性


## 使用的方法


- [[动态相量法|动态相量法]]
- [[多速率仿真|多速率仿真]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[梯形积分法|梯形积分法]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[接口数据映射算法|接口数据映射算法]]


## 涉及的模型


- [[ieee-118节点系统|IEEE 118节点系统]]
- [[风电场|风电场]]
- [[电力电子变流器|电力电子变流器]]
- [[输电网络|输电网络]]
- [[旋转电机|旋转电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[网络分区|网络分区]]
- [[谐波分析|谐波分析]]
- [[数值稳定性|数值稳定性]]
- [[风电场建模|风电场建模]]


## 主要发现


- 在不同时间步长比下验证接口精度，混合仿真显著降低整体计算耗时
- 基于IEEE 118节点系统验证协同架构的数值稳定性与波形还原精度
- 动态相量法有效替代外部网络详细建模，在保证精度前提下大幅提升效率


