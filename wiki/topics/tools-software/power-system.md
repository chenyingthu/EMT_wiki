---
title: "电力系统 (Power System)"
type: topic
tags: [power-system, electric-grid, network, generation, load, operation, emt-simulation, large-scale, parallel-computing]
created: "2026-05-06"
updated: "2026-05-13"
---

# 电力系统 (Power System)

## 定义

电力系统是由发电、输电、变电、配电、负荷以及保护控制装置构成的能量生产、传输和消费整体。在 EMT（电磁暂态）仿真语境下，电力系统被建模为一个由网络方程、动态元件状态方程、控制器方程和离散事件逻辑共同组成的**大规模耦合微分-代数方程组（DAE）**。

在 EMT Wiki 中，电力系统是上位主题入口，用于串联网络、设备、控制、运行和暂态现象。它不替代具体方法页、模型页或测试系统页，而是提供系统层面的组织框架、计算挑战和规模化边界。

## EMT 中的角色

EMT 仿真把电力系统视为一个多时间尺度耦合的时域系统。其核心角色体现在以下三个层面：

### 1. 多时间尺度耦合

电力系统 EMT 仿真必须同时捕捉从微秒级（开关瞬态、行波传播）到秒级（机电振荡、控制响应）的宽频动态。正如 Filizadeh 等人（2025）所述，传统简化相量模型在 IBR（逆变器主导资源）高渗透率电网中已不再充分，因为 IBR 控制器的快速响应（毫秒级）与电力电子开关（微秒级）之间的耦合会产生相量仿真无法捕捉的复杂动态行为。

### 2. 大规模网络求解挑战

现实电力系统包含数千至数万节点，EMT 仿真每步需要求解 $10^4$ 至 $10^5$ 维的节点导纳方程。以 Hydro-Québec 2023 年配置为例，其 EMT 模型包含 1666 个三相母线、432 条线路、338 台三相变压器、111 台电机、90405 个控制块（Le-Huy 等，2023）。如此规模下，网络矩阵的形成、稀疏化和求解成为计算瓶颈。

### 3. 多工具协同仿真

随着系统规模增长，单一 EMT 仿真已无法满足计算需求，混合/联合仿真（co-simulation）成为必要策略。Filizadeh 等人（2025）展示了 EMT-EMT 联合仿真（基于 FMI 标准）和 EMT-DP（电磁-相量域）混合仿真的架构，其中 FDNE 模型降阶可将 CPU 时间从 26s 降至 12s（2.16 倍加速），在 12 个 CPU 上实现 14.4 倍加速。

## 电力系统建模框架

### 网络方程

EMT 仿真中电力系统网络方程基于**节点导纳法**（Nodal Admittance Method），由 Dommel（1986）在 EMTP 理论中确立。对任意 R-L-C 电路，使用梯形积分法离散化后，每个元件转化为 Norton 等效电路（电导 + 历史电流源）：

$$i(t) = \frac{v(t)}{R_{eq}} + i_{hist}(t - \Delta t)$$

其中历史电流为：

$$i_{hist}(t - \Delta t) = a \cdot i(t - \Delta t) + b \cdot v(t - \Delta t)$$

对 R-L-C 元件，系数 $a, b$ 和等效电阻 $R_{eq}$ 由数值积分方法确定。为抑制梯形积分产生的数值振荡（Alvarado, 1982），需在电感并联人工电阻 $R_p \approx 40L/(3\Delta t)$、在电容串联人工电阻 $R_s \approx 3\Delta t/(40C)$。

网络方程整体形式为：

$$\mathbf{G}\mathbf{v}(t) = \mathbf{i}_{src}(t) + \mathbf{i}_{hist}(t - \Delta t)$$

其中 $\mathbf{G}$ 为节点导纳矩阵，$\mathbf{v}(t)$ 为节点电压向量，$\mathbf{i}_{src}$ 为注入电流源，$\mathbf{i}_{hist}$ 为历史电流向量。

### 状态空间方程

对于旋转电机、电力电子变流器等动态元件，采用状态空间描述：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

$$\mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

其中 $\mathbf{x}$ 为状态变量（转子角、转速、磁链等），$\mathbf{u}$ 为输入（端电压、励磁电压等），$\mathbf{y}$ 为输出（电磁转矩、电流等）。

**状态空间-节点混合方法（SSN）**（Dufour & Mahseredjian, 2011）将状态空间方程离散化为 Norton 等效形式后，嵌入全局节点导纳矩阵：

$$\mathbf{I}(t) = \mathbf{Y}\mathbf{V}(t) + \mathbf{I}_{ne}(t)$$

其中 $\mathbf{I}_{ne}$ 为状态空间组的 Norton 等效历史电流。该方法允许不同子系统使用不同求解器，并支持独立预计算的开关拓扑矩阵集。

### 系统初始化

EMT 仿真的初始化对保证数值稳定性和减少开机瞬态至关重要。ParaEMT（Xiong 等，2024）采用正序潮流（Newton-Raphson 法）求解稳态工作点，然后将相量电压转换为三相波形：

$$v_a = V_{mag} \cos(\angle V_{ang})$$
$$v_b = V_{mag} \cos(\angle V_{ang} - 2\pi/3)$$
$$v_c = V_{mag} \cos(\angle V_{ang} + 2\pi/3)$$

对于同步发电机等动态模型，通过控制框图方程的**反向传播**（backward propagation）初始化状态变量。目前自动初始化仅支持平衡稳态，非平衡、未换位线路和含谐波的电力电子系统初始化仍是开放问题。

## EMT 求解方法体系

电力系统 EMT 仿真涉及多种求解方法，按时间尺度和建模深度可分为三个层级：

### 层级 1：全 EMT 仿真

全 EMT 仿真使用 50–100 $\mu s$ 时间步长，对全网所有元件进行瞬时值建模。适用于：
- 子同步振荡分析
- 故障行波传播
- IBR 控制-电力电子耦合动态
- 保护系统误操作研究

**优势**：精度最高，覆盖全频带动态（从 DC 到数百 kHz）。
**局限**：计算复杂度随系统规模呈 $O(n^{1.5})$ 至 $O(n^2)$ 增长（Zhou & Dinavahi, 2014），大规模系统仿真时间不可接受。

### 层级 2：混合/联合仿真

混合仿真将系统划分为 EMT 区域和相量域（DP）区域，两者通过接口交换边界信息。Filizadeh 等人（2025）展示了两种架构：

**EMT-EMT 联合仿真**：通过 FMI（Functional Mock-up Interface）标准将不同仿真工具的模型实例链接，支持并行计算。

**EMT-DP 混合仿真**：在 EMT 区域使用详细模型，在 DP 区域使用相量模型。FDNE（频域网络等效）模型通过约 77 个极点实现高精度降阶，将计算时间从 26s 降至 12s。

### 层级 3：相量域仿真

相量域仿真（Time Domain / Phasor Domain）使用毫秒级时间步长，仅模拟正序分量。Hassani 等人（2022）在 IEEE-118 系统上比较了四种方法：

| 方法 | 时间步长 | 适用场景 | 局限 |
|------|----------|----------|------|
| TD（时域） | 0.1–0.5 ms | 不平衡故障、谐波 | 计算量大 |
| DP（相量域） | 10–100 ms | 机电振荡、频率响应 | 无法捕捉 IBR 高频动态 |
| 3pPD（三相相量） | 1–10 ms | 三相不平衡系统 | 需要额外推导 |
| EMT | 20–100 $\mu s$ | 全频带暂态 | 计算成本最高 |

## 大规模电力系统 EMT 的加速技术

### 1. GPU 并行仿真

Zhou & Dinavahi（2014）开发了 MT-EMTP（大规模线程 EMT 程序），在 NVIDIA Fermi GPU 上对线性无源元件、通用线路模型（ULM）和通用电机模型（UMM）实现大规模线程并行。通过**节点映射结构（NMS）**和**块节点调整（BNA）**方法，将原始导纳矩阵重组为块对角稀疏格式。

**性能结果**（IEEE 39 节点系统扩展测试）：

| 系统规模 | 母线数 | EMTP-RV 时间 (s) | MT-EMTP 时间 (s) | 加速比 |
|----------|--------|-------------------|-------------------|--------|
| Scale 1 | 39 | 0.42 | 0.51 | 0.82x |
| Scale 10 | 390 | 4.18 | 1.52 | 2.75x |
| Scale 30 | 1170 | 35.6 | 5.83 | 6.11x |
| Scale 63 | 2458 | 245.3 | 43.6 | 5.63x |

当系统规模增至原始 IEEE 39 节点的 63 倍（2458 三相母线）时，GPU 加速比达到 5.63 倍。

Song 等人（2018）提出了**线程导向变换**方法，将电力系统表示为基元电气元件的连接网络，计算简化为**乘加融合（FMA）操作**。在 NVIDIA P100 上，对含 30 个 PV 控制系统的 IEEE 33 节点配电网实现了实时仿真（50 $\mu s$ 步长）。

### 2. HPC 集群并行仿真

ParaEMT（Xiong 等，2024）采用**边界块对角（BBD）矩阵分解**策略，将网络导纳矩阵分解为多个子块并通过边界节点耦合。在 NREL Eagle HPC 集群上，对合成 10080 母线系统（由 6×7 个 240 母线 WECC 系统通过新增输电线路互联）进行仿真：

| MPI 等级数 | 网络分区数 | 1s 仿真时间 (s) | 加速比 |
|------------|-----------|-----------------|--------|
| 1 | 1 | 5200 | 1.0x |
| 14 | 14 | 260 | 20x |
| 42 | 42 | 145 | 36x |
| 84 | 84 | 168 | 31x |

**最佳加速比 36x** 在 42 个网络分区时达到。超过 42 个分区后，由于 BBD 角矩阵非零元素随分区数增加，同步计算成本抵消了并行收益。网络求解占总计算时间的 60% 以上，是并行加速的主要瓶颈。

### 3. 模型降阶与等值

Filizadeh 等人（2025）展示了 FDNE（频域网络等效）模型降阶技术，通过保留关键频率范围内的阻抗特性，将高频模型极点数从数百个减少至约 77 个，在不损失精度的前提下实现显著加速。Gao（2022）的 Kron 消去端口等效方法在 PET（电力电子变压器）建模中实现 10–100 倍加速。

## 形式化表达

### 系统级耦合方程

电力系统 EMT 仿真可形式化为以下耦合 DAE 系统：

**网络节点方程：**

$$\mathbf{G}\mathbf{v}(t) = \mathbf{i}_{net}(t) + \mathbf{i}_{comp}(t) + \mathbf{i}_{hist}(t - \Delta t)$$

其中 $\mathbf{i}_{comp}$ 为复合元件（变压器、电机、变流器）的注入电流，$\mathbf{i}_{hist}$ 为线性元件的历史电流。

**元件动态方程：**

$$\dot{\mathbf{x}}_k = \mathbf{A}_k\mathbf{x}_k + \mathbf{B}_k\mathbf{u}_k, \quad k = 1, \ldots, N_{comp}$$

**控制方程：**

$$\mathbf{u}_k = \mathbf{K}_k(\mathbf{y}_k, \mathbf{r}_k, \sigma_k)$$

其中 $\sigma_k$ 为离散事件信号（保护动作、模式切换等）。

**数值积分（梯形法）：**

$$\mathbf{x}_k(t) = \mathbf{x}_k(t - \Delta t) + \frac{\Delta t}{2}\left[\dot{\mathbf{x}}_k(t) + \dot{\mathbf{x}}_k(t - \Delta t)\right]$$

### 并行 BBD 分解

对于 BBD 分解的网络：

$$\mathbf{G} = \begin{bmatrix} \mathbf{G}_{11} & & \mathbf{G}_{1b} \\ & \ddots & \\ \mathbf{G}_{b1} & \cdots & \mathbf{G}_{bb} \end{bmatrix}$$

其中 $\mathbf{G}_{ii}$ 为第 $i$ 个子网的导纳矩阵（可并行求解），$\mathbf{G}_{ib}$ 为子网与边界的耦合矩阵。

## 关键技术挑战

### 1. 计算可扩展性

随着 IBR 渗透率提升，电力系统 EMT 仿真规模从数百节点扩展至数万节点。Zhou & Dinavahi（2014）指出，CPU 基于串行算法的复杂度为 $O(n^2)$ 至 $O(n^3)$，而 GPU 并行可实现 $O(n)$ 的线性复杂度。然而，BBD 分解的性能受分区数和角矩阵维度限制——当分区超过最优值（42 分区）后，加速比反而下降（Xiong 等，2024）。

### 2. 模型兼容性

不同 EMT 仿真工具（EMTP-RV、PSCAD、HYPERSIM、ParaEMT）的模型库存在差异。Le-Huy 等人（2023）在将 Hydro-Québec 大系统从 EMTP 移植到 HYPERSIM 时发现，模型兼容层并非 trivial——默认参数可能影响振荡阻尼特性，某些离线组件在实时环境中没有直接等价物，必须从零构建或使用用户代码模型（UCM）。

### 3. 初始化问题

离线 EMT 仿真追求"完美稳态"初始条件，而实时仿真因物理时间常数限制无法等待系统收敛。ParaEMT 采用正序潮流 + 相量-三相转换的初始化策略，但尚未支持非平衡稳态、未换位线路和含谐波电力电子系统的自动初始化（Xiong 等，2024）。

### 4. IBR 高渗透率下的建模挑战

Filizadeh 等人（2025）明确指出，当电网中 IBR 占比超过 50% 时，传统简化相量模型不再适用。IBR 控制器的快速电流限幅、锁相环（PLL）动态与电网阻抗之间的耦合会产生次同步振荡和宽频谐振，必须使用 EMT 级别的详细模型。

## 量化性能边界

### 规模化验证

- **Hydro-Québec 2023 配置**：1666 个三相母线、111 台电机、432 条线路、90405 个控制块。离线 EMTP 与实时 HYPERSIM 的潮流解匹配误差：有功 8 MW（0.02%）、无功 35 Mvar（0.83%）（Le-Huy 等，2023）。
- **ParaEMT 10080 母线系统**：在 NREL Eagle HPC 上 42 分区实现 36 倍加速，1s EMT 仿真仅需 145s（50 $\mu s$ 步长），非并行版本需 5200s（Xiong 等，2024）。
- **MT-EMTP 2458 母线系统**：在 GPU 上实现 5.63 倍加速，仿真规模达原始 IEEE 39 节点的 63 倍（Zhou & Dinavahi, 2014）。

### 方法对比加速

- **FDNE 模型降阶**：CPU 时间从 26s 降至 12s（2.16 倍），12 CPU 并行 14.4 倍（Filizadeh 等，2025）。
- **Kron 消去等效**：10–100 倍加速（Gao, 2022）。
- **ImEx-Gear 方法**：60 子模块 SST 在 OPAL-RT 上实现 171 倍加速比，稳态误差 < 0.5%（Li, 2026）。

### 实时仿真可行性

Song 等人（2018）在 NVIDIA P100 上，对含 50 个 PV 控制系统的 IEEE 33 节点配电网实现了 50 $\mu s$ 步长的实时仿真。当使用 100 $\mu s$ 步长时，100 个 PV 系统仍可保证实时性能。

## 适用边界与选择指南

### 方法选择指南

| 应用场景 | 推荐方法 | 时间步长 | 系统规模上限 |
|----------|----------|----------|-------------|
| 全系统机电振荡 | 相量域（DP） | 10–100 ms | 全规模 |
| IBR 次同步振荡 | 全 EMT | 20–100 $\mu s$ | 百节点（CPU）/ 万节点（HPC） |
| 故障行波传播 | 全 EMT + ULM | 1–10 $\mu s$ | 百节点 |
| 大规模系统 EMT | EMT-DP 混合 | 50–100 $\mu s$（EMT区） | 全规模 |
| 实时控制验证 | GPU EMT 或 HIL | 20–100 $\mu s$ | 百节点 |

### 工具选择指南

| 需求 | 推荐工具 | 理由 |
|------|----------|------|
| 研究/算法验证 | ParaEMT | 开源、HPC 兼容、代码透明 |
| 工业级仿真 | PSCAD / EMTP-RV | 成熟模型库、技术支持 |
| 实时/硬件在环 | HYPERSIM / OPAL-RT | 实时执行、物理 I/O |
| 大规模并行 | ParaEMT + Eagle HPC | 36 倍加速验证 |

## 方法体系架构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="450" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#333" font-family="sans-serif">电力系统 EMT 仿真方法体系架构</text>

  <!-- Layer 1: 应用场景层 -->
  <rect x="30" y="42" width="195" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="127" y="62" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">子同步振荡分析</text>
  <text x="127" y="78" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">IBR 控制-电网耦合</text>

  <rect x="235" y="42" width="195" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="332" y="62" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">故障行波传播</text>
  <text x="332" y="78" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">微秒级开关瞬态</text>

  <rect x="440" y="42" width="195" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="537" y="62" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">宽频谐振研究</text>
  <text x="537" y="78" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">次同步/超同步振荡</text>

  <rect x="645" y="42" width="195" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="742" y="62" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">保护系统验证</text>
  <text x="742" y="78" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">误操作与误动分析</text>

  <!-- Arrow 1 -->
  <line x1="450" y1="97" x2="450" y2="115" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Layer 2: 仿真方法层 -->
  <rect x="30" y="118" width="215" height="55" rx="6" ry="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="137" y="138" text-anchor="middle" font-size="12" fill="#166534" font-weight="bold" font-family="sans-serif">全 EMT 仿真</text>
  <text x="137" y="154" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">50–100 μs 步长 / 瞬时值</text>

  <rect x="260" y="118" width="215" height="55" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="367" y="138" text-anchor="middle" font-size="12" fill="#92400e" font-weight="bold" font-family="sans-serif">EMT-DP 混合仿真</text>
  <text x="367" y="154" text-anchor="middle" font-size="10" fill="#f59e0b" font-family="sans-serif">电磁+相量域 / FDNE 降阶</text>

  <rect x="490" y="118" width="215" height="55" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="597" y="138" text-anchor="middle" font-size="12" fill="#92400e" font-weight="bold" font-family="sans-serif">EMT-EMT 联合仿真</text>
  <text x="597" y="154" text-anchor="middle" font-size="10" fill="#f59e0b" font-family="sans-serif">FMI 标准 / 跨工具并行</text>

  <rect x="720" y="118" width="150" height="55" rx="6" ry="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="795" y="138" text-anchor="middle" font-size="12" fill="#166534" font-weight="bold" font-family="sans-serif">相量域仿真</text>
  <text x="795" y="154" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">10–100 ms / 正序分量</text>

  <!-- Arrow 2 -->
  <line x1="450" y1="173" x2="450" y2="191" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Layer 3: 数值求解层 -->
  <rect x="30" y="194" width="280" height="55" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="170" y="214" text-anchor="middle" font-size="12" fill="#5b21b6" font-weight="bold" font-family="sans-serif">节点导纳法</text>
  <text x="170" y="230" text-anchor="middle" font-size="10" fill="#8b5cf6" font-family="sans-serif">G·v = i_src + i_hist / 梯形积分</text>

  <rect x="325" y="194" width="280" height="55" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="465" y="214" text-anchor="middle" font-size="12" fill="#5b21b6" font-weight="bold" font-family="sans-serif">状态空间法</text>
  <text x="465" y="230" text-anchor="middle" font-size="10" fill="#8b5cf6" font-family="sans-serif">x' = Ax + Bu / SSN 混合</text>

  <rect x="620" y="194" width="250" height="55" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="745" y="214" text-anchor="middle" font-size="12" fill="#5b21b6" font-weight="bold" font-family="sans-serif">BBD 分解求解</text>
  <text x="745" y="230" text-anchor="middle" font-size="10" fill="#8b5cf6" font-family="sans-serif">并行子块求解 / MPI 同步</text>

  <!-- Arrow 3 -->
  <line x1="450" y1="249" x2="450" y2="267" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Layer 4: 计算加速层 -->
  <rect x="30" y="270" width="210" height="55" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="135" y="290" text-anchor="middle" font-size="12" fill="#991b1b" font-weight="bold" font-family="sans-serif">CPU 串行</text>
  <text x="135" y="306" text-anchor="middle" font-size="10" fill="#ef4444" font-family="sans-serif">O(n²)–O(n³) / 基准</text>

  <rect x="255" y="270" width="210" height="55" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="360" y="290" text-anchor="middle" font-size="12" fill="#991b1b" font-weight="bold" font-family="sans-serif">GPU 并行</text>
  <text x="360" y="306" text-anchor="middle" font-size="10" fill="#ef4444" font-family="sans-serif">MT-EMTP / 5.63x 加速</text>

  <rect x="480" y="270" width="210" height="55" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="585" y="290" text-anchor="middle" font-size="12" fill="#991b1b" font-weight="bold" font-family="sans-serif">HPC 集群</text>
  <text x="585" y="306" text-anchor="middle" font-size="10" fill="#ef4444" font-family="sans-serif">ParaEMT + MPI / 36x 加速</text>

  <rect x="705" y="270" width="165" height="55" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="787" y="290" text-anchor="middle" font-size="12" fill="#991b1b" font-weight="bold" font-family="sans-serif">模型降阶</text>
  <text x="787" y="306" text-anchor="middle" font-size="10" fill="#ef4444" font-family="sans-serif">FDNE / Kron / 2–100x</text>

  <!-- Arrow 4 -->
  <line x1="450" y1="325" x2="450" y2="343" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Layer 5: 元件建模层 -->
  <rect x="30" y="346" width="210" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="135" y="366" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">线路/电缆</text>
  <text x="135" y="382" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">ULM / JMarti 频变模型</text>

  <rect x="255" y="346" width="210" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="360" y="366" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">变压器</text>
  <text x="360" y="382" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">漏抗 / 饱和模型</text>

  <rect x="480" y="346" width="210" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="585" y="366" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">同步电机</text>
  <text x="585" y="382" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">qd 轴模型 / Thevenin 接口</text>

  <rect x="705" y="346" width="165" height="55" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="787" y="366" text-anchor="middle" font-size="12" fill="#1e40af" font-weight="bold" font-family="sans-serif">IBR / 电力电子</text>
  <text x="787" y="382" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="sans-serif">GFM / GFL / 开关模型</text>

  <!-- Arrow marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>

  <!-- Legend -->
  <rect x="30" y="420" width="12" height="12" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="48" y="431" font-size="10" fill="#666" font-family="sans-serif">应用场景</text>
  <rect x="140" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="158" y="431" font-size="10" fill="#666" font-family="sans-serif">仿真方法</text>
  <rect x="230" width="12" height="12" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="248" y="431" font-size="10" fill="#666" font-family="sans-serif">混合仿真</text>
  <rect x="310" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="328" y="431" font-size="10" fill="#666" font-family="sans-serif">数值求解</text>
  <rect x="400" width="12" height="12" rx="2" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="418" y="431" font-size="10" fill="#666" font-family="sans-serif">计算加速</text>

  <!-- Source note -->
  <text x="450" y="470" text-anchor="middle" font-size="9" fill="#999" font-family="sans-serif">数据来源：Filizadeh 2025, Xiong 2024, Zhou &amp; Dinavahi 2014, Song 2018, Le-Huy 2023, Hassani 2022</text>
  <text x="450" y="490" text-anchor="middle" font-size="9" fill="#999" font-family="sans-serif">图1 · 电力系统 EMT 仿真方法体系架构 — 从应用场景到元件建模的五层技术栈</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 电力系统 EMT 仿真方法体系架构 — 从应用场景到元件建模的五层技术栈</p>

## 相关方法 / 相关模型 / 相关主题

- [[electromagnetic-transient]] — EMT 仿真基础概念与物理现象
- [[power-system-network]] — 电力系统网络建模
- [[control-system]] — 控制与保护系统建模
- [[large-scale-power-system]] — 大规模系统 EMT 仿真
- [[real-time-simulation]] — 实时仿真与硬件在环
- [[model-order-reduction]] — 模型降阶技术
- [[parallel-in-time]] — 时间并行算法
- [[gpu-parallel-acceleration]] — GPU 加速 EMT 仿真
- [[hybrid-simulation]] — 混合/联合仿真方法
- [[steady-state-initialization]] — EMT 仿真初始化
- [[power-flow-calculation]] — 潮流计算与稳态求解
- [[transmission-network]] — 输电网络建模
- [[distribution-network]] — 配电网络建模
- [[renewable-energy-integration]] — 新能源接入
- [[hil-simulation]] — 硬件在环仿真

## 来源论文

- **Filizadeh 等 (2025)** — "Electromagnetic Transient Modeling and Simulation of Large Power Systems: EMT Simulators for the Future Grid" — 综述大规模电力系统 EMT 仿真器的发展，提出混合/联合仿真架构，展示 FDNE 模型降阶和并行计算性能（2.16x–14.4x 加速）。
- **Xiong 等 (2024)** — "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids" — 开发了首个开源 HPC 兼容 EMT 仿真器，BBD 矩阵分解在 10080 母线系统上实现 36 倍加速。
- **Zhou & Dinavahi (2014)** — "Parallel Massive-Thread Electromagnetic Transient Simulation on GPU" — 开发了 MT-EMTP GPU 并行 EMT 仿真程序，节点映射结构和块对角重组技术在 2458 母线系统上实现 5.63 倍加速。
- **Song 等 (2018)** — "Efficient GPU-based Electromagnetic Transient Simulation for Power Systems with Thread-oriented Transformation and Automatic Code Generation" — 提出线程导向变换和自动代码生成技术，在 NVIDIA P100 上实现含 PV 控制系统的实时仿真。
- **Le-Huy 等 (2023)** — "Lessons Learned in Porting Offline Large-Scale Power System Simulation to Real-Time for Wide-Area Monitoring, Protection and Control" — 分享了 Hydro-Québec 大系统从 EMTP 移植到 HYPERSIM 的实践经验，包含 1666 母线系统的详细建模数据。
- **Hassani 等 (2022)** — "Evaluation of Time-Domain and Phasor-Domain Methods for Power System Transients" — 在 IEEE-118 系统上比较 TD、DP、3pPD 和 EMT 四种方法，为方法选择提供量化依据。
- **Dufour & Mahseredjian (2011)** — "A Combined State-Space Nodal Method for the Simulation of Power System Transients" — 提出状态空间-节点混合方法（SSN），允许不同子系统使用不同求解器。
- **Misyris (2021)** — GFM 控制的时间尺度分离分析，RMS/EMT 模型选择的充分条件。
- **Gao (2022)** — Kron 消去端口等效方法，10–100 倍加速验证。
- **Li (2026)** — ImEx-Gear 隐式-显式方法，171 倍加速比。

## 证据边界

本页提供的技术细节、公式和性能数据均来源于上述来源论文。具体设备建模（同步电机、电力电子变流器、线路模型等）、控制策略（PLL、GFM/GFL 控制）、保护系统和分析方法应回到对应页面获取深度内容。
