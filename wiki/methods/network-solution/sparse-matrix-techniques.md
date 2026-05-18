---
title: "稀疏矩阵技术 (Sparse Matrix Techniques)"
type: method
tags: [sparse-matrix, numerical-methods, computational-efficiency, power-system, KLU, LU-decomposition]
created: "2026-05-02"
updated: "2026-05-19"
---

# 稀疏矩阵技术 (Sparse Matrix Techniques)

## 定义与边界

稀疏矩阵技术是利用电力网络矩阵中大量零元素的结构特征来降低存储、组装、分解和求解成本的一组数值方法。它包括稀疏存储格式、重排序、符号分解、数值分解、迭代求解、预处理和稀疏数据结构维护。

本页讨论矩阵层方法，不把"稀疏"直接等同于"快速"或"实时"。实际收益取决于非零元数量、填充元、条件数、开关事件、缓存局部性和并行调度。网络方程背景见 [[nodal-admittance-matrix]]，伴随模型来源见 [[companion-model]]。

## EMT 中的角色

固定步长 EMT 常在每个步长求解：

$$\mathbf{Y}_k \mathbf{v}_k = \mathbf{i}_k$$

其中 $\mathbf{Y}_k$ 由网络拓扑、伴随导纳、开关状态和等效源共同决定。多数电网拓扑只连接局部节点，因此 $\mathbf{Y}_k$ 的非零元素数量 $nnz$ 通常远小于 $n^2$。稀疏矩阵技术的主要作用是：

- 避免存储完整 $n \times n$ 矩阵。
- 在结构稳定时复用符号分析、重排序和分解结构。
- 降低每步前代/回代或迭代求解成本。
- 为 [[gpu-parallel-acceleration]] 和 [[heterogeneous-computing]] 提供可并行数据结构。

## 存储格式

常见格式包括：

| 格式 | 适用环节 | 主要风险 |
|------|----------|----------|
| CSR | 按行访问、SpMV、迭代法 | 插入新非零元成本高 |
| CSC | 稀疏直接法、列消去 | 行访问不便 |
| COO | 矩阵组装、并行累加中间态 | 求解前通常需排序和压缩 |
| Block CSR | 三相或多端口块结构 | 块大小不均会浪费存储 |

对 EMT 而言，矩阵组装阶段和求解阶段可能需要不同格式。COO 适合并行收集元件贡献，CSR/CSC 适合后续求解；格式转换本身也应计入性能评估。

## 符号分解与数值分解

稀疏直接法通常分为四个步骤：

1. **重排序**：寻找置换矩阵 $\mathbf{P}$，使 $\mathbf{PYP}^T$ 的填充元较少（AMD 排序可减少 50–80% 填充元，Abusalah 2020）。
2. **符号分解**：确定 $L$ 和 $U$ 的非零结构，只执行一次。
3. **数值分解**：计算具体数值 $L$ 和 $U$，步长/拓扑未变时可复用。
4. **前代/回代**：求解 $\mathbf{Ly} = \mathbf{b}$、$\mathbf{Ux} = \mathbf{y}$，复杂度 $O(nnz)$。

若开关状态不改变矩阵结构，符号分解可在多个步长复用；若拓扑频繁改变，则必须重新检查结构、排序或分解，收益会下降。

## KLU 求解器与 EMT 并行增强

KLU 是 EMT 类程序中最流行的稀疏直接求解器（Ng & Matinpaniha 2012，IEEE Trans on Power Systems）。KLU 采用**两层分解流程**：

**符号分析阶段**（初始化时只执行一次）：

$$\mathbf{A} \xrightarrow{\text{AMD 重排序}} \mathbf{P}_r \mathbf{A} \mathbf{P}_c \xrightarrow{\text{BTF 分解}} \mathbf{A}_{\text{BTF}}$$

其中 BTF（Block Triangular Form）将矩阵自动分解为块对角形式：

$$\mathbf{A}_{\text{BTF}} = \begin{bmatrix} \mathbf{A}_{11} & & \\ \mathbf{A}_{21} & \mathbf{A}_{22} & \\ & \ddots & \ddots \\ & & \mathbf{A}_{k,k-1} & \mathbf{A}_{kk} \end{bmatrix}$$

各对角块 $\mathbf{A}_{ii}$ 相互独立，可在不同线程并行求解。分布参数线路/电缆模型的自然解耦特性使 BTF 可自动识别子网络边界，无需人工干预。

**数值分解阶段**（每步/每次重分解）：对每个 BTF 块 $i$：
1. 执行 Gilbert-Peierls 算法定位 $L_i$ 和 $U_i$ 的非零元。
2. 执行左向数值分解（含部分主元）计算 $L_i$ 和 $U_i$。
3. **主元有效性测试**：给定容差 $\varepsilon_p$，检验

$$\frac{|a_{\text{new}}^{\text{pivot}}|}{|a_{\text{old}}^{\text{pivot}}|} > \varepsilon_p$$

是否成立；若成立则接受当前 LU 结构，否则触发**部分重分解**。

**部分重分解**（Abusalah 2020）仅对受拓扑/非线性变化影响的 BTF 块重新执行数值分解，而非全矩阵重分解。通过识别"动态列"（时变/非线性元件对应列），保留静态列的 $L$、$U$ 因子：

$$\mathbf{A}_{\text{dynamic}} = \begin{bmatrix} \mathbf{L}_{11} & \\ \mathbf{L}_{21} & \mathbf{L}_{22} \end{bmatrix} \begin{bmatrix} \mathbf{U}_{11} & \mathbf{U}_{12} \\ & \mathbf{U}_{22}^{\text{new}} \end{bmatrix}$$

其中 $\mathbf{U}_{22}^{\text{new}}$ 仅从第 $k$ 列（首个动态列）开始重新分解。

KLU 的适用规模：**1000–100000 节点**。1000 节点以下可用稠密矩阵求解器；100000 节点以上需考虑多级分区策略。

## 排序与填充控制

填充元是稀疏直接法的核心成本来源。常用排序算法：

| 算法 | 类型 | 特点 |
|------|------|------|
| AMD（近似最小度） | 局部分解 | 效果好，O(n²) 开销，适合一般网络 |
| COLAMD | 列排序 | 适合列操作居主的 CSC 格式 |
| 嵌套剖分（Nested Dissection） | 全局几何 | 需图分割工具（METIS/Scotch），最优但开销大 |
| Tinney 类排序 | 电力系统传统 | 基于网络拓扑的启发式方法 |

填充控制指标——**填充因子**：

$$\rho_{\text{fill}} = \frac{nnz(\mathbf{L}) + nnz(\mathbf{U})}{nnz(\mathbf{Y})}$$

AMD 排序通常使 $\rho_{\text{fill}} \in [1.5, 5]$（视网络拓扑而异），而无排序可达 10–50。

## 直接法与迭代法对比

### 直接法

稀疏 LU/Cholesky 适合需要稳定、可重复求解的中小到大规模网络。失败模式：主元过小导致数值不稳定、填充元失控使稀疏变稠密、内存不足、开关导致结构频繁改变。

### 迭代法

CG、BiCGSTAB、GMRES 等迭代法以 SpMV（稀疏矩阵-向量乘）为核心：

$$O(nnz) = O(n \cdot \bar{d}), \quad \bar{d} = \text{平均每行非零元数}$$

收敛速度取决于矩阵条件数 $\kappa(\mathbf{A})$。对于非对称、不定或病态矩阵（如电力电子接口），收敛性不能默认保证。

### 预处理

Jacobi、ILU（不完全 LU）、块 Jacobi、AMG（代数多重网格）等预处理可降低迭代次数：

$$\mathbf{A} \approx \mathbf{M} = \mathbf{L}\mathbf{U}, \quad \mathbf{M}^{-1}\mathbf{A} \approx \mathbf{I}$$

预处理的代价是额外构造开销 + 并行化难度，须在迭代节省与预处理成本间权衡。

## EMT 实施要点

- **元件组装**：应避免并行写冲突；常用策略是局部缓冲、原子累加或先 COO 后压缩为 CSR/CSC。
- **开关事件分类**：区分"只改数值"（更新 $Y$ 矩阵元素）和"改变结构"（重做符号分析），后者对分解复用影响更大。
- **BTF 并行化**：利用传输线延迟自然解耦特性，在分区后各 BTF 块分配至独立线程。
- **恒导纳策略**：当开关状态不变时（$\mathbf{Y}_k$ 结构固定），每步只需更新右端项 $\mathbf{i}_k$，复用 LU 分解结果。
- **KLU + 网络分区**：KLU 的 BTF 结构可与 [[network-partitioning]] 联合使用，后者通过分区算法改变矩阵块结构。
- 稀疏求解应同时报告重排序、分解、求解、格式转换和数据传输时间，而非只报告总耗时。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| AMD 排序填充元减少 | 50–80% | Abusalah 2020 |
| KLU 并行加速比（12 核，H-Q grid） | 9.2×（SMPEMT2 相对单核） | Abusalah 2020 |
| KLU 相对单核基准加速（12 核） | 39× | Abusalah 2020 |
| KLU 相对 EMTP 求解器（12 核） | 33.8×（H-Q grid，41815 节点） | Abusalah 2020 |
| T0-grid 详细模型加速（12 核） | 12.6× | Abusalah 2020 |
| T0-grid 平均值模型加速（8 核） | 9.4× | Abusalah 2020 |
| MKLU + 填充元减少性能提升 | 最高 50%（实时 HIL） | Bruned 2023 |
| 主元有效性测试避免无效重分解 | >90% | Abusalah 2020（原文摘要） |
| KLU 适用规模 | 1000–100000 节点 | Ng 2012 |

**H-Q Grid 测试**（Abusalah 2020）：规模 41815×41815 矩阵，168025 非零元，29803 节点，349 台同步发电机（带励磁和调速器），23181 条 RLC 支路。并行版本 SMPEMT2 在 12 核下耗时 31 s，相对 EMTP（1048 s）和单核 KLU（1216 s）分别约 33.8 倍和 39 倍。

**T0-Grid 测试**（Abusalah 2020）：400 kV/50 Hz 网络，含 72 台同步发电机和大量可再生能源，详细模型 12 核下耗时 204 s（相对 EMTP 2580 s 约 12.6 倍），平均值模型 8 核下 27 s（相对 EMTP 253 s 约 9.4 倍）。

**实时 HIL**（Bruned 2023）：MKLU 替代 GenCode（基于代码生成的求解器），填充元减少 + 部分重分解结合，HYPERSIM 实时环境下性能提升最高 50%。测试案例：Xavier 配电网（619 节点）和 GHOST 微电网（663 节点）。

## 适用边界与失败模式

| 场景 | 推荐方法 | 失败模式 |
|------|----------|----------|
| 拓扑稳定、右端频繁变化 | KLU 直接法（复用 LU） | 主元过小、填充元失控 |
| 开关频繁改变结构 | KLU 部分重分解 | 频繁重排序、性能下降 |
| 强非线性/病态矩阵 | GMRES/BiCGSTAB + ILU 预处理 | 迭代不收敛、需预处理调优 |
| >100000 节点 | 多级分区 + KLU 分块并行 | 分区边界处理复杂 |
| GPU 稀疏计算 | CSR/SpMV + GPU 并行 | 不规则访问、负载不均 |
| 实时 HIL 步长约束 | MKLU + 补偿法（CM） | 主元失效导致数值不稳定 |

- 稀疏度高不必然意味着求解快；填充元和内存访问模式可能主导成本。
- GPU 上的稀疏计算受不规则内存访问和负载不均限制，不适合高填充元矩阵。
- 迭代法在强非线性、开关密集或病态网络上可能需要频繁重启或改用直接法。
- 主元有效性测试容差（通常 1%）需根据具体网络调试，过严会失去收益，过松会导致数值失稳。
- 只报告 $nnz$ 而不报告填充因子 $\rho_{\text{fill}}$、矩阵条件数、步长、拓扑变化频率和收敛准则，证据不完整。

## 相关页面

- [[nodal-admittance-matrix]]：节点导纳矩阵天然稀疏，KLU 的 BTF 结构可自动识别其块结构
- [[companion-model]]：EMT 元件离散化后贡献等效导纳和历史源，注入 $\mathbf{Y}_n$
- [[computational-acceleration]]：把稀疏技术放入更大的加速策略中
- [[gpu-parallel-acceleration]]：讨论 CSR/SpMV 等在 GPU 上的实现问题
- [[heterogeneous-computing]]：讨论稀疏组装、求解和事件处理在不同硬件间的分配
- [[network-partitioning]]：通过分区改变矩阵块结构和接口耦合
- [[iterative-solvers]]：GMRES/BiCGSTAB 等迭代求解方法
- [[newton-raphson-method]]：非线性方程的牛顿求解，与稀疏 Jacobian 矩阵配合

## 来源论文

- Abusalah 等 2019 - Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients (IEEE Open Access Journal of Power and Energy, 2020) — KLU 并行化改进，主元有效性测试 + 部分重分解，Hydro-Québec 网格 33.8× 加速
- Bruned 等 2023 - Sparse solver application for parallel real-time electromagnetic transient simulations (Electric Power Systems Research) — MKLU 集成到 HYPERSIM，填充元减少 + 部分重分解，实时 HIL 最高 50% 性能提升
- Ng & Matinpaniha 2012 - KLU: A Solver for Circuit Simulation (IEEE Trans on Power Systems) — KLU 求解器原始论文