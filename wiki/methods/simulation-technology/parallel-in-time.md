---
title: "时间并行方法 (Parallel-in-Time)"
type: method
tags: [parallel-in-time, mgrit, parareal, time-parallel, mmc, hvdc, acceleration, pegr, matrix-diagonalization]
created: "2026-05-10"
updated: "2026-05-13"
---

# 时间并行方法 (Parallel-in-Time)

## 定义

时间并行方法（Parallel-in-Time, PiT）是一类将仿真时间轴划分后并行推进的加速技术，与传统的空间并行（网络分区解耦）正交。核心思想不是把电路拓扑拆成子网络，而是把整个仿真时间窗口划分为若干粗时间区间，每个区间内的细步长计算分配到不同计算核心并行执行。

时间并行方法起源于 Lions 等人 2001 年提出的 Parareal 算法 [Lions 2001]，后经 Gander 等人发展为多层时间网格的 MGRIT（Multi-Grid Reduction in Time）框架 [Gander 2007]。在电力系统电磁暂态（EMT）仿真中，时间并行方法为 MMC-HVDC 等空间并行度受限的大规模电力电子系统提供了额外的加速维度。

EMT 场景的特殊性在于：传统数值积分方法（如隐式梯形法、CDA 法）的逐步推进本质上是串行的——每个时间步的解依赖于前一步的结果。时间并行方法通过粗/细模型的双层网格结构和状态映射机制，打破了这一串行依赖。

## EMT 中的角色

EMT 仿真的并行化长期受限于空间并行度瓶颈：

- **MMC 桥臂限制**：MMC 换流器的空间并行通常按 6 个桥臂拆分，最多 6 路并行，每个桥臂内大量子模块状态仍需串行更新。Debnath [2019] 指出，随着每个桥臂子模块数量增至千级，臂内串行计算的计算负担急剧上升，空间并行效率受限于内存访问延迟。
- **细步长约束**：电力电子开关频率要求微秒级步长（$\sim 1\mu\text{s}$），长时间仿真总步数巨大。
- **传输线延迟耦合**：行波线模型（如 Bergeron 模型）引入了延迟微分方程（DDE），使得不同时间点的状态强耦合。Cheng [2020] 指出，传输线延迟 $\tau$ 导致历史状态依赖，限制了时间窗口的选择。

时间并行的补充作用在于：在空间并行已达上限时，沿时间轴提供额外并行度，实现"空间 + 时间"双维度加速。

## 核心算法框架

### Parareal 算法

Parareal 是时间并行方法中最经典的迭代算法，由 Lions 等人于 2001 年提出。其核心思想是将仿真时间 $[t_0, t_{\text{end}}]$ 划分为 $N$ 个子区间 $I_k = [T_{k-1}, T_k]$，使用粗算子 $G$ 和细算子 $F$ 交替迭代。

对于 $N$ 个时间区间，建立如下非线性方程组：

$$
W(U) := \begin{cases}
U_1 - F(T_1, T_0, U_0) = 0, \\
U_2 - F(T_2, T_1, U_1) = 0, \\
\vdots \\
U_N - F(T_N, T_{N-1}, U_{N-1}) = 0,
\end{cases}
\quad (1)
$$

其中 $U_k$ 为第 $k$ 个时间点的系统状态向量，$U_0$ 为已知初始值。系统 (1) 可用 Newton 法求解，对每个 $U_j$ 的迭代更新公式为：

$$
U_j^{(k)} = F(T_j, T_{j-1}, U_{j-1}^{(k-1)}) + \frac{\partial F}{\partial U}(T_j, T_{j-1}, U_{j-1}^{(k-1)}) (U_{j-1}^{(k)} - U_{j-1}^{(k-1)})
\quad (2)
$$

为并行化计算，式 (2) 中的雅可比项被粗算子 $G$ 近似：

$$
\frac{\partial F}{\partial U} \approx \frac{F(T_j, T_{j-1}, U_{j-1}^{(k-1)}) - F(T_j, T_{j-1}, U_{j-1}^{(k-2)})}{U_{j-1}^{(k-1)} - U_{j-1}^{(k-2)}}
\quad (3)
$$

代入后得到 **Parareal 迭代公式**：

$$
U_j^{(k)} = F(T_j, T_{j-1}, U_{j-1}^{(k-1)}) + G(T_j, T_{j-1}, U_{j-1}^{(k)}) - G(T_j, T_{j-1}, U_{j-1}^{(k-1)})
\quad (4)
$$

该公式是一个 **Quasi-Newton 方法** [Lions 2001]。算法执行流程为：

1. **初始化**：粗算子 $G$ 串行生成初始猜测 $G^{(0)}$
2. **并行细算**：各细算子 $F$ 并行计算 $F^{(k)}$
3. **粗算修正**：粗算子串行修正 $U^{(k+1)} = G^{(k+1)} - P$，其中 $P = F^{(k+1)} - G^{(k)}$
4. **收敛检查**：计算相对误差

$$
\text{error}^{(k)} = \frac{\sum_{j=k+1}^{N-1} \|U_j^{(k+1)} - U_j^{(k)}\|}{\sum_{j=k+1}^{N-1} \|U_j^{(k)}\|}
\quad (5)
$$

若误差超过容差，则返回步骤 2 继续迭代。

### MGRIT 算法

MGRIT（Multi-Grid Reduction in Time）是 Parareal 的多层推广 [Heimbach 2017]。与 Parareal 的两层网格不同，MGRIT 构建了多层时间粗化网格：

$$
\text{Level 0: } \delta t \quad \rightarrow \quad \text{Level 1: } 2\delta t \quad \rightarrow \quad \cdots \quad \rightarrow \quad \text{Level L: } 2^L \delta t
$$

在每一层上执行粗/细网格迭代，粗层提供更低精度的初始猜测，逐层细化。MGRIT 的收敛速度理论上优于 Parareal，因为多层粗化能更有效地传播低频误差。

### PEGR 方法

Cai 等人 [2021] 提出了 **方程分组与重排并行化**（Parallelization-in-Time Equation Grouping and Reordering, PEGR）方法，基于修改增广节点分析（MANA）公式。该方法将连续时间点的网络方程分组后联合求解，利用稀疏 LU 分解（KLU 求解器）和 OpenMP 多线程实现并行。

对于 16 个连续时间点的网络方程，PEGR 将扩展方程组写成：

$$
\begin{bmatrix}
D & 0 & 0 & \cdots \\
O & D & 0 & \cdots \\
0 & O & D & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_{16}
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_{16}
\end{bmatrix}
\quad (6)
$$

通过奇偶行/列重排和递归 LU 分解，前 8 个方程变为独立可并行求解，剩余 8 个方程继续递归分组。该方法的优势在于直接作用于 EMT 网络方程，无需改变组件模型。

## 矩阵对角化时间并行方法

汪芳宗等人 [2017] 提出了一种基于矩阵对角化的严格时间解耦并行方法。该方法对 CDA（临界阻尼调整）算法进行完全并行化。

### 线性系统的时间解耦

考虑常微分初值问题：

$$
\begin{cases}
\dot{x}(t) = f(x) + g(t) \\
x(t=0) = x_0
\end{cases}
\quad (7)
$$

对 $N$ 个时间网格点连续离散化，可得：

$$
(A \otimes I_m)X = (B \otimes I_m)F(X) + (B \otimes I_m)G(t)
\quad (8)
$$

其中 $\otimes$ 为 Kronecker 积（张量积），$A$ 为积分系数矩阵。对于线性系统 $\dot{x} = Ux + g(t)$，方程 (8) 简化为：

$$
(H \otimes I_m - I_N \otimes U)X = G(t)
\quad (9)
$$

其中 $H$ 为下三角矩阵，其元素由积分步长和积分方法决定。关键步骤是对 $H$ 进行 **特征值分解（对角化）**：

$$
H = PDP^{-1}
\quad (10)
$$

其中 $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_N)$ 为特征值对角矩阵，$P$ 为特征向量矩阵，其元素为：

$$
p_{ij} = \frac{\prod_{k=j+1}^{N} [(1-\alpha_k)h_k + \alpha_j h_j]}{\prod_{k=j+1, k\neq i}^{N} (\alpha_j h_j - \alpha_k h_k)}
\quad (11)
$$

令 $Y = (P^{-1} \otimes I_m)X$，$\hat{G}(t) = (P^{-1} \otimes I_m)G(t)$，代入式 (9) 得：

$$
(D \otimes I_m - I_N \otimes U)Y = \hat{G}(t)
\quad (12)
$$

由于 $D$ 是对角矩阵，方程 (12) 可完全解耦为 $N$ 个独立方程：

$$
(\lambda_k I_m - U)y_k = \hat{g}_k(t), \quad k \in \{1, \dots, N\}
\quad (13)
$$

每个方程可独立并行求解。求得 $y_k$ 后，通过 $X = (P \otimes I_m)Y$ 反变换得到完整解。

### 非线性系统的牛顿并行方法

对于非线性系统 $f(x)$，定义 Jacobian 矩阵和平均向量：

$$
J(x) = \frac{\partial f(x)}{\partial x}, \quad \bar{x} = \frac{1}{N}\sum_{k=1}^{N} x_k
\quad (14)
$$

利用 Newton 法线性化后，迭代方程为：

$$
[H \otimes I_m - I_N \otimes J(\bar{x}^{(\eta)})]\Delta X^{(\eta)} = R(X^{(\eta)})
\quad (15)
$$

类似地，通过特征值分解对角化后得到并行求解的修正方程：

$$
[\lambda_k I_m - J(\bar{x}^{(\eta)})]\Delta y_k^{(\eta)} = \hat{r}_k(X^{(\eta)}), \quad k \in \{1, \dots, N\}
\quad (16)
$$

求解后通过反变换得到 $\Delta X^{(\eta)}$，更新 $X^{(\eta+1)} = \Delta X^{(\eta)} + e_N \otimes \bar{x}^{(\eta)}$。

### 变步长要求

该算法的一个关键约束是：**必须采用完全变步长**，即同一时间网格内所有步长必须互异。这是因为式 (11) 的分母要求 $\alpha_j h_j \neq \alpha_k h_k$。汪芳宗 [2017] 提出了两种互异步长选择方法：

1. **渐近平均法**：
$$
h_k = \frac{(1+\epsilon)^k}{\sum_{j=1}^{N}(1+\epsilon)^j} T, \quad k \in \{1, \dots, N\}
\quad (17)
$$
其中 $\epsilon \approx \pm 0.01$ 为小量。当 $\epsilon \to 0$ 时 $h_k \to T/N$。

2. **Radau 网格法**：基于 Radau 多项式 $d^{N-1}/dx^{N-1}(x^N(x-1)^{N-1})$ 的 $N-1$ 个零点构成网格，步长为 $h_k = (c_k - c_{k-1})T$。

### 与 CDA 的兼容性

该方法与 EMTP 中的 CDA（临界阻尼调整）方法天然兼容：在系统发生突变时采用隐式欧拉法（$\alpha = 1$），在正常时段采用隐式梯形积分法（$\alpha = 1/2$）。由于变步长条件下不同积分方法产生不同的系数矩阵 $H$，CDA 的切换恰好提供了所需的互异步长。

## EMT 中的具体实现

### Debnath 的 MMC-HVDC 并行算法

Debnath [2019] 将 Parareal/MGRIT 框架应用于 MMC-HVDC 系统的 EMT 仿真，提出了专门针对电力电子系统的粗/细模型配对和状态映射机制。

#### 三层状态定义

算法定义了三种状态：
- **粗状态** $\tilde{x}$：基于平均值模型（AVM），在粗时间步 $T_{\text{coarse}}$ 上评估
- **细状态** $\hat{x}$：基于详细开关模型，在细时间步 $T_{\text{fine}}$ 上评估
- **最终状态** $x$：通过粗/细状态组合得到的最终系统状态

#### 迭代流程

每个仿真窗口 $T_{\text{window}} = N_{\text{par}} \cdot T_{\text{coarse}}$ 内执行以下迭代：

1. **初始化**（第 0 次迭代）：
$$
\tilde{x}_0[0] = x_0[0], \quad \tilde{x}_0[k-1] \rightarrow \tilde{x}_0[k], \forall k \in \{1, N_{\text{par}}\}
\quad (18)
$$
$$
x_0[k] = \tilde{x}_0[k], \quad \forall k \in \{1, N_{\text{par}}\}
\quad (19)
$$

2. **状态映射**（Translation，$i \geq 1$）：
$$
x_{i-1}[k] \mapsto \hat{x}_i[k], \quad \forall k \in \{0, N_{\text{par}}\}
\quad (20)
$$
将上一轮迭代的最终状态映射为当前轮细状态的初始值。映射基于 MMC 的下层控制系统：粗状态中的调制指数 $m_{y,j}$ 转换为详细模型中的开关信号 $S_{y,l,j}$。

3. **细算**（Fine Operation）：
$$
\hat{x}_i[k-1] \rightarrow \hat{x}_i[k], \quad \forall k \in \{1, N_{\text{par}}\}
\quad (21)
$$
各粗区间内的细步长计算可并行执行，最大并行度为 $N_{\text{par}}$。

4. **粗状态重初始化和最终状态更新**：
$$
\tilde{x}_i[k] = \hat{x}_i[k], \quad \forall k \in \{0, 1\}
\quad (22)
$$
$$
\tilde{x}_i[k-1] \rightarrow \tilde{x}_i[k], \quad \forall k \in \{2, N_{\text{par}}\}
\quad (23)
$$
$$
x_i[k] = \tilde{x}_i[k] + A_{\text{error}}(\hat{x}_i[k] - \tilde{x}_{i-1}[k]), \quad \forall k \in \{1, N_{\text{par}}\}
\quad (24)
$$
其中 $A_{\text{error}}$ 为误差修正矩阵。

5. **收敛检查**：
$$
e_{\text{tol}} = \sqrt{\sum_{k=0}^{N_{\text{par}}} (x_i[k] - x_{i-1}[k])^T E (x_i[k] - x_{i-1}[k])} \leq E_{\text{tol}}
\quad (25)
$$
其中 $E$ 为正定对角矩阵，用于加权不同状态变量的误差。

#### MMC 模型

**详细模型**（细层）：SM 电容电压动态：

$$
C_{\text{SM}} \frac{dv_{cy,l,j}}{dt} = -\frac{v_{cy,l,j}}{R_p} + S_{y1,l,j} i_{y,j} + (1-S_{y1,l,j})(1-S_{y2,l,j}) i_{y,j} \text{sgn}(i_{y,j})
\quad (26)
$$

**平均值模型**（粗层）：桥臂电流动态：

$$
(L_o + L_s)\frac{di_{p,j}}{dt} - L_s\frac{di_{n,j}}{dt} = -(R_o + R_s)i_{p,j} + R_s i_{n,j} + \frac{V_{\text{dc}}}{2} - v_j - v_{\text{cm}} - v_{p,j}
\quad (27)
$$

桥臂电压的 AVM 表示：

$$
v_{y,j} = m_{y,j} v_{cy,j}^{\Sigma} + (1 - SD_{y,j}) \frac{v_{cy,j}^{\Sigma}}{N} \text{sgn}(i_{y,j})
\quad (28)
$$

#### 仿真参数

Debnath [2019] 在 401 层 MMC-HVDC 系统上的仿真参数：

| 参数 | 值 |
|------|------|
| 桥臂电感 $L_o$ | 65 mH |
| 换流器电感 $L_s$ | 80 mH |
| SM 电容 $C_{\text{SM}}$ | 15 mF |
| PWM 频率 | 360 Hz |
| 粗时间步 $T_{\text{coarse}}$ | 60 $\mu$s |
| 细时间步 $T_{\text{fine}}$ | 4 $\mu$s |
| 仿真窗口 $T_{\text{window}}$ | 300 $\mu$s |
| 并行核心数 $N_{\text{par}}$ | 5 |

#### 量化结果

在 France-Espain MMC-HVDC 系统（401 层）上的仿真结果 [Debnath 2019]：

| 工况 | 并行时间 (s) | 串行时间 (s) | 加速比 | 电压误差 (%) | 电流误差 (%) |
|------|-------------|-------------|--------|-------------|-------------|
| 稳态运行 | 7.2 | 25.015 | 3.47x | 1.23 | 0.23 |
| 直流故障闭锁 | 7.42 | 22.79 | 3.07x | 2.71 | 0.30 |
| 直流侧启动 | 5.3 | 11.32 | 2.14x | 0.72 | 0.06 |
| 交流侧启动 | 8.66 | 25.81 | 2.98x | 3.83 | 0.61 |

最大加速比 3.47x（5 核），低于理论值 5x 的原因是部分时间步需要更多迭代次数才能收敛。

### Cheng 的 Parareal EMT 仿真框架

Cheng 等人 [2020] 提出了面向电力系统 EMT 仿真的 Parareal 算法实现，针对传统 EMT 模型的特殊性进行了多项改进。

#### 组件化架构

提出了基于组件的对象化 EMT 系统求解器架构。每个组件继承自 `TransientComponent` 基类，提供标准接口：`initialize()`、`assemble_mat()`、`update_i()`、`update_hist()`。电路对象通过图拓扑关系管理组件，全局系统矩阵由组件信息组装。

#### 传输线 DDE 处理

传输线行波模型引入延迟微分方程（DDE）：

$$
i_{\text{hist}}^m(t) = -2G v_k(t-\tau) - i_{\text{hist}}^k(t-\tau)
\quad (29)
$$

$$
i_{\text{hist}}^k(t) = -2G v_m(t-\tau) - i_{\text{hist}}^m(t-\tau)
\quad (30)
$$

其中 $\tau$ 为传播延迟。Parareal 迭代中，细网格的历史数据在粗网格中不存在，Cheng 等人提出了 **细网格增强插值策略**：

$$
j_{\text{fine}} = \left\lfloor j_{\text{coarse}} \frac{\Delta t}{\delta t} + \left(\frac{\tau}{\Delta t} - 1\right) \right\rfloor
\quad (31)
$$

其中 $j_{\text{fine}}$ 为细网格历史向量中的索引，$j_{\text{coarse}}$ 为粗网格索引，$\Delta t$ 为粗时间步，$\delta t$ 为细时间步。粗网格传输线从细网格历史向量读取数据，提高了粗算预测精度。

#### 时变窗算法

为减少长时仿真的计算浪费和内存消耗，提出了时变窗口（Windowed）算法：仅在当前时间窗口附近启动并行工作线程，窗口结束后将最后一个子区间的解传递给下一个窗口的起始线程。

#### 量化结果

在 IEEE-118 系统上的仿真结果 [Cheng 2020]：

| 粗时间步 $\Delta t$ | 加速比 | 并行效率 | 相对于串行加速 |
|---------------------|--------|----------|---------------|
| 40 $\mu$s | 2.30x | 40% | 2.08x |
| 80 $\mu$s | 1.85x | 37% | — |
| 200 $\mu$s | 2.10x | 42% | — |
| 400 $\mu$s | 1.50x | 30% | — |

5 线程下，$\Delta t = 200\mu\text{s}$ 时达到最佳性能：比串行快 2.08x，并行效率 42%，开销约 10%。

### 汪芳宗的矩阵对角化方法

汪芳宗等人 [2017] 将矩阵对角化方法应用于电力系统 EMT 仿真，实现了 CDA 方法的完全时间并行化。

#### 高压输电线路空载合闸算例

220kV 高压长线路，50 段空间离散，$N=15$ 个时间网格点，$T = N \times 10\mu\text{s}$。

- 采用"渐近平均法"和"Radau 网格"两种步长选择方案
- 第一个时间步采用隐式欧拉法（检测合闸突变），后续采用隐式梯形法
- 与定步长 $h=10\mu\text{s}$ CDA 方法结果对比，误差在可接受范围内

#### VFTO 计算算例

550kV GIS 隔离开关操作特快速暂态过电压（VFTO）：
- 变压器等值电感 $L_T = 20\text{mH}$，对地电容 $C_T = 3000\text{pF}$
- 电弧模型：$R(t) = R_1 e^{-t/\tau_1} + R_2 e^{t/\tau_2}$，其中 $R_1 = 10\Omega, R_2 = 0.5\Omega, \tau_1 = 1\text{ns}, \tau_2 = 1\mu\text{s}$
- 线路 L1 分为 20 段，L2 分为 7 段
- Newton 迭代收敛精度：$\|\Delta Y\|_\infty \leq 10^{-4}$

#### 加速比测试结果

在 Intel E5-2600v3（18 核）上的测试结果：
- 线性系统：加速比与并行度 $N$ 近似成正比
- 非线性系统（VFTO）：加速比不与并行度完全成正比，高并行度下迭代次数增加
- $N=15$ 时，VFTO 算例加速比约为 8-10x

## 形式化表达

### Parareal 框架通用形式

$$
U_j^{(k)} = F_j(U_{j-1}^{(k-1)}) + G_j(U_{j-1}^{(k)}) - G_j(U_{j-1}^{(k-1)})
\quad (32)
$$

### MGRIT 多网格形式

$$
\begin{aligned}
\text{Fine sweep: } & U^{(k)}_{\text{fine}} = F(U^{(k)}_{\text{coarse}}) \\
\text{Correction: } & U^{(k+1)} = U^{(k)}_{\text{fine}} + \text{I}_h^H (U^{(k)}_{\text{coarse}} - G(U^{(k)}_{\text{fine}}))
\end{aligned}
\quad (33)
$$

### 矩阵对角化解耦形式

$$
(\lambda_k I_m - J(\bar{x}^{(\eta)}))\Delta y_k^{(\eta)} = \hat{r}_k(X^{(\eta)}), \quad k \in \{1, \dots, N\}
\quad (34)
$$

### 误差收敛判据

$$
\text{error}^{(k)} = \frac{\sum_{j} \|U_j^{(k+1)} - U_j^{(k)}\|}{\sum_{j} \|U_j^{(k)}\|} \leq \epsilon_{\text{tol}}
\quad (35)
$$

## 关键技术挑战

### 传输线延迟耦合

传输线行波模型（Bergeron 模型）引入的 DDE 是时间并行的最大障碍。历史状态 $x(t-\tau)$ 在粗网格中不连续存在，导致粗算子无法准确预测细网格的历史值。Cheng [2020] 指出，解决策略包括：(1) 限制时间窗口小于传输线延迟；(2) 细网格增强插值策略，粗网格从细网格历史数据读取；(3) 对短线路使用 pi 型等效模型替代行波模型。

### 非线性系统的收敛性

Parareal 算法要求粗算子 $G$ 能够良好近似细算子 $F$。在 EMT 仿真中，电力电子开关的非线性特性（如 IGBT 开通/关断）导致 $F$ 和 $G$ 的差异较大，需要更多迭代次数才能收敛。Debnath [2019] 观察到，在某些时间步需要多次迭代，导致实际加速比低于理论值。

### 变步长约束

矩阵对角化方法要求所有时间步长互异，这在实践中需要通过渐近平均法或 Radau 网格来构造。Parareal 方法虽然不要求变步长，但粗/细步长比的选择对收敛速度有显著影响。Cheng [2020] 指出，步长比过小会导致细算工作量不足，步长比过大会增加迭代次数。

### 内存开销

Parareal 算法需要在每个迭代轮次存储所有时间点的状态，内存需求与仿真时长成正比。Cheng [2020] 的时变窗口算法将内存限制在一个时间窗口内，但牺牲了部分并行度。

## 量化性能边界

### 加速比范围

| 方法 | 系统规模 | 并行度 | 加速比 | 来源 |
|------|---------|--------|--------|------|
| Debnath MMC-HVDC | 401 层 MMC | 5 核 | 3.47x | Debnath 2019 |
| Cheng IEEE-118 | 354×354 矩阵 | 5 线程 | 2.30x | Cheng 2020 |
| 汪芳宗 220kV 线路 | 101 维 ODE | 18 核 | ~10x | 汪芳宗 2017 |
| 汪芳宗 VFTO | 59×59 时变矩阵 | 18 核 | ~8x | 汪芳宗 2017 |

### 误差范围

- Debnath [2019]：电压误差 0.72%~3.83%，电流误差 0.06%~0.61%
- Cheng [2020]：与 PSCAD/EMTDC 验证，误差在 0.01 容差范围内
- 汪芳宗 [2017]：与定步长 CDA 方法对比，结果吻合

### 并行效率

- Cheng [2020]：IEEE-118 系统 5 线程效率 40%~42%
- 汪芳宗 [2017]：非线性系统效率随并行度增加而下降

## 适用边界与选择指南

### 方法选择对比

| 方法 | 适用场景 | 优势 | 局限 |
|------|---------|------|------|
| Parareal + AVM/详细模型 | MMC-HVDC 电力电子系统 | 与空间并行正交，实现简单 | 收敛依赖粗算精度，迭代开销大 |
| MGRIT | 大规模电力电子系统 | 收敛速度快于 Parareal | 实现复杂，多层网格管理开销 |
| 矩阵对角化 | 线性/非线性 ODE 系统 | 严格时间解耦，无迭代 | 需变步长，仅适用于实特征值系统 |
| PEGR | 通用 EMT 网络仿真 | 直接作用于网络方程，无需改模型 | 仅适用于显式独立子问题，拓扑变化需回退串行 |

### 场景推荐

- **MMC-HVDC 系统**：优先使用 Parareal + AVM/详细模型配对 [Debnath 2019]，与空间并行互补
- **大规模输电网络**：优先使用 PEGR 方法 [Cai 2021] 或 Cheng 的组件化 Parareal 框架
- **线性网络分析**：优先使用矩阵对角化方法 [汪芳宗 2017]，可获得严格时间解耦
- **VFTO/开关瞬态**：矩阵对角化方法配合 CDA 切换策略，天然兼容突变检测

### 参数选择指南

- **粗/细步长比**：建议 10~50，过小导致细算工作量不足，过大增加迭代次数
- **时间窗口大小**：应小于最短传输线延迟（Cheng [2020]）
- **并行度**：受限于 $N_{\text{par}} = T_{\text{window}} / T_{\text{coarse}}$，过大导致迭代次数增加

## 相关页面

### 相关方法
- [[multirate-method]] — 多速率仿真，与时间并行互补的时间离散技术
- [[network-partitioning]] — 空间并行，与时间并行正交
- [[gpu-accelerated-simulation]] — GPU 加速，可与时间并行结合
- [[average-value-model]] — 粗层的核心建模工具
- [[companion-model]] — 时间离散中的伴随模型，与逐步积分相关
- [[numerical-integration]] — 数值积分方法，时间并行的基础

### 相关模型
- [[mmc-model]] — MMC 详细模型，时间并行的主要应用对象
- [[vsc-model]] — VSC 模型
- [[Bergeron-line-model]] — Bergeron 行波线模型
- [[equivalent-modeling]] — 等效建模方法

### 相关主题
- [[parallel-computing]]
- [[real-time-simulation]]
- [[multirate-and-network-partitioning]]
- [[gpu-parallel-acceleration]]
- [[large-scale-system-simulation]]

## 来源论文

- **Debnath [2019]** — *Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System*, IEEE JESTPE. 提出面向 MMC-HVDC 的 Parareal/MGRIT 算法，定义了粗/细模型配对和状态映射机制，验证了 3.47x 加速比。
- **Cheng, Duan & Dinavahi [2020]** — *Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power Systems*, IEEE Access. 提出组件化 EMT 系统求解器架构，解决了传输线 DDE 的 Parareal 收敛问题，在 IEEE-118 系统上验证 2.30x 加速比。
- **汪芳宗, 王永, 宋墩文等 [2017]** — *基于矩阵对角化的电磁暂态时间并行计算方法*, 电网技术. 提出基于 CDA 算法和矩阵实特征值分解的严格时间解耦并行方法，在 220kV 线路和 VFTO 算例上验证。
- **Cai, Mahseredjian, Kocar et al. [2021]** — *A parallelization-in-time approach for accelerating EMT simulations*, EPSR. 提出 PEGR 方法，基于 MANA 公式的方程分组与重排技术，使用 KLU 稀疏求解器和 OpenMP 实现。
- **Lions & Maday [2001]** — *Résolution d'EDP par un schéma en temps pararéel*, CRAS. Parareal 算法的原始提出。
- **Gander & Vandewalle [2007]** — *Analysis of the parareal time-parallel integration method*, SIAM J. Sci. Comput. Parareal 算法的收敛性分析。
