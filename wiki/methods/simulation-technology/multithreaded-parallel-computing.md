---
title: "多线程并行计算 (Multithreaded Parallel Computing)"
type: method
tags: [multithreading, openmp, parallel, cpu, shared-memory, cpu-parallel, omp]
created: "2026-05-02"
updated: "2026-05-15"
---

# 多线程并行计算 (Multithreaded Parallel Computing)

## 定义

多线程并行计算（Multithreaded Parallel Computing）是在共享内存多核CPU上，将电磁暂态（EMT）仿真任务划分为多个线程并行执行的计算方法。它属于[[computational-acceleration]]的核心实现路线之一，与[[gpu-parallel-acceleration]]（数据并行）、[[heterogeneous-computing]]（CPU-FPGA/CPU-GPU协同）和[[high-performance-computing]]（多节点集群）共同构成EMT仿真的加速体系。

多线程的核心特征是**共享地址空间**：所有线程访问同一进程的主存，线程间通信通过共享变量直接完成，无需网络复制或IPC机制。这使得线程创建/销毁开销低、同步延迟小，但也带来**锁竞争**、**内存带宽饱和**和**NUMA跨节点访问**等制约因素。

本页关注CPU共享内存多线程在EMT中的应用，涵盖线程级任务划分、稀疏矩阵并行求解、网络分区接口并行化和多换流器并行更新等典型场景。

## EMT 中的角色

固定步长EMT每时间步的计算流程通常包含：

1. **元件更新**：R/L/C、开关、换流器子模块、电力电子器件的状态更新
2. **矩阵组装**：节点导纳矩阵 $\mathbf{Y}_k$ 和右端项 $\mathbf{i}_k$ 的稀疏化组装
3. **线性方程求解**：$\mathbf{Y}_k\mathbf{v}_k = \mathbf{i}_k$ 的稀疏矩阵求解
4. **控制器计算**：PI控制、PWM调制、PLL、VSG等控制算法的时域执行
5. **开关事件处理**：开关状态判断、拓扑变化重构
6. **输出记录**：波形存储、日志I/O

多线程并行可在以上各环节发挥作用：
- **元件级并行**：大量相似RLC支路、换流器子模块、风机/光伏逆变器单元的并行更新
- **矩阵组装并行**：稀疏矩阵各非零元的并行填充（需避免写冲突）
- **线性代数并行**：并行SpMV（稀疏矩阵-向量乘）、三角求解、LU分解（BTF/稀疏直接法）
- **网络分区并行**：基于[[network-partitioning]]的子网并行求解，接口通过迭代或补偿法同步
- **场景级并行**：参数扫描、故障集、Monte Carlo工况的批量并行运行

多线程不适合的场景包括：小规模系统（线程创建开销超过计算收益）、内存带宽饱和后继续增核、无结构化稀疏性的密集矩阵求解、以及需要严格确定性回放的仿真验证。

## 核心机制

### 数学框架

对时间步 $k$，串行EMT流程可写作：

$$
\mathbf{Y}_k \mathbf{v}_k = \mathbf{i}_k, \quad \mathbf{x}_{k+1} = \Phi(\mathbf{x}_k, \mathbf{v}_k, \mathbf{u}_k)
$$

其中 $\mathbf{Y}_k$ 为节点导纳矩阵，$\mathbf{v}_k$ 为节点电压向量，$\mathbf{i}_k$ 为等效电流注入，$\mathbf{x}_k$ 为状态变量，$\Phi$ 为元件状态更新算子。多线程化不改变数学模型，只改变 $\mathbf{Y}_k$、$\mathbf{i}_k$ 和 $\Phi$ 的**计算组织方式**。

并行收益受Amdahl定律约束：

$$
S(N) = \frac{T_1}{T_N} \leq \frac{1}{f_s + \frac{f_p}{N}}
$$

其中 $f_s$ 为串行部分比例，$f_p = 1 - f_s$ 为可并行部分比例，$N$ 为线程数。$T_N$ 必须是端到端时间（含同步、调度、矩阵重组和I/O），而非单个内核时间。

### 线程级任务划分

**粒度层级**决定线程划分策略：

| 粒度 | 划分方式 | 适用场景 | 并行潜力 | 风险 |
|------|----------|----------|----------|------|
| 元件级 | 每线程处理一组独立RLC/子模块/逆变器 | 大量相似元件、大规模风电场/光伏电站 | 高（无数据依赖） | 写入节点矩阵时写冲突 |
| 子网级 | 分区后各子网并行求解，接口迭代/补偿同步 | 大规模网络、多换流器系统 | 中（受接口同步限制） | 接口延迟影响精度 |
| 场景级 | 多个EMT工况并行（参数扫描/故障集） | 参数优化、可靠性分析、Monte Carlo | 高（完全独立） | 单个工况内部未加速 |
| 线性代数级 | 并行SpMV、三角求解、BTF块并行 | 稀疏矩阵求解（BTF/稀疏直接法） | 中（受数据依赖限制） | 内存带宽饱和 |
| 控制器级 | 多设备控制算法并行（PI/PWM/PLL/VSG） | 多换流器协调控制、风电场群控 | 中（受测量同步限制） | 共享测量需原子操作 |

### 边界块三角形式（BTF）与稀疏并行

BTF（Bordered Block Triangular）形式是EMT网络矩阵并行求解的核心数据结构。通过识别输电线路/电缆引入的**自然延迟解耦**，将大矩阵分解为对角块和边界块：

$$
\begin{bmatrix}
\mathbf{B}_1 & 0 & \cdots & 0 & \mathbf{G}_1 \\
0 & \mathbf{B}_2 & \cdots & 0 & \mathbf{G}_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & \mathbf{B}_n & \mathbf{G}_n \\
\mathbf{H}_1^T & \mathbf{H}_2^T & \cdots & \mathbf{H}_n^T & \mathbf{C}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}_1 \\ \mathbf{v}_2 \\ \vdots \\ \mathbf{v}_n \\ \mathbf{v}_b
\end{bmatrix} = 
\begin{bmatrix}
\mathbf{i}_1 \\ \mathbf{i}_2 \\ \vdots \\ \mathbf{i}_n \\ \mathbf{i}_b
\end{bmatrix}
$$

各对角块 $\mathbf{B}_i$ 可独立并行求解，边界部分 $\mathbf{v}_b$ 联立求解后将结果注入各块。Abusalah 2018在Hydro-Québec L-Network（41797×41797矩阵，181个BTF块，最大块13584×13584）中实测：4线程加速到1176s（1线程1630s），但超过6线程后因开销增加反而减速（6线程1225s，12线程1263s）。

### 设备级解耦与诺顿等效并行

对于多换流器系统（如风电场、光伏电站），可先对各设备做端口等效，将内部节点消去，再对外部端口并行更新。典型流程：

1. **端口等效**：将DFIG/VSC/光伏逆变器等设备用诺顿等效表示为 $\mathbf{i}_{eq} = \mathbf{G}_{eq}\mathbf{v}_{port} + \mathbf{i}_{hist}$
2. **历史电流源并行更新**：各线程独立计算历史源，不相互依赖
3. **端口电压并行求解**：修正节点方程维度降低后，各子块并行求解
4. **内部状态恢复**：各线程独立更新内部状态（如dq轴电流、电容电压）

Xu 2025在100 MW光伏电站（含多VSC并联）中实测：解耦低维化带来**80倍以上串行加速**（相对详细模型），多线程并行额外获得**2-3倍加速**，误差"几乎不牺牲精度"。

### 多速率与多线程结合

[[multirate-and-network-partitioning]]将时间步长差异和分区并行结合：慢速元件（同步机、变压器）用大步长，快速元件（换流器子模块、电力电子开关）用小步长。多线程可在慢速区域和快速区域内各自并行，但需要接口变量在同一物理时刻的一致性插值。

## 量化性能边界

### CPU多线程加速经验数据

| 来源 | 系统规模 | 矩阵维度 | 线程数 | 加速比 | 验证条件 |
|------|----------|----------|--------|--------|----------|
| Abusalah 2018（L-Network）| Hydro-Québec 735kV系统 | 41797×41797 | 1→4 | 1.0→1.39 | 50μs步长，1s仿真，故障工况 |
| Abusalah 2018（L-Network）| Hydro-Québec 735kV系统 | 41797×41797 | 1→6 | 1.0→1.33 | 同上，6线程后减速 |
| Abusalah 2018（L'-Network）| Hydro-Québec 735kV降阶 | 3402×3402，169块 | 1→8 | 1.0→2.01 | 169个BTF块，最大块13584×13584 |
| Abusalah 2018（L'-Network）| Hydro-Québec 735kV降阶 | 3402×3402 | 1→12 | 1.0→2.17 | 12线程后收益趋于平缓 |
| Xu 2025（串行部分）| 100 MW光伏电站，多VSC | 未报告 | 1→串行 | >80× | 相对详细开关模型，误差未量化 |
| Xu 2025（并行部分）| 100 MW光伏电站，多VSC | 未报告 | 多线程 | 2-3× | OpenMP，误差"几乎不牺牲" |
| Feng 2023 | CHB-PET，48单相模块 | 未报告 | 多线程 | >10000× | 相对详细模型，最大误差<3% |
| DFIG风电场（细粒度划分）| 50台DFIG | 子系统≤18维 | OpenMP | ~100× | 5μs步长，最大相对误差1.68% |
| Xiong 2024（ParaEMT）| 10080节点（30240母线）| 未报告 | HPC多核 | 25-36× | 相对PSCAD，IEEE WECC 240母线验证 |

### 性能边界与失效模式

- **加速比上限**：受Amdahl定律中串行比例 $f_s$ 限制。若EMT流程中20%为串行（网络方程求解接口、开关事件处理），则8线程理论上限为 $1/(0.2+0.8/8) = 3.2\times$
- **线程数与收益曲线**：Abusalah 2018显示L-Network在4线程处达到最优（1.39×），之后因BTF块边界同步开销和内存带宽饱和而下降；L'-Network因问题规模小、块数多（169块），收益随线程数持续增加到12线程（2.17×）
- **内存带宽饱和**：当矩阵规模大、BTF块较小时，多线程同时访问主存导致内存带宽成为瓶颈，继续增核几乎无收益
- **NUMA效应**：在多插槽服务器上，线程跨NUMA节点访问远端内存延迟增加3-5倍，应使用first-touch策略和线程绑定

## 关键技术挑战

### 稀疏矩阵写冲突

稀疏矩阵组装时，多个线程可能同时写入同一非零元位置（如相邻节点共享的互导纳）。解决方案包括：

- **局部累加-合并**：各线程先写入线程本地缓冲，最后合并到全局矩阵
- **图着色**：为非零元分配颜色，同色非零元可并行写入
- **原子操作**：OpenMP `atomic` 或 `critical` 保护关键写操作（开销较高）
- **预标记结构**：事先分配好矩阵非零元Pattern，组装时直接写入索引位置

### 锁竞争与同步开销

OpenMP的barrier、锁和原子操作会引入同步开销。当并行粒度较细（每次迭代计算量小）时，同步开销可能超过并行收益。应对策略：

- **粗粒度并行**：增大每线程工作量（如批量处理多个子模块而非单个）
- **延迟同步**：使用生产者-消费者模式，只在必要时同步
- **无锁设计**：通过线程本地累加替代原子加法

### 数值一致性与浮点误差

浮点归约顺序不确定可能导致结果在边界工况下存在微小差异。这在工程验收中需要明确约定：

- **固定归约顺序**：使用 `@reduction(order: ...)` 或手动显式循环
- **接受微小差异**：规定KCL残差容差而非逐点波形比较
- **确定性调度**：通过 `OMP_PROC_BIND=spread` 和固定线程亲和性消除调度不确定性

### 负载均衡

各线程工作量可能不均，导致部分线程成为瓶颈：

- **动态调度** `schedule(dynamic, chunk_size)`：自动将任务分发到空闲线程
- **工作窃取**（Work-stealing）：Pthreads自定义线程池实现
- **静态分析**：对BTF块按规模排序后分配，保证各线程处理总工作量接近

## 适用边界与选择指南

| 场景 | 推荐并行方式 | 预期收益 | 备注 |
|------|-------------|----------|------|
| 大规模风电场/光伏电站（多换流器并联） | 设备级解耦+诺顿等效+OpenMP | 80-100×（串行）+ 2-3×（并行） | 适用于多VSC独立直流侧和并联直流侧两种拓扑 |
| 大型交流网络（10000+节点） | BTF分块+稀疏直接法+OpenMP | 2-5× | 需线路/电缆自然解耦，6-12线程内收益最佳 |
| 参数扫描/Monte Carlo | 场景级多进程（MPI或进程池） | 与工况数成正比 | 单工况内部未加速，但完全独立无同步开销 |
| CHB-PET等模块化功率电子系统 | 导纳预存+诺顿等效+多线程 | 10000×+ | 48模块CHB-PET详细模型案例，H桥导纳二值化是关键 |
| 实时仿真平台 | 多核CPU+专用线程绑定 | 受实时时延约束 | 需保证最坏情况执行时间，OpenMP动态调度不适合 |
| GPU不适用的中等规模问题 | CPU多线程+SIMD向量化 | 2-10× | 内存带宽敏感问题，BTF块较小时优先CPU多线程 |

**不适用场景**：
- 小规模系统（<1000节点）：线程创建开销超过收益
- 密集矩阵求解：无稀疏性，内存访问模式不友好
- 需要严格确定性回放：浮点归约顺序不确定

## 相关方法

- [[computational-acceleration]]：多线程是EMT加速策略四大方向（算法/数据结构/并行/硬件）之一
- [[sparse-matrix-techniques]]：提供并行矩阵组装和求解的数据结构基础（KLU/BTF格式）
- [[network-partitioning]]：改变多线程任务粒度和接口耦合方式
- [[multirate-and-network-partitioning]]：将时间步长差异和分区并行结合
- [[gpu-parallel-acceleration]]：对比共享内存CPU多线程与GPU数据并行的适用场景
- [[heterogeneous-computing]]：讨论CPU-FPGA/CPU-GPU协同在EMT中的并行架构
- [[high-performance-computing]]：扩展到多节点集群级并行（HPC）

## 来源论文

| 论文 | 年份 | 主要贡献 |
|------|------|----------|
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie]] | 2023 | CHB-PET导纳预存+诺顿等效，多线程并行>10000×加速 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin]] | 2023 | 海上风电场多线程并行+风机等值建模 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f]] | 2024 | DFIG风电场细粒度网络划分+OpenMP，50台风机~100×加速（误差1.68%） |
| [[low-dimensional-equivalent-models-and-multithreading-based-parallel-emt-simulati]] | 2025 | 多VSC半隐式混合积分解耦+低维等效，80×串行+2-3×并行，100 MW光伏 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri]] | 2018 | KLU稀疏矩阵BTF并行，Hydro-Québec L-Network 41797维，1-12线程性能曲线 |
| [[an-open-source-parallel-emt-simulation-framework]] | 2024 | ParaEMT开源框架，Python+BTF+并行状态更新，10080节点25-36×加速 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources]] | 2023 | FMI接口co-simulation，多实例并行，传输线延迟自然解耦+多速率 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation]] | 2024 | 新型电力系统EMT并行仿真综述，四层分类体系（分网并行/多速率/硬件加速/平台） |