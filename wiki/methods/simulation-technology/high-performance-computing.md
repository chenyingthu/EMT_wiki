---
title: "高性能计算 (High Performance Computing)"
type: method
tags: [hpc, high-performance-computing, parallel, cluster, supercomputing, mpi, openmp, gpu, heterogeneous]
created: "2026-05-02"
updated: "2026-05-14"
---

# 高性能计算 (High Performance Computing)

## 定义

高性能计算（High Performance Computing, HPC）是指利用多核处理器、共享内存服务器、分布式集群、并行文件系统和作业调度环境来执行大规模电磁暂态（EMT）仿真或批量仿真的计算范式。HPC 关注的是**系统级并行架构**——包括通信机制、负载均衡、任务调度和可扩展性——而非单一硬件平台的加速能力。

HPC 与 GPU 加速、FPGA 实时仿真构成互补关系：[[gpu-parallel-acceleration]] 聚焦于单卡或多卡内核层加速，[[hardware-acceleration]] 讨论专用硬件能力，[[heterogeneous-computing]] 处理节点内 CPU/GPU/FPGA 协同。HPC 层则解决跨节点通信、集群管理、数据归档和可复现实验等更高层问题。

在 EMT 仿真中，HPC 的核心挑战来源于三个维度：

1. **高维度**：新型电力系统节点数目剧增（如 Hydro-Québec 1666 母线实测系统、NREL 10080 母线合成系统），网络方程维数达到数万至数十万。
2. **高精度**：电力电子设备纳秒级开关动作要求 50–100 μs 甚至更小的仿真步长，单个 MMC 可含数百个开关器件。
3. **高速度**：批量参数扫描、故障集分析、蒙特卡洛仿真和硬件在环（HIL）对仿真吞吐量和实时性提出严苛要求。

## EMT 中的角色

HPC 在 EMT 仿真中服务三大目标：

| 目标 | 场景 | 关键技术 |
|------|------|----------|
| 大规模网络仿真 | 数千至数万母线系统、交直流混联电网 | [[network-partitioning]]、稀疏求解、并行通信 |
| 批量吞吐 | 参数扫描、故障集、蒙特卡洛、控制参数整定 | 任务并行、多速率、异构计算 |
| 工程运行 | 长仿真管理、检查点、日志、数据归档、可复现实验 | MPI 集群、作业调度、并行文件系统 |

对实时 HIL，HPC 集群并不天然满足硬实时约束——必须证明最坏步长时间、网络通信时延和 I/O 抖动满足 [[real-time-simulation]] 与 [[hil-simulation]] 的要求。

## 核心并行架构

### 1. 共享内存并行（Shared-Memory Parallelism）

共享内存并行通常使用线程（OpenMP、pthread）或任务运行时，适合单节点内的元件更新、稀疏向量操作和部分组装任务。

**OpenMP 多线程模型**：

$$
\text{speedup}_{\text{OpenMP}} = \frac{T_1}{T_p} \leq p \cdot \left(1 + \frac{\alpha}{p}\right)^{-1}
$$

其中 $\alpha$ 表示串行部分比例（Amdahl 定律），$p$ 为线程数。实际 EMT 应用中还需考虑：

- **NUMA 访问延迟**：跨 NUMA 节点的内存访问比本地节点慢 2–3 倍
- **锁竞争**：共享全局变量（如历史电流源数组）的互斥操作
- **伪共享（False Sharing）**：不同线程写入同一缓存行的相邻变量
- **动态负载不均**：不同子网计算量差异导致线程空闲等待

Xu 等（2025）提出的低维等效模型结合 OpenMP 多线程，在 100 MW 光伏电站中实现了**串行模式 80 倍加速**，并行模式获得**2–3 倍二次加速**，验证了 OpenMP 在中等规模多 VSC 系统中的有效性。

### 2. 分布式内存并行（Distributed-Memory Parallelism）

分布式内存并行使用 MPI（Message Passing Interface），每个进程持有子网络、局部矩阵和边界变量，通过消息传递交换接口量。

**子域分解形式**：

$$
\begin{bmatrix}
\mathbf{Y}_{11} & \mathbf{Y}_{12} \\
\mathbf{Y}_{21} & \mathbf{Y}_{22}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}_1 \\
\mathbf{v}_2
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{i}_1 \\
\mathbf{i}_2
\end{bmatrix}
$$

其中 $\mathbf{Y}_{11}$ 和 $\mathbf{Y}_{22}$ 为子域自导纳矩阵，$\mathbf{Y}_{12} = \mathbf{Y}_{21}^\top$ 为子域间互导纳矩阵。通过传输线自然解耦（TLM delay）或补偿法（compensation method）使 $\mathbf{Y}_{12}$、$\mathbf{Y}_{21}$ 稀疏化，从而减少通信量。

**Bordered Block Diagonal (BBD) 形式**：

ParaEMT（Xiong et al. 2024）将网络导纳矩阵重组为 BBD 形式：

$$
\mathbf{G} =
\begin{bmatrix}
\mathbf{B}_1 & \mathbf{E}_1 & & \\
\mathbf{E}_1^\top & \mathbf{D}_1 & \mathbf{E}_2 & \\
& \mathbf{E}_2^\top & \mathbf{B}_2 & \mathbf{E}_3 \\
& & \mathbf{E}_3^\top & \mathbf{B}_n
\end{bmatrix}
$$

其中 $\mathbf{B}_i$ 为块对角主矩阵（可并行求解），$\mathbf{D}_i$ 为边界对角矩阵，$\mathbf{E}_i$ 为边界耦合项。BBD 分解使网络求解可完全并行化，边界耦合通过 Schur 补或迭代法处理。

### 3. 任务并行（Task Parallelism）

任务并行将每个仿真案例作为独立任务运行，通信少、可扩展性通常更好。适合离线统计分析（参数扫描、蒙特卡洛），但不能替代单个闭环 EMT 场景的实时性证明。

**FMI 协同仿真架构**：

Ouafi 等（2023）基于 Functional Mock-up Interface (FMI) 标准实现了多实例 EMT 协同仿真：

$$
\text{Master Device} \leftrightarrow \text{Master Link} \leftrightarrow \text{Buffer}_1/\text{Buffer}_2 \leftrightarrow \text{Slave Link} \leftrightarrow \text{Slave Device}
$$

采用双缓冲（Double-Buffer）方案保证数据完整性，通过信号量（semaphore）实现低层同步。每个 EMT 实例在独立核心上运行子网络，通过解耦传输线交换历史电流信息。

### 4. 混合并行（Hybrid Parallelism）

陈来军等（2010）提出**元件级并行 + 网络级并行**的混合架构：

- **元件级并行**：将计算量大的多相电机分拆为多个互相耦合的小电机，降低单个元件计算量
- **网络级并行**：利用元件级并行实现系统切分方案的优化设计

在典型综合电力系统（12 相发电机 + 15 相电动机）中，传统 MATE 算法分区方案 1（2 区）加速比仅 2.0，方案 2（9 区）加速比仅 2.5。引入元件级并行后，系统可更灵活切分，协调侧计算规模显著降低。

**混合并行计算流**：

$$
T_{\text{total}} = \max_i(T_i^{\text{compute}}) + T_{\text{coord}} + T_{\text{sync}}
$$

其中 $T_i^{\text{compute}}$ 为各子分区计算时间，$T_{\text{coord}}$ 为协调侧计算时间，$T_{\text{sync}}$ 为同步等待时间。优化目标是同时降低 $\max_i(T_i^{\text{compute}})$ 和 $T_{\text{coord}}$。

## 可扩展性评估

### 强扩展（Strong Scaling）

固定问题规模，增加处理器数：

$$
S_p = \frac{T_1}{T_p}, \quad E_p = \frac{S_p}{p}
$$

其中 $S_p$ 为加速比，$E_p$ 为效率。EMT 报告应明确：

- 问题规模（节点数、支路数、元件类型、开关事件）
- 是否计入矩阵组装、通信、I/O、检查点和后处理
- 分区方法、进程映射和网络环境
- 误差指标和基线求解器

### 弱扩展（Weak Scaling）

保持每处理器工作量近似不变，观察总时间是否稳定。

### Karp-Flatt 度量

Le-Huy 等（2023）引入 Karp-Flatt 度量评估并行质量：

$$
\sigma(n) = \frac{1}{S_n} - \frac{1}{n}
$$

其中 $\sigma(n)$ 为串行比例估计。实际测量中需考虑单处理器额外开销：

$$
T'(n, 1) = \sigma(n) + \phi(n) + \kappa'(n, 1)
$$

其中 $\phi(n)$ 为并行额外开销，$\kappa'(n, 1)$ 为单处理器上的额外串行开销。若 $\kappa'(n, 1)$ 不可忽略，将导致人为偏高的加速比甚至超线性加速。

## 通信基础设施评估

Le-Huy 等（2023）在 Hydro-Québec 离线 EMT 仿真中系统评估了四种通信Fabric对 MPI 并行性能的影响：

| 通信 Fabric | 类型 | 架构特点 | EMT 适用性 |
|------------|------|----------|-----------|
| SGI NUMAlink 7 | 单系统镜像 | 多主板共享内存，全局一致 | 高（低延迟） |
| HPE Flex Grid Interconnect | 单系统镜像 | 分布式资源统一编址 | 高 |
| Mellanox InfiniBand QDR | 集群 | 独立 OS，本地资源 | 中（需 MPI 优化） |
| Mellanox InfiniBand HDR | 集群 | 100 Gb/s 带宽 | 高（高吞吐） |

关键发现：通信 Fabric 的选择对**每步仿真时间**有显著影响。单系统镜像架构（NUMAlink、FGI）因共享内存一致性避免了显式消息传递，在 EMT 这种通信密集型应用中表现更优。集群架构（InfiniBand）需要更精细的 MPI 通信模式优化才能达到同等性能。

## 硬件加速与异构计算

### CPU-GPU 异构架构

Lin 等（2023）在 IEEE 118 总线系统（集成大量分布式电池）中实现了 CPU-GPU 异构计算：

- **CPU 端**：系统级机电暂态稳定（TS）仿真
- **GPU 端**：设备级 EMT 仿真，利用多流（multi-streaming）和多线程（multithreading）能力实现异步顺序并行处理

 achieves **200+ 倍加速**，实现了 EMT-TS 协同仿真的可行性。

### 机器学习增强并行

Cheng 等（2025）提出了**数据驱动 + 实体-组件-系统（ECS）架构**的机器学习增强并行方法：

- 使用门控循环单元（GRU）神经网络替代传统物理 EMT 模型
- 基于 ECS 架构将 200 万个 RES 实体分组到微电网
- 在 CPU-GPU 上实现**400 倍加速**，相比传统 CPU 非线性迭代计算

$$
\text{Speedup} = \frac{T_{\text{CPU-NR}}}{T_{\text{ANN-GPU}}} \approx 400
$$

其中 $T_{\text{CPU-NR}}$ 为 CPU 上 Newton-Raphson 迭代时间，$T_{\text{ANN-GPU}}$ 为 GPU 上 ANN 推理时间。

### 多速率并行

Debnath 等（2023）提出了解耦详细等效模型用于并行和多速率 EMT 仿真：

- MMC-BESS 系统采用多速率策略：电力电子部分使用小步长（1–5 μs），电网部分使用大步长（50–100 μs）
- 通过解耦接口实现不同速率子网间的信息交换
- 在保持精度的同时大幅降低计算负担

## 任务分配与图划分

Brunner 等（2020）研究了实时 EMT 仿真中的任务分配问题，将其表述为**任务分配问题（Task Allocation Problem, TAP）**：

**两步并行化流程**：

1. **任务分离**：利用传输线传播延迟或图划分算法将网络切分为多个任务
2. **任务映射**：将各任务映射到模拟器处理器

$$
\min \sum_{i,j} C_{ij} \cdot X_{ij} \quad \text{s.t.} \quad \sum_j X_{ij} = 1, \quad \sum_i X_{ij} \leq 1
$$

其中 $C_{ij}$ 为任务 $i$ 映射到处理器 $j$ 的代价（含通信开销），$X_{ij}$ 为二元决策变量。

**两种分离技术**：

- **传输线解耦**：利用分布参数传输线的自然传播延迟（大于仿真步长）实现无近似切分
- **图划分算法**：使用 Metis 等启发式算法自动并行化，通过超参数调优提升实时性能

验证表明：图划分算法在 RTE（法国输电运营商）的大规模工业算例中表现优异，Hyper parameter 调优可进一步提升实时性能。

## 稀疏矩阵求解器并行

Abusalah 等（2018）在 EMTP 中实现了基于 KLU 稀疏矩阵求解器的并行化：

- 通过自动检测传输线/电缆模型中的自然解耦子矩阵，并行求解
- 应用于全迭代求解器（Newton 方法处理所有非线性模型）
- 在 Hydro-Québec 大规模电网基准上验证

Bruned 等（2023）进一步将稀疏求解器应用于并行实时 EMT 仿真：

- KLU 求解器的部分重构（partial refactorization）技术减少重复计算
- 在实时 HIL 场景中验证了数值稳定性

## 量化性能边界

| 论文 | 系统规模 | 方法 | 加速比 | 验证平台 |
|------|---------|------|--------|---------|
| Xiong et al. 2024 (ParaEMT) | 10,080 母线 / 30,240 节点 | BBD 分解 + MPI | 25–36x | NREL Eagle HPC |
| Xiong et al. 2024 (ParaEMT) | 240 母线 / 720 节点 | BBD 分解 | 1x (基准) | PSCAD 对标验证 |
| Zhou & Dinavahi 2014 | 2,458 三相母线 | MT-EMTP GPU | 5.63x | EMTP-RV 对标 |
| Lin et al. 2023 | IEEE 118 + BESS | CPU-GPU 异构 | 200+x | MATLAB/Simulink |
| Cheng et al. 2025 | 200 万 RES 实体 | ANN-GPU ECS | 400x | MATLAB/Simulink |
| Xu et al. 2025 | 100 MW 光伏电站 | OpenMP 多线程 | 80x (串行) + 2–3x (并行) | 实验平台 |
| Chen et al. 2010 | 12 相发电机 + 15 相电机 | 混合并行 | >2.5x | 综合电力系统 |
| Le-Huy et al. 2023 | Hydro-Québec 系统 | MPI 集群 | 取决于 Fabric | IREQ 仿真平台 |

## 关键技术挑战

### 1. 强耦合网络分区

电力电子密集型网络中，子域间耦合强烈（$\mathbf{Y}_{12}$、$\mathbf{Y}_{21}$ 非稀疏），导致通信频率高、接口迭代收敛困难。补偿法（compensation method）和状态空间节点分析（state-space nodal analysis）可在无传输线场景下实现任意位置切分，但需要求解器代码修改。

### 2. 负载均衡

不同子网计算量差异导致线程/进程空闲等待。动态负载平衡策略（如工作窃取、自适应分区）在时变网络拓扑中尤为重要。

### 3. I/O 瓶颈

长时间仿真中，数据记录和检查点 I/O 可能主导总仿真时间。并行文件系统（Lustre、GPFS）和异步 I/O 策略是必要的。

### 4. 可复现性

集群运行结果需要版本、模型、平台和随机种子的完整可追溯性。目前缺乏包含通信、I/O、检查点和误差指标的 EMT HPC 统一基准。

## 适用边界与选择指南

### 方法选择指南

| 应用场景 | 推荐方法 | 原因 |
|---------|---------|------|
| 数千母线以上大规模系统 | BBD 分解 + MPI 分布式并行 | ParaEMT 验证 25–36x 加速 |
| 多 VSC / 光伏电站 | 低维等效 + OpenMP 多线程 | 串行 80x + 并行 2–3x |
| 批量参数扫描 / 蒙特卡洛 | 任务并行 | 通信少、可扩展性好 |
| 实时 HIL | 图划分 + 高效任务映射 | 保证最坏步长约束 |
| 大规模 BESS / RES | CPU-GPU 异构 + 多速率 | 200–400x 加速 |
| 无传输线网络 | 补偿法 / 状态空间节点分析 | 不依赖 TLM 自然解耦 |
| 超大规模 (10万+ 节点) | 机器学习替代 + GPU ECS | 400x 加速，突破非线性迭代瓶颈 |

### 失败模式

- 强耦合网络分区会导致频繁通信或接口迭代
- 固定小模型在过多节点上运行会因通信开销降低效率
- I/O 和数据记录可能主导长时间仿真
- 云或共享集群的网络抖动通常不适合未经验证的硬实时 HIL
- 只报告总加速比而不说明基线、进程数、问题规模和通信占比，证据不足

## 并行仿真平台现状

### 国内外 EMT 平台并行策略

| 平台 | 并行方式 | 特点 |
|------|---------|------|
| ParaEMT (Xiong et al. 2024) | MPI + BBD | 开源 Python，HPC 兼容，NREL Eagle 验证 |
| EMTP® (Ouafi et al. 2023) | FMI + 多实例 | DLL 接口无需修改源码，支持多速率 |
| HYPERSIM (Bruned et al. 2020) | 图划分 + 自动并行 | RTE 工业验证，支持 HIL |
| MT-EMTP (Zhou & Dinavahi 2014) | GPU 多线程 | 2458 三相母线验证 |
| PSCAD (Zhang et al. 2024) | GPU + 频移分析 |  faster-than-real-time |
| DSATools / TSAT | 机电暂态 | 系统级稳定性评估 |

### 算法-硬件深度融合趋势

江艺宝等（2024）综述指出，新型电力系统对 EMT 并行仿真提出三个新需求：

1. **更高的仿真维度**：节点数目急剧增加，网络方程维数骤增
2. **更高的仿真精度**：设备级详细模型替代聚合等值模型
3. **更高的仿真速度**：批量仿真和实时 HIL 的双重压力

未来发展方向是**算法-硬件深度融合的仿真平台**——并行算法与 CPU/GPU/FPGA 硬件架构协同设计，而非简单的算法移植。

## 开放问题

1. 如何建立包含通信、I/O、检查点和误差指标的 EMT HPC 统一基准
2. 如何在强耦合电力电子网络中设计稳定的分区接口
3. 如何让集群运行结果具备版本、模型、平台和随机种子的完整可追溯性
4. 如何在机器学习替代模型与传统物理模型之间平衡精度与效率
5. 如何实现自适应多速率策略的自动化选择

## 相关方法

- [[computational-acceleration]]：总览加速策略
- [[sparse-matrix-techniques]]：提供局部矩阵求解基础
- [[heterogeneous-computing]]：讨论 HPC 节点内 CPU/GPU/FPGA 协同
- [[gpu-parallel-acceleration]]：讨论单 GPU 或多 GPU 内核层加速
- [[hardware-acceleration]]：讨论专用硬件能力和边界
- [[network-partitioning]]：支撑空间并行的分区机制
- [[interface-technique]]：并行子域间接口交换方法
- [[multithreaded-parallel-computing]]：多线程并行实现细节
- [[real-time-simulation]]：实时仿真约束与 HPC 的关系
- [[hil-simulation]]：硬件在环仿真中的 HPC 应用
- [[large-scale-system-simulation]]：大规模 EMT 仿真主题背景
- [[parallel-in-time]]：时间并行化方法

## 来源论文

1. **Xiong et al. 2024 (ParaEMT)** — 开源 Python HPC 兼容 EMT 仿真器，BBD 矩阵分解，10080 母线系统 25–36x 加速验证
2. **Jiang et al. 2024** — 新型电力系统 EMT 并行仿真关键技术综述，分网并行/多速率/硬件加速/仿真平台四大方向系统梳理
3. **Abusalah et al. 2018** — CPU 共享内存并行稀疏求解器（KLU），基于传输线自然解耦，Hydro-Québec 大规模电网验证
4. **Lin et al. 2023** — CPU-GPU 异构计算用于大规模 BESS EMT-TS 协同仿真，IEEE 118 系统 200+ 倍加速
5. **Cheng et al. 2025** — 机器学习增强（GRU-ANN）+ ECS 架构的 GPU 并行仿真，200 万 RES 实体 400x 加速
6. **Xu et al. 2025** — 低维等效模型 + OpenMP 多线程并行，100 MW 光伏电站串行 80x + 并行 2–3x 加速
7. **Ouafi et al. 2023** — FMI 标准多实例协同仿真，双缓冲通信，自动并行化，支持多速率
8. **Le-Huy et al. 2023** — MPI 通信 Fabric 评估（NUMAlink/FGI/InfiniBand），Karp-Flatt 并行质量度量
9. **Bruned et al. 2020** — 图划分算法用于实时 EMT 任务分配，RTE 工业验证，Hyper parameter 调优
10. **Chen et al. 2010** — 元件级 + 网络级混合并行算法，多相电机分解，综合电力系统验证
