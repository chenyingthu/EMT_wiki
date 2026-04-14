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

- 提出了一种发电机端次同步阻尼控制器（GTSDC），用于抑制串联补偿电力系统中的多模态次同步谐振（SSR）
- 基于复转矩系数法推导了GTSDC输出电流与发电机电磁转矩之间的定量关系
- 采用非线性优化方法整定多模态控制路径参数，实现了不同工况下所有扭振模态阻尼的有效提升

## 使用的方法

- [[复转矩系数法|复转矩系数法]]
- [[非线性优化算法|非线性优化算法]]
- [[特征值分析|特征值分析]]
- [[电磁暂态-emt-仿真|电磁暂态（EMT）仿真]]
- [[电流跟踪控制技术|电流跟踪控制技术]]

## 涉及的模型

- [[发电机端次同步阻尼控制器-gtsdc|发电机端次同步阻尼控制器（GTSDC）]]
- [[带电流跟踪控制的电力电子逆变器|带电流跟踪控制的电力电子逆变器]]
- [[汽轮发电机组轴系模型|汽轮发电机组轴系模型]]
- [[实际串联补偿电力系统模型|实际串联补偿电力系统模型]]

## 相关主题

- [[次同步谐振-ssr-抑制|次同步谐振（SSR）抑制]]
- [[多模态扭振阻尼控制|多模态扭振阻尼控制]]
- [[串联补偿输电系统稳定性|串联补偿输电系统稳定性]]
- [[电力电子辅助阻尼装置|电力电子辅助阻尼装置]]
- [[电磁暂态仿真验证|电磁暂态仿真验证]]

## 主要发现

- GTSDC通过注入与扭振模态频率互补的电流，可在发电机轴系上产生正向阻尼转矩，从而有效抑制SSR
- 特征值分析与电磁暂态仿真结果表明，优化后的GTSDC在不同运行工况下均能显著增强所有扭振模态的阻尼，验证了控制策略的有效性与鲁棒性
