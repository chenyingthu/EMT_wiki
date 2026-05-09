---
title: "计算加速 (Computational Acceleration)"
type: method
tags: [acceleration, optimization, algorithm, parallel, efficiency]
created: "2026-05-02"
---

# 计算加速 (Computational Acceleration)


```mermaid
graph TD
    subgraph Ncmp[计算加速 (Computational Accelera…]
        N0[稀疏直接法优化: 结构稳定的网络方程]
        N1[迭代法与预处理: 大规模稀疏系统、可接受残差准则]
        N2[元件级并行: 大量相似元件或子模块]
        N3[网络分区: 弱耦合子网、大规模系统]
        N4[多速率: 时间尺度分离明显的系统]
        N5[批量任务并行: 参数扫描、蒙特卡洛、N-1 场景]
    end
```


## 定义与边界

计算加速是通过算法、数据结构、并行执行、模型等效和硬件部署来降低 EMT 仿真时间、提高吞吐量或满足固定步长时限的一组方法。它是总览页，不等同于 GPU、HPC 或硬件加速中的任一单项技术。

本页的边界是“如何判断和组织加速路线”。具体稀疏矩阵方法见 [[sparse-matrix-techniques]]，GPU 实现见 [[gpu-parallel-acceleration]]，硬件执行见 [[hardware-acceleration]]，集群扩展见 [[high-performance-computing]]，异构协同见 [[heterogeneous-computing]]。

## EMT 中的作用

EMT 仿真的计算成本通常来自：

- 元件伴随模型更新和历史源计算。
- 网络矩阵组装与开关状态处理。
- 线性或非线性方程求解。
- 多速率、接口、插值和输出记录。
- 多场景扫描、参数不确定性分析和 HIL 闭环接口。

加速方法必须保持目标物理量、时间步、事件时刻和数值稳定性可审核。只缩短运行时间而不说明误差和边界，不足以构成严谨方法页结论。

## 成本模型

单步成本可粗略分解为：

$$
T_{step}=T_{model}+T_{assemble}+T_{solve}+T_{event}+T_{io}
$$

若使用并行或硬件资源：

$$
T_{step}=T_{serial}+T_{parallel}/p+T_{comm}+T_{sync}+T_{transfer}
$$

该表达强调：加速比不仅受处理器数量影响，还受通信、同步、数据迁移和不可并行部分限制。对于 HIL，评价对象还包括最坏步长时间和抖动，而不只是平均耗时。

## 加速层次

### 算法层

算法层包括重排序、符号分解复用、局部网络更新、接口解耦、波形松弛、多速率积分和模型降阶。它通常比硬件替换更先被检查，因为算法结构决定可并行性和数据移动规模。相关页面包括 [[multirate-method]]、[[interface-technique]] 和 [[model-order-reduction]]。

### 数据结构层

数据结构层关注稀疏格式、块结构、缓存局部性、矩阵增量更新和历史源布局。该层与 [[sparse-matrix-techniques]] 直接相关。

### 并行层

并行层包括元件级并行、网络分区、任务并行和多场景并行。空间分区通常依赖 [[network-partitioning]]；共享内存多线程见 [[multithreaded-parallel-computing]]。

### 硬件层

硬件层包括 GPU、FPGA、DSP 和专用实时仿真设备。硬件层应建立在清楚的任务划分上，否则数据传输和事件处理可能抵消计算核的收益。

## 常见工作流

1. 建立基线：记录模型规模、步长、求解器、平台、误差指标和运行时间。
2. 定位瓶颈：区分组装、求解、事件、I/O 和通信。
3. 选择最小改动路线：先复用结构和稀疏格式，再考虑并行或硬件部署。
4. 保持数值对照：比较电压、电流、开关时刻、能量误差和收敛记录。
5. 报告边界：说明适用拓扑、步长、精度、硬件和是否包含数据传输。

## 主要变体

| 变体 | 适合对象 | 不适合对象 |
|------|----------|------------|
| 稀疏直接法优化 | 结构稳定的网络方程 | 填充元失控或频繁变拓扑 |
| 迭代法与预处理 | 大规模稀疏系统、可接受残差准则 | 病态、不定或强事件驱动系统 |
| 元件级并行 | 大量相似元件或子模块 | 少量复杂且分支多的模型 |
| 网络分区 | 弱耦合子网、大规模系统 | 接口强耦合且通信密集系统 |
| 多速率 | 时间尺度分离明显的系统 | 接口误差主导或快速事件跨区传播 |
| 批量任务并行 | 参数扫描、蒙特卡洛、N-1 场景 | 单次闭环实时测试 |

## 适用边界与失败模式

- “实时”必须绑定步长、硬件、模型和最坏时延；不能从离线加速比推出。
- 模型降阶和近似计算需要误差度量，不能只以速度评价。
- 并行效率会受串行段、通信、负载不均和同步限制。
- 开关密集系统可能使缓存、分解复用和任务划分失效。
- 数据记录和可视化在长仿真中可能成为真实瓶颈。

## 代表性证据

- [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f]] 支撑“模型结构改写可改善数值效率”的单篇证据。
- [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp]] 可作为异构硬件用于详细风机实时仿真的代表性来源。
- [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad]] 可作为 FPGA EMT 实时仿真路线的代表性来源。

这些来源只能支撑其各自算例和平台条件；跨论文综合只能用于分类和边界描述，不应写成固定倍数或通用能力。

## 与相关页面的关系

- [[hardware-acceleration]]：关注专用硬件资源的执行层。
- [[gpu-parallel-acceleration]]：关注 GPU 编程模型和内存层次。
- [[high-performance-computing]]：关注多节点并行、强弱扩展和批量吞吐。
- [[heterogeneous-computing]]：关注多类执行资源的任务划分。
- [[large-scale-system-simulation]]：是计算加速的主要应用主题之一。

## 开放问题

- 如何建立跨平台、含误差边界的 EMT 加速基准。
- 如何把最坏时延、平均耗时、能耗、数值稳定性和模型维护成本放入同一评价框架。
- 如何让自动代码生成的加速实现保持与原 EMT 模型可追溯等价。
