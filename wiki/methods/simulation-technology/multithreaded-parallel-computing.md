---
title: "多线程并行计算 (Multithreaded Parallel Computing)"
type: method
tags: [multithreading, openmp, parallel, cpu, shared-memory]
created: "2026-05-02"
---

# 多线程并行计算 (Multithreaded Parallel Computing)


```mermaid
graph TD
    subgraph Ncmp[多线程并行计算 (Multithreaded Paral…]
        N0[元件级: 每个线程处理一组元件更新]
        N1[子网级: 分区后子网并行求解，接口迭代或补偿]
        N2[场景级: 多个 EMT 工况并行运行]
        N3[线性代数级: 并行 SpMV、三角求解、因子分解]
        N4[控制器级: 多设备控制计算并行]
    end
```


## 定义与边界

多线程并行计算是在共享内存 CPU 上把 EMT 仿真任务划分给多个线程执行的方法。它关注线程级任务划分、同步、缓存局部性和负载均衡，属于[[computational-acceleration]]的一类实现路线。

本页不把“多线程”直接等同于“实时”或“线性加速”。实际收益取决于网络分区、矩阵结构、开关事件、串行比例、内存带宽和线程调度开销。

## EMT 中的作用

固定步长 EMT 每个时间步通常包含元件更新、网络矩阵组装、线性方程求解、控制器计算、开关事件处理和输出记录。多线程可用于：

- 并行更新大量相似元件、负荷、线路段或换流器子模块。
- 并行组装稀疏矩阵或右端项。
- 对[[network-partitioning]]后的子网并行求解。
- 批量运行参数扫描、故障集或 Monte Carlo 工况。
- 加速不适合 GPU 的中等规模 CPU 工作负载。

它与[[gpu-parallel-acceleration]]、[[high-performance-computing]]和[[heterogeneous-computing]]的区别在于：多线程共享同一进程地址空间，通信成本低但更容易受内存带宽、锁竞争和 NUMA 影响。

## 并行模型

对时间步 $k$，串行 EMT 流程可写为

$$
\mathbf{Y}_k\mathbf{v}_k=\mathbf{i}_k,\quad
\mathbf{x}_{k+1}=\Phi(\mathbf{x}_k,\mathbf{v}_k,\mathbf{u}_k).
$$

多线程化通常不改变数学模型，而改变 $\mathbf{Y}_k$、$\mathbf{i}_k$ 和 $\Phi$ 的计算组织。可并行部分的收益受 Amdahl 型关系限制：

$$
S(N)=\frac{T_1}{T_N},
$$

其中 $T_N$ 必须是端到端时间，包含同步、调度、矩阵重组和 I/O。若只报告某个内核时间，不能推导完整 EMT 仿真加速比。

## 工作流

1. 建立单线程基线：固定步长、容差、事件处理和输出。
2. 识别热点：区分元件更新、矩阵组装、求解器、控制器和日志 I/O 的耗时。
3. 选择粒度：按元件、子网、端口、场景或时间块划分任务。
4. 处理共享写入：采用局部缓冲、图着色、归约或原子操作。
5. 控制同步：减少 barrier、锁和频繁小任务。
6. 验证一致性：比较波形、残差、事件时间和非确定性差异。
7. 报告性能：给出硬件、线程数、绑定策略、问题规模和端到端时间。

## 并行粒度

| 粒度 | 机制 | 适用场景 | 风险 |
|---|---|---|---|
| 元件级 | 每个线程处理一组元件更新 | 大量独立 RLC、负荷、子模块 | 写入节点矩阵时冲突 |
| 子网级 | 分区后子网并行求解，接口迭代或补偿 | 大规模网络、弱耦合区域 | 接口迭代和延迟影响精度 |
| 场景级 | 多个 EMT 工况并行运行 | 参数扫描、故障集、校准采样 | 单个工况不加速 |
| 线性代数级 | 并行 SpMV、三角求解、因子分解 | 稀疏矩阵求解 | 内存访问和依赖限制强 |
| 控制器级 | 多设备控制计算并行 | 多换流器、多风机 | 事件同步和共享测量需谨慎 |

## 共享内存实现要点

- OpenMP 适合循环和任务并行，但应显式说明调度策略和数据作用域。
- Pthreads 或 C++ 线程适合自定义队列和长生命周期工作线程。
- NUMA 系统应注意 first-touch、线程绑定和跨节点内存访问。
- 稀疏矩阵组装应避免多个线程写同一非零元；先局部累加再合并通常更可控。
- 可重复性需要固定归约顺序或接受浮点舍入导致的小差异，并在验证中说明。

## 与数值求解的关系

多线程并行不会自动改善数值稳定性。对[[sparse-matrix-techniques]]和[[network-partitioning]]而言，性能变化常来自：

- 符号分解和重排序是否可复用。
- 分区接口变量是否引入额外迭代。
- 线程并行是否改变事件处理顺序。
- 直接法、迭代法和预处理器是否适合共享内存并行。

因此，性能报告应与波形误差、KCL 残差、收敛日志和事件时间共同出现。

## 适用边界与失败模式

- 小系统或串行求解器占主导时，多线程开销可能超过收益。
- 内存带宽饱和后增加线程数可能几乎不再加速。
- 负载不均会让少数复杂子网或换流器成为尾部瓶颈。
- 锁、原子操作和频繁 barrier 会抵消理论并行度。
- 非确定性调度可能改变浮点归约顺序，影响边界工况下的事件触发。
- 只给“CPU 核数”和“加速比”而不报告问题规模、线程绑定和端到端时间，证据不足。

## 代表性证据

- [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri]] 可作为 CPU 并行 EMT 的具体来源；其加速结论应绑定原文网络规模、硬件和算法。
- [[an-open-source-parallel-emt-simulation-framework]] 支撑开源并行 EMT 框架的实现案例；不能据此推断所有模型均可并行。
- [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized]] 支撑模块化换流器或解耦框架中的并行化路线；精度依赖解耦假设和验证工况。
- [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn]] 支撑并行仿真性能需要考虑通信或同步开销；属于具体平台证据。

## 与相关页面的关系

- [[computational-acceleration]]：多线程是 EMT 加速策略之一。
- [[sparse-matrix-techniques]]：提供并行矩阵组装和求解的数据结构背景。
- [[network-partitioning]]：改变多线程任务粒度和接口耦合。
- [[multirate-and-network-partitioning]]：把时间步差异和分区并行结合。
- [[gpu-parallel-acceleration]]：对比共享内存 CPU 与 GPU 数据并行。
- [[high-performance-computing]]：讨论多节点或集群级扩展。
- [[real-time-simulation]]：定义实时仿真需要满足的最坏时延和抖动证据。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[low-dimensional-equivalent-models-and-multithreading-based-parallel-emt-simulati|Low-Dimensional Equivalent Models and Multithreading-Based P]] | 2025 |
