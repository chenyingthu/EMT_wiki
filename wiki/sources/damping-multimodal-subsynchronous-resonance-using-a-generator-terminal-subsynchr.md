---
title: "Damping multimodal subsynchronous resonance using a generator terminal subsynchronous damping controller"
type: source
authors: ['Xiaorong Xie']
year: 2013
journal: "Electric Power Systems Research, 99 (2013) 1-8. 10.1016/j.epsr.2012.11.020"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/12/Xie 等 - 2013 - Damping multimodal subsynchronous resonance using a generator terminal subsynchronous damping contro.pdf"]
---

# Damping multimodal subsynchronous resonance using a generator terminal subsynchronous damping controller

**作者**: Xiaorong Xie
**年份**: 2013
**来源**: `12/Xie 等 - 2013 - Damping multimodal subsynchronous resonance using a generator terminal subsynchronous damping contro.pdf`

## 摘要

1. Introduction the STATCOM-based scheme, auxiliary subsynchronous damping controller (SSDC) is generally adopted, which, by modulating the Series-capacitor compensation in long-distance transmission reactive current reference or bus voltage of STATCOM, produces systems is a very economical metho...

## 核心贡献


- 提出发电机端次同步阻尼控制器，通过多模态独立路径同时抑制次同步谐振
- 基于复转矩系数法建立输出电流与电磁转矩映射，实现控制器参数直接整定
- 采用非线性优化算法整定各模态增益与相位，提升变工况下的阻尼鲁棒性


## 使用的方法


- [[复转矩系数法|复转矩系数法]]
- [[非线性优化|非线性优化]]
- [[特征值分析|特征值分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电流跟踪控制|电流跟踪控制]]
- [[模态带通滤波|模态带通滤波]]


## 涉及的模型


- [[串联补偿输电系统|串联补偿输电系统]]
- [[汽轮发电机轴系|汽轮发电机轴系]]
- [[电力电子逆变器|电力电子逆变器]]
- [[多机系统|多机系统]]


## 相关主题


- [[次同步谐振|次同步谐振]]
- [[串联补偿系统|串联补偿系统]]
- [[多模态阻尼控制|多模态阻尼控制]]
- [[轴系扭振抑制|轴系扭振抑制]]
- [[发电机端附加控制|发电机端附加控制]]


## 主要发现


- 特征值分析表明控制器显著提升各扭振模态电气阻尼，有效消除谐振风险
- 电磁暂态仿真验证了多模态控制策略在不同工况下均能快速抑制轴系扭振
- 独立模态路径设计避免了频率耦合干扰，大幅增强了实际多机系统的稳定性


