---
title: "Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations"
type: source
authors: ['M.B. Luchini']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109624. doi:10.1016/j.epsr.2023.109624"
tags: ['ibg']
created: "2026-04-13"
sources: ["EMT_Doc/17/Luchini 等 - 2023 - Equivalent grid-following inverter-based generator model for ATPATPDraw simulations.pdf"]
---

# Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations

**作者**: M.B. Luchini
**年份**: 2023
**来源**: `17/Luchini 等 - 2023 - Equivalent grid-following inverter-based generator model for ATPATPDraw simulations.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Equivalent grid-following inverter-based generator model for ATP/ATPDraw M.B. Luchini a,∗, O.E. Batista a, F.V. Lopes b, R.L.A. Reis b, B.A. Souza c a Department of Electrical Engineering, Federal University of Espírito Santo, Vitória, ES, Brazil b Department of Electrical Engineering, Federal University of Paraiba, João Pessoa, PB, Brazil

## 核心贡献


- 提出适用于EMTP的跟网型逆变器等效时域模型替代复杂全开关模型
- 在ATP平台实现并提供详细建模指南支持灵活配置不同控制策略
- 集成DSOGI-PLL与低通滤波锁相环精确捕捉畸变电网暂态同步动态


## 使用的方法


- [[时域等效建模|时域等效建模]]
- [[锁相环同步技术|锁相环同步技术]]
- [[参考坐标变换|参考坐标变换]]
- [[低通滤波技术|低通滤波技术]]


## 涉及的模型


- [[跟网型逆变器-ibr|跟网型逆变器(IBR)]]
- [[光伏发电系统|光伏发电系统]]
- [[vsc-model|VSC]]
- [[储能系统|储能系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[逆变器并网资源建模|逆变器并网资源建模]]
- [[故障穿越特性|故障穿越特性]]
- [[电网故障分析|电网故障分析]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 相比完整开关模型仿真耗时降低约70%显著提升大规模电网计算效率
- 故障工况下输出电流平均误差仅约2.33%准确复现逆变器暂态响应
- 采用DSOGI-PLL同步策略可有效抑制电网谐波保障电流合成质量


