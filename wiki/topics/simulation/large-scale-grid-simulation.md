---
title: "大规模电网仿真 (Large-Scale Grid Simulation)"
type: topic
tags: [large-scale, grid, simulation, parallel, hpc, gpu, multi-rate, co-simulation, ibm, ib-r]
created: "2026-05-02"
updated: "2026-05-14"
---

# 大规模电网仿真 (Large-Scale Grid Simulation)

## 定义

大规模电网仿真指对跨区域交流网、交直流混联系统、新能源基地、HVDC/FACTS 群和保护控制系统进行可复现的系统级暂态计算。其核心是在模型规模、仿真目的和计算资源之间取得平衡，使得电磁暂态（EMT）仿真能够覆盖从数百到数万母线的实际电网尺度。

"大规模"不是固定节点数门槛，而是由以下因素共同定义：节点数、支路数、设备模型复杂度（同步机、电力电子、保护控制）、时间步长、仿真时长、输出通道数量和并行架构。当系统规模使得传统串行单核 EMT 仿真在可接受时间内无法完成时，即进入大规模仿真范畴。

本页与[[large-scale-power-system]]的区别在于：后者定义大规模电力系统作为物理对象和拓扑结构；本页讨论围绕该对象开展 EMT、混合、实时或离线仿真的方法体系与工程实践。它也不同于[[fast-system-simulation]]，后者关注加速策略本身，而本页聚焦大电网场景下的方法选择、边界条件和量化性能。

## EMT 中的角色

EMT 在大规模电网仿真中用于捕捉相量模型难以描述的快速动态现象：

- **电力电子控制与开关事件**：逆变器控制环路（带宽数百至数千赫兹）、子模块电容充放电、限流闭锁动作引起的微秒至毫秒级暂态。
- **HVDC 多馈入相互作用**：LCC-HVDC 换相失败、直流故障传播、VSC-MTDC 多端协调控制引发的系统级振荡。
- **宽频响应**：频率相关线路模型、电缆JMarti模型、接地回路、滤波器和谐波共振引起的数十至数千赫兹响应。
- **保护与通信耦合**：继电保护动作、WAMPAC（广域测量与保护控制系统）、通信延迟对系统暂态的反馈影响。

高比例逆变器型资源（IBR）接入是驱动大规模 EMT 仿真的核心因素。传统同步机主导系统可用正序机电暂态（PDT）模型评估暂态稳定，但 IBR 含千赫兹量级电力电子开关、低惯量特性和宽频带控制，局部快速动态可能扩展为系统级影响，因此必须将 EMT 仿真从局部设备研究扩展到全网尺度。

## 并行仿真方法体系

大规模电网 EMT 仿真的加速方法可分为三大类：**网络分区并行**、**时间并行**和**硬件并行**。这三类方法正从"单一维度加速"走向"多维协同"。

### 网络分区并行（Network Partitioning Parallelism）

网络分区并行是大规模 EMT 仿真最经典、应用最广的加速策略。其核心思想是将全网划分为若干子网，各子网在独立处理器上并行求解，仅通过边界变量交换信息。

**伴随电路离散化基础**：EMT 时间步计算的伴随电路方法将 R-L-C 支路经梯形积分离散后，表示为当前等效导纳与上一时步历史电流源的组合：

$$G_n v_n + i_n^{hist} = 0$$

其中 $G_n$ 是节点电导矩阵，$v_n$ 是节点电压向量，$i_n^{hist}$ 是历史电流注入向量。每个时间步中，先由设备和网络历史项构造注入电流，再求解节点电压方程。

**块对角分解（BBD）**：ParaEMT 框架将全网电导矩阵自动组织为加边块对角（Banded Block Diagonal, BBD）形式。设网络划分为 $P$ 个子块，则电导矩阵可重写为：

$$G = \begin{bmatrix} G_{11} & 0 & \cdots & G_{1B} \\ 0 & G_{22} & \cdots & G_{2B} \\ \vdots & \vdots & \ddots & \vdots \\ G_{B1} & G_{B2} & \cdots & G_{BB} \end{bmatrix}$$

其中 $G_{ii}$ 是子块内部导纳矩阵（对角块），$G_{iB}$ 是子块与边界节点的耦合项（加边块）。各子块电压解可分配到不同 MPI 进程并行求解，边界耦合通过 Schur 补过程协调：

$$G_{BB}^{eff} v_B = i_B - \sum_{i=1}^{P} G_{iB}^T G_{ii}^{-1} i_i^{hist}$$

**传播延迟线路的自然解耦**：Filizadeh 2025 指出，利用传播延迟型输电线/电缆模型替代经典π型等值，可在线路两端形成自然解耦——延迟模型把线路两端在一个时间步内的电气关系转化为依赖历史行波量的端口注入，因此当前时刻两端不再出现在同一个代数方程组中，网络导纳矩阵天然可组织为多个子电路块。其接口量本质上是线路端口电压、电流以及由传播延迟产生的历史源项。

**补偿法（Compensation Method）**：当网络中没有适合作为分割边界的延迟线路时，补偿法通过等效注入修正子网络间相互作用。该方法已在含非线性模型场景中得到验证，其核心思想是在每个子网的边界节点注入等效电流以补偿被割断的耦合支路影响。

**局限**：短线路会迫使数值积分步长小于传播延迟，从而限制分割收益；当线路电气长度小于或接近数值积分步长时，传统基于线路延迟的分割方法失效。

### 多速率仿真（Multi-Rate Simulation）

多速率仿真的基本假设是大系统中不同区域具有不同的动态时间尺度。快动态区域（如电力电子变流器、HVDC 控制）使用小步长，慢动态区域（如同步机摇摆、负荷频率调节）使用大步长。

**多速率接口方程**：大系统可抽象为多个子系统，其接口关系为：

$$x_i^{k+1} = F_i(x_i^k, z_{\partial i}^k, u_i^k), \qquad 0 = \Psi(z_{\partial 1}^k, \ldots, z_{\partial m}^k)$$

其中 $x_i$ 是第 $i$ 个子系统状态，$z_{\partial i}$ 是接口电压、电流、相量或功率变量，$\Psi$ 是接口一致性约束。[[electromechanical-electromagnetic-hybrid-simulation]]、[[co-simulation]] 和 [[multirate-method]] 的差别主要在模型域、时间步长和接口同步方式。

**多速率实现策略**：
- **子网级多速率**：不同子网采用不同步长，通过接口插值同步
- **设备级多速率**：同一子网内不同设备使用不同步长，如变流器用 50 μs、同步机用 500 μs
- **混合多速率**：EMT 区域用微秒级步长，机电区域用毫秒级步长

### 时间并行（Parallel-in-Time）

时间并行（如 Parareal、MGRIT）从时间维度而非空间维度并行化 EMT 仿真。与网络分区并行不同，时间并行在同一空间网格上对时间步进行并行迭代。

**Parareal 算法**：使用粗步长预测器和细步长修正器的迭代框架：

$$x_{n+1}^{k+1} = G_{fine}(x_n^{k+1}, \Delta t_{fine}) + G_{coarse}(x_n^k, \Delta t_{coarse}) - G_{coarse}(x_n^k, \Delta t_{coarse})$$

其中 $G_{fine}$ 是细步长传播算子，$G_{coarse}$ 是粗步长传播算子。时间并行在 EMT 仿真中的适用性取决于系统的时间尺度分离特性——对于具有明显快慢动态分离的系统，粗步长预测器能够提供合理的初值。

### 硬件并行（Hardware Parallelism）

硬件并行利用多核 CPU、GPU 众核架构或 FPGA 并行硬件加速 EMT 计算。

**GPU Massive-Thread 并行**：Zhou & Dinavahi 2014 提出的 MT-EMTP 面向 GPU massive-thread 架构重构线性无源元件、通用线路模型和通用电机模型。其核心创新是 node-mapping structure——将原始电力系统导纳矩阵转换为 block-node diagonal sparse 格式，使不同块节点的数据访问和计算更规则，减少串行节点遍历对 GPU SIMT 执行的阻碍。

**全 GPU 驻留求解器**：Aluthge 等 2026 构建的全 GPU 驻留 EMT 实现中，网络矩阵、元件状态、右端项组装和稀疏求解尽量都在 GPU 侧完成，用 cuDSS/Cholesky 作为核心求解路径，避免每个时间步 CPU-GPU 往返传输。其核心方程仍为经典 EMT 伴随电路形式：

$$Y(t) v(t) = i(t)$$

算法流程为：在 GPU 上保存稀疏导纳矩阵、元件参数、历史电流和节点电压；对 $Y$ 做符号分析与数值分解；时间推进时由 CUDA 内核并行更新非动态电流源、无源元件历史项和同步机相关方程，再组装 RHS 并调用 GPU 稀疏求解器求 $v$。Cholesky 分解 $Y = LL^T$ 利用实数、对称正定导纳矩阵结构减少存储和计算；Woodbury 公式用于评估少量矩阵元素变化时是否可用低秩修正替代全矩阵重分解。

## 高性能计算平台

### ParaEMT 框架

ParaEMT 是一个开源、Python-based、可并行且 HPC-compatible 的 EMT 仿真框架，由 Xiong 等 2024 提出。其计算内核沿用经典 EMT 伴随电路思想，核心特征包括：

- **BBD 网络电导矩阵分解**：自动将全网电导矩阵组织为加边块对角形式
- **设备状态并行更新**：各子网设备状态更新分配到不同 MPI 进程
- **网络历史电流并行更新**：历史电流源更新天然按元件分解，可并行执行

**验证数据**（来源：Xiong 2024 原文摘要）：
- 精度验证：缩减 240 母线、720 三相节点的 WECC 系统，以 PSCAD/EMTDC 为 EMT 动态 benchmark
- 可扩展性：合成 10080 母线、30240 节点系统，利用 NREL Eagle HPC 资源获得约 25 至 36 倍加速（相对串行实现）
- 应用展示：将缩减 240 母线系统的加州区域构造成 100% renewable case，研究大规模电网中系统级 IBR 交互

### GPU 加速仿真平台

**MT-EMTP**（Zhou & Dinavahi 2014）：面向 GPU massive-thread 架构的 EMT 仿真器，测试系统最大为 2458 个三相母线，与商业软件 EMTP-RV 比较仿真结果和执行时间。原文摘要报告通过 GPU 众核和 block-node diagonal sparse 矩阵组织提升离线大规模仿真的计算吞吐。

**GPU-cuDSS 求解器**（Aluthge 等 2026）：在 IEEE 39 节点系统中，101 s 仿真、50 μs 步长下 GPU 求解器 220 s、PSCAD/EMTDC 260 s；在 Texas 2000 节点合成电网（15618 阶矩阵）、5 s 仿真中，GPU 求解器 51 s 而 PSCAD/EMTDC 2016 s（加速约 39.5 倍）。

### CPU 并行仿真

**Abusalah 等 2018**：基于 CPU 多核并行的 EMT 仿真，利用自然解耦线路模型形成块对角结构，在大规模电力电子集成系统中实现并行加速。

## 机器学习加速

Cheng 等 2025 提出 ML-reinforced massively parallel transient simulation，将机器学习引入大规模新能源并网 EMT 仿真。

**方法架构**：三层结构：
1. **RES 数据驱动模型**：对 PV 阵列等近似时不变非线性组件采用 MLP 表示端口量、环境量到输出电气量的映射；对 DFIG 和储能电池等动态组件采用 GRU 保留历史状态。MLP 的线性变换加非线性激活用于近似原物理模型中的非线性代数关系；GRU 通过更新门、重置门、候选隐状态和隐状态融合，决定当前输入与上一时刻记忆对输出的贡献。
2. **训练流程**：用传统物理 EMT 模型产生可靠训练数据，用 MATLAB/Simulink 进行验证。
3. **实现架构**：在 CPU-GPU 异构仿真中，RES ANN 被封装进 ECS 的组件体系；大量相同结构实体通过 GPU instancing 组织为连续、规则的数据布局。

**验证数据**（来源：Cheng 2025 原文摘要）：
- 在 2,560,000 个 MLP PV 面板规模下（双 V100 GPU），相比 traditional CPU nonlinear iterative computations 达到 **400 倍加速**
- 精度：额定辐照度下相对误差约 0.2%，部分阴影条件下约 4%
- 测试系统：RES components grouped into a microgrid connected to a synthetic AC/DC system based on the IEEE 118-Bus system

## 多尺度等效建模

### 低维等效模型（Low-Dimensional Equivalent Models）

Xu 等 2025 提出多 VSC 电路的低维等效模型，适用于高比例新能源并网后大型光伏电站、柔直等场景中 VSC 数量快速增加的情况。

**核心机制**：在 VSC 与交流电网接口处用半隐式混合积分引入半步长交错量，把内部节点与外部节点的直接代数耦合拆开。半隐式混合积分把梯形积分与中心差分结合，使某一子系统在 $n+1$ 或 $n+1/2$ 时刻的更新只依赖另一子系统半步滞后的量，从而把原本同一步内必须联立求解的内外节点拆成可并行的局部问题。

随后对每相电路进行等效综合，把多 VSC 开关网络在外部看来转换为低维等效导纳和历史源。针对直流侧独立与直流侧并联分别推导等效关系，使模型能覆盖光伏单元独立直流侧以及类似背靠背/并联系统的直流耦合情况。

**验证数据**（来源：Xu 2025 原文摘要）：
- 测试系统：并网 100 MW 光伏电站，包含多 VSC 运行
- 串行加速：由解耦和低维化带来的串行模式加速超过 **80 倍**
- 并行加速：在此基础上启用 OpenMP 并行模式后获得 **2–3 倍二次加速**
- 精度描述："almost uncompromising accuracy"

### 通用 N 端口等效模型

Wang 等 2026 提出任意拓扑 N 端口子模块的通用等效模型，以离散状态空间 A、B、C、D 描述 N 端口网络。Norton 形式中端口电压为输入、端口电流为输出、历史电流源为状态量。

**验证数据**（来源：Wang 2026 原文）：
- DBM²C-SST 算例：N_FPN=500 时详细模型总耗时 121.44 s、等效模型 16.75 s，节点电压求解耗时由 100.23 s 降至 4.36 s（加速约 23 倍）
- MMC 算例：N_SM=500 时详细模型、子模块等效模型、桥臂等效模型总耗时分别为 216.90 s、133.40 s、7.36 s；桥臂等效总体加速比 **29.47**

## 量化性能边界

### 并行加速性能汇总

| 方法 | 系统规模 | 硬件 | 加速比 | 数据来源 |
|------|---------|------|--------|---------|
| ParaEMT (BBD) | 10080 母线 (30240 节点) | NREL Eagle, 84 MPI ranks | 25–36× | Xiong 2024 |
| MT-EMTP (GPU) | 2458 三相母线 | GPU | ~40× | Zhou & Dinavahi 2014 |
| GPU-cuDSS | Texas 2000 节点 (15618 阶) | GPU | ~39.5× | Aluthge 2026 |
| GPU-cuDSS | IEEE 39 节点, 101s 仿真 | GPU vs PSCAD | 1.18× | Aluthge 2026 |
| ML-ANN (Cheng) | 2.56M PV panels | Dual V100 GPUs | 400× | Cheng 2025 |
| 低维等效 (Xu) | 100 MW PVPS, 多 VSC | OpenMP | 80× (串行) + 2-3× (并行) | Xu 2025 |
| N端口等效 (Wang) | MMC N_SM=500 | Matlab | 29.47× | Wang 2026 |

### 仿真步长与精度权衡

| 仿真类型 | 典型步长 | 适用场景 | 精度范围 |
|---------|---------|---------|---------|
| 全 EMT 详细模型 | 50–100 μs | IBR 控制、开关事件、HVDC 故障 | 波形级 |
| 平均模型 (AVM) | 100–500 μs | 场站级动态、控制交互 | 基频±3次谐波 |
| 动态相量 (DP) | 1–10 ms | 宽频振荡、次同步交互 | 10–500 Hz |
| 机电暂态 (PDT) | 10–100 ms | 功角稳定、频率稳定 | < 10 Hz |

### 并行扩展性限制

| 因素 | 影响机制 | 典型表现 |
|------|---------|---------|
| BBD 角矩阵非零增长 | 子块数增加导致边界耦合矩阵膨胀 | 超过 ~42 个分区后加速比饱和 |
| 短线路传播延迟 | 数值步长小于线路延迟，无法自然解耦 | 需要补偿法或联合节点-状态空间方法 |
| GPU 通信开销 | CPU-GPU 数据传输抵消计算加速 | 全 GPU 驻留方案可减少 |
| 拓扑频繁变化 | 导纳矩阵反复变化导致预分解失效 | Woodbury 公式或补偿法处理 |

## 实时与 HIL 迁移

当大规模电网用于 [[real-time-simulation]] 或 [[hil-simulation]]，还必须满足：

$$\max_k T_{\mathrm{step}}(k) < \Delta t$$

或至少给出 overrun 处理规则。

**工程移植经验**（来源：Le-Huy 等 2023）：Hydro-Québec 从多年工具开发和工程移植经验中总结出离线 EMT 模型到实时 HIL 模型的系统化移植流程。核心挑战包括：
- 两套软件环境（EMTP 离线 vs HYPERSIM 实时）的组件、参数、连线、控制模块和实时约束差异
- 复杂内部控制多时，手工重建、核对信号和处理无直接等价元件成为专家密集型任务
- 缺少导出/导入和自动 place-and-route 导致历史上移植代价很高

**大规模混合实时仿真案例**（来源：Zhou 等 2021, Nelson River 多馈入 HVDC 系统）：支撑大规模多馈入 HVDC 混合实时 HIL 的模块化建模、逐级集成和现场投运验证边界。

## 关键技术挑战

### 1. 开放基准测试缺失

公开 benchmark 不足时，单个工程系统的容量、加速比和实时性不应外推为领域共识。如何建立开放、可复现且包含控制保护细节的大规模 EMT benchmark 仍是未决问题。

### 2. 外部系统等值误差与局部 EMT 精度的联合评价

如何同时评价外部系统等值误差、局部 EMT 精度、接口稳定性和并行扩展性，是大规模仿真验证的核心挑战。[[emt-simulation-verification]] 说明大规模仿真结果需要怎样的波形、接口和证据校核。

### 3. 工程保密模型的可审计性

如何在工程保密模型不可公开时提供足够的审计证据，使大规模仿真结论可复核，是工业界面临的实际困难。

### 4. IBR 电网的自动初始化

电力电子和可再生能源模型的初始化仍比传统同步机更困难。Filizadeh 2025 指出，自动初始化是从潮流解出发，尽快构造时域模型的稳态初值，并特别处理同步发电机控制、电力电子变换器和可再生能源电站的初始条件，以减少启动阶段非物理暂态。

## 分网算法选择指南

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|-----|
| 含大量长距离输电线路的系统 | 传播延迟线路 + BBD 分区 | 天然解耦，边界清晰 |
| 城市配电网/短线路为主 | 补偿法 / 节点-状态空间联合 | 短线路无自然延迟边界 |
| 含大量电力电子变流器 | GPU 并行 + 多速率 | 开关密度高，时间尺度分离明显 |
| 大规模新能源场站 | 低维等效 + 多线程并行 | 多 VSC 并联，矩阵维度高 |
| 百万级细粒度 RES 实体 | ML-ANN + GPU instancing | 非线性迭代难以并行 |
| 实时 HIL 移植 | 系统化移植流程 + 模型库兼容 | 工具链差异导致手工重建成本高 |

## 适用边界

- **"大规模"是相对概念**：规模应与节点、支路、设备模型、控制逻辑、步长、输出通道和仿真时长一起报告，不应仅用节点数定义。
- **全系统统一小步长的代价**：可能可解释性强但成本过高；过度等值则可能丢失外部网络动态、频带响应或保护相关波形。
- **并行分区的收益递减**：并行分区可能降低矩阵规模，但接口延迟、通信和迭代收敛可能抵消收益。BBD 角矩阵非零增长会导致加速比在分区数超过约 42 后饱和。
- **初始化敏感性**：大规模模型初始化、潮流一致性、控制状态、保护定值和事件时间对结果影响很大，不能只检查稳态潮流。
- **验证范围限制**：论文结果通常仅覆盖作者测试的特定系统、元件模型集合和基线工具，不等同于已证明适用于实时仿真、所有控制模型、所有故障类型或后续硬件平台。

## 相关方法

### 并行与计算加速
- [[parallel-computing]] — 并行计算基础
- [[multithreaded-parallel-computing]] — 多线程并行
- [[high-performance-computing]] — HPC 仿真
- [[gpu-parallel-acceleration]] — GPU 加速
- [[network-partitioning]] — 网络分区方法
- [[parallel-in-time]] — 时间并行算法

### 多速率与混合仿真
- [[multirate-method]] — 多速率仿真方法
- [[co-simulation]] — 协同仿真
- [[electromechanical-electromagnetic-hybrid-simulation]] — 机电-电磁混合仿真
- [[heterogeneous-computing]] — 异构计算

### 等效建模
- [[network-equivalent]] — 网络等值
- [[fdne-model]] — FDNE 模型
- [[dynamic-phasor]] — 动态相量法
- [[low-rank-solver]] — 低秩求解器

### 验证与实时
- [[emt-simulation-verification]] — EMT 仿真验证
- [[real-time-simulation]] — 实时仿真
- [[hil-simulation]] — HIL 仿真
- [[hardware-in-loop]] — 硬件在环

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Filizadeh 2025 — Electromagnetic Transient Modeling and Simulation of Large Power Systems | 2025 | EMT 仿真器技术路线综述：传播延迟线路、补偿法、自动初始化、多域协同仿真 |
| Xiong 等 2024 — ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator | 2024 | 开源 BBD 并行 EMT 框架，10080 母线 36× 加速，NREL Eagle HPC 验证 |
| Zhou & Dinavahi 2014 — Parallel Massive-Thread EMT Simulation on GPU | 2014 | MT-EMTP GPU 并行架构，node-mapping structure，2458 母线验证 |
| Aluthge 等 2026 — Accelerating EMT Simulations Using GPUs | 2026 | 全 GPU 驻留求解器，cuDSS/Cholesky，Texas 2000 节点 39.5× 加速 |
| Cheng 等 2025 — ML-Reinforced Massively Parallel Transient Simulation | 2025 | ML-ANN 替代非线性迭代，2.56M PV 面板 400× 加速 |
| Xu 等 2025 — Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT | 2025 | 多 VSC 低维等效 + OpenMP 并行，100 MW 光伏电站 80× 串行加速 |
| Wang 等 2026 — Component-Level Modeling and Fine-Grained Simulation for Renewable Energy | 2026 | N 端口通用子模块等效，MMC 500 子模块 29.47× 加速 |
| Le-Huy 等 2023 — Lessons Learned in Porting Offline Large-Scale EMT to Real-Time | 2023 | Hydro-Québec 离线到实时 HIL 移植经验，WAMPAC 系统 |
| Le-Huy 等 2023 — Performance Evaluation of Communication Fabrics for Offline Parallel EMT | 2023 | 离线并行 EMT 平台评估，通信结构对扩展性的影响 |
| Jiang 等 2024 — Key Technologies for EMT Parallel Simulation in New Power System | 2024 | 新型电力系统 EMT 并行仿真关键技术综述 |
| Zhou 等 2021 — Large-Scale Hybrid Real-Time Simulation for Nelson River HVDC | 2021 | Nelson River 多馈入 HVDC 混合实时 HIL 现场验证 |
| Abusalah 等 2018 — CPU-Based Parallel Computation of EMT for Large Power Grids | 2018 | CPU 多核并行 EMT，自然解耦线路模型 |
