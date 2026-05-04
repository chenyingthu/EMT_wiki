---
title: "接口技术 (Interface Technique)"
type: method
tags: [interface, coupling, subnetwork, connection, partitioning]
created: "2026-05-02"
---

# 接口技术 (Interface Technique)

## 概述

接口技术是电力系统电磁暂态（EMT）仿真中将多个子网络或多个仿真域连接起来的关键技术。在分网并行仿真、混合仿真和联合仿真中，接口技术决定了子系统之间的数据交换方式和耦合精度，直接影响仿真的准确性和稳定性。

接口技术的核心问题包括：
- **等值表示**：如何用简化的等值电路表示子系统对外部网络的电气特性
- **数据交换**：在接口边界处交换电压、电流或功率信息
- **时间同步**：处理不同子系统可能采用的不同仿真步长
- **稳定性保障**：确保接口不会引入数值不稳定或物理不准确

## 理论基础

### 网络撕裂理论

网络撕裂（Network Tearing）是接口技术的理论基础，通过将大规模电力网络分解为若干子网络来降低计算复杂度。撕裂点处的边界条件需要精确处理以保证整体解的一致性。

**基本撕裂方程**：

将网络导纳矩阵按内部节点和边界节点分块：

$$\begin{bmatrix} Y_{ii} & Y_{ib} \\ Y_{bi} & Y_{bb} \end{bmatrix} \begin{bmatrix} V_i \\ V_b \end{bmatrix} = \begin{bmatrix} I_i \\ I_b \end{bmatrix}$$

其中：
- $Y_{ii}$：内部节点自导纳矩阵
- $Y_{ib}, Y_{bi}$：内部-边界节点互导纳矩阵
- $Y_{bb}$：边界节点自导纳矩阵
- $V_i, V_b$：内部和边界节点电压向量
- $I_i, I_b$：内部和边界节点注入电流向量

**舒尔补（Schur Complement）**：

消去内部节点后，边界节点的等效方程为：

$$Y_{bb}^{eq} V_b = I_b^{eq}$$

其中等效导纳和等效电流源为：

$$Y_{bb}^{eq} = Y_{bb} - Y_{bi} Y_{ii}^{-1} Y_{ib}$$

$$I_b^{eq} = I_b - Y_{bi} Y_{ii}^{-1} I_i$$

这构成了接口等值的基础数学框架。详见`schur-complement`。

### 域分解方法

域分解（Domain Decomposition）是将计算域划分为子域并行求解的数学方法，广泛应用于EMT并行仿真。

**重叠型域分解（Schwarz方法）**：
- 子域间存在重叠区域
- 通过迭代交换重叠区信息实现收敛
- 收敛速度较慢但实现简单

**非重叠型域分解（Schur方法）**：
- 子域间通过接口边界连接
- 构造并求解缩减的接口问题
- 通信量小但接口矩阵可能稠密

**有限元撕裂与互联（FETI）**：
- 引入接口拉格朗日乘子
- 子域问题独立求解
- 通过协调方程保证界面连续性

## 电压型接口

### 戴维南等值基础

电压型接口采用戴维南等值电路表示子系统，由一个理想电压源串联等效阻抗构成。

**单端口戴维南等值**：

$$v_{eq}(t) = v_{th}(t) - Z_{th} \cdot i(t)$$

其中：
- $v_{th}(t)$：开路电压（戴维南电压）
- $Z_{th}$：等效阻抗（戴维南阻抗）
- $i(t)$：接口电流

**等效阻抗计算**：

对于线性网络，戴维南阻抗可通过下式计算：

$$Z_{th} = \frac{V_{oc}}{I_{sc}}$$

其中$V_{oc}$为开路电压，$I_{sc}$为短路电流。

或从导纳矩阵直接提取：

$$Z_{th} = \left(Y_{bb}^{eq}\right)^{-1}$$

详见[[thevenin-equivalent]]。

### 多端口戴维南等值

当接口包含多个连接点时，需要采用多端口戴维南等值。

**矩阵形式**：

$$\mathbf{v}_{eq}(t) = \mathbf{v}_{th}(t) - \mathbf{Z}_{th} \cdot \mathbf{i}(t)$$

其中：
- $\mathbf{v}_{eq}$：接口电压向量（$n \times 1$）
- $\mathbf{v}_{th}$：开路电压向量（$n \times 1$）
- $\mathbf{Z}_{th}$：等效阻抗矩阵（$n \times n$）
- $\mathbf{i}$：接口电流向量（$n \times 1$）

**阻抗矩阵元素**：

$Z_{th,ij}$表示在端口$j$注入单位电流时，端口$i$的开路电压变化：

$$Z_{th,ij} = \frac{\partial v_i}{\partial i_j}$$

**对称性**：对于互易网络，$\mathbf{Z}_{th}$为对称矩阵，即$Z_{th,ij} = Z_{th,ji}$。

**时域实现**：

在EMT仿真中，等效阻抗通常采用离散化伴随模型表示。对于电阻$R$、电感$L$、电容$C$元件：

- 电阻：$R_{eq} = R$
- 电感（梯形法）：$R_{eq} = \frac{2L}{\Delta t}$，$J_{hist} = i_n + \frac{v_n \Delta t}{2L}$
- 电容（梯形法）：$R_{eq} = \frac{\Delta t}{2C}$，$J_{hist} = -i_n - \frac{v_n}{R_{eq}}$

### 戴维南接口的数值特性

**优势**：
- 物理意义明确，易于理解
- 对电流型负载稳定性好
- 便于实现电压控制型设备接口

**局限**：
- 对电压源型负载可能产生数值振荡
- 等效阻抗矩阵求逆计算量大
- 非线性子系统线性化引入误差

## 电流型接口

### 诺顿等值基础

电流型接口采用诺顿等值电路表示子系统，由一个理想电流源并联等效导纳构成。

**单端口诺顿等值**：

$$i_{eq}(t) = i_{n}(t) - Y_{n} \cdot v(t)$$

其中：
- $i_{n}(t)$：短路电流（诺顿电流）
- $Y_{n}$：等效导纳（诺顿导纳）
- $v(t)$：接口电压

**等效导纳计算**：

$$Y_{n} = \frac{1}{Z_{th}} = Y_{bb}^{eq}$$

诺顿等值与戴维南等值通过源变换相互转换：

$$i_n = \frac{v_{th}}{Z_{th}}, \quad Y_n = \frac{1}{Z_{th}}$$

详见[[norton-equivalent]]。

### 多端口诺顿等值

**矩阵形式**：

$$\mathbf{i}_{eq}(t) = \mathbf{i}_{n}(t) - \mathbf{Y}_{n} \cdot \mathbf{v}(t)$$

其中：
- $\mathbf{i}_{eq}$：接口电流向量（$n \times 1$）
- $\mathbf{i}_{n}$：短路电流向量（$n \times 1$）
- $\mathbf{Y}_{n}$：等效导纳矩阵（$n \times n$）
- $\mathbf{v}$：接口电压向量（$n \times 1$）

**导纳矩阵与阻抗矩阵关系**：

$$\mathbf{Y}_{n} = \mathbf{Z}_{th}^{-1}$$

**诺顿等值的物理实现**：

在节点分析框架下，诺顿等值直接对应节点注入电流：

$$\mathbf{I}_{inj} = \mathbf{i}_{n} - \mathbf{Y}_{n} \mathbf{V}$$

这使得诺顿接口与EMT仿真中的节点电压法天然兼容。

### 诺顿接口的数值特性

**优势**：
- 与节点电压法直接兼容
- 导纳矩阵通常稀疏，计算高效
- 对电压源型负载稳定性好

**局限**：
- 对电流源型负载可能产生数值振荡
- 导纳矩阵可能需要LU分解
- 开路处理需要特殊技巧（大电阻法）

## 混合型接口

### 功率型接口

功率型接口以功率交换为核心，适用于机电-电磁混合仿真等场景。

**功率平衡方程**：

$$P_{emt} + jQ_{emt} = P_{ts} + jQ_{ts}$$

其中EMT侧提供瞬时功率，机电侧提供基波功率。

**接口变量选择**：

功率型接口需要选择适当的接口变量组合：

- **电压-电流型**：EMT侧电压→机电侧，机电侧电流→EMT侧
- **电流-电压型**：EMT侧电流→机电侧，机电侧电压→EMT侧
- **功率-电压型**：交换功率和电压，计算电流

详见`power-interface`。

### 混合参数表示

对于多端口网络，可采用混合参数（h参数）描述接口特性：

$$\begin{bmatrix} \mathbf{v}_1 \\ \mathbf{i}_2 \end{bmatrix} = \begin{bmatrix} \mathbf{H}_{11} & \mathbf{H}_{12} \\ \mathbf{H}_{21} & \mathbf{H}_{22} \end{bmatrix} \begin{bmatrix} \mathbf{i}_1 \\ \mathbf{v}_2 \end{bmatrix}$$

混合参数适用于不同类型端口的混合连接场景。

## 直接接口技术

### 节点撕裂法

节点撕裂（Node Tearing）将网络在边界节点处分离，形成独立的子网络和接口方程。

**撕裂点选择准则**：
- 最小化接口节点数
- 最大化子网络并行度
- 保持子网络电气完整性
- 避免数值病态条件

**撕裂方程推导**：

设网络有$n$个节点，撕裂后分为$m$个子网络。全局导纳方程为：

$$\mathbf{Y} \mathbf{V} = \mathbf{I}$$

按子网络分块：

$$\begin{bmatrix} \mathbf{Y}_1 & & & \mathbf{Y}_{1b} \\ & \mathbf{Y}_2 & & \mathbf{Y}_{2b} \\ & & \ddots & \vdots \\ \mathbf{Y}_{b1} & \mathbf{Y}_{b2} & \cdots & \mathbf{Y}_{bb} \end{bmatrix} \begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \\ \vdots \\ \mathbf{V}_b \end{bmatrix} = \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \\ \vdots \\ \mathbf{I}_b \end{bmatrix}$$

各子网络独立求解：

$$\mathbf{V}_k = \mathbf{Y}_k^{-1} \left( \mathbf{I}_k - \mathbf{Y}_{kb} \mathbf{V}_b \right), \quad k=1,2,...,m$$

边界节点电压通过接口方程求解：

$$\mathbf{Y}_{bb}^{*} \mathbf{V}_b = \mathbf{I}_b^{*}$$

其中：

$$\mathbf{Y}_{bb}^{*} = \mathbf{Y}_{bb} - \sum_{k=1}^{m} \mathbf{Y}_{bk} \mathbf{Y}_k^{-1} \mathbf{Y}_{kb}$$

$$\mathbf{I}_b^{*} = \mathbf{I}_b - \sum_{k=1}^{m} \mathbf{Y}_{bk} \mathbf{Y}_k^{-1} \mathbf{I}_k$$

详见`node-tearing`和[[network-partitioning]]。

### 支路撕裂法

支路撕裂（Branch Tearing）在网络支路处进行分离，适用于特定拓扑结构。

**撕裂支路电流作为变量**：

$$\mathbf{V}_m - \mathbf{V}_n = \mathbf{Z}_b \mathbf{I}_b + \mathbf{V}_s$$

其中$\mathbf{V}_m, \mathbf{V}_n$为支路两端节点电压，$\mathbf{Z}_b$为支路阻抗，$\mathbf{I}_b$为支路电流，$\mathbf{V}_s$为支路电压源。

**改进节点分析法（MNA）**：

将支路电流作为独立变量，扩展节点方程：

$$\begin{bmatrix} \mathbf{Y}_n & \mathbf{A} \\ \mathbf{A}^T & \mathbf{Z}_b \end{bmatrix} \begin{bmatrix} \mathbf{V} \\ \mathbf{I}_b \end{bmatrix} = \begin{bmatrix} \mathbf{I}_n \\ \mathbf{V}_s \end{bmatrix}$$

其中$\mathbf{A}$为支路-节点关联矩阵。

### 撕裂方程的并行求解

**两步求解策略**：

1. **本地阶段**：各子网络独立进行LU分解和求解
   $$\mathbf{L}_k \mathbf{U}_k = \mathbf{Y}_k$$

2. **协调阶段**：求解缩减的接口问题
   $$\mathbf{Y}_{bb}^{*} \mathbf{V}_b = \mathbf{I}_b^{*}$$

3. **回代阶段**：将边界电压代入求内部节点电压
   $$\mathbf{V}_k = \mathbf{Y}_k^{-1} \left( \mathbf{I}_k - \mathbf{Y}_{kb} \mathbf{V}_b \right)$$

这种分解使得大规模并行计算成为可能。

## 迭代接口方法

### 波形松弛法

波形松弛（Waveform Relaxation, WR）通过迭代交换子系统的时域波形实现耦合求解。

**基本迭代格式**：

$$\mathbf{x}_i^{(k+1)} = \mathbf{f}_i\left(\mathbf{x}_i^{(k+1)}, \mathbf{x}_{j \neq i}^{(k)}\right), \quad i=1,2,...,N$$

其中$\mathbf{x}_i^{(k)}$为第$i$个子系统在第$k$次迭代的解波形。

**收敛条件**：

$$\|\mathbf{x}^{(k+1)} - \mathbf{x}^{(k)}\| < \varepsilon$$

或

$$\|\mathbf{x}^{(k+1)} - \mathbf{x}^{*}\| < \varepsilon$$

其中$\mathbf{x}^{*}$为精确解。

详见`waveform-relaxation`。

### Jacobi与Gauss-Seidel迭代

**Jacobi迭代（并行型）**：

$$\mathbf{x}_i^{(k+1)} = g_i\left(\mathbf{x}_1^{(k)}, \mathbf{x}_2^{(k)}, ..., \mathbf{x}_N^{(k)}\right)$$

所有子系统基于前一次迭代的结果并行更新。

**Gauss-Seidel迭代（串行型）**：

$$\mathbf{x}_i^{(k+1)} = g_i\left(\mathbf{x}_1^{(k+1)}, ..., \mathbf{x}_{i-1}^{(k+1)}, \mathbf{x}_i^{(k)}, ..., \mathbf{x}_N^{(k)}\right)$$

子系统按顺序更新，利用最新可用的信息。

**收敛速度比较**：

- Gauss-Seidel通常收敛更快（信息更新更及时）
- Jacobi更适合大规模并行实现
- 超松弛（SOR）可加速收敛：
  $$\mathbf{x}_i^{(k+1)} = (1-\omega)\mathbf{x}_i^{(k)} + \omega g_i(\cdot)$$
  其中$\omega$为松弛因子（$1 < \omega < 2$）

详见`iterative-method`。

### 收敛性分析

**收敛充分条件**：

若子系统间的耦合足够弱，波形松弛保证收敛。数学上，要求耦合矩阵的谱半径小于1：

$$\rho(\mathbf{M}^{-1}\mathbf{N}) < 1$$

其中$\mathbf{M}$为块对角矩阵，$\mathbf{N}$为耦合矩阵。

**时间窗策略**：

为提高收敛速度，常采用时间窗（Time Window）技术：

1. 将仿真时段划分为多个窗口
2. 在每个窗口内独立进行WR迭代
3. 窗口间传递最终状态作为初始条件

## 时域接口

### 插值方法

当子系统采用不同仿真步长时，需要在接口处进行插值。

**线性插值**：

$$v(t) = v(t_1) + \frac{t - t_1}{t_2 - t_1} \left[v(t_2) - v(t_1)\right]$$

优点：计算简单，保证稳定性
缺点：精度较低，仅一阶准确

**三次样条插值**：

$$v(t) = a_i + b_i(t-t_i) + c_i(t-t_i)^2 + d_i(t-t_i)^3, \quad t \in [t_i, t_{i+1}]$$

优点：二阶连续，精度高
缺点：计算复杂，可能产生过冲

**Hermite插值**：

利用函数值和导数值：

$$v(t) = h_1(t)v_1 + h_2(t)v_2 + h_3(t)\dot{v}_1 + h_4(t)\dot{v}_2$$

其中$h_i(t)$为Hermite基函数。

详见[[interpolation-method]]。

### 外推方法

当需要预测未来时刻的接口值时，采用外推方法。

**线性外推**：

$$v(t+\Delta t) = v(t) + \frac{dv}{dt}\Delta t$$

**二阶外推**：

$$v(t+\Delta t) = v(t) + \frac{dv}{dt}\Delta t + \frac{1}{2}\frac{d^2v}{dt^2}(\Delta t)^2$$

**稳定性考虑**：

外推引入的误差可能导致数值不稳定，需要限制外推阶数或采用滤波。

详见[[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da]]。

### 多速率接口

多速率仿真中，子系统以不同步长运行，接口需要处理时间尺度差异。

**整数倍速率比**：

若$\Delta t_1 = m \cdot \Delta t_2$（$m$为整数），可采用以下策略：

- 慢子系统每$m$步更新一次接口值
- 快子系统每步向慢子系统提供累积效应或平均值

**非整数倍速率比**：

需要更复杂的插值/外推策略，或采用事件驱动同步。

**回插技术（Back-interpolation）**：

当快子系统检测到事件（如开关动作），可能需要回退慢子系统并重新计算：

1. 快子系统检测到事件在$t_{event}$
2. 插值得到慢子系统在$t_{event}$的状态
3. 重新同步两个子系统

详见[[multirate-method]]。

### 接口稳定性分析

**延迟效应**：

接口处的一步延迟可建模为：

$$v_{recv}(t) = v_{send}(t - \tau)$$

其中$\tau$为等效延迟时间。

**稳定性判据**：

采用小增益定理分析接口稳定性。对于线性系统，要求：

$$\|G_1(s)\|_\infty \cdot \|G_2(s)\|_\infty < 1$$

其中$G_1, G_2$为子系统传递函数，$\|\cdot\|_\infty$为H无穷范数。

**阻尼电阻法**：

在接口处添加虚拟阻尼电阻可改善稳定性：

$$R_{damp} = \sqrt{\frac{L_{eq}}{C_{eq}}}$$

其中$L_{eq}, C_{eq}$为等效电感和电容。

详见`interface-stability`和[[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models]]。

## EMT仿真应用

### 分网并行仿真

大规模电力系统EMT仿真中，网络分区并行是提升计算效率的关键技术。

**分区策略**：

- **地理分区**：按地理位置划分
- **电气分区**：按电气距离或耦合强度划分
- **功能分区**：按设备类型或电压等级划分

**并行效率**：

并行加速比受限于Amdahl定律：

$$S = \frac{1}{(1-P) + \frac{P}{N}}$$

其中$P$为可并行化比例，$N$为处理器数量。

接口开销主要来自：
- 边界数据通信
- 接口方程求解
- 同步等待

详见[[network-partitioning]]。

### 混合仿真

EMT与机电暂态（TS）混合仿真结合了两种方法的优势。

**EMT-TS接口**：

- EMT侧：详细模型，小步长（$\mu$s级）
- TS侧：基波模型，大步长（ms级）

**功率交换接口**：

1. EMT侧计算瞬时功率
2. 滤波提取基波功率
3. 传递给TS侧作为负荷/电源
4. TS侧计算基波电压
5. 作为等值电压源施加于EMT侧

**稳定性挑战**：

不同时间尺度的耦合可能引发数值振荡，需要：
- 适当的接口滤波
- 时延补偿技术
- 协调的仿真步长

详见[[hybrid-simulation]]和[[electromechanical-electromagnetic-hybrid-simulation]]。

### 联合仿真与FMI

联合仿真（Co-simulation）允许多个仿真工具协同求解。

**FMI标准**：

功能 mock-up 接口（FMI）定义了标准化的联合仿真接口：

- **FMU**：包含模型和求解器的封装单元
- **主从架构**：主程序协调各FMU的求解
- **数据交换**：通过标准化API交换变量

**FMI for Co-simulation**：

$$\mathbf{x}_{k+1} = f(\mathbf{x}_k, \mathbf{u}_k, \Delta t)$$

其中$\Delta t$为通信步长，$\mathbf{u}_k$为输入变量。

**通信步长选择**：

- 过小：通信开销大
- 过大：精度下降，稳定性问题
- 通常取子系统最小步长的整数倍

详见[[co-simulation]]和`fmi`。

## 接口优化技术

### 接口最小化

减少接口变量数可降低通信开销和计算复杂度。

**端口缩减技术**：

- **模态分析**：仅保留主导模态对应的接口
- **平衡截断**：基于可控性和可观性格拉姆矩阵
- **Krylov子空间**：矩匹配降阶

**等值简化**：

采用[[fdne-model]]（频率相关网络等值）简化外部网络，减少接口节点数。

详见`interface-optimization`。

### 预处理技术

预处理改善接口方程的数值特性，加速求解。

**不完全LU预处理（ILU）**：

$$\mathbf{M} \approx \mathbf{L}\mathbf{U} \approx \mathbf{Y}_{bb}^{*}$$

求解预处理系统：

$$\mathbf{M}^{-1}\mathbf{Y}_{bb}^{*}\mathbf{V}_b = \mathbf{M}^{-1}\mathbf{I}_b^{*}$$

**对角缩放**：

$$\mathbf{D}^{-1/2}\mathbf{Y}_{bb}^{*}\mathbf{D}^{-1/2}\mathbf{D}^{1/2}\mathbf{V}_b = \mathbf{D}^{-1/2}\mathbf{I}_b^{*}$$

其中$\mathbf{D} = diag(\mathbf{Y}_{bb}^{*})$。

详见`preconditioning`。

### 通信优化

**聚合通信**：

将多个小消息聚合为大数据包，减少通信延迟：

$$T_{comm} = T_{latency} + \frac{N_{bytes}}{Bandwidth}$$

**异步通信**：

采用非阻塞通信重叠计算与通信：

```
开始通信 -> 本地计算 -> 等待通信完成 -> 接口求解
```

**预测-校正**：

利用历史数据预测接口值，减少通信频率：

$$\hat{v}(t+\Delta t) = 2v(t) - v(t-\Delta t) \quad \text{(线性预测)}$$

## 稳定性分析与改善方法

### 接口延迟稳定性

延迟是影响接口稳定性的关键因素。

**延时微分方程**：

含延迟的接口方程：

$$\frac{d\mathbf{x}}{dt} = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{x}(t-\tau)$$

**稳定性判据**：

特征方程：

$$det\left(s\mathbf{I} - \mathbf{A} - \mathbf{B}e^{-s\tau}\right) = 0$$

对于简单系统，可得到显式稳定条件。例如，对于$LC$电路与延迟电阻接口：

$$\tau < \frac{\pi}{2}\sqrt{LC}$$

详见[[the-computer-simulation-and-real-time-stabilization-control-for-the-inverted-pen]]。

### 阻抗匹配法

通过调整接口阻抗改善稳定性。

**特性阻抗匹配**：

接口阻抗与子系统特性阻抗匹配：

$$Z_{interface} = \sqrt{Z_{in} \cdot Z_{out}}$$

**虚拟阻抗**：

在接口处引入虚拟阻抗$Z_v$：

$$v_{eq} = v_{th} - (Z_{th} + Z_v)i$$

适当选择$Z_v$可阻尼振荡模式。

### 滤波技术

**低通滤波**：

一阶低通滤波器：

$$H(s) = \frac{1}{1 + sT_f}$$

其中$T_f$为滤波时间常数。

**陷波滤波**：

针对特定振荡频率：

$$H(s) = \frac{s^2 + \omega_0^2}{s^2 + \frac{\omega_0}{Q}s + \omega_0^2}$$

**滤波参数选择**：

- 截止频率需高于关注的最高频率
- 过低的截止频率会引入额外延迟
- 需要权衡稳定性与精度

### 时延补偿

**Smith预测器**：

预测无延迟时的输出：

$$\hat{y}(t) = y(t) + G_p(1-e^{-\tau s})u(t)$$

其中$G_p$为无延迟过程模型。

**相位超前补偿**：

$$G_c(s) = K\frac{1 + sT_d}{1 + sT_d/N}$$

补偿延迟引入的相位滞后。

## 实现考虑

### 数值积分方法影响

不同积分方法对接口特性有不同影响：

**梯形法**：
- A-稳定，适合刚性系统
- 可能引入数值振荡
- 接口伴随模型：$R_{eq} = \frac{2L}{\Delta t}$或$\frac{\Delta t}{2C}$

**后向欧拉**：
- L-稳定，数值阻尼大
- 精度较低（一阶）
- 接口伴随模型：$R_{eq} = \frac{L}{\Delta t}$或$\frac{\Delta t}{C}$

**Gear法**：
- 多步法，高阶精度
- 需要历史值存储
- 启动需单步法配合

### 非线性处理

非线性元件的接口处理：

**分段线性化**：

$$i = G_{eq}v + I_{eq}$$

其中$G_{eq}, I_{eq}$在工作点处线性化。

**牛顿迭代**：

$$\mathbf{J}\Delta\mathbf{x} = -\mathbf{F}(\mathbf{x})$$

其中$\mathbf{J}$为雅可比矩阵。

### 开关处理

开关动作时的接口处理：

**插值开关**：

精确确定开关时刻$t_{sw}$，插值得到该时刻状态，重启仿真。

**临界阻尼调整**：

开关瞬间调整接口阻尼，抑制数值振荡。

## 相关方法

- [[network-partitioning]] - 网络分区
- `coupling-method` - 耦合方法
- `domain-decomposition` - 域分解
- `substructuring` - 子结构
- [[thevenin-equivalent]] - 戴维南等值
- [[norton-equivalent]] - 诺顿等值
- [[multirate-method]] - 多速率方法
- [[co-simulation]] - 联合仿真
- `waveform-relaxation` - 波形松弛
- `iterative-method` - 迭代法
- [[interpolation-method]] - 插值方法
- `schur-complement` - 舒尔补

## 来源论文

接口技术在EMT仿真领域的应用涉及以下研究方向：

- 分网并行仿真的网络撕裂方法
- EMT-TS混合仿真的接口稳定性
- 基于FMI的电力系统联合仿真
- 多速率仿真中的接口插值技术
- 大规模系统的域分解算法

详参见 [[index.md]] 获取更多 获取更多接口技术相关文献。
