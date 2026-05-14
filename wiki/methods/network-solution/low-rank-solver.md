---
title: "低秩求解器与分裂状态空间法"
type: method
tags: [low-rank, splitting-state-space, exponential-integrator, order-reduction, matrix-factorization, woodbury, svd, fdne-compression]
created: "2026-05-10"
updated: "2026-05-14"
---

# 低秩求解器与分裂状态空间法

## 定义

低秩求解器（Low-Rank Solver）和分裂状态空间法（Splitting State-Space Method）是一类以矩阵低秩近似、分解和子空间压缩为核心的高效 EMT 网络求解技术。其共同思想是：大规模含变流器系统的网络状态矩阵包含大量不随开关状态变化的常数结构，通过识别并分离这部分结构，可大幅降低时变部分的计算维度，避免对完整时变矩阵反复求逆或求指数。

低秩求解器侧重于**矩阵本身的低秩压缩**——利用 SVD、Woodbury 恒等式、分层树结构将 $O(N^3)$ 矩阵求逆降为 $O(N\log N)$ 或 $O(N)$；分裂状态空间法侧重于**状态矩阵的代数分裂**——将 $A = A_1 + A_2(s)$ 拆分为常数部分和开关相关时变部分，利用指数分裂公式将矩阵指数分解为可复用的子乘积。

核心公式：

$$
\dot{x} = Ax + Bu = (A_1 + A_2(s))x + Bu
$$

$$
Gv(t) = i_{\text{in}}(t) + i_{\text{his}}(t - \Delta t) \implies v(t) = G^{-1}i(t)
$$

$$
A \approx U_r \Sigma_r V_r^T, \quad r \ll n
$$

$$
(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}
$$

## EMT 中的角色

含电力电子变换器的大规模 EMT 仿真面临的核心计算瓶颈是网络方程求解：

- **网络求解占主导**：商业 EMT 程序在 87000 节点系统上仿真 1 秒暂态可耗时约 80 小时，其中 80%–97% 的时间用于网络方程求解 [Zhang 2021]。
- **状态矩阵时变**：开关状态变化改变电路拓扑，使系统矩阵 $A$ 每次变化时需重新处理；传统稀疏 LU 分解虽适合大规模稀疏网络，但前代/回代具有较强顺序性，难以并行。
- **维数灾难**：大规模新能源并网系统包含数十至数百个变流器，状态变量可达数万维，矩阵指数计算复杂度 $O(N^3)$ 成为效率瓶颈。
- **低秩/分裂方法的切入点**：将时变部分限制在开关相关子电路范围内，常数部分可复用预计算结果；利用网络矩阵的结构性低秩特性，将高维求逆转化为低维修正。

## 核心机制

### 方法一：分层低秩近似网络求解器（Zhang 2021）

#### 原理

Zhang 等提出了一种基于分层低秩近似（Hierarchical Low-Rank Approximation）的网络方程快速求解器 [Zhang 2021]。其核心观察是：电力网络导纳矩阵的逆中，**远距离母线组之间的交互子矩阵通常稀疏且可低秩近似**。

算法分为三个阶段：

**阶段 1：图划分与层次树构建**

基于全系统导纳矩阵 $G$ 构建无向图 $H = (V, E)$。初始化所有母线为独立节点，按层级执行平衡合并：

$$
W(S_1, S_2) = \frac{\sum_{v_1 \in S_1, v_2 \in S_2} G_{v_i, v_j}}{\max(|S_1|, |S_2|)}
$$

其中 $W(S_1, S_2)$ 为图划分权重函数，衡量两组母线间的平均电导。优先合并度为 1 的节点与其唯一邻居；随后在剩余节点中迭代选取权重最大的节点对进行合并，确保每层每个节点仅合并一次。重复该过程直至所有节点合并为单一根节点，生成高度为 $O(\log N)$ 的平衡二叉树层次结构。

**阶段 2：逆矩阵低秩近似**

预处理阶段计算全网络导纳逆矩阵 $G^{-1}$。从二叉树根节点开始递归遍历：

- 若当前子矩阵维度或数值秩小于预设阈值 $r_{\text{th}}$，则直接存储为显式矩阵。
- 否则计算其完整 SVD，根据预设误差阈值 $\varepsilon_{\text{th}}$ 截断保留前 $r$ 个奇异值及对应 $U, \Sigma, V$ 矩阵：

$$
A \approx A_r = \sum_{i=1}^{r} \sigma_i u_i v_i^*
$$

截断误差由 Eckart-Young-Mirsky 定理控制：

$$
\varepsilon = \|A - A_r\|_F = \sqrt{\sigma_{r+1}^2 + \dots + \sigma_p^2}
$$

- 若秩仍大于 $r_{\text{th}}$，则将子矩阵按行列索引划分为四个子块，对每个子块递归执行相同近似流程。

**阶段 3：快速矩阵向量乘法**

在每个仿真时间步，先计算历史电流 $i_{\text{his}}(t-\Delta t)$ 与注入电流 $i_{\text{in}}(t)$ 之和得到 $i(t)$。自顶向下遍历层次树执行矩阵向量乘法：

- 若子矩阵为显式形式，直接计算 $v = G^{-1}i$。
- 若为低秩形式 $(U, \Sigma, V)$，先计算中间向量 $x = \Sigma(Vi)$，再计算 $v = Ux$。
- 若为子块组合形式，则递归调用子节点计算并合并结果。

时间复杂度递推公式：

$$
T(N) \leq \begin{cases}
CN^2 & \text{if } N \leq r_{\text{th}} \\
CNr_{\text{th}} & \text{if rank}(G^{-1}) \leq r_{\text{th}} \\
2T(N/2) + 2C(N/2)r_{\text{th}} + N & \text{otherwise}
\end{cases}
$$

由此严格证明快速矩阵向量乘法算法的整体时间复杂度为 $O(N\log N)$。

#### 特点与适用场景

- **优势**：将固定拓扑下重复出现的线性求解转化为可预处理的分层矩阵向量乘法；低秩块天然具有并行计算潜力。
- **适用**：大规模交直流电网（39 母线、179 母线及扩展算例）、网络拓扑变化不频繁的场景。
- **局限**：若网络拓扑或元件状态频繁改变导致 $G$ 频繁更新，预处理 $G^{-1}$ 和分层 SVD 的代价可能影响总体收益 [Zhang 2021]。

### 方法二：分裂状态空间法（Fu 2025）

#### 原理

Fu 等提出了一种分裂状态空间法，用于含变流器电力系统的 EMT 仿真 [Fu 2025]。该方法通过通用解耦原则将状态空间方程拆分为常数部分和开关相关时变部分，再用多阶指数分裂公式组合求解。

**步骤 1：系统建模与增广转换**

含变流器的电力系统状态空间方程为：

$$
\dot{x} = Ax + Bu, \quad x(0) = x_0
$$

通过增广技术将非自治系统转为自治形式：

$$
\dot{\tilde{x}} = \tilde{A}\tilde{x}, \quad \tilde{x} = \begin{bmatrix} x \\ x_u \end{bmatrix}
$$

其中 $\tilde{x}$ 包含原始状态 $x$ 和辅助状态变量 $x_u$，用于包裹输入 $u$ 的影响。状态转移方程为：

$$
\tilde{x}(t) = e^{t\tilde{A}}\tilde{x}(0)
$$

**步骤 2：SASV 识别与矩阵分裂**

通过自动开关分组和开关相邻状态变量（SASV, Switch Adjacent State Variables）识别，定位每个开关周围的最小子电路拓扑。将状态矩阵分裂为：

$$
A = A_1 + A_2(s(t))
$$

其中 $A_1$ 包含不随开关状态变化的网络、元件和耦合关系（如线路、滤波器等），$A_2(s(t))$ 只保留由开关状态 $s(t)$ 决定的最小子电路贡献，具有块对角结构。

**步骤 3：指数分裂公式**

利用指数分裂公式将矩阵指数分解为子矩阵指数乘积。一阶 Trotter 公式：

$$
e^{t(A_1 + A_2)} = e^{tA_1}e^{tA_2} + O(t^2)
$$

二阶 Strang 分裂公式：

$$
e^{t(A_1 + A_2)} = e^{\frac{t}{2}A_1}e^{tA_2}e^{\frac{t}{2}A_1} + O(t^3)
$$

更高阶分裂公式（如 Yoshida 四阶分裂）可通过系数 $\alpha_i, \beta_i$ 的精心选择达到 $O(t^4)$ 精度：

$$
e^{t(A_1 + A_2)} \approx \prod_{i=1}^{m} e^{\alpha_i t A_1} e^{\beta_i t A_2}
$$

**步骤 4：预计算与复用**

- $A_1$ 对应的矩阵指数在仿真开始计算一次，整个仿真过程中保持不变。
- $A_2(s(t))$ 仅在开关状态改变时局部更新，避免对完整时变矩阵反复求指数。

#### 特点与适用场景

- **优势**：将时变计算限制在开关相关子电路，将不变网络部分的指数计算复用；可通过不同阶数指数分裂控制近似误差。
- **适用**：含多开关变流器系统（MMC、风电场、LLC 谐振变换器等）、开关频率达数百 kHz 的高频场景。
- **局限**：需要精确的 SASV 识别；高阶分裂公式实现复杂度增加；对非变流器主导的网络系统收益有限。

#### 量化结果 [Fu 2025]

| 测试场景 | 系统规模 | 计算负担降低 | 精度 | 加速比 |
|---------|---------|------------|------|--------|
| 含 DC 负载配电网 | 33 节点 | 40%–60% | 最大局部误差 <0.1% | 1.7x–2.5x |
| LLC 谐振变换器 | 开关频率 200 kHz | 高频下优势显著 | 累积误差 <0.5% | 3x–5x |
| 大型风电场 | 100 台 2MW VSC 风机 | 内存减少约 30% | 最大偏差 <0.3% | >5x |
| MMC-HVDC 换流器 | 400 子模块 | 矩阵指数计算从 80% 降至 <15% | — | 4x–6x |

### 方法三：连接域提取分解法（Duan 2020）

#### 原理

Duan 和 Dinavahi 提出了一种连接域提取（LDE, Linking-Domain Extraction）分解方法，用于大规模交直流网络的并行 EMT 仿真 [Duan 2020]。

**LDE 分解**：将网络电导矩阵 $G$ 解耦为对角块矩阵 $G_d$ 与连接域矩阵 $L$ 之和：

$$
G = G_d + L
$$

其中 $G_d$ 由多个子系统内部矩阵沿对角线组成（可并行求逆），$L$ 只描述子系统之间的连接关系。

**引理：连接域矩阵的零和特性**

对连接域矩阵 $L$ 有严格的行列和为零特性：

$$
\sum_{j=1}^{N} L_{i,j} = 0, \quad \forall 1 \leq i \leq N
$$

由此可证明 $L$ 可分解为：

$$
L = C \Lambda C^T
$$

其中 $\Lambda$ 为非负对角阵（存储耦合电导值），$C$ 为仅含 $\{0, 1, -1\}$ 的稀疏拓扑变换矩阵（节点-支路关联矩阵）。

**Woodbury 恒等式并行求逆**：

$$
G^{-1} = G_d^{-1} - G_d^{-1}C(\Lambda^{-1} + C^T G_d^{-1}C)^{-1}C^T G_d^{-1}
$$

该公式将 $O(N^3)$ 全局求逆转化为：
1. 对角块 $G_d^{-1}$ 的完全并行求逆
2. $k \times k$ 小矩阵 $(\Lambda^{-1} + C^T G_d^{-1}C)^{-1}$ 的求逆（$k$ 为连接域维度，通常 $k \ll N$）

**算法流程**：
1. 网络离散化：采用梯形积分法将动态元件离散为等效并联电导与历史电流源。
2. 拓扑解耦：根据子系统划分边界，将非对角耦合元素提取至 $L$。
3. 连接域特征提取：构建 $\Lambda$ 和 $C$，验证 $L = C\Lambda C^T$。
4. 并行预计算：在 FPGA/GPU 上并行求取 $G_d^{-1}$ 和小矩阵修正项。
5. 时步求解：执行并行矩阵向量乘法 $v = G^{-1}i_{\text{eq}}$。

#### 量化结果 [Duan 2020]

| 指标 | 数值 |
|------|------|
| 矩阵求逆复杂度 | $O(N^3) \to O(N)$ |
| FPGA 单步延迟 | <10 μs (Xilinx UltraScale+) |
| GPU 单步延迟 | <25 μs (NVIDIA CUDA) |
| 相比 PSCAD/EMTDC 最大相对误差 | <0.05% |
| 相比 Schur Complement FPGA 加速比 | 6.8x |
| 相比 Schur Complement GPU 加速比 | 4.2x |
| 连接域扩大 300% 时 LDE 时间增长 | ~18% |
| 连接域扩大 300% 时 SC 时间增长 | >400% |

### 方法四：FDNE 低秩压缩（Hu 2015）

#### 原理

Hu 等针对 FDNE（频率相关网络等值）在 RTDS 实时仿真中的算力瓶颈，提出了一种结合 SVD 低秩压缩与模块划分的方案 [Hu 2015]。

FDNE 的导纳矩阵有理函数模型为 $Y(s) = \sum_{k=1}^{n} \frac{R_k}{s - a_k} + D$，其中 $R_k$ 为第 $k$ 个极点的留数矩阵。传统状态空间实现中，同一极点会为 $N$ 端口矩阵重复引入大量状态变量，但对应留数矩阵 $R_k$ 往往是低秩的。

对每个 $R_k$ 作 SVD 分解：

$$
R_k = U S V^T
$$

当矩阵秩 $r < (N+1)/2$ 时，通过 $USV^T$ 重构状态矩阵，剔除冗余状态变量。单极点计算量从 $2N^2 + 2N$ 降至 $4rN$，降幅可达 50% 以上。

FDNE 单步仿真计算量（浮点乘法次数）：

$$
O = 2nN^2 + N^2 + 2nN
$$

压缩后划分为 $k$ 个并行子模块，单模块计算量：

$$
O_{\text{component}} = \frac{2nN^2}{k} + N^2 + \frac{2nN}{k}
$$

#### 量化结果 [Hu 2015]

| FDNE 端口 | 压缩前计算量 | 压缩后计算量 | RMS 误差 | 是否实时 |
|-----------|------------|------------|---------|---------|
| Y1 (P=1, n=30) | 1080 | — | $1.2 \times 10^{-5}$ | 是 |
| Y4 (P=2, n=46) | 3900 | 3276 | $1.96 \times 10^{-5}$ | 是 |
| Y10 (P=6, n=64) | 44410 | 26964 | — | 需划分 |

Y10 进一步划分为 11 个子模块后，各模块计算量分布在 1692–3204 之间，全部低于 RTDS GPC 处理器阈值 3396，实现 100% 实时仿真成功率。

## 形式化表达汇总

| 符号 | 含义 |
|------|------|
| $N$ | 系统母线/状态变量总数 |
| $r$ | 低秩近似的有效秩，$r \ll N$ |
| $G$ | 网络导纳/电导矩阵 |
| $G^{-1}$ | 网络逆矩阵（预处理） |
| $A_1$ | 分裂状态空间中的常数矩阵 |
| $A_2(s)$ | 分裂状态空间中的开关相关时变矩阵 |
| $SASV$ | 开关相邻状态变量（Switch Adjacent State Variables） |
| $r_{\text{th}}$ | 预设秩阈值 |
| $\varepsilon_{\text{th}}$ | 预设截断误差阈值 |
| $k$ | LDE 连接域维度 / FDNE 划分子模块数 |
| $G_d$ | 对角块矩阵（LDE） |
| $L$ | 连接域矩阵（LDE） |
| $C, \Lambda$ | LDE 中 $L = C\Lambda C^T$ 的因子 |

## 关键技术挑战

### 低秩结构的条件依赖性

低秩近似的有效性依赖于网络拓扑的结构性特征——远距离母线组间交互子矩阵的自然稀疏性。但这并非所有拓扑和运行方式下的普遍规律。在高度互联、紧密耦合的网络中，子矩阵可能不具备低秩特性，导致压缩收益有限甚至为负 [Zhang 2021]。

### 开关事件触发的局部更新

分裂状态空间法中，$A_2(s(t))$ 仅在开关状态改变时更新。但当系统中开关数量众多且事件频繁时，局部更新次数增加，可能抵消预计算复用的收益。SASV 识别的精确性也直接影响 $A_2$ 的维度——识别过粗会导致时变部分过大，识别过细则增加管理开销 [Fu 2025]。

### 拓扑变化时的预处理成本

分层低秩近似和 LDE 方法均依赖网络拓扑相对固定的前提。当线路投切、元件故障等导致 $G$ 频繁变化时，预处理阶段（SVD 分解、层次树重建、$G_d^{-1}$ 计算）的代价可能超过单步求解的节省。对于频繁拓扑变化的场景，需评估预处理-求解的总成本 [Zhang 2021; Duan 2020]。

### 数值误差的累积控制

指数分裂公式引入的局部截断误差在长时间仿真中可能累积。一阶 Trotter 公式局部误差为 $O(t^2)$，二阶 Strang 为 $O(t^3)$，高阶公式虽精度更高但实现更复杂。需要设计自适应阶数选择或误差监控机制，在精度和效率间取得平衡 [Fu 2025]。

## 量化性能边界

| 方法 | 加速比 | 误差控制 | 适用规模 | 数据来源 |
|------|--------|---------|---------|---------|
| 分层低秩近似 | 最高 2.8x（相对稀疏 LU） | 截断误差 < $\varepsilon_{\text{th}}$ | 39–179 母线及扩展 | Zhang 2021 |
| 分裂状态空间 | 1.7x–6x（依场景） | 局部误差 <0.1% | 33 节点至 400 SM MMC | Fu 2025 |
| LDE 分解 | 4.2x–6.8x（相对 SC） | 相对误差 <0.05% | 含 MMC 大规模交直流 | Duan 2020 |
| FDNE SVD 压缩 | 计算量降低 15%–50% | RMS 误差 $<2 \times 10^{-5}$ | 1–6 端口 FDNE | Hu 2015 |

## 适用边界与选择指南

### 场景-方法推荐表

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|------|
| 大规模交直流电网，拓扑稳定 | 分层低秩近似 / LDE 分解 | 网络求解占 80%–97%，低秩压缩收益最大 |
| 含多开关变流器系统（MMC、风电场） | 分裂状态空间法 | 自动识别开关相关子电路，避免重复计算 |
| 高频谐振变换器（>100 kHz） | 分裂状态空间法 | 高频开关下指数分裂优势显著（3x–5x） |
| FPGA/GPU 实时并行仿真 | LDE 分解 | 直接并行求逆，FPGA <10 μs 单步延迟 |
| FDNE 多端口实时部署 | FDNE SVD 压缩 + 划分 | 消除状态冗余，多核并行分摊 |
| 拓扑频繁变化场景 | 需谨慎评估 | 预处理代价可能超过收益，考虑增量更新策略 |

### 方法对比表

| 方法 | 核心策略 | 复杂度 | 并行性 | 预处理需求 | 典型加速 |
|------|---------|--------|--------|-----------|---------|
| 分层低秩近似 | SVD + 层次树 | $O(N\log N)$ | 高（低秩块并行） | 是（$G^{-1}$ 分解） | 2.8x |
| 分裂状态空间 | $A = A_1 + A_2$ | $O(r^3)$ 每块 | 中（块内并行） | 是（$e^{tA_1}$ 预计算） | 1.7x–6x |
| LDE 分解 | $G = G_d + L$ + Woodbury | $O(N)$ | 高（对角块并行） | 是（$G_d^{-1}$ 预计算） | 4.2x–6.8x |
| FDNE SVD 压缩 | 留数矩阵秩压缩 | $O(rN)$ | 中（子模块并行） | 是（SVD 分解） | 计算量降 50% |

## 相关方法

- [[state-space-method]] — 状态空间建模基础
- [[exponential-integrator]] — 指数积分与分裂求解
- [[model-order-reduction]] — 模型降阶理论
- [[vector-fitting]] — 有理逼近与留数提取
- [[frequency-dependent-network-equivalent]] — FDNE 等值
- [[companion-circuit]] — 伴随电路与 Schur 补
- [[nodal-analysis]] — 节点导纳矩阵法
- [[parallel-computing]] — 并行计算加速
- [[numerical-integration]] — 数值积分方法

## 相关模型

- [[fdne-model]] — 频率相关网络等值模型
- [[mmc-model]] — MMC 大规模系统模型
- [[equivalent-modeling]] — 等效建模方法

## 相关主题

- [[low-rank-and-efficient-solvers]]
- [[network-equivalent]]
- [[parallel-computing]]
- [[real-time-simulation]]
- [[emt-simulation]]

## 来源论文

- **Zhang 等 (2021)** — "A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation", IEEE Trans. Power Delivery. 提出分层低秩近似算法，将网络求解复杂度从 $O(N^2)$ 降至 $O(N\log N)$，在 39/179 母线系统上验证最高 2.8x 加速。
- **Fu 等 (2025)** — "Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations", IEEE Trans. Power Delivery, 40(1). 提出分裂状态空间法，通过 SASV 识别自动分离常数/时变部分，结合多阶指数分裂公式，在 MMC/风电场/LLC 变换器等场景中验证 1.7x–6x 加速。
- **Duan & Dinavahi (2020)** — "A Novel Linking-Domain Extraction Decomposition Method for Parallel EMT Simulation of Large-Scale AC/DC Networks", IEEE Trans. Power Delivery. 提出 LDE 分解法，利用 Woodbury 恒等式实现网络矩阵的直接并行求逆，在 FPGA/GPU 上验证 4.2x–6.8x 加速。
- **Hu 等 (2015)** — "Compacting and partitioning-based simulation solution for frequency-dependent network equivalents in real-time digital simulator", IET Gen. Trans. Distrib. 提出 FDNE 的 SVD 低秩压缩与模块划分联合策略，在 RTDS 上实现多端口 FDNE 的实时仿真。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[a-hierarchical-low-rank-approximation-based-network-solver-for-emt-simulation|A Hierarchical Low-Rank Approximation Based Network Solver f]] | 2020 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[adaptive-variable-step-size-calculation-method-for-transient-temperature-rise-and-fall|Adaptive Variable Step Size Calculation Method for Transient]] | 2024 |
| [[an-interface-method-for-co-simulation-of-emt-model-and-shifted-frequency-emt-mod|An Interface Method for Co-Simulation of EMT Model and Shift]] | 2025 |
