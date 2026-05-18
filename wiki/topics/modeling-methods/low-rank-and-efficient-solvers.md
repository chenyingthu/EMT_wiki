---
title: "低秩近似与高效求解器 (Low-Rank Approximation and Efficient Solvers)"
type: topic
tags: [low-rank, sparse-solver, klu, efficient-computation, emt]
created: "2026-05-01"
book-chapter: "13"
---

# 低秩近似与高效求解器 (Low-Rank Approximation and Efficient Solvers)

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="450" y="28" font-family="Times New Roman" font-size="18" font-weight="bold" text-anchor="middle" fill="#1a1a1a">低秩近似与高效求解器 · EMT网络方程求解体系</text>
  <line x1="120" y1="38" x2="780" y2="38" stroke="#555" stroke-width="0.8"/>

  <!-- Layer 1: 输入 -->
  <rect x="310" y="55" width="280" height="55" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="450" y="72" font-family="Times New Roman" font-size="13" font-weight="bold" text-anchor="middle" fill="#1e3a8a">网络方程输入</text>
  <text x="450" y="90" font-family="Times New Roman" font-size="11" text-anchor="middle" fill="#1e3a8a">导纳矩阵 G(v) · 注入电流 i(t) · 历史电流 i_his</text>

  <!-- Arrow 1-2 -->
  <line x1="450" y1="110" x2="450" y2="135" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#333"/></marker></defs>

  <!-- Layer 2: 求解框架 -->
  <rect x="60" y="145" width="780" height="75" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="450" y="162" font-family="Times New Roman" font-size="13" font-weight="bold" text-anchor="middle" fill="#92400e">核心求解框架</text>
  <text x="100" y="180" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">稀疏LU</text>
  <text x="100" y="195" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">O(N^(1.2~1.5))</text>
  <text x="310" y="180" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">KLU/BTF</text>
  <text x="310" y="195" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">O(N) 电力优化</text>
  <text x="530" y="180" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">低秩近似</text>
  <text x="530" y="195" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">O(N log N)</text>
  <text x="740" y="180" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">分层H矩阵</text>
  <text x="740" y="195" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#78350f">O(N log²N)</text>
  <line x1="205" y1="160" x2="205" y2="210" stroke="#d97706" stroke-width="0.5" stroke-dasharray="3,2"/>
  <line x1="420" y1="160" x2="420" y2="210" stroke="#d97706" stroke-width="0.5" stroke-dasharray="3,2"/>
  <line x1="630" y1="160" x2="630" y2="210" stroke="#d97706" stroke-width="0.5" stroke-dasharray="3,2"/>

  <!-- Arrow 2-3 -->
  <line x1="450" y1="220" x2="450" y2="245" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 3: 优化技术 -->
  <rect x="60" y="255" width="780" height="90" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="450" y="272" font-family="Times New Roman" font-size="13" font-weight="bold" text-anchor="middle" fill="#166534">优化技术</text>
  <rect x="80" y="285" width="160" height="48" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="160" y="301" font-family="Times New Roman" font-size="10" font-weight="bold" text-anchor="middle" fill="#166534">AMD/ND排序</text>
  <text x="160" y="315" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">最小度/嵌套剖分</text>
  <text x="160" y="327" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">填充元↓50-90%</text>
  <rect x="260" y="285" width="160" height="48" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="340" y="301" font-family="Times New Roman" font-size="10" font-weight="bold" text-anchor="middle" fill="#166534">BTF预处理</text>
  <text x="340" y="315" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">块三角分解</text>
  <text x="340" y="327" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">天然并行+故障隔离</text>
  <rect x="440" y="285" width="160" height="48" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="520" y="301" font-family="Times New Roman" font-size="10" font-weight="bold" text-anchor="middle" fill="#166534">部分重分解</text>
  <text x="520" y="315" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">Sherman-Morrison</text>
  <text x="520" y="327" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">80%开关时间↓</text>
  <rect x="620" y="285" width="160" height="48" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="700" y="301" font-family="Times New Roman" font-size="10" font-weight="bold" text-anchor="middle" fill="#166534">超节点/向量</text>
  <text x="700" y="315" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">SIMD向量化</text>
  <text x="700" y="327" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#166534">缓存友好访问</text>

  <!-- Arrow 3-4 -->
  <line x1="450" y1="345" x2="450" y2="370" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 4: 应用场景 -->
  <rect x="60" y="380" width="780" height="58" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="450" y="397" font-family="Times New Roman" font-size="13" font-weight="bold" text-anchor="middle" fill="#4c1d95">应用场景</text>
  <text x="130" y="418" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#5b21b6">RTDS/HYPERSIM</text>
  <text x="130" y="432" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#5b21b6">实时HIL</text>
  <text x="320" y="418" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#5b21b6">PSCAD/EMTDC</text>
  <text x="320" y="432" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#5b21b6">离线仿真</text>
  <text x="510" y="418" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#5b21b6">GPU加速(KLU/cuSOLVER)</text>
  <text x="510" y="432" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#5b21b6">万级节点&lt;50μs</text>
  <text x="700" y="418" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#5b21b6">FPGA实现</text>
  <text x="700" y="432" font-family="Times New Roman" font-size="9" text-anchor="middle" fill="#5b21b6">微秒级542节点</text>

  <!-- Arrow 4-5 -->
  <line x1="450" y1="438" x2="450" y2="463" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 5: 量化性能 -->
  <rect x="150" y="473" width="600" height="42" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="450" y="490" font-family="Times New Roman" font-size="13" font-weight="bold" text-anchor="middle" fill="#991b1b">量化性能边界</text>
  <text x="240" y="507" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#991b1b">KLU vs 稠密LU: 5-10%分解</text>
  <text x="450" y="507" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#991b1b">分层低秩: 2.8×加速(Zhang 2021)</text>
  <text x="660" y="507" font-family="Times New Roman" font-size="10" text-anchor="middle" fill="#991b1b">实时: &lt;50μs/步长</text>

  <!-- Legend -->
  <rect x="16" y="60" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="34" y="71" font-family="Times New Roman" font-size="10" fill="#1e3a8a">输入层</text>
  <rect x="16" y="80" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="34" y="91" font-family="Times New Roman" font-size="10" fill="#92400e">求解框架</text>
  <rect x="16" y="100" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="34" y="111" font-family="Times New Roman" font-size="10" fill="#166534">优化技术</text>
  <rect x="16" y="120" width="14" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="34" y="131" font-family="Times New Roman" font-size="10" fill="#5b21b6">应用场景</text>
  <rect x="16" y="140" width="14" height="14" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="34" y="151" font-family="Times New Roman" font-size="10" fill="#991b1b">量化性能</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 低秩近似与高效求解器体系架构（五层结构）</p>

## 概述

低秩近似（Low-Rank Approximation）与高效求解器是EMT仿真中解决大规模网络方程计算瓶颈的核心技术。EMT时间步进中，80%–97%的计算时间消耗在网络方程求解（导纳矩阵与电流向量的线性代数运算）上（Zhang等2021）。大规模电网（>10,000节点）若采用传统稠密LU分解，计算复杂度达$O(N^3)$，单步求解时间动辄数秒，无法满足实时仿真要求的微秒级响应。通过利用矩阵的低秩结构、稀疏性和特殊块结构，求解复杂度可降至$O(N)$甚至$O(N \log N)$，使万级节点系统的实时仿真成为可能。

核心技术路线：
- **稀疏LU分解优化**：通过AMD排序、BTF预处理、超节点技术将复杂度降至$O(N^{1.0\sim1.5})$
- **低秩更新**：利用Sherman-Morrison-Woodbury公式避免整体重分解
- **分层低秩（H矩阵）**：利用远距离母线组间相互作用的低秩近似性质
- **快速多极子方法（FMM）**：将$O(N^2)$矩阵向量乘法降至$O(N)$

## 核心挑战

| 挑战类型 | 具体描述 | 影响 |
|---------|---------|------|
| **计算复杂度瓶颈** | 传统稠密LU分解$O(N^3)$无法应对大规模系统 | 10,000+节点系统单步求解可达数秒 |
| **开关频繁重分解** | 拓扑变化导致导纳矩阵数值和结构变化 | 每次开关动作触发完整LU重分解，计算浪费 |
| **实时仿真约束** | 实时HIL要求单步计算时间<步长（50μs@50μs步长） | 制约控制器闭环测试的保真度 |
| **数值稳定性** | 极端导纳比（Ropen/Rclose）建模引起条件数病态 | 欠佳的主元选择导致求解发散 |
| **填充元膨胀** | LU分解将原零元素变为非零（fill-in） | 存储需求可膨胀10–100倍 |

## EMT建模方法

### 13.1 稀疏矩阵技术基础

**稀疏性原理** — 电力系统导纳矩阵具有天然稀疏性：

- 500节点系统：非零元素占比约0.5%–1.0%
- 10,000节点系统：非零元素占比约0.05%–0.1%
- 稀疏模式：对称或近似对称

**稀疏存储格式对比**：

| 格式 | 存储方式 | 适用场景 | 存储效率 |
|------|----------|---------|---------|
| COO | (行,列,值)三元组 | 构建阶段 | 低 |
| CSR | 行指针+列索引+值 | 行访问频繁场景 | 中 |
| CSC | 列指针+行索引+值 | 列访问频繁场景 | 中 |
| 对角存储 | 主对角+副对角 | 带状矩阵 | 高 |

**填充元（Fill-in）控制**：

LU分解产生填充元——原本为零的元素位置变为非零。填充元控制策略：

最小度算法（AMD — Approximate Minimum Degree）：
$$\min_i \{ \deg_i^{(k)} \}$$

每次选择度数最小的节点消去，目标是最小化填充元数量。效果：可将填充元减少50%–90%（AMD排序，2010年基准数据）。

嵌套剖分（Nested Dissection, ND）：
- 基于图划分思想，将矩阵对应图递归地划分为若干不相连子图
- 适合高度结构化的大规模矩阵（如规则电网）
- 对输电网格效果显著

### 13.2 稀疏LU分解优化

**符号分解与数值分解分离** — 稀疏LU分解分为两个独立阶段：

符号分解（仅在拓扑变化时执行一次）：
1. 确定L/U的非零结构（通过消去树）
2. 预分配存储空间
3. 构建消去树（elimination tree）

数值分解（每次拓扑或数值变化时执行）：
1. 基于符号分解预分配的结构
2. 计算L/U的具体数值
3. 利用消去树并行化数值计算

**部分重分解（Partial Refactorization）** — 当网络拓扑仅发生少量开关变化时：

$$Y_{\text{new}} = Y_{\text{old}} + \Delta Y$$

利用Sherman-Morrison-Woodbury公式避免整体重分解：
$$(Y + UCV)^{-1} = Y^{-1} - Y^{-1}U(C^{-1} + VY^{-1}U)^{-1}VY^{-1}$$

其中$U$和$V$为低秩修正矩阵（开关状态变化对应位置），$C$为对角修正矩阵。适用于少量开关变化（<5%节点变化）的场景——原文报告开关处理时间减少80%（部分重分解，2015年）。

**BTF预处理（Block Triangular Form）** — 对网络拓扑做块三角分解：

$$P Y P^T = \begin{bmatrix} Y_{11} & Y_{12} & \cdots \\ 0 & Y_{22} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix}$$

优势：
- 各对角块可独立求解（天然并行性）
- 故障隔离（某块内变化不影响其他块）
- 大规模系统求解速度提升40%（BTF预处理，2018年）

**主元有效性测试（Pivot Validity Testing）** — Abusalah等（2020）提出在KLU中嵌入主元有效性测试：检测当前分解列中是否存在数值过小的主元，若存在则触发选择性重分解而非全量重分解，显著减少不必要的数值重分解次数。

### 13.3 低秩近似方法

**低秩更新（Low-Rank Update）** — 网络变化可表示为低秩修正：

$$Y_{\text{new}} = Y_{\text{old}} + uv^T$$

其中$u$和$v$为$N \times 1$向量（单条支路变化时）。利用矩阵求逆引理：
$$Y_{\text{new}}^{-1} = Y_{\text{old}}^{-1} - \frac{Y_{\text{old}}^{-1}uv^TY_{\text{old}}^{-1}}{1 + v^TY_{\text{old}}^{-1}u}$$

计算复杂度：$O(N^2)$（低秩更新）vs $O(N^3)$（重分解）。当网络仅有单条或少数几条支路变化时，低秩更新远快于重分解。

**快速多极子方法（FMM — Fast Multipole Method）** — 适用于N体问题类计算：

- 远场相互作用用低秩近似（$O(N)$精度可控）
- 近场精确计算
- 矩阵向量乘法复杂度：$O(N)$ vs $O(N^2)$（稠密矩阵）

在EMT中的典型应用：
- 输电线路互阻抗计算
- 大地返回阻抗建模
- 变电站接地网分析

**分层低秩（Hierarchical Low-Rank, H矩阵）** — Zhang等（2021）提出的核心方法。利用"远距离母线组之间的相互作用子矩阵通常稀疏且可低秩近似"这一关键观察：

H矩阵结构：
$$H = \begin{bmatrix} H_{11} & H_{12} \\ H_{21} & H_{22} \end{bmatrix}$$

其中非对角块通过低秩近似：
$$H_{12} \approx UV^T, \quad U \in \mathbb{R}^{n \times k}, \quad V \in \mathbb{R}^{m \times k}, \quad k \ll \min(n,m)$$

存储复杂度：$O(N \log N)$
求解复杂度：$O(N \log^2 N)$
在179节点系统测试中，相比KLU稀疏LU求解器加速达2.8倍，精度损失<0.1%。

### 13.4 KLU求解器与实时优化

KLU（Tim Davis开发）是专门为电力系统优化的直接稀疏求解器，集成于HYPERSIM、RTDS、PSCAD/EMTDC等主流平台：

**KLU核心特点**：

| 优化特性 | 具体实现 | 效果 |
|---------|---------|------|
| AMD排序 | 近似最小度节点编号 | 填充元减少70%–90% |
| BTF预处理 | 块三角分解 + 独立求解 | 40%求解速度提升 |
| 部分重分解 | Sherman-Morrison低秩修正 | 开关处理时间↓80% |
| 主元有效性测试 | 检测病态主元触发选择重分解 | 数值稳定性提升 |
| 实时性优化 | 超节点合并 + SIMD向量化 | 微秒级求解 |

**性能对比（典型500节点系统）**：

| 求解器 | 分解时间 | 求解时间 | 备注 |
|-------|---------|---------|------|
| 稠密LU | 100%（基准） | 100%（基准） | N³复杂度 |
| 稀疏LU | 10%–20% | 5%–10% | 通用优化 |
| KLU | 5%–10% | 3%–5% | 电力系统定制 |

**MKLU（改进KLU）** — Bruned等（2023）将MKLU集成到工业实时仿真平台HYPERSIM：
- 在542节点系统上实现实时HIL仿真（50μs步长）
- 通过任务打包（基于浮点运算量NFPO）实现多核并行
- 在1,000节点实际电网HIL测试中，MKLU比GenCode快2.1倍且数值更稳定

### 13.5 分裂状态空间与ADI方法

**分裂式积分（Splitting Integration）** — 将状态空间方程分裂：

$$\dot{x} = f(x) + g(x)$$

其中：
- $f(x)$：线性部分 → 可预先分解，实时调用高效
- $g(x)$：非线性部分 → Newton迭代处理

**ADI交替方向隐式法** — 交替方向隐式法将二维/三维问题降维：

$$\begin{cases} (I - \frac{h}{2}A_1)u^{n+1/2} = (I + \frac{h}{2}A_2)u^n \\ (I - \frac{h}{2}A_2)u^{n+1} = (I + \frac{h}{2}A_1)u^{n+1/2} \end{cases}$$

其中$A = A_1 + A_2$，$h$为步长。优势：
- 一维问题求解替代二维/三维问题
- 三对角矩阵可用Thomas算法$O(N)$求解
- 数值稳定性优于显式方法

## 形式化表达

### 核心方程汇总

**EMT网络方程（节点分析）**：
$$G \mathbf{v}(t) = \mathbf{i}_{\text{in}}(t) + \mathbf{i}_{\text{his}}(t - \Delta t)$$

其中$G$为导纳矩阵，$\mathbf{v}$为节点电压向量，$\mathbf{i}_{\text{in}}$为注入电流，$\mathbf{i}_{\text{his}}$为历史电流。

**Sherman-Morrison-Woodbury低秩更新**：
$$(Y + UV^T)^{-1} = Y^{-1} - Y^{-1}U(V^TY^{-1}U)^{-1}VY^{-1}$$
当$U$和$V$为低秩（$k \ll N$）时，$(V^TY^{-1}U)^{-1}$是$k \times k$矩阵求逆而非$N \times N$。

**分层H矩阵近似**：
$$G^{-1}\mathbf{b} \approx \sum_{l=1}^{L} U_l (V_l^T \mathbf{b}) + O(\varepsilon)$$

其中$L$为分层深度，$U_l, V_l$为各层低秩因子，存储复杂度$O(N \log N)$。

**BTF块三角分解**：
$$\hat{G} = P^T \begin{bmatrix} G_{11} & G_{12} & \\ 0 & G_{22} & \\ & & \ddots \end{bmatrix} P$$

各对角块独立求解，并行度等于对角块数量。

**ADI交替方向隐式**：
$$u^{n+1} = (I - \frac{h}{2}A_2)^{-1}(I + \frac{h}{2}A_1)(I - \frac{h}{2}A_1)^{-1}(I + \frac{h}{2}A_2)u^n$$

等价于两步交替求解两个三对角系统。

### 复杂度对比汇总

| 方法 | 分解复杂度 | 求解复杂度 | 存储复杂度 | 适用规模 |
|------|-----------|-----------|-----------|---------|
| 稠密LU | $O(N^3)$ | $O(N^2)$ | $O(N^2)$ | $N < 100$ |
| 稀疏LU | $O(N^{1.2\sim1.5})$ | $O(N)$ | $O(N)$ | $N < 10,000$ |
| KLU | $O(N^{1.0\sim1.2})$ | $O(N)$ | $O(N)$ | $N < 100,000$ |
| 低秩更新 | $O(N^2)$（修正） | $O(N)$ | $O(N)$ | 少量变化 |
| 分层低秩 | $O(N \log N)$ | $O(N \log^2 N)$ | $O(N \log N)$ | $N < 1,000,000$ |
| FMM | $O(N)$ | $O(N)$ | $O(N)$ | N体问题 |

## 关键技术挑战

**挑战1：填充元控制与排序质量** — AMD排序虽有70%–90%的填充元减少效果，但最小度计算本身$O(N^2)$；ND排序对非结构化拓扑效果下降。动态运行时排序优化仍不成熟。

**挑战2：变拓扑下的重分解策略** — 极端导纳比（如开断开关Ropen=10⁶Ω，Rclose=10⁻⁶Ω）导致条件数病态，主元选择不当会引发数值不稳定。部分重分解的触发阈值需根据系统特性自适应调整。

**挑战3：并行求解的负载均衡** — BTF分解天然产生不均衡块规模——最大块决定整体求解时间（Amdahl定律）。基于NFPO（浮点运算量）的任务打包在理论上最优，但实际电网拓扑异质性导致核间负载偏差可达30%。

**挑战4：实时约束下的精度-速度权衡** — 实时HIL要求50μs内完成一步求解（@50μs步长），其中LU分解占比40%–60%（目标<20μs）。GPU加速（cuSOLVER）可将10,000节点求解压缩至<50μs，但需批量矩阵批次（≥32步）才能充分并行——单步实时性仍受限。

**挑战5：低秩近似的精度控制** — H矩阵低秩近似精度由秩$k$控制：$k$越大精度越高但计算量越大；$k$太小近似误差累积。目前缺乏统一的误差界估计方法，实际工程需通过对比基准解验证。

## 量化性能边界

| 性能指标 | 数值 | 来源 |
|---------|------|------|
| KLU vs 稠密LU分解时间 | 5%–10% vs 100% | Davis KLU, 2004 |
| AMD排序填充元减少 | 70%–90% | AMD理论, 2010 |
| BTF预处理求解加速 | 40% | BTF预处理研究, 2018 |
| 部分重分解开关时间↓ | 80% | 部分重分解研究, 2015 |
| 分层低秩 vs KLU加速 | 2.8× | Zhang等2021, 179节点 |
| 低秩更新 vs 重分解加速 | 3–5× | 低秩更新技术, 2020 |
| 分层低秩存储需求↓ | 60% | 分层低秩研究, 2023 |
| FPGA 542节点实时仿真 | 单步<1μs | FPGA研究, 2016 |
| GPU 10,000节点求解 | <50μs/步 | GPU加速研究, 2021 |
| MKLU vs GenCode实时加速 | 2.1× | Bruned等2023, HYPERSIM |

**单步计算时间分配（实时仿真典型配置）**：

| 阶段 | 占比 | 目标时间 |
|-----|------|---------|
| 历史项更新 | 10%–20% | <5μs |
| 矩阵组装 | 5%–15% | <3μs |
| LU分解 | 40%–60% | <20μs |
| 前代回代 | 20%–40% | <15μs |
| 开关处理 | 5%–20% | <5μs |

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 关键原因 |
|---------|---------|---------|
| 离线仿真（精度优先） | KLU/UMFPACK | 成熟稳定，无需实时约束 |
| 实时HIL仿真 | KLU定制版 + BTF | 速度优先，部分重分解减少重分解开销 |
| 少量开关变化的动态仿真 | Sherman-Morrison低秩更新 | 避免全量重分解，$O(N^2)$修正 |
| 超大规模系统（>100k节点） | 分层低秩（H矩阵） | $O(N \log N)$存储，$O(N \log^2 N)$求解 |
| 输电线路互阻抗计算 | FMM | 利用远场低秩结构 |
| 高度结构化大矩阵 | BTF + ND排序 | 天然块结构，并行度最高 |
| 非结构化拓扑 | AMD排序 + KLU | 无需先验拓扑知识 |
| GPU异构加速 | cuSOLVER + KLU批量 | 批处理32+步并行 |

**不适用场景**：
- 稀疏度<90%的矩阵（填充元过多，稀疏存储优势丧失）
- 少量节点变化但涉及关键路径的大规模拓扑修改（低秩更新优势不复存在）
- 病态系统（条件数>10⁸）——需预处理或迭代求解器

## 相关方法

- [[methods/network-solution/sparse-matrix-solver]] — 稀疏LU技术基础（AMD排序、KLU、BTF）
- [[methods/system-studies/model-order-reduction]] — 低秩近似理论（矩阵降阶方法）
- [[methods/numerical-methods/fixed-admittance]] — 恒导纳模型（避免拓扑变化导致的重复分解）
- [[topics/simulation/parallel-computing]] — 并行求解加速（多核CPU/GPU协同）
- [[methods/numerical-methods/numerical-integration]] — 分裂式积分（ADI方法与状态空间分裂）

## 相关模型

- [[topics/modeling-methods/network-equation-solution]] — 网络方程求解（求解器应用场景）
- [[models/equivalent/fdne-model]] — 频率相关网络等值（降阶后求解）
- [[models/converter/mmc-model]] — 模块化多电平换流器（大规模系统高效求解需求）

## 相关主题

- [[topics/simulation/parallel-computing]] — 求解器并行化（多核/GPU计算）
- [[topics/simulation/real-time-simulation]] — 实时仿真约束（微秒级求解要求）
- [[methods/system-studies/model-order-reduction]] — 低秩结构应用（系统降阶）

## 来源论文

- **Zhang等2021** — 分层低秩近似网络求解器，O(N log N)复杂度，2.8×加速（IEEE TPWRD）
- **Abusalah等2020** — KLU并行化与BTF预处理，EMT自动并行化（IEEE OAJPE）
- **Bruned等2023** — MKLU集成HYPERSIM实时仿真，2.1×加速（Electric Power Systems Research）