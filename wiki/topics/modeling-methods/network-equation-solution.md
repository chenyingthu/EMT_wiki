---
title: "网络方程的建立与求解 (Network Equation Formulation and Solution)"
type: topic
tags: [network-equation, nodal-analysis, admittance-matrix, switch-handling, sparse-matrix, iterative-solver]
created: "2026-05-01"
book-chapter: "3"
---

# 网络方程的建立与求解 (Network Equation Formulation and Solution)

## 概述

网络方程的建立与求解是EMT仿真的核心计算环节。在每个仿真时步，EMT软件需要将电力系统中的各种元件（发电机、变压器、线路、负荷、电力电子设备等）转化为等效电路模型，组装成节点导纳矩阵，并求解大型稀疏线性方程组得到节点电压。这一过程决定了仿真的精度、效率和可扩展性。

在EMT语境下，网络方程求解面临独特挑战：需要处理开关事件导致的拓扑频繁变更、非线性元件的迭代求解、大规模系统的稀疏矩阵技术，以及实时仿真的确定性延迟要求。理解这些技术的原理和适用边界，是掌握EMT仿真的关键。

## 形式化表达

### 基本节点电压方程

EMT仿真采用改进增广节点分析法（Modified Augmented Nodal Analysis, MANA），统一的矩阵形式为：

$$
\begin{bmatrix} \mathbf{Y}_n & \mathbf{A} \\ \mathbf{B} & \mathbf{C} \end{bmatrix}
\begin{bmatrix} \mathbf{v} \\ \mathbf{i}_x \end{bmatrix} =
\begin{bmatrix} \mathbf{j} \\ \mathbf{e} \end{bmatrix}
$$

其中：
- $\mathbf{Y}_n \in \mathbb{R}^{n \times n}$：节点导纳矩阵（Nodal Admittance Matrix）
- $\mathbf{v} \in \mathbb{R}^n$：节点电压向量
- $\mathbf{j} \in \mathbb{R}^n$：注入电流源向量
- $\mathbf{i}_x$：附加支路电流（如电压源、电感等需要增广的变量）

### 伴随电路离散化

各动态元件通过数值积分转换为伴随电路（Companion Circuit）：

**电感元件（梯形积分法，Trapezoidal Rule）**：

$$
i_L(t) = G_{eq,L} \, v_L(t) + I_{hist,L}, \quad G_{eq,L} = \frac{\Delta t}{2L}
$$

$$
I_{hist,L} = i_L(t-\Delta t) + \frac{\Delta t}{2L} \, v_L(t-\Delta t)
$$

**电容元件（梯形积分法）**：

$$
i_C(t) = G_{eq,C} \, v_C(t) + I_{hist,C}, \quad G_{eq,C} = \frac{2C}{\Delta t}
$$

$$
I_{hist,C} = -\left[ \frac{2C}{\Delta t} v_C(t-\Delta t) + i_C(t-\Delta t) \right]
$$

**阻尼历史项的统一形式**：

对于任意动态元件，其历史电流项可统一写为：

$$
I_{hist} = \alpha \, x(t-\Delta t) + \beta \, v(t-\Delta t)
$$

其中 $(\alpha, \beta)$ 由数值积分方法决定（梯形法：$\alpha=1, \beta=\Delta t/2L$；后向欧拉法：$\alpha=1, \beta=\Delta t/L$）。

**导纳矩阵组装**：

$$
\mathbf{Y}_n = \mathbf{A}_a \mathbf{Y}_b \mathbf{A}_a^{\mathsf{T}}
$$

其中：$\mathbf{A}_a$ 为节点-支路关联矩阵，$\mathbf{Y}_b$ 为支路导纳对角矩阵。

### 非线性元件的牛顿-拉夫逊迭代

求解非线性方程 $F(x) = 0$ 的迭代格式为：

$$
\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - \mathbf{J}^{-1}(\mathbf{x}^{(k)}) \mathbf{F}(\mathbf{x}^{(k)})
$$

其中雅可比矩阵 $\mathbf{J} \in \mathbb{R}^{n \times n}$ 为：

$$
J_{ij} = \frac{\partial F_i}{\partial x_j}
$$

**饱和变压器的牛顿迭代**：

非线性磁化特性 $\Phi = f(i_m)$ 的迭代格式为：

$$
i_m^{(k+1)} = i_m^{(k)} - \frac{\Phi(i_m^{(k)}) - \Phi_{target}}{d\Phi/di_m}
$$

**简化牛顿法（固定雅可比）**：

$$
\mathbf{J}_0 \, \Delta\mathbf{x}^{(k)} = -\mathbf{F}(\mathbf{x}^{(k)})
$$

减少LU分解次数，适用于弱非线性系统。

## 核心机制

### 1. 节点导纳矩阵的构建

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 380" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景 -->
  <rect width="900" height="380" fill="#fafafa"/>
  
  <!-- 标题 -->
  <text x="450" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#333">图1 · EMT网络方程求解流程</text>
  
  <!-- 第1层: 输入 -->
  <rect x="30" y="45" width="840" height="55" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="450" y="60" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1e40af">输入</text>
  <text x="130" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">网络拓扑</text>
  <text x="310" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">元件参数</text>
  <text x="450" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">时间步长Δt</text>
  <text x="600" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">开关状态</text>
  <text x="760" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">边界条件</text>
  
  <!-- 箭头1 -->
  <line x1="450" y1="100" x2="450" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <!-- 第2层: 元件离散化 -->
  <rect x="30" y="120" width="840" height="55" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="450" y="135" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#166534">步骤1 · 元件离散化（伴随电路）</text>
  <text x="130" y="153" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">电感: Geq=Δt/2L</text>
  <text x="310" y="153" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">电容: Geq=2C/Δt</text>
  <text x="480" y="153" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">电阻/开关: Geq=1/R</text>
  <text x="650" y="153" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">电压源→增广</text>
  <text x="800" y="153" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">历史项Ihist</text>
  
  <!-- 箭头2 -->
  <line x1="450" y1="175" x2="450" y2="195" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <!-- 第3层: 矩阵组装 -->
  <rect x="30" y="195" width="840" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="450" y="210" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#92400e">步骤2 · 矩阵组装 Y<tspan baseline-shift="sub" font-size="8">n</tspan>=A<tspan baseline-shift="sub" font-size="8">a</tspan>Y<tspan baseline-shift="sub" font-size="8">b</tspan>A<tspan baseline-shift="sub" font-size="8">a</tspan><tspan baseline-shift="super" font-size="8">T</tspan></text>
  <text x="200" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">建立关联矩阵A<tspan baseline-shift="sub" font-size="8">a</tspan></text>
  <text x="400" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">组装Y<tspan baseline-shift="sub" font-size="8">n</tspan>→CSC格式</text>
  <text x="600" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">注入向量Iinj</text>
  <text x="780" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">边界条件处理</text>
  
  <!-- 箭头3 -->
  <line x1="450" y1="250" x2="450" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <!-- 第4层: 求解 -->
  <rect x="30" y="270" width="840" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="450" y="285" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#5b21b6">步骤3 · 线性方程组求解 Ax=b</text>
  <text x="130" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">N&lt;1000: KLU直接</text>
  <text x="320" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">N&lt;10000: KLU+AMD</text>
  <text x="510" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">N≥10000: GMRES+ILU</text>
  <text x="700" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">实时: 恒导纳+查表</text>
  
  <!-- 箭头4 -->
  <line x1="450" y1="325" x2="450" y2="345" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <!-- 第5层: 输出 -->
  <rect x="30" y="345" width="840" height="30" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="450" y="365" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#991b1b">输出: 节点电压v → 更新历史电流项 → 下一时步</text>
  
  <!-- 箭头标记 -->
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EMT网络方程求解流程：拓扑输入→元件离散化→矩阵组装→方程求解→状态更新</p>

### 2. 开关事件处理：拓扑变更的方法

#### 变导纳方法（Variable Admittance）

开关状态改变时直接修改导纳矩阵：
- **闭合**：$G_{sw} = G_{on}$（大电导，如 $10^6$ S）
- **断开**：$G_{sw} = G_{off}$（小电导，如 $10^{-6}$ S）

**问题**：每次开关动作都需要重新分解导纳矩阵，计算开销大。

#### 临界阻尼调整（CDA）

在开关事件点插入半步长后向欧拉（Backward Euler）：

$$
x\!\left(t + \frac{\Delta t}{2}\right) = x(t) + \frac{\Delta t}{2} \, f\!\left(t + \frac{\Delta t}{2}, x\!\left(t + \frac{\Delta t}{2}\right)\right)
$$

**作用**：
- 抑制梯形法数值振荡
- 保持整体2阶精度
- 需要检测开关事件

#### 恒定导纳矩阵技术（ADC模型）

通过约束开关等效电感电容乘积等于时间步长平方：

$$
L_{sw} \, C_{sw} = (\Delta t)^2
$$

确保开关状态变化时系统导纳矩阵保持不变。Abusalah等（2020）将此技术与并行稀疏矩阵求解结合，实现变拓扑网络的自动并行化。

#### 预计算策略（GENE方法）

- 枚举子模块所有开关状态组合（$2^N$ 种，N为开关数）
- 为每种组合预存LU分解结果
- 运行时直接查表，查找时间 $<1\,\mu\text{s}$（Gnanarathna等，2006）

#### 插值精确化开关时刻

$$
t_{sw} = t_n + \frac{v_{sw} - v(t_n)}{v(t_{n+1}) - v(t_n)} \, \Delta t
$$

### 3. 非线性元件的处理：迭代法 vs 线性化

#### 分段线性化（Piecewise Linear）

将非线性V-I特性分段线性近似：

| 区域 | 特性 | 等效参数 |
|------|------|---------|
| 导通区 | 线性 | $R = R_{on}$ |
| 关断区 | 线性 | $R = R_{off}$ |
| 过渡区 | 线性插值 | $R = f(v)$ |

#### 预测-校正策略（Predictor-Corrector）

$$
\text{Predictor}: \quad \mathbf{x}^{(0)} = \mathbf{x}_n + h \, \mathbf{f}(\mathbf{x}_n) \quad \text{（显式欧拉）}
$$

$$
\text{Corrector}: \quad \mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - \mathbf{J}^{-1} \mathbf{F}(\mathbf{x}^{(k)})
$$

### 4. 稀疏矩阵技术

#### 稀疏性原理

电力系统导纳矩阵的稀疏特性（Abusalah等，2020）：

| 系统规模 | 非零元素占比 |
|----------|-------------|
| 100节点 | ~2% |
| 1,000节点 | ~0.5% |
| 10,000节点 | ~0.05% |

#### 稀疏存储格式

| 格式 | 存储方式 | 适用场景 |
|------|----------|----------|
| COO | (行,列,值)三元组 | 构建阶段 |
| CSR | 行指针+列索引+值 | 行访问频繁 |
| CSC | 列指针+行索引+值 | 列访问频繁（EMT常用）|

#### LU分解与填充元控制

**最小度算法（AMD）**：
- 每次选择度数最小的节点进行消去
- 目标：最小化填充元数量
- 比精确MD快10-100倍，质量接近（Abusalah等，2020）

**BTF预处理（块三角形式）**：

$$
\mathbf{P}^{\mathsf{T}} \mathbf{Y} \mathbf{Q} = \begin{bmatrix} \mathbf{A}_{11} & & \\ \mathbf{A}_{21} & \mathbf{A}_{22} & \\ \vdots & \vdots & \ddots \end{bmatrix}
$$

#### KLU求解器流程

KLU是针对电路仿真优化的高性能稀疏求解器（Abusalah等，2020）：

```
1. AMD排序（首次）：最小度排序建立消去顺序
2. BTF分解（首次）：块三角形式分解
3. 符号分解（首次）：确定L/U结构
4. 数值分解（拓扑变化时）：计算L/U数值
5. 前代回代（每步执行）：代入右端项求解
```

### 5. 直接法 vs 迭代法

| 特性 | 直接法（LU分解） | 迭代法（Krylov子空间） |
|------|-----------------|----------------------|
| 计算复杂度 | $O(N^3)$（稠密），$O(N^{1.2})$（稀疏） | $O(kN)$，$k$为迭代次数 |
| 内存需求 | $O(N^2)$（填充后） | $O(N)$ |
| 确定性 | 计算时间确定，适合实时仿真 | 计算时间不确定 |
| 多右端项 | 分解一次可求解多组右端项 | 需重新迭代 |
| 并行性 | 有限 | 高，适合GPU/CPU多核 |

**选择指南**：

| 系统规模 | 推荐方法 | 理由 |
|---------|---------|------|
| < 1,000节点 | KLU直接法 | 简单、确定、高效 |
| 1,000-10,000节点 | KLU/GMRES混合 | 稀疏技术+预处理 |
| > 10,000节点 | GMRES/ILU | 内存效率、可扩展性 |
| 实时仿真 | KLU+恒导纳ADC | 确定性计算时间 |

## 关键技术挑战

### 挑战1：拓扑频繁变更导致的重分解

电力电子系统（如MMC换流器）中开关状态频繁变化，每次变化都可能改变导纳矩阵结构，触发LU重分解。解决路径：
- 恒定导纳ADC：约束 $L_{sw}C_{sw}=(\Delta t)^2$，开关不触发重分解
- 预计算查表（GENE）：枚举状态组合，$O(1)$ 查找
- 补偿法：开关变化作为电流源补偿，避免修改矩阵结构

### 挑战2：填充元膨胀

高斯消去过程中产生的填充元（Fill-in）会严重影响计算效率和内存。解决路径：
- AMD排序：使填充元最小化（Abusalah等，2020报告减少50-90%）
- BTF块三角分解：将系统分解为条件独立的子块，并行求解
- 混合存储格式：根据矩阵结构动态选择CSC/CSR

### 挑战3：非线性收敛性

强非线性系统（如饱和变压器、避雷器）的牛顿迭代可能不收敛。解决路径：
- 阻尼牛顿法：引入阻尼因子 $\alpha \in (0,1]$，$x^{(k+1)} = x^{(k)} - \alpha J^{-1}F$
- 分段线性化：用有限段折线逼近非线性特性，避免迭代
- 简化牛顿法：固定雅可比矩阵，减少每步LU分解开销

### 挑战4：大规模系统的条件数

大规模系统的导纳矩阵条件数随系统规模急剧增大，导致迭代法收敛变慢甚至发散。解决路径：
- ILU预处理器：通过不完全LU分解改善条件数
- 块雅可比预处理的GMRES：每个子块独立预处理
- 代数多重网格（Algebraic Multigrid）：层级粗糙化加速收敛

### 挑战5：实时仿真的确定性约束

实时仿真要求计算时间严格小于时间步长（$\Delta t$），不允许迭代或自适应策略。解决路径：
- 恒定导纳矩阵：拓扑变化不触发重分解
- 预计算查表：GENE方法，查表时间 $<1\,\mu\text{s}$
- 硬件事先规划：KLU+AMD的固定计算图，FPGA流水化

## 量化性能边界

### 求解器性能

| 数据来源 | 方法 | 系统规模 | 性能指标 |
|---------|------|---------|---------|
| Abusalah等2020 | KLU并行化 | 多种规模 | 相比标准LU加速10-1000×（稀疏矩阵） |
| Abusalah等2020 | AMD排序 | 100节点 | 填充元减少50-90% |
| Gnanarathna等2006 | GENE预计算 | 子模块有限 | 开关处理时间 $<1\,\mu\text{s}$ |
| — | KLU直接求解 | 100节点 | ~10 μs/步 |
| — | KLU+并行 | 1,000节点 | ~50 μs/步 |
| — | GMRES+ILU | 10,000节点 | ~200 μs/步（需并行）|

### 开关处理技术量化

| 技术 | 重分解触发 | 计算开销 | 适用场景 |
|------|-----------|---------|---------|
| 变导纳 | 每次开关 | 高 | 开关不频繁 |
| CDA | 事件点插入BE | 中 | 精确性要求高 |
| 恒导纳ADC | 不触发 | 低 | 电力电子变流器 |
| GENE预计算 | 不触发 | 极低 | 子模块数有限（$<20$）|
| 补偿法 | 不触发 | 低 | 快速近似 |

### 非线性求解参数

| 应用场景 | 最大迭代 | 绝对容差 | 雅可比更新策略 |
|----------|---------|---------|----------------|
| 饱和变压器 | 5-10 | $10^{-6}$ | 每步更新 |
| 避雷器（ZnO）| 3-5 | $10^{-4}$ | 固定/简化 |
| 开关分段 | 1-2 | $10^{-3}$ | 线性化 |
| 混合仿真接口 | 3-10 | $10^{-3}$ | 预测-校正 |

## 适用边界与选择指南

| 场景 | 推荐方法 | 不推荐 |
|------|---------|--------|
| 开关不频繁（ $<1$ 次/步）| 变导纳+CDA | 预计算（状态爆炸）|
| 开关频繁（如MMC PWM）| 恒导纳ADC+GENE | 变导纳（重分解爆炸）|
| 弱非线性系统 | 简化牛顿法 | 完全牛顿（开销浪费）|
| 强非线性系统（饱和磁路）| 分段线性化或阻尼牛顿 | 固定雅可比（可能不收敛）|
| 小规模实时（$<1000$节点）| KLU+恒导纳 | GMRES（不确定性）|
| 大规模离线（$>>10000$节点）| GMRES+ILU+并行 | KLU（填充元爆炸）|
| 硬实时（$\Delta t\leq 50\,\mu$s）| KLU预计算+ADC | 迭代法（时间不确定）|

## 技术演进脉络

### 1960s-1970s：奠基时期
- **Dommel节点法**（1969）：提出伴随电路离散化，节点导纳矩阵求解框架
- **稀疏矩阵概念引入**（1970s）：利用电力系统稀疏性，减少计算量和存储需求

### 1980s-1990s：稀疏技术成熟
- **最小度算法（MD/AMD）**（1980s）：填充元最小化，符号分解优化
- **BTF预处理**（1990s）：块三角形式分解，并行求解基础

### 2000s-2010s：开关处理突破
- **GENE方法**（Gnanarathna等，2006）：预计算开关状态，避免在线LU分解
- **恒定导纳ADC**（2000s）：开关不触发重分解，实时仿真实现
- **KLU求解器**（Abusalah等，2020）：AMD排序+BTF预处理，并行稀疏矩阵加速

### 2010s-2026年：大规模与并行
- **KLU求解器**（Abusalah等，2020）：针对电路仿真优化，CPU多核并行
- **分网并行**（2010s）：大规模系统分解，多核/GPU加速
- **混合求解**（2020s）：直接法+迭代法，自适应策略

## 相关方法
- [[methods/network-solution/nodal-analysis.md]] - EMT标准求解框架
- [[methods/network-solution/sparse-matrix-solver.md]] - KLU等高性能求解器
- [[methods/network-solution/iterative-solvers.md]] - GMRES/Krylov子空间方法
- [[methods/numerical-methods/fixed-admittance.md]] - ADC恒定导纳技术
- [[methods/numerical-methods/numerical-integration.md]] - 梯形法/BE离散化
- [[methods/power-electronics/switch-modeling.md]] - 开关处理技术

## 相关模型
- [[models/transmission-line/transmission-line-model.md]] - 行波等值与节点接入
- [[models/transformer/transformer-model.md]] - 饱和特性与迭代求解
- [[models/converter/mmc-model.md]] - 大规模换流器矩阵优化
- [[models/converter/vsc-model.md]] - 电力电子节点建模
- [[models/rotating-machine/synchronous-machine-model.md]] - 电机等效电路

## 相关主题
- [[topics/simulation/parallel-computing.md]] - 大规模系统并行求解
- [[topics/simulation/real-time-simulation.md]] - 实时约束下的求解优化
- [[topics/simulation/co-simulation.md]] - 多子系统协调求解
- [[topics/modeling-methods/network-equivalent.md]] - 矩阵降阶技术
- [[topics/simulation/emt-mathematical-foundation.md]] - 求解数学原理

## 来源论文

| 论文 | 年份 | 关联要点 |
|------|------|---------|
| Abusalah等 - Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients | 2020 | KLU并行化、AMD排序+BTF预处理、稀疏矩阵加速10-1000× |
| Rashidirad等 - Unified MANA-based load-flow for multi-frequency hybrid AC/DC multi-microgrids | 2023 | 统一MANA框架、多频混合系统、多相微电网 |
| Gnanarathna等 - Nested Fast and Simultaneous Solution | 2006 | GENE方法、预计算开关状态、稀疏矩阵加速 |
| Mahseredjian等 - A combined state-space nodal method for the simulation of power system transient | — | 状态空间节点法、EMT求解框架 |