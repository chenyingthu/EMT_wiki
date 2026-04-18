---
title: "平均值模型"
type: method
tags: []
created: "2026-04-13"
---

# 平均值模型

## 论文方法分析
> 基于 13 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 平均值建模(AVM) | 3 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| 参数化平均值建模(PAVM) | 3 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 节点分析法 | 2 | Dynamic Average-Value Modeling of |
| 平均值建模 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 阻塞模块等效法 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 解析损耗计算 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 增强型平均值模型（Enhanced AVM） | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 桥臂电流初始化方法 | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 控制信号驱动建模 | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 平均值建模 (Average-Value Modeling) | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 解析表征法 | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 等效电路简化 | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 直接接口技术(Direct Interfacing) | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| 节点导纳矩阵联立求解 | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| EMTP型离散化方法 | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 平均值模型(AVM) | 3 |
| MMC-HVDC系统 | 2 |
| 模块化多电平换流器（MMC） | 2 |
| 电压源换流器(VSC) | 2 |
| 详细开关模型 | 2 |
| 参数化平均值模型(PAVM) | 2 |
| 模块化多电平换流器(MMC) | 2 |
| MMC | 1 |
| 多类型子模块 | 1 |
| 闭锁模块（Blocking Module） | 1 |
| 带嵌入式储能的模块化多电平换流器 (MMC-ES) | 1 |
| 子模块级电池储能系统 | 1 |
| 详细电磁暂态(DEM)模型 | 1 |
| 交直流电力系统 | 1 |
| 电网换相AC-DC换流器(LCC/LCR) | 1 |
### 验证方式分布
- **仿真/对比**: 4 篇
- **仿真**: 3 篇
- **仿真与实验对比验证**: 1 篇
- **实验与仿真对比验证**: 1 篇
- **仿真对比验证**: 1 篇
- **仿真与对比**: 1 篇
- **仿真对比**: 1 篇
- **仿真与实验**: 1 篇
## 技术演进脉络
### 2014年 (2篇)
- **Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC G**
  - 💡 通过改进传统平均值模型的拓扑结构，解决了其在直流故障暂态下仿真精度不足的问题，兼顾了计算效率与准确性。
  - 评估了平均值模型在VSC-HVDC电网中MMC应用的适用性与局限性。
  - 指出传统平均值模型无法准确模拟直流故障下的暂态过程。
- **Dynamic Average-Value Modeling of**
  - 💡 将数值提取的非线性代数函数方法应用于12脉冲换流器的动态平均值建模，实现了跨仿真平台的高效精确等效。
  - 开发了适用于状态变量和节点分析两类仿真平台的CIGRE HVDC基准系统动态平均值模型。
  - 通过数值提取技术构建了12脉冲换流器的非线性代数函数，有效规避了详细开关级建模的复杂性。
### 2016年 (1篇)
- **Improved Accuracy Average Value Models of Modular Multilevel Converters**
  - 💡 通过多项改进策略优化传统MMC平均值模型，在保持高计算效率的同时显著提升仿真精度并支持直流故障等复杂工况分析。
  - 针对现有MMC平均值模型的局限性提出了多项改进策略。
  - 开发了一种精度显著提升的增强型MMC平均值模型。
### 2018年 (1篇)
- **An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Rep**
  - 💡 提出带桥臂电流初始化机制的增强型平均值模型，在免除调制控制器依赖的同时，实现了对MMC闭锁工况及暂态初始条件的精确高效表征。
  - 提出一种增强型平均值模型，能够精确表征MMC的闭锁运行工况。
  - 引入桥臂电流初始化方法，有效补偿了传统控制信号型AVM的初始条件误差。
### 2019年 (1篇)
- **A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Conv**
  - 💡 通过通用阻塞模块架构首次在同一平均值模型中统一处理多子模块拓扑及闭锁/解锁工况，并集成解析损耗计算功能。
  - 提出了一种通用的基于阻塞模块的平均值模型，可兼容多种子模块拓扑结构。
  - 实现了换流器在闭锁与解锁两种运行模式下的高精度动态仿真。
### 2020年 (1篇)
- **Combining Detailed Equivalent Model With Switching-Function-Based Average Value **
  - 💡 提出了一种将详细等效模型与开关函数平均值模型相结合的通用框架，实现了仿真过程中高精度与高速度模型的平滑动态切换。
  - 提出了一种融合DEM与SFB-AVM的通用桥臂等效电路建模框架。
  - 实现了动态仿真过程中两种模型之间的平滑无缝切换。
### 2021年 (2篇)
- **Average-Value Model for a Modular Multilevel Converter With Embedded Storage**
  - 💡 提出了一种兼顾计算效率与解析能力的MMC-ES平均值模型，突破了传统数值模型难以直接用于控制器调参、小信号分析及元件参数设计的局限。
  - 提出了一种计算高效的MMC-ES平均值模型，显著降低了系统级仿真的计算负担。
  - 实现了对环流和子模块电容电压波动的解析表征，支持含或不含环流抑制控制的分析。
- **Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne**
  - 💡 首次将参数化平均值建模扩展至交流不平衡工况，通过显式建立正负序谐波与直流纹波对电网不平衡度的依赖关系，实现了LCC的高效高精度仿真。
  - 将参数化平均值建模(PAVM)方法扩展至交流电网不平衡工况下的电网换相换流器仿真。
  - 建立了交流侧正负序谐波与直流侧纹波相对于电网不平衡度的解析数学关系。
### 2022年 (2篇)
- **Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail**
  - 💡 首次将考虑内部故障的PAVM方法应用于电网换相逆变器，结合自动故障检测技术，实现了换相失败工况下仿真精度与计算效率的有效平衡。
  - 将参数化平均值建模(PAVM)方法从交流-直流整流器成功扩展至直流-交流逆变器系统。
  - 在平均值模型框架内准确表征了开关器件的换相失败故障动态。
- **Direct Interfacing of Parametric Average-Value Models of AC&#x2013;DC Converters**
  - 💡 通过将PAVM接口方程线性化并直接嵌入节点导纳矩阵，彻底消除了传统EMTP仿真中因间接接口引入的一步时间延迟，实现了大时间步长下的高精度稳定仿真。
  - 提出了一种针对电网换相整流器(LCR)参数化平均值模型(PAVM)的直接接口方法。
  - 通过线性化PAVM接口方程并将其子矩阵和历史项直接嵌入网络节点方程，消除了传统间接接口所需的一步时间延迟。
### 2023年 (1篇)
- **Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMT**
  - 💡 通过将VSC平均值模型转化为节点导纳形式并与系统网络方程联立求解，实现了无延迟的直接接口，突破了传统AVM在大步长仿真中的数值稳定性瓶颈。
  - 提出了一种适用于VSC的直接接口平均值模型，彻底消除了传统间接接口的一步时间延迟。
  - 将AVM方程重构为节点形式，使其能够与外部网络节点方程同步联立求解，从而支持大仿真步长。
### 2024年 (1篇)
- **Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal**
  - 💡 提出基于扩展等效导纳矩阵的直接接口平均值模型，彻底消除传统受控源接口在节点法EMT仿真中的计算延迟，实现大时间步长下的高精度稳定仿真。
  - 将直接接口平均值模型（DI-AVM）的数学公式推广至任意接口节点配置。
  - 构建了假设所有节点浮空的VSC扩展等效导纳矩阵。
### 2026年 (1篇)
- **Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transie**
  - 💡 在时间域内将平均价值模型作为主干并融合谐波分量计算，实现了兼顾高计算效率与精确谐波表征的系统级变流器建模。
  - 提出了一种谐波保留平均价值模型(HP-AVM)，将AVM计算与谐波分量计算集成于统一仿真框架中。
  - 在保持系统级仿真高计算效率的同时，实现了与开关函数模型(SFM)相当的精度。
## 关键发现汇总
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 仅当子模块电容足够大以维持电压近似恒定时，平均值模型才有效。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 改进拓扑后的平均值模型能准确捕捉直流故障暂态，克服了传统模型的缺陷。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 相比详细电磁暂态模型，改进模型在保证关键暂态精度的同时实现了显著的计算加速。
- [2014] **Dynamic Average-Value Modeling of**: 动态平均值模型的大信号时域暂态响应与详细开关级仿真结果高度一致。
- [2014] **Dynamic Average-Value Modeling of**: 相比详细模型，该平均值模型大幅减少了计算时间，具备显著的系统级仿真计算优势。
- [2016] **Improved Accuracy Average Value Models of Modular Multilevel**: 改进后的AVM在仿真精度上显著优于传统平均值模型。
- [2016] **Improved Accuracy Average Value Models of Modular Multilevel**: 新模型能够准确模拟直流故障等暂态过程，验证了其更广泛的适用性。
- [2016] **Improved Accuracy Average Value Models of Modular Multilevel**: 模型在提升精度的同时保持了较高的计算效率，适用于大规模系统仿真。
- [2018] **An Enhanced Average Value Model of Modular Multilevel Conver**: 增强型AVM在显著提升仿真效率的同时，能精确复现桥臂电压纹波和环流动态。
- [2018] **An Enhanced Average Value Model of Modular Multilevel Conver**: 所提初始化方法有效消除了传统AVM在暂态和闭锁过程中的初始条件不匹配问题。
- [2018] **An Enhanced Average Value Model of Modular Multilevel Conver**: 模型无需子模块开关函数即可准确模拟换流器闭锁期间的交直流侧电气行为。
- [2019] **A Universal Blocking-Module-Based Average Value Model of Mod**: 所提模型在41电平MMC-HVDC系统中的仿真精度与详细开关模型及现有先进AVM高度一致。
- [2019] **A Universal Blocking-Module-Based Average Value Model of Mod**: 模型在保持高精度的同时显著提升了电磁暂态仿真效率，适用于大规模系统分析。
- [2019] **A Universal Blocking-Module-Based Average Value Model of Mod**: 解析损耗计算方法能够准确反映不同子模块拓扑下的半导体损耗特性。
- [2020] **Combining Detailed Equivalent Model With Switching-Function-**: SFB-AVM的仿真速度显著优于DEM，且子模块数量越多加速效果越显著。
- [2020] **Combining Detailed Equivalent Model With Switching-Function-**: 所提框架支持在仿真运行中按需切换模型，且切换过程平滑无暂态扰动。
- [2020] **Combining Detailed Equivalent Model With Switching-Function-**: SFB-AVM能够准确反映不同子模块类型MMC的动态电气特性。
- [2021] **Average-Value Model for a Modular Multilevel Converter With **: 所提平均值模型在大幅降低计算复杂度的同时，保持了与详细EMT模型高度一致的动态响应精度。
- [2021] **Average-Value Model for a Modular Multilevel Converter With **: 模型能够准确解析计算环流分量与子模块电容电压纹波，为控制器调参和小信号分析提供理论支撑。
- [2021] **Average-Value Model for a Modular Multilevel Converter With **: 基于该模型的元件 sizing 分析结果与实验数据吻合，验证了其在不同运行工况下的设计指导价值。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 新PAVM能够高精度重构交流电网不平衡工况下的交直流侧电压与电流波形。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 所提模型的计算效率显著高于传统详细开关模型，有效缓解了系统级EMT仿真的计算瓶颈。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 所提PAVM能够准确预测换相失败事件并重构出与详细开关模型高度一致的电气波形。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 该模型通过忽略高频开关事件显著降低了计算负担，大幅提升了系统级仿真的运行速度。
- [2022] **Direct Interfacing of Parametric Average-Value Models of AC&**: 仿真结果表明该方法在较大时间步长下仍能保持极高的仿真精度。
- [2022] **Direct Interfacing of Parametric Average-Value Models of AC&**: 有效消除了传统间接接口导致的数值不稳定问题，显著提升了EMTP类求解器的计算效率与稳定性。
- [2023] **Average-Value Model for Voltage-Source Converters With Direc**: 新模型成功消除了传统接口的一步延迟，允许在EMTP类程序中使用较大的仿真时间步长。
- [2023] **Average-Value Model for Voltage-Source Converters With Direc**: 在较大时间步长条件下，该模型的仿真精度和数值稳定性显著优于现有的VSC平均值模型。
- [2023] **Average-Value Model for Voltage-Source Converters With Direc**: 所提模型在VSC的整流和逆变两种运行模式下均保持有效。
- [2024] **Numerically Efficient Average-Value Model for Voltage-Source**: 在大仿真时间步长下，该模型的数值精度显著优于传统受控源AVM。

## 深度增强内容

 ---
title: "平均值模型"
type: method
tags: []
created: "2026-04-13"
---

# 平均值模型（Average-Value Model, AVM）

## 1. 核心原理详解

平均值模型（AVM）是一种基于**开关函数平均**与**状态空间平均**的降阶建模方法，通过忽略电力电子器件的高频开关细节，将换流器及其控制系统等效为受控源网络或低阶等效电路，从而在保持关键电磁暂态特性的同时显著提升仿真效率。

### 1.1 数学基础

**开关周期平均算子**定义如下：
$$\bar{x}(t) = \frac{1}{T_s}\int_{t-T_s}^{t} x(\tau)d\tau$$

其中$T_s$为开关周期。对于MMC等复杂拓扑，采用**广义状态空间平均法（GSSA）**扩展至谐波域：
$$\langle x \rangle_k(t) = \frac{1}{T}\int_{t-T}^{t} x(\tau)e^{-jk\omega_s\tau}d\tau$$

当仅保留直流分量（$k=0$）时，GSSA退化为传统状态空间平均法（SSA）。

### 1.2 MMC桥臂等效原理

对于模块化多电平换流器（MMC），第$j$相上桥臂的瞬时电压可表示为：
$$v_{arm,j}(t) = \sum_{i=1}^{N} S_{j,i}(t) \cdot v_{c,j,i}(t)$$

其中$S_{j,i} \in \{0,1\}$为子模块开关函数。AVM通过引入**开关占空比**$d_j(t) \in [0,1]$进行平均化：
$$\bar{v}_{arm,j}(t) = d_j(t) \cdot \bar{v}_{c,j}^{eq}(t)$$

等效电容电压$\bar{v}_{c}^{eq}$基于**能量守恒原理**计算。假设所有子模块电容电压平衡，六桥臂总储能等效为：
$$C_{eq} = \frac{6C_{SM}}{N}$$

单桥臂能量等效为：
$$C_{eq}^{arm} = \frac{3C_{SM}}{N}$$

### 1.3 损耗建模

引入等效电阻$R_{eq}$表征半导体通态损耗与开关损耗：
$$R_{eq} = \frac{2nR_{on}}{3}$$

其中$n$为子模块数，$R_{on}$为IGBT导通电阻。改进型AVM（MAVM）通过解析损耗计算将误差控制在**<2%**，显著优于仅考虑$I^2R$损耗的传统模型（误差通常>8%）。

### 1.4 闭锁工况处理

针对直流故障等需模拟换流器闭锁的场景，引入**阻塞模块（Blocking Module, BM）**：
$$v_{arm}^{block} = \begin{cases} 
R_{on} \cdot i_{arm}, & i_{arm} > 0 \ (\text{二极管导通}) \\
R_{off} \cdot i_{arm}, & i_{arm} \leq 0 \ (\text{二极管截止})
\end{cases}$$

增强型AVM（EAVM）通过**桥臂电流初始化**补偿闭锁瞬间初始条件：
$$i_L(0^+) = i_{arm}(t_{block})$$

消除传统模型交直流侧电流不连续现象。

## 2. 算法流程

### 2.1 标准AVM构建流程

```markdown
步骤1: 拓扑分析与开关函数提取
  └─ 识别换流器拓扑（VSC/MMC/LCC等）
  └─ 定义开关函数 S(t) ∈ {0,1} 或连续占空比 d(t) ∈ [0,1]

步骤2: 状态变量平均化
  └─ 对电容电压、电感电流进行周期平均
  └─ 傅里叶分解（可选）：保留直流 + 基频分量（k=0,±1），忽略k≥2高次谐波
  └─ 数学形式：⟨x⟩(t) = [⟨x⟩₀, ⟨x⟩₁, ⟨x⟩₋₁]ᵀ

步骤3: 等效电路构建
  └─ 戴维南等效：电压源 + 串联电阻
  └─ 诺顿等效：电流源 + 并联电导
  └─ 对于MMC：桥臂等效为受控电压源 v_arm = f(v_dc, m, θ)

步骤4: 离散化与导纳矩阵构建
  └─ 采用梯形法（Trapezoidal）或后退欧拉法离散化
  └─ 构建恒定导纳矩阵 G（AVM特性：G不随开关状态变化）
  └─ 历史项注入：I_hist(t) = f(v(t-Δt), i(t-Δt))

步骤5: 网络方程联立求解
  └─ 求解线性方程组：G·V = I_inj + I_hist
  └─ 计算节点电压 V 与支路电流 I

步骤6: 状态更新与反算
  └─ 更新等效电容电压：v_c(t) = v_c(t-Δt) + (i_c·Δt)/C_eq
  └─ 子模块电容电压映射（如需细节）：v_sm = v_c^eq · N
```

### 2.2 分段广义状态空间平均（P-GSSA）流程

针对变流器多时间尺度特性：

```markdown
步骤1: 分段判定
  └─ 监测占空比变化率：|d(t) - d(t-T_s)| < ε₁
  └─ 若连续r个周期满足条件，合并为一段（通常1-3个载波周期）

步骤2: 分段平均方程建立
  └─ 对每段[t_k, t_{k+1}]建立平均状态方程：ẋ = A_k·x + B_k·u

步骤3: 变步长求解
  └─ 段内采用大步长（10-100μs）
  └─ 段间边界处采用插值或减小步长保证精度

步骤4: 状态变量重构（后处理）
  └─ 基于保留的傅里叶系数重构时域波形
  └─ x(t) ≈ ⟨x⟩₀ + 2Re{⟨x⟩₁·e^{jωt}}
```

## 3. 参数选取指南

### 3.1 等效电容取值策略

| 应用场景 | 推荐公式 | 数值示例 | 精度特点 |
|---------|---------|---------|---------|
| **稳态运行** | $C_{eq} = \frac{6C_{SM}}{N}$ | 若$C_{SM}=20\text{mF}, N=100$，则$C_{eq}=1.2\text{mF}$ | 稳态阶段精度最优，长期能量追踪误差<3% |
| **暂态初期**（0-5ms） | $C_{eq} = \frac{3C_{SM}}{N}$ | 同上，$C_{eq}=0.6\text{mF}$ | 阶跃响应初期精度最优，避免过冲 |
| **闭锁工况** | 采用受控电流源初始化 | $i_L(0^+) = i_{arm}(t_{block})$ | 消除电流不连续，故障峰值误差<1.5% |

### 3.2 仿真步长配置

| 模型类型 | 推荐步长 | 适用条件 | 注意事项 |
|---------|---------|---------|---------|
| **详细开关模型** | 1-5 μs | 需捕捉IGBT开关细节、子模块均压 | 计算密集型，仅用于小系统验证 |
| **桥臂等效模型(AEM)** | 20-50 μs | 保留电容电压波动，研究环流 | 需处理虚假功率损耗问题 |
| **平均值模型(AVM)** | 50-100 μs | 系统级研究、直流电网暂态 | 要求$C_{SM}$足够大（纹波<5%） |
| **分段GSSA** | 变步长（0.1-1ms） | 长时间尺度机电暂态 | 段间需平滑处理避免数值振荡 |

### 3.3 损耗参数整定

- **等效电阻法**：$R_{loss} = P_{rated} \times 1\% / I_{rated}^2$，适用于稳态潮流计算
- **解析损耗模型**：分别计算通态损耗$P_{cond} = V_{ce} \cdot I_{avg} + R_{ce} \cdot I_{rms}^2$与开关损耗$P_{sw} = E_{on/off} \cdot f_{sw}$，适用于效率评估
- **注入法**：通过衰减函数将损耗等效为电流/电压源注入，避免阻抗修改导致的数值稳定性问题

## 4. 性能分析

### 4.1 计算效率对比

| 论文来源 | 模型对比 | 加速比 | 仿真步长 | 系统规模 |
|---------|---------|-------|---------|---------|
| *Average-Value Modeling of Line-Commutated AC-DC Converters* (2021) | PAVM vs DSM | **>100倍** | 50μs vs <1μs | 12脉冲换流器 |
| *A Universal Blocking-Module-Based AVM* (2019) | AVM vs DEM | **15-20倍** | 50μs vs 1-5μs | 混合子模块MMC |
| *Full-state Arm AVM* (2022) | AVM vs DEM | **O(1)复杂度**（与子模块数N无关） | 50μs | 有源型MMC |
| *Simplified EMT Model of MAB-PET* (2025) | SEM vs DM | **100-1000倍** | - | 多主动桥PET |
| *CH-MMC电磁暂态快速仿真* (2024) | 高效模型 vs DSM | **518倍** | - | 21电平MMC-SCES |
| *The Use of AVM* (2014) | AVM vs 详细IGBT | **90-98%时间节省** | - | 4端HVDC电网 |

### 4.2 精度指标汇总

| 评估指标 | 典型误差范围 | 最优实现 | 限制条件 |
|---------|-------------|---------|---------|
| **稳态电压** | <1-2% | <0.5% | 电容足够大（$C_{sm} \geq 20\text{mF}$） |
| **故障电流峰值** | <5% | <1.5% | 需改进AVM或阻塞模块 |
| **功率损耗** | 3-8% | <2% | 需解析损耗模型，非简单$I^2R$ |
| **直流电压纹波** | <3% | <1% | 等效电容取值准确 |
| **交流谐波** | THD偏差<0.8% | <0.3% | GSSA保留适当谐波阶数 |
| **小信号阻抗** | <2%（10Hz-2kHz） | <1% | PAVM谐波项表征准确 |

### 4.3 虚假功率问题

经典AVM/AEM因单步延迟（$\Delta t$）产生的虚假功率：
$$\Delta p_0 = 0.5 \cdot \Delta t \cdot \omega \cdot V_1 \cdot I_1 \cdot \sin(\varphi_v - \varphi_i)$$

典型HVDC工况（$V_1=100\text{kV}, I_1=1\text{kA}, \Delta t=50\mu\text{s}$）下，每臂虚假功率可达**785kW**，六臂总计**4.71MW**（可达实际损耗的30-60%）。**解决方案**：采用联立求解（Simultaneous Solution）而非交替求解，消除控制框与主电路间的时间偏移。

## 5. 最佳实践与注意事项

### 5.1 适用场景判断

✅ **推荐使用AVM**：
- 系统级机电暂态分析（惯性响应、功角稳定）
- 直流电网潮流计算与稳态运行优化
- 长时间尺度（秒级至分钟级）控制策略验证
- 硬件在环（HIL）实时仿真（步长≥50μs）

❌ **避免使用标准AVM**（需采用DEM或改进AVM）：
- 子模块电容电压严重不平衡（纹波>5%）
- 直流故障闭锁暂态（需EAVM+阻塞模块）
- 子模块级故障（旁路开关动作、电容失效）
- 高频谐振分析（>2kHz，AVM无法表征）

### 5.2 模型配置 checklist

1. **电容验证**：确认$C_{sm} \geq 20\text{mF}$或电压纹波<2%，否则AVM在暂态过程中会失效
2. **初始化设置**：利用打靶法（Shooting Method）或稳态求解器确定初始条件，避免启动振荡
   - AVM状态变量数：$O(1)$（与N无关）
   - 打靶法收敛精度：$\|\Delta\mathbf{x}\| < 10^{-6}$
3. **闭锁逻辑**：配置阻塞模块（BM）处理直流故障，确保二极管导通电阻$R_{on}$在mΩ级，截止电阻$R_{off}$在MΩ级
4. **损耗校准**：若关注效率，采用解析损耗计算而非简单等效电阻，特别是在轻载工况（虚假功率可能超过实际损耗）

### 5.3 常见数值问题

- **电流不连续**：闭锁瞬间若未初始化电感电流，会导致交直流侧电流突变。解决方案：采用受控电流源强制连续
- **虚假功率损耗**：控制环节与主电路间一步延迟导致。解决方案：采用EMTP型联立求解（Simultaneous Solution）
- **高频振荡**：步长过大时可能出现数值振荡。解决方案：采用临界阻尼调整（CDA）或减小步长至20μs以下

## 6. 与其他方法的对比

### 6.1 详细开关模型（Detailed Model, DM）

| 维度 | AVM | DM |
|-----|-----|-----|
| **计算复杂度** | $O(1)$，与器件数无关 | $O(N)$，随子模块数线性增长 |
| **仿真步长** | 50-100 μs | 1-5 μs |
| **开关细节** | 完全忽略 | 精确捕捉 |
| **适用场景** | 系统级、长时间尺度 | 阀级保护、均压控制验证 |
| **直流故障** | 需改进模型（EAVM+BM） | 原生支持 |

### 6.2 桥臂等效模型（Arm Equivalent Model, AEM）

| 维度 | AVM | AEM |
|-----|-----|-----|
| **内部动态** | 仅保留总能量/平均电压 | 保留子模块电容电压分布 |
| **计算效率** | 极高（节点数恒定） | 中等（节点数$\propto$桥臂数） |
| **虚假功率** | 较大（六臂总和等效） | 单臂级别，可控 |
| **环流模拟** | 需额外建模 | 自然涌现 |
| **适用场景** | 外部电网交互 | 内部控制（环流抑制、均压） |

### 6.3 戴维南等效模型（Detailed Equivalent Model, DEM）

| 维度 | AVM | DEM |
|-----|-----|-----|
| **开关表征** | 连续受控源 | 二值电阻（$R_{on}/R_{off}$） |
| **导纳矩阵** | 恒定（无需 refactorization） | 变导纳（每步需LU分解） |
| **计算速度** | 快（50-100倍） | 中等（10-20倍于DM） |
| **精度** | 低频准确 | 宽频带准确 |
| **实现复杂度** | 需平均化推导 | 自动离散化（伴随电路） |

### 6.4 分段广义状态空间平均（P-GSSA）

| 维度 | 传统AVM | P-GSSA |
|-----|---------|--------|
| **谐波保留** | 仅直流或基频 | 可配置（通常k=0,±1） |
| **多时间尺度** | 单一时间尺度 | 分段处理，支持变步长 |
| **适用场景** | 恒定开关频率 | 变频控制、间歇性调制 |
| **计算效率** | 高 | 中-高（取决于分段策略） |
| **精度** | 低频稳态优 | 暂态过程精度更高 |

### 6.5 选择决策树

```markdown
是否需要模拟子模块级故障或均压控制？
├─ 是 → 采用 DEM 或 AEM
└─ 否 → 关注时间尺度？
    ├─ 长期动态（>1s）→ AVM（最大效率）
    ├─ 中期暂态（10ms-1s）→ P-GSSA（精度与效率平衡）
    └─ 短期暂态（<10ms）+ 闭锁工况 → EAVM（增强型AVM）或 DEM
```

## 深度增强内容

 ---
title: "平均值模型"
type: method
tags: []
created: "2026-04-13"
---

# 平均值模型

## 论文方法分析
> 基于 13 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 平均值建模(AVM) | 3 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| 参数化平均值建模(PAVM) | 3 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 节点分析法 | 2 | Dynamic Average-Value Modeling of |
| 平均值建模 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 阻塞模块等效法 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 解析损耗计算 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 增强型平均值模型（Enhanced AVM） | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 桥臂电流初始化方法 | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 控制信号驱动建模 | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 平均值建模 (Average-Value Modeling) | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 解析表征法 | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 等效电路简化 | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 直接接口技术(Direct Interfacing) | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| 节点导纳矩阵联立求解 | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| EMTP型离散化方法 | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 平均值模型(AVM) | 3 |
| MMC-HVDC系统 | 2 |
| 模块化多电平换流器（MMC） | 2 |
| 电压源换流器(VSC) | 2 |
| 详细开关模型 | 2 |
| 参数化平均值模型(PAVM) | 2 |
| 模块化多电平换流器(MMC) | 2 |
| MMC | 1 |
| 多类型子模块 | 1 |
| 闭锁模块（Blocking Module） | 1 |
| 带嵌入式储能的模块化多电平换流器 (MMC-ES) | 1 |
| 子模块级电池储能系统 | 1 |
| 详细电磁暂态(DEM)模型 | 1 |
| 交直流电力系统 | 1 |
| 电网换相AC-DC换流器(LCC/LCR) | 1 |
### 验证方式分布
- **仿真/对比**: 4 篇
- **仿真**: 3 篇
- **仿真与实验对比验证**: 1 篇
- **实验与仿真对比验证**: 1 篇
- **仿真对比验证**: 1 篇
- **仿真与对比**: 1 篇
- **仿真对比**: 1 篇
- **仿真与实验**: 1 篇
## 技术演进脉络
### 2014年 (2篇)
- **Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC G**
  - 💡 通过改进传统平均值模型的拓扑结构，解决了其在直流故障暂态下仿真精度不足的问题，兼顾了计算效率与准确性。
  - 评估了平均值模型在VSC-HVDC电网中MMC应用的适用性与局限性。
  - 指出传统平均值模型无法准确模拟直流故障下的暂态过程。
- **Dynamic Average-Value Modeling of**
  - 💡 将数值提取的非线性代数函数方法应用于12脉冲换流器的动态平均值建模，实现了跨仿真平台的高效精确等效。
  - 开发了适用于状态变量和节点分析两类仿真平台的CIGRE HVDC基准系统动态平均值模型。
  - 通过数值提取技术构建了12脉冲换流器的非线性代数函数，有效规避了详细开关级建模的复杂性。
### 2016年 (1篇)
- **Improved Accuracy Average Value Models of Modular Multilevel Converters**
  - 💡 通过多项改进策略优化传统MMC平均值模型，在保持高计算效率的同时显著提升仿真精度并支持直流故障等复杂工况分析。
  - 针对现有MMC平均值模型的局限性提出了多项改进策略。
  - 开发了一种精度显著提升的增强型MMC平均值模型。
### 2018年 (1篇)
- **An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Rep**
  - 💡 提出带桥臂电流初始化机制的增强型平均值模型，在免除调制控制器依赖的同时，实现了对MMC闭锁工况及暂态初始条件的精确高效表征。
  - 提出一种增强型平均值模型，能够精确表征MMC的闭锁运行工况。
  - 引入桥臂电流初始化方法，有效补偿了传统控制信号型AVM的初始条件误差。
### 2019年 (1篇)
- **A Universal Bl

## 1. 核心原理详解

### 1.1 状态空间平均理论基础

平均值模型（Average-Value Model, AVM）的核心在于利用**开关周期平均算子**消除电力电子变换器的高频开关细节，保留低频包络动态。对于周期性开关信号$s(t) \in \{0,1\}$，其平均值为：

$$
\langle s(t) \rangle_{T_s} = \frac{1}{T_s} \int_{t-T_s}^{t} s(\tau) d\tau = d(t)
$$

其中$T_s$为开关周期，$d(t)$为瞬时占空比。基于该定义，时变状态方程可转化为：

$$
\frac{d\langle \mathbf{x} \rangle}{dt} = \mathbf{A}(d)\langle \mathbf{x} \rangle + \mathbf{B}(d)\langle \mathbf{u} \rangle
$$

### 1.2 MMC平均值模型拓扑

对于模块化多电平换流器（MMC），传统详细模型（DM）中第$j$个桥臂电压为：

$$
v_{arm,j} = \sum_{i=1}^{N} s_{j,i} \cdot v_{c,j,i}
$$

平均值模型将其等效为受控电压源。根据能量守恒原理，桥臂等效电容与等效电压满足：

$$
C_{eq} = \frac{C_{SM}}{N}, \quad v_{c}^{eq} = \sum_{i=1}^{N} v_{c,i}
$$

其中$C_{SM}$为子模块电容，$N$为子模块数。改进型AVM采用六倍等效电容以准确表征能量动态：

$$
C_{eq} = \frac{6C_{SM}}{N}
$$

该等效确保了MMC内部总储能$E_{tot} = \frac{1}{2}C_{eq}(v_{c}^{eq})^2$与实际系统一致。

### 1.3 参数化平均值建模（PAVM）

针对电网不平衡工况，PAVM引入**正负序分离**与**谐波项表征**。桥臂电压分解为：

$$
v_{arm} = V_{dc} + \sum_{h=1}^{\infty} \left[ V_h^+ \cos(h\omega t + \phi_h^+) + V_h^- \cos(h\omega t + \phi_h^-) \right]
$$

其动态特性可通过代数相量形式或动态微分形式表征。代数形式计算量较动态形式降低约30%，适用于超大规模系统仿真。

### 1.4 闭锁工况建模

MMC闭锁时，二极管整流桥等效电路需引入**阻塞模块（Blocking Module, BM）**。桥臂电流初始化机制通过受控电流源补偿初始条件：

$$
i_{arm}(t_0^+) = i_{arm}(t_0^-) + \Delta i_{init}
$$

其中初始化电流$\Delta i_{init}$由故障前稳态工作点计算，确保交直流侧电流连续性误差趋于零。

### 1.5 损耗解析计算

传统AVM忽略开关损耗，改进模型引入等效损耗电阻：

$$
R_{loss} = \frac{2nR_{on}}{3}
$$

开关损耗通过开关频率曲面法近似：

$$
P_{sw} = P_{sw_{max}} \cdot \frac{f_{real}}{f_{max}}
$$

其中$f_{real}$为实时开关频率，通过二维插值查表获得，通态与开关损耗综合计算误差可控制在<2%。

## 2. 算法流程

### 2.1 经典AVM实现步骤

**步骤1：占空比计算**
根据调制策略（NLC或PWM）计算各桥臂等效占空比：
$$
n_{on} = \text{round}\left(\frac{v_{ref} + v_{dc}/2}{v_{c}^{avg}}\right)
$$

**步骤2：等效电路参数更新**
更新受控电压源与等效电容：
$$
v_{arm}^{avg} = n_{on} \cdot v_{c}^{eq}, \quad C_{eq} = \frac{6C_{SM}}{N}
$$

**步骤3：网络方程求解**
构建节点导纳矩阵$\mathbf{G}$，求解系统电压电流：
$$
\mathbf{G}\mathbf{V} = \mathbf{I}_{inj}
$$

**步骤4：状态变量更新**
利用梯形法更新等效电容电压：
$$
v_{c}^{eq}(t+\Delta t) = v_{c}^{eq}(t) + \frac{\Delta t}{2C_{eq}}(i_{arm}(t) + i_{arm}(t+\Delta t))
$$

### 2.2 分段广义状态空间平均（P-GSSA）算法

**输入**：开关周期$T_s$，占空比方差阈值$\varepsilon_1$，保留傅里叶阶数$k$

**流程**：
1. **分段检测**：监测占空比$d(t)$的方差，当连续$r$个周期方差小于$\varepsilon_1$时合并为一段
2. **谐波分解**：对每段内状态变量进行傅里叶分解，保留$\pm k$次谐波：
   $$
   x(t) \approx \sum_{n=-k}^{k} \langle x \rangle_n(t) e^{jn\omega_s t}
   $$
3. **状态空间构建**：建立分段平均方程：
   $$
   \frac{d\langle \mathbf{x} \rangle_n}{dt} = \mathbf{A}_n \langle \mathbf{x} \rangle_n + \mathbf{B}_n \langle \mathbf{u} \rangle_n - jn\omega_s \langle \mathbf{x} \rangle_n
   $$
4. **尺度变换**：根据频段选择仿真步长$\Delta t \in [T_s, 3T_s]$

### 2.3 增强型AVM（EAVM）闭锁处理流程

**预故障阶段**：
- 正常运行AVM，记录桥臂电流$i_{arm}$与电容电压$v_c$

**闭锁触发**：
1. **电流初始化**：计算闭锁瞬间桥臂电感电流：
   $$
   i_{L}(t_{block}) = \frac{2}{3}i_{dc} - \frac{1}{3}i_{ac}
   $$
2. **拓扑切换**：将受控电压源切换为二极管整流等效电路，投入阻塞模块
3. **受控源注入**：通过受控电流源注入初始电流，消除数值不连续

## 3. 参数选取指南

### 3.1 等效电容配置策略

| 应用场景 | 推荐等效电容 | 数学表达 | 精度特点 |
|---------|-------------|---------|---------|
| 稳态工况分析 | 六倍等效 | $C_{eq} = \frac{6C_{SM}}{N}$ | 稳态电压平衡精度高，误差<1% |
| 暂态初始阶段（<5ms） | 三倍等效 | $C_{eq} = \frac{3C_{SM}}{n}$ | 阶跃响应初始精度最优 |
| 闭锁故障仿真 | 可变等效 | $C_{eq} = f(v_{c}, i_{arm})$ | 考虑电容电压重新分布 |

### 3.2 等效电阻设置

- **通态损耗等效**：$R_{on}^{eq} = \frac{R_{on}}{N}$，其中$R_{on}$为IGBT导通电阻（典型值0.01Ω）
- **总损耗等效**：按换流器额定功率的1%选取，$R_{loss} = \frac{P_{rated} \cdot 0.01}{3I_{arm,rms}^2}$

### 3.3 仿真步长选择

| 模型类型 | 推荐步长 | 适用条件 |
|---------|---------|---------|
| 详细开关模型（DSM） | 1-5 μs | 需捕捉开关瞬间细节，子模块数<50 |
| 戴维南等效模型（DEM） | 10-20 μs | 保留子模块动态，中等规模系统 |
| 平均值模型（AVM） | 20-100 μs | 系统级分析，关注机电暂态 |
| 分段GSSA | 100 μs-1 ms | 稳态或慢变工况，大规模新能源并网 |

### 3.4 P-GSSA控制参数

- **占空比方差阈值**：$\varepsilon_1 \in [0.01, 0.05]$，越小分段越细，精度越高
- **傅里叶截断阶数**：$k=0$（仅直流）适用于极慢动态；$k=1$（基频）适用于稳态；$k\geq2$适用于谐波分析

## 4. 性能分析

| 性能指标 | 详细模型(DSM) | 戴维南等效(DEM) | 平均值模型(AVM) | 改进型AVM | 数据来源 |
|---------|--------------|----------------|----------------|----------|---------|
| **计算加速比** | 1× (基准) | 10-20× | 50-100× | 15-20× (含闭锁逻辑) | 2014, 2019, 2022 |
| **仿真步长** | 1-5 μs | 10-20 μs | 50-100 μs | 20-50 μs | 多篇论文 |
| **电压误差** | <0.1% | <0.5% | 1-2.5% | <1% | 2014, 2016 |
| **电流误差** | <0.1% | <0.5% | 2-5% | <1.5% | 2018, 2019 |
| **适用电平数** | 任意 | 401级验证 | 11-401级 | 21-401级 | 2014, 2022 |
| **直流故障精度** | 基准 | 较高 | 失效/误差>30% | 误差<5% | 2014, 2016 |
| **闭锁工况支持** | 支持 | 支持 | 不支持 | 支持 | 2018, 2019 |
| **虚假功率** | 无 | 低 | 显著 (4.71MW/站) | 可消除 | 2020 |

**关键发现**：
- 当子模块电容$C_{SM} \geq 20$ mF（电压纹波<2%）时，AVM精度与详细模型相当；当$C_{SM} = 10$ mF（纹波>5%）时，传统AVM失效
- 经典AVM因控制框单步延迟产生的虚假功率可达实际半导体损耗的30-60%，极端工况下可能超过实际损耗

## 5. 最佳实践与注意事项

### 5.1 适用边界条件

**必须使用AVM的场景**：
- 多端HVDC电网系统级分析（节点数>100）
- 长时间暂态仿真（>10s）或机电暂态分析
- 控制器参数优化与硬件在环测试（需实时性）

**避免使用AVM的场景**：
- 子模块级故障分析（如电容短路、IGBT击穿）
- 高频谐波 resonant 分析（>2kHz）
- 直流故障初始瞬间精确电流峰值计算（除非使用改进型AVM）

### 5.2 虚假功率消除

单步延迟导致的虚假功率计算公式：

$$
\Delta p_0 = 0.5 \cdot \Delta t \cdot \omega \cdot V_1 \cdot I_1 \cdot \sin(\varphi_v - \varphi_i)
$$

**消除措施**：
1. 采用**代数环消除技术**，将控制延迟补偿纳入受控源计算
2. 使用**可变电阻模型**替代受控电压源模型，实现与主网络方程联立求解
3. 在闭锁工况下采用**桥臂电流初始化**，避免电流不连续

### 5.3 初始化策略

基于打靶法的AVM初始化可显著减少启动暂态：

1. 利用AVM降阶特性（状态变量从$O(N)$降至$O(1)$），降低雅可比矩阵维度
2. 通过牛顿迭代求解周期性稳态条件：$\|\Delta\mathbf{x}\| < 10^{-6}$
3. 将收敛后的状态变量映射至详细模型（如需混合仿真）

### 5.4 数值稳定性建议

- **电容电压平衡**：AVM假设所有子模块电压均衡，实际应用中需确保$C_{SM}$足够大（纹波<5%）
- **步长耦合**：当AVM与外部网络接口时，建议采用**直接接口技术**（Direct Interfacing），通过节点导纳矩阵联立求解避免插值误差
- **插值修正**：在大步长（>20μs）下捕捉开关事件时，采用**线性插值**修正开关时刻，可将THD误差控制在0.3%以内

## 6. 与其他方法的对比

### 6.1 AVM vs 详细开关模型（DSM）

| 维度 | 详细开关模型 | 平均值模型 |
|-----|-------------|-----------|
| **建模粒度** | 单个IGBT/二极管开关瞬态 | 桥臂级平均行为 |
| **计算复杂度** | $O(N^3)$（每步长需重新LU分解） | $O(1)$（与子模块数无关） |
| **精度** | 最高（开关瞬间μs级） | 低频动态准确（<500Hz） |
| **适用规模** | 单换流器（<100子模块） | 多端电网（>1000子模块） |
| **直流故障** | 精确 | 传统失效/改进型近似 |

### 6.2 AVM vs 桥臂等效模型（AEM）

- **AEM特点**：保留子模块电容电压个体动态，通过戴维南等效将桥臂简化为$N:1$节点网络
- **对比**：AVM计算速度比AEM快5-10倍，但AEM能捕捉子模块间电压不平衡（误差<0.3%）
- **选择建议**：需分析电容电压均衡控制时选AEM，仅需外特性时选AVM

### 6.3 AVM vs 分段广义状态空间平均（P-GSSA）

- **P-GSSA优势**：通过多时间尺度建模，可在同一仿真中自动切换详细与平均模型
- **AVM优势**：实现简单，无需傅里叶系数计算，实时性更好
- **融合趋势**：现代高效仿真方法常将AVM作为P-GSSA在$k=0$（直流分量）时的特例，或作为DEM的降阶切换模型

### 6.4 混合仿真接口

在机电-电磁混合仿真中，AVM可作为**电磁侧简化模型**与机电暂态接口：
- **数据交互**：通过多端口戴维南/诺顿等值电路接口
- **时序协调**：AVM大步长（50μs）与机电暂态步长（10ms）通过插值或预测校正算法同步
- **精度控制**：接口功率偏差通过3-5次迭代收敛至<0.1%

---

**总结**：平均值模型通过牺牲高频开关细节换取计算效率的数量级提升，是现代大规模电力电子电力系统电磁暂态仿真的核心方法。随着改进型AVM（支持闭锁与故障）和参数化AVM（支持不平衡工况）的发展，其适用范围已从稳态分析扩展至全工况暂态仿真，成为连接详细电磁暂态与机电暂态分析的重要桥梁。