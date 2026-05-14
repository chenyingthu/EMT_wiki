---
title: "指数积分器 (Exponential Integrator)"
type: method
tags: [exponential-integrator, numerical-integration, state-space, gpu, parallel-computation, stability, matrix-exponential, phi-function, l-stability]
created: "2026-05-10"
updated: "2026-05-14"
---

# 指数积分器 (Exponential Integrator)

## 定义

指数积分器（Exponential Integrator, EI）是一类利用矩阵指数函数 $e^{Ah}$ 及其 $\varphi$ 函数精确积分线性部分的数值积分方法。对线性状态空间方程 $\dot{x} = Ax + Bu$，指数积分器将线性部分的齐次解以矩阵指数形式精确解析求解，仅对输入项 $Bu$ 的卷积积分做数值近似。与传统 EMTP 积分器（梯形法、后向欧拉、Gear 法）逐点迭代推进不同，指数积分器通过解析处理系统矩阵的刚性模态，在较大步长下仍保持数值稳定性，且天然具备 L 稳定性——即对任意步长和系统刚性程度，数值解均单调收敛，无数值振荡。

指数积分器在 EMT 仿真中的独特价值体现在三个方面：(1) 对刚性电力电子系统，L 稳定性保证大步长下无数值振荡；(2) 矩阵指数运算可分解为规则矩阵-向量操作，天然适配 GPU SIMT 并行架构；(3) 矩阵指数和 $\varphi$ 函数可在拓扑不变时预计算，大幅降低主循环在线计算负载。

相关方法：[[state-space-method]]（状态空间建模基础）；[[numerical-integration]]（传统积分方法对比）；[[gpu-accelerated-simulation]]（GPU 并行加速实现）；[[companion-circuit]]（传统 EMTP 伴随电路法）；[[stiff-system-handling]]（刚性系统处理策略）。

## EMT 中的角色

在 EMT 仿真中，指数积分器承担以下关键角色：

1. **刚性电力电子系统的稳定积分器**：含高频开关的变流器网络具有极强的刚性（特征值实部可达 $-10^6 \sim -10^8$），传统 A 稳定方法（如梯形法）虽然理论上无条件稳定，但在开关事件处会产生数值振荡（numerical ringing）。指数积分器因具备 L 稳定性，可完全消除此类振荡。

2. **大步长高精度积分**：高阶指数积分器（如 (3,3) Padé 近似，6 阶精度）在相同步长下精度远高于 2 阶梯形法。对于仅含直流输入源的电力电子电路，强迫函数项为零，矩阵指数给出精确解，截断误差为零。

3. **GPU 并行加速的算子基础**：矩阵指数 $e^{Ah}$ 和 $\varphi_k(hA)$ 的计算可分解为稀疏矩阵-向量乘法和 $\varphi$ 函数与向量的乘法，均可映射到 GPU SIMT 架构，实现跨时间步并行（parallel-rate）和步内运算并行的双重加速。

4. **开关事件驱动仿真的核心算子**：在离散状态事件驱动（DSED）框架中，指数积分器的矩阵指数可在每个开关拓扑切换时预计算，主循环仅做矩阵-向量乘法和 $\varphi$ 项组合，计算复杂度从 $O(N^3)$ 降为 $O(N^2)$ 级别。

## 核心机制

### 线性系统的精确解

对线性时不变状态空间方程

$$
\dot{x}(t) = Ax(t) + Bu(t)
$$

其精确解为

$$
x(t_0 + h) = e^{Ah}x(t_0) + \int_0^h e^{A(h-\tau)}Bu(t_0+\tau)\,d\tau
$$

其中 $e^{Ah}$ 是矩阵指数算子。线性部分的动态被精确积分，唯一近似来自输入 $u(t)$ 在积分区间内的变化近似。此公式是指数积分器的基石：对电力电子系统，每个开关拓扑对应一组 $(A_k, B_k)$，在拓扑不变期间，$e^{A_k h}$ 为常数。

### $\varphi$ 函数与强迫函数展开

为数值实现输入积分项，引入 $\varphi$ 函数族：

$$
\varphi_0(z) = e^z, \quad \varphi_1(z) = \frac{e^z - 1}{z}, \quad \varphi_k(z) = \frac{\varphi_{k-1}(z) - \varphi_{k-1}(0)}{z}
$$

对输入 $u(t)$ 在步长内为常数的情形（电力电子系统最常见的情况），积分项可简洁表示为：

$$
x_{n+1} = e^{Ah}x_n + h\varphi_1(hA)Bu_n
$$

对输入为多项式或分段常数的更一般情形，强迫函数项展开为 $\varphi$ 函数与输入导数的组合：

$$
x_{n+1} = e^{Ah}x_n + \sum_{j=0}^{p} h^{j+1}\varphi_{j+1}(hA)B^{(j)}u_n
$$

其中 $p$ 为强迫函数展开阶数，$B^{(j)}$ 为输入导数项。在 Paull 2025 提出的 AGEI 算法中，通过自适应调整 $p$ 的值来满足误差阈值，在精度和计算量之间动态平衡。

$\varphi$ 函数的数值计算可采用递归公式或 Taylor 级数展开：

$$
\varphi_j(z) = \sum_{k=0}^{\infty} \frac{z^k}{(k+j)!}
$$

### 矩阵指数的数值计算

矩阵指数 $e^{Ah}$ 的计算是指数积分器的核心瓶颈。常用方法包括：

**Padé 有理逼近**：将矩阵指数近似为有理函数

$$
e^{z} \approx r_{km}(z) = \frac{p_k(z)}{q_m(z)}
$$

其中 $k$ 为分子阶数，$m$ 为分母阶数。对角 Padé 逼近 $(k,k)$ 的局部误差为 $O(h^{2k+1})$。例如，(3,3) Padé 逼近为 6 阶精度，是指数积分器中常用的高阶选项。

**缩放与平方法（Scaling and Squaring）**：对 $e^{A}$，先选择 $s$ 使 $\|A/2^s\| < 1$，计算 $e^{A/2^s}$ 的 Padé 逼近，然后平方 $s$ 次恢复：$e^A = (e^{A/2^s})^{2^s}$。此方法数值稳定性好，是 MATLAB `expm` 和 Li 2020 中 dense output 的基础。

### 并行率（Parallel-Rate）计算

高阶指数积分器的核心优势在于跨时间步并行：由于 $e^{Ah}$ 在拓扑不变时不变，多个离散步的状态更新可同时计算。对 $k$ 个并行步（Paull 2026）：

$$
\begin{bmatrix} x_{n+1} \\ x_{n+2} \\ \vdots \\ x_{n+k} \end{bmatrix} =
F\left( \begin{bmatrix} x_n \\ x_{n+1} \\ \vdots \\ x_{n+k-1} \end{bmatrix} \right)
$$

宏观时间维度上并行计算多个离散时间步的状态更新，微观步内维度上并行化矩阵-向量运算，形成双重并行加速。

### 分裂指数积分（Splitting EI）

当系统矩阵可分解为 $A = A_1 + A_2(s)$（$A_1$ 为常数部分，$A_2$ 为开关相关时变部分），指数分裂公式将矩阵指数近似为：

**一阶 Trotter 公式**：

$$
e^{h(A_1+A_2)} \approx e^{hA_1}e^{hA_2}
$$

**二阶 Strang 分裂**：

$$
e^{h(A_1+A_2)} \approx e^{\frac{h}{2}A_1}e^{hA_2}e^{\frac{h}{2}A_1}
$$

**高阶分裂公式**（Fu 2025）：

$$
e^{h(A_1+A_2)} \approx \prod_{i=1}^{m} e^{\alpha_i h A_1}e^{\beta_i h A_2}
$$

其中系数 $\alpha_i, \beta_i$ 根据所需精度阶数确定。常数部分 $e^{hA_1}$ 可复用，开关相关部分仅在拓扑变化时更新。

## 分类与变体

### 指数 Euler 公式

一阶格式，结构最简单：

$$
x_{n+1} = x_n + h\varphi_1(hA)(Ax_n + g_n)
$$

其中 $g_n$ 包含非线性和控制项。计算核主要为稀疏矩阵-向量乘法和 $h\varphi_1(hA)$ 与向量的乘法，均可映射到 GPU SIMT 架构。

### 高阶 Padé 逼近指数积分

使用 (p, q) 阶 Padé 逼近计算矩阵指数，精度为 $O(h^{p+q+1})$。Paull 2025 中采用 (3,3) Padé 逼近，达到 6 阶离散精度。Li 2020 提出 MEXP 方法，通过灵活选择 Padé 阶数 $(k,m)$ 控制精度，实现变量阶积分。

### 自适应步长指数积分（AGEI）

Paull 2025 提出的 AGEI 算法将指数积分嵌入 DSED 框架：(1) 对"仔细选择的离散化步长"预计算矩阵指数和 $\varphi$ 函数；(2) 在开关事件之间用可查表的中间步长顺序积分；(3) 通过自适应调整强迫函数项数 $p$ 满足误差阈值。AGEI 是变步长、固定高阶、变强迫函数项数的 ODE 求解器。

### 分裂状态空间指数积分

Fu 2025 提出的分裂方法通过自动开关分组和 SASV（Switch Adjacent State Variables）识别，定位最小的开关状态相关子电路，将状态矩阵分解为常数部分 $A_1$ 和开关相关时变部分 $A_2(s)$，使用多阶指数分裂公式组合求解。

### 并行率指数积分（Parallel-Rate EI）

Paull 2026 提出的 multi-granular GPU parallel-rate EI 算法：(1) 在 GPU 上预计算矩阵指数和 $\varphi$ 函数；(2) 跨时间步并行生成多个离散输出步；(3) 在每个时间步内并行化矩阵-向量运算；(4) 将求解器应用于无源/二极管开关事件检测。

## 形式化表达

### 核心公式汇总

| 符号 | 含义 | 公式 |
|------|------|------|
| $e^{Ah}$ | 矩阵指数算子 | $e^{Ah} = \sum_{k=0}^{\infty} \frac{(Ah)^k}{k!}$ |
| $\varphi_k(z)$ | $\varphi$ 函数族 | $\varphi_k(z) = \frac{\varphi_{k-1}(z) - \varphi_{k-1}(0)}{z}$ |
| $r_{km}(z)$ | Padé $(k,m)$ 有理逼近 | $e^z \approx \frac{p_k(z)}{q_m(z)}$ |
| $x_{n+1}$ | 一步更新（常数输入） | $x_{n+1} = e^{Ah}x_n + h\varphi_1(hA)Bu_n$ |
| $x_{n+1}$ | 一步更新（多项式输入） | $x_{n+1} = e^{Ah}x_n + \sum_{j=0}^{p} h^{j+1}\varphi_{j+1}(hA)B^{(j)}u_n$ |
| $e^{h(A_1+A_2)}$ | 一阶 Trotter 分裂 | $\approx e^{hA_1}e^{hA_2}$ |
| $e^{h(A_1+A_2)}$ | 二阶 Strang 分裂 | $\approx e^{\frac{h}{2}A_1}e^{hA_2}e^{\frac{h}{2}A_1}$ |

### 稳定性定义

对测试方程 $\dot{x} = \lambda x$，指数积分器的数值解为 $x_{n+1} = \Phi(h\lambda)x_n$，其中 $\Phi(z)$ 为稳定函数。稳定性区域定义为：

$$
R = \{ z \in \mathbb{C} : |x_{n+1}| < |x_n| \}
$$

- **A 稳定**：稳定性区域包含整个左半平面，即 $\forall \text{Re}\{\lambda\} < 0, |x_{n+1}| < |x_n|$
- **L 稳定**：在 A 稳定基础上，衰减速度随 $\text{Re}\{\lambda\}$ 更负而增加，即 $\lim_{\text{Re}\{\lambda\}\to-\infty} |\Phi(h\lambda)| = 0$

指数积分器的稳定函数为 $\Phi(z) = r_{km}(z) + \text{forcing terms}$。对于齐次方程（forcing terms = 0），指数积分器的稳定函数等于 Padé 逼近 $r_{km}(z)$。对角 Padé 逼近 $(k,k)$ 是 L 稳定的，因为 $\lim_{z\to-\infty} r_{kk}(z) = 0$。

### 稠密输出公式（Dense Output）

Li 2020 提出的稠密输出公式基于缩放与平方法，在计算 $e^{hA}$ 的同时获得 $2^s - 1$ 个内部点的输出：

$$
x\left(t_0 + \frac{h}{2^s}i\right) = \left[I_n \quad 0\right] \cdot e^{2^{s-i}hA} \cdot \begin{bmatrix} x_0 \\ 0 \end{bmatrix}, \quad i = 0, 1, \ldots, 2^s - 1
$$

稠密输出复用缩放与平方法的中间计算结果，无额外代价。这些内部点等价于反复减半步长的仿真结果，精度不低于原始 $x(t_0+h)$。

## 关键技术挑战

### 矩阵指数计算复杂度

矩阵指数 $e^{Ah}$ 的计算复杂度为 $O(N^3)$，其中 $N$ 为系统状态维度。对于大规模电力系统，这是主要计算瓶颈。Fu 2025 的分裂方法通过限制时变矩阵维度来缓解此问题：仅对开关相关的最小子电路计算矩阵指数，常数部分复用。

### 开关事件检测与插值精度

Li 2020 分析指出，对于含开关事件的 EMT 仿真，开关时刻的插值精度是全局精度的瓶颈。当无开关事件时，矩阵指数方法（MEXP）可达 6 阶精度；但当存在开关事件时，线性插值会导致全局精度降至 $O(h^2)$。稠密输出公式和高阶插值可缓解此问题。

### 预计算内存管理

Wu 2020 指出，GPU 上缓存矩阵指数可避免重复计算，但开关组合数量可能极大。缓存命中率（文献中报告 80-90%）和缓存替换策略直接影响仿真效率和显存占用。缓存管理策略需在速度收益和显存容量之间折中。

### 刚性与非刚性系统的统一处理

AGEI 算法（Paull 2025）的核心优势在于统一处理刚性和非刚性系统：L 稳定性保证刚性系统稳定，而自适应强迫函数项数使非刚性系统在大步长下仍保持高精度。对于仅含直流输入的系统，强迫函数项为零，矩阵指数给出精确解。

## 量化性能边界

| 来源 | 指标 | 数值 | 场景 |
|------|------|------|------|
| Paull 2025 (AGEI) | 相对 Simulink 加速比 | > 8× | 典型电力电子变换器（DC 输入） |
| Paull 2025 (AGEI) | 相对 PLECS 加速比 | > 3× | 典型电力电子变换器 |
| Paull 2025 (AGEI) | 相对 Simulink ode15s 加速比 | 5× | 极刚性系统（含 RC 共模电路） |
| Paull 2025 (AGEI) | 相对 PLECS DOPRI 加速比 | 3× | 极刚性系统 |
| Paull 2025 (AGEI) | 整体相对误差 | 2.34×10⁻⁷ | DC 输入变换器（vs 0.1μs Simulink 参考） |
| Paull 2025 (AGEI) | 离散阶数 | 6 阶 (3,3) Padé | 固定高阶 |
| Paull 2026 (Parallel-Rate EI) | 并行粒度 | 跨时间步 + 步内双重并行 | GPU SIMT |
| Wu 2020 (GPU Matrix Exp.) | 缓存命中率 | 80-90% | 风电场变流器仿真 |
| Li 2020 (MEXP) | 无开关事件精度 | 6 阶 | 相比 EMTP/PSCAD 的 2 阶 |
| Li 2020 (MEXP) | 稠密输出内部点数 | $2^s-1$ 个 | 复用缩放平方法中间结果 |

> 注：Paull 2025 的加速数据来自 MATLAB 实现，C++ 实现可进一步放大加速比。Fu 2025 的加速倍数在原文片段中未给出可核验数值，此处仅列出方法结构优势。

## 适用边界与选择指南

### 适用场景

| 场景 | 推荐程度 | 说明 |
|------|----------|------|
| 刚性电力电子变换器仿真 | ★★★★★ | L 稳定性保证大步长无振荡，AGEI 加速 >8× |
| 仅含直流输入源的变换器 | ★★★★★ | 强迫函数项为零，矩阵指数给出精确解 |
| GPU 并行离线仿真 | ★★★★★ | 矩阵-向量运算天然适配 GPU SIMT |
| 含高频开关的变流器网络 | ★★★★ | 开关事件间大步长积分，减少无效计算点 |
| 大规模风电场/新能源场站 | ★★★★ | Wu 2020 验证含电力电子接口风电机组的 GPU 加速 |
| 二极管/无源开关事件检测 | ★★★ | Paull 2026 验证 parallel-rate EI 可用于事件定位 |

### 不适用场景

| 场景 | 原因 |
|------|------|
| 实时硬件在环仿真 | 矩阵指数预计算开销大，不适合硬实时约束 |
| 强非线性器件（饱和磁件、电弧） | 指数积分仅精确处理线性部分，非线性需迭代求解 |
| 极大规模电网（>10000 节点） | $O(N^3)$ 矩阵指数计算成为瓶颈，需结合稀疏化或分裂方法 |
| 含复杂保护逻辑的系统 | 保护动作逻辑不在状态空间方程中，需额外处理 |

### 方法选择决策

- **需要极高精度且步长可接受** → 高阶指数积分（(3,3) Padé，6 阶）
- **GPU 并行加速** → Parallel-Rate EI（Paull 2026）或 GPU 缓存矩阵指数（Wu 2020）
- **大规模变流器网络** → 分裂状态空间指数积分（Fu 2025），限制时变矩阵维度
- **变步长 + 自适应精度** → AGEI（Paull 2025），DSED 框架 + 自适应强迫函数项数
- **需要稠密输出（事件间插值）** → MEXP + 稠密输出公式（Li 2020）

## 相关方法
- [[state-space-method]] — 指数积分的基础建模框架
- [[numerical-integration]] — 传统积分方法（梯形法、后向欧拉、Gear 法）对比
- [[gpu-accelerated-simulation]] — GPU 并行加速实现
- [[companion-circuit]] — 传统 EMTP 伴随电路方法
- [[stiff-system-handling]] — 刚性系统处理策略

## 相关模型
- [[power-electronics-modeling]] — 电力电子变换器开关级模型
- [[dfig-model]] — 大规模风电场 EMT 模型

## 相关主题
- [[parallel-computing]]
- [[numerical-integration-methods]]
- [[large-scale-system-simulation]]

## 来源论文
- **Paull 等 — Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter Systems (IEEE TPWRD 2025)** — 提出 AGEI 算法，将指数积分嵌入 DSED 框架，自适应步长 + 预计算矩阵指数/φ函数 + 变强迫函数项数，相对 Simulink 加速 >8×，相对 PLECS 加速 >3×，硬件实验验证精度。
- **Paull 等 — GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of Power Electronic Systems (IEEE OAJPE 2026)** — 提出 multi-granular GPU parallel-rate EI 算法，实现跨时间步并行 + 步内矩阵运算并行的双重加速，GPU 端矩阵指数/φ函数预计算框架，应用于二极管开关事件检测。
- **Fu 等 — Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations (IEEE TPWRD 2025)** — 提出分裂状态空间方法，通过自动开关分组和 SASV 识别定位最小开关相关子电路，将状态矩阵分解为常数部分和开关相关时变部分，使用多阶指数分裂公式（Trotter/Strang/高阶）组合求解。
- **Li 等 — Interpolation for Power Electronic Circuit Simulation Revisited with Matrix Exponential and Dense Outputs (Electric Power Systems Research 2020)** — 提出 MEXP 方法，基于 Padé 逼近和稠密输出公式，实现变量阶积分（可灵活选择 Padé 阶数控制精度），稠密输出复用缩放平方法中间结果，无额外计算代价。
- **Wu 等 — GPU-based Power Converter Transient Simulation with Matrix Exponential Integration and Memory Management (Electric Power and Energy Systems 2020)** — 提出 GPU 端矩阵指数缓存和内存管理策略，通过缓存同一开关组合的矩阵指数避免重复计算，减少 CPU-GPU 数据传输，在不同规模风电场上验证加速效果。
- **赵金利等 — 面向指数积分方法的电磁暂态仿真 GPU 并行算法 (中国电机工程学报 2018)** — 面向指数积分方法的 GPU 并行实现，利用 GPU 多线程加速矩阵指数运算，在电力电子 EMT 仿真中提升计算效率。
