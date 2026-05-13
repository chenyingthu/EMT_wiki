---
title: "硬件在环仿真 (Hardware-in-the-Loop, HIL)"
type: topic
tags: [hil, hardware-in-loop, real-time, testing, controller, power-electronics, fpga, rtds, opal-rt, phil]
created: "2026-05-04"
updated: "2026-05-13"
---

# 硬件在环仿真 (Hardware-in-the-Loop, HIL)

## 定义

硬件在环仿真（Hardware-in-the-Loop, HIL）是将**真实物理硬件**（控制器、保护装置、功率变流器等）与**实时数字仿真器**相连，形成闭环测试系统的技术。在 HIL 中，电力系统由数字仿真器实时模拟，被测硬件通过 I/O 接口与仿真器交互，验证其在真实工况下的控制、保护和动态性能。

HIL 的核心特征是**闭环实时性**：仿真器必须在每个时间步长内完成计算，并将结果通过 I/O 传递给真实硬件，硬件的输出又作为下一时刻的仿真输入，形成完整的控制-被控回路。实时约束可表示为

$$T_{\mathrm{solve}} + T_{\mathrm{IO}} + T_{\mathrm{comm}} + T_{\mathrm{hw}} \leq \Delta t,$$

其中 $T_{\mathrm{solve}}$ 为仿真器计算时间，$T_{\mathrm{IO}}$ 为 I/O 传输时间，$T_{\mathrm{comm}}$ 为通信延迟，$T_{\mathrm{hw}}$ 为硬件控制处理时间，$\Delta t$ 为仿真步长（实时 deadline）。

**边界限定**：本页面聚焦于 HIL 仿真的原理、架构、建模方法和工程实践，不包括具体设备操作手册。HIL 与纯离线仿真（如 PSCAD/EMTDC 离线计算）和纯数字 co-simulation 的根本区别在于**被测对象是真实硬件**而非软件模型。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  <text x="450" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#333">HIL 系统架构与分类</text>
  <rect x="30" y="50" width="240" height="100" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="150" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#2563eb">控制器 HIL</text>
  <text x="150" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">信号级闭环测试</text>
  <text x="150" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">步长: 10-50 μs</text>
  <text x="150" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">FO: 32.6 μs 刷新</text>
  <rect x="330" y="50" width="240" height="100" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#16a34a">功率 HIL (PHIL)</text>
  <text x="450" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">功率级闭环测试</text>
  <text x="450" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">功放 + 阻抗匹配</text>
  <text x="450" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">ITM/DIM/PCD 接口</text>
  <rect x="630" y="50" width="240" height="100" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="750" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#d97706">RMS-EMT 多域 HIL</text>
  <text x="750" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">保护/广域控制测试</text>
  <text x="750" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">ePhasorSim + RTDS</text>
  <text x="750" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">传输线接口耦合</text>
  <line x1="150" y1="150" x2="150" y2="180" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="150" x2="450" y2="180" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="750" y1="150" x2="750" y2="180" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="30" y="200" width="240" height="90" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="150" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#16a34a">实时仿真器</text>
  <text x="150" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">RTDS / OPAL-RT</text>
  <text x="150" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">FPGA 自定义平台</text>
  <rect x="330" y="200" width="240" height="90" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#d97706">I/O 接口层</text>
  <text x="450" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">DAQ / DIO / FO</text>
  <text x="450" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">模拟/数字/光纤通信</text>
  <rect x="630" y="200" width="240" height="90" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="750" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#7c3aed">被测硬件 (DUT)</text>
  <text x="750" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">控制器 / 保护装置</text>
  <text x="750" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">功率变流器 / IED</text>
  <line x1="150" y1="290" x2="450" y2="290" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="290" x2="750" y2="290" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="750" y1="290" x2="450" y2="340" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="340" x2="150" y2="340" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="150" y1="340" x2="150" y2="290" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="450" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666" font-style="italic">闭环反馈: y → DUT → u → 仿真器</text>
  <rect x="30" y="370" width="240" height="130" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="150" y="398" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#dc2626">实时约束</text>
  <text x="150" y="420" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">T_solve + T_IO + T_comm</text>
  <text x="150" y="437" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">+ T_hw ≤ Δt</text>
  <text x="150" y="457" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">RTDS 小步长: Δt ≤ 3 μs</text>
  <text x="150" y="475" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">节点 ≤ 30, 开关 ≤ 6</text>
  <rect x="330" y="370" width="240" height="130" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="450" y="398" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#dc2626">接口稳定性</text>
  <text x="450" y="420" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">|Z_sim| &lt; |Z_real|</text>
  <text x="450" y="440" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">(ITM 判据)</text>
  <text x="450" y="460" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">Stub line + Pejovic</text>
  <text x="450" y="478" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">开关引入寄生影响</text>
  <rect x="630" y="370" width="240" height="130" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="750" y="398" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#dc2626">信号保真度</text>
  <text x="750" y="420" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">量程 / 采样保持</text>
  <text x="750" y="437" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">抗混叠滤波</text>
  <text x="750" y="457" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">通信协议差异</text>
  <text x="750" y="475" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">量化误差影响保护动作</text>
  <rect x="630" y="50" width="240" height="100" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6,3"/>
  <text x="750" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#7c3aed">FTRT HIL</text>
  <text x="750" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">超实时硬件 emulation</text>
  <text x="750" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">AC/TS + DC/EMT 混合</text>
  <text x="750" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#777">加速比: 51x ~ 277x</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · HIL 系统架构与分类概览</p>

## EMT 中的角色

在电磁暂态（EMT）仿真语境下，HIL 是控制器和保护系统验证的关键手段，其核心价值体现在：

- **控制器验证**：在真实投入前验证 VSC、MMC、SVG/SVC 等电力电子设备的控制策略，包括启动、负荷跟踪、故障穿越等工况。
- **保护测试**：验证继电保护装置在交流/直流故障、CT/PT 饱和、通信异常等多种工况下的动作正确性。
- **多厂商互操作性测试**：如 Rault 2020 在三个端子 HVDC 网格中同时接入 ABB DCCB 和换流器控制硬件，验证不同厂商设备间的协调。
- **安全测试**：在虚拟环境中测试极端故障（如直流短路、换相失败、级联故障），避免物理设备损坏。
- **成本节约**：减少物理原型和现场试验次数，Manitoba Hydro 在 Nelson River Bipole III 投运前利用 HIL 模型将技术风险显著降低。
- **可重复性**：精确复现特定工况，支持控制参数整定的迭代优化。

## HIL 分类与架构

### 1. 控制器 HIL（Control HIL）

控制器 HIL 是最常见的 HIL 形式。真实控制器（如 DCS、PLC、专用保护继电器）通过模拟量（±10 V、4-20 mA）和数字量（开关量、脉冲）接口与实时仿真器连接。

**系统架构**：

```
┌─────────────┐    模拟/数字信号    ┌──────────────┐    模拟/数字信号    ┌─────────────┐
│  实时仿真器   │ ◄──────────────► │  I/O 接口板卡  │ ◄──────────────► │  被测硬件    │
│ (RTDS/OPAL-RT)│    测量信号 y     │  (DAQ/DIO)    │    控制信号 u     │ (控制器/保护)│
│ 电力系统模型  │                   │               │                   │              │
└─────────────┘                   └──────────────┘                   └─────────────┘
```

**关键参数**：
- 典型步长：10-50 μs（常规 EMT HIL），3 μs（小步长 MMC 详细模型 HIL）
- 闭环延迟：$d = T_{\mathrm{solve}} + T_{\mathrm{IO}} + T_{\mathrm{comm}}$，需控制在半个开关周期以内
- I/O 刷新率：标准 I/O 为 1 ms 级，高速 FO（Fiber Optic）可达 32.6 μs（512 点/周期）

**Le-Huy & Tremblay 2023 的工程实践**：在 Hydro-Québec La Verendrye 混合 SVC-VSC 项目中，DPS（动态性能研究）和 FAT（工厂验收测试）阶段采用 3 μs 小步长 HIL，MMCsim 模块以 32.5521 μs（512 点/周期）通过 FO 接口向真实控制器发送等效电压指令，同时从控制器接收电枢电流反馈。

### 2. 功率 HIL（Power HIL, PHIL）

功率 HIL 将**实际功率设备**（而非仅控制信号）接入仿真回路。功率放大器驱动真实负载，被测设备与仿真器之间交换的是**功率信号**（大电流、高电压），而非小信号。

**原理**：
- 功率放大器（通常为宽带变流器）模拟电网阻抗，向真实设备注入电压/电流
- 真实设备的响应被测量后反馈给仿真器，形成功率级闭环
- 需要专门的接口稳定性控制，否则可能引发非物理振荡

**接口稳定性判据**：

理想变压器模型（ITM）的稳定性条件为：

$$|Z_{\mathrm{sim}}| < |Z_{\mathrm{real}}|,$$

其中 $Z_{\mathrm{sim}}$ 为仿真侧等效阻抗，$Z_{\mathrm{real}}$ 为真实设备输入阻抗。不满足此条件时，接口可能产生振荡。

**常用接口方法**：
- 理想变压器模型（ITM, Ideal Transformer Model）
- 阻尼阻抗法（DIM, Damped Impedance Method）
- 部分电路复制法（PCD, Partial Circuit Duplication）

**风险**：若功放带宽不足、延迟补偿不当或接口阻抗选择不当，PHIL 可能出现非物理振荡甚至损坏设备。

### 3. RMS-EMT 多域 HIL

当被测区域需要 EMT 精度而外部大系统仅需 RMS 动态时，采用 RMS-EMT 多域 HIL。

**架构**（Espinoza 2021）：
- RMS 侧：OPAL-RT ePhasorSim，步长 ~ms 级，模拟大电网动态
- EMT 侧：RTDS，步长 ~μs 级，模拟被测区域和继电保护
- 接口：基于传输线模型的双向耦合，RMS 相量通过非缓冲快速曲线拟合转换为 EMT 瞬时波形

**优势**：在保护继电器 HIL 测试中，外部电网动态得以保留，被测区域的 EMT 细节（如故障暂态、谐波）不被简化。

### 4. 更快-than-real-time（FTRT）HIL

FTRT HIL 允许仿真以**超过实时速度**运行（如 50x、200x 加速），用于大规模系统的安全分析和大量 contingency 扫描。

**Cao 2022/2023 的实现**：
- AC 网格采用 TS（暂态稳定）模型，允许大步长
- DC 网格采用 EMT 模型，需要小步长捕捉换流器快速动态
- 动态电压注入接口协调 AC/DC 两种仿真类型
- 在 6 个 ACTIVSg 500-bus 系统 + 6 端子 DC 网格上实现 208x FTRT 加速
- 单个 500-bus 系统实现 277x FTRT 加速
- 分析超过 5500 种 contingency 场景

**Dinavahi 组的风电场 FTRT**：微电网集群中，MG 采用 EMT 模型，AC 主网采用 TS 模型，FPGA 并行部署实现 51x FTRT 加速。

## 平台与硬件架构

### 主流实时仿真平台

| 平台 | 架构 | 典型步长 | 特点 | 典型应用 |
|------|------|----------|------|----------|
| **RTDS** | 分布式多核 CPU | 1-50 μs | 工业标准，支持小步长模式（≤ 3 μs），节点数受限（小步长模式 ≤ 30 单相节点/任务） | HVDC/HIL 测试、保护验证 |
| **OPAL-RT** | 多核 CPU + FPGA 混合 | 1-100 μs | ePhasorSim 支持 RMS 仿真，与 RTDS 可 co-simulation | RMS-EMT 混合 HIL、微电网 |
| **dSPACE** | 多核 DSP + FPGA | 1-10 μs | 汽车/工业控制 HIL 主流，也用于电力系统 | 控制器开发、DRM 测试 |
| **FPGA 自定义平台** | 多 FPGA 板并行 | 0.38-2 μs | 亚微秒级步长，资源受限，需重新综合 | 电力电子详细模型、WBG 器件 |

### FPGA 硬件加速架构

FPGA 是实现 HIL 亚微秒级仿真的核心硬件。其架构特点包括：

- **并行性**：与 CPU 的串行 EMT 算法不同，FPGA 可实现 nodal admittance matrix 的并行求解
- **固定步长**：FPGA 天然适合固定步长仿真，步长由硬件时钟决定
- **资源受限**：单块 FPGA 的逻辑资源有限，大规模系统需多板分布式部署
- **Li 2026 的 CPU-FPGA 协作**：CLCC-HVDC 多速率 HIL 中，CPU 处理慢动态（控制、保护），FPGA 处理快动态（开关瞬态，2 μs 步长），计算时间减少约 77%

**Xu 2020 的 LIM 解耦方法**：在微电网 FPGA 仿真中，采用时域传输法（TLM）划分系统，配电线路用 π 型电路建模并通过延迟插入法（LIM）求解，使各 DG 系统解耦并行。在 Xilinx Kintex-7 410T 上实现 380 ns 最小步长。

## 建模方法

### 1. 常规 EMT 步长建模（Δt ≥ 20 μs）

常规步长 HIL 使用标准 EMT 模型（如 Bergeron 传输线模型、经典开关模型），适用于系统规模较大、开关细节要求不高的场景。

**特点**：
- 支持所有标准组件模型
- 不受小步长模式节点数限制
- 闭环延迟较大（~1 ms 级 I/O 刷新）
- 不适合高速开关器件（如 GaN、SiC）的直接仿真

**Le-Huy & Tremblay 2023 的结论**：常规步长 HIL 在闭环延迟和系统规模上有优势，但无法捕捉开关谐波细节。适用于控制逻辑验证和低频动态测试。

### 2. 小步长 EMT 建模（Δt ≤ 5 μs）

小步长 HIL 使用 Pejovic 开关模型等高速开关模型，时间步长可低至 1-3 μs。

**特点**：
- 可捕捉开关谐波和快速暂态
- 系统规模受限（单任务最多 30 个单相节点）
- 电力电子模型受限（单任务仅支持 6 个 Ron/Roff 开关）
- 需引入 stub line 和 Pejovic 开关来满足实时约束

**Pejovic 开关模型参数**（基于步长 ΔT、开关电流 i、电压 v 和阻尼因子 δ）：

$$R_{\mathrm{on}} = \frac{\Delta T}{2C_{\mathrm{par}}}, \quad C_{\mathrm{par}} = \delta \cdot \frac{i \cdot \Delta T}{v},$$

其中 $R_{\mathrm{on}}$ 为导通电阻，$C_{\mathrm{par}}$ 为并联电容。这些寄生参数会引入非物理影响，需在 HIL 验证中予以考虑。

### 3. 机器学习加速模型

Zhang 2023 提出物理特征神经网络（PFNN, Physical Feature Neural Network）来加速 WBG 器件（GaN HEMT、SiC IGBT）的 HIL 仿真：

- 将 ML 算法与物理建模相结合
- 支持可变时间步长（低至 1 ns）
- 在 FPGA 上实现 ultra-fast 瞬态 emulation
- 相比 PSCAD/EMTDC 离线仿真，HIL 结果高度吻合

**PFNN 优势**：
- 灵活性高：可适应不同器件类型和工况
- 精度好：物理约束保证外推可靠性
- 速度快：神经网络前向推理远快于微分方程数值求解

### 4. 传输线接口方法

在 RMS-EMT 多域 HIL 中，传输线接口是关键。Espinoza 2021 使用 Bergeron 模型作为接口：

$$i_{km}(t) = \frac{v_k(t)}{Z_c} + h_k(t-\tau),$$

$$i_{mk}(t) = \frac{v_m(t)}{Z_c} + h_m(t-\tau),$$

其中 $Z_c$ 为波阻抗，$h(\cdot)$ 为历史电流项，$\tau$ 为传输延迟。RMS 侧的相量通过非缓冲快速曲线拟合转换为 EMT 瞬时值。

## 形式化表达

### 实时闭环系统

HIL 闭环系统可形式化描述为离散时间系统：

$$y_k = H(x_k) + \eta_k, \qquad u_k = C_{\mathrm{hw}}(y_{k-d}), \qquad x_{k+1} = F(x_k, u_k),$$

其中 $x_k$ 为仿真模型状态向量，$y_k$ 为传给硬件的测量量，$u_k$ 为硬件输出控制量，$d$ 为等效采样-转换-通信-处理延迟，$H$ 为测量函数，$C_{\mathrm{hw}}$ 为硬件控制器，$F$ 为仿真器状态更新函数，$\eta_k$ 为测量噪声和量化误差。

### 小步长约束

RTDS 小步长模式的约束条件：

$$N_{\mathrm{nodes}} \leq 30, \quad N_{\mathrm{switches}} \leq 6, \quad \Delta t \leq 3~\mu\mathrm{s},$$

其中 $N_{\mathrm{nodes}}$ 为单任务单相节点数，$N_{\mathrm{switches}}$ 为标准 Ron/Roff 开关数。

### 接口稳定性

PHIL 接口稳定性要求：

$$\left\| \frac{Z_{\mathrm{sim}}(j\omega) - Z_{\mathrm{ref}}(j\omega)}{Z_{\mathrm{sim}}(j\omega) + Z_{\mathrm{ref}}(j\omega)} \right\|_\infty < 1,$$

其中 $Z_{\mathrm{ref}}$ 为参考阻抗。

## 关键技术挑战

### 1. 实时性与计算复杂度

大规模系统 HIL 面临的核心矛盾：EMT 精度要求小步长（μs 级），但系统规模越大计算量呈指数增长。

**解决方案**：
- FPGA 并行计算（Cao 2022 实现 208x FTRT）
- CPU-FPGA 协作（Li 2026 减少 77% 计算时间）
- 多速率仿真（快动态 FPGA + 慢动态 CPU）
- 降阶模型（平均值模型、等效电压源）

### 2. 接口延迟与稳定性

HIL 闭环的总延迟 $d$ 必须控制在被控动态的时间常数以内。对于电力电子开关频率 10 kHz（周期 100 μs），延迟应小于 10-20 μs。

**延迟来源**：
- 仿真计算时间 $T_{\mathrm{solve}}$
- I/O 刷新时间 $T_{\mathrm{IO}}$（标准 I/O ~1 ms，FO ~32.6 μs）
- 通信延迟 $T_{\mathrm{comm}}$（以太网、光纤）
- 硬件处理时间 $T_{\mathrm{hw}}$（控制器扫描周期）

**Le-Huy & Tremblay 2023 的发现**：小步长模式引入的 stub line 和 Pejovic 开关会显著改变系统阻抗特性，必须在 HIL 验证中予以考虑。常规步长和小步长 HIL 的匹配需要在寄生元件层面进行校准。

### 3. 信号保真度

I/O 的量程、采样保持、抗混叠滤波和通信协议可能改变保护或控制动作。必须作为模型边界说明，而不能假设"理想信号传输"。

### 4. 多厂商互操作性

Rault 2020 在三个端子 DC 网格中同时测试 ABB DCCB 和换流器控制硬件，验证了多厂商设备的协调性。关键挑战包括：
- 不同厂商通信协议差异
- 保护定值协调
- 故障检测时间差异（需在数 ms 内隔离故障）

## 量化性能边界

| 指标 | 数值范围 | 来源 |
|------|----------|------|
| 最小时间步长（FPGA） | 380 ns | Xu 2020（Kintex-7 410T） |
| 典型 HIL 步长（RTDS 常规） | 20-50 μs | Le-Huy 2023 |
| 典型 HIL 步长（RTDS 小步长） | 1-3 μs | Le-Huy 2023 |
| FTRT 加速比（500-bus AC） | 277x | Cao 2022 |
| FTRT 加速比（AC/DC 混合） | 208x | Cao 2022 |
| FTRT 加速比（微电网集群） | 51x | Cao 2023 |
| CPU-FPGA 计算时间减少 | ~77% | Li 2026 |
| 归一化 RMS 电压误差 | < 7% | Li 2026 |
| PFNN 最小时间步长 | 1 ns | Zhang 2023 |
| FO 接口刷新率 | 32.5521 μs (512点/周期) | Le-Huy 2023 |
| 保护 HIL 步长 | 50-100 μs | 常规保护测试 |
| 控制器 HIL 步长 | 10-50 μs | 常规控制测试 |

## 适用边界与选择指南

### HIL 方法选择指南

| 应用场景 | 推荐方法 | 步长 | 平台 |
|----------|----------|------|------|
| 控制逻辑验证（低频动态） | 常规 EMT HIL | 20-50 μs | RTDS / OPAL-RT |
| MMC/VSC 开关细节测试 | 小步长 EMT HIL | 1-3 μs | RTDS（小步长模式） |
| WBG 器件（GaN/SiC）测试 | PFNN 加速 HIL | 1 ns-1 μs | FPGA / dSPACE |
| 保护继电器测试 | RMS-EMT 多域 HIL | RMS: ms, EMT: μs | OPAL-RT + RTDS |
| 大规模系统安全分析 | FTRT HIL | AC: ms, DC: μs | 多 FPGA 板 |
| 功率设备实测 | PHIL | 10-50 μs | 功率放大器 + RTDS |
| 多厂商互操作性 | 混合 HIL | 按组件 | RTDS + 真实硬件 |

### 失效边界

- **接口不稳定**：PHIL 功率接口振荡（阻抗比不满足稳定性判据）
- **时序溢出**：$T_{\mathrm{solve}} > \Delta t$，导致实时 deadline 失败
- **信号失真**：I/O 量化、延迟、抗混叠滤波引入的误差
- **模型精度不足**：平均值模型无法捕捉保护动作所需的高频分量
- **资源耗尽**：FPGA 逻辑资源不足，无法容纳完整系统模型

## 相关方法 / 相关模型 / 相关主题

[[real-time-simulation]] - 实时仿真技术基础

[[hil-simulation]] - HIL 仿真方法详解（控制器 HIL、功率 HIL）

[[fpga-real-time-simulation]] - FPGA 实时仿真硬件加速

[[co-simulation]] - 多工具联合仿真（RMS-EMT、离线-实时）

[[offline-to-realtime-porting]] - 离线模型迁移到实时平台

[[interface-technique]] - 电压/电流/功率接口方法

[[electromagnetic-transient]] - 电磁暂态分析

[[power-system]] - 电力系统建模

[[control-system]] - 控制系统设计

[[protection-relay-modeling]] - 继电保护建模

[[bergeron-line-model]] - Bergeron 传输线模型（HIL 接口基础）

## 来源论文

- **Le-Huy & Tremblay 2023** (Electric Power Systems Research) — 混合 SVC-VSC 工程中常规步长与小步长两种 HIL 建模路径的详细对比，揭示了小步长寄生元件的影响。
- **Rault et al. 2020** — 工业 DCCB 控制器在三个端子 HVDC 网格中的 HIL 测试，验证了多厂商互操作性。
- **Espinoza et al. 2021** (IPST) — RMS-EMT 多域实时 HIL 接口方法，用于保护继电器测试。
- **Zhang et al. 2023** (IEEE OJPEL) — 基于 PFNN 机器学习加速的 WBG 器件 HIL  emulation，支持 1 ns 可变步长。
- **Cao et al. 2022** (IEEE TPWRS) — AC/DC 混合电网 FTRT 硬件 emulation，208x 加速比，5500+ contingency 分析。
- **Cao et al. 2023** (IEEE OAJPE) — 微电网集群 FTRT emulation，51x 加速比。
- **Li et al. 2026** (International Journal of Electrical Power and Energy Systems) — CPU-FPGA 协作多速率 HIL 框架，CLCC-HVDC 应用，计算时间减少 77%。
- **Zhou et al. 2021** — Nelson River 多馈入 HVDC 大规模混合实时 HIL 建模与工程应用。
- **Xu et al. 2020** — FPGA 亚微秒级微电网实时仿真，LIM 解耦算法，380 ns 步长。
- **Scheibe et al.** — RTDS Novacor 与 PSS/E 的 EMT-RMS 耦合接口，UDP 和光纤两种实现方案。
