---
title: "时域建模 (Time Domain Modeling)"
type: topic
tags: [time-domain, transient-analysis, numerical-simulation, emt, differential-equations, dae, state-space, nodal-analysis]
created: "2026-05-04"
updated: "2026-05-17"
# 时域建模 (Time Domain Modeling)

## 定义

时域建模是以时间为自变量，通过直接求解微分方程或差分方程来获得系统状态变量随时间演化轨迹的一类建模方法。在EMT（电磁暂态）仿真中，时域建模是分析电磁暂态过程的核心范式，能够处理非线性元件、开关动作、非对称故障等复杂现象，与频域方法形成互补 [Dommel 1969]。

电力系统时域建模的核心数学对象是**微分-代数方程组（DAE）**：

$$
\begin{cases}
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{v}, t) & \text{（元件动态方程）} \\
\mathbf{0} = \mathbf{g}(\mathbf{x}, \mathbf{v}, t) & \text{（网络代数方程）}
\end{cases}
$$

其中 $\mathbf{x}$ 为状态变量（电感电流、电容电压），$\mathbf{v}$ 为节点电压，$\mathbf{f}$ 描述储能元件动态，$\mathbf{g}$ 描述网络拓扑约束 [Kundur 1994]。

## EMT中的作用

时域建模是EMT仿真的基础范式，其核心价值体现在：

- **暂态过程捕捉**：开关操作、故障、雷击的完整波形记录，精度可达微秒级
- **非线性设备处理**：变压器饱和特性、电晕效应、电力电子开关动作
- **控制系统接口**：保护继电器、调速系统、励磁控制的离散/连续混合仿真
- **波形分析**：电压电流瞬时值、相位关系、谐波含量的时域表征
- **设备应力评估**：过电压/过电流峰值及变化率（dV/dt、dI/dt）的精确计算

时域仿真的典型时间尺度覆盖：

$$
\tau_{EMT} \sim \mu\text{s to ms}, \quad \tau_{TS} \sim 100\text{ms to s}
$$

混合仿真需处理 $10^3$ 至 $10^6$ 倍的时间尺度差异 [Mu 2014]。

## EMT建模方法体系

时域建模方法可按求解范式分为三大类：状态空间法、节点分析法和混合方法。

### 1. 状态空间法（State-Space Method）

**基本形式** [Hairer 1993]：

$$
\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \quad \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}
$$

**离散化形式**（梯形积分）：

$$
\mathbf{x}_{n+1} = \mathbf{x}_n + \frac{\Delta t}{2}\left( \mathbf{f}(\mathbf{x}_n) + \mathbf{f}(\mathbf{x}_{n+1}) right)
$$

状态空间法的优势在于：积分规则可事后选择（便于变步长）、便于控制器设计接口、自动生成状态矩阵。但其计算瓶颈在于**状态矩阵的自动生成**耗时，且对频繁开关事件需要预计算大量开关组合的矩阵集 [Dufour 2011]。

**分段广义状态空间平均法（P-GSSA）** [王磊等 2019]：

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{d}, \mathbf{u}) \quad \text{其中 } \mathbf{d} = [d_a, d_b, d_c]^T \text{ 为占空比向量}
$$

P-GSSA将动作特性相近的若干开关周期合并为一个求解区间，在区间内用傅里叶系数描述状态变量，实现时间尺度上的自适应压缩。

### 2. 节点分析法（Nodal Analysis Method）

**节点导纳方程** [Dommel 1969]：

$$
\mathbf{G}\mathbf{v}(t) = \mathbf{i}(t) + \mathbf{i}_h(t)
$$

其中 $\mathbf{G}$ 为节点导纳矩阵，$\mathbf{i}_h$ 为历史电流源向量。离散伴随支路的等效导纳为 $G_{eq} = frac{2C}{Delta t}$（电容）和 $G_{eq} = frac{Delta t}{2L}$（电感）。

节点法的核心优势是稀疏矩阵求解效率高，适合大规模网络。固定步长下 $\mathbf{G}$ 不变，可预分解后重复使用。

**时域戴维南等值法**（Prony识别）[Ramos 2004]：

外部系统等值为若干一阶离散滤波支路的并联组合，每个模态实现为：

$$
v_n = R_{eq,i} \cdot i_n + V_{h,i,n-1}
$$

其中 $V_{h}$ 为历史电压源，通过Prony模态分解识别驱动点网络函数的留数和特征值。

### 3. 状态空间-节点混合法（SSN方法）

**核心思想** [Dufour 2011]：将任意规模的状态空间电气集群离散化后，作为类似节点法离散伴随支路的等效接口并入同一个节点导纳矩阵，实现状态空间子系统与节点网络的同步求解。

**V型SSN群（诺顿等值）**：

$$
\mathbf{i}_{h,k} = \mathbf{Y}_k \mathbf{v}_k + \mathbf{i}_{ext,k}
$$

**I型SSN群（戴维南等值）**：

$$
\mathbf{v}_{h,k} = \mathbf{Z}_k \mathbf{i}_k + \mathbf{v}_{ext,k}
$$

**混合型SSN群**：

$$
\begin{bmatrix} \mathbf{i}^I \\ \mathbf{i}^V \end{bmatrix} = \begin{bmatrix} \mathbf{Y}^{II} & \mathbf{Y}^{IV} \\ \mathbf{Y}^{VI} & \mathbf{Y}^{VV} \end{bmatrix} \begin{bmatrix} \mathbf{v}^I \\ \mathbf{v}^V \end{bmatrix} + \begin{bmatrix} \mathbf{i}_{ext}^I \\ \mathbf{i}_{ext}^V \end{bmatrix}
$$

SSN方法将状态空间集群以节点伴随等效形式接入全局导纳矩阵，同时利用节点法的大规模稀疏求解能力和状态空间法的分组建模、积分器选择及控制接口便利性。不同集群可并行求解（Step 3-6和Step 8可分配到独立CPU核心）[Dufour 2011]。

### 4. 指数分裂状态空间法（Splitting State-Space Method）

**核心思想** [Fu等 2025]：将状态矩阵分解为时变部分和常数部分，分别求解后组合，以回避整体矩阵指数运算。

**矩阵分裂**：

$$
\mathbf{A} = \mathbf{A}_1 + \mathbf{A}_2(t)
$$

其中 $\mathbf{A}_1$ 为常数分裂矩阵（开关状态无关），$\mathbf{A}_2(t)$ 为块级时变分裂矩阵（随开关状态变化）。通过自动开关分组和开关邻近状态变量识别（ SASV）定位最小子电路拓扑。

**一阶Trotter公式**：

$$
e^{h(\mathbf{A}_1 + \mathbf{A}_2)} = e^{h\mathbf{A}_1} e^{h\mathbf{A}_2} + O(h^2)
$$

**二阶对称公式**：

$$
e^{h(\mathbf{A}_1 + \mathbf{A}_2)} = e^{h\mathbf{A}_1/2} e^{h\mathbf{A}_2} e^{h\mathbf{A}_1/2} + O(h^3)
$$

Trotter公式将每个积分步骤分裂为两个子步骤：先用SASV识别的开关状态计算 $f_1(h\mathbf{A}_2(s(t_n)))$，再用常数阵 $\mathbf{A}_1$ 的预计算指数推进 $e^{h\mathbf{A}_1}$。

### 5. 半解析状态空间法

**核心思想** [Xiong等 2024]：从状态空间模型出发，用微分变换推导高阶半解析解，在每个时间段内用时间幂级数表示状态演化，使求解阶数和步长可在仿真中调整。

**局部时间幂级数**：

$$
\mathbf{x}(t) = \mathbf{x}_n + \sum_{k=1}^{N} c_k (t - t_n)^k
$$

系数 $c_k$ 通过递推计算得到。利用高阶项估计截断误差并自适应调整步长。对于开关或限值事件，先二分缩小含事件区间，再用二次插值估计事件时刻。

## 形式化表达

### 电力系统DAE方程组

$$
\begin{cases}
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{v}) & \text{设备动态} \\
\mathbf{0} = \mathbf{g}(\mathbf{x}, \mathbf{v}) & \text{网络代数}
\end{cases}
$$

### 离散时间状态空间

$$
\mathbf{x}_{n+1} = \mathbf{A}_d \mathbf{x}_n + \mathbf{B}_d \mathbf{u}_n
$$

### Z变换传递函数

$$
\mathbf{X}(z) = (z\mathbf{I} - \mathbf{A}_d)^{-1} \mathbf{B}_d \mathbf{U}(z)
$$

### 伴随电路等效导纳

| 元件 | 等效导纳 $Y_{eq}$ | 历史源项 |
|------|------------------|---------|
| 电容 $C$ | $frac{2C}{\Delta t}$ | $i_h = i_n + frac{2C}{\Delta t}v_n$ |
| 电感 $L$ | $frac{\Delta t}{2L}$ | $i_h = i_n + frac{\Delta t}{2L}v_n$ |
| 电阻 $R$ | $frac{1}{R}$ | 无历史源 |

## 关键技术挑战

### 挑战1：开关事件的数值处理

开关动作引入拓扑突变，传统方法需要对每个开关组合预生成矩阵集，导致内存爆炸。SSN方法通过状态空间集群分组减少预计算集数量——将系统分为两个群后，预计算集数从 $2^6 = 64$ 降至 $2^3 + 2^3 = 16$（三相系统示例）[Dufour 2011]。

### 挑战2：快慢时间尺度耦合

电力电子设备的时间常数跨度极大（IGBT关断 $\mu$s级 vs 机电动态 s级）。多时间尺度问题的核心困难在于数值刚性（stiffness）——隐式积分法需要求解非线性方程组，显式法受稳定性限制步长。

### 挑战3：大规模系统的稀疏矩阵求解

节点导纳矩阵的规模随系统节点数增长，LU分解的时间复杂度为 $O(n^3)$，稀疏矩阵技术（度MD等）可将复杂度降至接近 $O(n)$。实时仿真要求在固定步长内完成求解，对硬件性能要求严苛。

### 挑战4：数值阻尼与振荡控制

梯形法在传输线等分布参数模型中可能引入数值振荡（一级LC电路中 $x_{n+1} = x_n + \Delta t \cdot f(x_n)$ 的能量守恒误差累积）。后向欧拉法提供数值阻尼（能量耗散），但精度较低。

### 挑战5：状态矩阵指数的高效计算

指数分裂法回避了 $O(N^3)$ 的矩阵指数运算，但分裂阶数的选择需要在精度和效率之间权衡。文献 [Fu等 2025] 报告：二阶分裂公式在相同步长下误差比一级公式降低约一个数量级，同时计算开销仅增加约30%。

## 量化性能边界

### 时间步长范围

| 仿真类型 | 典型步长 | 适用场景 |
|---------|---------|---------|
| 开关细节EMT | 1-10 μs | 电力电子换流器、故障暂态 |
| 中等步长EMT | 10-100 μs | 传输线操作、HVDC |
| 长时间EMT | 100 μs - 1 ms | 机电暂态、谐波 |
| 实时EMT | ≤ 50 μs | 硬件在环（HIL）、控制器测试 |

### 性能指标

| 指标 | 典型范围 | 说明 |
|------|---------|------|
| 仿真精度 | 误差 < 1% | 与详细开关模型对比 |
| 计算效率 | 10-1000节点/s | 取决于系统规模和数值方法 |
| 内存占用 | 随系统规模线性增长 | 稀疏矩阵存储 |
| 实时步长约束 | ≤ 50 μs (RT-HIL) | 硬件在环测试要求 |

### 方法效率对比（定性）

| 方法 | 矩阵计算 | 开关处理 | 控制接口 | 并行潜力 |
|------|---------|---------|---------|---------|
| 纯节点法 | 高效（稀疏矩阵） | 需重建拓扑 | 较差 | 中等 |
| 纯状态空间法 | 需全量生成 | 预计算爆炸 | 优秀 | 低 |
| SSN混合法 | 中等（分块） | 分组减少 | 优秀 | 高 |
| 指数分裂法 | 回避矩阵指数 | 自适应分裂 | 中等 | 高 |
| 半解析法 | 高阶多项式 | 事件检测精确定位 | 中等 | 中 |

## 适用边界与选择指南

### 何时使用时域建模

- 需要详细波形信息（过电压峰值、谐波含量）
- 非线性/开关效应显著（变压器饱和、PWM调制）
- 控制系统与网络强耦合（闭环控制器测试）
- 故障、雷击等快速暂态过程

### 时域建模的失效场景

| 失效场景 | 原因 | 替代方法 |
|---------|------|---------|
| 长时仿真（数秒以上） | 计算量随时间线性累积 | 动态相量法、频域谐波潮流 |
| 刚性系统（多时间尺度差异 > 10^6） | 数值稳定性要求极小步长 | 多速率EMT、降阶模型 |
| 大规模系统（> 10000节点）实时 | 计算资源需求过高 | 网络等值、分群并行 |
| 高频振荡（开关频率 > 100 kHz） | 数值阻尼不足引入伪振荡 | 频域分析、专用开关模型 |
| 稳态谐波计算 | 需FFT后处理，效率低 | 频域谐波潮流 |

### 方法选择决策表

| 需求场景 | 推荐方法 |
|---------|---------|
| 大规模网络 + 控制器接口 | SSN混合法 [Dufour 2011] |
| 高开关频率变流器（如MMC） | 指数分裂法 [Fu 2025] |
| 变步长 + 误差自适应控制 | 半解析状态空间法 [Xiong 2024] |
| 周期性PWM变流器快速仿真 | P-GSSA [王磊等 2019] |
| 外部系统等值（黑箱阻抗） | Prony时域识别法 [Ramos 2004] |
| 通用大规模网络高效仿真 | 节点分析法 + 稀疏矩阵 |

## 相关方法

| 类别 | 页面 | 说明 |
|------|------|------|
| 数值积分 | [[trapezoidal-rule]]、[[backward-euler]]、[[runge-kutta-in-emt]] | EMT核心数值方法 |
| 求解框架 | [[state-space-method]]、[[nodal-analysis]] | 两大求解范式 |
| 数值稳定性 | [[numerical-damping-optimization]]、[[numerical-integration-error]] | 阻尼与误差控制 |
| 混合仿真 | [[electromechanical-electromagnetic-hybrid-simulation]]、[[multirate-and-network-partitioning]] | 多时间尺度处理 |
| 频域对比 | [[frequency-domain-analysis]]、[[dynamic-phasor]] | 与频域方法的互补 |
| 加速方法 | [[parallel-computing]]、[[real-time-simulation]] | 大规模/实时加速 |

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] (Dufour, Mahseredjian, Bélanger) | 2011 | 提出SSN方法，状态空间集群与节点法同步求解 |
| [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation]] (Xiong等) | 2024 | 半解析状态空间方法，高阶局部幂级数变步长 |
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo]] (Ramos等) | 2004 | Prony时域网络等值，离散戴维南滤波器 |
| [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti]] (王磊等) | 2019 | P-GSSA分段广义状态空间平均模型 |
| Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations (Fu等) | 2025 | 指数分裂法回避矩阵指数，自适应误差控制 |

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*