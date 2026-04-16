---
title: "Modeling Synchronous Voltage Source Converters in Transmission System Planning Studies - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modeling synchronous voltage source converters in transmission system planning studies.pdf"]
---

# Modeling Synchronous Voltage Source Converters in Transmission System Planning Studies - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Modeling synchronous voltage source converters in transmission system planning studies.pdf`

## 摘要

A Voltage Source Converter (VSC) can be benefi- cial to power utilities in many ways [I, 2, 3, 41. To evaluate the VSC performance in potential applications, the device has to be represented appropriately in planning studies. This pa- per addresses VSC modeling for EMTP, powerflow, and tran- sient stability studies. First, the VSC operating principles are overviewed, and the device model for EMTP studies is pre- sented. The ratings of VSC components are discussed, and the device operating characteristics are derived based on these ratings. A powerflow model is presented and various control modes are proposed. A detailed stability model is developed, and its step-by-step initialization procedure is described. A simplified stability model is also derived under stated assump- tions. Finally, 

## 核心贡献


- 提出适用于EMTP、潮流和暂态稳定研究的VSC综合建模方法
- 推导VSC详细与简化暂态稳定模型，并给出逐步初始化流程
- 建立基于零停驻角与功率角的双自由度电压幅相控制策略


## 使用的方法


- [[emtp仿真-bpa-atp|EMTP仿真(BPA-ATP)]]
- [[tacs受控开关建模|TACS受控开关建模]]
- [[atp-models控制语言|ATP-Models控制语言]]
- [[基频等效电路法|基频等效电路法]]
- [[多脉冲谐波抵消技术|多脉冲谐波抵消技术]]
- [[逐步初始化算法|逐步初始化算法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[statcon-静止同步补偿器|Statcon(静止同步补偿器)]]
- [[bes-电池储能系统|BES(电池储能系统)]]
- [[gto晶闸管阀|GTO晶闸管阀]]
- [[耦合变压器阵列|耦合变压器阵列]]
- [[直流侧电容-电池|直流侧电容/电池]]


## 相关主题


- [[输电系统规划|输电系统规划]]
- [[无功补偿|无功补偿]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[潮流计算|潮流计算]]
- [[vsc-model|VSC]]
- [[谐波抑制|谐波抑制]]


## 主要发现


- 详细与简化稳定模型在暂态响应上与EMTP仿真结果高度吻合
- 通过调节功率角与零停驻角可实现有功无功的独立快速控制
- 多脉冲耦合变压器阵列有效消除了17次以下特征谐波


