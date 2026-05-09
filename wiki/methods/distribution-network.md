---
title: "Distribution Network"
type: method
tags: [distribution-network]
created: "2026-05-04"
---

# Distribution Network

## 定义与边界

本页是配电网相关链接的受控入口。配电网作为系统对象时，应优先归入 [[microgrid-distribution-network]] 或 [[power-system-network]]；涉及配电网中雷电感应、电能质量、分布式电源接入或保护配合的 EMT 算例时，再从本页转到对应专题。

## 概念边界

- 不是新的线路模型或网络方程页面；线路、电缆和网络求解应分别连接 [[transmission-line-modeling]]、[[distribution-test-feeders]] 或 [[power-system-network]]。
- 不是配电自动化、调度或规划综述页；慢时间尺度问题不应被写成 EMT 方法。
- 若研究对象是“配电网中的雷电感应电压”，应连接 [[lightning-overvoltage]]、[[high-frequency-transient-analysis]] 和具体 source 页。

## 核心机制

配电网 EMT 仿真的核心在于求解三相不平衡系统的网络方程。对于含 $n$ 个节点的配电网，其节点电压方程可写为：

$$
\mathbf{Y}_{	ext{bus}} \mathbf{V}_{	ext{bus}} = \mathbf{I}_{	ext{bus}}
$$

其中 $\mathbf{Y}_{	ext{bus}}$ 为三相节点导纳矩阵，考虑了线路耦合、变压器联结组别和中性点接地方式。配电网的特点是 $R/X$ 比值高、三相不平衡、分布式电源接入点多，导致 $\mathbf{Y}_{	ext{bus}}$ 的条件数较大，求解时可能需要采用前推回推或改进节点法。

## 链接用法

- 从中文或英文“配电网 / distribution network”锚文本进入本页时，用作消歧入口。
- 系统对象和微电网/配电网建模：转至 [[microgrid-distribution-network]]。
- EMT 网络边界和等值：转至 [[power-system-network]]。
- 配电网雷击感应电压算例：转至 [[lightning-overvoltage]] 或 [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]]。

## 代表性来源

- [[an-fpga-based-electromagnetic-transient-analysis-of-power-distribution-network]]
- [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]]

## 证据边界

本页只保留术语入口和路由关系，不给出固定节点规模、步长、误差百分比或实时性能结论。配电网 EMT 结论必须绑定具体拓扑、线路参数、分布式电源模型、接地条件、仿真工具和验证指标。
