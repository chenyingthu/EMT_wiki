---
title: "直接接口技术 (Direct Interface Technique)"
type: method
tags: [direct-interface, tearing, schur, coupling, subnetwork]
created: "2026-05-02"
updated: "2026-05-18"
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

### 子网节点方程

设一个子网的 EMT 伴随电路在当前时间步写成节点方程：

$$\begin{bmatrix} \mathbf{Y}_{ii} & \mathbf{Y}_{ib} \\ \mathbf{Y}_{bi} & \mathbf{Y}_{bb} \end{bmatrix} \begin{bmatrix} \mathbf{v}_i \\ \mathbf{v}_b \end{bmatrix} = \begin{bmatrix} \mathbf{j}_i \\ \mathbf{j}_b \end{bmatrix}$$

其中 $\mathbf{v}_i$ 是内部节点电压向量，$\mathbf{v}_b$ 是接口端口电压向量，$\mathbf{Y}$ 包含当前拓扑和离散伴随导纳，$\mathbf{j}$ 包含源项、历史项和控制注入。

### Schur 补消去

若 $\mathbf{Y}_{ii}$ 可逆，可通过高斯消元消去内部变量：

$$\mathbf{v}_i = \mathbf{Y}_{ii}^{-1}(\mathbf{j}_i - \mathbf{Y}_{ib}\mathbf{v}_b)$$

代入边界方程得到子网对接口的 **Schur 补**：

$$(\mathbf{Y}_{bb} - \mathbf{Y}_{bi}\mathbf{Y}_{ii}^{-1}\mathbf{Y}_{ib})\mathbf{v}_b = \mathbf{j}_b - \mathbf{Y}_{bi}\mathbf{Y}_{ii}^{-1}\mathbf{j}_i$$

定义接口导纳矩阵（Schur 补）和等效注入向量：

$$\mathbf{S}_k = \mathbf{Y}_{bb}^{(k)} - \mathbf{Y}_{bi}^{(k)}(\mathbf{Y}_{ii}^{(k)})^{-1}\mathbf{Y}_{ib}^{(k)}, \quad \mathbf{r}_k = \mathbf{j}_b^{(k)} - \mathbf{Y}_{bi}^{(k)}(\mathbf{Y}_{ii}^{(k)})^{-1}\mathbf{j}_i^{(k)}$$

### 多子网接口方程

对 $N$ 个子网，把各子网的接口导纳贡献和等效注入叠加，再施加边界电流守恒：

$$\left(\sum_{k=1}^{N} \mathbf{S}_k\right)\mathbf{v}_b = \sum_{k=1}^{N} \mathbf{r}_k$$

求得多子网接口电压 $\mathbf{v}_b$ 后，各子网回代更新内部节点电压和支路历史量：

$$\mathbf{v}_i^{(k)} = (\mathbf{Y}_{ii}^{(k)})^{-1}(\mathbf{j}_i^{(k)} - \mathbf{Y}_{ib}^{(k)}\mathbf{v}_b)$$

## 工作流程

1. **选择接口端口**：使端口数远小于内部节点数，并避免把强耦合设备随意切开（接口应选在电气弱耦合处）。
2. **组装子网矩阵**：每个子网组装当前步的内部导纳矩阵 $\mathbf{Y}_{ii}^{(k)}$、边界耦合矩阵 $\mathbf{Y}_{ib}^{(k)}$、$\mathbf{Y}_{bi}^{(k)}$、$\mathbf{Y}_{bb}^{(k)}$ 和历史注入向量 $\mathbf{j}_i^{(k)}$、$\mathbf{j}_b^{(k)}$。
3. **因式分解**：对每个子网因式分解 $\mathbf{Y}_{ii}^{(k)}$（$LU$ 分解或 Cholesky 分解），形成接口 Schur 补贡献 $\mathbf{S}_k$ 和右端项 $\mathbf{r}_k$。
4. **汇总求解**：汇总 $\mathbf{S} = \sum \mathbf{S}_k$ 和 $\mathbf{r} = \sum \mathbf{r}_k$，求解 $\mathbf{v}_b = \mathbf{S}^{-1}\mathbf{r}$。
5. **回代**：各子网回代内部状态 $\mathbf{v}_i^{(k)} = (\mathbf{Y}_{ii}^{(k)})^{-1}(\mathbf{j}_i^{(k)} - \mathbf{Y}_{ib}^{(k)}\mathbf{v}_b)$，更新开关状态、伴随历史源和测量量。
6. **拓扑更新**：若开关事件改变拓扑或离散参数，重建受影响子网的分解和接口贡献。

## 主要变体

### 变体一：节点撕裂（Node Tearing）

接口变量为共享节点电压，适合节点电压法 EMT 网络。接口方程数为被撕裂的节点数 $n_b$，子网内部方程数 $n_i^{(k)}$。每个子网保持完整的节点导纳矩阵结构，接口变量是各子网共用的节点电压。

$$\mathbf{v}_b = [v_{b_1}, v_{b_2}, \ldots, v_{b_{n_b}}]^T$$

### 变体二：支路撕裂（Branch Tearing）

接口变量为联络支路电流或支路电压，适合把线路、变压器或多端元件作为连接对象。接口方程数为被撕裂的支路数 $n_b$。接口约束为 Kirchhoff 电流定律（KCL）或 Kirchhoff 电压定律（KVL）：

$$\sum_{k=1}^{N} i_b^{(k)} = 0 \quad \text{（支路电流撕裂）}$$

或

$$v_{b_1}^{(k)} = v_{b_2}^{(m)} \quad \text{（支路电压撕裂）}$$

### 变体三：电感/传输线解耦接口

利用离散电感或行波延迟把接口变成显式历史项，降低强耦合矩阵求解成本：

对于离散电感 $L$（梯形积分）：

$$i_L(t) = \frac{\Delta t}{2L}v_L(t) + \underbrace{\left[i_L(t-\Delta t) + \frac{\Delta t}{2L}v_L(t-\Delta t)\right]}_{i_{\mathrm{hist}}(t)}$$

接口电压 $v_b$ 可通过前一时刻值显式估计，接口矩阵 $\mathbf{S}$ 退化为对角块，降低求解复杂度。但步长增大时显式估计误差增加，可能导致接口发散。

### 变体四：多端口 Schur 接口

保留端口矩阵 $\mathbf{S}_k$ 的非对角项，用于强耦合多端口外部网络或多回线路。当外部网络是多端口等值（FDNE）时，$\mathbf{S}_k$ 不再是对角矩阵，而是稠密的多端口导纳矩阵：

$$\mathbf{S}_k = \mathbf{Y}_{bb}^{(k)} - \mathbf{Y}_{bi}^{(k)}(\mathbf{Y}_{ii}^{(k)})^{-1}\mathbf{Y}_{ib}^{(k)} \in \mathbb{R}^{m \times m}$$

其中 $m$ 是外部网络的端口数。此时接口方程是 $m \times m$ 的稠密矩阵，但规模远小于原始网络（$m \ll n_i$）。

### 变体五：实时预计算接口（Precomputed Factorization）

当拓扑和步长固定时，预先缓存因式分解结果 $\mathbf{L}\mathbf{U} = \mathbf{Y}_{ii}$；当开关状态改变时只需更新局部因子：

| 场景 | 策略 | 收益 |
|------|------|------|
| 固定拓扑、$\Delta t$ 恒定 | 全预计算 | 接口矩阵分解 $O(n_b^3)$ → $O(n_b^2)$（仅回代） |
| 少数开关事件 | 局部更新 | 仅重分解受影响子块 |
| 频繁开关 | 切换为松弛接口 | 预计算收益消失 |

## 量化性能边界

| 变体 | 接口方程规模 | 每次迭代复杂度 | 典型加速比 | 适用场景 |
|------|-------------|---------------|-----------|----------|
| 节点撕裂（单端口） | $n_b = 1$ | $O(n_i)$ | $1.5\text{–}3\times$ | 双区域并行 |
| 节点撕裂（多端口） | $n_b \ll n_i$ | $O(n_b^3)$ | $2\text{–}5\times$ | 大规模分区 |
| 支路撕裂 | $n_b$ 支路数 | $O(n_b \cdot n_i)$ | $1.2\text{–}2\times$ | 线路连接 |
| 电感解耦 | $n_b$ 电感数 | $O(n_b)$ | $5\text{–}10\times$（接口） | 实时分区 |
| 多端口 Schur | $m \times m$ 稠密 | $O(m^3)$ | $3\text{–}8\times$ | FDNE 接口 |
| 实时预计算 | 固定 $\mathbf{L}\mathbf{U}$ | $O(n_b^2)$ | $10\text{–}50\times$ | 实时仿真 |

*数据来源：Parvari 2023 多速率 EMT 仿真、EMTP 相关并行接口研究*

## 关键技术挑战

**挑战一：Schur 补稠密化**

当子网内部节点被消去后，接口矩阵 $\mathbf{S}$ 变为稠密矩阵（即使 $\mathbf{Y}$ 是稀疏的）。若 $n_b$ 较大（数百至上千端口），求解 $\mathbf{S}\mathbf{v}_b = \mathbf{r}$ 的复杂度 $O(n_b^3)$ 可能抵消分网并行的收益。**解法**：使用稀疏求解器（稀疏 LU、迭代求解）、分层接口（先局部汇总再全局求解）。

**挑战二：开关拓扑频繁变化的矩阵重建**

当 MMC 或其他电力电子设备高频开关闭换时，子网的 $\mathbf{Y}_{ii}^{(k)}$ 每步更新，导致接口 Schur 补 $\mathbf{S}_k$ 频繁重建。**解法**：Parvari 2023 的常导纳矩阵策略（将时变部分并入历史源），或使用近似的接口预估值（当开关频率远低于接口更新频率时）。

**挑战三：接口变量的数值振荡**

当接口两侧子网的特性阻抗差异较大时（典型如输电线路与换流器直流侧），Schur 补接口方程可能激发高频数值振荡（类似于直接联接两个不同特性阻抗的传输线）。**解法**：在接口处插入阻尼支路（虚拟阻尼电阻 $R_d$）或使用阻抗匹配条件。

**挑战四：多端口耦合保持与精度边界**

多端口外部网络（FDNE）的接口矩阵 $\mathbf{S}_k$ 是稠密矩阵，建模时必须保留端口间耦合。若错误地将多端口降为多个单端口独立源，会丢失交互耦合效应（如多回线路间的零序耦合）。**解法**：使用多端口 Schur 接口而非单端口等值。

## 适用边界与失败模式

- 接口矩阵可能稠密。端口数过多时，Schur 补求解会成为瓶颈。
- $\mathbf{Y}_{ii}$ 病态、孤岛化或包含理想源冲突时，消元可能失败或放大误差。
- 开关拓扑高频变化会削弱预计算收益，并可能造成接口矩阵频繁重建。
- 直接接口并不自动保证物理正确性。若分区位置切断控制闭环、保护逻辑或强非线性设备，仍需做全模型或测量基准对比。
- 与松耦合接口相比，它减少了接口外推误差，但增加同步、矩阵通信和实现复杂度。
- 当接口端口选在强耦合设备内部（如把同一桥臂的上下管分属不同子网），接口方程可能病态，导致数值不稳定。

## 代表性证据与证据边界

直接接口的数学等价性只在离散网络方程、接口变量和拓扑状态一致时成立。若论文只在特定平台、特定分区或特定实时硬件上报告加速或稳定性，不能外推为所有 EMT 网络都更快或更稳定。与 [[co-simulation]]、[[real-time-simulation]] 或 [[hardware-acceleration]] 相关的性能结论应绑定具体步长、端口数、设备模型和通信机制。

可作为证据入口的来源包括 [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic]]、[[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne]] 和 [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre]]。这些来源支持"接口一致性、补偿和多速率并行是 EMT 分区仿真的关键问题"，但不支撑无条件的精度或实时性断言。

## 相关页面

- [[interface-technique]]：接口方法总览，覆盖直接接口、等值源接口、功率接口和松耦合数据交换。
- [[hybrid-modeling]]：说明不同详细程度和不同物理域模型如何组合。
- [[electromechanical-electromagnetic-hybrid-simulation]]：说明机电暂态与 EMT 的相量/瞬时值接口。
- [[compensation-method]]：讨论分区或等值误差通过补偿源修正的路线。
- [[network-partitioning]]：讨论接口位置和分区粒度选择。
- [[nodal-admittance-matrix]]：提供直接接口所依赖的节点方程背景。
- [[schur-complement]]：Schur 补数学理论。
- [[real-time-simulation]]：实时仿真中的接口预计算策略。
- [[co-simulation]]：多工具协同仿真中的接口技术。

## 来源论文

- [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Le-Huy 等 2023]] — 并行仿真中的协同接口与补偿方法
- [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|Parvari 等]] — 多速率并行 EMT 仿真算法，基于网络撕裂的直接接口
- [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre|FMI-based parallel approach]] — 基于 FMI 的并行多步接口方法