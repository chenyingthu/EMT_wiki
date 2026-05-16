---
title: "DAE 求解器 (DAE Solvers)"
type: method
tags: [dae, differential-algebraic, solver, implicit, integration, newton]
created: "2026-05-02"
updated: "2026-05-16"
---

# DAE 求解器 (DAE Solvers)

## 定义与边界

DAE（Differential-Algebraic Equation，微分-代数方程）求解器用于求解同时包含微分方程和代数约束的系统。电力系统仿真中，微分方程通常来自电感、电容、旋转电机、控制器和动态等值元件，代数约束通常来自网络 KCL/KVL、端口接口、开关状态和控制限值。

半显式形式可写为

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},t), \quad
\mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},t),
$$

其中 $\mathbf{x}$ 为动态状态向量，$\mathbf{y}$ 为代数变量向量。更一般的隐式形式为

$$
\mathbf{F}(\dot{\mathbf{z}},\mathbf{z},t)=\mathbf{0}.
$$

在 EMT 仿真中，DAE 求解器的性能取决于以下六个维度：

| 维度 | 说明 |
|------|------|
| 模型指数 (index) | 指标越高，代数约束的隐式依赖越强，求解越困难 |
| 事件处理 | 开关切换、限幅动作、保护跳闸等不连续事件的重初始化 |
| 雅可比构造 | 牛顿迭代中偏导数矩阵的计算效率和稀疏性保持 |
| 线性求解器 | 每个牛顿步求解稀疏线性系统的计算复杂度 |
| 步长策略 | 变步长时误差估计与步长自适应逻辑 |
| 初始条件一致性 | 仿真启动时 $\mathbf{g}(\mathbf{x}_0,\mathbf{y}_0,t_0)=\mathbf{0}$ 的满足程度 |

本页讨论 DAE 求解的数值结构，不把某个商业软件或某个积分公式写成通用最优方案。

## EMT 中的角色

EMT 网络在离散化后通常变为代数网络方程和历史源更新的耦合问题。[[companion-circuit]] 把动态元件转成等效导纳与历史源，使主网络可用 [[nodal-analysis]] 或 [[nodal-admittance-matrix]] 求解；当网络中存在非线性支路、控制约束、混合仿真接口或变步长历史项时，问题常表现为隐式 DAE 或离散非线性方程组。

在机电-电磁混合仿真或动态相量模型中，DAE 求解器还承担接口一致性任务。Rupasinghe 等 (2023) 记录了用 Newton-Raphson 接口迭代求解交直流接口不平衡量的做法——EMT 侧保留三相瞬时变量，动态相量侧使用基频相量压缩，中间通过 MATE 接口协议交换端口信息。该来源页明确提示，当前抽取文本不足以支撑具体迭代次数、误差或加速比数据。

DAE 求解器的本质是**时域推进算法**：给定当前状态 $(\mathbf{x}_n, \mathbf{y}_n)$ 和下一步时间 $t_{n+1}$，寻找满足离散残差方程的新状态 $(\mathbf{x}_{n+1}, \mathbf{y}_{n+1})$。

## 核心机制

DAE 求解通常包括四个层次：

1. **建立连续模型**：明确状态变量 $\mathbf{x}$、代数变量 $\mathbf{y}$、端口变量和事件变量。
2. **离散微分方程**：选择 [[trapezoidal-rule]]（梯形法）、[[backward-euler]]（后向欧拉）、[[gear-method]]（Gear/多步法）或其他隐式积分规则，将 $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},t)$ 转化为代数残差。
3. **组装残差方程**：把离散状态方程和代数约束合并为 $\mathbf{R}(\mathbf{z}_{n+1})=\mathbf{0}$。
4. **求解非线性和线性子问题**：用 [[newton-raphson-method]] 或其变体形成雅可比系统，再调用 [[sparse-matrix-solver]]。

### 隐式一步法的离散化框架

以隐式一步法为例，离散后可写为

$$
\mathbf{R}(\mathbf{x}_{n+1},\mathbf{y}_{n+1})=
\begin{bmatrix}
\mathbf{r}_x(\mathbf{x}_{n+1},\mathbf{y}_{n+1}) \\
\mathbf{g}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})
\end{bmatrix}
=\mathbf{0}.
$$

牛顿迭代的线性化系统为

$$
\begin{bmatrix}
\partial\mathbf{r}_x/\partial\mathbf{x} & \partial\mathbf{r}_x/\partial\mathbf{y} \\
\partial\mathbf{g}/\partial\mathbf{x} & \partial\mathbf{g}/\partial\mathbf{y}
\end{bmatrix}
\begin{bmatrix}
\Delta\mathbf{x} \\
\Delta\mathbf{y}
\end{bmatrix}
=
-\begin{bmatrix}
\mathbf{r}_x \\
\mathbf{g}
\end{bmatrix}. \quad\quad (1)
$$

其中左端 $2\times2$ 分块矩阵为完整雅可比矩阵 $\mathbf{J}$。若 $\partial\mathbf{g}/\partial\mathbf{y}$ 在运行点附近奇异或近奇异（病态代数约束），代数约束可能难以消元，求解器表现为收敛困难、步长拒绝或初始化失败。

### 分区 DAE 的接口一致性

当系统按 [[hybrid-simulation]] 或 [[co-simulation]] 范式划分为多个子系统时，每个子系统各自维护局部 DAE，子系统间通过接口量交换信息。接口一致性要求

$$
\mathbf{g}_{\text{interface}}(\mathbf{x}^{(i)},\mathbf{y}^{(i)},\mathbf{x}^{(j)},\mathbf{y}^{(j)})=\mathbf{0},
$$

即相邻子系统共享变量的代数约束必须同时满足。常见接口形式包括：

- **Norton-Thevenin 等效**：将子系统 $j$ 对子系统 $i$ 的作用等效为阻抗 $Z_j$ 与历史源 $e_j$，接口方程为 $i_{ij}=Y_j v_i - I_j$。
- **功率守恒接口**：注入功率相等 $\{P_i=P_j^{\text{received}}, Q_i=Q_j^{\text{received}}\}$，适用于多速率分区。

### 指标问题与初始化

实际电力系统 DAE 多为指标 1（index-1），即代数约束可显式解出 $\mathbf{y}$ 关于 $\mathbf{x}$ 的隐函数。然而以下情形会导致有效指标升高：

| 情形 | 有效指标变化 | 求解影响 |
|------|------------|---------|
| 开关动作瞬间 | index 突变 | 需要事件检测+重初始化 |
| 控制限幅饱和 | 约束从等式变为不等式 | 主动/被动约束切换导致残差结构变化 |
| 保护动作后网络拓扑重构 | 网络方程结构阶跃 | 需要重新因子分解雅可比 |
| 动态相量与 EMT 接口 | 不同描述域的约束耦合 | 接口变量在相量与瞬时值间转换 |

**一致初始化**（consistent initialization）是 DAE 求解的关键前置步骤。Cirilo Leandro 等 (2024) 针对电压源换流器提出的三阶段初始化方法：将潮流结果转化为三相 AC 稳态相量，再映射为 EMT 离散积分器的历史项，使电感电流、电容电压和控制积分器的历史项与稳态微分/积分关系一致。验证中，未初始化的 EMT 仿真到 300 ms 仍未达到稳态，而采用该方法几乎无可见暂态启动。

## 分类与变体

| 类别 | 机制 | EMT 中的典型位置 | 注意事项 |
|------|------|----------------|---------|
| 固定步长隐式 DAE | 每步用固定 $\Delta t$ 离散并求解残差 | 传统 EMT、实时仿真、开关级仿真 | 易于同步硬件或事件表，但步长需覆盖最快关注动态 |
| 变步长/变阶 DAE | 根据误差估计调整步长或阶数 | 离线 EMT、长时域暂态、混合多物理仿真 | 事件点和历史项重初始化是主要风险 |
| 分区 DAE | 把网络、控制器、设备模型或子系统分开迭代 | [[hybrid-simulation]]、[[co-simulation]] | 接口延迟和收敛判据必须显式说明 |
| 固定导纳伴随模型 | 把设备整理成固定导纳和历史源 | 实时仿真、恒导纳变流器模型 | 固定导纳不等于无误差，状态反演和事件重初始化仍需验证 |
| 多速率 DAE | 不同子系统使用不同步长并交换接口量 | [[multirate-method]]、局部 EMT 嵌入 | 插值、外推和接口能量误差可能主导精度 |

## 形式化表达

### 半显式 DAE 的标准形式

$$
\begin{cases}
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},t), & \text{微分方程（动态元件）} \\
\mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},t), & \text{代数约束（网络方程）}
\end{cases}
$$

### 隐式 DAE 的一般形式

$$
\mathbf{F}(\dot{\mathbf{z}},\mathbf{z},t)=\mathbf{0}, \quad \mathbf{z}\in\mathbb{R}^n.
$$

### 梯形积分离散（半隐式）

给定 $\mathbf{x}_n$、$\mathbf{y}_n$，求 $\mathbf{x}_{n+1}$、$\mathbf{y}_{n+1}$：

$$
\mathbf{x}_{n+1}-\mathbf{x}_n-\frac{\Delta t}{2}\left[\mathbf{f}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})+\mathbf{f}(\mathbf{x}_n,\mathbf{y}_n,t_n)\right]=\mathbf{0}.
$$

### 后向欧拉离散

$$
\mathbf{x}_{n+1}-\mathbf{x}_n-\Delta t\cdot\mathbf{f}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})=\mathbf{0}.
$$

### 牛顿迭代收敛判据

$$
\|\mathbf{R}(\mathbf{x}_{n+1}^{(k)},\mathbf{y}_{n+1}^{(k)}\|_2 < \epsilon_{\text{tol}},
$$

其中 $\epsilon_{\text{tol}}$ 通常取 $10^{-6}\sim 10^{-8}$（相对值），或 $|\Delta\mathbf{x}^{(k)}|/|\mathbf{x}^{(k)}|$ 作为相对收敛判据。

### 雅可比矩阵结构（伴随电路形式）

$$
\mathbf{J}=
\begin{bmatrix}
\mathbf{J}_{11} & \mathbf{J}_{12} \\
\mathbf{J}_{21} & \mathbf{J}_{22}
\end{bmatrix}
=
\begin{bmatrix}
\frac{\partial\mathbf{r}_x}{\partial\mathbf{x}} & \frac{\partial\mathbf{r}_x}{\partial\mathbf{y}} \\
\frac{\partial\mathbf{g}}{\partial\mathbf{x}} & \frac{\partial\mathbf{g}}{\partial\mathbf{y}}
\end{bmatrix}.
$$

其中 $\mathbf{J}_{22}$ 对应网络导纳矩阵的拓扑结构，稀疏性格式（如 Yale/BGPS 格式）对其存储和求逆效率至关重要。

## 关键技术挑战

### 挑战一：指标升高导致求解失效

当代数约束的隐式依赖链过长（有效 index > 1），隐式积分器无法直接应用。电力系统中开关切换瞬间、控制限幅触发或保护动作可能导致有效指标在仿真中途发生变化。**解法**：在事件检测后重新调用一致初始化算法，在新约束条件下重新满足代数方程。切换后雅可比矩阵结构可能发生稀疏模式跳变，需要重新分析稀疏填充模式。

### 挑战二：变步长历史项重初始化

变步长方法中，当步长从 $\Delta t_1$ 切换到 $\Delta t_2$ 时，递归卷积历史项和动态相量状态必须按新步长重新初始化，否则会产生非物理的数值振荡。**解法**：存储中间步状态并用插值/外推重建历史轨迹，或采用多步法使历史项对步长变化不那么敏感。Multiphase Power Flow Solutions (EMTP-Newton) 论文中展示了多相潮流 Newton 求解器的 Jacobian 稀疏填充优化策略（124 节点：重排序前 24.82% 填充率，Tinney 排序后 4.40%），可作为大规模稀疏矩阵处理的经验参考。

### 挑战三：强非线性导致牛顿迭代发散

MMC 子模块电容电压平衡、PWM 调制死区、限幅器饱和等强非线性环节会使雅可比矩阵在迭代中途剧烈变化，导致牛顿迭代超调或振荡。**解法**：添加阻尼因子 $(\alpha\in(0,1])$ 限制步长 $\Delta\mathbf{z}^{(k+1)}=\Delta\mathbf{z}^{(k)}-\alpha\mathbf{J}^{-1}\mathbf{R}$；或采用弧长延 CONTINUATION 方法使路径跟踪更稳健。

### 挑战四：分区接口的延迟误差累积

在 [[co-simulation]] 框架下，EMT 子系统和 TS/DP 子系统分别推进步长，接口信息交换存在天然延迟。延迟误差若不加以控制，会在长时域仿真中累积并导致相角漂移或能量不守恒。**解法**：使用 MATE（Multi-Area Thevenin Equivalent）接口协议将延迟误差吸收为戴维南等效的接口修正量；或采用无损 Bergeron 传输线显式耦合，利用物理传播延时作为接口延迟的精确表示（Rupasinghe 2023 报告 118 节点系统 10 s 仿真从 1126 s 降至 88 s，约 12.8 倍加速）。

### 挑战五：初值不一致导致启动暂态

若初始条件 $\mathbf{x}_0$、$\mathbf{y}_0$ 不满足 $\mathbf{g}(\mathbf{x}_0,\mathbf{y}_0,t_0)=\mathbf{0}$，仿真启动瞬间会出现非物理冲击，控制器积分器可能饱和或发散。Cirilo Leandro 等 (2024) 的 VSC 三阶段初始化方法通过 AC 稳态相量映射为 EMT 积分器历史项，可有效消除启动暂态；大规模 FCI 方法（风电场场景）报告达到稳态判据的时间：FCI 约 0.22 s，LFSI 约 1.54 s，NI（未初始化）约 8.57 s（据 Comprehensive Full-Scale Converter Wind Park Initialization 论文，待原文核验）。

## 量化性能边界

| 指标 | 典型数值 | 来源/条件 |
|------|---------|-----------|
| 固定步长 EMT 步长 | $0.1\sim 50$ μs | 开关级仿真；MMC 子模块需亚微秒 |
| 动态相量步长 | $0.1\sim 1$ ms | 基频相量压缩；与 EMT 接口需 0.1 ms 级 |
| 暂态稳定步长 | $1\sim 10$ ms | 机电暂态研究 |
| 牛顿迭代收敛容差 | $10^{-6}\sim 10^{-8}$（相对） | 工程常用 $10^{-7}$ |
| 稀疏矩阵填充率（124 节点，未重排序） | 24.82% | Multiphase Power Flow 论文 |
| 稀疏矩阵填充率（124 节点，Tinney 排序） | 4.40% | 同上 |
| EMT-TS 协同仿真加速比（118 节点） | ~12.8×（1126 s → 88 s） | Rupasinghe 2023，10 s 仿真 |
| VSC 初始化后稳态建立时间 | ~0.22 s（FCI）vs ~8.57 s（NI） | Comprehensive Wind Park Initialization 论文，待原文核验 |
| 大规模系统 FCI 初始化耗时 | 36.65 s（FCI）vs 380.3 s（LFSI） | 同上，EMTP，50 μs 步长，Intel i7-8550U |

## 适用边界与选择指南

| 场景 | 推荐 DAE 求解器类型 | 关键理由 |
|------|-------------------|---------|
| 实时仿真（硬件在环） | 固定步长隐式 DAE + 固定导纳伴随模型 | 确定性步长，无变步长开销，利于 FPGA/CPU 并行 |
| 开关级 EMT（详细换流器） | 固定步长 + 事件检测 | 微秒级步长覆盖快动态，切换时重初始化 |
| 长时间机电暂态研究 | 变步长 DAE + 分区 DAE | 毫秒至秒级步长，自动适应系统动态 |
| EMT-TS 协同仿真 | 分区 DAE + MATE 接口 | 接口误差可控，多求解器生态 |
| 大规模 HVDC 系统 | 固定步长 + 稀疏矩阵求解器 + 多速率 | 大系统需稀疏求解加速；多速率降低计算负担 |
| 含控制器初始化的 VSC 研究 | 一致初始化 + 后向欧拉 | 从稳态出发避免启动暂态；后向欧拉利于控制器初始化 |

## 相关方法

- [[newton-raphson-method]]：DAE 求解器中最常见的非线性残差求解内核
- [[trapezoidal-rule]]：DAE 离散化的常用隐式积分规则，无数值阻尼但有数值振荡风险
- [[backward-euler]]：无条件稳定的隐式积分，但一阶精度、可能过度阻尼快动态
- [[gear-method]]：Gear 多步法（BDF），适合刚性 DAE 但需较多历史步存储
- [[companion-circuit]]：EMT 中把微分元件纳入代数网络求解的关键形式
- [[sparse-matrix-solver]]：大规模 DAE 每个牛顿步的主要计算负担
- [[steady-state-initialization]]：DAE 初值一致性的前置步骤，避免启动暂态
- [[stiff-system-handling]]：DAE 求解稳定性和步长选择的重要背景
- [[hybrid-simulation]]：分区 DAE 在 EMT-机电混合仿真中的典型应用
- [[co-simulation]]：多求解器协同仿真的框架，子系统独立推进并交换接口量
- [[multirate-method]]：多速率 DAE 的实现策略，不同子系统使用不同步长

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Rupasinghe 等 - A multi-solver framework for co-simulation of transients in modern power systems | 2023 | 多求解器协同仿真框架（EMT/DP/BFAST/TS），提出 MATE 接口协议，118 节点系统 12.8× 加速 |
| Cirilo Leandro 等 - A steady-state initialization procedure for generic voltage source converters in EMT simulation | 2024 | VSC 三阶段初始化（潮流→AC 稳态→EMT 历史项），零初始条件到 300 ms 未达稳态 vs 几乎无暂态启动 |
| Comprehensive Full-Scale Converter Wind Park Initialization | 2024 | 风电场全功率变流器 FCI 初始化方法，0.22 s vs 8.57 s 稳态建立（待原文核验）|
| Multiphase power flow solutions using EMTP and Newton's method | — | 多相 Newton 潮流嵌入 EMTP，Tinney 重排序后填充率 4.40%（124 节点） |
| Shooting method based MMC initialization | 2024 | 基于打靶法的 MMC 周期稳态初始化，将初始化问题转化为求周期映射不动点 |

## 修订与证据使用注意事项

- 不应写"电力系统 DAE 多为指标 1"之类宽泛判断，除非绑定教材、模型类别或具体来源。
- 不应把某个来源中的接口算法写成所有 EMT-TS 混合仿真的标准做法。
- 涉及容差、步长、迭代次数、加速比时，必须同时给出来源、模型、平台、基线和工况。
- 未在原文中报告可核验数值结果的指标（如初始化后 CPU 时间节省具体数值），应注明"原文未报告可核验的数值结果"或"待原文核验"。