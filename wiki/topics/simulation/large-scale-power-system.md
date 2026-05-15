---
title: "大规模电力系统 (Large-Scale Power System)"
type: topic
tags: [large-scale, power-system, simulation, parallel-computing, network-equivalent]
created: "2026-05-02"
updated: "2026-05-16"
---

# 大规模电力系统 (Large-Scale Power System)

## 定义与边界

大规模电力系统指包含多区域交流网络、发电与负荷群、HVDC/FACTS、新能源电站、保护控制系统和通信/调度层的互联系统。其"大规模"来自**拓扑规模、模型细节、时间尺度、设备异质性和控制保护逻辑的共同作用**，而不是某个固定母线数量。

$$\mathcal{S}=(\mathcal{N},\mathcal{E},\mathcal{D},\mathcal{C})$$

其中 $\mathcal{N}$ 是母线和端口集合，$\mathcal{E}$ 是线路、变压器和开关支路，$\mathcal{D}$ 是发电机、换流器、负荷、滤波器和保护设备，$\mathcal{C}$ 是控制、通信和运行策略。EMT 模型需要说明哪些集合被详细建模，哪些被等值或聚合。

同一系统在不同任务中边界不同。规划研究关注外部网络强度和新能源接入容量；保护研究关注故障电流、测量链和动作时序；实时 HIL 关注控制硬件接口和 deadline；运行预演关注可重复工况和调度设定。

## EMT 中的角色

在大规模电力系统中，EMT 的价值在于**局部高频和非线性现象会影响系统级结论**：

- **多馈入 LCC-HVDC**：换相失败、恢复和直流功率转移需要微秒级精度 [[lcc-model]]
- **VSC/MMC/风电/光伏/储能**：弱网或故障中的快速相互作用需要详细开关模型 [[vsc-model]][[mmc-model]]
- **频率相关线路/电缆/变压器饱和**：对暂态电压电流的影响需要宽频建模 [[frequency-domain-analysis]][[cable-model]]
- **保护动作/控制限幅/通信延迟/HIL**：系统动态闭环影响需要硬件在环验证 [[hardware-in-loop]]

## 形式化表达

### 系统结构层级

大规模系统按区域、设备层级和时间尺度描述为四元组：

$$\mathcal{S}=(\mathcal{N},\mathcal{E},\mathcal{D},\mathcal{C})$$

- $\mathcal{N}$：母线和端口集合（$|\mathcal{N}|$ 可从 10 到数万）
- $\mathcal{E}$：线路、变压器和开关支路
- $\mathcal{D}$：发电机、换流器、负荷、滤波器和保护设备
- $\mathcal{C}$：控制、通信和运行策略

### 分区与接口变量

若把系统划分为区域 $\mathcal{S}_1,\ldots,\mathcal{S}_m$，接口变量为：

$$z_{ij} = [v_{ij},\, i_{ij},\, p_{ij},\, q_{ij}]^\mathsf{T}$$

其中 $v_{ij}$ 和 $i_{ij}$ 是区域间端口电压、电流，$p_{ij},q_{ij}$ 是功率或相量域变量。[[network-partitioning]] 和 [[interface-technique]] 决定这些变量如何交换、同步和验证。

### 动态方程组

大规模 EMT 系统可写为微分-代数方程组（DAE）：

$$\mathbf{f}(\dot{\mathbf{x}}, \mathbf{x}, \mathbf{y}) = \mathbf{0}$$

其中 $\mathbf{x} \in \mathbb{R}^{n_x}$ 是状态变量（发电机转子角、磁链、控制积分状态），$\mathbf{y} \in \mathbb{R}^{n_y}$ 是代数变量（节点电压、支路电流）。数值求解时每步需解大规模稀疏线性系统：

$$\mathbf{G}(\Delta t) \cdot \mathbf{y}^{(k+1)} = \mathbf{b}(\mathbf{x}^{(k)}, \mathbf{y}^{(k)}, \Delta t)$$

其中 $\mathbf{G}$ 是节点导纳矩阵的某种变形，维度为 $|\mathcal{N}| \times |\mathcal{N}|$，稀疏率通常 > 90%。

## 主要分支与机制

### 1. 分区协同仿真

#### EMT-Phasor 多速率协同

核心思想：按电气距离和频率内容分区，用不同步长求解各区。

- **快区**（故障附近、MMC-HVDC、电力电子）：EMT 步长 $\Delta t_{EMT} \in [1\mu s, 50\mu s]$
- **慢区**（远端交流网络）：动态相量/Phasor 步长 $\Delta t_{DP} \in [0.1ms, 5ms]$

**BFAST 接口**（Rupasinghe 2023）：在 EMT 与基频动态相量间自适应切换，重构式：

$$x(t-T+s) = \mathrm{Re}\left(\langle X \rangle_B(t) e^{j\omega_s(t-T+s)}\right)$$

其中 $\omega_s$ 是频移参数，$T=1/f_0$ 是基频周期。接口处用 Bergeron 传输线显式耦合：

$$h_M(t) = \frac{2v_K(t-\tau)}{Z_C} - h_K(t-\tau)$$

利用传播延时作为物理延时，避免额外一步计算滞后。

**MATE 接口**（Multi-Area Thévenin Equivalent）：各子系统先独立求局部解，TS 正序量插值转为三相接口量，再由戴维南等效计算联络支路电流：

$$I_\alpha = Z_\alpha^{-1} e_\alpha$$

注入接口节点完成同步耦合。

量化数据（Rupasinghe 2023, IEEE 118 改进系统）：
- 10s 仿真：全 EMT 耗时 1126s，EMT-Phasor 协同 88s，**加速比 ≈ 12.8×**
- 相对多速率纯 EMT 的 358s，**加速比 ≈ 4.1×**
- TS 步长 5ms，相对 10μs EMT 步长为 **500× 步长比**

#### SFA-EMT 多速率协同

**移频分析（SFA）**（Zhang 2024）：将电力系统变量表示为基频附近的复包络：

$$u(t) = u_I(t)\cos\omega_0 t - u_Q(t)\sin\omega_0 t$$

$$\Rightarrow U(t) = u_I(t) + ju_Q(t) \quad \text{（动态相量）}$$

将频谱按 $\omega_0$ 移至零频附近，使核心状态量变为"慢变化复包络"，可使用更大步长。SFA-EMT 混合框架用 MATE 思想组织接口：每个子系统在接口处形成多端口 Thévenin 等效，全局由各等效组合求连接支路电流。验证目标：数百至数千节点系统达到 **faster-than-real-time**。

**移频-动态相量（SFP）多速率**（Li 2020）：风电场保留 EMT 细节，大交流电网用 SFP 模型步长扩展到 500μs，通过 MD-TLM（移动窗口传输线模型）多速率接口在两个域间传递宽频带相互作用。适用于次/超同步相互作用（S2SI）场景：含固定串补、DFIG 风机和大规模交流电网的宽频带电磁暂态交互。

#### 完全动态相量内部多速率

**DP-Only 多速率**（多源文献综合）：在同一动态相量仿真器内部，只对最慢的发电机变量及其控制器放大步长，其余变量仍按常规 EMT 步长求解：

$$\Delta t_{slow} = k \cdot \Delta t_{fast}, \quad k \in [10, 100]$$

慢步长内慢变量通过插值驱动快方程，快变量在慢步长窗口内做平均驱动慢方程。慢步长末端计算不匹配量（mismatch），用于判断是否需要重算。

### 2. 并行计算加速

#### 空间并行（区域分解）

**网络分区**（Network Partitioning）：将大规模系统按电气耦合关系划分为若干区域，各区域可独立求解，通过接口变量交换同步。关键问题是分区边界选择：电气距离近的节点不应分属不同区域，避免接口变量交换频繁导致同步开销超过并行收益。

**区域等值**（Dynamic Equivalent）：外部系统用等值模型替代，仅保留端口特性。常用等值方法包括 [[network-equivalent]]（潮流等值）、[[fdne-model]]（频率相关网络等值）、[[dynamic-phasor]]（动态相量等值）。

#### 时间并行

**Parareal/MGRIT**：将时间区间分解为多个时间窗口，各窗口并行求解。适用于故障集扫描、长时段仿真（稳态小信号分析）。

#### 硬件并行

**GPU 并行**：利用数据并行（大量同类组件映射到 GPU 线程）和任务并行（不同组件计算/网络计算并发）加速 EMT 仿真（Song 2018, Zhang 2024）。GPU 并行面临电网拓扑导致的写冲突问题，需图结构驱动的线程安全设计。

**CPU 集群 MPI 并行**：Hydro-Québec EMT 软件的离线并行模式在 SGI NUMAlink 7、HPE Flex Grid Interconnect、Mellanox InfiniBand ConnectX-3 QDR/ConnectX-6 HDR 等不同通信架构上的扩展性评估。用 Karp-Flatt 指标诊断通信瓶颈：表观串行分数 $\sigma = \frac{1/p - T_{parallel}/T_{serial}}{1 - 1/p}$。

#### 实时移植

**离线→实时迁移**（Lessons Learned, Hydro-Québec）：从离线 EMTP 环境迁移到实时 HYPERSIM 环境，涉及模型库兼容、控制模块等价、用户代码重建、原理图修改和信号校核。工程实践要点：
1. 在实时工具中实例化对应电气与控制组件
2. 逐项迁移参数和连接
3. 对无直接等价物的离线组件，用基础模块合成或手写 UCM 实现
4. 信号检查和系统行为验证
5. 根据实时约束修改步长和调度

### 3. 大规模 HVDC 系统实时 HIL

**Nelson River 案例**（Hydro-Québec RTDS）：Manitoba Hydro Nelson River 三回双极 LCC-HVDC 系统（Bipole I/II/III）的实时 HIL 平台构建经验：

- **平台**：RTDS + PSCAD/EMTDC 离线模型 + 控制保护硬件副本
- **建模策略**：按 Pole/Bipole/双极逐级构建验证；用 RTDS 标准库页面模块重构控制；用标幺接口统一信号
- **关键发现**：Dorsey 站计算瓶颈处可选择同一网络组内降阶等效，避免接口变压器带来的一个实时步长延迟
- **验证**：以现场暂态故障录波（TFR）为基准，逐级比较直流电压、电流、触发角/控制响应波形
- **量化**：Bipole III 现场投运期间（2018 年 7 月）已接入 Bipole III 控制保护硬件副本用于 HIL 调试

### 4. 典型参数范围

| 参数 | 典型范围 |
|------|---------|
| EMT 步长 | $1\mu s \sim 100\mu s$ |
| Phasor/DP 步长 | $0.1ms \sim 5ms$ |
| 系统规模 | $10 \sim 10{,}000+$ 节点 |
| 仿真时长 | $0.1s \sim 10s$（稳态研究）/ $10s \sim 1000s$（机电暂态） |
| 电压等级 | $10kV \sim 500kV$ |
| 功率范围 | $1MW \sim 100{,}000MW$ |
| 频率 | $50Hz / 60Hz$ |

## 关键技术挑战

### 挑战 1：等值误差与保真度权衡

大规模系统通常需要 [[network-equivalent]] 或 [[fdne-model]]。等值后应报告保留端口、频带、扰动类型、控制状态和对照基准。

**常见等值方法对比**：

| 等值方法 | 保真度 | 计算成本 | 适用场景 |
|---------|-------|---------|---------|
| 潮流等值 | 低 | 极低 | 离线规划研究 |
| 频率相关等值（FDNE） | 高 | 中 | 谐波分析、宽频振荡 |
| 动态相量等值 | 中 | 中 | 机电暂态、稳定性研究 |
| 平均值模型（AVM） | 中 | 低 | 电力电子设备聚合 |

### 挑战 2：多区域耦合的接口误差

多区域耦合、低阻抗接口和快速控制闭环会**放大分区延迟与插值误差**。接口算法的选择直接影响整体仿真精度。

**接口方法对比**：

| 接口方法 | 延迟 | 精度 | 稳定性 |
|---------|------|------|--------|
| 固定 Thévenin 等值 | 1步 | 低 | 一般 |
| 时变 Thévenin 等值 | <1步 | 中 | 较好 |
| Bergeron 传输线 | 物理延时 | 高 | 好 |
| MATE 多端口等值 | <1步 | 高 | 好 |

### 挑战 3：大规模系统参数一致性

大规模系统的参数、控制逻辑和保护定值常来自不同来源。**版本不一致会导致看似数值问题的模型错误**。建议：
- 建立参数溯源体系，记录每个参数来自哪个设计文件/测量数据
- 版本对比工具检测参数漂移
- 控制和保护逻辑的等值需保留限幅、滞环等非线性特性

### 挑战 4：实时约束下的模型简化

实时 HIL 要求每个步长在 deadline 内完成。模型简化时需权衡：
- **精度损失**：简化模型可能丢失高频动态或控制限幅细节
- **实时 Deadline**：步长内必须完成所有计算+通信
- **HIL 同步**：与真实硬件互联时需保证通信延迟可控

### 挑战 5：验证与数据管理

输出数据量、故障集和长时段仿真可能成为验证瓶颈。只保存少量波形会限制事后审计。

**验证建议**：
- 保留关键节点的全时段波形数据
- 分层验证：先验知识（理论极限）→小系统基准→大规模扩展
- 建立故障集标准库，覆盖 N-1/N-2 故障类型

## 量化性能边界

| 性能指标 | 典型值 | 来源 |
|---------|--------|------|
| EMT-Phasor 协同加速比 | 12.8×（10s仿真，118节点） | Rupasinghe 2023 |
| 多速率 vs 全 EMT | 4.07× | Rupasinghe 2023 |
| SFA GPU 实时能力 | 数百至数千节点 | Zhang 2024 |
| MPI 并行效率（InfiniBand） | 随进程数增加而下降，Karp-Flatt 指标诊断 | Hydro-Québec 通信评估 |
| Nelson River RTDS 平台 | 已实际投运（2018） | Hydro-Québec |

## 适用边界与选择指南

| 仿真目标 | 推荐方法 | 步长范围 |
|---------|---------|---------|
| 换相失败/故障瞬态 | 全 EMT 或 EMT-Phasor 协同（高频区用 EMT） | $1\sim50\mu s$ |
| 次/超同步振荡（S2SI） | SFP-EMT 多速率或 DP-Only 多速率 | $10\sim500\mu s$ |
| 机电暂态稳定性 | Phasor/TS 或 DP-Only 多速率 | $1\sim10ms$ |
| 谐波/宽频振荡分析 | FDNE 或 EMT-Phasor 协同（谐波区用 EMT） | $10\sim100\mu s$ |
| 实时 HIL | 离线→实时移植，分区并行 | 按实时平台定 |
| 长时段工频稳态 | DP-Only 多速率 | $5\sim50ms$ |

**方法选择决策树**：

```
仿真目标？
├─ 需捕捉开关细节/故障瞬态 → 全 EMT 或 EMT-Phasor 协同
├─ 宽频振荡/谐波分析 → FDNE + Phasor 分区
├─ 机电+电磁多尺度 → DP-Only 多速率 或 SFA-EMT 协同
└─ 实时 HIL / 快速扫描 → 区域并行 + 模型降阶
    ├─ 实时 Deadline 严格 → 子系统降阶等值
    └─ 精度要求高 → MATE 接口 + 时变 Thévenin
```

## 相关方法与模型

- [[large-scale-grid-simulation]]：从仿真任务角度组织大规模系统
- [[large-scale-hybrid-acdc-simulation]]：聚焦 AC/DC、HVDC、VSC 和 MMC 耦合场景
- [[network-equivalent]]：外部系统等值方法
- [[fdne-model]]：频率相关端口等值
- [[dynamic-phasor]]：动态相量建模
- [[network-partitioning]]：系统分区方法
- [[interface-technique]]：接口同步技术
- [[hardware-in-loop]]：硬件在环仿真
- [[parallel-computing]]：并行计算技术
- [[multirate-method]]：多速率仿真
- [[hil-simulation]]：HIL 仿真边界
- [[dispatch-operation]]：运行点与调度设定来源

## 来源论文

- [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Zhang 等 2024]] — SFA+GPU LB-LMC 并行框架，faster-than-real-time 能力验证
- [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|Rupasinghe 等 2023]] — 多求解器协同仿真框架，12.8×加速比（118节点）
- [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|Li 等 2020]] — SFP-EMT 多速率，500μs 步长适用于次同步振荡研究
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Hydro-Québec RTDS 团队]] — Nelson River LCC-HVDC 实时 HIL 平台构建经验
- [[performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn|Hydro-Québec]] — MPI 并行离线 EMT 在不同通信架构上的性能评估，Karp-Flatt 指标
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Hydro-Québec]] — 离线→实时模型移植流程，工程实践检查表
- [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems]] — DP-Only 多速率仿真，慢变量插值驱动快方程机制
- [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems]] — SFA-EMT 多速率，MATE 接口协议设计
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]] — MMC-MTDC 与大交流系统多速率协同仿真框架