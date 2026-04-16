---
title: "Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Prediction"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Electronics;2022;37;10;10.1109/TPEL.2022.3176687"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Gao 等 - 2022 - Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Predic.pdf"]
---

# Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Prediction

**作者**: 
**年份**: 2022
**来源**: `19、20、21/EMT_task_19/Gao 等 - 2022 - Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Predic.pdf`

## 摘要

— Voltage source converter (VSC) is fundamental and critical in renewable energy integration and transmission and has become ubiquitous in power systems. For the design and operation of power systems with VSCs, electromagnetic transient (EMT) simulation is indispensable. However, a large number of VSCs in power systems cause a high time-consuming issue in EMT sim- ulation. This article proposes a fast EMT simulation model for VSCs with arbitrary topology based on switch-state prediction. The accurate switch-state prediction has two steps: Preliminary switch- state prediction and simultaneous switching prediction. It avoids the iterative computation required to obtain a feasible switch-state combination in the traditional EMT simulators. Extensive tests on different types of VSCs and a dc m

## 核心贡献


- 提出基于开关状态预测的VSC快速EMT模型，将复杂拓扑分解为半桥单元独立判断
- 构建半桥开关状态有限状态机，通过初步与同时开关预测避免全网迭代计算
- 实现任意拓扑VSC详细电磁暂态仿真加速，在保持精度的同时显著提升效率


## 使用的方法


- [[开关状态预测|开关状态预测]]
- [[有限状态机|有限状态机]]
- [[节点分析法|节点分析法]]
- [[两步预测法|两步预测法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[半桥变换器-hbc|半桥变换器(HBC)]]
- [[两电平变换器|两电平变换器]]
- [[三电平npc变换器|三电平NPC变换器]]
- [[三电平t型变换器|三电平T型变换器]]
- [[直流微电网|直流微电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子建模|电力电子建模]]
- [[仿真加速|仿真加速]]
- [[开关状态预测|开关状态预测]]
- [[新能源并网系统|新能源并网系统]]


## 主要发现


- 在多种VSC及直流微电网测试中，模型在保持详细仿真精度的同时显著提升计算速度
- 开关状态预测法有效避免了传统EMT仿真中的全网迭代计算，大幅降低单步耗时
- 半桥单元独立状态判断策略成功适用于任意拓扑VSC，验证了方法的通用性


