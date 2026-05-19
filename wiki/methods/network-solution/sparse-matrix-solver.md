title: "稀疏矩阵求解方法 (Sparse Matrix Solver)"
type: method
tags: [sparse-matrix, klu, amd, btf, lu-decomposition, iterative-solver]
created: "2026-04-13"
updated: "2026-05-10"
---

# 稀疏矩阵求解方法 (Sparse Matrix Solver)

## 1. 物理背景与工程需求

### 为什么需要稀疏矩阵求解器？

EMT 仿真每步都需要求解节点方程 $
\mathbf{Y}_n \mathbf{v} = \mathbf{i}$。$\mathbf{Y}_n$ 的大小与电网节点数成正比——一个 1000 节点的系统就是 $1000 \times 1000$ 的矩阵。

如果使用稠密高斯消去法，求解复杂度是 $O(N^3)$，1000 节点需要约 $10^9$ 次浮点运算。但 $\mathbf{Y}_n$ 是高度稀疏的（每行仅 3-6 个非零元素），这就给求解带来了极大的优化空间。

稀疏矩阵求解器的核心思想：**只存储和计算非零元素，跳过所有零元素的操作**。

### 为什么不能直接用稠密求解？

| 节点数 | 稠密存储 | 稀疏存储（每行 5 个非零） | 稠密 LU 运算量 | 稀疏 LU 运算量 |
|--------|----------|--------------------------|----------------|----------------|
| 1000 | 8 MB | 40 KB | $\sim 10^9$ | $\sim 10^5$ |
| 10000 | 800 MB | 400 KB | $\sim 10^{12}$ | $\sim 10^7$ |
| 100000 | 80 GB | 4 MB | $\sim 10^{15}$ | $\sim 10^9$ |

对于大规模电网仿真，稠密求解不仅在存储上不可行，在计算时间上也完全无法接受。


## 2. 数学描述

### LU 分解

$\mathbf{Y}_n \mathbf{v} = \mathbf{i}$ 的标准求解流程分为三步：

1. **符号分解**：分析 $\mathbf{Y}_n$ 的稀疏模式，确定 LU 分解中填充元的位置
2. **数值分解**：计算 $\mathbf{L}$ 和 $\mathbf{U}$ 因子的数值
3. **前代回代**：$\mathbf{Ly} = \mathbf{i}$ 和 $\mathbf{Uv} = \mathbf{y}$

其中符号分解只需做一次（只要矩阵稀疏模式不变），数值分解在步长/拓扑不变时可复用。

### 填充元

填充元是稀疏矩阵 LU 分解中的核心概念。即使 $\mathbf{Y}_n$ 是稀疏的，$\mathbf{L}$ 和 $\mathbf{U}$ 中也会出现 $\mathbf{Y}_n$ 中原本为零的位置——这些就是填充元。

填充元的存在意味着：**$\mathbf{L} + \mathbf{U}$ 可能比 $\mathbf{Y}_n$ 稠密得多**。通过重排序来最小化填充元是稀疏矩阵技术的核心。


## 3. 计算模型与离散化

### 关键算法

**AMD（Approximate Minimum Degree）重排序**：

AMD 通过贪心策略选择度最小的节点进行消去，目标是减少 LU 分解中的填充元数量。对于电力系统节点导纳矩阵，AMD 通常能减少 50-80% 的填充元。

**BTF（Block Triangular Form）**：

BTF 将矩阵重排为块对角形式，使得对角块独立求解。对于分网仿真的场景，BTF 可以将大矩阵分解为多个小矩阵并行求解。

**KLU 求解器**：

KLU 是专门为电路仿真设计的稀疏求解器，是 EMTP 类程序的标准选择。它结合了 BTF 预处理、AMD 重排序和左看 LU 分解。

### 求解器对比

| 求解器 | 适用规模 | 特性 | EMT 适用性 |
|--------|----------|------|-----------|
| KLU | $10^3 \sim 10^5$ | 电路优化，BTF+AMD | EMTP 标准选择 |
| SuperLU | $10^4 \sim 10^6$ | 通用，支持分布式 | 大规模离线仿真 |
| PARDISO | $10^4 \sim 10^6$ | 共享内存并行 | 多核 EMT 仿真 |
| MUMPS | $10^5 \sim 10^7$ | 分布式并行 | 超大规模 EMT |
| 迭代法（GMRES） | $10^5 \sim 10^7$ | 无需分解，收敛依赖预条件 | 适合对角占优系统 |


## 4. 实现方法与算法细节

### 符号分解 vs 数值分解

符号分解与数值分解的分离是稀疏矩阵技术的关键：

```text
仿真开始：
  1. 符号分解（一次）：分析稀疏模式，计算填充元位置，分配存储
  2. 数值分解（初次）：计算 L 和 U 因子的数值
  3. 每时步：前代回代（复用 L 和 U）

开关动作（变导纳模型）：
  4. 局部更新：只修改受影响的行/列
  5. 部分重分解：只重新计算受影响的 L/U 部分

步长变化：
  6. 完全数值重分解（符号分解可复用）
```

### 部分重分解

当开关动作只影响少数支路时，不需要对完整矩阵重新做 LU 分解。部分重分解只更新被修改的行/列对应的 L/U 因子，计算量与受影响节点数成正比。

### 补偿法的替代方案

如果不希望修改矩阵（恒导纳策略），补偿法通过 Sherman-Morrison-Woodbury 公式修正右端项来模拟开关效果：

$$
(\mathbf{Y}_n + \Delta \mathbf{Y})^{-1} \mathbf{i} \approx \mathbf{Y}_n^{-1} \mathbf{i} - \mathbf{Y}_n^{-1} \Delta \mathbf{Y} (\mathbf{I} + \mathbf{Y}_n^{-1} \Delta \mathbf{Y})^{-1} \mathbf{Y}_n^{-1} \mathbf{i}
$$

这避免了矩阵重分解，代价是需要额外的矩阵-向量乘和小规模线性求解。


## 5. 适用边界与失效模式

### 什么条件下好？

- 电网规模大但连接稀疏（稀疏度 $> 99\%$）
- $\mathbf{Y}_n$ 结构稳定（符号分解可复用）
- 节点导纳矩阵对角占优（迭代法收敛快）

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 填充元爆炸 | LU 分解内存暴增 | 矩阵结构不佳，AMD 无效 | 换用更好的重排序或近似分解 |
| 矩阵病态 | 求解精度丧失 | 大/小导纳共存 | 改善开关电导比或预处理 |
| 迭代法不收敛 | GMRES 残差卡住 | 矩阵非对角占优 | 使用直接法或改善预条件 |
| 频繁重分解 | 仿真速度慢 | 开关动作密集 | 使用恒导纳 + 补偿法 |
| 并行效率低 | 多核加速比差 | BTF 块太小导致负载不均 | 合并小块或重新分网 |

### 工程经验值

- 1000-50000 节点：KLU 是最优选择
- $> 50000$ 节点：考虑 SuperLU 或迭代法
- AMD 排序通常减少 50-80% 填充元
- BTF 分解后对角块大小与分网策略相关


## 6. 应用说明

### 简单示例

对两节点电路：

$$
\mathbf{Y}_n = \begin{bmatrix} 0.01 & -0.01 \\ -0.01 & 0.03 \end{bmatrix}
$$

LU 分解：

$$
\mathbf{L} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix},
\quad
\mathbf{U} = \begin{bmatrix} 0.01 & -0.01 \\ 0 & 0.02 \end{bmatrix}
$$

前代 $\mathbf{Ly} = \mathbf{i} = [1, 0]^T$：$y_1 = 1$，$y_2 = 1$

回代 $\mathbf{Uv} = \mathbf{y}$：$v_2 = 50$，$v_1 = 150$

本例中 $\mathbf{Y}_n$ 极小，没有填充元问题。实际大规模系统中，AMD 重排前后填充元数量可相差 5-10 倍。


## 7. 延伸阅读

### 核心参考文献

- [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat]] — 嵌套求解中的矩阵复用技术
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] — 状态空间与节点方程结合中的矩阵处理
- [[accurate-time-domain-simulation-of-power-electronic-circuits]] — 功率电子仿真中的稀疏矩阵技术

### 相关页面

- [[nodal-admittance-matrix]] — 节点导纳矩阵的构造
- [[nodal-analysis]] — 节点分析法框架
- [[companion-circuit]] — 伴随电路与矩阵装配
- [[fixed-admittance]] — 恒导纳策略避免重分解
- [[compensation-method]] — 补偿法的矩阵修正原理
- [[parallel-computing]] — 并行求解技术


## 8. 稀疏求解器的EMT并行化与实时化

### 8.1 KLU求解器的EMT并行化（Abusalah 2019）

Abusalah等(2019)针对EMT仿真中稀疏矩阵求解的计算瓶颈，将KLU求解器与并行计算结合，实现无需用户干预的自动网络并行化。

**核心方法**：修正增广节点分析法(MANA)构建网络方程$\mathbf{A}\mathbf{x}=\mathbf{b}$，通过块三角分解(BTF)自动识别由分布参数线路解耦的子网络块，主元有效性检验（容差1%）避免90%以上的无效全量重分解，部分重分解技术仅更新变化列。

**KLU并行化架构**：
$$$\mathbf{A}_{BTF} = P_R \mathbf{A} P_C$$$

其中$P_R$、$P_C$为行列置换矩阵，将原矩阵转化为块对角形式。NFPO(浮点运算量)估算各子块计算量，实现基于OpenMP的动态负载均衡。

**量化性能**：
- Hydro-Québec电网(HQ-grid)：41815阶矩阵，217子块，12核并行下SMPEMT2耗时31s，较传统EMTP单核(1048s)加速33.8倍
- 含风电IGBT模型T0-grid：4703阶矩阵，12核并行下204s，较EMTP(2580s)加速12.6倍
- 主元有效性检验避免90%以上无效全量重分解

### 8.2 实时EMT仿真的MKLU求解器（Bruned 2023）

Bruned等(2023)将改进的KLU(MKLU)集成到工业级实时仿真环境HYPERSIM中，替代传统GenCode求解器。

**核心方法**：填充元减少(AMD/COLAMD/Nested Dissection)降低LU分解非零元；部分重分解(RefactChg/RefactVarOpt)仅重构变化列；部分选主元策略确保数值稳定性；结合传输线延迟解耦(LD)和补偿法(CM)实现并行实时求解。

**矩阵分块重排序**：
$$$	ilde{\mathbf{Y}}_n = P_n \mathbf{Y}_n Q_n$$$

**固定-时变分块结构**：
$$$\mathbf{Y}_n = egin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$$$

其中$Y_f$为线性元件子矩阵（固定），$Y_v$为时变元件子矩阵（开关、非线性）。

**量化性能**：
- Xavier配电网(619节点)：50μs步长，CM并行，性能提升最高达50%
- GHOST微电网(663节点)：100μs步长，孤岛模式切换，部分选主元确保数值稳定性
- RefactVarOpt将重分解限制在右下角$Y_v$块，显著减少重构列数

### 8.3 选主元与数值稳定性

EMT仿真中，开关建模为$R_{open}/R_{close}$极端导纳比会导致近零主元。部分选主元(partial pivoting)在每列选择绝对值最大元素作为主元：

$$$|a_{ pivot}| = \max_{i \geq k} |a_{ik}|$$

**无选主元风险**：传统GenCode求解器在开关动作时可能数值不稳定。

**选主元收益**：确保含开关的复杂电网仿真在每个时间步的数值稳定。

## 9. 来源论文

- [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat|Nested Fast and Simultaneous Solution]] (Strunz & Carlson, 2006) — GENE嵌套求解框架，稀疏矩阵复用，实时CIGRE HVDC基准
- [[accelerated-sparse-matrix-based-computation-of-electromagnetic-transients|Abusalah et al. 2019]] — KLU并行化，BTF自动分块，主元检验，部分重分解，12核39倍加速
- [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Bruned et al. 2023]] — MKLU工业实时集成，AMD/COLAMD排序，部分重分解，HYPERSIM HIL验证，50%性能提升
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|Degaudenzi & Pare 2011]] — 状态空间与节点分析结合
- [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|McNaught & Zovan 2011]] — FPGA实时非线性EMT求解
- [[parallel-massive-thread-electromagnetic-transient-simulation-on-gpu|Liu & Pil 2014]] — GPU大规模EMT并行
- [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|Mudunkotuwa & Filizadeh 2018]] — CPU多核并行EMT
- [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Noda 2018]] — 频率相关特性法加速
- [[a-parallelization-in-time-approach-for-accelerating-emt-simulations|Zhang et al. 2021]] — 时间并行EMT加速
- [[partial-refactorization-techniques-for-electromagnetic-transient-simulations|Ferrand et al. 2025]] — 部分重分解技术最新进展
