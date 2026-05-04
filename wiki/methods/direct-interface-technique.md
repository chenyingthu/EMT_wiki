---
title: "直接接口技术 (Direct Interface Technique)"
type: method
tags: [direct-interface, tearing, schur, coupling, subnetwork]
created: "2026-05-02"
---

# 直接接口技术 (Direct Interface Technique)

## 定义与边界

直接接口技术是在同一 EMT 网络方程或强耦合分区方程中显式求解边界变量的方法。它通常把系统按接口端口撕裂，消去各子网内部未知量，再求一个由边界电压或边界电流组成的缩减问题。其目标不是把一侧长期替换为粗略外部等值，而是在每个 EMT 时间步内保持接口处的 Kirchhoff 约束和伴随电路历史项一致。

本页讨论的是强耦合、矩阵型的直接接口。更宽泛的电压源、Norton 源、功率接口、多速率保持和工具协同数据交换属于 [[interface-technique]]；把 EMT 区域与机电暂态区域连接起来的应用场景属于 [[electromechanical-electromagnetic-hybrid-simulation]]。

## EMT 中的作用

在 EMT 中，开关、电感、电容、线路和控制接口经过离散化后形成每步更新的代数网络方程。直接接口技术的作用是把大网络拆成多个可并行求解的子网，同时避免接口变量只靠上一时刻外推。典型用途包括：

- 分网并行 EMT：各子网独立组装内部导纳矩阵，接口方程负责统一边界电压或电流。
- 实时仿真分区：在固定步长内预计算可复用矩阵，降低接口迭代次数的不确定性。
- 多端口设备或外部网络连接：保留端口间耦合，避免把多端口关系误降为互不相关的单端口源。
- 与 [[network-partitioning]]、[[nodal-analysis]] 和 [[companion-circuit]] 配合，控制分区后的矩阵规模和更新时间。

## 核心方程

设一个子网的 EMT 伴随电路在当前时间步写成节点方程：

$$
\begin{bmatrix}
Y_{ii} & Y_{ib} \\
Y_{bi} & Y_{bb}
\end{bmatrix}
\begin{bmatrix}
v_i \\
v_b
\end{bmatrix}
=
\begin{bmatrix}
j_i \\
j_b
\end{bmatrix}
$$

其中 $v_i$ 是内部节点电压，$v_b$ 是接口端口电压，$Y$ 包含当前拓扑和离散伴随导纳，$j$ 包含源项、历史项和控制注入。若 $Y_{ii}$ 可逆，可消去内部变量：

$$
v_i = Y_{ii}^{-1}(j_i - Y_{ib}v_b)
$$

代入边界方程得到子网对接口的 Schur 补：

$$
(Y_{bb} - Y_{bi}Y_{ii}^{-1}Y_{ib})v_b
= j_b - Y_{bi}Y_{ii}^{-1}j_i
$$

对多个子网，把各子网的接口导纳贡献和等效注入叠加，再施加边界电流守恒：

$$
\left(\sum_k S_k\right)v_b = \sum_k r_k
$$

其中 $S_k = Y_{bb}^{(k)} - Y_{bi}^{(k)}(Y_{ii}^{(k)})^{-1}Y_{ib}^{(k)}$，$r_k = j_b^{(k)} - Y_{bi}^{(k)}(Y_{ii}^{(k)})^{-1}j_i^{(k)}$。求得 $v_b$ 后，各子网回代更新内部节点电压和支路历史量。

## 工作流程

1. 选择接口端口，使端口数远小于内部节点数，并避免把强耦合设备随意切开。
2. 每个子网组装当前步的内部矩阵、边界耦合矩阵和历史注入。
3. 对每个子网因式分解 $Y_{ii}$，形成接口 Schur 补贡献和右端项。
4. 汇总并求解接口方程，得到边界电压或边界电流。
5. 各子网回代内部状态，更新开关状态、伴随历史源和测量量。
6. 若开关事件改变拓扑或离散参数，重建受影响子网的分解和接口贡献。

## 主要变体

- 节点撕裂：接口变量为共享节点电压，适合节点电压法 EMT 网络。
- 支路撕裂：接口变量为联络支路电流或支路电压，适合把线路、变压器或多端元件作为连接对象。
- 电感/传输线解耦接口：利用离散电感或行波延迟把接口变成显式历史项；这可降低强耦合成本，但本质上引入步长或传播延迟假设。
- 多端口 Schur 接口：保留端口矩阵 $S_k$ 的非对角项，用于强耦合多端口外部网络或多回线路。
- 实时预计算接口：当拓扑和步长固定时预先缓存因式分解；当开关状态频繁改变时需要局部重构策略。

## 适用边界与失败模式

- 接口矩阵可能稠密。端口数过多时，Schur 补求解会成为瓶颈。
- $Y_{ii}$ 病态、孤岛化或包含理想源冲突时，消元可能失败或放大误差。
- 开关拓扑高频变化会削弱预计算收益，并可能造成接口矩阵频繁重建。
- 直接接口并不自动保证物理正确性。若分区位置切断控制闭环、保护逻辑或强非线性设备，仍需做全模型或测量基准对比。
- 与松耦合接口相比，它减少了接口外推误差，但增加同步、矩阵通信和实现复杂度。

## 代表性证据与证据边界

直接接口的数学等价性只在离散网络方程、接口变量和拓扑状态一致时成立。若论文只在特定平台、特定分区或特定实时硬件上报告加速或稳定性，不能外推为所有 EMT 网络都更快或更稳定。与 [[co-simulation]]、[[real-time-simulation]] 或 [[hardware-acceleration]] 相关的性能结论应绑定具体步长、端口数、设备模型和通信机制。

可作为证据入口的来源包括 [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic]]、[[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne]] 和 [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre]]。这些来源支持“接口一致性、补偿和多速率并行是 EMT 分区仿真的关键问题”，但不支撑无条件的精度或实时性断言。

## 与相关页面的关系

- [[interface-technique]]：接口方法总览，覆盖直接接口、等值源接口、功率接口和松耦合数据交换。
- [[hybrid-modeling]]：说明不同详细程度和不同物理域模型如何组合。
- [[electromechanical-electromagnetic-hybrid-simulation]]：说明机电暂态与 EMT 的相量/瞬时值接口。
- [[compensation-method]]：讨论分区或等值误差通过补偿源修正的路线。
- [[network-partitioning]]：讨论接口位置和分区粒度选择。
- [[nodal-analysis]]：提供直接接口所依赖的节点方程背景。
