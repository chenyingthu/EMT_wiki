---
title: "IEEE 300 Bus System"
type: topic
tags: [ieee-300-bus-system, test-system, benchmark, power-system, large-scale]
created: "2026-05-04"
updated: "2026-05-18"
---

# IEEE 300 Bus System

## 定义

IEEE 300 Bus System 是电力系统分析领域的标准测试系统之一，是介于 IEEE 118-bus（118 母线）和更大规模输电网（如 1000+ 母线）之间的**中大规模 benchmark**。该系统通常包含 **300 个母线**、**约 400 条支路**（含变压器支路），是评估大规模电力系统仿真算法、潮流收敛性、协同仿真接口和网络等值方法的重要标尺。

与 IEEE 118-bus 相同，IEEE 300-bus 原始数据仅包含**正序稳态参数**（母线电压等级、支路导纳、发电机出力、负荷有功/无功），**不包含 EMT 所需的高频动态参数**（分布电容、频变线路参数、开关级换流器模型、保护定值等）。因此，其在 EMT 仿真中主要用于：① 外部交流系统等值背景；② 混合仿真（EMT-TS / DP-EMT）的基准网络；③ 并行计算加速算法的评测标尺。

## EMT 中的角色

IEEE 300-bus 在电磁暂态仿真中的定位与 IEEE 118-bus 类似，但规模更大，使其成为**大规模电力系统 EMT 研究的代表性测试用例**：

1. **大规模混合仿真基准**：作为 DP-EMT 协同仿真和 EMT-TS 接口的测试网络，验证多速率仿真和接口误差控制
2. **外部系统等值验证**：用于评估 FDNE/TLNE 等网络等值方法在中等规模系统上的精度和稳定性
3. **并行计算性能标尺**：作为 GPU/FPGA 并行 EMT 仿真加速比评测的标准算例
4. **大规模新能源并网评估**：用于评估大规模风电、光伏接入后的系统动态特性分析

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="520" fill="#ffffff" rx="8"/>
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">IEEE 300 Bus System 在 EMT 仿真中的应用架构</text>

  <!-- Central node -->
  <rect x="320" y="55" width="260" height="60" rx="12" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">IEEE 300 Bus System</text>
  <text x="450" y="100" text-anchor="middle" font-size="11" fill="#3b82f6">~300 母线 · ~400 支路 · 基准潮流数据</text>

  <!-- Arrow down -->
  <line x1="450" y1="115" x2="450" y2="145" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- EMT transformation -->
  <rect x="290" y="145" width="320" height="50" rx="10" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="165" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">EMT 改造</text>
  <text x="450" y="183" text-anchor="middle" font-size="10" fill="#22c55e">三相化 · 频变线路 · 发电机动态 · 负荷模型</text>

  <!-- Three branches -->
  <line x1="450" y1="195" x2="450" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="215" x2="220" y2="245" stroke="#333" stroke-width="1.5"/>
  <line x1="450" y1="215" x2="680" y2="245" stroke="#333" stroke-width="1.5"/>

  <!-- Left: Large-scale Co-simulation -->
  <rect x="60" y="245" width="230" height="70" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="175" y="268" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">DP-EMT 协同仿真</text>
  <text x="175" y="286" text-anchor="middle" font-size="10" fill="#b45309">大规模多速率混合仿真</text>
  <text x="175" y="302" text-anchor="middle" font-size="10" fill="#b45309">多相潮流求解 · EMT初始化</text>

  <!-- Center: Network Equivalent Testing -->
  <rect x="320" y="245" width="260" height="70" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="268" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">网络等值验证</text>
  <text x="450" y="286" text-anchor="middle" font-size="10" fill="#b45309">FDNE / TLNE 精度测试</text>
  <text x="450" y="302" text-anchor="middle" font-size="10" fill="#b45309">外网等值 · 实时仿真接口</text>

  <!-- Right: Parallel Computing -->
  <rect x="610" y="245" width="230" height="70" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="725" y="268" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">大规模并行 EMT</text>
  <text x="725" y="286" text-anchor="middle" font-size="10" fill="#b45309">GPU/FPGA 加速性能标尺</text>
  <text x="725" y="302" text-anchor="middle" font-size="10" fill="#b45309">Jalili-Marandi 2009 接口标准</text>

  <!-- Three arrows down from branches -->
  <line x1="175" y1="315" x2="175" y2="350" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="315" x2="450" y2="350" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="725" y1="315" x2="725" y2="350" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Bottom row: Application nodes -->
  <rect x="40" y="350" width="220" height="65" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="150" y="372" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">大规模新能源并网</text>
  <text x="150" y="392" text-anchor="middle" font-size="9" fill="#7c3aed">风电/光伏接入评估</text>
  <text x="150" y="406" text-anchor="middle" font-size="9" fill="#7c3aed">IBR 动态特性分析</text>

  <rect x="280" y="350" width="240" height="65" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="400" y="372" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">HVDC / FACTS 接口</text>
  <text x="400" y="392" text-anchor="middle" font-size="9" fill="#7c3aed">MMC-HVDC 建模与仿真</text>
  <text x="400" y="406" text-anchor="middle" font-size="9" fill="#7c3aed">多换流器交互因子分析</text>

  <rect x="545" y="350" width="280" height="65" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="685" y="372" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">CPU-GPU 异构并行</text>
  <text x="685" y="392" text-anchor="middle" font-size="9" fill="#7c3aed">GPU 并行 BESS 建模</text>
  <text x="685" y="406" text-anchor="middle" font-size="9" fill="#7c3aed">Lin 2023 (50K BESS 加速比 228×)</text>

  <!-- Bottom: Reliability Analysis -->
  <line x1="400" y1="415" x2="400" y2="445" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="685" y1="415" x2="685" y2="445" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="150" y1="415" x2="150" y2="445" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <rect x="60" y="445" width="780" height="55" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="450" y="468" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">系统可靠性与谐波分析</text>
  <text x="450" y="488" text-anchor="middle" font-size="10" fill="#b91c1c">电能质量评估 · 谐波潮流 · 电压暂降 · 暂态稳定性</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · IEEE 300 Bus System 在 EMT 仿真中的应用架构</p>

## 主要分支与机制

### 分支一：EMT 初始稳态初始化

将 IEEE 300-bus 的正序潮流数据转化为 EMT 仿真的初始条件，是所有后续 EMT 分析的前提。根据 [[sources/multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee.md]] 的研究，多相潮流求解需要在直角坐标下用 Newton 法处理支路电流约束，使得三相不平衡系统和含复杂接线（三角形负荷、相间电压源）的初始条件能正确收敛。

**核心方法**：以 EMTP 组装的 YBUS 表示线性网络，把非线性设备作为未知电流和约束方程加入 Newton 迭代，实现潮流约束与 EMT 初始化的统一求解。

**适用范围**：最多 500 节点级别的多相潮流-EMT 联合初始化（原文献测试规模）。

### 分支二：多速率动态相量仿真

IEEE 300-bus 作为大规模系统的代表，用于验证多速率动态相量（DP）方法在**快慢动态强耦合**场景下的有效性。根据 [[sources/multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems.md]] 的研究，系统含 HVDC、FACTS 和 IBR 等快速响应设备时，全系统 EMT 会让所有变量被迫采用最小 EMT 步长，运行时间过高。

**核心方法**：将状态/方程按动态速度分组：慢组（最慢发电机变量及控制器）采用大步长 $T_s$，快组（网络、电力电子）采用小步长 $T_f$。慢步长内用插值获得慢变量值驱动快方程：

$$\boldsymbol{x}_s(t) \approx \boldsymbol{x}_s(t_0) + \frac{t - t_0}{T_s} \bigl(\boldsymbol{x}_s(t_0 + T_s) - \boldsymbol{x}_s(t_0)\bigr)$$

快方程完成后，将快变量在慢步长窗口内做平均驱动慢方程：

$$\overline{\boldsymbol{x}}_f = \frac{1}{T_s} \int_{t_0}^{t_0+T_s} \boldsymbol{x}_f(\tau) \, d\tau$$

慢步长末端计算不匹配量（mismatch）：

$$\Delta \boldsymbol{x}_s = \bigl\| \boldsymbol{x}_s^{\text{interp}}(t_0 + T_s) - \boldsymbol{x}_s^{\text{coupled}}(t_0 + T_s) \bigr\|$$

若 $\|\Delta \boldsymbol{x}_s\| > \varepsilon_{\text{mismatch}}$，则撤销该步并用改进慢变量估计重算。

**性能提升**：在 IEEE 300-bus 级别的大电网上，相比单速率全 EMT 仿真可实现数量级加速比。

### 分支三：大规模 BESS 并行 EMT 建模

IEEE 300-bus 交直流电网中大量分布式电池储能单元（BESS）与电网的相互作用，需要 [[sources/massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high.md]] 提出的 CPU-GPU 异构框架：设备级 BESS EMT 计算在 GPU 上并行执行，系统级 TS 计算在 CPU 上推进。

**核心方法**：利用 GPU 多线程、多流能力进行异步顺序-并行处理，同时采用多速率机制降低重复计算。BESS 侧以电池等效电压、SOC、电流为核心状态，写成适合 GPU 逐元素计算的可向量化形式。

**量化数据**：在含 50K BESS 单元的 IEEE 300-bus 级别电网上，GPU 并行方案实现约 228× 加速比（Lin 2023）。

### 分支四：外部系统等值与实时仿真

IEEE 300-bus 用于评估实时数字仿真中"研究区域—外部系统"划分后的外部等值方法。根据 [[sources/real-time-transient-simulation-based-on-a-robust.md]] 的研究，外部系统等值需要在宽频带范围内同时保证准确性和低阶无源性。

**核心方法**：将外部系统分为表层频变传输线（TLNE）和深层低阶 FDNE；用向量拟合法构造表层导纳子矩阵，深层通过约束非线性最小二乘优化拟合，并施加稳定极点和正实性约束。

**典型应用**：继电保护闭环测试、数字控制器硬件在环（HIL）测试，要求外部等值在直流、工频和暂态高频范围均保持无源性。

## 关键技术挑战

### 挑战一：多相潮流收敛性

IEEE 300-bus 的三相化版本在含三角形负荷、相间电压源等非标准节点时，纯单相潮流无法处理，必须使用多相潮流求解器。挑战在于：

- 三相不平衡系统的 Jacobian 矩阵不对称，收敛性差
- 复杂接线方式的约束方程建模复杂
- EMTP 组装的 YBUS 与潮流求解器的接口一致性

设节点电压为 $\boldsymbol{V} \in \mathbb{C}^{n}$，已知电流源为 $\boldsymbol{I}_s$，非线性设备贡献的未知电流为 $\boldsymbol{I}_u$，则 KCL 约束为：

$$\begin{bmatrix} \boldsymbol{Y} \end{bmatrix} \boldsymbol{V} = \boldsymbol{I}_s + \boldsymbol{I}_u$$

Newton 迭代时，非线性约束方程的 Jacobian 为：

$$\boldsymbol{J}(\boldsymbol{x}) = \begin{bmatrix} \dfrac{\partial \boldsymbol{f}}{\partial \boldsymbol{V}} & \dfrac{\partial \boldsymbol{f}}{\partial \boldsymbol{I}_u} \\ \dfrac{\partial \boldsymbol{g}}{\partial \boldsymbol{V}} & \dfrac{\partial \boldsymbol{g}}{\partial \boldsymbol{I}_u} \end{bmatrix}$$

其中 $\boldsymbol{f}$ 为 KCL 方程残差，$\boldsymbol{g}$ 为元件约束方程残差。

### 挑战二：多速率接口误差控制

IEEE 300-bus 作为大规模系统，快慢动态强耦合带来接口误差问题：

- 慢变量插值带来的预测误差
- 快变量平均对慢方程的能量注入偏差
- 慢步长末端不匹配量的校验与回退机制

### 挑战三：大规模并行计算的通信开销

在 CPU-GPU 异构框架中：

- GPU 侧 BESS 模型数量庞大（50K+ 单元）时的线程调度
- CPU-GPU 数据传输带宽成为瓶颈
- 多速率与并行的协同调度

### 挑战四：外部等值的有源性保持

网络等值方法在宽频带范围内的无源性约束是关键挑战：

- 多端口 FDNE 的正实性约束
- TLNE 的直流响应和低频响应精度
- 全局优化与约束最小二乘的计算效率

## 量化性能边界

| 应用方向 | 代表方法 | 性能指标 | 来源 |
|---------|---------|---------|------|
| 潮流-EMT 初始化 | Newton 支路电流约束法 | 适用于最多 500 节点三相系统 | [[sources/multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee.md]] |
| 多速率 DP-EMT | 慢变量插值 + 快变量平均 | 数量级加速比（相比全 EMT） | [[sources/multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems.md]] |
| 大规模 BESS 并行 | CPU-GPU 异构 + 向量化 | 50K BESS 加速比 228× | [[sources/massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high.md]] |
| 外部系统等值 | TLNE + 约束最小二乘 | 直流 ~ 工频 ~ 暂态高频宽频带准确 | [[sources/real-time-transient-simulation-based-on-a-robust.md]] |
| 并行计算 | 多流异步 GPU 处理 | GPU 多线程/多流并行 | [[sources/massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high.md]] |

## 适用边界与选择指南

**IEEE 300-bus 适用于**：
- 中大规模电力系统（300 母线级别）的 EMT 仿真算法验证
- 需要潮流初始化 → EMT 瞬态分析完整流程的联合仿真研究
- 大规模新能源（风电、光伏、BESS）接入系统的动态特性分析
- 并行计算加速比的性能评测

**IEEE 300-bus 不适用于**：
- 超大规模系统（>1000 母线）的实时仿真性能标尺（应用 IEEE 118-bus 或更大规模测试系统）
- 需要高频开关细节的换流器设计研究（需换流器专项测试系统）
- 配电网级别（<100 节点）的精细化电能质量分析（需配电网专项测试系统）

**测试系统选择对照**：

| 系统规模 | 推荐测试系统 | 典型应用 |
|---------|------------|---------|
| 小规模（<50 母线） | IEEE 30-bus | 算法原型验证、基础 EMT 概念 |
| 中等规模（50~200 母线） | IEEE 118-bus | 并行计算标尺、协同仿真接口 |
| 中大规模（200~500 母线） | IEEE 300-bus | 大规模 BESS、新能源并网、多速率仿真 |
| 大规模（>500 母线） | IEEE 118-bus 扩展 / 自定义大规模系统 | 超大规模并行 EMT、实时仿真 |

## 相关页面

- [[topics/test-system/ieee-118-bus-system.md]] - IEEE 118 母线测试系统（中规模 benchmark）
- [[topics/test-system/ieee-39-bus-system.md]] - IEEE 39 母线测试系统（New England，含同步机动态）
- [[topics/tools-software/power-system.md]] - 电力系统建模总览
- [[topics/simulation/emt-simulation.md]] - EMT 仿真基础
- [[topics/simulation/electromechanical-electromagnetic-hybrid-simulation.md]] - 机电-电磁混合仿真
- [[topics/simulation/real-time-simulation.md]] - 实时仿真技术
- [[methods/simulation-technology/multirate-method.md]] - 多速率仿真方法
- [[topics/modeling-methods/network-equivalent.md]] - 网络等值方法

## 来源论文

- [[sources/multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee.md]] — 多相潮流求解器：直角坐标 Newton 法支路电流约束，适用于最多 500 节点三相系统与 EMTP 联合初始化
- [[sources/multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems.md]] — 多速率动态相量仿真：慢变量插值+快变量平均框架，用于大规模电力系统的快慢动态耦合仿真
- [[sources/massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high.md]] — CPU-GPU 异构并行 BESS 建模：50K BESS 单元在 IEEE 300-bus 级别电网上实现 228× 加速比
- [[sources/real-time-transient-simulation-based-on-a-robust.md]] — 鲁棒暂态实时仿真：TLNE+FDNE 两层外部等值，宽频带无源性约束用于继电保护 HIL 测试