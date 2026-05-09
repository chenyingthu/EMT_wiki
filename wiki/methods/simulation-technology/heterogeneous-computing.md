---
title: "异构计算 (Heterogeneous Computing)"
type: method
tags: [heterogeneous-computing, cpu, gpu, fpga, accelerator]
created: "2026-05-02"
---

# 异构计算 (Heterogeneous Computing)


```mermaid
graph TD
    N0[异构计算 (Heterogene…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[任务划分模型]
    N0 --> N3
    N4[核心工作流]
    N0 --> N4
    N5[典型架构]
    N0 --> N5
    N6[设计准则]
    N0 --> N6
    N7[适用边界与失败模式]
    N0 --> N7
    N8[代表性证据]
    N0 --> N8
```


## 定义与边界

异构计算是把同一 EMT 仿真流程中的不同任务分配给不同类型执行资源，例如 CPU、GPU、FPGA、DSP、实时 I/O 板卡或集群节点。其核心不是“硬件越多越快”，而是任务特征、数据移动、时序约束和数值验证之间的匹配。

本页关注协同调度和边界设计。单类硬件能力见 [[hardware-acceleration]]，GPU 细节见 [[gpu-parallel-acceleration]]，集群层见 [[high-performance-computing]]。

## EMT 中的作用

EMT 流程天然包含不同粒度的任务：

- CPU 适合仿真主循环、拓扑事件、文件 I/O、复杂控制和调度。
- GPU 适合批量元件更新、稀疏线性代数和多场景吞吐。
- FPGA 适合固定延迟流水线、PWM/IO、保护接口和某些固定拓扑子模型。
- 集群节点适合大规模分区或批量任务。

异构计算的目标是为每个任务选择合适资源，并证明跨资源接口不会破坏 EMT 的数值和时序要求。

## 任务划分模型

可把每步计算写成：

$$
T_{step}=\max(T_{cpu}, T_{gpu}, T_{fpga}) + T_{transfer}+T_{sync}
$$

若任务串行依赖强，则应改写为：

$$
T_{step}=T_{cpu}+T_{transfer}^{cpu\to acc}+T_{acc}+T_{transfer}^{acc\to cpu}+T_{sync}
$$

这说明异构系统的瓶颈经常在接口和同步，而不是单个设备峰值性能。

## 核心工作流

1. 列出每步任务图：模型更新、矩阵组装、求解、开关处理、控制接口、输出。
2. 标注每个任务的数据量、依赖、实时 deadline 和数值精度需求。
3. 把高吞吐、低分支任务映射到 GPU，把固定时序任务映射到 FPGA，把复杂控制留在 CPU。
4. 设计跨资源数据结构，避免每步全量复制。
5. 用端到端指标验证：波形误差、残差、事件时刻、最坏步长时间和抖动。

## 典型架构

### CPU + GPU

CPU 负责控制流、事件处理和 I/O；GPU 负责稀疏线性代数或大量同构元件更新。适合离线大规模仿真和批量任务，但 HIL 需额外证明最坏延迟。

### CPU + FPGA

CPU 负责模型管理和较复杂的非线性逻辑；FPGA 负责固定延迟的子电路、PWM、保护接口或高速 I/O。适合实时测试，但需要严格字长、资源和接口验证。相关页面见 [[fpga-real-time-simulation]] 和 [[fixed-point-conversion]]。

### CPU + GPU + FPGA

三类资源混合时，任务划分更细，但同步和数据一致性风险也更高。只有当 GPU 与 FPGA 的工作可并行重叠，且数据交换受控时，复杂性才可能被收益抵消。

### 分布式异构

在 HPC 环境中，每个节点可带 GPU 或 FPGA。此时既要处理节点内异构调度，也要处理节点间 MPI 通信、负载均衡和 I/O，相关问题见 [[high-performance-computing]]。

## 设计准则

- 先降低数据移动，再追求设备峰值算力。
- 让开关事件、拓扑修改和错误处理有明确的所有者。
- 保持接口变量最小化，例如只交换边界电压、电流或等效源。
- 对定点、单精度、双精度和混合精度分别做误差验证。
- 对 HIL 报告最坏延迟和抖动；对离线任务报告端到端耗时和误差。

## 适用边界与失败模式

- 任务划分过细会导致调度和传输开销超过计算收益。
- 多设备数值格式不一致可能造成小误差累积或事件时刻漂移。
- GPU 与 FPGA 之间直接通信若不可用，CPU 中转可能成为瓶颈。
- 实时系统中，平均执行时间不能替代最坏时延分析。
- 平台依赖强的实现需要记录硬件、驱动、编译器和模型版本。

## 代表性证据

- [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp]] 可作为详细风机模型异构实时仿真的代表性单篇来源。
- [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]] 可作为复杂换流器模型与实时实现关系的来源示例。
- [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad]] 可作为 FPGA 在 EMT 实时化中的来源示例。

这些来源不应被合并为“异构计算普遍实现实时”的强断言；它们支撑的是具体模型、平台和步长条件下的报告结果。

## 与相关页面的关系

- [[computational-acceleration]]：解释异构计算在总加速策略中的位置。
- [[hardware-acceleration]]：比较 GPU、FPGA 和专用硬件边界。
- [[gpu-parallel-acceleration]]：给出 GPU 侧任务的实现细节。
- [[high-performance-computing]]：处理多节点异构系统的扩展性。
- [[sparse-matrix-techniques]]：提供矩阵任务划分的数值基础。
- [[automatic-code-generation]]：与异构部署相关，但需要等价性验证。

## 开放问题

- 如何自动从 EMT 模型生成可验证的 CPU/GPU/FPGA 任务图。
- 如何在异构执行中统一误差、延迟、能耗和可维护性指标。
- 如何记录跨设备执行的完整 provenance，使仿真结果可复现和可审计。
