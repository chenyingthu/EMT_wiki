---
title: "Empirical model of a current-limiting fuse using EMTP"
type: source
authors: ['A. Petit', 'G. St-Jean', 'G. Fecteau']
year: 1998
journal: "IEEE Transactions on Power Delivery;1989;4;1;10.1109/61.19221"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/17/Petit 等 - 1989 - Empirical Model of a Current-Limiting Fuse using EMTP.pdf"]
---

# Empirical model of a current-limiting fuse using EMTP

**作者**: A. Petit, G. St-Jean, G. Fecteau
**年份**: 1998
**来源**: `17/Petit 等 - 1989 - Empirical Model of a Current-Limiting Fuse using EMTP.pdf`

## 摘要

Authorized licensed use limited to: Tsinghua University. Downloaded on April 10,2026 at 03:50:46 UTC from IEEE Xplore.  Restrictions apply.

## 核心贡献


- 提出限流熔断器经验模型，利用电容与非线性电阻分别等效电弧电压上升与下降阶段
- 基于TACS设计开关控制逻辑，依据焦耳积分与过渡电压实现熔断、升压与熄弧切换
- 模型无需复杂物理参数，可快速评估电源合闸角对熔断器通过能量及电压波形的影响


## 使用的方法


- [[经验建模|经验建模]]
- [[tacs控制逻辑|TACS控制逻辑]]
- [[伏安特性拟合|伏安特性拟合]]
- [[开关逻辑控制|开关逻辑控制]]
- [[焦耳积分计算|焦耳积分计算]]


## 涉及的模型


- [[限流熔断器|限流熔断器]]
- [[配电变压器|配电变压器]]
- [[理想熔断器|理想熔断器]]
- [[等效电路模型|等效电路模型]]


## 相关主题


- [[配电网保护|配电网保护]]
- [[故障限流|故障限流]]
- [[电弧电压建模|电弧电压建模]]
- [[焦耳积分分析|焦耳积分分析]]
- [[合闸角影响分析|合闸角影响分析]]


## 主要发现


- 电源合闸角显著影响熔断器通过焦耳积分，在熔断时间小于四分之一周期时差异最大
- 熔断器电压上升越快且维持高位时间越长，限流效果越好，通过能量显著降低
- 经验模型能准确复现实测伏安特性曲线，在EMTP中数值稳定且易于非专家使用


