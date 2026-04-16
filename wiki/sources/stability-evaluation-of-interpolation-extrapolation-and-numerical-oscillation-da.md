---
title: "Stability Evaluation of Interpolation, Extrapolation, and Numerical Oscillation Damping Methods Applied in EMT Simulation of Power Networks with Switching Transients"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3018651"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/TPWRD.2020.3018651.pdf.pdf"]
---

# Stability Evaluation of Interpolation, Extrapolation, and Numerical Oscillation Damping Methods Applied in EMT Simulation of Power Networks with Switching Transients

**作者**: 
**年份**: 2020
**来源**: `35/TPWRD.2020.3018651.pdf.pdf`

## 摘要

—For Electro-Magnetic-Transient (EMT) simulations of power networks with switches, techniques such as linear interpolation and Critical Damping Adjustment (CDA) are widely used for improving numerical robustness. This paper analyzes the numerical stability of simulations with these techniques. Firstly, it is mathematically shown that the interpolation or CDA step is equivalent to the introduction of additional switching states. Subsequently, Common Quadratic Lyapunov Function (CQLF) theory is used to investigate the numerical stability of the whole simulation considering these new switching states. It is proved that the widely used strategies like linear interpolation and CDA always result a stable simulation if the original switched system is strictly passive in all switching states. Fina

## 核心贡献



- 数学证明了线性插值与临界阻尼调整（CDA）等效于在仿真中引入额外的开关状态
- 引入公共二次李雅普诺夫函数（CQLF）理论，建立了含开关切换的EMT仿真数值稳定性分析框架
- 证明了该分析框架可推广用于评估其他实际插值与外推算法的数值稳定性

## 使用的方法


- [[interpolation]]
- [[numerical-integration]]
- [[state-space]]

## 涉及的模型

- [[含开关电力网络|含开关电力网络]]
- [[电力电子器件|电力电子器件]]
- [[二极管|二极管]]

## 相关主题


- [[passivity]]

## 主要发现



- 线性插值和CDA步骤在数学上可严格等效为系统引入了额外的开关状态
- 若原始开关系统在所有开关状态下均满足严格无源性，则采用线性插值或CDA的EMT仿真必然保持数值稳定
- 基于CQLF的稳定性判据为各类插值、外推及数值振荡抑制方法提供了通用的理论验证工具