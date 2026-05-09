---
title: "电力电子变压器方法入口 (PET)"
type: method
tags: [pet, power-electronic-transformer, sst, energy-router, isolated-converter]
created: "2026-05-04"
updated: "2026-05-07"
---

# 电力电子变压器方法入口 (PET)

## 定义与边界

PET（Power Electronic Transformer）通常指通过多级电力电子变换和高频隔离链实现电压变换、功率调节和多端口能量路由的设备与建模方法入口。它常与 SST、能源路由器和柔性变电场景相关。

本页讨论的是 PET 的系统级建模和 EMT 入口边界，不把输电线路相域模型、无关 PLL 设计或任意开关等效方法误写成 PET 方法本身。

## EMT 中的作用

在 EMT 仿真中，PET 方法主要用于：

- 组织多级功率模块、高频隔离链和外端口接口的系统级模型；
- 比较详细模型、平均值模型、等效模型和多速率模型的边界；
- 研究 PET 在柔性配电网、交直流混合配网和新能源接入中的动态作用；
- 为实时仿真和提速建模提供设备级背景。

## 常见分支

- CHB-DAB 型 PET：常见于级联 H 桥与 DAB 组合场景。
- MAB/PM 聚合型 PET：强调多端口和高频链直接功率传输。
- 高速等效/多速率 PET：强调端口等效、并行求解和多级频率分区。
- 平均值或简化 EMT PET：强调系统级速度与端口行为保留。

## 形式化表达

对 PET 的系统级最小抽象，可把其看作多端口功率变换接口：

$$
\sum P_{in} - P_{loss} = \sum P_{out}
$$

其 EMT 难点通常不在静态功率平衡，而在于高频链、多模块连接方式以及内部节点如何被端口等效或分层处理。

## 与相关页面的关系

- [[dual-active-bridge]]：DAB 是 PET 的常见中间级功率模块。
- [[m3c]]：说明特殊多端口换流器与普通 PET 的边界。
- [[n-port-network]]：PET 高阶端口等效的相关背景。
- [[real-time-simulation]]：PET 常是 EMT 提速和实时验证的重要对象。
- [[offshore-wind-integration]]：PET 可能作为新能源接入和能量路由设备背景。

## 代表性来源

- [[高频隔离型电力电子变压器电磁暂态加速仿真方法与展望]]：PET EMT 提速建模框架背景。
- [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie]]：CHB-PET 并行等效建模背景。
- [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi]]：PET 多速率 EMT 建模背景。

## 证据边界

本页不写无来源的效率、容量、节点数优势或统一拓扑结论。具体能力必须绑定 PET 结构、模块类型和验证工况。

## 开放问题

- 当前页尚未系统拆分 CHB-DAB、MAB 和其他高频隔离 PET 分支之间的模型边界。
- PET 入口后续是否应提升为 topic 级页面，仍需看相邻方法页和场景页的收敛情况。
