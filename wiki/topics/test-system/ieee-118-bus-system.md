---
title: "IEEE 118 Bus System"
type: topic
tags: [ieee-118, test-system, benchmark, power-system, large-scale, emt-simulation]
created: "2026-05-02"
updated: "2026-05-13"
---

# IEEE 118 Bus System

## 定义

IEEE 118 Bus System 是电力系统分析领域最广泛使用的标准测试系统之一，由 Christie 于 1993 年整理发布（[Power Systems Test Case Archive](https://www.ee.washington.edu/research/pstca/pf118/pg_tca118bus.htm)）。该系统包含 **118 个母线**、**186 条支路**（含变压器支路）、**54 台发电机** 和 **99 个负荷节点**，总发电容量约 4.4 GW，是介于 IEEE 39-bus（New England，10 机 39 母线）和 IEEE 300-bus 之间的大型输电网 benchmark。

IEEE 118 最初设计用于稳态潮流（Power Flow）、最优潮流（OPF）、安全性评估（Security Assessment）和机电暂态（Transient Stability）研究。其原始数据仅包含正序（positive-sequence）稳态参数——母线电压等级、支路导纳、发电机出力/限值、负荷有功/无功——**不包含任何 EMT 所需的高频动态参数**（如线路分布电容/电感、变压器绕组频变参数、换流器开关级模型、保护继电器定值、励磁/调速器动态细节）。

因此，IEEE 118 在 EMT 仿真中只能作为**外部交流系统背景**或**混合仿真（Co-simulation）的基准网络**使用，必须经过专门改造才能支撑电磁暂态级别的结论。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;">
  <!-- Background -->
  <rect width="900" height="480" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">IEEE 118 Bus System 在 EMT 仿真中的应用架构</text>
  
  <!-- Central node: IEEE 118 -->
  <rect x="330" y="60" width="240" height="60" rx="12" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">IEEE 118 Bus System</text>
  <text x="450" y="105" text-anchor="middle" font-size="11" fill="#3b82f6">118 母线 · 186 支路 · 54 发电机</text>
  
  <!-- Arrow down from center -->
  <line x1="450" y1="120" x2="450" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Process node: EMT Transformation -->
  <rect x="300" y="155" width="300" height="50" rx="10" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="175" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">EMT 改造</text>
  <text x="450" y="193" text-anchor="middle" font-size="10" fill="#22c55e">三相化 · 频变线路 · 发电机动态 · 负荷模型</text>
  
  <line x1="450" y1="205" x2="450" y2="235" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Branch: 3 paths -->
  <!-- Left: Co-simulation -->
  <line x1="450" y1="235" x2="200" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="60" y="270" width="220" height="65" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="170" y="293" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">DP-EMT 协同仿真</text>
  <text x="170" y="310" text-anchor="middle" font-size="10" fill="#b45309">Mudunkotuwa 2018</text>
  <text x="170" y="325" text-anchor="middle" font-size="10" fill="#b45309">加速比 5.26× ~ 21.69×</text>
  
  <!-- Center: FPGA Real-time -->
  <line x1="450" y1="235" x2="450" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="310" y="270" width="220" height="65" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="420" y="293" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">FPGA 实时仿真</text>
  <text x="420" y="310" text-anchor="middle" font-size="10" fill="#b45309">Cao 2021 (FT-SCADA)</text>
  <text x="420" y="325" text-anchor="middle" font-size="10" fill="#b45309">加速比 &gt; 222×</text>
  
  <!-- Right: GPU Parallel BESS -->
  <line x1="450" y1="235" x2="700" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="560" y="270" width="280" height="65" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="700" y="293" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">GPU 并行 BESS 建模</text>
  <text x="700" y="310" text-anchor="middle" font-size="10" fill="#b45309">Lin 2023 (50K BESS)</text>
  <text x="700" y="325" text-anchor="middle" font-size="10" fill="#b45309">加速比 228×</text>
  
  <!-- Bottom row: Extended applications -->
  <line x1="170" y1="335" x2="170" y2="380" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="335" x2="420" y2="380" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="700" y1="335" x2="700" y2="380" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Application nodes -->
  <rect x="40" y="380" width="200" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="140" y="400" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">新能源改造</text>
  <text x="140" y="418" text-anchor="middle" font-size="9" fill="#7c3aed">Cheng 2024 (2.56M PV)</text>
  
  <rect x="270" y="380" width="240" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="390" y="400" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">HVDC 接口</text>
  <text x="390" y="418" text-anchor="middle" font-size="9" fill="#7c3aed">Cao 2021 (4-T MMC-HVDC)</text>
  
  <rect x="540" y="380" width="280" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="680" y="400" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">大规模并行仿真标尺</text>
  <text x="680" y="418" text-anchor="middle" font-size="9" fill="#7c3aed">CPU-GPU 异构 · 多速率求解</text>
  
  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto" fill="#333">
      <polygon points="0 0, 10 3.5, 0 7"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · IEEE 118 Bus System 在 EMT 仿真中的应用架构</p>

## EMT 中的角色

IEEE 118 在 EMT 仿真中有以下核心用途：

- **大规模 EMT 算法测试平台**：检验节点导纳矩阵组装、稀疏 LU 分解、PCG 迭代求解器在 118 母线规模下的内存占用和计算时间
- **EMT-TS 混合仿真（Co-simulation）基准网络**：将 IEEE 118 划分为 EMT 子网（含详细电力电子设备的局部区域）和动态相量（DP）/暂态稳定（TS）子网（外部系统），利用 Bergeron 传输线延迟实现多速率解耦
- **新能源/HVDC/FACTS 改造背景**：在特定母线上添加光伏阵列、风电机组、BESS 或 MMC-HVDC 换流器，研究 IBR 并网动态
- **FPGA 实时仿真验证**：在 Xilinx Virtex UltraScale+ 等 FPGA 板上部署 IEEE 118 同步机模型，验证 FT-SCADA（Faster-Than-SCADA）动态仿真架构
- **大规模并行仿真标尺**：作为 CPU-GPU 异构并行 EMT 仿真的标准测试用例，报告加速比和可扩展性

> **关键区别**：IEEE 118 原始数据 ≠ EMT 可用模型。任何 EMT 结论必须明确说明"改造后的 IEEE 118"版本，不能将改造版本的性质泛化为原始 benchmark 属性。

## EMT 改造方法

将 IEEE 118 从稳态潮流系统转换为 EMT 可用模型需要以下改造步骤：

### 1. 三相化与频变线路参数

原始 IEEE 118 为正序单相等效模型。EMT 需要：

- 将每条支路展开为**三相模型**，包含自/互感、对地电容
- 长线路（> 100 km）需采用 **JMarti 频变模型** 或 **Berngoren 常数参数模型**
- 对于 138 kV 及以上电压等级的线路，需考虑**土壤频率特性**对接地阻抗的影响

以 Mudunkotuwa & Filizadeh (2018) 的 DP-EMT 协同仿真为例，IEEE 118 中用于 EMT-DP 接口的 150 km 输电线路（B8-B9）的正序参数为（基准 138 kV/100 MVA）：

$$
R = 0.0025 \text{ pu}, \quad X = 0.0305 \text{ pu}, \quad B = 1.1620 \text{ pu}
$$

该线路的物理长度决定了 DP 侧最大时间步长：

$$
l_{\min} \approx 3 \times 10^5 \times \Delta T \quad (\text{km})
$$

即 $\Delta T = 500\,\mu\text{s}$ 时需要至少 150 km 的线路延迟。

### 2. 发电机动态模型扩展

IEEE 118 原始数据仅包含发电机的有功出力上限/下限。EMT 扩展需要：

- **同步机模型**：从 6 阶简化模型升级为 **9 阶完整模型**（包含 $E_d'$, $E_q'$, $E_{fd}$, $\delta$, $\omega$ 等状态变量）
- **励磁系统**：添加 AVR（自动电压调节器）模型，如 IEEE Type EX1 或 EX2
- **调速系统**：添加汽轮机/水轮机调速器模型（IEEE Type GO 或 GOV1）
- **PSS（电力系统稳定器）**：添加相位补偿网络 $G_{PSS}(s)$

Cao et al. (2021) 在 FT-SCADA 架构中采用 9 阶同步机模型对 IEEE 118 进行 EMT-TS 混合仿真：

$$
\dot{\delta}_i = \omega_i - \omega_{\mathrm{ref}}
$$

$$
\frac{2H_i}{\omega_{\mathrm{base}}} \dot{\omega}_i = P_{m,i} - P_{e,i} - D_i(\omega_i - \omega_{\mathrm{ref}})
$$

$$
T_{a0,i} \dot{E_{q,i}'} = -E_{q,i}' - (X_i - X_i')I_{d,i} + E_{fd,i}
$$

其中 $H_i$ 为惯性常数，$P_{m,i}$ 为机械功率，$P_{e,i}$ 为电磁功率。

### 3. 负荷模型改造

原始 IEEE 118 使用恒定功率负荷（$P + jQ$ 常数）。EMT 需要：

- **感应电动机负荷**：添加 1 阶或 2 阶感应电动机模型，捕捉电压恢复动态
- **ZIP 负荷**：分解为恒阻抗（Z）、恒电流（I）、恒功率（P）组合
- **电子负荷**：若研究配电侧 EMT 动态，需添加 VSC 型负荷详细模型

### 4. 新能源/HVDC/FACTS 改造

在特定母线上添加动态设备是 IEEE 118 最常见的 EMT 改造方式：

**光伏改造**（Marthi et al., 2024）：
- 在指定母线添加 Type-4 全功率换流器型风电机组（6 MW/台，75 台聚合为 450 MW 风场）
- 换流器采用开关级详细模型（IGBT/diode），保留所有控制器反馈信号在 EMT 侧

**BESS 改造**（Lin et al., 2023）：
- IEEE 118 包含 3 个区域、总发电 4.4 GW
- 在 Bus 56, 63, 43, 33, 83 等节点添加 500 台 BESS 单元（每台 2.0 MVA）
- 采用 GPU 并行 EMT 建模，Type 1（Ni-Cd 电池）和 Type 2（Li-ion 电池）混合

**HVDC 改造**（Cao et al., 2021）：
- 在 Bus 25 和 Bus 54 连接四端（4-T）MMC-HVDC 系统
- MMC3/MMC4 作为整流侧，MMC1/MMC2 作为逆变侧
- AC 侧采用 TS 仿真（1 ms~10 ms 灵活时间步），DC 侧采用 EMT 仿真（固定 200 $\mu$s）

## 形式化表达

### 原始潮流模型

IEEE 118 的基准潮流模型为：

$$
I = Y_{\mathrm{bus}}V, \qquad P_i + jQ_i = V_i I_i^*
$$

其中 $Y_{\mathrm{bus}}$ 为 118×118 节点导纳矩阵（稀疏，平均每行约 4-5 个非零元）。

### EMT 扩展模型

进入 EMT 时，系统扩展为：

$$
\mathcal{S}_{\mathrm{EMT}} = \{Y_{abc}, x_0, c, \mathcal{D}, h\}
$$

其中：
- $Y_{abc}$：三相节点导纳矩阵（包含频变线路参数）
- $x_0$：初始状态向量（发电机转子角、励磁电压、负荷状态等）
- $c$：控制器集合（AVR、调速器、PSS、换流器控制器）
- $\mathcal{D}$：扰动集合（三相短路、负荷突变、新能源出力阶跃）
- $h$：仿真步长集合（可能包含多速率步长）

### DP-EMT 协同仿真模型

Mudunkotuwa & Filizadeh (2018) 提出的 DP-EMT 接口模型将 IEEE 118 分为两部分：

$$
\Delta T = n \Delta t
$$

其中 $\Delta T$ 为 DP 侧大步长，$\Delta t$ 为 EMT 侧小步长，$n$ 为整数倍率（如 $n = 25$，即 500 $\mu$s : 20 $\mu$s）。

接口条件依赖传输线传播延迟 $\tau$：

$$
\Delta T \leq \tau, \quad l_{\min} \approx 3 \times 10^5 \times \Delta T
$$

## 关键技术挑战

### 1. 规模与求解器性能

IEEE 118 的 118 母线规模在机电暂态中属于小规模，但在 EMT 中（特别是添加详细电力电子模型后）可能产生数万至数十万个微分代数方程。Filizadeh et al. (2025) 指出，大规模 EMT 仿真的核心挑战在于：

- **节点导纳矩阵规模**：$Y_{\mathrm{bus}}$ 从 118×118 膨胀到 $N \times N$（$N$ 为 EMT 状态变量总数）
- **稀疏模式变化**：添加详细换流器模型后，矩阵稀疏性下降，LU 分解的 fill-in 增加
- **多速率同步**：不同设备的时间步长不一致时的数据插值和同步

### 2. 参数缺失与等效

IEEE 118 原始数据不包含以下 EMT 必需参数：

| 参数类型 | 原始数据 | EMT 需求 | 等效方法 |
|---------|---------|---------|---------|
| 线路参数 | 正序 R/X/B | 三相频变 Z(f), Y(f) | JMarti 模型 / 常数参数等效 |
| 发电机 | Pmax/Pmin | 9阶模型 + H, D, T' | 基于同类机组统计值 |
| 负荷 | P+Q 常数 | ZIP + 感应电动机 | 基于负荷类型假设 |
| 变压器 | 支路阻抗 | 绕组频变 + 铁芯饱和 | IEEE C57.12.004 标准 |

### 3. 数据版本差异

不同来源的 IEEE 118 数据可能存在参数差异：
- **Christie 原始版本**（1993）：正序稳态数据
- **Pena et al. 扩展版本**（2018）：添加高比例可再生能源的 IEEE 118 变体
- **各仿真工具内置版本**：PSAT、MATLAB/Simulink、DSATools/TSAT、PSCAD 等各有微调

报告结果时必须明确数据来源和版本。

## 量化性能边界

### DP-EMT 协同仿真加速比

Mudunkotuwa & Filizadeh (2018) 在 IEEE 118 上的仿真时间对比（3 秒仿真时长）：

| 仿真器 | 运行时间 | 加速比 |
|--------|---------|--------|
| 全 EMT（20 $\mu$s） | 694 s | 基准 |
| DP-EMT（500 $\mu$s : 20 $\mu$s） | 132 s | **5.26×** |
| DP-EMT（电压源接口） | 32 s | **21.69×** |

误差分析：DP-EMT 在故障前后能准确捕捉低频动态分量，高频瞬变因大步长滤波而丢失，但基频振荡波形与全 EMT 完全一致。

### FPGA 实时仿真性能

Cao et al. (2021) 在 Xilinx Virtex UltraScale+ FPGA 上运行 IEEE 118 的 FT-SCADA 架构：

- **FT-SCADA/RT 比**：稳态时 > 222（即比实时快 222 倍）
- **最小 FT-SCADA/RT 比**：扰动时 ≥ 101
- **EMT 时间步长**：200 $\mu$s，FPGA 时钟周期 10 ns
- **硬件资源**：3 块 VCU118 FPGA 板，总计 2,364,480 LUTs + 2,607,360 FFs（Board 1）+ 1,303,680 LUTs + 2,607,360 FFs（Board 2）
- **负载扰动测试**：Bus 25 移除 200 MW、Bus 54 移除 100 MW 后，系统频率最低降至 59.2 Hz（超出 ±1% 阈值）

### GPU 并行 BESS 仿真

Lin et al. (2023) 在 IEEE 118（3 区域、4.4 GW 总发电）上集成 BESS 的 GPU 加速结果：

- **50,000 台 BESS 仿真**：加速比达 **228×**（vs 纯 CPU）
- **200,000 台 BESS（非线性 IGBT）**：加速比约 **178×**
- **AC/DC 网格总仿真时间**：全部 Type 1 BESS 约 20 秒，含 Type 2 约 27 秒

### ML 增强 EMT 仿真

Cheng et al. (2024) 使用 4 个互联的 IEEE 118 系统构建 256 万 MLP 建模 PV 面板的测试网络：

- **加速比**：较传统 CPU 并行非线性迭代计算快 **400×**
- **验证精度**：MLP PV 模型与原始非线性模型相对误差 < 0.2%（额定工况）、< 4%（部分阴影工况）
- **GRU 风电模型**：相对误差 < 1%（风速阶跃扰动）

## 适用边界与选择指南

### IEEE 118 适合 EMT 研究的场景

| 场景 | 适用性 | 说明 |
|------|--------|------|
| DP-EMT 协同仿真基准 | ★★★★★ | 最经典用途，Mudunkotuwa 2018 已验证 |
| FPGA 实时仿真验证 | ★★★★★ | Cao 2021 已实现 FT-SCADA 架构 |
| GPU 并行 BESS 建模 | ★★★★☆ | Lin 2023 已验证 50K BESS 规模 |
| ML 增强 EMT 仿真 | ★★★★☆ | Cheng 2024 已验证 2.56M PV 面板 |
| 纯 EMT 设备级验证 | ★★☆☆☆ | 规模过大，建议用 IEEE 39-bus 或更小规模 |
| 保护继电器整定 | ★★★☆☆ | 需补充详细保护定值 |

### 与其他 IEEE 测试系统的对比

| 测试系统 | 母线数 | 发电机数 | EMT 适用场景 |
|---------|--------|---------|-------------|
| IEEE 14-bus | 14 | 5 | 算法原型验证、教学 |
| IEEE 39-bus (New England) | 39 | 10 | 中小规模 EMT、HVDC 接口 |
| IEEE 57-bus | 57 | 7 | 中等规模 EMT、保护研究 |
| **IEEE 118-bus** | **118** | **54** | **大规模 EMT 算法测试、混合仿真** |
| IEEE 300-bus | 300 | 46 | 超大规模并行仿真 |

## 相关方法 / 相关模型 / 相关主题

- [[ieee-14-bus-system]] - 14 母线小规模测试系统
- [[ieee-39-bus-system]] - 39 母线 New England 测试系统
- [[ieee-57-bus-system]] - 57 母线中等规模测试系统
- [[model-verification-benchmark]] - 模型验证与 benchmark 流程
- [[large-scale-system-simulation]] - 大规模系统仿真问题
- [[large-scale-grid-simulation]] - 大规模电网 EMT 仿真
- [[large-scale-power-system]] - 大规模电力系统仿真
- [[power-flow-calculation]] - 潮流计算
- [[optimal-power-flow]] - 最优潮流
- [[economic-dispatch]] - 经济调度
- [[parallel-computing]] - 并行计算
- [[network-partitioning]] - 网络分区
- [[model-order-reduction]] - 模型降阶
- [[co-simulation]] - 混合协同仿真
- [[frequency-dependent-modeling]] - 频变建模
- [[fdne-model]] - FDNE 模型

## 来源论文

- **Mudunkotuwa & Filizadeh (2018)** - *Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators*, Electric Power Systems Research. 在 IEEE 118 上实现 DP-EMT 协同仿真，验证了 5.26×~21.69× 加速比，是 IEEE 118 用于 EMT 混合仿真的经典案例。
- **Cao et al. (2021)** - *Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for Faster-Than-SCADA Applications*, IEEE Trans. Power Systems. 在 IEEE 118 上实现 FPGA 实时仿真，FT-SCADA/RT 比 > 222，验证了 9 阶同步机模型在大规模系统中的实时仿真能力。
- **Lin et al. (2023)** - *Massively Parallel Modeling of Battery Energy Storage Systems for AC/DC Grid High-Performance Transient Simulation*, IEEE Trans. Power Systems. 在 IEEE 118（3 区域、4.4 GW）上集成 50,000 台 BESS，GPU 加速比达 228×。
- **Cheng et al. (2024)** - *Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems*, IEEE Trans. Power Systems. 使用 4 个互联 IEEE 118 系统构建 256 万 PV 面板测试网络，实现 400× 加速比。
- **Marthi et al. (2024)** - *Benchmark High-Fidelity EMT Models for Power Grid with PV Plants*, Oak Ridge National Laboratory. 提供高保真 EMT 基准模型开发方法，适用于 IEEE 118 等大规模电网的新能源改造。
- **Zhou et al. (2021)** - *Large-scale hybrid real time simulation modeling and benchmark for Nelson River multi-infeed HVDC system*, Electric Power Systems Research. 大规模混合实时仿真建模方法，为 IEEE 118 的 RTDS 仿真提供参考。
- **Pena et al. (2018)** - *An extended IEEE 118-bus test system with high renewable penetration*, IEEE Trans. Power Systems. 提出高比例可再生能源版本的 IEEE 118 扩展系统。
