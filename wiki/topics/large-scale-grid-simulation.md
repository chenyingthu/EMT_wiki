---
title: "大规模电网仿真 (Large-Scale Grid Simulation)"
type: topic
tags: [large-scale, grid, simulation, parallel, efficiency, distributed, hpc]
created: "2026-05-02"
---

# 大规模电网仿真 (Large-Scale Grid Simulation)

## 定义与边界

大规模电网仿真指对跨区域交流网、交直流混联系统、新能源基地、HVDC/FACTS 群和保护控制系统进行可复现的系统级暂态计算。它关注“电网仿真任务”如何在模型规模、仿真目的和计算资源之间取得平衡。

本页与[[large-scale-power-system]]的区别是：后者定义大规模电力系统作为对象和结构；本页讨论围绕该对象开展 EMT、混合、实时或离线仿真的方法边界。它也不同于[[fast-system-simulation]]，后者关注加速策略本身。

## EMT 中的作用

EMT 在大规模电网仿真中通常用于局部或全局地捕捉相量模型难以描述的现象：

- 电力电子控制、限流、闭锁、子模块电容和开关事件引起的快速暂态。
- LCC-HVDC 换相失败、直流故障和多馈入相互作用。
- 频率相关线路、电缆、接地回路、滤波器和变压器饱和引起的宽频响应。
- 保护动作、控制器 HIL、WAMPAC 与通信延迟对系统暂态的影响。

## 主要分支与机制

### 全 EMT 与局部 EMT

全 EMT 模型把研究系统全部表示为相域或多导体时域模型，适合需要瞬时波形和保护动作的范围；局部 EMT 则只把关键区域详细化，外部系统用[[network-equivalent]]、[[fdne-model]]、[[dynamic-phasor]] 或机电相量模型表示。边界选择应报告保留区域、外部等值端口、故障位置和验证基准。

### 混合与多速率仿真

大系统可抽象为多个子系统

$$
x_i^{k+1}=F_i(x_i^k,z_{\partial i}^k,u_i^k),\qquad
0=\Psi(z_{\partial 1}^k,\ldots,z_{\partial m}^k),
$$

其中 $x_i$ 是第 $i$ 个子系统状态，$z_{\partial i}$ 是接口电压、电流、相量或功率变量，$\Psi$ 是接口一致性约束。[[electromechanical-electromagnetic-hybrid-simulation]]、[[co-simulation]] 和 [[multirate-method]] 的差别主要在模型域、时间步长和接口同步方式。

### 并行与高性能计算

[[network-partitioning]]、[[parallel-computing]]、[[multithreaded-parallel-computing]] 和 [[high-performance-computing]] 可扩展大系统仿真规模。并行证据应以端到端每步时间、通信开销、负载均衡和波形一致性报告。[[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn]] 支撑“通信结构会限制离线并行 EMT 扩展”的判断。

### 实时与 HIL 迁移

当大规模电网用于 [[real-time-simulation]] 或 [[hil-simulation]]，还必须满足

$$
\max_k T_{\mathrm{step}}(k) < \Delta t
$$

或至少给出 overrun 处理规则。[[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] 支撑离线模型迁移到实时环境时，模型兼容、控制代数环、初始化策略和信号校核会成为仿真质量的一部分。

## 适用边界与失败模式

- “大规模”不是固定节点数门槛；规模应与节点、支路、设备模型、控制逻辑、步长、输出通道和仿真时长一起报告。
- 全系统统一小步长可能可解释性强但成本过高；过度等值则可能丢失外部网络动态、频带响应或保护相关波形。
- 并行分区可能降低矩阵规模，但接口延迟、通信和迭代收敛可能抵消收益。
- 大规模模型初始化、潮流一致性、控制状态、保护定值和事件时间对结果影响很大，不能只检查稳态潮流。
- 公开 benchmark 不足时，单个工程系统的容量、加速比和实时性不应外推为领域共识。

## 代表性来源

- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：支撑大规模多馈入 HVDC 混合实时 HIL 的模块化建模、逐级集成和现场投运验证边界。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]]：支撑大系统离线到实时迁移的工程流程和证据纪律。
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]：支撑大型 AC 与 MMC-MTDC 多速率 EMT 协同仿真，不引用未核验的泛化加速结论。
- [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]]：支撑实时并行任务映射需要同时考虑任务负载和处理器拓扑。
- [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn]]：支撑离线并行 EMT 平台评估需要报告通信结构和应用级指标。

## 与相关页面的关系

- [[large-scale-power-system]] 定义大规模互联电力系统对象；本页讨论如何仿真该对象。
- [[large-scale-hybrid-acdc-simulation]] 聚焦交直流混联和 HVDC/VSC/MMC 接口。
- [[fast-system-simulation]] 汇总加速策略；本页只在大电网场景中使用这些策略。
- [[network-partitioning]] 是大规模仿真分区和并行的基础方法页。
- [[emt-simulation-verification]] 说明大规模仿真结果需要怎样的波形、接口和证据校核。

## 开放问题

- 如何建立开放、可复现且包含控制保护细节的大规模 EMT benchmark。
- 如何同时评价外部系统等值误差、局部 EMT 精度、接口稳定性和并行扩展性。
- 如何在工程保密模型不可公开时提供足够的审计证据，使大规模仿真结论可复核。
