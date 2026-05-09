---
title: "快速系统仿真 (Fast System Simulation)"
type: topic
tags: [fast-simulation, acceleration, parallel, model-reduction, gpu, fpga]
created: "2026-05-02"
---

# 快速系统仿真 (Fast System Simulation)


```mermaid
graph LR
    N0[技术背景]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N1 --> N2
    N3[主要分支与机制]
    N2 --> N3
    N4[适用边界与失败模式]
    N3 --> N4
    N5[代表性来源]
    N4 --> N5
    N6[与相关页面的关系]
    N5 --> N6
    N7[开放问题]
    N6 --> N7
```


## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

快速系统仿真指在保持目标暂态现象可解释的前提下，缩短 EMT 仿真端到端时间的算法、模型和计算实现集合。它包括[[computational-acceleration]]、[[parallel-computing]]、[[model-order-reduction]]、[[network-partitioning]]、[[multirate-method]]、[[hardware-acceleration]] 和 [[fpga-real-time-simulation]] 等路线。

本页不把“快速”直接等同于“高精度”“实时”或“通用加速”。任何加速比、误差或实时裕度都必须绑定测试系统、模型层级、步长、硬件平台、通信方式和基准求解器。若只报告局部内核耗时，不能外推为完整 EMT 工作流加速。

## EMT 中的作用

EMT 仿真常由最小步长、频繁开关事件、稀疏线性方程求解、控制器更新和输出记录共同决定耗时。快速系统仿真的作用是把计算资源集中在研究对象需要的频带、区域和事件上，使以下任务可计算或可重复：

- 大规模电网故障、换相失败、保护动作和控制限幅的批量扫描。
- 含 MMC、VSC、风电场、光伏电站或 HVDC 的局部详细 EMT 与外部系统等值联合分析。
- [[real-time-simulation]] 与 [[hil-simulation]] 中的 deadline 约束检查。
- 参数辨识、模型校准、概率工况和运行策略筛选中的重复 EMT 运行。

## 主要分支与机制

### 算法与求解器加速

节点方程通常可写成

$$
Y_k v_k=i_k,\qquad x_{k+1}=\Phi(x_k,v_k,u_k),
$$

其中 $Y_k$ 是第 $k$ 步等效导纳矩阵，$v_k$ 是节点电压，$i_k$ 是历史源和注入电流，$x_k$ 是元件与控制状态。加速可来自[[sparse-matrix-solver]]、矩阵重排序、局部分解复用、[[fixed-admittance]]、事件局部更新和更适合刚性问题的[[numerical-integration]]。这些方法不改变研究对象本身，但会改变每步求解成本和事件处理代价。

### 分区、并行与任务映射

若系统被划分为 $P$ 个任务，端到端时间近似受

$$
T_{\mathrm{step}}=\max_{p\le P} T_{\mathrm{solve},p}+T_{\mathrm{comm}}+T_{\mathrm{sync}}
$$

约束。$T_{\mathrm{solve},p}$ 为第 $p$ 个分区求解时间，$T_{\mathrm{comm}}$ 为接口通信时间，$T_{\mathrm{sync}}$ 为同步和调度开销。[[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]] 将实时 EMT 的任务分离和任务映射明确建模为图划分问题，可作为“并行性能依赖硬件拓扑和通信代价”的代表证据。

### 多速率与模型层级选择

[[multirate-method]] 通过快区步长 $h_f$ 与慢区步长 $h_s=N h_f$ 的组合降低全系统小步长负担；[[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]] 支撑大型 AC 与 MMC-MTDC 系统按动态时间尺度分区的路线。模型层级方面，[[average-value-model]]、[[dynamic-phasor]]、[[network-equivalent]] 和 [[fdne-model]] 可减少状态数量或频带范围，但会舍弃部分开关、谐波、保护瞬时量或端口互耦。

### 硬件与异构加速

[[gpu-parallel-acceleration]]、[[hardware-acceleration]] 和 [[fpga-real-time-simulation]] 关注把矩阵运算、批量元件更新或固定拓扑求解映射到 GPU、FPGA 或异构平台。硬件加速的证据应同时报告波形误差、资源占用、数据搬移、最坏步长耗时和失败工况；不能只用设备峰值算力说明 EMT 仿真能力。

## 适用边界与失败模式

- 加速效果受 Amdahl 型限制：串行事件处理、I/O、同步、控制器代数环和通信可能支配总耗时。
- 分区接口若跨越强耦合、低阻抗或快速控制闭环，可能引入非物理延迟、功率不平衡或数值振荡。
- 模型降阶和等值只在指定端口、频带、工况和控制状态内有效；故障、闭锁和保护动作可能需要切回详细模型。
- GPU 或 FPGA 对规则、批量、固定结构计算更有利；稀疏不规则拓扑、频繁分支和小规模算例可能无法受益。
- “超实时”与 HIL 实时不同。前者强调平均运行快于真实时间，后者要求每个步长满足最坏时延和抖动约束。


### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s
- 电压等级：10kV ~ 500kV
- 功率范围：1MW ~ 1000MW
- 频率范围：50Hz / 60Hz

## 代表性来源

- [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]]：支撑实时并行 EMT 中任务分离、源图到目标图映射、负载均衡和通信代价约束；具体网络规模、步长和平台结论应限于原文案例。
- [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn]]：支撑离线 MPI 并行 EMT 性能需要用每步时间、加速比、效率和 Karp-Flatt 指标解释，而不能只看核心数。
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]：支撑多速率 AC-MTDC EMT 协同仿真机制；当前页面不引用未核验的具体加速百分比。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]]：支撑离线大系统迁移到实时平台时，模型兼容、信号校核和实时性能约束共同决定是否可运行。
- [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el]] 与 [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad]] 可作为 FPGA 实时 EMT 的入口，结论必须绑定原文电路、芯片和步长。

## 与相关页面的关系

- [[large-scale-grid-simulation]] 关注大电网 EMT 问题本身；本页关注让这些问题更快求解的策略。
- [[network-partitioning]] 是并行和多速率加速的结构基础，但分区本身不保证加速。
- [[real-time-simulation]] 定义硬实时 deadline；快速系统仿真可以服务于实时化，也可只用于离线批量分析。
- [[model-order-reduction]]、[[average-value-model]] 和 [[fdne-model]] 是降低模型复杂度的具体方法页。
- [[parallel-computing]] 和 [[high-performance-computing]] 讨论计算架构；本页只综合它们在 EMT 任务中的证据使用规则。

## 开放问题

- 如何建立同时报告端到端时间、波形误差、事件时间、接口功率误差和硬件资源的公共 benchmark。
- 如何在保护动作、控制限幅和开关事件密集时动态选择详细模型、平均模型和等值模型。
- 如何把图分区、任务映射、通信拓扑和模型误差统一到可审核的 EMT 加速证据链中。
