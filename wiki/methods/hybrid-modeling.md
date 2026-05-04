---
title: "混合建模 (Hybrid Modeling)"
type: method
tags: [hybrid-modeling, co-simulation, multi-time-scale, interface, emt]
created: "2026-05-02"
---

# 混合建模 (Hybrid Modeling)

## 概述

混合建模是指将不同详细程度、不同时间尺度的模型结合起来，形成一个统一的仿真系统。在电力系统EMT仿真中，混合建模可以兼顾计算效率和仿真精度，广泛应用于机电-电磁混合仿真、详细-简化模型混合等场景。

混合建模的核心价值在于通过合理划分系统边界，在保证关键区域仿真精度的同时，大幅降低整体计算成本。这种技术特别适合分析大规模电力系统中的局部复杂现象，如[[cigre-hvdc-benchmark]]换流站故障、[[wind-farm-modeling]]风电场并网、`facts-control`FACTS设备控制等场景。

## 混合类型

### 按时间尺度分类

#### EMT-TS混合
电磁暂态（EMT）与机电暂态（TS）混合仿真是电力系统仿真的重要技术手段。

- **EMT侧**: 采用微秒级步长，详细模拟电磁暂态过程，适用于分析快速动态和[[harmonic-analysis]]谐波
- **TS侧**: 采用毫秒级步长，关注机电振荡和功角稳定性
- **典型比率**: 时间步长比通常为10:1到1000:1
- **应用场景**: [[electromechanical-electromagnetic-hybrid-simulation]] - 机电电磁混合仿真

#### 快-慢动态混合

- **快子系统**: 开关动作、控制系统响应、谐波动态
  - 时间尺度: 微秒到毫秒
  - 典型元件: [[vsc-model]]换流器、[[mmc-model]]MMC、保护装置
  
- **慢子系统**: 机械运动、热动态、长期稳定性
  - 时间尺度: 毫秒到秒
  - 典型元件: [[synchronous-machine-model]]同步机转子、[[pmsm-model]]永磁电机

#### 多时间尺度层次

| 时间尺度 | 典型过程 | 建模方法 | 仿真步长 |
|---------|---------|---------|---------|
| 纳秒-微秒 | IGBT开关、电弧 | 详细器件模型 | <1μs |
| 微秒-毫秒 | 控制系统、谐波 | 平均模型+EMT | 10-100μs |
| 毫秒-百毫秒 | 机电振荡 | 相量模型 | 1-10ms |
| 百毫秒-秒 | 长期稳定 | 简化动态 | 10-100ms |

### 按详细程度分类

#### 详细-简化混合
- **关注区域**: 采用详细[[emt-simulation]]EMT模型
  - 完整三相电路表示
  - 非线性元件精确建模
  - 控制系统详细实现
  
- **外部网络**: 采用简化等值模型
  - [[network-equivalent]] - 动态等值
  - [[fdne-model]] - 频率相关网络等值
  - 理想电压/电流源

#### 元件-系统混合

- **元件级**: 单个设备的详细物理模型
  - 半导体开关器件
  - 磁路详细建模
  - 局部场分析

- **系统级**: 整体网络等值模型
  - [[nodal-analysis]]节点导纳矩阵
  - 端口等值电路
  - 黑箱模型

### 按领域分类

#### 场路耦合混合

场路耦合混合将电磁场分析与电路分析相结合：

- **电磁场域**: Maxwell方程求解
  - 有限元分析（FEA）
  - 时域有限差分（FDTD）
  - 矩量法（MoM）
  
- **电路域**: 基尔霍夫定律求解
  - [[transmission-line-model]]传输线模型
  - 集中参数等效
  - 分布参数表示

`field-circuit-coupling` - 场路耦合技术在变压器、电机分析中有广泛应用。

#### 机电混合

- **电气系统**: 电磁暂态仿真
- **机械系统**: 多体动力学
- **耦合变量**: 电磁转矩、机械转角
- **典型应用**: [[dfig-model]]DFIG风力发电机、电动汽车驱动系统

## 接口技术

### 接口变量类型

#### 电压型接口

电压型接口将子系统表示为理想电压源：

$$
\mathbf{v}_{interface} = \mathbf{V}_{eq}
$$

**优点**:
- 实现简单，直接施加节点电压
- 对电流变化具有强鲁棒性
- 适合驱动高阻抗负载

**缺点**:
- 可能引入数值振荡
- 存在代数环风险
- 源阻抗为零，物理意义不直观

**实现要点**:
```
V_side_A → 接口电压 → V_side_B
I_side_A ← 实测电流 ← I_side_B
```

[[interface-technique]] - 接口技术是混合仿真的核心。

#### 电流型接口

电流型接口将子系统表示为理想电流源：

$$
\mathbf{i}_{interface} = \mathbf{I}_{eq}
$$

**优点**:
- 电流直接注入节点
- 适合并联连接
- 开路稳定

**缺点**:
- 对电压变化敏感
- 可能产生数值不稳定
- 需要并联阻尼

**典型应用**:
- `current-source-inverter`电流源型换流器
- 并联[[dc-rlc-filter]]滤波器建模
- 分布式电源接口

#### 功率型接口

功率型接口基于功率守恒原理：

$$
P_{in} = P_{out} + P_{loss}
$$

**功率平衡方程**:

$$
\mathbf{v}_1^T \mathbf{i}_1 = \mathbf{v}_2^T \mathbf{i}_2 + P_{loss}
$$

**特点**:
- 物理意义清晰
- 能量守恒保证
- 适合多端系统
- 实现复杂度较高

### 接口电路等值

#### 戴维南等值接口

$$
\mathbf{v}_{port} = \mathbf{v}_{th} - \mathbf{Z}_{th} \mathbf{i}_{port}
$$

其中：
- $\mathbf{v}_{th}$: 戴维南等值电压源
- $\mathbf{Z}_{th}$: 等值阻抗矩阵
- 适用于电压驱动型系统

#### 诺顿等值接口

$$
\mathbf{i}_{port} = \mathbf{i}_{n} - \mathbf{Y}_{n} \mathbf{v}_{port}
$$

其中：
- $\mathbf{i}_{n}$: 诺顿等值电流源
- $\mathbf{Y}_{n}$: 等值导纳矩阵
- 适用于电流驱动型系统

### 接口稳定性理论

#### 延迟稳定性分析

接口传输延迟是影响稳定性的关键因素：

$$
\mathbf{v}(t) = \mathbf{v}_{remote}(t - \tau_d)
$$

**稳定性判据**（基于小信号分析）:

$$
\tau_d < \frac{1}{2 f_{max}}
$$

其中 $f_{max}$ 是系统最高有效频率分量。

#### 阻抗匹配条件

接口处阻抗匹配对稳定性至关重要：

$$
Z_{out} \ll Z_{in}
$$

或采用功率匹配：

$$
Z_{out} = Z_{in}^*
$$

#### 阻尼注入技术

为提高接口稳定性，常采用阻尼注入：

$$
\mathbf{Y}_{damped} = \mathbf{Y}_{original} + \mathbf{G}_{damping}
$$

其中阻尼矩阵：

$$
\mathbf{G}_{damping} = \text{diag}(g_1, g_2, ..., g_n)
$$

`interface-stability` - 接口稳定性分析需要综合考虑时延、阻抗和数值特性。

### 直接接口技术

[[direct-interface-technique]] - 直接接口技术避免了等值近似。

#### 节点撕裂法

节点撕裂将网络在接口处分割：

`node-tearing` - 节点撕裂

$$
\begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} \end{bmatrix} \begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix} = \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \end{bmatrix}
$$

撕裂节点电压通过边界条件耦合：

$$
\mathbf{V}_{tear} = \mathbf{f}(\mathbf{I}_{tear}, \mathbf{V}_{remote})
$$

#### 拉格朗日乘子法

将接口约束作为优化问题处理：

$$
\min_{\mathbf{x}} \mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda^T \mathbf{g}(\mathbf{x})
$$

## 多速率仿真

### 速率划分原理

多速率仿真基于不同子系统的动态特性差异：

$$
\Delta t_{fast} = \frac{\Delta t_{slow}}{N_r}
$$

其中 $N_r$ 是速率比，通常为2的幂次（2, 4, 8, 16, 32, 64, 128...）

#### 子系统速率选择准则

| 准则 | 快速子系统 | 慢速子系统 |
|-----|-----------|-----------|
| 特征时间常数 | $\tau < 1$ ms | $\tau > 10$ ms |
| 开关频率 | $f_{sw} > 1$ kHz | 无开关 |
| 控制带宽 | $\omega_c > 1000$ rad/s | $\omega_c < 100$ rad/s |
| 谐波含量 | 显著 | 可忽略 |

[[multirate-method]] - 多速率方法可以显著提升仿真效率。

### 插值与外推方法

#### 线性插值

[[interpolation-method]] - 插值方法

从慢速到快速的线性插值：

$$
\mathbf{x}(t) = \mathbf{x}_k + \frac{t - t_k}{\Delta t_{slow}} (\mathbf{x}_{k+1} - \mathbf{x}_k)
$$

**优点**: 简单、计算量小
**缺点**: 精度有限，可能产生锯齿波

#### 高阶插值

三次样条插值：

$$
\mathbf{x}(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3
$$

系数通过边界条件确定：
- 位置连续性
- 速度连续性
- 加速度连续性

**Hermite插值**:

$$
\mathbf{x}(t) = \mathbf{x}_k h_{00}(\tau) + \mathbf{x}_{k+1} h_{01}(\tau) + \dot{\mathbf{x}}_k h_{10}(\tau) + \dot{\mathbf{x}}_{k+1} h_{11}(\tau)
$$

其中 $h_{ij}$ 是Hermite基函数。

#### 外推方法

**零阶保持**:

$$
\mathbf{x}(t) = \mathbf{x}_k, \quad t \in [t_k, t_{k+1})
$$

**一阶外推**:

$$
\mathbf{x}(t) = \mathbf{x}_k + \dot{\mathbf{x}}_k (t - t_k)
$$

**二阶外推**（抛物线）:

$$
\mathbf{x}(t) = \mathbf{x}_k + \dot{\mathbf{x}}_k (t - t_k) + \frac{1}{2} \ddot{\mathbf{x}}_k (t - t_k)^2
$$

### 速率匹配策略

#### 同步多速率

固定比率的多速率仿真：

```
Slow step: |--------|--------|--------|
Fast step:  |-|-|-|-|-|-|-|-|-|-|-|-|-|
            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
```

**插值策略**:
- 慢→快: 插值提供边界条件
- 快→慢: 取平均或最后值

`synchronization` - 同步是确保数据一致性的关键。

#### 异步多速率

自适应步长调整：

$$
\Delta t_{new} = f(\text{local truncation error}, \text{stability constraint})
$$

**优点**:
- 自动适应动态变化
- 效率更高
- 精度可控

**挑战**:
- 同步复杂性高
- 回退机制设计
- 状态保存开销

### 子循环技术

在慢速步长内进行多次快速计算：

$$
\text{Subcycles} = \frac{\Delta t_{slow}}{\Delta t_{fast}}
$$

**实现要点**:
1. 慢速系统在快速子循环期间保持不变
2. 快速系统使用插值边界条件
3. 子循环结束后更新慢速系统

## 机电-电磁混合仿真框架

### 混合仿真架构

[[hybrid-simulation]] - 混合仿真

#### 分层结构

```
┌─────────────────────────────────────────────────────────┐
│                    协调层 (Coordinator)                   │
│              时间管理、数据交换、收敛控制                   │
├───────────────────────────┬─────────────────────────────┤
│      机电暂态侧 (TS)         │       电磁暂态侧 (EMT)       │
│  - 相量模型               │   - 三相时域模型            │
│  - 大时间步长             │   - 小时间步长              │
│  - 功角稳定分析           │   - 快速暂态分析            │
│  - RMS值                 │   - 瞬时波形                │
└───────────────────────────┴─────────────────────────────┘
```

### TS侧建模

#### 相量模型

采用对称分量法表示：

$$
\mathbf{V}_{abc} = \mathbf{T} \mathbf{V}_{012}
$$

其中变换矩阵：

$$
\mathbf{T} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix}, \quad a = e^{j2\pi/3}
$$

#### 网络方程

机电暂态网络方程：

$$
\begin{bmatrix} \Delta \delta \\ \Delta \omega \\ \Delta E_q' \end{bmatrix} = \mathbf{A} \begin{bmatrix} \Delta \delta \\ \Delta \omega \\ \Delta E_q' \end{bmatrix} + \mathbf{B} \Delta V_{bus}
$$

### EMT侧建模

#### 三相时域模型

三相电路方程：

$$
\mathbf{Y}_{abc}(t) \mathbf{v}_{abc}(t) = \mathbf{i}_{abc}(t) + \mathbf{i}_{history}(t)
$$

#### 详细元件模型

- [[switch-modeling]]开关详细模型
- [[igbt-model]]IGBT物理模型
- [[diode-model]]二极管反向恢复
- `snubber-circuit`缓冲电路

### 接口边界处理

#### 序分量转换

三相量到序分量的转换：

[[sequence-component-method]] - 序分量

$$
\begin{bmatrix} V_0 \\ V_1 \\ V_2 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix}
$$

#### 等值电路类型

- **正序等值**: 对称正常运行
  
  $$
  \mathbf{Z}_{eq} = \mathbf{Z}_1
  $$

- **三相详细等值**: 不对称故障
  
  $$
  \mathbf{Z}_{eq} = \text{diag}(\mathbf{Z}_0, \mathbf{Z}_1, \mathbf{Z}_2)
  $$

### 应用场景

#### 远端故障分析

[[fault-analysis]] - 故障分析

当故障发生在EMT详细区域外部时：
- TS侧计算故障前稳态
- 故障瞬间切换到EMT详细模型
- 故障清除后恢复TS模型

#### FACTS设备控制

`facts-control` - FACTS控制

- [[statcom]]STATCOM无功补偿
- [[svc-model]]SVC电压调节
- [[mmc-upfc电磁-机电混合仿真技术研究]]UPFC潮流控制

## 详细-简化混合建模

### 关注区域划分

#### 内部详细区域

- 完整三相EMT模型
- 非线性详细建模
- 控制系统完整实现
- 保护逻辑详细表示

[[emt-simulation]] - 电磁暂态仿真

#### 外部简化区域

[[detailed-equivalent-model]] - 等值模型

##### WARD等值

`ward-equivalent` - WARD等值

线性网络的WARD等值：

$$
\begin{bmatrix} \mathbf{Y}_{RR} & \mathbf{Y}_{RE} \\ \mathbf{Y}_{ER} & \mathbf{Y}_{EE} \end{bmatrix} \begin{bmatrix} \mathbf{V}_R \\ \mathbf{V}_E \end{bmatrix} = \begin{bmatrix} \mathbf{I}_R \\ \mathbf{I}_E \end{bmatrix}
$$

等值导纳：

$$
\mathbf{Y}_{eq} = \mathbf{Y}_{EE} - \mathbf{Y}_{ER} \mathbf{Y}_{RR}^{-1} \mathbf{Y}_{RE}
$$

##### REI等值

`rei-equivalent` - REI等值

保留外部关键节点的等值方法：

$$
\mathbf{Y}_{REI} = \mathbf{A}^T \mathbf{Y}_{original} \mathbf{A}
$$

##### 同调等值

`coherency-equivalent` - 同调等值

基于发电机同调性的动态等值：

$$
\delta_{eq} = \frac{\sum_{i \in C} M_i \delta_i}{\sum_{i \in C} M_i}
$$

其中 $C$ 是同调机群，$M_i$ 是惯性时间常数。

### 在线安全评估

`online-security-assessment` - 在线安全评估

#### 实时等值更新

- 基于状态估计的拓扑更新
- 在线参数辨识
- 自适应等值边界

#### 计算效率优化

| 方法 | 速度提升 | 精度损失 | 适用场景 |
|-----|---------|---------|---------|
| 全详细 | 1x | 0% | 离线研究 |
| 静态等值 | 5-10x | <5% | 在线评估 |
| 动态等值 | 3-5x | <3% | 安全分析 |
| 混合建模 | 10-50x | <2% | 实时仿真 |

## 场路耦合混合建模

### 场路耦合原理

`field-circuit-coupling` - 场路耦合

#### Maxwell方程组

电磁场由Maxwell方程描述：

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

$$
\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}
$$

$$
\nabla \cdot \mathbf{D} = \rho
$$

$$
\nabla \cdot \mathbf{B} = 0
$$

#### 有限元-电路耦合

场路耦合的方程系统：

$$
\begin{bmatrix} \mathbf{K}_{field} & \mathbf{C}_{fc} \\ \mathbf{C}_{cf} & \mathbf{K}_{circuit} \end{bmatrix} \begin{bmatrix} \mathbf{A} \\ \mathbf{V} \end{bmatrix} = \begin{bmatrix} \mathbf{F}_{field} \\ \mathbf{F}_{circuit} \end{bmatrix}
$$

其中：
- $\mathbf{K}_{field}$: 场方程刚度矩阵
- $\mathbf{K}_{circuit}$: 电路导纳矩阵
- $\mathbf{C}_{fc}, \mathbf{C}_{cf}$: 耦合矩阵

### 变压器场路耦合

#### 磁路模型

变压器磁路方程：

$$
\mathbf{\Phi} = \mathbf{P} \mathbf{F}
$$

其中磁导矩阵：

$$
\mathbf{P} = \begin{bmatrix} P_{11} & P_{12} & P_{13} \\ P_{21} & P_{22} & P_{23} \\ P_{31} & P_{32} & P_{33} \end{bmatrix}
$$

#### 绕组电路方程

$$
\mathbf{v} = R \mathbf{i} + \frac{d\mathbf{\psi}}{dt}
$$

磁链与磁通关系：

$$
\psi_i = N_i \Phi_i
$$

### 电机场路耦合

#### 多截面模型

[[synchronous-machine-model]]同步机和[[pmsm-model]]永磁电机可采用多截面场路耦合：

- **气隙磁场**: 有限元详细分析
- **端部绕组**: 集中参数电路
- **铁心饱和**: 非线性磁化曲线

## EMT实现细节

### 伴随模型接口

[[companion-model]] - 伴随模型

#### 离散化方法

采用梯形法离散化：

$$
\mathbf{v}(t) = R_{eq} \mathbf{i}(t) + \mathbf{e}_{history}
$$

其中：

$$
R_{eq} = \frac{2L}{\Delta t} + R
$$

$$
\mathbf{e}_{history} = \mathbf{v}(t-\Delta t) + R_{eq} \mathbf{i}(t-\Delta t)
$$

#### 历史电流计算

接口处历史电流源：

$$
\mathbf{i}_{history}(t) = G_{eq} \mathbf{v}(t-\Delta t) + \mathbf{i}_{history}(t-\Delta t)
$$

### 网络分块求解

[[network-partitioning]] - 网络分区

#### Schur补方法

分块矩阵的Schur补求解：

$$
\begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{bmatrix} = \begin{bmatrix} \mathbf{b}_1 \\ \mathbf{b}_2 \end{bmatrix}
$$

Schur补系统：

$$
(\mathbf{D} - \mathbf{C}\mathbf{A}^{-1}\mathbf{B}) \mathbf{x}_2 = \mathbf{b}_2 - \mathbf{C}\mathbf{A}^{-1}\mathbf{b}_1
$$

#### 块对角预处理

预处理矩阵：

$$
\mathbf{M}^{-1} = \text{diag}(\mathbf{A}_1^{-1}, \mathbf{A}_2^{-1}, ..., \mathbf{A}_n^{-1})
$$

### 波形松弛法

`waveform-relaxation` - 波形松弛

#### Gauss-Seidel迭代

第$k$次迭代的子系统更新：

$$
\mathbf{x}_1^{(k)} = \mathbf{f}_1(\mathbf{x}_2^{(k-1)}, t)
$$

$$
\mathbf{x}_2^{(k)} = \mathbf{f}_2(\mathbf{x}_1^{(k)}, t)
$$

#### 收敛判据

$$
||\mathbf{x}^{(k)} - \mathbf{x}^{(k-1)}|| < \epsilon
$$

或

$$
\frac{||\mathbf{x}^{(k)} - \mathbf{x}^{(k-1)}||}{||\mathbf{x}^{(k)}||} < \epsilon_{rel}
$$

## 并行混合仿真

### 空间并行

[[parallel-computing]] - 并行计算

#### 域分解方法

`domain-decomposition` - 域分解

重叠型域分解（Schwarz方法）：

$$
\Omega = \Omega_1 \cup \Omega_2 \cup ... \cup \Omega_n
$$

重叠区域 $\Omega_{overlap} = \Omega_i \cap \Omega_j$ 保证信息传递。

#### 非重叠分解

非重叠型（Schur补方法）：

- 内部子域独立求解
- 界面问题协调求解
- 适合大规模系统

### 时间并行

#### 流水线并行

`pipelining` - 流水线

多时间窗流水线：

```
时间窗1: [计算]→[通信]→[输出]
时间窗2:      [计算]→[通信]→[输出]
时间窗3:           [计算]→[通信]→[输出]
```

#### 抛物areal方法

粗粒度时间并行：

$$
\mathbf{x}(t_n) = \mathbf{\Phi}(\mathbf{x}(t_0), t_n - t_0)
$$

预测-校正迭代：

$$
\mathbf{x}^{(k+1)} = \mathbf{\Phi}(\mathbf{x}^{(k)})
$$

### 异构计算

[[heterogeneous-computing]] - 异构计算

#### CPU+GPU协同

任务分配策略：

| 任务类型 | 处理单元 | 原因 |
|---------|---------|-----|
| 稀疏矩阵求解 | CPU | 不规则访存 |
| 矩阵向量乘法 | GPU | 高并行度 |
| 元件计算 | GPU | 数据并行 |
| 通信协调 | CPU | 复杂逻辑 |

[[hardware-acceleration]] - 硬件加速

#### FPGA加速

- 固定步长计算
- 流水线架构
- 确定性时延

## 验证与误差分析

### 精度验证方法

`accuracy-verification` - 精度验证

#### 与详细模型对比

误差指标：

**绝对误差**:

$$
\epsilon_{abs} = |x_{hybrid} - x_{reference}|
$$

**相对误差**:

$$
\epsilon_{rel} = \frac{|x_{hybrid} - x_{reference}|}{|x_{reference}|}
$$

**均方根误差**:

$$
\epsilon_{RMS} = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_{hybrid,i} - x_{reference,i})^2}
$$

#### 频域验证

频响函数对比：

$$
H(f) = \frac{\mathcal{F}\{output\}}{\mathcal{F}\{input\}}
$$

幅值误差：

$$
\epsilon_{mag}(f) = |20\log_{10}|H_{hybrid}|| - |20\log_{10}|H_{ref}||
$$

### 误差来源分析

#### 截断误差

泰勒展开截断误差：

$$
\epsilon_{trunc} = \frac{\Delta t^{p+1}}{(p+1)!} \frac{d^{p+1}x}{dt^{p+1}}
$$

其中 $p$ 是积分阶数。

#### 接口误差

接口近似引入的误差：

$$
\epsilon_{interface} = f(\tau_d, Z_{mismatch}, interpolation\_order)
$$

主要因素：
- 时延 $\tau_d$: 延迟引起的相位误差
- 阻抗失配 $Z_{mismatch}$: 反射引起的波形失真
- 插值阶数: 插值精度限制

### 稳定性验证

[[numerical-stability]] - 数值稳定性

#### 长期稳定性测试

长时间仿真验证数值稳定性：

$$
t_{sim} = 100 \times t_{settling}
$$

检查能量守恒：

$$
\Delta E = E_{final} - E_{initial} < \epsilon_{energy}
$$

#### 物理合理性检查

- 功率方向正确性
- 电压电流相位关系
- 能量耗散非负
- 设备限值检查

## 应用案例

### HVDC混合仿真

[[vsc-hvdc]] - 柔性直流输电

#### 系统配置

```
AC Grid (TS) --[Interface]-- VSC Station (EMT) -- DC Line -- VSC Station (EMT) --[Interface]-- AC Grid (TS)
```

#### 仿真策略

- **换流站**: EMT详细模型
  - [[vsc-model]]VSC详细开关模型
  - 控制保护完整实现
  - 谐波滤波器
  
- **交流网**: TS相量模型
  - 大规模电网等值
  - 机电振荡分析
  - 多机系统

#### 典型结果

| 指标 | 全EMT | 混合仿真 | 误差 |
|-----|-------|---------|-----|
| 仿真时间 | 24h | 2h | - |
| 直流电压峰值 | 1.15 pu | 1.14 pu | <1% |
| 故障电流 | 基准 | 0.98 p.u. | 2% |
| 暂态过程 | 详细 | 一致 | - |

### 风电场仿真

[[wind-farm-modeling]] - 风电场建模

#### 聚合策略

- **关注风机**: 详细[[dfig-model]]DFIG/[[pmsm-model]]PMSM模型
- **其他风机**: 等值聚合模型
  - 单机等值
  - 多机等值
  - 风速分布聚合

#### 电气集电系统

- 详细电缆模型: 关注区域
- 等值阻抗: 远端集电

### 城市电网分析

`urban-power-grid` - 城市电网

#### 关注馈线分析

- **详细区域**: 关注馈线及其负荷
  - 配电变压器详细
  - 负荷时变性
  - 电能质量问题

- **外部网络**: 输电网等值
  - 变电站等值
  - 上级电网简化

#### 应用场景

- `power-quality`电能质量分析
- `voltage-stability`电压稳定性评估
- `protection-coordination`保护配合研究
- [[distributed-generation]]分布式电源接入

### 微电网混合仿真

#### 分层建模

- **设备层**: 详细开关模型
  - [[energy-storage-converter-model]]储能变流器
  - `solar-inverter`光伏逆变器
  - `diesel-generator`柴油发电机

- **系统层**: 功率平衡模型
  - 功率流计算
  - 能量管理
  - 稳定性分析

### 海上风电送出

#### 复杂系统配置

- **海上风电场**: 详细模型
  - 海上集电网络
  - 升压站
  - [[cigre-hvdc-benchmark]]HVDC换流站

- **陆上电网**: 等值模型
  - 交流主网
  - 负荷中心

## 挑战与发展趋势

### 自动分区技术

`automatic-partitioning` - 自动分区

#### 基于图论的分区

电网拓扑图 $G = (V, E)$：

目标函数：

$$
\min \sum_{edges\ cut} w_{ij} + \lambda \sum_{subdomains} |N_k - N_{avg}|^2
$$

约束：
- 子系统规模平衡
- 接口数量最少
- 动态特性匹配

#### 基于聚类的分区

K-means聚类应用于电网分区：

$$
J = \sum_{k=1}^K \sum_{i \in C_k} ||\mathbf{x}_i - \mathbf{\mu}_k||^2
$$

特征向量包含：
- 电气距离
- 动态时间常数
- 功率交换量

### 自适应精度控制

`adaptive-accuracy` - 自适应精度

#### 动态模型切换

根据系统状态自动切换模型：

$$
Model(t) = \begin{cases}
Model_{detailed} & \text{if } |\Delta v| > v_{threshold} \\
Model_{simplified} & \text{otherwise}
\end{cases}
$$

#### 误差估计与调整

局部截断误差估计：

$$
\epsilon_{local} = ||\mathbf{x}_{high-order} - \mathbf{x}_{low-order}||
$$

步长调整：

$$
\Delta t_{new} = \Delta t_{old} \left(\frac{\epsilon_{target}}{\epsilon_{local}}\right)^{1/(p+1)}
$$

### 新兴技术趋势

#### 数字孪生集成

- 实时数据驱动模型更新
- 虚实结合验证
- 预测性分析

#### 人工智能辅助

- 机器学习加速等值
- 神经网络代理模型
- 智能分区决策

#### 云仿真平台

- 分布式云资源
- 弹性计算能力
- 协同仿真环境

## 相关方法

- [[co-simulation]] - 联合仿真
- [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems]] - 多速率仿真
- [[time-domain-modeling-of-a-subsea-buried-cable]] - 时域建模
- `distributed-simulation` - 分布式仿真
- [[electromechanical-electromagnetic-hybrid-simulation]] - 机电电磁混合仿真
- [[interpolation-method]] - 插值方法
- [[interface-technique]] - 接口技术
- [[network-equivalent]] - 动态等值
- [[model-order-reduction]] - 模型降阶
- [[real-time-simulation]] - 实时仿真

## 来源论文

参见 [[index.md]] 获取更多混合建模相关文献。

---

*本页面基于EMT仿真领域混合建模方法的系统整理，涵盖了接口技术、多速率仿真、机电-电磁混合等核心技术。*
