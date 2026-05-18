---
title: "硬件在环仿真 (HIL Simulation)"
type: topic
tags: [hil, real-time, simulation, hardware, testing, controller-validation]
created: "2026-05-02"
updated: "2026-05-18"
---

# 硬件在环仿真 (HIL Simulation)

## 定义与边界

硬件在环仿真（Hardware-in-the-Loop, HIL）是把真实控制器、保护装置、功率设备或通信设备接入实时仿真闭环的测试方法。仿真器提供被控电力系统或设备模型，硬件通过模拟量、数字量、通信或功率接口交换信号。

HIL 有三类核心接口形式：

| 接口类型 | 信号形式 | 典型应用 | 实时约束 |
|---------|---------|---------|---------|
| 控制器 HIL（CHIL） | 模拟量/数字量/I/O | 控制保护算法验证 | I/O 延迟 < 1 μs |
| 功率 HIL（PHIL） | 功率放大器 output | MMC/换流器功率回路测试 | 功放带宽 > 10 kHz |
| 快速控制原型（RCP） | 直接 PWM/触发信号 | 算法快速迭代 | 步长 < 5 μs |

本页关注 EMT 语境下 HIL 的模型、接口和证据边界。它不同于纯软件 [[co-simulation]]，也不同于只追求离线加速的快速仿真。HIL 的核心约束是：**闭环可实时**、**接口语义一致**、**被测硬件看到的信号可信**。

## EMT 中的作用

HIL 让控制保护硬件在投运前经历可重复、可注入故障且风险可控的 EMT 场景，常见用途包括：

- HVDC、FACTS、MMC、VSC 和新能源控制保护系统的动态性能测试（DPS）。
- 继电保护装置在交流故障、直流故障、互感器饱和或通信条件变化下的闭环验证——包括工厂验收测试（FAT）和预投运测试（Pre-commissioning）。
- [[wide-area-monitoring-protection]]、通信仿真器和真实 IED 的联合测试。
- 大型离线 EMT 模型迁移到 [[real-time-simulation]] 平台后的信号、波形和 deadline 校核。

HIL 相比纯离线仿真的本质优势在于：**覆盖真实控制硬件的采样、处理、通信和动作协调链路**，这些环节在离线模型中通常被简化或忽略。

## 主要分支与机制

### 控制器 HIL（Controller HIL）

控制器 HIL 中真实硬件只处理测量、控制和保护逻辑，功率系统由实时 EMT 或 RMS-EMT 模型表示。基本闭环方程为：

$$
y_k = H(x_k) + \eta_k, \qquad u_k = C_{\mathrm{hw}}(y_{k-d}), \qquad x_{k+1} = F(x_k, u_k)
$$

其中 $x_k$ 是仿真模型状态，$y_k$ 是传给硬件的测量量，$u_k$ 是硬件输出控制量，$d$ 表示采样、转换、通信和处理形成的等效延迟步数，$\eta_k$ 为量测噪声。$d$、量程、采样率、滤波和信号方向的显式说明是 HIL 接口规范的核心。

以 Le-Huy & Tremblay（2023）中 Hydro-Québec La Vérendrye 735 kV 混合 SVC-VSC 为例：RTDS 实时仿真器（RTS）通过光纤接口（FO）连接 MMC 仿真器 MMCsim，MMCsim 再通过 FO 与主控制系统（MMS）交换等效电压/电流信号。MMCsim 的刷新率为每周期 512 点（周期 $T = 32.5521\,\mu\text{s}$），MMCsim 接收来自 RTS 的桥臂等效电压 $V_{\text{On}}$ 和 $V_{\text{Block}}$，同时将桥臂电流回传给 RTS，构成闭环。

控制器 HIL 验证的核心证据包括：测量量与参考电压偏差、控制输出 PWM 占空比、保护动作逻辑序列。**两步验证策略**：制造商在 FAT 阶段使用小步长（$t_s < 5\,\mu\text{s}$）RT EMT，研究所预投运阶段使用常规步长（$t_s > 20\,\mu\text{s}$），两者在"权宜处理"（开关等效、接口刷新、MMC 等效）被显式纳入模型后结果一致。

### 功率 HIL（Power HIL, PHIL）

功率 HIL 让实际功率设备通过功率放大器或变流器接入仿真环境。接口稳定性通常比控制器 HIL 更敏感，因为功率放大器带宽、延迟、输出阻抗和被测设备动态共同进入闭环。最低限度应检查：

- **接口注入功率**：功放输出功率与 EMT 模型接口功率的匹配。
- **阻抗匹配**：功放输出阻抗与被测设备输入阻抗的共轭匹配。
- **延迟补偿**：功放带宽限制引入的延迟必须在上游 EMT 模型中补偿，否则会导致非物理振荡。
- **故障时饱和/限流行为**：故障穿越时功放限流可能导致控制保护动作与纯仿真不一致。

### 含宽禁带器件的功率 HIL（WBG PHIL）

宽禁带（Wide-Bandgap, WBG）器件——GaN HEMT 和 SiC IGBT——的开关瞬态在纳秒级（< 1 μs 甚至低至 50 ns），传统物理非线性模型计算量大，固定步长 EMT 算法在实时 FPGA 上产生过多计算负担。Zhang 等（2023）提出的解决方案是**分层 HIL 框架**：

- **系统层**：用传输线模型法（TLM）将直流铁路微电网（DRM）分区并行化，结合 GRU（门控循环单元）与 EMT 处理子系统。
- **器件层**：提出物理特征神经网络（PFNN），让网络预测波形中的物理特征点而非固定间隔全采样点，再通过插值重构高分辨率瞬态，从而服务于 FPGA 实时硬件仿真。

TLM 接口方程（以节点 $i$ 为例）：

$$
i_{k+1}^i = \frac{2}{Z_i} v_k^i + i_k^i, \qquad v_{k+1}^i = Z_i i_{k+1}^i + v_k^i
$$

其中 $n$ 为序列长度，$v$ 和 $i$ 分别为子系统端口电压和电流。TLM 将 DRM 划分为 AC-变压器-整流子系统（ACTRS）、直流铁路子系统、储能子系统和隔离 DC/DC（IDCDC）变换器，并行计算。

**PFNN 关键结果**（Zhang 2023）：步长可低至 **1 ns**，系统级 EMT 步长为 $10\,\mu\text{s}$，PFNN 预测波形与 SaberRD 离线仿真结果吻合，误差 < 2%。

### 混合 DCCB 控制器 HIL

Rault 等（2020）构建了含 MMC 换流站、混合式高压直流断路器及其工业控制保护硬件的三端 HVDC 网 HIL 平台。混合 DCCB 模型的实时化核心是：

- 将离线详细阀级模型（含非线性半导体特性、杂散电感/电容）转换为可实时运行的等效模型。
- 向控制器提供电流、电压、开关位置/状态等测量/反馈量。
- 接收控制器输出的分闸、合闸、闭锁、触发等数字命令。

**DCCB HIL 接口数据**：三端直流网，含 1 个 MMC 换流站和 **12 个 DCCB**，工业 DCCB 控制器与换流器控制器均接入 HIL 平台。测试场景包括电缆充电（energization）和故障清除（fault clearance）。HIL 平台可验证：控制调参、控制与保护全流程链（采集、处理时间、独立控制器间协调）、离线研究无法覆盖的动态范围。

### 多速率 RTDS-FPGA 联合实时 HIL

对于含电力电子设备的电力系统，多速率仿真是解决计算规模与实时性矛盾的关键方法。RTDS 利用传输线接口的自然延迟特性实现快慢系统之间的并行计算，将分布式发电系统从大电网中独立出来（牺牲部分精度换取接口稳定性）。FPGA 的仿真步长能达到**几百纳秒甚至几十纳秒**，编程灵活且具有成本优势。

多速率实时仿真的核心挑战在于：慢速系统（电磁暂态网络）和快速系统（电力电子开关）之间的数据交互延迟和接口一致性。常用策略：

1. **传输线模型法（TLM）接口**：利用传输线的自然延迟特性实现子系统间的自耦解耦，无需迭代即可保证接口电压/电流的物理一致性。
2. **变量分组多速率**：快慢变量采用不同步长（如 $t_{\text{fast}} = 1\,\mu\text{s}$，$t_{\text{slow}} = 50\,\mu\text{s}$），通过事件检测和异步重同步管理子系统间交互。

### 大型系统混合实时 HIL

大型 HVDC 或 WAMPAC 平台往往同时包含软件化旧控制、真实新控制硬件和详细 AC/DC 网络。典型流程：

1. **模块化分层构建**：将系统按 Pole、Bipole、双极逐级构建和验证（如 Manitoba Hydro Nelson River 三回双极 LCC-HVDC，Bipole I/II 运行 40+ 年）。
2. **遗留控制处理**：老式模拟逻辑、极间和双极间差异在实时模型中等效为标幺接口信号。
3. **计算瓶颈处理**：同网络组内降阶等效（如 Dorsey 站多逆变器、阀组和同步调相机汇聚处）。
4. **硬件副本接入**：控制保护硬件副本与 RTDS 软件化模型闭环，完成预投运验证。

## 形式化表达

### 实时约束不等式

实时性必须以最坏步长时间和抖动判断：

$$
T_{\mathrm{solve}} + T_{\mathrm{io}} + T_{\mathrm{comm}} + T_{\mathrm{hw}} \le \Delta t
$$

其中 $\Delta t$ 是实时步长，$T_{\mathrm{solve}}$ 为 EMT 求解时间，$T_{\mathrm{io}}$ 为 I/O 接口时间，$T_{\mathrm{comm}}$ 为通信延迟，$T_{\mathrm{hw}}$ 为硬件响应或控制处理进入闭环的等效时间。

### 控制器 HIL 闭环方程

$$
\begin{aligned}
y_k &= H(x_k) + \eta_k && \text{（EMT 模型输出）} \\
u_k &= C_{\mathrm{hw}}(y_{k-d}) && \text{（硬件控制器）} \\
x_{k+1} &= F(x_k, u_k) && \text{（EMT 状态更新）}
\end{aligned}
$$

### WBG PFNN 物理特征预测

$$
\hat{v}_{\text{feat}}^k = \text{PFNN}(v^{k-n:k-1}, i^{k-n:k-1}; \theta), \qquad v_{\text{recon}}^k = \text{Interpolate}(\hat{v}_{\text{feat}}^k)
$$

PFNN 预测波形中的物理特征点而非全采样点，再用插值重构高分辨率瞬态。

### TLM 接口解耦方程

$$
i_{k+1}^i = \frac{2}{Z_i} v_k^i + i_k^i, \qquad v_{k+1}^i = Z_i i_{k+1}^i + v_k^i
$$

TLM 分区后各子系统可并行计算，仅通过阻抗 $Z_i$ 交换历史电压/电流信息。

## 关键技术挑战

### 接口延迟与抖动

HIL 中的延迟来源包括：CT/CVT 传感延迟（$T_{\text{CT}}$）、A/D 转换延迟（$T_{\text{ADC}}$）、控制处理延迟（$T_{\text{proc}}$）、D/A 转换延迟（$T_{\text{DAC}}$）、PWM 刷新延迟（$T_{\text{PWM}}$）。总延迟 $d$ 必须在 EMT 接口方程中显式建模，否则控制器看到的反馈量滞后于真实系统状态，导致不稳定或保护误动作。

### 开关谐波与等效精度权衡

为满足实时 deadline 而采用平均值模型、等效电压源或降阶阀组时，必须说明以下信息的舍弃代价：

- 开关谐波（尤其是 MMC 子模块电容电压纹波）
- 子模块状态（FB-MMC 每个子模块的投切状态）
- 保护瞬时量（故障电流峰值、上升率）

### 功率 HIL 的稳定性

功率 HIL 若功放带宽不足、延迟补偿不当或接口阻抗选择不当，可能出现非物理振荡甚至损坏设备。需要闭环稳定性分析方法（如阻抗匹配判据、小信号阻抗分析）。

### WBG 器件的多时间尺度耦合

系统级 EMT（$10\,\mu\text{s}$ 步长）与器件级 WBG 瞬态（< 1 μs）的时间尺度差异巨大。PFNN 的物理特征提取需要：① 大量离线数据训练；② 物理约束（单调性、对称性）嵌入损失函数；③ FPGA 定点量化误差控制。

### 多厂商设备互操作性

多端直流电网中，不同厂商的换流站和 DCCB 控制保护硬件需要统一接口协议。HIL 测试是互操作性验证的必要前置环节，但 HIL 通过不等于现场投运保证——未覆盖的故障、通信异常、固件版本和硬件配置仍是残余风险。

## 量化性能边界

### 时间步长与计算平台

| 计算平台 | 典型步长 | 适用场景 | 代表成果 |
|---------|---------|---------|---------|
| CPU 实时（RTDS/RT-LAB） | 20–50 μs | 大系统机电暂态 | Nelson River 三回 HVDC（RTDS） |
| 小步长 RT-EMT | 1–5 μs | MMC 换流器详细仿真 | La Vérendrye 混合 SVC-VSC FAT |
| FPGA | 0.05–1 μs | WBG 器件级仿真 | Zhang 2023: 1 ns（PFNN 辅助） |
| CPU+FPGA 多速率 | 1 μs / 50 μs | 含电力电子的大系统 | RTDS-FPGA 联合平台 |

### 接口性能指标

| HIL 类型 | 接口延迟 | 带宽要求 | 典型精度 |
|---------|---------|---------|---------|
| 控制器 HIL（CHIL） | < 1 μs | I/O: DC–10 kHz | 取决于 A/D 分辨率（≥ 12 bit） |
| 功率 HIL（PHIL） | 5–50 μs | 功放: DC–5 kHz | 功放输出波形 THD < 2% |
| WBG PHIL | 1–10 ns（器件级） | FPGA: DC–100 MHz | PFNN 预测误差 < 2% |
| 多速率 HIL | 跨速率重同步延迟 | TLM 接口稳定性 | 接口电压/电流偏差 < 0.5% |

### 典型参数范围

| 参数 | 范围 |
|------|------|
| 时间步长 | 1 μs ~ 50 μs（CPU）；0.05–1 μs（FPGA） |
| 系统规模 | 10 ~ 1000 节点 |
| 仿真时长 | 0.1 s ~ 10 s（实时闭环）|
| 电压等级 | 10 kV ~ 500 kV |
| 功率范围 | 1 MW ~ 1000 MW |
| 频率范围 | 50 Hz / 60 Hz |
| DCCB 清除时间 | < 5 ms |

### DCCB HIL 量化数据（Rault 2020）

- 三端 HVDC 网：1 个 MMC 换流站 + 12 个混合 DCCB。
- 测试场景：电缆充电（energization）和故障清除（fault clearance）。
- 验证内容：控制调参、控制与保护全流程链（采集、处理时间、独立控制器间协调）。
- 离线研究对比：覆盖了离线仿真无法涵盖的动态范围（因计算时间长或控制简化的限制）。

### WBG HIL 量化数据（Zhang 2023）

- DRM 系统：AC-变压器-整流子系统 + 直流铁路子系统 + 储能 + IDCDC（8 kV MVDC 总线）。
- WBG 器件：SiC IGBT（MVDC→LVDC），GaN HEMT（LVDC→电动车充电）。
- PFNN 步长：低至 **1 ns**。
- 精度：PFNN 预测与 SaberRD 离线仿真误差 < 2%。
- 资源：GRU + EMT 并行计算，FPGA 定点实现。

## 适用边界与选择指南

### HIL 类型选择决策表

| 需求场景 | 推荐 HIL 类型 | 步长要求 | 接口要求 |
|---------|-------------|---------|---------|
| 控制保护算法验证（通用） | 控制器 HIL | ≥ 20 μs | 数字 I/O |
| MMC/HVDC 详细动态性能测试 | 小步长控制器 HIL | 1–5 μs | 光纤接口（≥ 512 点/周期） |
| 新能源并网功率回路测试 | 功率 HIL | ≥ 5 μs | 功率放大器 |
| WBG 器件超快瞬态仿真 | WBG PHIL（PFNN+FPGA） | 1 ns–1 μs | FPGA 并行计算 |
| 直流电网保护与 DCCB 协调 | DCCB 控制器 HIL | ≥ 10 μs | 工业控制保护硬件 |
| 含电力电子的大系统仿真 | 多速率 RTDS-FPGA | 1 μs / 50 μs | TLM 接口 |
| 大型 HVDC 系统预投运 | 大型混合实时 HIL | ≥ 20 μs | 控制保护硬件副本 |

### 模型选择与步长权衡

- **步长 ≤ 5 μs**：保留开关细节和 MMC 子模块状态，适用于控制保护算法验证和动态性能测试。
- **步长 20–50 μs**：使用平均值模型或戴维南等效，适用于大系统稳态和故障后恢复研究。
- **FPGA 级步长（< 1 μs）**：仅用于器件级仿真或需要纳秒级分辨率的特殊测试（WBG 器件、故障行波）。

### 与相关页面的关系

- [[real-time-simulation]] 讨论固定步长和 deadline；HIL 在此基础上增加真实硬件、I/O 和安全约束。
- [[interface-technique]] 解释电压、电流、功率、相量和多端口接口；HIL 需要把这些接口落实到物理或通信通道。
- [[offline-to-realtime-porting]] 关注离线模型迁移；HIL 是迁移后的闭环使用场景之一。
- [[protection-control-device]] 和 [[distance-relay]] 解释被测保护控制对象的模型边界。
- [[large-scale-grid-simulation]] 与 [[large-scale-hybrid-acdc-simulation]] 提供 HIL 常见系统背景。
- [[co-simulation]] 讨论多工具多速率协同仿真，HIL 是其实时化的具体形态。

## 开放问题

- 如何为 HIL 报告统一的接口延迟、抖动、量化误差、波形误差和硬件版本信息。
- 如何在满足实时 deadline 的同时保留保护动作所需的瞬时量和高频分量。
- 如何把通信网络、真实 IED、功率接口和 EMT 数值稳定性纳入同一验证报告。

## 来源论文

- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Le-Huy & Tremblay 2023]] — 混合 SVC-VSC 小步长与常规步长 HIL 两类建模路径对比；MMCsim 刷新率 512 点/周期（$32.55\,\mu\text{s}$）；FAT 阶段 $t_s < 5\,\mu\text{s}$，预投运阶段 $t_s > 20\,\mu\text{s}$；两者结果一致的必要条件是"权宜处理"被显式纳入模型。
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Rault 等 2020]] — 三端 HVDC 网 HIL：1 MMC + 12 混合 DCCB + 工业控制保护硬件；混合 DCCB 实时化模型；电缆充电和故障清除测试。
- [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Zhang 等 2023]] — DRM 分层 HIL：TLM 分区并行 + GRU/EMT 系统层 + PFNN（WBG 器件级 1 ns 步长）；误差 < 2%。
- [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|Automated FPGA Real-Time Simulator]] — MANA+FAMNM+开关电导优化+稀疏矩阵并行；电路网表到 FPGA 求解器的自动化生成流程。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Nelson River 大规模混合实时仿真]] — Manitoba Hydro Nelson River 三回双极 LCC-HVDC；RTDS 模块化分层建模；遗留控制处理策略；预投运 HIL 验证。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Porting Offline to Real-Time]] — 离线大系统向实时 HIL 迁移；模型兼容层、信号校核和波形比较是工程证据的核心组成。
- [[emt-simulation-verification]] — HIL 波形、接口和 deadline 证据的验证框架。