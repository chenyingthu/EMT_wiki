---
title: "平均值模型"
type: method
tags: [average-value-model, avm, converter, emt]
created: "2026-04-13"
---

# 平均值模型

## 定义与概述

平均值模型（Average-Value Model, AVM）是一类用周期平均、开关函数平均或状态空间平均替代详细开关动作的 EMT 建模方法。它把变流器在一个开关周期内的高频通断细节压缩为连续控制量、受控源或等效电路，从而保留功率交换、控制响应和低频暂态，同时降低详细开关模型带来的计算负担。

AVM 常用于 [[models/vsc-model|VSC]]、[[models/mmc-model|MMC]]、LCC 换流器、风电变流器和系统级 HVDC 研究。它与详细 EMT 模型互补：详细模型用于开关应力、保护动作和高频谐波验证，平均值模型用于控制设计、系统级暂态、混合仿真和大规模参数扫描。

## 作用机制

平均值模型的核心是把离散开关变量替换为连续调制量或平均开关函数。例如换流器桥臂电压可由子模块开关状态求和得到，AVM 则用占空比、插入指数或调制函数近似桥臂平均电压。随后模型可表示为：

$$
\bar{v}_{\mathrm{arm}}(t)=m(t)V_{\mathrm{dc}},\qquad
\dot{x}=f(x,\bar{v}_{\mathrm{arm}},u)
$$

其中 $m(t)$ 是调制函数或插入指数，$\bar{v}_{\mathrm{arm}}$ 是开关周期平均桥臂电压，$x$ 可表示电容电压、环流、滤波器状态或控制状态。

- **受控源接口**：用受控电压源或电流源连接外部网络，计算简单，但可能引入接口延迟。
- **直接接口 AVM**：把平均模型方程嵌入节点导纳矩阵，与外部网络联立求解，减少间接接口延迟。
- **参数化 AVM（PAVM）**：用预先提取的参数或解析函数重构换流器在不平衡、换相失败或故障下的平均行为。
- **增强型 MMC AVM**：额外描述桥臂能量、环流、子模块电容电压纹波、闭锁/解锁状态或损耗。
- **混合模型切换**：在需要局部高保真时切换到详细等效模型，在系统级区段使用 AVM 提升效率。

## 适用边界

- 适合系统级暂态、控制器设计、机电-电磁混合仿真、VSC-HVDC 或 MMC-HVDC 大范围工况分析。
- 适合关注基波、低频控制动态、功率流和主要故障暂态，而不是逐个器件开关瞬态的任务。
- 对谐波、开关纹波、器件损耗、保护误动作和子模块电容局部不均衡敏感的研究，应使用增强 AVM、谐波保留 AVM 或详细模型复核。
- 传统受控源 AVM 在大步长或强耦合网络中可能出现接口延迟；直接接口模型更适合对数值稳定性要求高的节点法 EMT 求解器。
- 对直流故障、闭锁、换相失败和不平衡交流系统，必须确认模型是否显式覆盖相应运行模式，不能默认所有平均值模型都适用。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid]] | 2014 | 讨论 MMC 平均值模型在 VSC-HVDC 网格中的适用性和故障边界。 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 | 用动态平均值方法描述 AC-DC 换流器。 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation]] | 2018 | 增强 MMC AVM，关注闭锁和暂态初始条件。 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Converters]] | 2019 | 用阻塞模块统一处理多子模块拓扑和闭锁/解锁模式。 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model]] | 2020 | 讨论详细等效模型与开关函数 AVM 的动态切换。 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With Embedded Storage]] | 2021 | 面向带嵌入式储能 MMC 的平均值建模。 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Networks]] | 2021 | 将参数化 AVM 扩展到交流不平衡工况。 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC-DC Converters]] | 2022 | 讨论 PAVM 与节点方程的直接接口。 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMT]] | 2023 | 面向 VSC 的直接接口 AVM。 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal Analysis]] | 2024 | 将 VSC AVM 写成适合节点求解的扩展等效导纳形式。 |

## 相关页面

- [[models/vsc-model|VSC 模型]]
- [[models/mmc-model|MMC 模型]]
- [[topics/vsc-hvdc|VSC-HVDC]]
- [[state-space-method|状态空间法]]
- [[fixed-admittance|恒导纳模型]]
- [[topics/dynamic-phasor|动态相量]]

## 技术演进脉络

### 2014年 (AVM基础理论与MMC应用)
- **Average-Value Models for MMC Operating in a VSC-HVDC Grid (2014)**
  - 💡 系统评估MMC平均值模型在VSC-HVDC电网中的适用性边界
  - 揭示了传统AVM在直流故障工况下无法准确模拟暂态过程的局限性
  - 提出拓扑改进方案，显著提升直流故障工况下的仿真精度
- **Dynamic Average-Value Modeling of AC-DC Converters (2014)**
  - 💡 建立动态平均值建模理论框架，用开关函数平均化描述AC-DC换流器
  - 实现换流器高频开关细节的连续化表示

### 2018-2019年 (增强型AVM与闭锁工况)
- **An Enhanced Average Value Model of MMC for Accurate Representation (2018)**
  - 💡 针对MMC提出增强型平均值模型，精确表征闭锁和暂态初始条件
  - 解决传统AVM在故障工况下精度不足的瓶颈
- **A Universal Blocking-Module-Based Average Value Model of MMC (2019)**
  - 💡 提出通用阻塞模块统一处理多种子模块拓扑和闭锁/解锁模式
  - 实现AVM在双模式（解锁/闭锁）下的高精度动态仿真
- **Spurious Power Losses in MMC Arm Equivalent Model (2019)**
  - 💡 首次系统揭示EMT控制模块实现方式导致MMC桥臂等效模型产生虚假功率损耗的机理
  - 给出兼顾精度与效率的替代建模方案

### 2020-2021年 (模型切换与参数化AVM)
- **Combining Detailed Equivalent Model With Switching-Function-Based AVM (2020)**
  - 💡 提出DEM与开关函数AVM的动态切换框架，兼顾仿真精度与计算效率
  - 支持仿真过程中根据精度与计算时间约束平滑切换
- **Average-Value Modeling of Line-Commutated Converters With Unbalanced AC Networks (2021)**
  - 💡 将参数化AVM扩展到交流不平衡工况，拓宽了AVM应用范围
- **Average-Value Model for MMC With Embedded Storage (2021)**
  - 💡 针对带嵌入式储能MMC开发平均值模型，支持系统级分析与元件设计

### 2022-2024年 (直接接口与数值效率)
- **Direct Interfacing of Parametric AVM of AC-DC Converters (2022)**
  - 💡 提出PAVM与节点方程的直接接口方法，消除传统受控源接口的一步延迟
  - 允许仿真步长从数十微秒提升至毫秒级
- **Average-Value Model for VSC With Direct Interfacing in EMT (2023)**
  - 💡 面向VSC的直接接口AVM，将AVM重构为节点导纳形式与外部网络联立求解
- **Numerically Efficient Average-Value Model for VSC in Nodal Analysis (2024)**
  - 💡 将VSC AVM写成适合节点求解的扩展等效导纳形式
  - 实现VSC平均值模型在EMT仿真中的数值高效求解

### 2024-2025年 (前沿发展)
- **Fast Loss Evaluation Method Based on MMC Average Simulation Model (2024)**
  - 💡 将开关频率曲面、衰减函数损耗注入与AVM相结合
  - 实现MMC损耗兼顾高精度与快速计算的在线评估
- **Simplified EMT Model of MAB-Based Power Electronic Transformer (2025)**
  - 💡 针对多 active bridge PET提出简化EMT模型，在保持精度同时显著降低计算负担

## 关键发现汇总

### 建模精度与适用边界
- **[2014]** MMC平均值模型仅在子模块电容足够大以维持电压近似恒定时才有效；传统AVM在直流故障暂态下精度严重不足
- **[2014]** 改进拓扑后的AVM在直流故障工况下暂态仿真精度显著提升，计算效率大幅提高
- **[2018]** 增强型AVM通过引入臂电流初始化机制与闭锁工况等效表征，解决了传统控制信号型AVM初始条件不准及无法模拟闭锁运行的问题
- **[2019]** 通用闭锁模块平均值模型统一支持多种子模块类型及闭锁/解锁工况的高效仿真与损耗计算

### 计算效率提升
- **[2014]** 改进AVM在保持动态精度的同时显著提升了计算速度，允许采用更大的积分步长进行仿真
- **[2022]** 直接接口AVM(DI-AVM)消除传统间接接口的一步延迟，允许仿真步长放宽至1000μs（传统方法极限约100μs）
- **[2024]** 基于MMC平均值仿真模型的损耗快速评估方法，在保持高精度的同时大幅降低了EMT仿真的计算负担

### 接口与数值稳定性
- **[2019]** 揭示了AEM和AVM模型中因控制框图实现导致的一步延迟会产生非物理的虚假功率，证明了虚假功率在特定工况下可占换流站总损耗的显著比例
- **[2023]** DI-AVM通过节点导纳形式实现与外部网络同步求解，消除了传统受控源接口的数值稳定性问题

## 深度增强内容

### 1. 平均值模型数学描述

#### 1.1 基本AVM框架

平均值模型的核心是将离散开关变量替换为连续调制量。对于两电平VSC：

**交流侧受控电压源：**
$$
\mathbf{v}_{abc}(t) = \frac{1}{2} m_{abc}(t) \cdot v_{dc}(t)
$$

**直流侧受控电流源：**
$$
i_{dc}(t) = \frac{3}{4} \sum_{k=a,b,c} m_k(t) \cdot i_k(t)
$$

其中 $m_{abc} \in [-1, 1]$ 为调制比，由PWM策略决定。

**交直流功率平衡：**
$$
P_{ac} = \frac{3}{2}(v_d i_d + v_q i_q) = V_{dc} I_{dc} = P_{dc}
$$

#### 1.2 MMC增强型AVM

针对模块化多电平换流器，桥臂平均电压为：

$$
\bar{v}_{arm} = n_{on} \cdot \bar{v}_{C}^{arm}
$$

其中 $n_{on} \in [0,N]$ 为投入子模块数，$\bar{v}_{C}^{arm}$ 为桥臂平均电容电压。

**环流动力学**（考虑二倍频分量）：
$$
L_{arm} \frac{di_{circ}}{dt} + R_{arm}i_{circ} = \frac{V_{dc}}{2} - \frac{\bar{v}_{u} + \bar{v}_{l}}{2}
$$

**增强型AVM (EAVM)** 引入桥臂电流初始化补偿，闭锁工况下：
$$
i_{arm}(t^+) = i_{arm}(t^-) \cdot \frac{L_{arm}}{L_{arm} + L_{eq}}
$$

#### 1.3 直接接口AVM (DI-AVM)

传统AVM采用受控源间接接口引入一个步长延迟，DI-AVM通过节点导纳形式实现同步求解：

**节点导纳方程重构：**
$$
\begin{bmatrix} \mathbf{Y}_{net} & \mathbf{Y}_{interface} \\ \mathbf{Y}_{conv} & \mathbf{Y}_{internal} \end{bmatrix} \begin{bmatrix} \mathbf{V}_{net} \\ \mathbf{V}_{conv} \end{bmatrix} = \begin{bmatrix} \mathbf{I}_{inj} \\ \mathbf{I}_{eq} \end{bmatrix}
$$

**关键优势：**
- 消除传统间接接口（IDI-AVM）的 $\Delta t$ 延迟
- 允许仿真步长放宽至 $\Delta t \leq 1000\,\mu\text{s}$

**数值稳定性判据：**
$$
Y_{eq} \geq \frac{C_{eq}}{\Delta t}
$$

#### 1.4 参数化AVM (PAVM)

PAVM用预先提取的参数或解析函数重构换流器行为：

$$
\bar{v}_{conv} = f(m, V_{dc}, I_{ac}, \phi, \text{fault\_state})
$$

适用于不平衡、换相失败或故障工况。

### 2. 仿真参数参考表

| 参数类别 | 参数名称 | 典型值/范围 | 单位 | 备注 |
|---------|---------|------------|------|------|
| **开关参数** | 开关频率 | 1980 - 2000 | Hz | 两电平VSC典型值 |
| | 等效调制比 | -1 ~ 1 | - | 取决于控制策略 |
| **MMC特定** | 子模块数量 | 200 - 400 | 个/桥臂 | 鲁西工程400+ |
| | 子模块电容 | 4 - 10 | mF | 电压波动±10% |
| | 桥臂电感 | 50 - 200 | mH | 等效为相电感 |
| **仿真设置** | 传统AVM步长 | 40 - 100 | μs | 基频模型 |
| | DI-AVM最大步长 | 1000 | μs | 直接接口方法 |
| | 机电暂态步长 | 1 - 10 | ms | 简化模型 |
| **模型精度** | 稳态偏差 | < 2 | % | 相比详细模型 |
| | 暂态误差 | < 1.5 | % | 故障工况 |
| | 计算加速比 | 20 - 100 | 倍 | 相比详细开关模型 |

### 3. 模型选择指南

| 应用场景 | 推荐模型 | 步长建议 | 关键考量 |
|---------|---------|---------|---------|
| **系统级暂态分析** | 标准AVM | 50-100 μs | 关注功率流、基频动态 |
| **直流故障穿越** | EAVM / UBM-AVM | 20-50 μs | 必须准确模拟闭锁瞬间电流连续性 |
| **控制策略验证** | DI-AVM | 50-1000 μs | 消除接口延迟，支持大步长 |
| **机电暂态仿真** | 简化AVM | 1-10 ms | 功角稳定、频率控制策略验证 |
| **损耗评估** | AVM + 损耗计算 | 10 μs | 基于桥臂电流解析计算器件损耗 |
| **大规模新能源场站** | 解耦AVM | 50-200 μs | 恒定导纳矩阵，支持并行计算 |

### 4. 前沿研究方向

#### 4.1 多尺度混合建模
- **EMT-HPD协同仿真**：电磁暂态与谐波相量域混合方法，支持宽频振荡分析
- **多速率接口技术**：基于延迟插入法的细粒度并行，支持纳秒级电力电子与毫秒级电网动态交互

#### 4.2 智能自适应建模
- **模型自动切换**：基于暂态严重程度自动在详细模型/AVM/机电模型间切换
- **AI辅助降阶**：利用神经网络逼近开关函数非线性，构建数据驱动的黑箱降阶模型

#### 4.3 虚假损耗消除
- **即时联立求解**：消除AVM中的单步延迟，实现与详细模型一致的功率守恒
- **虚拟二极管方法**：针对闭锁工况精确模拟二极管续流

#### 4.4 新型拓扑专用模型
- **混合MMC (CH-MMC)**：半桥与全桥子模块混合的AVM，支持直流故障自清除能力量化
- **储能型MMC**：含嵌入式DC-DC变换器的平均值模型

## 来源论文

| 论文 | 年份 |
|------|------|
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[the-use-of-averaged-value-model-of-modular-37|The Use of Averaged-Value Model of Modular]] | 2014 |
| [[the-use-of-averaged-value-model-of-modular-37|The Use of Averaged-Value Model of Modular]] | 2014 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Spurious Power Losses in Modular Multilevel Converter Arm Eq]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters W]] | 2021 |
| [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb|The Averaged-value Model of a Flexible Power Electronics Bas]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[协调分布式潮流控制器串并联变流器能量交换的等效模型|协调分布式潮流控制器串并联变流器能量交换的等效模型]] | 2022 |
| [[协调分布式潮流控制器串并联变流器能量交换的等效模型|协调分布式潮流控制器串并联变流器能量交换的等效模型]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[模块化多电平换流器的高效电磁暂态仿真方法研究|模块化多电平换流器的高效电磁暂态仿真方法研究]] | 2022 |
| [[直驱式风电机组机电暂态建模及仿真|直驱式风电机组机电暂态建模及仿真]] | 2022 |
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|Modeling of MMC-based STATCOM with embedded energy storage f]] | 2023 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[多样性子模块混合型mmc统一外特性高效电磁暂态模型|多样性子模块混合型MMC统一外特性高效电磁暂态模型]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[基于mmc平均值仿真模型的损耗快速评估方法|Fast Loss Evaluation Method Based on MMC Average Simulation ]] | 2024 |
| [[基于mmc平均值仿真模型的损耗快速评估方法|Fast Loss Evaluation Method Based on MMC Average Simulation ]] | 2024 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|An Electromagnetic Transient Simulation Model of MMC-BESS fo]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
