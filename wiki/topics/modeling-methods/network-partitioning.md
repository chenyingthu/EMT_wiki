---
title: "网络分区 (Network Partitioning)"
type: topic
tags: [network-partitioning, decomposition, parallel, co-simulation, latency, domain-decomposition, schur-complement]
created: "2026-05-02"
---

# 网络分区 (Network Partitioning)


```mermaid
graph TD
    N0[网络分区 (Network Pa…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[主要分支与机制]
    N0 --> N3
    N4[适用边界与失败模式]
    N0 --> N4
    N5[代表性来源]
    N0 --> N5
    N6[与相关页面的关系]
    N0 --> N6
    N7[开放问题]
    N0 --> N7
```


## 定义与边界

网络分区是在电力系统拓扑、设备模型或计算任务上选择边界，把一个 EMT 问题拆成多个子系统求解的技术。它服务于并行计算、多速率仿真、实时任务分配、混合仿真和局部详细建模。

本页讨论分区作为主题的边界：它不是单一算法，也不等同于一定加速或一定稳定。具体接口方程见[[interface-technique]]和[[direct-interface-technique]]；多步长耦合见[[multirate-method]]；分区后的计算实现见[[parallel-computing]]和[[multithreaded-parallel-computing]]。

## EMT 中的作用

EMT 的小步长和稀疏网络求解使分区具有两类价值：

- 计算价值：降低单个矩阵维度、并行元件更新、把任务映射到多核、多机或 FPGA 资源。
- 建模价值：把研究区域保留详细 EMT，把外部系统等值、降阶或放到相量域。

分区也引入新问题：边界电压电流是否连续、接口延迟是否可接受、快慢步长是否稳定、故障和保护事件是否在两侧同步。

## 主要分支与机制

### 图分区与负载均衡

把电网表示为图 $G=(V,E)$ 后，可将节点集合划分为 $V_1,\ldots,V_P$。常见目标是同时控制割边和负载：

$$
\min \sum_{(i,j)\in E_{\mathrm{cut}}} w_{ij},\qquad
\left|L_p-\bar L\right|\le \epsilon \bar L.
$$

其中 $w_{ij}$ 是边权重，$L_p$ 是分区 $p$ 的计算负载，$\bar L$ 是平均负载，$\epsilon$ 是允许不平衡率。[[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]] 说明实时 EMT 中还需要把源图任务映射到目标处理器图，通信强的任务应靠近放置。

### 电气距离与物理边界

电气距离、弱联络线、长传输线、变压器、直流接口和区域边界常被用作候选分区位置。长线路可用传播延迟自然解耦；低阻抗短连接和强控制闭环通常不是安全边界。分区选择应说明是为了物理解释、计算负载、接口稳定性，还是为了工具或实时平台限制。

### Schur 补与等效接口

对线性化网络方程

$$
\begin{bmatrix}
Y_{aa} & Y_{ab}\\
Y_{ba} & Y_{bb}
\end{bmatrix}
\begin{bmatrix}
v_a\\v_b
\end{bmatrix}
=
\begin{bmatrix}
i_a\\i_b
\end{bmatrix},
$$

消去外部节点可得端口等值

$$
Y_{\mathrm{eq}}=Y_{aa}-Y_{ab}Y_{bb}^{-1}Y_{ba}.
$$

该式解释了 [[network-equivalent]]、Thevenin/Norton 接口和多端口等值的关系。频率相关外部网络还需要 [[fdne-model]]、[[vector-fitting]] 和 [[passivity-enforcement]] 控制时域实现稳定性。

### 延迟、多速率与小步综合

传输线延迟、离散电感、电容或人工延迟可用于解耦当前步方程，但会改变接口动态。多速率分区中，快区步长 $h_f$ 与慢区步长 $h_s=N h_f$ 需要插值、保持、平均或迭代校正。[[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e]] 代表了把分区接口储能支路内部用小步长综合以改善稳定边界的路线；其数值结论应限于原文验证系统和参数。

## 适用边界与失败模式

- 最小割并不等于最佳 EMT 分区；强电气耦合、控制闭环和事件同步可能比割边数量更重要。
- 只按节点数均衡可能忽略 MMC 子模块、开关频率、控制器复杂度和非线性迭代成本。
- 显式接口、人工延迟和零阶保持可能在弱阻尼系统中注入虚假能量。
- 分区改变矩阵结构后，稀疏求解器重排序、填充和通信成本可能抵消理论收益。
- 频率相关或多端口等值若未检查无源性，可能在时域 EMT 中引入不稳定极点。
- 实时平台中的分区还受最坏步长、I/O 拓扑和处理器互连限制。

## 代表性来源

- [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]]：支撑任务分离、图划分、负载均衡和处理器拓扑映射。
- [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn]]：支撑分区后通信结构会影响离线 MPI EMT 扩展性。
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]：支撑按 AC/MMC-MTDC 动态时间尺度分区，并用时变等效与预测校正处理接口。
- [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e]]：支撑储能支路分区稳定性和小步综合模型讨论；不能外推为所有拓扑均稳定。
- [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized]] 与 [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat]] 可作为换流器或模块化系统分区解耦的入口。

## 与相关页面的关系

- [[interface-technique]]：定义分区之间交换什么变量以及如何同步。
- [[direct-interface-technique]]：讨论强耦合或矩阵层面的直接接口。
- [[multirate-and-network-partitioning]]：专门讨论分区和多速率结合。
- [[large-scale-grid-simulation]]：使用分区作为大电网可计算性的手段。
- [[fast-system-simulation]]：把分区作为加速路线之一，但不把分区等同于加速。
- [[sparse-matrix-techniques]] 和 [[nodal-admittance-matrix]]：解释分区如何改变矩阵结构和求解成本。

## 开放问题

- 如何把拓扑割边、计算负载、接口稳定性、事件同步和硬件通信拓扑合成一个可审核分区指标。
- 如何在分区后自动检测哪些故障、开关或保护动作需要临时细化边界或切回统一求解。
- 如何为分区接口建立公开 benchmark，报告功率误差、波形误差、收敛、通信和 deadline 证据。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |