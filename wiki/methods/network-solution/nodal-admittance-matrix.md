---
title: "节点导纳矩阵 (Nodal Admittance Matrix)"
type: method
tags: [nodal-admittance-matrix, nodal-analysis, sparse-matrix, companion-circuit]
created: "2026-04-13"
updated: "2026-05-18"
---

# 节点导纳矩阵 (Nodal Admittance Matrix)

## 定义与物理背景

节点导纳矩阵（$\mathbf{Y}_n$）是 EMT 仿真中所有节点电压方程的系数矩阵，是整个 [[methods/network-solution/nodal-analysis|节点分析]] 框架的核心数学载体。

对一个有 $N$ 个节点的网络（不含参考节点），节点导纳矩阵 $\mathbf{Y}_n \in \mathbb{C}^{N \times N}$ 定义为：

$$\mathbf{Y}_n \mathbf{v} = \mathbf{i}$$

其中 $\mathbf{v}$ 是节点电压向量，$\mathbf{i}$ 是注入电流向量。

矩阵元素的物理含义：

- **对角元** $Y_{kk}$：与节点 $k$ 相连的所有支路导纳之和（自导纳）
- **非对角元** $Y_{kj} = -y_{kj}$：连接节点 $k$ 和 $j$ 的支路导纳取负（互导纳），仅当两节点直接相连时非零

节点导纳矩阵在 EMT 中的核心性质：

1. **稀疏性**：电网中每个节点平均只与 2–5 个其他节点相连。对于 1000 节点的电网，$\mathbf{Y}_n$ 每行仅 3–6 个非零元素，稀疏度达 99.5% 以上
2. **叠加性**：每个独立元件的贡献可直接累加，无需整体重新推导
3. **对称性**：对不含移相器等非互易元件的网络，$\mathbf{Y}_n$ 为对称矩阵
4. **恒定性**：步长不变时，$\mathbf{Y}_n$ 在仿真过程中保持不变，可复用 LU 分解结果

## 装配规则与叠加原理

对连接节点 $p$ 和 $q$ 的支路导纳 $y$（$p \neq q$），其对 $\mathbf{Y}_n$ 的贡献按**叠加法**规则注入：

$$Y_{pp} \mathrel{+}= y, \quad Y_{qq} \mathrel{+}= y, \quad Y_{pq} \mathrel{-}= y, \quad Y_{qp} \mathrel{-}= y$$

这个装配规则的物理意义：每条导纳支路对两个端节点各提供一个自导纳增量，同时在两节点间引入一个负的互导纳。所有元件独立计算贡献后累加得到最终 $\mathbf{Y}_n$。

装配过程的伪代码：

```text
function assemble_Y_n(elements, n_nodes):
    Y = sparse_matrix(n_nodes, n_nodes)
    for each element in elements:
        p = element.node_p
        q = element.node_q
        g = element.equivalent_conductance()
        if p != 0:        # 节点 0 为参考节点
            Y[p][p] += g
            Y[p][q] -= g
        if q != 0:
            Y[q][q] += g
            Y[q][p] -= g
    return Y
```

## 伴随电路对导纳矩阵的贡献

经 [[methods/numerical-methods/companion-circuit|伴随电路]] 转化后，各元件的时间离散化结果注入 $\mathbf{Y}_n$ 的形式为等效电导。梯形法（Trapezoidal Rule）和后向欧拉法（Backward Euler）给出不同的等效电导：

| 元件 | 参数 | 梯形法 $G_{eq}$ | 后向欧拉法 $G_{eq}$ |
|------|------|-----------------|---------------------|
| 电阻 $R$ | — | $g = 1/R$ | $g = 1/R$ |
| 电感 $L$ | — | $G_L = \Delta t/(2L)$ | $G_L = \Delta t/L$ |
| 电容 $C$ | — | $G_C = 2C/\Delta t$ | $G_C = C/\Delta t$ |
| 开关（闭合） | 大导纳 | $G_{on} = 10^5$ S | $G_{on} = 10^5$ S |
| 开关（断开） | 小导纳 | $G_{off} = 10^{-5}$ S | $G_{off} = 10^{-5}$ S |

梯形法等效电导的推导（以电感 $L$ 为例）：电感电压-电流关系 $v = L \, di/dt$，梯形离散化为

$$\frac{i(t) - i(t-\Delta t)}{\Delta t} = \frac{v(t) + v(t-\Delta t)}{2L}$$

整理得 $i(t) = \underbrace{\frac{\Delta t}{2L}}_{G_L} v(t) + \underbrace{i(t-\Delta t) - \frac{\Delta t}{2L} v(t-\Delta t)}_{i_{hist}(t)}$

其中 $G_L = \Delta t/(2L)$ 为伴随电导，$i_{hist}(t)$ 为历史电流源项。

电感的等效诺顿电路：电导 $G_L$ 与历史电流源 $i_{hist}$ 并联。电容的梯形等效类似，电导 $G_C = 2C/\Delta t$，历史电流源为 $i_{hist}(t) = -G_C v(t-\Delta t) + i(t-\Delta t)$。

## 修改节点分析法的增广矩阵结构

经典节点分析仅以节点电压为未知量。EMT 程序广泛使用**修改节点分析法**（Modified Nodal Analysis, MNA），将独立电压源支路电流也纳入未知量，增广方程为：

$$\mathbf{G} \mathbf{V}(t) = \mathbf{J}(t)$$

其中增广未知量 $\mathbf{V}(t) = \begin{bmatrix} \mathbf{v}_N^T(t) & \mathbf{i}_S^T(t) \end{bmatrix}^T$ 包含：
- $\mathbf{v}_N(t)$：节点电压向量
- $\mathbf{i}_S(t)$：独立电压源支路电流向量

增广右端项 $\mathbf{J}(t) = \begin{bmatrix} \mathbf{i}_{HS}^T(t) & \mathbf{v}_S^T(t) \end{bmatrix}^T$ 包含：
- $\mathbf{i}_{HS}(t)$：电感、电容的历史电流源向量
- $\mathbf{v}_S(t)$：独立电压源电压向量

MNA 方程的矩阵 $\mathbf{G}$ 结构为：

$$\mathbf{G} = \begin{bmatrix} \mathbf{C} & \mathbf{A}_{L,vS} \\ \mathbf{A}_{L,vS}^T & \mathbf{0} \end{bmatrix}$$

其中 $\mathbf{C}$ 是由所有支路导纳构成的节点导纳矩阵（$N \times N$），$\mathbf{A}_{L,vS}$ 是电感-电压源关联矩阵（$N \times n_{vS}$）。

## 描述状态空间方程与节点分析的接口

DSE（Descriptor State-space Equation）方法将电路方程用 MNA 形式在连续时间域写为：

$$\mathbf{E} \dot{\mathbf{x}} = -\mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

其中状态变量 $\mathbf{x} = \begin{bmatrix} \mathbf{v}_N^T & \mathbf{i}_L^T & \mathbf{i}_S^T \end{bmatrix}^T$，输入 $\mathbf{u} = \begin{bmatrix} \mathbf{v}_S^T & \mathbf{j}_S^T \end{bmatrix}^T$。

状态矩阵 $\mathbf{E}$ 可以是奇异的（例如电容与电压源回路会产生奇异性），因此不能简单地转化为标准状态空间形式 $\dot{\mathbf{x}} = \mathbf{A}_{ss}\mathbf{x} + \mathbf{B}_{ss}\mathbf{u}$。奇异 $\mathbf{E}$ 矩阵意味着系统中存在代数约束，描述状态变量之间存在线性依赖关系。

EMT 中常用的两种方程列写方式对比：

| 特性 | 伴随电路法（CC） | 描述状态空间法（DSE） |
|------|----------------|---------------------|
| 未知量 | 节点电压 + 电压源电流 | 节点电压 + 电感电流 + 电压源电流 |
| 矩阵结构 | 对称 $\mathbf{Y}_n$（固定拓扑） | 非对称 $\mathbf{G}$（含电压源关联） |
| 开关处理 | 每次动作需更新 $\mathbf{Y}_n$ | 可通过状态变量直接处理 |
| 特征值分析 | 需后处理附加计算 | 状态空间矩阵可直接求特征值 |
| 实现复杂度 | 低（已被所有商业 EMT 程序采用） | 中（需要 MNA 自动列写） |

## 稀疏矩阵技术与 LU 分解

节点导纳矩阵的稀疏性是 EMT 高效求解的关键。常用稀疏存储格式：

- **CSR（Compressed Sparse Row）**：三数组格式（值、列索引、行指针），最适合行操作和矩阵-向量乘法
- **CSC（Compressed Sparse Column）**：适合列操作为主的算法（如三角求解回代）
- **COO（Coordinate List）**：便于装配，常作为中间格式

LU 分解是 EMT 仿真中单步计算量最大的操作。恒导纳策略的核心是减少分解次数：

1. **符号分解**：分析矩阵稀疏模式，确定 L 和 U 的非零位置，只需一次
2. **数值分解**：根据实际数值计算 L 和 U 因子，步长/拓扑未变时可复用
3. **前代回代**：每步执行 $\mathbf{L}\mathbf{y} = \mathbf{i}$ 和 $\mathbf{U}\mathbf{v} = \mathbf{y}$，复杂度 $O(nnz)$

AMD（Approximate Minimum Degree）重排序的作用：通过选择最优消元顺序，最小化 LU 分解中的填充元数量。Abusalah 等 2020 报告 AMD 排序通常能减少 50–80% 的填充元。

## KLU 求解器与并行增强

KLU 是 EMT 类程序中最流行的稀疏求解器（Ng & Matinpanihar 2012, IEEE Trans on Power Systems）。KLU 的两层分解流程：

**符号分析阶段**（只执行一次）：

```text
输入: 矩阵 A 的稀疏结构
1. 应用 AMD 重排序得到排列矩阵 P 和 Q
2. 计算 A 的块三角形式 (BTF)
3. 确定 L 和 U 的非零模式
输出: 符号因子结构
```

**数值分解阶段**（每步/每次重分解）：

```text
输入: 矩阵 A 的数值和符号结构
1. 对每个 BTF 块 i:
   a. 执行 Gilbert-Peierls 算法定位 L_i 和 U_i 的非零元
   b. 执行左向数值分解（含部分主元）计算 L_i 和 U_i
   c. 主元有效性测试（tolerance ε_p）
      - 若 |new_pivot|/|old_pivot| > ε_p：接受
      - 否则：触发部分重分解
2. 执行前代回代求解
输出: 电压向量 v
```

**BTF（Block Triangular Form）**：将 $\mathbf{A}$ 自动分解为块对角形式 $A_{BTF} = P_r A P_c^T$，各对角块相互独立可在不同线程并行求解。分布式参数线路/电缆模型的自然解耦特性使 BTF 可自动识别子网络边界，无需人工干预。

**EMT 中的 KLU 改进**（Abusalah 等 2020）：

- **主元有效性测试**：定义容差 $\varepsilon_p$，每次重分解时检查 $|a_{new}^{pivot}| / |a_{old}^{pivot}| > \varepsilon_p$ 是否成立；若成立则继续使用原 LU 结构，否则触发部分重分解
- **部分重分解**：仅对受拓扑变化影响的 BTF 块重新执行数值分解，而非全矩阵重分解
- **并行回代**：各 BTF 块的前代回代在独立线程并行执行

KLU 的适用规模：1000–100000 节点。1000 节点以下可用稠密矩阵求解器；100000 节点以上需考虑多级分区策略。

## 参考节点处理与矩阵奇异性

$\mathbf{Y}_n$ 是奇异的（行和为零），因为所有节点电压是相对于参考节点的差值。常见处理方式：

- **直接删去参考节点对应的行和列**：矩阵降为 $(N-1) \times (N-1)$，最常用
- **添加大接地导纳**：在参考节点与其他节点间注入 $G_{ref} = 10^{-9}$ S，数值上近似非奇异
- **浮点参考**：不指定参考节点，用迭代法求解（较少使用）

## 矩阵更新策略与事件处理

| 事件类型 | 对 $\mathbf{Y}_n$ 的影响 | 处理策略 |
|----------|--------------------------|----------|
| 步长变化 | 所有动态元件的 $G_{eq}$ 改变 | 重新数值分解 |
| 开关动作（变导纳） | 开关支路导纳改变 | 更新受影响元素，部分重分解 |
| 开关动作（恒导纳） | $\mathbf{Y}_n$ 不变 | 补偿法修正右端项 |
| 拓扑变化（线路投切） | 矩阵结构改变 | 完整重新分解（符号+数值） |
| 非线性迭代 | 增量电导变化 | 每次牛顿迭代更新 $\mathbf{Y}_n$ |

**补偿法**的核心思想：当开关动作不改变 $\mathbf{Y}_n$ 结构时（恒导纳开关），不重分解 $\mathbf{Y}_n$，而是在右端项 $\mathbf{i}$ 中注入补偿电流修正量 $\Delta \mathbf{i} = \Delta \mathbf{Y}_n \mathbf{v}$，避免昂贵的 LU 重新分解。

## 失效模式与工程经验

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 矩阵病态 | 求解精度丧失 | 大/小导纳并存导致条件数过大 | 合理选择开关电导比（$10^4$–$10^6$） |
| 奇异矩阵 | 求解失败 | 存在浮空节点或纯电压源回路 | 添加对地大电阻或使用增广节点法 |
| 填充元过多 | LU 分解变慢 | 矩阵稀疏模式不佳，AMD 排序无效 | 改用 COLAMD 或其他重排序策略 |
| 频繁重分解 | 仿真速度骤降 | 开关动作频繁，每次需更新矩阵 | 使用恒导纳模型或补偿法 |
| 数值非对称 | 对称求解器不适用 | 含移相器或某些控制环节 | 改用非对称求解器 |

**工程经验值**：

- 开关电导比推荐 $10^5$：$G_{on} = 10^5$ S，$G_{off} = 10^{-5}$ S（基准导纳归一化后）
- KLU 是 1000–100000 节点规模的最优选择
- AMD 排序通常能减少 50–80% 的填充元
- BTF 并行加速比在 4–12 核CPU上可达 3–8×（取决于网络解耦程度）

## 典型两节点示例

电阻 $R_1 = 100\,\Omega$ 连接节点 1 和 2，电阻 $R_2 = 50\,\Omega$ 连接节点 2 和地，电流源 $I_s = 1$ A 注入节点 1。

对 $R_1$（节点 1–2）：$g_1 = 0.01$ S
- $Y_{11} += 0.01$，$Y_{22} += 0.01$，$Y_{12} -= 0.01$，$Y_{21} -= 0.01$

对 $R_2$（节点 2–地）：$g_2 = 0.02$ S
- $Y_{22} += 0.02$

最终矩阵：

$$\mathbf{Y}_n = \begin{bmatrix} 0.01 & -0.01 \\ -0.01 & 0.03 \end{bmatrix}, \quad \mathbf{i} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

求解得 $v_1 = 150$ V，$v_2 = 50$ V。用欧姆定律验证：$I_s = v_1/100 + (v_1 - v_2)/100 = 1.5 + 1.0 = 1$ A ✓

## 来源论文

- [[sources/a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — 对比伴随电路法与描述状态空间方程法在 EMT 仿真中的精度和效率，Sinkar 等，Electric Power Systems Research 2021
- [[sources/accelerated-sparse-matrix-based-computation-of-electromagnetic-transients]] — KLU 稀疏求解器并行化改进（主元有效性测试+部分重分解），Abusalah 等，IEEE Open Access Journal of Power and Energy 2020
- [[sources/a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] — 状态空间-节点分析混合方法，Dufour 等，IEEE TPWRD 2010
- [[sources/2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat]] — 嵌套快速求解中的矩阵复用技术