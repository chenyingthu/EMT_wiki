---
title: "调度运行 (Dispatch Operation)"
type: topic
tags: [dispatch, operation, control-center, scada, ems, power-grid, faster-than-real-time, digital-twin, dynamic-security, co-simulation, real-time-simulation]
created: "2026-05-02"
updated: "2026-05-14"
---

# 调度运行 (Dispatch Operation)

## 定义

调度运行是电力系统运行控制中的计划、监视、校核和再调度活动，核心对象是发电、负荷、输电约束、备用、无功电压和运行风险。它不是 EMT 仿真方法，也不是单一优化算法；[[power-flow-calculation]]、[[optimal-power-flow]]、[[economic-dispatch]] 和安全稳定校核只是调度运行中的分析工具。

在 EMT 语境下，调度运行与电磁暂态仿真的关系可以概括为：**调度提供运行方式和扰动场景，EMT 校验这些场景下的暂态安全性**。调度运行工作在秒级到小时级的慢时间尺度，而 EMT 仿真工作在微秒到秒级的快时间尺度。二者之间的接口——如何将调度结论映射为 EMT 场景、如何将 EMT 结果反馈为调度约束——是本页的核心主题。

$$
\mathcal{S}_{\mathrm{EMT}} = G(P_G, Q_G, P_L, Q_L, V, \theta, c, \mathcal{D})
$$

其中 $P_G, Q_G$ 表示发电和无功设定，$P_L, Q_L$ 表示负荷，$V, \theta$ 表示潮流初值，$c$ 表示控制和保护定值，$\mathcal{D}$ 表示故障或扰动集合。EMT 校核的是 $\mathcal{S}_{\mathrm{EMT}}$ 下的暂态响应；它不能直接给出调度优化目标或市场结算结果。

## EMT 中的角色

调度运行与 EMT 仿真的接口体现在三个方向：

**（1）调度 → EMT：运行场景注入。** 调度给出运行方式、潮流断面、机组出力、HVDC 功率指令、无功补偿状态和新能源出力场景，作为 EMT 初始条件和扰动集合。Cao 等 (2023) 在 6 个 ACTIVSg 500-bus 交流系统加 6 端直流网的混合系统中，将数百个 N-1/N-2 故障场景注入混合 TS-EMT 仿真平台，验证了大规模故障扫描在超实时硬件上的可行性 [1]。

**（2）EMT → 调度：暂态安全边界反馈。** EMT 检查运行方式下的换流器控制交互、保护动作、故障穿越、暂态过电压和宽频振荡风险，结果可反馈为运行约束或校核规则。Kuranage 等 (2023) 展示了 EMT 仿真如何嵌入优化循环，通过筛选对最优解影响不大的变量降低优化维度，使 EMT 从被动评价器变为可批量调用的主动设计工具 [2]。

**（3）实时/超实时接口：在线预演与数字孪生。** [[real-time-simulation]] 和 [[hil-simulation]] 可用于调度员培训、保护控制闭环演练和 WAMPAC 类应用。Le-Huy 等 (2023) 总结了 Hydro-Québec 将大规模离线 EMT 模型移植到实时 HYPERSIM 环境的经验，指出模型兼容、控制模块和信号校核是 WAMPAC 与调度支撑应用的关键证据边界 [3]。

## 主要分支与机制

### 经济与安全调度

以成本、备用、输电限额和安全约束为主，常依赖 [[economic-dispatch]]、[[optimal-power-flow]] 和 N-1 校核。它们通常不表示开关暂态和相域不平衡。当新能源渗透率升高时，传统正序安全约束最优潮流 (SCOPF) 无法覆盖换流失败、保护误动、暂态过电压等快速电磁过程，必须引入 EMT 或超实时仿真进行补充校核。

### 动态安全评估 (DSA)

把 [[transient-stability-analysis]]、小信号振荡、电压稳定和频率安全作为调度约束来源。是否需要 EMT 取决于电力电子渗透率、保护判据和暂态对象。Cao 等 (2023) 在大规模 AC/DC 系统中采用多 FPGA 超实时硬件仿真平台，交流侧用暂态稳定模型、直流侧用 EMT 模型，通过动态电压注入接口耦合两种时间尺度，在低硬件延迟下完成大规模故障扫描 [1]。

### 新能源与储能调度

处理预测误差、爬坡、备用和电压支撑。若控制器、PLL、限流器或构网控制行为影响安全边界，应与 [[renewable-energy-integration]]、[[gfl-inverter-model]]、[[gfm-inverter-model]] 的 EMT 模型联动。Zhang 等 (2024) 基于移频分析 (SFA) 在 GPU 上实现了超实时电力系统仿真，将 SFA 用于 EMT 类系统建模以平衡负载与精度，并通过 LB-LMC 并行化框架将组件计算与网络求解组织为适合 GPU 的数据并行和任务并行执行 [4]。

### 调度培训与在线预演

通过离线仿真、超实时仿真或实时 HIL 演练事故处置。Scheibe 等 (2022) 给出了 RTDS Novacor (实时 EMT) 与 PSS/E (离线 RMS) 之间的两种接口方案：基于以太网 UDP 的纯软件方案和基于 FPGA + Aurora 光纤协议的硬件方案，说明了瞬时值—相量—正序量转换、步长匹配和电气接口耦合的实现流程 [5]。

## 形式化表达

### 1. 调度-EMT 场景映射

调度运行与 EMT 的接口可形式化为从慢时间尺度运行点到快时间尺度暂态场景的映射：

$$
\mathcal{S}_{\mathrm{EMT}} = G(P_G, Q_G, P_L, Q_L, V, \theta, c, \mathcal{D})
$$

其中 $G(\cdot)$ 为 EMT 仿真算子，输入为调度给定的运行点参数和扰动集合 $\mathcal{D}$，输出为暂态响应波形。EMT 校核的是 $\mathcal{S}_{\mathrm{EMT}}$ 下的暂态安全性，其判据包括：

- 换流器电流是否超出限幅：$|i_{conv}(t)| \leq I_{\max}$
- 母线电压是否在安全范围内：$V_{\min} \leq |V_{bus}(t)| \leq V_{\max}$
- 频率偏差是否可接受：$|\Delta f(t)| \leq \Delta f_{\max}$

### 2. 混合时间尺度耦合

当调度运行涉及交直流混合系统时，需采用多速率或混合仿真方法。Rupasinghe 等 (2023) 提出的多求解器框架按扰动电气距离划分网络域：

$$
x_{fast}(t) = A_{fast} x_{fast}(t) + B_{fast} u_{fast}(t) + K_{interface}(x_{slow}, u_{slow})
$$

$$
x_{slow}(t) = A_{slow} x_{slow}(t) + B_{slow} u_{slow}(t) + J_{interface}(x_{fast}, u_{fast})
$$

其中 $K_{interface}$ 和 $J_{interface}$ 为跨尺度接口算子，负责在 EMT 子系统和 TS 子系统之间交换边界量 [6]。

### 3. 超实时加速比模型

超实时仿真的核心指标是加速比 (Speedup Ratio)：

$$
SR = \frac{T_{sim}}{T_{real}}
$$

其中 $T_{sim}$ 为仿真时长，$T_{real}$ 为实际计算时间。Cao 等 (2023) 在微电网群—交流主网系统中实现了 51 倍超实时运行 [7]；在 SSCI 阻尼应用中实现了 122 倍超实时推演 [8]。Zhang 等 (2024) 基于 GPU + SFA 的仿真加速比可达数十倍至百倍量级 [4]。

### 4. 数字孪生一致性约束

数字孪生用于在线调度决策时，虚拟模型必须满足实时一致性：

$$
\| y_{virtual}(t) - y_{physical}(t) \|_2 \leq \epsilon_{tol}
$$

其中 $y_{virtual}$ 为孪生模型输出，$y_{physical}$ 为物理系统实测值，$\epsilon_{tol}$ 为可接受误差阈值。Huang 等 (2023) 提出的全纯嵌入模型 (HEM) 通过收敛半径模型 (CRM) 判断模型有效时间范围，以支撑实时仿真步长选择 [9]。

## 关键技术挑战

### 挑战 1：时间尺度鸿沟

调度运行（秒～小时）与 EMT 仿真（微秒～秒）之间存在 6-9 个数量级的时间尺度差异。直接全 EMT 仿真无法在调度时间窗口内完成大量故障场景扫描。解决方案包括：多速率仿真（同一动态相量表示下放大最慢变量步长 [10]）、混合仿真（EMT-TS 分区 [6]）、以及移频分析（SFA）放宽计算负担 [4]。

### 挑战 2：模型移植与一致性

将离线 EMT 模型移植到实时 HIL 环境时，软件接口、组件替换、控制模块重构和信号校核是专家密集型任务。Le-Huy 等 (2023) 总结了 Hydro-Québec 的移植经验，指出无直接等价元件的内部控制模块重建、波形比较验证和实时性能评估是三大关键步骤 [3]。

### 挑战 3：新能源不确定性

高比例新能源接入后，预测误差、控制限幅、保护动作和 EMT 模型不确定性共同影响调度决策可靠性。Kuranage 等 (2023) 提出通过变量筛选降低优化维度，结合混合优化算法与并行处理来应对新能源参数不确定性 [2]。

### 挑战 4：硬件资源与通信延迟

FPGA 超实时仿真虽然计算速度快，但硬件资源有限、通信延迟和分区负载不均会限制系统规模。Multi-FPGA 设计中，按元件功能类型而非地理/拓扑区域聚类（功能分解），把同类模型放到专用处理硬件上并行流水线执行，可在不插入额外分区元件的前提下保持原始系统连接关系 [11]。

### 挑战 5：接口数值稳定性

混合仿真中，EMT 子系统和 TS 子系统之间的接口耦合是数值稳定性的关键。Rupasinghe 等 (2023) 的多求解器框架采用 BFAST（基频动态相量自适应切换）机制，通过基频动态相量重构式 $x(t-T+s)$ 在 EMT 与基频动态相量间自适应切换 [6]。Chagas 和 Tomim (2022) 则采用基于行波理论的虚构传输线接口，用历史项交换替代即时端口耦合，避免了代数环 [12]。

## 量化性能边界

| 来源 | 系统规模 | 方法 | 加速比 | 精度/验证 |
|------|---------|------|--------|----------|
| Cao 等 (2023) [1] | 6×500-bus AC + 6-terminal DC | 多 FPGA 混合 TS-EMT | 超实时（SCADA 尺度内） | 数百个 N-1/N-2 故障场景扫描 |
| Cao 等 (2023) [7] | 微电网群 + 交流主网 | FPGA 混合仿真 | 51× 超实时 | 光伏/DFIG/BESS 组件级 EMT 模型 |
| Zhang 等 (2024) [4] | 大规模电力系统 | GPU + SFA + LB-LMC | 数十至百倍 | GPU 线程安全设计，编译期异构转换 |
| 光伏 SSCI 阻尼 [8] | 400 MW PV + IEEE 39 + 4-terminal HVDC | FPGA 混合 EM-TS | 122× 超实时 | SSCI 检测与有功/无功控制动作 |
| Huang 等 (2023) [9] | 电-气-热多能网 | 全纯嵌入模型 (HEM) | 实时（收敛半径内） | PDE 管网动态转化为代数递推 |
| Le-Huy 等 (2023) [3] | Hydro-Québec 大规模系统 | 离线→实时 HIL 移植 | — | 软件接口、模型替换、波形比较流程 |
| Scheibe 等 (2022) [5] | RTDS + PSS/E | UDP/FPGA 混合接口 | 实时 | 瞬时值—相量—正序量转换 |
| Chen 等 (2023) [13] | DFIG 风电系统 | FPGA 数字孪生 IP 核 | 超实时 | 虚拟电容等效法实现定转子解耦 |
| Wang 等 (2026) [14] | 新能源组件级系统 | GPU + GLIM 细粒度并行 | 高并行度 | 蛙跳格式节点/支路交错更新 |

## 适用边界与选择指南

### 场景-方法决策表

| 应用场景 | 推荐方法 | 原因 | 不适用场景 |
|---------|---------|------|----------|
| 大规模 N-1/N-2 故障扫描 | 多 FPGA 混合 TS-EMT | 交流侧 TS 加速、直流侧 EMT 精度 | 纯交流系统（无需 EMT） |
| 微电网群扰动预演 | FPGA 混合仿真 (51×) | 微电网 EMT 详细模型 + 主网 TS | 单微电网（无需混合） |
| 新能源控制参数优化 | EMT + 并行优化循环 | EMT 从被动评价器变为主动设计工具 | 参数少且解析模型可用 |
| 在线动态安全评估 | 灵活步长动态仿真 + EMT | AC 侧灵活步长 + DC 侧 EMT | 纯交流系统 |
| 实时 HIL 培训 | 离线→实时 HIL 移植 | 成熟移植流程 + 波形比较验证 | 非关键设备 |
| 交直流混合系统接口 | UDP/FPGA 双接口 | 软件灵活 + 硬件实时 | 纯 RMS 研究 |
| 大规模系统超实时 | GPU + SFA | 组件并行 + 编��期异构转换 | 高频暂态需精确波形 |
| 多能网数字孪生 | 全纯嵌入模型 (HEM) | PDE→代数递推，收敛半径内实时 | 超出收敛半径 |

### 调度-EMT 联合工作流

```
调度运行点 → 潮流计算 → EMT 初始条件
    → 扰动集合 D 生成 → EMT 仿真 → 暂态波形
    → 安全判据检查 → 通过 → 调度决策
    → 不通过 → 约束更新 → 重新调度
```

## 相关方法 / 相关主题

- [[emt-simulation]] — EMT 仿真基础
- [[real-time-simulation]] — 实时仿真技术
- [[hil-simulation]] — 硬件在环仿真
- [[power-flow-calculation]] — 稳态潮流计算
- [[optimal-power-flow]] — 最优潮流
- [[economic-dispatch]] — 经济调度
- [[transient-stability-analysis]] — 暂态稳定分析
- [[co-simulation]] — 混合仿真
- [[multirate-method]] — 多速率方法
- [[shifted-frequency-analysis]] — 移频分析
- [[renewable-energy-integration]] — 新能源并网
- [[gfl-inverter-model]] — 跟网型逆变器模型
- [[gfm-inverter-model]] — 构网型逆变器模型
- [[power-system]] — 电力系统建模
- [[electromagnetic-transient]] — 电磁暂态分析
- [[control-system]] — 控制系统设计

## 来源论文

[1] Cao 等 (2023) — *Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of Large-Scale AC/DC Systems*：多 FPGA 超实时硬件仿真平台，混合 TS-EMT 建模，数百个 N-1/N-2 故障场景扫描

[2] Kuranage 等 (2023) — *Improved Methods for Optimization of Power Systems with Renewable Generation Using Electromagnetic Transient Simulation*：EMT 嵌入优化循环，变量筛选降低维度，混合优化算法与并行处理

[3] Le-Huy 等 (2023) — *Lessons Learned in Porting Offline Large-Scale Power System Simulation to Real-Time for Wide-Area Monitoring, Protection, and Control*：Hydro-Québec 大规模离线 EMT 到实时 HIL 移植经验，软件接口、模型替换、波形比较

[4] Zhang 等 (2024) — *Shifted Frequency Analysis Based, Faster-Than-Real-Time Simulation of Power Systems on Graphics Processors*：GPU + SFA 超实时仿真，LB-LMC 并行化，图结构驱动线程安全设计

[5] Scheibe 等 (2022) — *Interfacing Real-Time and Offline Power System Simulation Tools Using UDP or FPGA Systems*：RTDS Novacor + PSS/E 两种接口方案（UDP 软件 / FPGA Aurora 硬件），瞬时值—相量—正序量转换

[6] Rupasinghe 等 (2023) — *A Multi-Solver Framework for Co-Simulation of Transients in Modern Power Systems*：按电气距离划分网络域的多求解器框架（EMT1/EMT2/BFAST/DP/TS），BFAST 自适应切换机制

[7] Cao 等 (2023) — *Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids*：微电网群—交流主网 FPGA 混合仿真，51× 超实时，组件级 EMT 模型

[8] *Damping of Subsynchronous Control Interactions in Large-Scale PV Installations Through Faster-Than-Real-Time Dynamic Emulation*：400 MW 光伏 + IEEE 39 + 4-terminal HVDC，122× 超实时 SSCI 阻尼

[9] Huang 等 (2023) — *Digital Twins of Multiple Energy Networks Based on Real-Time Simulation Using Holomorphic Embedding*：电-气-热多能网数字孪生，全纯嵌入模型 (HEM)，收敛半径模型 (CRM)

[10] Liu 等 (2026) — *Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation*：风电场解耦模型最优分配，CPU-GPU 并行 EMT 仿真

[11] *Multi-FPGA Digital Hardware Design for Detailed Large-Scale Real-Time Electromagnetic Transient Simulation of Power Systems*：多 FPGA 功能分解设计，按元件功能类型聚类，3-FPGA/10-FPGA 实时验证

[12] Chagas 和 Tomim (2022) — *Co-Simulation Applied to Power Systems with High Penetration of Distributed Energy Resources*：FMI/FMU + 行波理论虚构传输线接口，OpenModelica + OpenDSS 联合仿真

[13] Chen 等 (2023) — *Faster-Than-Real-Time Simulation of Stator-Rotor Decoupling Digital Twin of Doubly-Fed Induction Generator*：DFIG 虚拟电容等效法实现定转子解耦，纯 Verilog FPGA IP 核

[14] Wang 等 (2026) — *A Component-Level Modeling and Fine-Grained Simulation Method for Renewable Energy Power Systems Suitable for GPU*：GLIM 细粒度并行建模，蛙跳格式节点/支路交错更新

[15] *Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for Faster-Than-SCADA Applications*：FPGA 并行硬件上构建 FT-SCADA/FT-RT 框架，AC 侧灵活步长动态仿真 + DC 侧 EMT，功率—电压接口
