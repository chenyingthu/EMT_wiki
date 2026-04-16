---
title: "Real-time digital simulator of the electromagnetic transients of power transmission lines - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['real-time', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/32/61.25614.pdf.pdf"]
---

# Real-time digital simulator of the electromagnetic transients of power transmission lines - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `32/61.25614.pdf.pdf`

## 摘要

This paper presents the theory and results of a new real-time digital simulator of transmission lines. The simulator is based on time domain formulation. It obtains the electromagnetic transient performance of balanced three-phase lines in real-time. Sample results of energizing a transmission line from balanced and unbalanced sources are presented. The real-time digital simulator results are verified for accuracy by simulating the same system , off line, on EMTP program. The newly developed real-time digital simulator can readily be incorporated into modern TNA and hvdc simulators. Their application , in place of large number of n or r sections of pas- sive networks, is economical, space saving and accurate. As well the realization of real-time digital simulators of transmission lines sig

## 核心贡献


- 提出基于时域与贝杰龙法的输电线路实时数字仿真器，替代传统TNA中大量无源Π/Γ节。
- 采用相模变换解耦多相线路方程，支持多处理器并行计算，显著提升实时仿真效率。
- 结合集中电阻近似与梯形积分法，实现有损分布参数线路的高精度离散时间域实时求解。


## 使用的方法


- [[时域公式化|时域公式化]]
- [[贝杰龙模型|贝杰龙模型]]
- [[相模变换|相模变换]]
- [[集中电阻近似|集中电阻近似]]
- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[平衡三相线路|平衡三相线路]]
- [[分布参数线路|分布参数线路]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电磁暂态|电磁暂态]]
- [[输电线路建模|输电线路建模]]
- [[并行计算|并行计算]]
- [[数字仿真器|数字仿真器]]


## 主要发现


- 仿真结果与离线EMTP对比验证，在平衡与非平衡电源激励下均保持高精度。
- 该模型可无缝集成至现代TNA与HVDC仿真器，大幅节省硬件空间并降低成本。
- 模态解耦架构使三相线路电磁暂态计算满足实时性要求，验证了全数字仿真的可行性。


