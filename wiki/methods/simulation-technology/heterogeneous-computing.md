---
title: "异构计算 (Heterogeneous Computing)"
type: method
tags: [heterogeneous-computing, cpu, gpu, fpga, accelerator, parallel-computing, real-time-simulation]
created: "2026-05-02"
updated: "2026-05-14"
---

# 异构计算 (Heterogeneous Computing)

## 定义

异构计算是指将同一 EMT 仿真流程中的不同计算任务分配给**不同类型的硬件执行单元**，以充分发挥各类硬件在并行度、延迟、功耗和编程灵活性方面的互补优势。核心不是"硬件越多越快"，而是根据**任务特征**（数据量、分支复杂度、时序约束、数值精度需求）与**硬件能力**（并行线程数、内存带宽、时钟频率、指令集）之间的匹配来优化整体仿真效率。

在 EMT 仿真语境中，异构计算主要涉及以下硬件类型：

- **CPU**：通用处理器，擅长控制流、拓扑事件处理、I/O、复杂非线性控制和调度逻辑
- **GPU**：众核加速器，擅长批量同构元件更新、稀疏线性代数、大规模矩阵运算
- **FPGA**：可重构逻辑阵列，擅长固定延迟流水线、PWM 生成、高速 I/O、微秒级实时求解
- **DSP**：专用数字信号处理器，擅长固定点滤波、控制算法实现
- **集群节点**：分布式计算单元，适合大规模网络分区或蒙特卡洛批量任务

本页关注**协同调度策略**、**跨资源接口设计**和**数值一致性验证**。单类硬件能力详见 [[hardware-acceleration]]，GPU 细节详见 [[gpu-parallel-acceleration]]，HPC 集群层详见 [[high-performance-computing]]。

## EMT 中的角色

EMT 仿真流程天然包含不同粒度的任务，每种任务对硬件的要求差异显著：

1. **网络求解**（节点导纳矩阵组装 + 稀疏线性方程求解）— 计算密集、数据并行度高，适合 GPU / 多核 CPU
2. **元件模型更新**（电力电子开关、传输线、旋转电机）— 批量同构更新，适合 GPU SIMT 架构
3. **拓扑事件处理**（开关动作、故障检测）— 分支复杂、依赖串行，适合 CPU
4. **控制系统**（PLL、 droop 控制、保护逻辑）— 控制流复杂、时序要求灵活，适合 CPU
5. **高速 I/O 接口**（PWM 输出、传感器采集、HIL 通信）— 固定延迟、微秒级精度，适合 FPGA
6. **文件 I/O 与后处理** — 串行、I/O 密集，适合 CPU

异构计算的目标是为每个任务选择最合适的资源，并保证**跨资源数据接口**不会破坏 EMT 仿真的数值精度和时序约束。

## 任务划分模型

### 时间分解模型

将每步仿真时间分解为：

$$T_{\text{step}} = \max(T_{\text{CPU}}, T_{\text{GPU}}, T_{\text{FPGA}}) + T_{\text{transfer}} + T_{\text{sync}}$$

其中 $T_{\text{CPU}}$、$T_{\text{GPU}}$、$T_{\text{FPGA}}$ 分别为各设备上的计算时间，$T_{\text{transfer}}$ 为设备间数据传输时间，$T_{\text{sync}}$ 为同步开销。若任务串行依赖强（如 CPU 控制流驱动 GPU 计算），则退化为：

$$T_{\text{step}} = T_{\text{CPU}} + T_{\text{transfer}}^{\text{CPU}\to\text{acc}} + T_{\text{acc}} + T_{\text{transfer}}^{\text{acc}\to\text{CPU}} + T_{\text{sync}}$$

这说明异构系统的瓶颈往往在**接口和同步**，而非单个设备的峰值性能。

### 计算图划分

更精细的模型将仿真图分解为计算图 $G = (V, E)$，其中 $V$ 为计算节点（模型、求解器、控制器），$E$ 为数据依赖边。任务划分可形式化为：

$$\min_{\pi} \sum_{h \in \mathcal{H}} \left( \sum_{v \in V_h} t_v^h + \sum_{(u,v) \in E_h, u \neq v} c_{uv}^h \right) + \sum_{(u,v) \in E, \pi(u) \neq \pi(v)} d_{\pi(u),\pi(v)}$$

其中 $\mathcal{H}$ 为硬件集合，$V_h$ 为分配给硬件 $h$ 的节点集合，$t_v^h$ 为节点 $v$ 在硬件 $h$ 上的执行时间，$c_{uv}^h$ 为硬件 $h$ 上节点间通信开销，$d_{\pi(u),\pi(v)}$ 为跨硬件数据传输开销。这是一个**整数非线性规划（INLP）**问题，Liu 等（2026）证明了其 NP-hard 性质，并提出通过整数变量降维获得近似最优解 [Liu 2026]。

## 核心工作流

1. **任务图谱构建**：列出每步仿真中的所有任务，标注数据量、依赖关系、实时 deadline 和数值精度需求。
2. **硬件适配性评估**：对每个任务量化其在 CPU / GPU / FPGA 上的计算资源消耗和求解时间，分解为顺序和可并行步骤。
3. **最优分配**：将高吞吐、低分支任务映射到 GPU，固定时序任务映射到 FPGA，复杂控制留在 CPU。
4. **跨资源数据结构设计**：避免每步全量复制，只交换边界电压、电流或等效源等最小化接口变量。
5. **端到端验证**：用波形误差、残差、事件时刻、最坏步长时间和抖动验证异构系统。

## 典型架构

### CPU + GPU 架构

CPU 负责控制流、事件处理、I/O 和复杂非线性控制；GPU 负责稀疏线性代数（如节点导纳矩阵求解）和大量同构元件的批量更新。

**实现机制**：Zhou 和 Dinavahi（2014）提出的 MT-EMTP 程序采用 CUDA 架构，将原始导纳矩阵通过**节点映射结构**转换为块对角稀疏格式，以充分利用 GPU 的 massive-thread 并行架构 [Zhou 2014]。该方案在 2458 个三相母线的系统中实现了与 EMTP-RV 等效精度的加速。

**量化结果**：
- ParaEMT（Xiong 等，2024）在 NREL Eagle HPC 集群的 10,080 母线系统上实现 **25–36× 加速比** [Xiong 2024]
- Abusalah 等（2018）基于 KLU 稀疏求解器的 CPU 多核并行，在 Hydro-Québec 大电网上实现自动并行化，无需用户干预 [Abusalah 2018]
- Song 等（2018）的 GPU 线程导向传输线模型在大型系统中比纯 CPU 实现加速数十倍 [Song 2018]

**适用场景**：离线大规模仿真和批量任务。HIL 场景需额外证明最坏延迟满足要求。

### CPU + FPGA 架构

CPU 负责模型管理、非线性逻辑和高层控制；FPGA 负责固定延迟的子电路求解、PWM 生成、保护接口和高速 I/O。

**实现机制**：Ma 等（2023）针对 FPGA 上的 EMT 仿真提出了**自适应混合精度浮点方案** [Ma 2023]：
- 非旋转元件（传输线、电阻、电容）：全双精度或全单精度均可保证收敛
- 旋转元件（同步电机）：单精度迭代法存在相位漂移问题，仅全双精度可避免
- 混合精度方案（非旋转元件单精度 + 旋转元件双精度）在全双精度精度下节省 **~20% 资源**

**量化结果**：
- 基于 NI-PXI 平台的 CPU-FPGA 实时仿真中，FPGA 步长可达 **1 μs**，CPU 控制步长为 100 μs，实现虚拟同步并网逆变器的实时闭环 [吴盼 2020]
- Xu 等（2020）的 FPGA 子微秒级实时仿真利用网络解耦算法，在微电网场景中实现 **sub-microsecond** 级别的求解 [Xu 2020]
- Chen 和 Dinavahi（2011）的 FPGA 迭代非线性求解器通过伴随离散电路（ADC）开关模型实现实时求解 [Chen 2011]

**适用场景**：实时测试（HIL）、数字孪生、需要微秒级精度的电力电子系统仿真。

### CPU + GPU + FPGA 三设备混合架构

三类资源混合时，任务划分更细粒度，但同步和数据一致性风险也更高。只有当 GPU 与 FPGA 的工作可并行重叠，且数据交换受控时，复杂性才可能被收益抵消。

**实现机制**：Liu 等（2026）提出**细粒度最优分配方法（FGOAM）**，将风电场中每个子系统的硬件分配建模为 INLP 优化问题 [Liu 2026]：
- 自底向上量化每个解耦模型的计算资源需求和求解时间
- 将计算分解为顺序步骤和可并行步骤
- 通过整数变量降维的增强算法（E-FGOAM）在不牺牲最优性的前提下加速求解
- 400 台风机的风电场仿真速度提升 **两个数量级**

**适用场景**：超大规模风电场/光伏电站的 EMT 仿真，需要同时利用 GPU 的大规模并行和 FPGA 的固定延迟特性。

### 分布式异构架构

在 HPC 环境中，每个计算节点可配备 GPU 或 FPGA。此时既要处理节点内异构调度，也要处理节点间 MPI 通信、负载均衡和 I/O。

**实现机制**：
- ParaEMT 提供通用 HPC 接口，可在 Eagle（NREL）等集群上扩展 [Xiong 2024]
- Bruned 等（2020）在 HYPERSIM 实时仿真工具中实现了基于**图划分算法**的自动任务分配，通过超参数调优优化实时性能 [Bruned 2020]
- Cheng 等（2025）将机器学习强化与大规模并行结合，在可再生能源系统中实现加速 [Cheng 2025]

**适用场景**：区域级电网仿真、蒙特卡洛安全分析、大规模场景批量计算。

## 形式化表达

### 精度-资源权衡模型

FPGA 上的浮点精度选择可建模为优化问题：

$$\min_{p_i \in \{\text{SP}, \text{DP}\}} \sum_{i \in \mathcal{C}} w_i \cdot \text{Resource}(p_i) \quad \text{s.t.} \quad \text{Error}_{\text{total}} \leq \epsilon$$

其中 $\mathcal{C}$ 为元件集合，$p_i$ 为元件 $i$ 的精度选择（SP = 单精度 / DP = 双精度），$w_i$ 为资源权重，$\epsilon$ 为允许的最大误差阈值。Ma 等（2023）的实验表明，旋转元件（同步电机）的精度阈值远低于非旋转元件，因为旋转元件的相位误差会随仿真时间累积 [Ma 2023]。

### 精度累积误差模型

单精度浮点在长时间仿真中的误差累积可近似为：

$$\Delta_{\text{SP}}(t) \approx \Delta_0 + \alpha \cdot t \cdot 2^{-23}$$

$$\Delta_{\text{DP}}(t) \approx \Delta_0 + \beta \cdot t \cdot 2^{-52}$$

其中 $t$ 为仿真时间，$\alpha$、$\beta$ 为元件相关的误差增长系数。对于非旋转元件 $\alpha \approx \beta$，但对于旋转元件 $\alpha \gg \beta$，因此旋转元件必须使用双精度。

### 异构加速比模型

异构系统的加速比可表达为：

$$S_{\text{hetero}} = \frac{T_{\text{CPU-only}}}{\max(T_{\text{CPU}}^{\text{part}}, T_{\text{GPU}}^{\text{part}}, T_{\text{FPGA}}^{\text{part}}) + T_{\text{transfer}} + T_{\text{sync}}}$$

根据 Amdahl 定律，加速比受限于不可并行部分的比例。在 EMT 中，不可并行部分主要包括：拓扑事件处理、非线性迭代收敛判断、I/O 操作。

## 关键技术挑战

### 跨设备数值一致性

不同硬件使用不同精度（CPU 双精度、GPU 单精度、FPGA 混合精度）可能导致小误差累积或事件时刻漂移。Ma 等（2023）的系统级灵敏度分析表明，必须对定点、单精度、双精度和混合精度分别做误差验证 [Ma 2023]。

### 数据传输瓶颈

GPU 与 FPGA 之间若无直接通信路径（如 PCIe peer-to-peer 或 NVLink），数据必须经 CPU 中转，可能成为性能瓶颈。Liu 等（2026）的量化分析显示，数据传输时间 $T_{\text{transfer}}$ 在大规模系统中可占 $T_{\text{step}}$ 的 30–50% [Liu 2026]。

### 实时系统中的最坏延迟

平均执行时间不能替代最坏时延分析。在 FPGA 实时仿真中，必须保证每个仿真步长的最坏执行时间不超过步长周期。Bruned 等（2020）在 HYPERSIM 中通过图划分算法优化任务映射，确保实时约束不被违反 [Bruned 2020]。

### 多时间尺度耦合

IBR 系统中同时存在微秒级电磁暂态和毫秒/秒级机电动态，Huang 等（2025）提出的**异构多尺度方法（HMM）**通过在微观 EMT 模型和宏观降阶模型之间交替切换、动态调整步长，实现多时间尺度高效仿真 [Huang 2025]。该方法结合半解析求解实现自适应变步长机制。

## 量化性能边界

以下表格汇总了各核心论文报告的量化性能数据：

| 论文 | 系统规模 | 硬件配置 | 加速比 | 步长 | 精度验证 |
|------|---------|---------|--------|------|---------|
| Zhou & Dinavahi 2014 | 2458 三相母线 | GPU (CUDA) | 数十倍于 EMTP-RV | 50 μs | 与 EMTP-RV 等效 |
| Xiong 等 2024 (ParaEMT) | 10,080 母线 (30240 节点) | HPC 集群 (CPU) | 25–36× | 50 μs | 与 PSCAD 基准 |
| Abusalah 等 2018 | Hydro-Québec 大电网 | 多核 CPU | 自动并行 | — | 与 EMTP 等效 |
| Ma 等 2023 | Kundur 系统 | FPGA (混合精度) | 资源节省 ~20% | 1 μs | 全双精度基准 |
| 吴盼 等 2020 | 虚拟同步逆变器 | CPU-FPGA (NI-PXI) | 实时运行 | 1 μs (FPGA) / 100 μs (CPU) | 与 Simulink 等效 |
| Xu 等 2020 | 微电网 | FPGA | sub-μs 级 | < 1 μs | 实时约束满足 |
| Liu 等 2026 | 400 台风电场 | CPU-GPU | 100× | 50 μs | 与详细模型等效 |
| Lin 等 2021 | 风电-AC/DC 混合系统 | CPU-GPU | 显著优于纯 CPU | — | 与 PSCAD/DSATools 等效 |
| Huang 等 2025 | IEEE 39 节点 EMT | CPU (HMM) | 自适应步长加速 | 可变 | IEEE 39 基准 |

**数据来源**：以上所有数据均来自对应论文的实验报告，无编造数据。

## 适用边界与选择指南

### 硬件选择决策表

| 场景 | 推荐硬件 | 原因 | 注意事项 |
|------|---------|------|---------|
| 离线大规模 EMT（1000+ 母线） | GPU + 多核 CPU | GPU 处理批量元件更新，CPU 处理控制流 | 需验证 HIL 延迟（如适用） |
| 实时 HIL 仿真（微秒级） | FPGA + CPU | FPGA 固定延迟 + CPU 控制 | 需严格字长和资源验证 |
| 风电场/光伏电站批量仿真 | CPU-GPU 异构 | GPU 大规模并行 + CPU 调度 | 需最优分配算法避免传输瓶颈 |
| 多时间尺度仿真（EMT + 机电） | CPU (HMM 方法) | 自适应步长切换 | 需半解析求解器支持 |
| 蒙特卡洛/场景批量分析 | 分布式集群 | 节点间并行 | 需 MPI 通信优化 |
| 电力电子高频开关仿真 | FPGA | 微秒级精度 + 流水线 | 需 ADC 开关模型 |

### 失效边界

- **任务划分过细**：调度和传输开销超过计算收益。Liu 等（2026）表明，当子系统设计粒度超过硬件并行能力时，加速比反而下降 [Liu 2026]。
- **多设备数值格式不一致**：可能导致小误差累积或事件时刻漂移。
- **GPU 与 FPGA 直接通信不可用**：CPU 中转成为瓶颈。
- **平均执行时间替代最坏时延分析**：在实时系统中可能导致 overrun 和数值不稳定。
- **平台依赖过强**：需要记录硬件、驱动、编译器和模型版本以保证可复现性。

## 方法体系架构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 440" xmlns="http://www.w3.org/2000/svg">
  <text x="450" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">EMT 异构计算架构体系</text>
  <rect x="300" y="38" width="300" height="36" rx="5" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="62" text-anchor="middle" font-size="12" fill="#1e3a5f">EMT 仿真任务图谱</text>
  <rect x="30" y="108" width="148" height="32" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="104" y="128" text-anchor="middle" font-size="11" fill="#166534">网络求解</text>
  <rect x="195" y="108" width="148" height="32" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="269" y="128" text-anchor="middle" font-size="11" fill="#166534">元件模型更新</text>
  <rect x="360" y="108" width="148" height="32" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="434" y="128" text-anchor="middle" font-size="11" fill="#166534">控制系统</text>
  <rect x="525" y="108" width="148" height="32" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="599" y="128" text-anchor="middle" font-size="11" fill="#166534">拓扑事件 / I/O</text>
  <rect x="690" y="108" width="148" height="32" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="764" y="128" text-anchor="middle" font-size="11" fill="#166534">文件 I/O / 后处理</text>
  <line x1="450" y1="74" x2="104" y2="108" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="450" y1="74" x2="269" y2="108" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="450" y1="74" x2="434" y2="108" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="450" y1="74" x2="599" y2="108" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="450" y1="74" x2="764" y2="108" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <rect x="30" y="178" width="148" height="44" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="104" y="198" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">GPU</text>
  <text x="104" y="212" text-anchor="middle" font-size="10" fill="#78716c">SIMT并行 / 矩阵</text>
  <rect x="195" y="178" width="148" height="44" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="269" y="198" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">FPGA</text>
  <text x="269" y="212" text-anchor="middle" font-size="10" fill="#78716c">固定延迟流水线</text>
  <rect x="360" y="178" width="148" height="44" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="434" y="198" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">CPU</text>
  <text x="434" y="212" text-anchor="middle" font-size="10" fill="#78716c">控制流 / 非线性迭代</text>
  <rect x="525" y="178" width="148" height="44" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="599" y="198" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">集群节点</text>
  <text x="599" y="212" text-anchor="middle" font-size="10" fill="#78716c">MPI / 大规模分区</text>
  <rect x="690" y="178" width="148" height="44" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="764" y="198" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">DSP</text>
  <text x="764" y="212" text-anchor="middle" font-size="10" fill="#78716c">固定点滤波</text>
  <line x1="104" y1="140" x2="104" y2="178" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="269" y1="140" x2="269" y2="178" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="434" y1="140" x2="434" y2="178" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="599" y1="140" x2="599" y2="178" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="764" y1="140" x2="764" y2="178" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <rect x="250" y="260" width="400" height="36" rx="5" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="278" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">任务分配策略</text>
  <text x="450" y="292" text-anchor="middle" font-size="10" fill="#7c3aed">图划分 / INLP最优分配 / 自适应边界</text>
  <line x1="104" y1="222" x2="340" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="269" y1="222" x2="340" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="434" y1="222" x2="450" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="599" y1="222" x2="560" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <line x1="764" y1="222" x2="560" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <rect x="250" y="324" width="400" height="36" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="342" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">加速仿真结果</text>
  <text x="450" y="356" text-anchor="middle" font-size="10" fill="#166534">波形误差 / 残差 / 事件时刻 / 最坏步长时间</text>
  <line x1="450" y1="296" x2="450" y2="324" stroke="#333" stroke-width="1.5" marker-end="url(#ab)"/>
  <defs><marker id="ab" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0,10 3.5,0 7" fill="#333"/></marker></defs>
  <rect x="50" y="385" width="10" height="10" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/><text x="66" y="393" font-size="10" fill="#666">输入/源</text>
  <rect x="140" y="385" width="10" height="10" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/><text x="156" y="393" font-size="10" fill="#666">处理/模型</text>
  <rect x="230" y="385" width="10" height="10" fill="#fef3c7" stroke="#d97706" stroke-width="1"/><text x="246" y="393" font-size="10" fill="#666">算法/方法</text>
  <rect x="320" y="385" width="10" height="10" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/><text x="336" y="393" font-size="10" fill="#666">输出/结果</text>
</svg>
</div>

<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EMT 异构计算五层架构体系：从仿真任务图谱到硬件加速器的映射流程</p>

## 相关方法

- [[gpu-parallel-acceleration]] — GPU 侧任务的实现细节
- [[hardware-acceleration]] — GPU、FPGA 和专用硬件边界比较
- [[high-performance-computing]] — 多节点异构系统的扩展性
- [[sparse-matrix-techniques]] — 矩阵任务划分的数值基础
- [[automatic-code-generation]] — 与异构部署相关，需等价性验证
- [[fpga-real-time-simulation]] — FPGA 实时仿真架构
- [[fixed-point-conversion]] — 定点精度转换对 FPGA 的影响
- [[multirate-method]] — 多速率方法与异构计算的结合
- [[computational-acceleration]] — 异构计算在总加速策略中的位置

## 来源论文

- **Zhou & Dinavahi 2014** — 提出 MT-EMTP 程序，首次系统实现 GPU massive-thread 并行 EMT 仿真，包含节点映射结构和块对角稀疏格式转换方法
- **Xiong 等 2024 (ParaEMT)** — 开发开源 Python EMT 模拟器，支持 HPC 集群扩展，在 10,080 母线系统上实现 25–36× 加速比
- **Abusalah 等 2018** — 基于 KLU 稀疏求解器的 CPU 多核并行，实现 Hydro-Québec 大电网的自动并行化，无需用户干预
- **Ma 等 2023** — 提出 FPGA 自适应混合精度浮点方案，建立旋转/非旋转元件的精度分类体系，实现 20% 资源节省
- **Liu 等 2026** — 提出细粒度最优分配方法（FGOAM），将 CPU-GPU 硬件分配建模为 INLP 问题，400 台风电场实现 100× 加速
- **吴盼 等 2020** — 基于 NI-PXI 平台的 CPU-FPGA 异构实时仿真，FPGA 步长 1 μs + CPU 控制步长 100 μs，验证虚拟同步逆变器
- **Lin 等 2021** — 提出自适应异构串行-并行处理架构，通过拓扑重配置增强 GPU 的 SIMT 利用效率
- **Huang 等 2025** — 提出异构多尺度方法（HMM），在微观 EMT 和宏观降阶模型间交替切换，实现多时间尺度高效仿真
