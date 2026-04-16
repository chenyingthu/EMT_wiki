---
title: "Combined transient and dynamic analysis of HVDC and FACTS systems"
type: source
authors: ['M. Sultan', 'J. Reeve', 'R. Adapa']
year: 2004
journal: "IEEE Transactions on Power Delivery;1998;13;4;10.1109/61.714495"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Sultan 等 - 1998 - Combined transient and dynamic analysis of HVDC and facts systems.pdf"]
---

# Combined transient and dynamic analysis of HVDC and FACTS systems

**作者**: M. Sultan, J. Reeve, R. Adapa
**年份**: 2004
**来源**: `10/Sultan 等 - 1998 - Combined transient and dynamic analysis of HVDC and facts systems.pdf`

## 摘要

A new approach to HVDC and FACTS transient/dynamic simula- tion based on an interactive execution of an ac transient stability program (TSP) and the Electro-Magnetic Transients Program (EMTP) is described. Through the integration of the detailed tran- sient model of FACTS with the transient stability program, authentic simulation is achieved without simplifications. Both HVDC and Thyristor Controlled Series Capacitor (TCSC) systems are used to validate the approach, under different coupling situa- tions between both TSP arid EMTP. Keywords: FACTS, HVDC, EMTP, Frequency Dependent Net- work Equivalents, Transient Stability Simulation. I. INTRODUCTION The ac transient stability programs based on fundamental fre- quency, single-phase, phasor modeling techniques cannot directly represent the fa

## 核心贡献


- 提出EMTP与暂态稳定程序交互执行的混合仿真架构，实现全频段精确模拟
- 构建时变戴维南/诺顿频变等值模型，实现外部交流网络高精度映射
- 采用最小二乘拟合提取三相基波正序相量，实现双程序间高精度数据交互


## 使用的方法


- [[混合仿真|混合仿真]]
- [[频变网络等值|频变网络等值]]
- [[戴维南-诺顿等值|戴维南/诺顿等值]]
- [[最小二乘曲线拟合|最小二乘曲线拟合]]
- [[基波相量提取|基波相量提取]]
- [[时间步协调|时间步协调]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[facts|FACTS]]
- [[tcsc|TCSC]]
- [[外部交流电网|外部交流电网]]
- [[频变等值模型|频变等值模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[暂态稳定仿真|暂态稳定仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[交直流相互作用|交直流相互作用]]


## 主要发现


- 频变等值模型有效抑制接口波形畸变，实现外部电网宽频响应的精确映射
- 交互策略成功协调双程序时间步，HVDC与TCSC算例验证了方法有效性
- 相量提取算法保障多接口数据交互精度，消除传统准稳态模型的简化误差


