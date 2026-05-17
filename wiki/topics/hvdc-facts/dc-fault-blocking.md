---
title: "直流故障闭锁 (DC Fault Blocking)"
type: topic
tags: [dc-fault, blocking, mmc, hvdc, protection, fault-current, full-bridge, hybrid-mmc]
created: "2026-05-04"
updated: "2026-05-13"
---

# 直流故障闭锁 (DC Fault Blocking)

## 定义

直流故障闭锁是模块化多电平换流器（MMC）高压直流输电系统在检测到直流侧故障时采取的快速保护策略。当直流线路发生 pole-to-pole 短路或接地故障时，换流器需在 **1~5 ms** 内将 IGBT 全部闭锁（block），使子模块进入自由续流状态或主动输出负电压，从而阻断故障电流的持续上升。

直流故障电流的物理本质是 **MMC 子模块电容的 RLC 放电过程**与 **交流侧通过二极管整流向故障点馈入电流** 的叠加。由于直流电流无自然过零点，传统交流断路器无法直接开断，因此闭锁策略是后续故障清除和系统恢复的前提。

**边界限定**：本页面聚焦于基于电力电子的直流故障处理策略（闭锁、降额、负电压阻断），不包括机械式直流断路器（DCCB）的分断机制。直流断路器本身属于 [[dc-protection]] 范畴。

## EMT 中的角色

直流故障闭锁是 MMC-MTDC 系统保护的核心环节，在 EMT 仿真中扮演三重角色：

1. **故障电流抑制**：闭锁前，子模块电容通过二极管向故障点放电，电流上升率可达 **10~50 kA/ms**（Wang et al. 2023）。闭锁后，半桥 MMC 无法阻断二极管续流，故障电流持续上升；全桥 MMC 则可通过插入负电压主动抑制电流。
2. **系统稳定性评估**：直流故障导致换流器有功功率骤降，交流侧经历功率不平衡暂态。Xiao et al. (2019) 指出，直流故障对大规模交直流系统暂态稳定性的影响需要在 **机电暂态模型** 中精确模拟 MMC 的二阶直流侧等效电路。
3. **仿真模型验证**：闭锁过程的准确性直接检验 EMT 模型的可靠性，包括子模块电容放电动态、二极管续流特性、控制系统的故障检测与响应延迟等。

## MMC 子模块拓扑与故障特性

直流故障闭锁行为从根本上取决于 MMC 子模块（SM）的拓扑结构。三种主流拓扑在故障中的表现截然不同：

### 1. 半桥子模块（HBSM）

半桥 MMC 是最广泛部署的拓扑（如上海南汇舟山五端、厦门真双极工程）。其子模块结构如图 1 所示：每个 HBSM 包含电容 $C_0$、两个 IGBT（T1, T2）和反并联二极管（D1, D2）。

**正常工作模式**：通过近邻电平调制（NLM），子模块可在三种状态间切换：
- **投入态**（T1 导通，T2 关断）：输出电压 $U_{sm}$
- **闭锁态**（T1, T2 均关断）：电容通过二极管续流，输出电压为 0（二极管压降忽略）
- **旁路态**（T1 关断，T2 导通）：输出 0

**直流故障时的行为**（Wang et al. 2023）：

当直流侧发生 pole-to-pole 短路时，交流侧电压通过整流桥（二极管）向故障点馈入电流，同时子模块电容储存的能量通过桥臂电感和等效电阻向故障点放电。等效放电回路如图 2 所示。

将 $N$ 个子模块串联的桥臂等效为集中参数：

$$C_{eq} = \frac{2C_0}{3N}, \quad L_{eq} = \frac{2L_0}{3}, \quad R_{eq} = \frac{2R_0}{3}$$

其中 $L_0$ 为桥臂电感，$R_0$ 为桥臂等效电阻，$C_0$ 为子模块电容。

故障电流的解析表达式为（Wang et al. 2023, 式 2.1~2.4）：

$$i(t) = \frac{V_0}{\omega_d L_{eq}} e^{-\alpha t} \sin(\omega_d t) + i_{ac}(t)$$

其中：

$$\alpha = \frac{R_{eq} + R_{dc}}{2L_{eq}}, \quad \omega_d = \sqrt{\frac{1}{L_{eq}C_{eq}} - \alpha^2}$$

$V_0$ 为故障前直流母线电压，$R_{dc}$ 和 $L_{dc}$ 为直流侧等效电阻和电感，$i_{ac}(t)$ 为交流侧通过二极管整流馈入的电流分量。

**关键结论**：半桥 MMC **无法阻断故障电流**。即使 IGBT 全部闭锁，二极管续流路径仍然存在，故障电流将持续上升直至交流断路器动作。这是半桥 MMC 的根本局限。

### 2. 全桥子模块（FBSM）

全桥 MMC 的每个子模块包含四个 IGBT 和反并联二极管，如图 3 所示。与 HBSM 的关键区别在于：**FB SM 在闭锁态下可以通过 IGBT 控制输出正电压、零电压或负电压**。

**直流故障阻断机制**（Marquardt 2011; Meng et al. 2019）：

当检测到直流故障时，全桥 MMC 执行以下操作：
1. **快速闭锁**（~1 ms）：所有 IGBT 关断
2. **负电压插入**（~1~3 ms）：逐步将子模块电容以反向串联方式插入，使桥臂输出电压从 $+U_{dc}/2$ 变为 $-U_{dc}/2$
3. **电流抑制**：负电压抵消线路电压，故障电流在 **3~5 ms** 内降至零

全桥 MMC 的故障电流抑制过程可表述为：

$$L_{line} \frac{di_{fault}}{dt} = \frac{U_{dc}}{2} - U_{arm}^{neg} - i_{fault} R_{line}$$

其中 $U_{arm}^{neg}$ 为全桥臂插入的负电压，其最大值为 $-N \cdot U_{sm}^{rated}$。当 $|U_{arm}^{neg}| > U_{dc}/2$ 时，故障电流开始下降。

**代价**：全桥 MMC 的导通损耗是半桥的约两倍（因为电流通路上有两个 IGBT 串联），且子模块数量翻倍，成本显著增加。

### 3. 混合子模块（MBSM：半桥 + 全桥）

混合 MMC 采用大部分半桥子模块（约 1/3 ~ 1/2）加少量全桥子模块的组合，兼顾成本与故障阻断能力。

**工作原理**（Meng et al. 2019）：
- 正常运行时，半桥子模块承担主要功率传输，全桥子模块处于投入态
- 故障检测后，全桥子模块快速插入负电压，半桥子模块闭锁
- 全桥子模块提供的负电压足以抵消直流线路电压，阻断故障电流

**设计折中**：全桥子模块占比越低，成本越低，但需要的负电压插入时间越长。工程实践中，全桥占比通常不低于 **25%**。

## 闭锁过程的时间序列

直流故障闭锁是一个多阶段过程，各阶段的时间尺度差异显著：

| 阶段 | 时间尺度 | 物理过程 | 电流特征 |
|------|----------|----------|----------|
| 故障检测 | 0.2~0.5 ms | 电压跌落 / 电流突增检测 | 故障电流开始上升 |
| 通信延迟 | 0.5~2.0 ms | 故障信息跨站通信 | 非故障站仍在馈入电流 |
| IGBT 闭锁 | 0.1~0.3 ms | 所有 IGBT 关断 | 二极管续流路径建立 |
| 负电压建立（FB/MB） | 1.0~3.0 ms | 子模块逐步反向插入 | 故障电流达到峰值后下降 |
| 电流过零 | 3.0~8.0 ms | 负电压完全抑制电流 | 故障电流降至零 |
| 交流断路器动作 | 50~150 ms | 交流侧断路器分断 | 故障电流彻底清除 |

**总故障清除时间**（从故障发生到电流完全清除）：
- 全桥 MMC：约 **50~100 ms**（含交流断路器动作时间）
- 混合 MMC：约 **50~150 ms**（取决于全桥占比）
- 半桥 MMC：约 **100~200 ms**（依赖交流断路器，无法主动阻断）

## EMT 建模方法

在 EMT 仿真中，直流故障闭锁过程的建模精度直接影响保护策略验证的可靠性。根据 Meng et al. (2019) 的分类，主要有以下建模层次：

### 1. 详细开关模型（Detailed Switch Model）

每个 IGBT 和二极管都显式建模，子模块电容电压动态精确追踪。这是最精确的方法，但计算量巨大——一个 80 电平 MMC 包含 **960 个 IGBT 开关事件**，时间步长需 ≤ 1 μs。

**适用场景**：子模块电容电压均衡算法验证、故障瞬态的精确波形分析。

### 2. 详细等效模型（DECM, Type 4）

将每个桥臂等效为离散时间的 Thevenin 等效电路（Meng et al. 2019; CIGRE B4.57 2014）。在故障闭锁过程中，DECM 需要通过额外的开关和二极管来模拟故障电流路径。

**改进 DECM**（Meng et al. 2019）：在桥臂等效电路中增加反并联二极管和受控电压源，以准确模拟闭锁瞬间的故障电流。CPU 仿真加速比约 **50~100x**，FPGA 实时仿真加速比约 **200~500x**。

### 3. 平均值模型（AVM, Type 5）

平均值模型将 MMC 桥臂等效为受控电压源和等效电容，忽略开关细节。Meng et al. (2019) 提出了一种 **通用闭锁模块（UBM, Universal Blocking Module）** 架构：

**UBM 核心思想**：在 AVM 中引入一个通用的闭锁模块，该模块根据 IGBT 门极信号动态切换等效电路拓扑：
- **去闭锁态**：正常调制，桥臂等效为受控电压源 $v_{bridge} = (2n_u - N) \cdot U_{sm} / N$
- **闭锁态**：桥臂等效为二极管整流电路 + 等效电容，输出由电容电压决定

UBM-AVM 的桥臂电压方程为：

$$v_{uj} = \begin{cases} e_{ref,j} \cdot \frac{U_{dc}}{2}, & \text{de-blocking} \\ \frac{U_{C,eq}^{u}}{2}, & \text{blocking (HB)} \\ -\frac{U_{C,eq}^{u}}{2}, & \text{blocking (FB, negative insertion)} \end{cases}$$

其中 $U_{C,eq}^{u}$ 为上桥臂等效电容电压，在闭锁期间由电容放电动态决定：

$$\frac{dU_{C,eq}^{u}}{dt} = -\frac{i_{uj}}{C_{eq}}$$

**AVM 的局限**：标准 AVM 在直流 pole-to-pole 故障期间精度不足（Meng et al. 2019），必须引入闭锁模块（BM）才能准确模拟故障瞬态。

### 4. 机电暂态模型（Type 6）

Xiao et al. (2019) 指出，传统的机电暂态 MMC 模型在直流侧采用 **一阶等效电路**（仅考虑等效电容 $C_{eq}$），忽略了桥臂电感的动态效应。他们提出将直流侧等效为 **二阶 RLC 电路**：

$$L_{arm} \frac{di_{dc}}{dt} + R_{arm} i_{dc} + \frac{1}{C_{eq}} \int i_{dc} dt = \frac{U_{dc}}{2} - U_{fault}$$

这一改进使得机电暂态模型能够准确模拟直流故障对大规模交直流系统暂态稳定性的影响，而无需重构直流网络拓扑。

## 形式化表达

### 故障电流解析解（Wang et al. 2023）

对于对称双极 MMC-MTDC 系统，子模块电容放电回路的拉普拉斯域表达式为：

$$I(s) = \frac{V_0/s}{sL_{eq} + R_{eq} + \frac{1}{sC_{eq}} + Z_{line}(s)}$$

其中 $Z_{line}(s)$ 为直流线路阻抗。在集总参数假设下：

$$i(t) = \frac{V_0}{\omega_d L_{eq}} e^{-\alpha t} \sin(\omega_d t) \cdot u(t)$$

多端系统中，每个换流器向故障点的放电电流可分为 **顺时针** 和 **逆时针** 两种路径（Wang et al. 2023）。对于多端复杂网络，可简化为双端模型进行计算。

### 全桥负电压阻断方程

全桥 MMC 在闭锁后，桥臂输出电压为：

$$U_{arm}^{FB}(t) = -\frac{N_{FB} \cdot U_{sm}^{cap}(t)}{N_{total}} \cdot U_{dc}^{rated}$$

其中 $N_{FB}$ 为全桥子模块数量，$U_{sm}^{cap}(t)$ 为全桥子模块电容电压（闭锁期间放电下降）。

### 闭锁判据

工程实践中，闭锁判据通常基于以下两个量：

$$\frac{dU_{dc}}{dt} < -\theta_{dv/dt} \quad \text{or} \quad I_{dc} > I_{threshold}$$

其中 $\theta_{dv/dt}$ 为直流电压下降率阈值（典型值 1~5 kV/ms），$I_{threshold}$ 为过流阈值（通常为额定电流的 1.5~2 倍）。

## 关键技术挑战

### 1. 故障检测与通信延迟

多端直流电网中，故障定位和选择性隔离依赖于站间通信。通信延迟（通常 1~5 ms）导致非故障站仍在向故障点馈入电流，加剧故障电流上升。Wang et al. (2023) 指出，六端系统中非故障站的放电电流可占总故障电流的 **40~60%**。

### 2. 子模块电容电压均衡

闭锁期间，子模块电容通过二极管不均匀放电，导致电容电压差异增大。故障清除后重新投入时，电压不均衡可能引发过电压和额外损耗。混合 MMC 中，HB 和 FB 子模块的放电特性不同，均衡问题更为复杂。

### 3. 交流侧馈入电流

即使直流侧闭锁，交流系统通过换流器二极管向故障点馈入电流。这一电流分量取决于交流电压幅值、系统阻抗和闭锁延迟。在弱交流系统中，故障可能导致交流电压跌落，从而限制馈入电流；但在强交流系统中，馈入电流可能非常大。

### 4. 重启动策略

故障清除后，换流器需要重新投入运行。重启动过程包括：
1. 交流断路器重合闸
2. 子模块电容预充电至额定电压
3. 调制信号逐步恢复
4. 功率设定值 ramp-up

预充电时间通常为 **100~500 ms**，取决于线路电容和充电电阻参数。

## 量化性能边界

### 故障电流上升率

| 拓扑类型 | 上升率 (kA/ms) | 峰值电流 (kA) | 数据来源 |
|----------|----------------|---------------|----------|
| 半桥 MMC (±500 kV) | 10~30 | 15~25 | Wang et al. 2023 |
| 全桥 MMC (±500 kV) | 10~30 (上升后下降) | 5~10 (3 ms 后) | Meng et al. 2019 |
| 混合 MMC (25% FB) | 10~25 | 8~15 (5 ms 后) | Meng et al. 2019 |

### 闭锁时间

| 操作 | 时间 (ms) | 说明 |
|------|-----------|------|
| 故障检测 | 0.2~0.5 | 基于电压下降率或过流 |
| 控制处理 | 0.1~0.2 | DSP/FPGA 计算 |
| IGBT 关断延迟 | 0.1~0.3 | 驱动电路延迟 |
| 全桥负电压建立 | 1.0~3.0 | 逐层插入子模块 |
| 总闭锁时间 (HB) | ~1.0 | IGBT 全部闭锁 |
| 总电流抑制时间 (FB) | 3.0~5.0 | 负电压完全阻断 |

### 仿真精度验证

Wang et al. (2023) 在 PSCAD/EMTDC 和数字物理半物理实验平台上验证了故障电流解析计算方法，**理论解与仿真误差 < 5%**，与实验数据误差 < 8%。

Xiao et al. (2019) 在 PSS/E 中对修改后的 IEEE 39 节点系统（含四端 MMC-HVDC）进行仿真，验证了二阶直流等效电路在故障模拟中的准确性，与 EMT 仿真结果误差 < 10%。

## 适用边界与选择指南

### 拓扑选择指南

| 应用场景 | 推荐拓扑 | 理由 |
|----------|----------|------|
| 低端子线 (radial) | HBSM | 成本低，末端故障可由上游断路器清除 |
| 环网/多端主干线 | FBSM 或 MB (≥25% FB) | 需要自限流能力 |
| 海上风电并网 | MB (30~50% FB) | 故障率高（架空线），需快速阻断 |
| 城市电缆网络 | HBSM + DCCB | 电缆故障率低，可用直流断路器 |

### 闭锁策略适用边界

- **半桥 MMC**：仅适用于有直流断路器保护的线路，或故障点位于交流断路器可清除范围内的场景。
- **全桥 MMC**：适用于需要自限流的无断路器多端直流电网，但成本较高。
- **混合 MMC**：适用于成本和性能折中的场景，全桥占比需根据故障电流抑制时间要求优化设计。

### EMT 模型选择指南

| 仿真目标 | 推荐模型 | 计算效率 |
|----------|----------|----------|
| 子模块级故障波形 | Detailed Switch | 基准（最慢） |
| 系统级故障暂态 | DECM with BM | 50~100x |
| 多端 MTDC 故障 | AVM with UBM | 100~500x |
| 大规模交直流稳定 | 机电模型 (二阶) | 1000x+ |

## 相关方法

- [[mmc-model]] - MMC 换流器建模基础
- [[vsc-hvdc]] - VSC-HVDC 系统架构
- [[fault-analysis-methods]] - 故障分析方法论
- [[fault-ride-through]] - 故障穿越策略
- [[dc-protection]] - 直流保护系统
- [[fault-analysis-methods]] - 故障分析方法论（含直流故障电流计算）
- [[electromagnetic-transient]] - 电磁暂态仿真
- [[emt-simulation]] - EMT 仿真基础
- [[real-time-simulation]] - 实时仿真技术
- [[co-simulation]] - 混合仿真方法
- [[control-system]] - 控制系统设计



## 来源论文

1. **Wang et al. 2023** - "Analysis and general calculation of DC fault currents in MMC-MTDC grids", *Electric Power Systems Research*, 224:109709. 提出了 MMC-MTDC 系统直流故障电流的通用解析计算方法，建立了子模块电容 RLC 放电的等效模型，分析了多端网络中各换流器的放电特性，并在 PSCAD/EMTDC 和数字物理半物理平台验证。

2. **Meng et al. 2019** - "A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Converters with Different Types of Submodules", *IEEE Transactions on Energy Conversion*, 35(1):132-143. 提出了通用闭锁模块（UBM）架构的 AVM 模型，可准确模拟 HB、FB 和 MB 子模块 MMC 在闭锁和去闭锁模式下的动态行为，包括半导体损耗建模。

3. **Xiao et al. 2019** - "Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults considered", *Electrical Power and Energy Systems*, 113:1002-1013. 指出传统机电模型直流侧一阶等效的局限性，提出二阶 RLC 直流等效电路，并给出了基于预设故障信息的直流故障处理方法，在 PSS/E 中验证。

4. **Marquardt, R. 2011** - "Modular Multilevel Converter with DC Short Circuit Current Limitation", *EPE Proceedings*. 奠基性工作，首次提出全桥 MMC 通过插入负电压阻断直流 pole-to-pole 故障电流的概念。

5. **Li et al. 2018** - "DC Fault Protection Strategy for MMC-HVDC", *IEEE Transactions on Power Delivery*. 系统研究了 MMC-HVDC 直流故障保护策略，包括故障检测、闭锁时序和交流断路器协调。

6. **CIGRE Working Group B4.57 2014** - "Guide for the development and usage of MMC models". 定义了 MMC 模型的七种类型（Type 1~7），为 EMT 和机电暂态仿真中的 MMC 建模提供了标准化框架。

---

| 论文 | 年份 |
|------|------|
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p]] | 2014 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]] | 2014 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters]] | 2016 |
| [[34tpwrd20172749427]] | 2017 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]] | 2018 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-]] | 2019 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-]] | 2023 |
