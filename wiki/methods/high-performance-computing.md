---
title: "高性能计算 (High Performance Computing)"
type: method
tags: [hpc, high-performance-computing, parallel, cluster, supercomputing]
created: "2026-05-02"
---

# 高性能计算 (High Performance Computing)

## 定义与边界

高性能计算是利用多核处理器、共享内存服务器、分布式集群、并行文件系统和作业调度环境来执行大规模 EMT 仿真或批量仿真的方法。它强调系统级并行、通信、调度和可扩展性，不等同于单卡 GPU 加速或单个硬件平台能力。

GPU 与 FPGA 属于可被 HPC 系统纳入的加速资源，分别见 [[gpu-parallel-acceleration]] 与 [[hardware-acceleration]]。多类资源协同见 [[heterogeneous-computing]]。

## EMT 中的作用

HPC 在 EMT 中主要服务三类目标：

- 大规模网络：通过 [[network-partitioning]]、稀疏求解和并行通信处理更大的系统。
- 批量吞吐：同时执行参数扫描、故障集、蒙特卡洛或控制参数整定。
- 工程运行：在集群上管理长仿真、检查点、日志、数据归档和可复现实验。

对实时 HIL，HPC 集群并不天然满足硬实时约束；必须证明最坏步长时间、网络通信时延和 I/O 抖动满足 [[real-time-simulation]] 与 [[hil-simulation]] 的要求。

## 并行模型

### 共享内存

共享内存并行通常使用线程、OpenMP 或任务运行时。它适合单节点内的元件更新、稀疏向量操作和部分组装任务。风险包括 NUMA 访问、锁竞争、伪共享和动态负载不均。相关方法见 [[multithreaded-parallel-computing]]。

### 分布式内存

分布式内存并行通常使用 MPI。每个进程持有子网络、局部矩阵和边界变量，通过消息传递交换接口量。典型子域形式为：

$$
\begin{bmatrix}
\mathbf{Y}_{11} & \mathbf{Y}_{12}\\
\mathbf{Y}_{21} & \mathbf{Y}_{22}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}_1\\
\mathbf{v}_2
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{i}_1\\
\mathbf{i}_2
\end{bmatrix}
$$

若接口项 $\mathbf{Y}_{12}$、$\mathbf{Y}_{21}$ 较强，通信和迭代收敛会限制扩展性。

### 任务并行

多场景任务并行将每个仿真案例作为独立任务运行，通信少、可扩展性通常更好。它适合离线统计分析，但不能替代单个闭环 EMT 场景的实时性证明。

## 可扩展性指标

强扩展固定问题规模并增加处理器数：

$$
S_p=\frac{T_1}{T_p}, \quad E_p=\frac{S_p}{p}
$$

弱扩展保持每个处理器的工作量近似不变，观察总时间是否稳定。EMT 报告应说明：

- 问题规模、节点数、支路数、元件类型和开关事件。
- 是否计入矩阵组装、通信、I/O、检查点和后处理。
- 使用的分区方法、进程映射和网络环境。
- 误差指标和基线求解器。

## 核心工作流

1. 对模型图进行分区，平衡计算量并减少边界耦合。
2. 为每个子域组装局部矩阵和历史源。
3. 通过接口方法交换边界电压、电流或等效源，见 [[interface-technique]]。
4. 并行推进步长，必要时做全局同步、收敛检查或事件广播。
5. 汇总输出并记录可复现实验元数据。

## 与稀疏矩阵和硬件的关系

HPC 的效率常由稀疏矩阵结构和通信模式共同决定。[[sparse-matrix-techniques]] 降低单进程求解成本，[[gpu-parallel-acceleration]] 或 FPGA 可加速局部子任务，但跨节点通信、负载均衡和数据归档仍属于 HPC 层问题。

## 适用边界与失败模式

- 强耦合网络分区会导致频繁通信或接口迭代。
- 固定小模型在过多节点上运行会因通信开销降低效率。
- I/O 和数据记录可能主导长时间仿真。
- 云或共享集群的网络抖动通常不适合未经验证的硬实时 HIL。
- 只报告总加速比而不说明基线、进程数、问题规模和通信占比，证据不足。

## 代表性证据

- [[large-scale-system-simulation]] 提供大规模 EMT 问题的主题背景。
- [[network-partitioning]] 和 [[interface-technique]] 支撑空间并行的机制说明。
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]] 可作为实时/HIL 场景中必须关注接口和时序证据的来源示例。

## 与相关页面的关系

- [[computational-acceleration]]：总览加速策略。
- [[sparse-matrix-techniques]]：提供局部矩阵求解基础。
- [[heterogeneous-computing]]：讨论 HPC 节点内的 CPU/GPU/FPGA 协同。
- [[gpu-parallel-acceleration]]：讨论单 GPU 或多 GPU 内核层。
- [[hardware-acceleration]]：讨论专用硬件能力和边界。

## 开放问题

- 如何建立包含通信、I/O、检查点和误差指标的 EMT HPC 基准。
- 如何在强耦合电力电子网络中设计稳定的分区接口。
- 如何让集群运行结果具备版本、模型、平台和随机种子的完整可追溯性。
