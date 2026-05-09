---
title: "PSCAD/EMTDC"
type: entity
entity_type: tool
tags: [pscad, emtdc, manitoba, simulation-tool]
created: "2026-04-13"
---

# PSCAD/EMTDC

## 概述

PSCAD/EMTDC 是由加拿大曼尼托巴大学（University of Manitoba）和曼尼托巴水电国际公司（Manitoba Hydro International）开发的电力系统电磁暂态仿真软件。

## 核心原理详解

PSCAD 是图形化建模环境，EMTDC 是时域 EMT 求解引擎。其基本计算仍可概括为：把网络元件离散为伴随电路，形成节点导纳矩阵，在每个微秒级时间步求解瞬时电压和电流。

$$
G_{\mathrm{eq},L}=\frac{\Delta t}{2L}, \qquad
G_{\mathrm{eq},C}=\frac{2C}{\Delta t}
$$

这些等效导纳和历史源使电感、电容、变压器、线路和电力电子开关可以统一进入节点方程。PSCAD/EMTDC 在 EMT Wiki 中的意义不是单一算法，而是大量论文用来提供“可信详细模型基准”的工具：新方法经常通过与 PSCAD 波形对比来证明精度。

## 特点

- 图形化建模界面（PSCAD）
- EMTDC求解引擎
- 广泛应用于工业界和学术界
- 支持用户自定义模型

## 关键技术

- 节点分析法（Nodal Analysis）
- 伴随电路模型
- 梯形积分法
- 稀疏矩阵求解

## 关键技术详解

| 技术面 | 作用 | Wiki 关联 |
|-------|------|-----------|
| 详细电力电子建模 | 保留开关、控制、保护和高频暂态，是平均模型和等效模型的常用基准 | [[average-value-model]], [[mmc-model]] |
| 自定义组件 | 支持用户实现新控制器、新接口模型和实验算法 | [[co-simulation]], [[dynamic-phasor]] |
| 线路/电缆模型 | 支持行波、频率相关参数和宽频暂态分析 | [[cable-modeling]], [[transmission-line-model]] |
| 混合仿真接口 | 常与 PSS/E、E-TRAN、RTDS 或自定义接口用于 EMT/TS 联合仿真 | [[co-simulation]] |

## 代表性用途

| 用途 | PSCAD/EMTDC 在论文中的角色 | 审核重点 |
|------|-----------------------------|----------|
| 新型换流器或 MMC 模型验证 | 作为详细开关级或详细等效模型基准 | 是否说明子模块数量、控制采样、死区、时间步长 |
| HVDC/FACTS 控制策略 | 承载主电路、控制器和故障工况 | 是否有对比控制策略和扰动设置 |
| EMT/TS 混合仿真 | 作为 EMT 子系统与机电暂态工具交换边界变量 | 接口量、同步方式和延迟补偿是否清楚 |
| 保护与行波暂态 | 产生高频故障波形和测量信号 | 线路模型、采样率和故障位置决定结论可信度 |

## 代表性页面

- [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map]]：使用 PSCAD/EMTDC 对比详细模型、状态空间模型和等效模型，适合检查“波形精度+计算效率”的证据链。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：把 PSCAD/EMTDC 用作并联 VSC-ESS 频率控制策略的 EMT 验证环境。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：体现 PSCAD/EMTDC 与实时或混合仿真基准之间的关系。

## 证据使用规则

- “PSCAD 仿真验证”只能说明在给定模型和工况下通过了数值实验；若没有基准、参数表或误差指标，不应扩写为工程已验证。
- 对电力电子模型，必须看是否包含死区、采样、PWM、限幅和保护逻辑；缺少这些细节时，PSCAD 波形仍可能过于理想化。
- 对混合仿真论文，PSCAD 侧的 EMT 精度不是唯一问题，边界等值、通信步长和插值策略同样会决定稳定性。

## 适用边界与注意事项

- PSCAD/EMTDC 适合高保真离线 EMT 和工程模型验证，但详细开关模型在大规模系统中计算成本高；这也是 [[average-value-model|平均值模型]]、[[state-space-method|状态空间等效]]、[[co-simulation|混合仿真]] 持续发展的原因。
- 论文中“与 PSCAD 一致”通常只能说明相同工况下波形接近；还需要关注时间步长、控制采样、开关插值、初值和故障位置是否一致。
- 当模型用于 HIL 或实时验证时，PSCAD 离线模型常需要转换到 [[rtds|RTDS]]、OPAL-RT 或 FPGA/GPU 平台，转换过程可能引入模型简化和接口延迟。

## 开放问题

- 大规模新能源场站和多端 HVDC 系统如何在 PSCAD 详细模型、实时模型和机电暂态模型之间保持一致性。
- 自定义组件如何形成可复用、可审计的模型库，而不是停留在单个工程项目脚本中。

## 相关方法
- [[nodal-analysis|节点分析法]] - PSCAD/EMTDC核心求解方法，形成节点导纳矩阵求解瞬时电压电流
- [[numerical-integration|数值积分法]] - 梯形积分和后退欧拉法处理开关时刻数值振荡
- [[vector-fitting|矢量拟合]] - 用于线路、电缆、变压器的宽频端口特性建模
- [[state-space-method|状态空间法]] - 用于电力电子设备等效模型和控制系统建模

## 相关模型
- [[mmc-model|MMC模型]] - 模块化多电平换流器详细开关模型和平均值模型
- [[transmission-line-model|输电线路模型]] - 行波模型、频率相关参数线路模型
- [[transformer-model|变压器模型]] - 宽频变压器模型和饱和模型
- [[fdne-model|FDNE模型]] - 频率相关网络等值用于外部系统降阶

## 相关主题
- [[real-time-simulation|实时仿真]] - PSCAD模型向RTDS等实时平台转换
- [[co-simulation|混合仿真]] - 与机电暂态软件(PSS/E)的联合仿真接口
- [[vsc-hvdc|VSC-HVDC]] - 柔性直流输电系统详细建模与验证
- [[cable-modeling|电缆建模]] - 海底电缆和地下电缆的宽频暂态分析

## 相关实体
- [[university-manitoba]]
- [[manitoba-hydro]]
- [[emtp]]
- [[rtds]]
- [[atp-emtp]]
- [[mmc-model]]

## 技术演进脉络

### 1980年代 (起源与早期发展)
- **EMTDC 诞生 (1980s)**
  - 💡 加拿大曼尼托巴大学开发 EMTDC 作为电磁暂态仿真引擎
  - 基于 Dommel 算法，采用梯形积分和节点分析法
  - 最初的命令行界面，主要用于研究目的

### 1990年代 (商业化与 PSCAD 诞生)
- **PSCAD 图形化界面 (1990s)**
  - 💡 引入 PSCAD (Power Systems Computer Aided Design) 图形化建模环境
  - 实现拖拽式建模，大幅降低 EMT 仿真使用门槛
  - 开始应用于工业界，特别是在高压直流输电研究中
- **自定义组件功能**
  - 💡 支持用户自定义模型和 Fortran/C 代码集成
  - 使研究人员能够实现新型控制器和保护逻辑

### 2000年代 (功能扩展与工业应用)
- **电力电子详细建模强化 (2000-2010)**
  - 💡 增强开关器件建模，支持 IGBT、GTO、晶闸管等多种器件
  - 改进电缆和线路模型，支持频变参数和行波分析
  - 广泛用于 HVDC、FACTS 和风力发电系统仿真
- **并行计算引入**
  - 💡 开始支持多核并行计算，提升大规模系统仿真能力

### 2010年代 (多物理场与混合仿真)
- **新能源与电力电子化 (2010-2018)**
  - 💡 针对大规模风电场、光伏电站和柔直电网优化建模
  - 成为新型电力系统暂态研究的主流基准工具
  - 与 MATLAB/Simulink、SimPowerSystems 等工具建立接口
- **混合仿真接口标准化**
  - 💡 支持与机电暂态软件 (PSS/E、PSASP) 的联合仿真
  - 支持 RTDS 实时仿真平台的数据交换

### 2020年代 (高精度与大规模仿真)
- **PSCAD v5 与性能优化 (2020-2025)**
  - 💡 全新64位架构，支持更大规模系统仿真
  - 改进数值稳定性和求解器效率
  - 增强与 Python 等现代编程语言的集成
- **新型电力系统应用深化**
  - 💡 广泛应用于 MMC-HVDC、构网型变换器、直流电网研究
  - 作为新方法验证的"黄参考标准"，大量论文以 PSCAD 结果为基准

## 关键发现汇总

### 验证基准地位
- **[2010-2025]** PSCAD/EMTDC 已成为电力电子和 EMT 仿真的行业基准工具，新方法验证普遍采用 PSCAD 对比
- **[2015+]** 华北电网等实际工程系统仿真中，PSCAD 被用作数模混合仿真的校核基准，误差要求 <2%
- **[2020+]** 在新能源场站建模研究中，PSCAD 详细模型常被用于验证平均值模型和降阶模型的精度

### 计算效率与精度权衡
- **[2017]** 电磁暂态仿真计算量约为机电暂态的数百倍（≥100倍），单个故障扫描耗时从机电暂态的20秒增至360秒（混合仿真）
- **[2020]** PSCAD 详细开关模型在大规模系统中计算成本高，推动平均值模型、状态空间等效和混合仿真技术发展
- **[2022]** 基于 FPGA/GPU 的并行加速可将 PSCAD 级详细模型实时化，但算法框架仍需优化以充分发挥硬件优势

### 模型精度要求
- **[2019+]** PSCAD 仿真验证需关注死区时间、采样控制、PWM 调制、限幅和保护逻辑等细节
- **[2020+]** 与 PSCAD "一致"的声明需配合时间步长、控制采样、开关插值、初值和故障位置一致性分析
- **[2023]** 电磁暂态模型对感应电动机、直流控制保护模型的封装参数存在约5-10%仿真偏差，需通过实测录波校正

## 深度增强内容

### 1. PSCAD/EMTDC 数学基础

#### 1.1 伴随电路模型

EMTDC 采用梯形积分法将动态元件离散化为伴随电路：

**电感伴随导纳：**
$$
G_{eq,L} = \frac{\Delta t}{2L}, \quad I_{hist,L}(t) = i_L(t-\Delta t) + \frac{\Delta t}{2L}v_L(t-\Delta t)
$$

**电容伴随导纳：**
$$
G_{eq,C} = \frac{2C}{\Delta t}, \quad I_{hist,C}(t) = -\frac{2C}{\Delta t}v_C(t-\Delta t) - i_C(t-\Delta t)
$$

**节点导纳方程：**
$$
G_{bus} \cdot V_{node} = I_{inj} + I_{hist}
$$

#### 1.2 开关模型

PSCAD 采用 Ron/Roff 模型处理开关器件：

$$
R_{switch} = \begin{cases}
R_{on} \approx 0.001-0.01\,\Omega & \text{导通} \\
R_{off} \approx 10^6\,\Omega & \text{关断}
\end{cases}
$$

开关动作触发导纳矩阵重构，计算复杂度 $O(N^\alpha)$，其中 $\alpha \approx 1.2-1.4$（利用稀疏矩阵技术）。

#### 1.3 数值积分稳定性

梯形积分法（TR）具有 A-稳定性：
$$
x(t) = x(t-\Delta t) + \frac{\Delta t}{2}[\dot{x}(t) + \dot{x}(t-\Delta t)]
$$

在开关时刻切换至后退欧拉法（BE）以抑制数值振荡：
$$
x(t) = x(t-\Delta t) + \Delta t \cdot \dot{x}(t)
$$

### 2. 仿真参数参考表

| 参数类别 | 参数名称 | 典型值/范围 | 单位 | 备注 |
|---------|---------|------------|------|------|
| **时间设置** | 仿真步长 | 1-50 | μs | 电力电子通常1-10μs |
| | 总仿真时长 | 0.1-10 | s | 视暂态过程而定 |
| | 输出步长 | 10-1000 | μs | 可大于计算步长 |
| **开关器件** | 导通电阻 $R_{on}$ | 0.001-0.01 | Ω | IGBT典型值 |
| | 关断电阻 $R_{off}$ | $10^6$ | Ω | 理想开关近似 |
| | 死区时间 | 2-10 | μs | 防止桥臂直通 |
| **收敛控制** | 最大迭代次数 | 5-20 | 次 | 非线性元件 |
| | 收敛容差 | $10^{-6}$-$10^{-4}$ | - | 相对误差 |
| **求解器选项** | 插值算法 | 线性/二次 | - | 开关时刻精度 |
| | 矩阵重构策略 | 全重构/部分重构 | - | 影响计算速度 |

### 3. 工具选择与应用指南

| 应用场景 | PSCAD/EMTDC 适用性 | 替代/补充工具 | 关键考量 |
|---------|-------------------|---------------|---------|
| **HVDC/MMC 详细建模** | 非常适合 | RTDS (实时)、PSMODEL | PSCAD 适合离线验证，RTDS 适合 HIL 测试 |
| **新能源场站仿真** | 非常适合 | DIgSILENT PowerFactory | PSCAD 精度高，PowerFactory 适合机电暂态 |
| **保护与控制策略开发** | 适合 | MATLAB/Simulink | Simulink 控制建模灵活，PSCAD 电气细节丰富 |
| **机电-电磁混合仿真** | 部分支持 | ADPSS、PSMODEL | ADPSS 更适合大规模系统混合仿真 |
| **实时 HIL 测试** | 不适合 (离线工具) | RTDS、Typhoon HIL | PSCAD 模型需转换至实时平台 |
| **大规模系统扫描** | 计算成本高 | 机电暂态软件 | 1000故障扫描：机电暂态0.5h vs 电磁暂态5-6h |
| **器件级损耗分析** | 支持 (有限) | PLECS、SPICE | PSCAD 可估算，PLECS 热模型更完善 |

### 4. 前沿发展方向

#### 4.1 高性能计算集成
- **GPU 加速求解器**：利用 CUDA 加速大规模节点方程求解
- **云端仿真服务**：基于 CloudPSS 等平台的 PSCAD 级仿真云化
- **分布式并行**：多机集群支持超大规模电网 EMT 仿真

#### 4.2 模型精度提升
- **多物理场耦合**：电热联合仿真，结温计算误差<2°C
- **宽频带建模**：支持 kHz-MHz 级高频振荡分析
- **数据驱动模型**：基于实测数据的 AI 辅助模型校正

#### 4.3 混合仿真深化
- **机电-电磁接口优化**：自动等值电路生成，误差<2%
- **多速率仿真**：支持机电侧 10ms 与电磁侧 10μs 步长无缝接口
- **与实时平台协同**：PSCAD 模型自动生成 RTDS/FPGA 可执行代码

#### 4.4 新型电力系统适配
- **构网型变换器建模**：支持虚拟同步机 (VSG) 控制详细建模
- **直流电网保护**：多端柔直故障分析与保护协调
- **电力电子化负荷**：电动汽车、储能系统大规模接入仿真

## 来源论文

| 论文 | 年份 |
|------|------|
| [[application-of-wavelet-singular-entropy-theory-in-transient-protection-and-accel|Application of wavelet singular entropy theory in transient ]] | 2009 |
| [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati|Photovoltaic generator modelling to improve numerical robust]] | 2012 |
| [[a-novel-substation-back-up-protection-based-on-communication-channel-of-pilot-pr|A Novel Substation Back-up Protection Based on Communication]] | 2013 |
| [[neutral-conductor-current-in-three-phase-networks-with-compact-fluorescent-lamps|Neutral conductor current in three-phase networks with compa]] | 2013 |
| [[a-multi-functional-series-compensator-to-squirrel-cage-induction-generator|A multi-functional series compensator to squirrel cage induc]] | 2015 |
| [[a-new-topology-for-current-limiting-hvdc-circuit-breaker|A new topology for current limiting HVDC circuit breaker]] | 2018 |
| [[characteristics-and-optimal-configuration-of-capacitive-current-limiter-consider|Characteristics and Optimal Configuration of Capacitive Curr]] | 2020 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[dynamic-synchrophasor-estimator-based-on-multi-frequency-phasor-model|Dynamic Synchrophasor Estimator Based on Multi-frequency Pha]] | 2023 |