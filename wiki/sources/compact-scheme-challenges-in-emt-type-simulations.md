---
title: "Compact scheme challenges in EMT-Type simulations"
type: source
authors: ['M.', 'Jafari', 'Matehkolaei']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112403. doi:10.1016/j.epsr.2025.112403"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Matehkolaei 等 - 2026 - Compact scheme challenges in EMT-Type simulations.pdf"]
---

# Compact scheme challenges in EMT-Type simulations

**作者**: M., Jafari, Matehkolaei
**年份**: 2025
**来源**: `10/Matehkolaei 等 - 2026 - Compact scheme challenges in EMT-Type simulations.pdf`

## 摘要

This paper investigates the potential of using the compact scheme (CS) integration method for Electromagnetic Transient simulation of power systems due to its high accuracy. It focuses on the challenges encountered with CS at discontinuity instants. Initially, the accurate response of the components at discontinuities and the impact of iterations at slope changes of nonlinear devices are elaborated. Afterward, the performance of CS at disconti­ nuities is investigated. This work demonstrates tha

## 核心贡献


- 提出CS与后向欧拉结合的CS_BE方法有效解决不连续点处的数值异常问题
- 推导紧凑格式在改进型增广节点分析法框架下的网络方程离散化公式
- 揭示非线性器件斜率变化时牛顿迭代对仿真精度的影响机制及物理响应规律


## 使用的方法


- [[紧凑格式积分法|紧凑格式积分法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[改进型增广节点分析法|改进型增广节点分析法]]
- [[稀疏表法|稀疏表法]]
- [[牛顿迭代法|牛顿迭代法]]
- [[不连续点处理|不连续点处理]]


## 涉及的模型


- [[理想电感|理想电感]]
- [[电容|电容]]
- [[分段线性非线性器件|分段线性非线性器件]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值积分方法|数值积分方法]]
- [[不连续点处理|不连续点处理]]
- [[非线性特性分析|非线性特性分析]]
- [[网络方程构建|网络方程构建]]


## 主要发现


- 紧凑格式在不连续点处会产生数值异常需结合后向欧拉法进行特殊处理
- 提出的CS_BE方法有效消除了开关动作与非线性斜率变化引发的数值振荡
- 基于MANA框架的CS离散化公式计算精度与EMTP一致验证了方法有效性


