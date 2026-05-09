---
title: "大规模电力系统 (Large-Scale Power System)"
type: topic
tags: [large-scale, power-system, simulation, parallel-computing, network-equivalent]
created: "2026-05-02"
---

# 大规模电力系统 (Large-Scale Power System)


```mermaid
graph TD
    N0[大规模电力系统 (Large-S…]
    N1[技术背景]
    N0 --> N1
    N2[定义与边界]
    N0 --> N2
    N3[EMT 中的作用]
    N0 --> N3
    N4[主要分支与机制]
    N0 --> N4
    N5[适用边界与失败模式]
    N0 --> N5
    N6[代表性来源]
    N0 --> N6
    N7[与相关页面的关系]
    N0 --> N7
    N8[开放问题]
    N0 --> N8
```


## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

大规模电力系统指包含多区域交流网络、发电与负荷群、HVDC、FACTS、新能源电站、保护控制系统和通信/调度层的互联系统。其“大规模”来自拓扑规模、模型细节、时间尺度、设备异质性和控制保护逻辑的共同作用，而不是某个固定母线数量。

本页定义 EMT 知识网络中的对象边界。[[large-scale-grid-simulation]] 讨论如何仿真该对象，[[large-scale-hybrid-acdc-simulation]] 讨论其中交直流混联场景，[[fast-system-simulation]] 讨论使仿真更快的计算路线。

## EMT 中的作用

在大规模电力系统中，EMT 的价值在于局部高频和非线性现象会影响系统级结论：

- 多馈入 LCC-HVDC 的换相失败、恢复和直流功率转移。
- VSC、MMC、风电、光伏和储能控制在弱网或故障中的快速相互作用。
- 频率相关线路、电缆、接地和变压器饱和对暂态电压电流的影响。
- 保护动作、控制限幅、通信延迟和 HIL 设备对系统动态的闭环影响。

## 主要分支与机制

### 结构层级

大规模系统可按区域、设备层级和时间尺度描述：

$$
\mathcal{S}=(\mathcal{N},\mathcal{E},\mathcal{D},\mathcal{C}),
$$

其中 $\mathcal{N}$ 是母线和端口集合，$\mathcal{E}$ 是线路、变压器和开关支路，$\mathcal{D}$ 是发电机、换流器、负荷、滤波器和保护设备，$\mathcal{C}$ 是控制、通信和运行策略。EMT 模型需要说明哪些集合被详细建模，哪些被等值或聚合。

### 运行与规划对象

同一系统在不同任务中边界不同。规划研究可能关注外部网络强度和新能源接入容量；保护研究关注故障电流、测量链和动作时序；实时 HIL 关注控制硬件接口和 deadline；运行预演关注可重复工况和调度设定。页面结论应把对象、任务和验证指标绑定。

### 等值、聚合与保真度

大规模系统通常需要[[network-equivalent]]、[[model-order-reduction]]、[[dynamic-phasor]]、[[average-value-model]] 或 [[fdne-model]]。这些方法改变的是系统表示，不是物理系统本身。等值后应报告保留端口、频带、扰动类型、控制状态和对照基准。

### 分区与计算边界

若把系统划分为区域 $\mathcal{S}_1,\ldots,\mathcal{S}_m$，接口变量可写为

$$
z_{ij} = [v_{ij},\, i_{ij},\, p_{ij},\, q_{ij}]^\mathsf{T}.
$$

其中 $v_{ij}$ 和 $i_{ij}$ 是区域间端口电压、电流，$p_{ij},q_{ij}$ 是功率或相量域变量。[[network-partitioning]] 和 [[interface-technique]] 决定这些变量如何交换、同步和验证。

## 适用边界与失败模式

- 不能把一个工程系统的节点数、容量、仿真步长或实时平台配置写成大规模电力系统的一般定义。
- 等值外部系统可能保留潮流和短路容量，却丢失低频振荡、宽频谐振、控制限幅或保护动作。
- 大规模系统的参数、控制逻辑和保护定值常来自不同来源；版本不一致会导致看似数值问题的模型错误。
- 多区域耦合、低阻抗接口和快速控制闭环会放大分区延迟与插值误差。
- 输出数据量、故障集和长时段仿真可能成为验证瓶颈；只保存少量波形会限制事后审计。


### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s
- 电压等级：10kV ~ 500kV
- 功率范围：1MW ~ 1000MW
- 频率范围：50Hz / 60Hz

## 代表性来源

- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：支撑多馈入 HVDC 工程系统的“对象复杂度”来自遗留控制、硬件副本、直流线路、交流等值和逐级集成。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]]：支撑大规模系统模型迁移时，模型兼容、控制建模差异和实时约束会影响结论。
- [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn]]：支撑大规模对象进入离线并行 EMT 后，通信架构和应用级指标决定计算可扩展性。
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]：支撑大型 AC 与 MMC-MTDC 系统可按动态特性划分为快慢子系统。
- [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]]：支撑大系统实时化需要把电网任务和处理器拓扑共同建模。

## 与相关页面的关系

- [[large-scale-grid-simulation]]：从仿真任务角度组织大规模系统。
- [[large-scale-hybrid-acdc-simulation]]：聚焦大系统中的 AC/DC、HVDC、VSC 和 MMC 耦合。
- [[dispatch-operation]]：提供运行点、调度设定和工况来源。
- [[network-equivalent]] 与 [[fdne-model]]：解释外部系统和频率相关端口等值。
- [[hil-simulation]]：把大规模系统模型接入真实控制保护硬件时的边界。

## 开放问题

- 如何定义可跨论文比较的“大规模”描述字段，而不仅是母线数或元件数。
- 如何在保密工程模型中公开足够的拓扑、控制、参数和验证证据。
- 如何在系统级结论中区分物理现象、模型简化误差、接口误差和计算平台限制。
