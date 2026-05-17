---
title: "伴随电路 (Companion Circuit)"
type: method
tags: [companion-circuit, nodal-analysis, discretization, emtp, trapezoidal-rule, numerical-integration]
created: "2026-05-02"
updated: "2026-05-10"
---


# 伴随电路 (Companion Circuit)

## 1. 物理背景与工程需求

### 为什么需要伴随电路？

EMT 仿真是在数字计算机上模拟电力系统的电磁暂态过程。但计算机本质上只能处理**代数方程**，而电路中的动态元件（电感、电容）是由**微分方程**描述的。伴随电路就是连接这两者的桥梁。

核心逻辑链：

```text
连续时间系统（微分方程）
    ↓ 数值积分（离散化）
离散时间系统（差分方程）
    ↓ 电路等效转化
伴随电路（诺顿等效：电导 + 历史电流源）
    ↓ 装配
节点方程 Y_n · v = i（纯代数方程组）
```

伴随电路把微分关系等价成了时步内的代数关系，使得全局求解退化为纯代数问题。整个仿真只需在每个时步求解一次线性方程组。

### 与节点分析的关系

伴随电路是 [[nodal-analysis]] 在 EMT 中发挥作用的前提。节点分析要求所有元件都能表示为诺顿等效（导纳 + 电流源）。固定电阻本身就是诺顿等效；但动态元件需要经过伴随电路转化才能纳入节点分析框架。

两者分工明确：

- **伴随电路**：负责每个元件的离散化（具体如何把微分方程变成代数方程）
- **节点分析**：负责全局组装（把所有元件的代数方程组合成系统方程组并求解）

这也解释了为什么 EMTP 类程序采用"元件-接口-求解"三层分离架构：伴随电路就是那个**接口层**，每个新元件只需实现自己的伴随电路接口就可以接入现有求解器。


## 2. 数学描述

### 核心思想：数值积分离散化

一个动态元件由微分方程描述。数值积分的作用就是把这个微分方程在时刻 $t_k$ 离散为差分方程。而伴随电路把这个差分方程重新解释为一个**等效电路**。

最关键的一点：无论用什么积分公式，离散后的结果都可以写成统一形式：

$$
i_k = G_{eq} v_k + I_{hist}
$$

这是一个**诺顿等效电路**：一个电导 $G_{eq}$（只与元件参数和步长有关）和一个电流源 $I_{hist}$（包含了上一时刻的历史信息）并联。

### 电感的伴随电路

电感方程：

$$
v_L(t) = L \frac{di_L(t)}{dt}
$$

用梯形法在 $t_k$ 时刻离散（从 $t_{k-1}$ 积分到 $t_k$）：

$$
i_k = i_{k-1} + \frac{1}{L} \int_{t_{k-1}}^{t_k} v(\tau) d\tau \approx i_{k-1} + \frac{\Delta t}{2L}(v_k + v_{k-1})
$$

整理成 $i_k = G_{eq} v_k + I_{hist}$ 的形式：

$$
i_k = \frac{\Delta t}{2L} v_k + \left(i_{k-1} + \frac{\Delta t}{2L} v_{k-1}\right)
$$

其中：

$$
G_{eq,L} = \frac{\Delta t}{2L}, \quad I_{hist,L}^{k-1} = i_{k-1} + G_{eq,L} v_{k-1}
$$

### 电容的伴随电路

电容方程：

$$
i_C(t) = C \frac{dv_C(t)}{dt}
$$

同样用梯形法离散：

$$
i_k = \frac{2C}{\Delta t} v_k - \left(\frac{2C}{\Delta t} v_{k-1} + i_{k-1}\right)
$$

其中：

$$
G_{eq,C} = \frac{2C}{\Delta t}, \quad I_{hist,C}^{k-1} = -\left(G_{eq,C} v_{k-1} + i_{k-1}\right)
$$

注意电容的历史电流源比电感多了一个负号。这是因为梯形法离散时积分方向不同造成的——但这个负号在编程实现时很容易漏掉，是常见的 bug 来源。

### 两种积分公式的对比

用后向欧拉替代梯形法，会得到不同形式的等效电导：

$$
\begin{array}{c|cc}
\text{元件} & \text{梯形法 } G_{eq} & \text{后向欧拉 } G_{eq} \\ \hline
\text{电感} & \Delta t/2L & \Delta t/L \\
\text{电容} & 2C/\Delta t & C/\Delta t \\
\end{array}
$$

后向欧拉的等效电导更大（导纳更大、阻抗更小），这带来了更强的**数值阻尼**——能够在开关突变后快速衰减非物理振荡。代价是精度从 $O(\Delta t^2)$ 降为 $O(\Delta t)$。


## 3. 计算模型与离散化

### 等效电导的恒定性与矩阵复用

观察 $G_{eq}$ 的表达式：

- 电感：$G_{eq,L} = \Delta t/(2L)$，只取决于电感值和步长
- 电容：$G_{eq,C} = 2C/\Delta t$，只取决于电容值和步长

这意味着：**如果步长不变，所有动态元件的等效电导在整个仿真过程中保持不变**。进而，节点导纳矩阵 $Y_n$ 也保持不变，只需做一次 LU 分解，之后每步只做前代回代。

这种"一次分解、多步复用"的策略是 EMTP 类程序高效运行的根本原因。

### 历史电流源的更新

虽然等效电导不变，但历史电流源 $I_{hist}$ 每个时步都要更新。更新需要用到上一时步的状态量（$v_{k-1}$ 和 $i_{k-1}$），所以求解完当前时步后必须保存这些值。

对于电感：

$$
I_{hist,L}^{k} = i_k + G_{eq,L} v_k
$$

对于电容：

$$
I_{hist,C}^{k} = -(G_{eq,C} v_k + i_k)
$$

### 一个时步的完整流程

```text
时刻 t_k 开始：
  1. 读取上一时步保存的状态量 (v_{k-1}, i_{k-1})
  2. 计算各元件的 I_hist（用上一步公式）
  3. 组装右端向量 i_k（独立源 + 历史源）
  4. 求解 Y_n · v_k = i_k（若 Y_n 不变则只需前代回代）
  5. 从 v_k 回代计算各支路电流
  6. 保存状态量 (v_k, i_k) 供下一时步使用
时刻 t_{k+1} 继续
```

### 推广到其他元件

伴随电路的核心思想——"微分关系 → 诺顿等效"——不只适用于 L 和 C。以下元件的 EMT 建模也基于同样的思路：

- **Bergeron 线路模型**：传输线方程的解可以用特性导纳 $Y_c = 1/Z_c$ 加延时历史源表示
- **频变线路模型**：通过矢量拟合将频域导纳表示为有理函数，每个极点-留数对贡献一个递推历史源
- **状态空间集群**：将局部系统的状态空间模型离散化，形成多端口诺顿等效
- **非线性元件**：牛顿迭代中每一步用增量电导 + 等效电流源线性化

所有这些方法的核心都是"在元件层面把微分/复杂关系转换成统一接口的诺顿等效"，然后装配到全局节点方程中统一求解。


## 4. 实现方法与算法细节

### 装配到节点方程

对连接在节点 $p$ 和 $q$ 之间的等效电导 $G_{eq}$：

$$
Y_{pp} \mathrel{+}= G_{eq}, \quad Y_{qq} \mathrel{+}= G_{eq}, \quad Y_{pq} \mathrel{-}= G_{eq}, \quad Y_{qp} \mathrel{-}= G_{eq}
$$

历史电流源 $I_{hist}$ 注入到右端向量 $i$ 的对应节点位置。

### 开关事件的处理

开关动作是伴随电路最容易出错的场景。当开关状态变化时：

1. **若使用变导纳模型**：开关的电导值变化 → $Y_n$ 改变 → 需要重新 LU 分解
2. **若使用恒导纳模型**：$Y_n$ 不变，但需要通过补偿法或插值修正历史源

无论哪种方式，历史源的修正都是关键：开关动作发生在时步内部，但程序只在时步边界处理。用旧拓扑下的历史源去解新拓扑的方程，会产生非物理能量。

工程实践中常用的处理手段：

- **CDA 算法**：检测到突变后，将梯形法切换为后向欧拉一步，利用后向欧拉的数值阻尼快速衰减振荡
- **插值定位**：通过插值找到开关动作的确切时刻，减小事件时间误差
- **重初始化**：突变后重新初始化历史源，切断错误能量

### 数值振荡的机理

梯形法在理论上是 A-稳定的，但它的 A-稳定边界恰好落在虚轴上。这意味着：理想开关的瞬间开断会产生一个高频分量，梯形法无法有效衰减这个分量，于是表现为电压/电流波形上的交替振荡。

后向欧拉是 L-稳定的，能快速衰减高频分量，所以通常作为"救火队员"在突变后临时切换使用。


## 5. 适用边界与失效模式

### 什么条件下好用？

- 系统大部分元件是线性的 L、C、R（可用恒定 $G_{eq}$ 表示）
- 步长相对于系统最快暂态足够小（梯形法二阶精度能充分发挥）
- 开关事件频率低（避免频繁重新分解 $Y_n$）

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 开关后数值振荡 | 电压/电流波形出现交替高频毛刺 | 梯形法无法有效阻尼突变产生的高频分量 | CDA 算法或后向欧拉切换 |
| 历史源不匹配 | 开关动作后解出错误电压 | 新拓扑下使用了旧拓扑的历史源 | 重初始化或插值定位 |
| 矩阵病态 | 求解结果精度丧失 | 开关开态/关态电导比太大或太小 | 保持比值在 $10^4\sim10^6$ |
| 步长过大 | 精度下降，甚至不稳定 | 梯形法在刚性系统中对大步长敏感 | 使用 L-稳定的积分公式（后向欧拉、Gear-2） |
| 状态量更新顺序错误 | 历史源使用了错误的状态量 | 求解后没有正确保存 v_k 和 i_k | 严格遵循"先更新历史源 → 求解 → 再保存状态"的顺序 |

### 工程经验值

- 梯形法是 EMT 的默认选择，CDA 作为安全网
- 开关电导比推荐 $10^5$ 左右：太大恶化条件数，太小漏电流过大
- 恒导纳模型中，非线性和开关通过补偿/诺顿等效修正，不做矩阵重分解


## 6. 一个简单的数值算例

考虑 RL 串联电路：电阻 $R=10\Omega$，电感 $L=50\text{mH}$，电压源 $V_s=100\text{V}$（阶跃输入 $t=0$ 时接通）。

**参数计算**（取 $\Delta t = 1\text{ms}$）：

$$
G_{eq,L} = \frac{\Delta t}{2L} = \frac{0.001}{2 \times 0.05} = 0.01 \text{ S}
$$

**节点方程**（只有一个独立节点）：

$$
\left(\frac{1}{R} + G_{eq,L}\right) v(t_k) = \frac{V_s}{R} + I_{hist}^{k-1}
$$

其中 $I_{hist}^{k-1} = i_{k-1} + G_{eq,L} v_{k-1}$。初始条件 $i(0)=0$。

**迭代步骤**（以第一时步为例）：

- $t=0$：$v(0)=0$，$i(0)=0$，由初始条件
- $t=1\text{ms}$：$I_{hist} = i(0) + G_{eq} \cdot v(0) = 0$，求解节点方程得 $v(1\text{ms})$，然后回代得 $i(1\text{ms})$
- 之后每步用新算出的 $v_k$、$i_k$ 更新 $I_{hist}$，重复求解

**解析对比**：该电路的电流解析解为 $i(t) = \frac{V_s}{R}(1 - e^{-Rt/L}) = 10(1 - e^{-200t})$。如果用四阶 RK 法或足够小的步长（$\Delta t = 1\mu\text{s}$）逼近这个解析解，梯形法伴随电路在 $\Delta t = 1\text{ms}$ 时的误差应在数个百分点以内。读者可以用 MATLAB 或 Python 自行验证。

注意：这个算例中没有开关突变，所以不会出现数值振荡。实际仿真中如果加入 PWM 开关或故障切除，需要在事件点启用 CDA 或插值处理。


## 7. 延伸阅读

### 核心参考文献

- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — 伴随电路离散策略的系统比较，对比梯形法、后向欧拉、Gear-2 的精度和稳定性
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] — 将状态空间集群的伴随电路推广到多端口诺顿等效
- [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us]] — MMC 子模块的伴随电路建模，Schur 补消去内部节点
- [[accurate-time-domain-simulation-of-power-electronic-circuits]] — 功率电子电路的伴随电路实现，事件定位与历史源修正
- [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss]] — Bergeron 线路模型作为伴随电路的一种形式

### 相关页面

- [[nodal-analysis]] — 伴随电路装配的目标框架
- [[fixed-admittance]] — 保持导纳矩阵不变的策略
- [[numerical-oscillation-suppression]] — 数值振荡的抑制方法
- [[trapezoidal-rule]] — 梯形积分公式的详细分析
- [[backward-euler]] — 后向欧拉的数值特性

## 来源论文

| 论文 | 年份 |
|------|------|
| [[mode-domain-multiphase-transmission-line-model-use-in-transient-studies-power-de.md]] | 2004 |
| [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat.md]] | 2006 |
| [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation.md]] | 2007 |
| [[frequency-adaptive-power-system-modeling-for.md]] | 2009 |
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient.md]] | 2011 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl.md]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines.md]] | 2011 |
| [[a-type-4-wind-power-plant-equivalent-model.md]] | 2012 |
| [[development-of-data-translators-for-interfacing-13&14.md]] | 2013 |
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies.md]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation.md]] | 2016 |
| [[30tpwrd20172714639-2.md]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-.md]] | 2017 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende.md]] | 2019 |
| [[fpga-based-sub-microsecond-level-real-time-simulation-for-microgrids-with-a-netw.md]] | 2020 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir.md]] | 2021 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients.md]] | 2022 |
| [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte.md]] | 2022 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete.md]] | 2023 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-.md]] | 2023 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech.md]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-.md]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us.md]] | 2023 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large.md]] | 2024 |
| [[a-julia-based-simulation-platform-for-power-system-transients.md]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab.md]] | 2025 |
| [[partial-refactorization-techniques-for-electromagnetic-transient-simulations.md]] | 2025 |
