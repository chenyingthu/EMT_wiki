---
title: "代数表征法 (Algebraic Characterization)"
type: method
tags: [algebraic, characterization, implicit, equation, dae, sparse-matrix]
created: "2026-05-02"
updated: "2026-05-16"
---

# 代数表征法 (Algebraic Characterization)

## 定义与边界

代数表征法（Algebraic Characterization）是把 EMT 模型在某一时间步或某一接口处整理成可求解的代数关系。它不是把动态过程"静态化"，而是通过隐式积分、端口等效、变量消去或约束组装，把连续方程和网络约束转成残差形式：

$$\mathbf{R}(\mathbf{z}_{n+1};\mathbf{z}_{n},\mathbf{p},t_{n+1})=\mathbf{0},$$

其中 $\mathbf{z}_{n+1}$ 可包含节点电压、支路电流、设备状态、控制变量和接口量，$\mathbf{p}$ 表示参数、拓扑和开关状态。若残差为线性，问题可直接进入稀疏矩阵求解；若残差为非线性，则通常需要 [[newton-raphson-method]] 或其他非线性求解器。

代数表征法是 [[time-domain-formulation]] 与 [[sparse-matrix-solver]]、DAE 求解器之间的中间层。它关注"方程如何被组织成代数求解问题"，不把某种稀疏矩阵格式、某个 DAE 工具或某个商业程序写成唯一标准。

## EMT 中的作用

EMT 主循环在每个时间步都要把元件历史、网络拓扑和控制状态合并。代数表征法使这些异质模型能够进入同一个求解接口：

1. **动态元件经积分后成为等效电导和历史源**：电感变成伴随电导 $G_{eq}=2\Delta t/L$，电容变成历史电流源
2. **线路、FDNE 和电缆模型经时延或递归卷积生成当前步注入量**
3. **电机、换流器和外部网络可通过 Norton、Thevenin 或多端口等效暴露端口关系**
4. **非线性元件通过局部线性化或残差方程联立求解**

## 核心机制

### 机制1：隐式离散

若连续模型为：

$$\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},t),\quad \mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},t),$$

用隐式积分替换 $\dot{\mathbf{x}}$ 后，可形成残差方程：

$$\mathbf{R}_{n+1}=\begin{bmatrix}\mathbf{r}_x(\mathbf{x}_{n+1},\mathbf{y}_{n+1})\\ \mathbf{g}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})\end{bmatrix}=\mathbf{0}.$$

梯形积分下，状态残差的一般形式为：

$$\mathbf{r}_x=\mathbf{x}_{n+1}-\mathbf{x}_n-\frac{\Delta t}{2}\left[\mathbf{f}(\mathbf{x}_n,\mathbf{y}_n,t_n)+\mathbf{f}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})\right].$$

后向欧拉格式则简化为：

$$\mathbf{r}_x=\mathbf{x}_{n+1}-\mathbf{x}_n-\Delta t\cdot\mathbf{f}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1}).$$

### 机制2：节点导纳表征（MANA）

修正增广节点分析法（Modified Augmented Nodal Analysis, MANA）将所有支路方程统一写为节点电压形式：

$$\mathbf{i}_{port,n+1}=\mathbf{G}_{eq}\mathbf{v}_{port,n+1}+\mathbf{i}_{hist,n+1}.$$

组装到网络后得到系统方程：

$$\mathbf{Y}\mathbf{v}=\mathbf{i}_{inj}.$$

这里的 $\mathbf{Y}$ 不是纯拓扑对象，而是包含电阻、伴随电导、端口等效、开关状态和部分控制接口的代数结果。

Abusalah 等（2019）将 MANA 与稀疏矩阵求解结合，提出通过块三角分解（BTF）自动识别由分布参数线路解耦的子网络块，实现无需用户干预的自动拓扑划分。

### 机制3：端口等效（诺顿/戴维南）

子网络的端口代数表征将其内部结构隐藏为等效电源加导纳/阻抗：

**诺顿等效**：

$$\mathbf{i}_{port}=\mathbf{Y}_{eq}\mathbf{v}_{port}+\mathbf{i}_{eq}.$$

**戴维南等效**：

$$\mathbf{v}_{port}=\mathbf{Z}_{eq}\mathbf{i}_{port}+\mathbf{v}_{eq}.$$

两种等效形式可通过以下关系互换：

$$\mathbf{Y}_{eq}=\mathbf{Z}_{eq}^{-1},\qquad \mathbf{i}_{eq}=\mathbf{Y}_{eq}\mathbf{v}_{eq}.$$

在 MMC/FNEC 等多端口等效中，常用嵌套诺顿—戴维南互换将子模块状态递归消去，仅保留端口变量。

### 机制4：变量消去（Schur补）

当模型包含内部节点和外部端口时，按分块矩阵表示：

$$\begin{bmatrix}\mathbf{Y}_{ee} & \mathbf{Y}_{ei}\\ \mathbf{Y}_{ie} & \mathbf{Y}_{ii}\end{bmatrix}\begin{bmatrix}\mathbf{v}_e\\ \mathbf{v}_i\end{bmatrix}=\begin{bmatrix}\mathbf{i}_e\\ \mathbf{i}_i\end{bmatrix}.$$

若 $\mathbf{Y}_{ii}$ 可逆，消去内部节点得到端口等效（Schur补）：

$$\mathbf{Y}_{eq}=\mathbf{Y}_{ee}-\mathbf{Y}_{ei}\mathbf{Y}_{ii}^{-1}\mathbf{Y}_{ie}.$$

这类消去可以降低主网络规模，但必须保留回代信息，否则内部状态、能量和测量量可能丢失。

## EMT建模方法

### 方法1：线性代数网络（固定拓扑）

对于线性网络，$\mathbf{Y}$ 固定不变，每时间步只需更新历史源 $\mathbf{i}_{hist}$：

$$\mathbf{Y}\mathbf{v}_{n+1}=\mathbf{i}_{inj,n+1}+\mathbf{i}_{hist,n+1}.$$

典型应用：固定拓扑的 RLC 网络、实时仿真中的恒定伴随电导。

代表论文：Abusalah 2019 指出，KLU 稀疏求解器在固定拓扑下可缓存 LU 分解结果，仅通过部分重分解（partial refactorization）更新动态列。

### 方法2：非线性残差迭代

非线性元件通过残差方程联立牛顿迭代求解：

$$\mathbf{R}(\mathbf{z}_{n+1})=\mathbf{0}\Rightarrow \mathbf{J}\Delta\mathbf{z}=-\mathbf{R},\quad \mathbf{z\leftarrow z}+\Delta\mathbf{z}.$$

其中雅可比矩阵 $\mathbf{J}=\partial\mathbf{R}/\partial\mathbf{z}$。

收敛判断准则：
$$\|\mathbf{R}(\mathbf{z}_{n+1})\|<\epsilon_{abs}\quad \text{或}\quad \frac{\|\mathbf{R}\|}{\|\mathbf{R}_0\|}<\epsilon_{rel}.$$

### 方法3：端口诺顿/戴维南等效（多速率接口）

外部网络、MMC 或电机等子系统通过诺顿/戴维南等效暴露端口变量，实现与主网络的接口：

- **诺顿接口**：$\mathbf{i}_{port}=\mathbf{Y}_{eq}\mathbf{v}_{port}+\mathbf{i}_{eq}$，注入主网络
- **戴维南接口**：$\mathbf{v}_{port}=\mathbf{Z}_{eq}\mathbf{i}_{port}+\mathbf{v}_{eq}$

在多速率仿真中，子系统以大步长 $\Delta T$ 更新等效参数，主网络以小步长 $\Delta t$ 求解。

### 方法4：补偿法（解耦非线性元件）

补偿法将非线性元件从主网络解耦，通过迭代补偿其影响：

对非线性电阻 $i=f(v)$，其在第 $k$ 次迭代的补偿电流为：

$$\Delta \mathbf{i}^{(k)}=\mathbf{Y}_{eq}\Delta\mathbf{v}^{(k)}.$$

主子网络保持不变，仅在迭代过程中注入补偿量。

### 方法5：DAE方程导向表征（Modelica/FMI）

保持元件级隐式方程，由工具链统一排序求解：

$$\mathbf{M}\dot{\mathbf{z}}=\mathbf{f}(\mathbf{z},\mathbf{u},t),\quad \mathbf{0}=\mathbf{g}(\mathbf{z},\mathbf{u},t).$$

优势在于保持方程语义，不强制写成 $A\mathbf{x}=\mathbf{b}$ 形式，便于模型复用和连接。

代表论文：MSEMT Modelica库将电力系统元件组织为隐式 DAE，通过 FMI 接口与主 EMT 程序交换数据。

## 形式化表达

**隐式积分残差（一般形式）**：

$$\mathbf{R}_{n+1}=\begin{bmatrix}\mathbf{x}_{n+1}-\mathbf{x}_n-\frac{\Delta t}{2}\left[\mathbf{f}(\mathbf{x}_n,\mathbf{y}_n)+\mathbf{f}(\mathbf{x}_{n+1},\mathbf{y}_{n+1})\right]\\ \mathbf{g}(\mathbf{x}_{n+1},\mathbf{y}_{n+1})\end{bmatrix}=\mathbf{0}.$$

**MANA 节点方程**：

$$\mathbf{Y}\mathbf{v}=\mathbf{i}_{inj}+\mathbf{i}_{hist}.$$

**Schur补端口等效**：

$$\mathbf{Y}_{eq}=\mathbf{Y}_{ee}-\mathbf{Y}_{ei}\mathbf{Y}_{ii}^{-1}\mathbf{Y}_{ie}.$$

**诺顿等效端口方程**：

$$\mathbf{i}_{port}=\mathbf{Y}_{eq}\mathbf{v}_{port}+\mathbf{i}_{eq}.$$

**戴维南等效端口方程**：

$$\mathbf{v}_{port}=\mathbf{Z}_{eq}\mathbf{i}_{port}+\mathbf{v}_{eq}.$$

**牛顿迭代格式**：

$$\begin{bmatrix}\frac{\partial\mathbf{R}}{\partial\mathbf{z}}\end{bmatrix}\Delta\mathbf{z}^{(k)}=-\mathbf{R}(\mathbf{z}^{(k)}),\quad \mathbf{z}^{(k+1)}=\mathbf{z}^{(k)}+\Delta\mathbf{z}^{(k)}.$$

## 关键技术挑战

### 挑战1：变拓扑的矩阵重分解开销

每次开关动作或拓扑变化都需要更新 $\mathbf{Y}$ 并重新执行 LU 分解，计算代价高。

**策略**：主元有效性检验（pivot validity check）避免无意义的重分解；部分重分解仅更新变化列的因子。

### 挑战2：非线性迭代的收敛性

雅可比矩阵病态或初值远离解域时，牛顿迭代可能出现不收敛或振荡。

**策略**：步长回退（step-size backtracking）、线搜索（line search）、弧长延拓（arc-length continuation）。

### 挑战3：端口等效的频带和精度权衡

用诺顿/戴维南等效替代完整子系统时，等效参数通常只在校替频率范围内准确，跨频率会产生误差。

**策略**：多频带等效（multi-band equivalent）、分段线性化、接口误差监测。

### 挑战4：Schur补消去的信息丢失

消去内部节点后，内部状态（磁链、能量）无法从端口变量直接恢复。

**策略**：保留内部状态回代路径；在等效中加入状态观测器。

### 挑战5：DAE指标方程的奇异性

微分-代数方程中的约束方程可能使系统矩阵奇异，导致求解器失败。

**策略**：指标约简（index reduction）、 Baumgarte 稳定性化、增广系统法。

## 量化性能边界

| 表征形式 | 适用场景 | 矩阵规模 | 计算效率 | 精度 |
|---------|---------|---------|---------|------|
| 线性代数网络（固定 $\mathbf{Y}$） | RLC网络、实时仿真 | 中等 | 最高 | 取决于步长 |
| 非线性残差迭代 | 饱和、避雷器、电力电子 | 中等 | 中（牛顿迭代） | 高 |
| 端口诺顿/戴维南 | 外部网络、机电接口 | 可降阶 | 高 | 等效频带内 |
| 补偿法 | 解耦非线性元件 | 不增维 | 高 | 迭代精度 |
| 方程导向DAE | Modelica/FMI跨域 | 大 | 取决于求解器 | 保留方程语义 |

**来源**：Abusalah 2019 报告 HQ-grid 在12核并行下实现39倍加速，主元有效性检验避免90%以上无效全量重分解；MSEMT库用 Modelica DAE 保持隐式方程语义，便于跨域建模。

## 适用边界与选择指南

| 场景 | 推荐表征形式 | 原因 |
|------|------------|------|
| 固定拓扑线性网络 | 线性代数网络 | 无需迭代，直接求解 |
| 非线性元件主导 | 非线性残差迭代 | 牛顿法收敛快 |
| 外部网络接口 | 端口诺顿/戴维南 | 实现多速率仿真 |
| 非线性元件解耦 | 补偿法 | 主子网络不变 |
| 跨域建模/多物理场 | 方程导向DAE | 保持方程语义 |
| 大规模稀疏系统 | MANA+BTF+稀疏求解 | 自动分块并行 |

## 与相关页面的关系

- [[time-domain-formulation]]：提供连续时域方程来源
- [[dae-solvers]]：求解代数表征形成的隐式残差
- [[newton-raphson-method]]：非线性代数表征的常用迭代内核
- [[compensation-method]]：通过端口等值和接口变量实现分离求解
- [[norton-equivalent]]：端口代数表征的基础形式
- [[thevenin-equivalent]]：端口代数表征的另一种基础形式
- [[sparse-matrix-solver]]：大规模线性代数表征的计算后端
- [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us]]：多端口 MMC 子模块通过 Schur 补递归消去内部节点

## 来源论文

- **Abusalah 等 2019** — 基于稀疏矩阵求解的 EMT 自动并行加速（IEEE Open Access J. Power Energy）：提出 MANA+BTF 自动拓扑划分和部分重分解技术，在 Hydro-Québec 23181支路/349机系统中实现12核39倍加速
- **Yonezawa 2023** — 基于磁路表示的相域同步机建模技术（Electric Power Systems Research）：将同步机时变电感矩阵用受控源映射为磁路网络，实现相域与 EMT 程序的兼容性
- **Noda 2015** — 频域分区拟合的相域频变线路建模（IEEE TPWRD）：将 FpF 方法引入 ULM 相域线路建模，最大拟合偏差降至 $1.2\times 10^{-3}$
- **MSEMT Modelica库** — 电力系统电磁暂态高级 Modelica 库（学术论文）：将元件和连接关系组织为隐式 DAE，通过 FMI 接口与 EMT 程序集成