---
title: "Reduced-order and simultaneous solution of power and control system equations in EMT simulations,"
type: source
authors: ['Jiaming Wang']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112412. doi:10.1016/j.epsr.2025.112412"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/Wang 等 - 2026 - Reduced-order and simultaneous solution of power and control system equations in EMT simulations,.pdf"]
---

# Reduced-order and simultaneous solution of power and control system equations in EMT simulations,

**作者**: Jiaming Wang
**年份**: 2025
**来源**: `33/Wang 等 - 2026 - Reduced-order and simultaneous solution of power and control system equations in EMT simulations,.pdf`

## 摘要

Reduced-order and simultaneous solution of power and control system a State Key Laboratory of Smart Power Distribution Equipment and System, Tianjin University, Tianjin 300072, China b Department of Electrical Engineering, Polytechnique Montr´eal, Montr´eal, Qu´ebec H3T 1J4, Canada The time-step delay between the power and control system solutions in EMT simulation may cause inaccurate results or even numerical instability in certain scenarios. A simultaneous solution is preferred theoretically,

## 核心贡献



- 提出基于指数积分器的降阶同步求解方法，消除电力与控制系统方程求解间的时间步延迟
- 引入 Sylvester 方程及其线性变换，将非对角块矩阵指数求解难题转化为线性矩阵求解过程
- 提出矩阵子块特征值平移技术，解决因结构诱导重复特征值导致的 Sylvester 方程无解问题，提升求解鲁棒性

## 使用的方法


- [[state-space]]
- [[numerical-integration]]
- [[interpolation]]

## 涉及的模型


- [[vsc-model]]

## 相关主题


- [[real-time]]

## 主要发现



- 同步求解策略能有效消除传统分离求解引入的人工延迟，避免特定场景下的数值不稳定并显著提升换流器仿真精度
- 结合 Sylvester 方程与特征值平移技术的降阶算法成功解耦了矩阵指数计算，实现了状态变量的同步插值与统一时间步进，兼顾了计算效率与准确性