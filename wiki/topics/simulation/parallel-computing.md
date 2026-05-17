---
title: "并行计算"
type: topic
tags: [并行计算, GPU加速, 多速率仿真, HPC, 实时仿真, EMT加速, BBD矩阵, 网络分区]
created: "2026-04-13"
updated: "2026-05-17"
---

# 并行计算

## 定义

并行计算在 EMT 语境中指通过网络分区、元件级解耦、时间并行、任务映射或硬件并行来降低大规模暂态仿真的墙钟时间。它既包括离线 HPC/GPU 加速，也包括满足确定步长约束的实时并行仿真。并行计算是大规模 [[real-time-simulation]] 和大规模 [[co-simulation]] 的计算底座，与 [[frequency-dependent-modeling]] 的快速拟合/宽频模型实现 ([[multirate-method]]) 的分区调度、以及 [[mmc-model]]、 [[vsc-model]] 等细粒度电力电子模型强相关。

## EMT中的角色

 EMT 仿真的计算瓶颈主要来自三个方面：① 大规模系统的导纳矩阵求逆（$O(n^3)$ 复杂度）；② 大量开关动作的状态更新；③ 多速率耦合系统的接口同步。并行计算通过以下方式解决这些瓶颈：

- **网络级并行**：利用传输线自然延迟特性，通过块对角分解（BTF）或边界块对角矩阵（BBD）实现网络方程的并行求解
- **元件级并行**：将 MMC、子模块、风电场等可独立更新的子系统分配到不同计算单元
- **时间并行**：通过 Parareal、PEGR 等算法在时间维度上实现并行
- **硬件加速**：利用 GPU SIMD/SIMT 架构或 FPGA 实现计算加速

## 分类或机制

### 网络级并行

网络级并行的核心是将系统导纳矩阵 $\mathbf{Y}$ 分解为可并行求解的对角块结构。主要方法包括：

**1. 块对角分解（BTF）**
当系统中存在自然解耦元件（如长传输线）时，$\mathbf{Y}$ 可分解为：
$$\mathbf{Y} = \begin{bmatrix} \mathbf{Y}_1 & 0 \\ 0 & \mathbf{Y}_2 \end{bmatrix}$$

各对角块 $\mathbf{Y}_i$ 可独立 LU 分解并并行求解。KLU 稀疏求解器利用传输线的自然解耦特性实现自动 BTF 分解。

**2. 边界块对角矩阵（BBD）**
对于人工分区的大型系统，导纳矩阵重排为：
$$\mathbf{Y}_{BBD} = \begin{bmatrix} \mathbf{Y}_1 & 0 & \cdots & \mathbf{C}_1 \\ 0 & \mathbf{Y}_2 & \cdots & \mathbf{C}_2 \\ \vdots & \vdots & \ddots & \vdots \\ \mathbf{C}_1^T & \mathbf{C}_2^T & \cdots & \mathbf{Y}_c \end{bmatrix}$$

其中 $\mathbf{Y}_i$ 为各分区的内部导纳矩阵，$\mathbf{C}_i$ 为边界连接矩阵。角矩阵 $\mathbf{Y}_c$ 的阶数远小于整体矩阵，可独立求逆后通过 Schur 补回代各子块。

**3. Woodbury 恒等式**
对于 $\mathbf{Y} = (\mathbf{Z} + \mathbf{U}\mathbf{C}\mathbf{V}^T)^{-1}$ 的结构，Woodbury 恒等式给出：
$$\mathbf{Y}^{-1} = \mathbf{Z}^{-1} - \mathbf{Z}^{-1}\mathbf{U}(\mathbf{C}^{-1} + \mathbf{V}^T\mathbf{Z}^{-1}\mathbf{U})^{-1}\mathbf{V}^T\mathbf{Z}^{-1}$$

Zhang 等 2020 提出基于连接域提取（Linking-Domain Extraction, LDE）与 Woodbury 恒等式的矩阵分解求逆算法，实现导纳矩阵的直接并行求逆。

**4. 稀疏求解器并行**
KLU 求解器通过稀疏矩阵填充度排序（COLAMD）优化 LU 分解的并行性：
- 超节点合并（supernodal amalgamation）
- 混合稀疏-密集 LU（BLKLU）
- 多线程 BTF 并行（OpenMP）

### 元件级并行

元件级并行将系统中可独立更新的元件分配到不同线程：

**1. MMC 子模块级并行**
MMC 每个桥臂含 $N$ 个子模块，每个子模块的状态更新（电容电压、开关状态）相互独立：
$$v_{cap,k}^{n+1} = v_{cap,k}^n + \frac{\Delta t}{C}\left(i_{arm,k}^n - i_{comp,k}^n\right)$$

可分配 $N$ 个 CUDA 线程并行处理各子模块，结合桥臂等效分组进一步减少线程同步开销。

**2. 风电场聚合并行**
风电场含大量相同型号风力发电机，每台机组的状态更新可并行执行：
$$\mathbf{x}_{wind,i}^{n+1} = f(\mathbf{x}_{wind,i}^n, \mathbf{u}_{grid}^n)$$

相同型号机组的模型参数相同，通过数据并行（SIMD）实现批量更新。

**3. 控制系统解耦并行**
控制系统（如 VSC-HVDC 的 PWM、PLL、内环控制器）可封装为独立 FMU（Functional Mock-up Interface）：
$$y_{FMU} = h(x_{FMU}^n, u_{interface}^n)$$

各 FMU 通过标准接口与主 EMT 求解器交互，实现控制与电气部分的并行计算。

### 时间并行与多速率

**1. Parareal 算法**
Parareal 将时间区间 $[0,T]$ 分解为 $N$ 个子区间，各子区间并行求解：
$$u_i^{k+1} = \mathcal{G}(\tau_i, \tau_{i-1})(u_{i-1}^{k+1}) + (\mathcal{F}_i - \mathcal{G})(\tau_i, \tau_{i-1})(u_{i-1}^k)$$

其中 $\mathcal{F}_i$ 为精细求解器（完整 EMT），$\mathcal{G}$ 为粗糙求解器（如平均值模型）。经过 $k$ 次迭代收敛后，$k \ll N$，实现时间并行。

**2. PEGR（Parallel Electromagnetic Transient Group Ranking）**
PEGR 通过对 EMT 方程重新排序实现时间并行：
$$[\mathbf{Y}_{BBD}]\mathbf{v}^{n+1} = \mathbf{i}_{hist}^n + \mathbf{i}_{source}^{n+1}$$

将系统分为 $P$ 组，各组方程在时间步 $n+1$ 内并行求解。Xiong 2024 将 PEGR 从状态空间推广至 MANA（改进增广节点分析）公式。

**3. 多速率联合仿真**
多速率方法允许不同子系统使用不同时间步长（如 500 μs 大系统 + 50 μs 电力电子）：
$$\Delta t_{slow} = M \cdot \Delta t_{fast}, \quad M \in \mathbb{N}$$

通过接口数据插值或历史项外推实现不同步长子系统间的数据交换。

### 硬件与通信平台

**1. GPU 架构**
NVIDIA GPU 采用流式多处理器（SM）架构，每个 SM 含多个 CUDA 核心：
- SIMD/SIMT 执行模式：同一指令在多个线程上并行执行
- 线程层级：Grid → Block → Thread → Warp（32 线程）
- 内存层级：Register → Shared Memory → Global Memory → Host Memory

**2. CPU 多线程**
多核 CPU 并行通过 OpenMP、MPI 或线程库实现：
- OpenMP：`#pragma omp parallel for` 自动并行化 for 循环
- MPI：多进程分布式并行，进程间通过消息传递同步

**3. FPGA 实时仿真**
FPGA 适用于纳秒级步长实时仿真：
- 流水化架构：将 EMT 计算流水线化
- 定点运算：避免浮点运算延迟
- 定制硬件：针对特定电路拓扑优化

**4. 异构计算**
CPU-GPU 异构架构将不同任务分配给最适合的处理单元：
- CPU：复杂逻辑判断、分支控制
- GPU：大规模矩阵运算、数据并行计算

## 形式化表示

### 加速比与并行效率

并行 EMT 的收益用加速比 $S_p$ 和并行效率 $E_p$ 描述：
$$S_p = \frac{T_1}{T_p}, \qquad E_p = \frac{S_p}{p}$$

其中 $T_1$ 为串行运行时间，$T_p$ 为 $p$ 个计算单元上的运行时间。理想线性加速下 $S_p = p$，$E_p = 1$。

### 网络级并行复杂度

KLU 稀疏求解器的复杂度为 $O(n \cdot nnz(Y))$，远低于密集 LU 的 $O(n^3)$。BTF 分解后各子块独立求解：
- 子块 $i$ 的求解时间：$O(n_i^2)$
- 总时间（并行）：$\max_i O(n_i^2)$
- 加速比：$\frac{\sum_i O(n_i^3)}{\max_i O(n_i^2)}$

### GPU 并行复杂度

MT-EMTP（Zhou & Dinavahi 2014）采用节点映射结构（NMS）将 $\mathbf{Y}$ 转换为块对角稀疏格式：
- 串行复杂度：$O(n^3)$（LU 分解）
- GPU 并行复杂度：$O(n \cdot nnz(Y) / t_{threads})$

当系统规模足够大时，GPU 加速比持续增长而无饱和趋势（Zhou 2014）。

### BBD 并行加速

ParaEMT（Xiong 2024）的 BBD 并行求解：
- $P$ 个 MPI 进程：各进程求解一个分区
- 最优分区数 $P_{opt} \approx 25 \sim 45$
- 最大加速比：36（10,080 母线系统）

### 实时仿真约束

实时仿真必须满足 $\Delta t \leq T_{deadline}$：
$$T_{compute} + T_{communicate} \leq \Delta t$$

对于纳秒级步长（如 FPGA 实时仿真），$T_{compute}$ 必须极短；对于毫秒级步长（如实时 HIL），$T_{deadline}$ 约束相对宽松。

## 关键技术挑战

### 1. 分区接口强耦合

当分区边界处的耦合元件（如近距离并联换流器）电气距离很小时，边界电流 $\mathbf{i}_{boundary}$ 变化剧烈，分区独立求解误差增大：
$$\|\mathbf{i}_{boundary}^{true} - \mathbf{i}_{boundary}^{approx}\| > \epsilon_{tol}$$

**解决思路**：迭代接口法（如惠特尼分解）或提高边界等值精度。

### 2. 负载不均衡

各分区计算量差异导致部分进程空闲：
$$\text{LoadBalance} = \frac{\max_i T_i}{\frac{1}{P}\sum_i T_i}$$

**解决思路**：图划分启发式算法（METIS、Scotch）结合线性规划精确验证。

### 3. 通信延迟

MPI 进程间同步和边界数据传递消耗大量时间：
$$T_{comm} = T_{latency} + \frac{data_{size}}{bandwidth}$$

**解决思路**：异步通信（计算与通信重叠）、边界数据压缩。

### 4. 时间并行收敛性

Parareal 类算法在强耦合系统（如高压直流）上收敛慢，需多次迭代：
$$|u_i^{k+1} - u_i^k| > \delta \quad \text{经过多次迭代}$$

**解决思路**：使用更好的粗糙求解器或混合空间-时间并行。

### 5. 内存带宽瓶颈

GPU 仿真中，显存带宽成为主要瓶颈：
$$T_{memory} \gg T_{compute}$$

**解决思路**：数据预取、共享内存复用、混合精度计算（FP16/FP32）。

## 量化性能边界

### GPU 并行加速（Zhou & Dinavahi 2014）

| 系统规模（母线） | EMTP-RV 时间 (s) | MT-EMTP 时间 (s) | 加速比 |
|----------------|-----------------|-----------------|--------|
| 39 (×1) | 0.89 | 0.97 | 0.92 |
| 39 (×8) | 10.2 | 4.5 | 2.27 |
| 39 (×16) | 44.5 | 12.8 | 3.48 |
| 39 (×32) | 189.3 | 43.7 | 4.33 |
| 39 (×63) | 892.1 | 158.4 | **5.63** |

测试条件：100 ms 仿真时长，Δt = 20 μs，NVIDIA Tesla C2075 GPU。

### ParaEMT BBD+MPI 并行（Xiong 2024）

| 分区数 | 1 MPI 进程 | 21 MPI 进程 | 42 MPI 进程 | 84 MPI 进程 |
|--------|-----------|------------|------------|------------|
| 1 | 1.0× | 1.0× | 1.0× | 1.0× |
| 21 | 0.9× | 15.2× | 17.8× | 18.1× |
| 42 | 0.8× | 22.4× | **36.0×** | 35.2× |
| 84 | 0.7× | 25.3× | 28.1× | 29.5× |

测试系统：10,080 母线（30,240 节点）合成系统，HPC 平台 NREL Eagle。

### CPU 并行加速（Abusalah 2018）

| 并行方法 | 测试系统 | 计算单元 | 加速比 |
|---------|---------|---------|--------|
| KLU+BTF | Hydro-Québec 1666 母线 | 12 线程 | 8.2× |
| MPI 域分解 | IEEE 118 | 8 进程 | 6.5× |
| OpenMP | IEEE 30 | 4 线程 | 3.1× |
| FMI+多步长 | CIGRE HVDC | 4 核 | 4.2× |

### 实时仿真规模

| 仿真平台 | 系统规模 | 步长 | 实时因子 |
|---------|---------|------|----------|
| RTDS | 48 母线 | 52 μs | 1.0× |
| HYPERSIM | 1666 母线，13626 RLC | 30 μs | 1.0× |
| FPGA (Virtex-7) | 100 节点 | 200 ns | 1.0× |
| GPU (MT-EMTP) | 2458 三相母线 | 20 μs | 0.1× (离线) |

## 适用边界与选择指南

### 按系统特性选择并行架构

| 系统特性 | 推荐并行方法 | 关键指标 |
|---------|------------|----------|
| 含长传输线/电缆自然解耦 | BTF 自动分解 | $S_p > 10$ |
| 大规模 IBR 换流器群 | BBD+MPI | $S_p \approx 25-36$ |
| 电力电子详细模型 | GPU 线程级并行 | $S_p \approx 5-10$ |
| 多速率联合仿真 | Parareal/PEGR | $S_p \propto k_{iter}$ |
| 实时 HIL 测试 | FPGA/实时仿真器 | $\Delta t \leq T_{deadline}$ |
| 异构集群 | CPU-GPU 协同 | $T_{compute}$ 最小化 |

### 按系统规模选择硬件

| 规模 | 节点数 | 推荐硬件 | 预期加速 |
|------|--------|---------|---------|
| 小型 | < 1000 | 单机多线程 | 2-5× |
| 中型 | 1000-10000 | GPU/多节点 MPI | 5-20× |
| 大型 | 10000+ | HPC 集群（MPI+GPU） | 20-100× |
| 超大规模 | 50000+ | 超级计算机 | 100-500× |

### 并行方法选择决策树

```
系统有自然传输线解耦？
  ├─ 是 → 使用 KLU/BTF 自动并行
  └─ 否 → 需要人工分区？
          ├─ 是 → BBD+MPI 适合 IBR 主导系统
          └─ 否 → 元件级并行/GPU 加速
                  
需要实时仿真？
  ├─ 是 → FPGA 或专用实时仿真器
  └─ 否 → 离线加速？
          ├─ 小系统 → OpenMP 多线程
          ├─ 中系统 → GPU 加速
          └─ 大系统 → HPC MPI+多 GPU
```

## 相关方法

- [[real-time-simulation]] - 实时仿真约束下的并行策略
- [[co-simulation]] - 多求解器并行协同
- [[multirate-method]] - 不同子系统差异化步长并行
- [[gpu-accelerated-simulation]] - GPU并行架构应用
- [[nodal-analysis]] - 网络分割与并行求解
- [[fixed-admittance]] - 避免导纳矩阵重构的并行优化
- [[state-space-method]] - 子系统状态空间并行求解
- [[numerical-integration]] - 并行积分算法实现
- [[hil-simulation]] - 分布式HIL并行测试
- [[frequency-dependent-modeling]] - 频变模型并行计算

## 相关模型

- [[mmc-model]] - 子模块级并行建模
- [[vsc-model]] - 换流器并行仿真
- [[fdne-model]] - 外部网络并行等值
- [[synchronous-machine-model]] - 电机集群并行计算
- [[dfig-model]] - 风电场聚合并行

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Zhou & Dinavahi | 2014 | MT-EMTP GPU 大规模线程并行框架，5.63× 加速 |
| Xiong 等 | 2024 | ParaEMT 开源框架，BBD+MPI，25-36× 加速 |
| Mu 等 | 2014 | 网络分区多速率并行EMT，稳定判据 |
| Abusalah | 2018 | KLU+BTF自动网络撕裂，Hydro-Québec 8.2× |
| Chen 等 | 2010 | 元件级与网络级混合并行架构 |
| Song 等 | 2018 | GPU线程映射与自动代码生成 |
| Bruned 等 | 2026 | 补偿法并行EMT联合仿真 |
| Zhang 等 | 2020 | LDE连接域提取+Woodbury恒等式 |
| Sun & Xu | 2023 | 电力电子变压器并行等效建模 |