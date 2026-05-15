---
title: "Energy Storage System"
type: topic
tags: [energy-storage-system, bess, mmc-bess, statcom, vsc-ess, grid-forming, emt-simulation]
created: "2026-05-04"
updated: "2026-05-15"
---

# Energy Storage System

## 定义

储能系统（Energy Storage System, ESS）是由储能介质（电池、超级电容、飞轮等）、功率变换器（PCS/DC-DC/DC-AC）、控制器、保护电路和并网接口共同构成的电力电子集成系统。在 EMT Wiki 中，本页作为储能系统主题的系统级入口，组织储能介质的物理特性、变流器的建模层级、控制系统架构以及大规模并网场景下的 EMT 仿真方法。

储能系统不是单一 EMT 数值方法或单一元件模型。设备级电池等效电路应进入 [[bess-model]]，并网功率变换器应进入 [[energy-storage-converter-model]]，MMC 子模块级建模应进入 [[dem]] 或 [[half-bridge-submodule]]，具体算例或测试平台应进入 test-system 页面。本页聚焦系统层问题：多尺度建模体系、精度-效率权衡、控制架构对比、并行仿真策略和适用边界。

## EMT 中的角色

储能系统在 EMT 仿真中承担四类核心角色：

1. **端口动态表征**：表示电池等储能介质的端口电压、电流、SOC（荷电状态）和限幅状态，捕捉毫秒至秒级的能量充放电动态。
2. **故障与暂态响应验证**：验证储能变流器在交流故障、电压跌落、功率指令阶跃切换和弱网条件下的动态响应，包括电流限幅、直流电压保护和控制模式切换。
3. **系统级暂态交互研究**：研究 BESS 与 HVDC、MMC、微电网或大规模交直流系统之间的暂态交互，如并联 VSC-ESS 的惯量协调、频率支撑中的功率振荡。
4. **混合仿真与实时仿真对象**：为 EMT-TS 混合仿真、GPU/并行仿真和硬件在环（HIL）测试提供设备集群对象，支撑大规模 BESS 集群的实时验证。

储能系统在 EMT 中的独特挑战在于其多时间尺度特性：开关级瞬变（微秒）、控制回路动态（毫秒）、能量管理（秒至分钟），以及大规模部署时的计算可扩展性（数百至数千台逆变器）。

## 储能介质层：电池、超级电容与飞轮

储能介质决定系统的能量密度、功率密度和时间常数范围，是 EMT 建模的起点。

### 电池储能（Battery Energy Storage）

电池储能是最主流的 ESS 技术，在 EMT 仿真中通常采用等效电路模型（ECM）或电化学-电路耦合模型。二阶 RC 等效电路是最常用的 EMT 级模型：

$$V_{t}(t) = V_{ocv}(SOC) - I_{b}(t)R_{0} - V_{1}(t) - V_{2}(t)$$

其中 $V_{ocv}(SOC)$ 是开路电压与 SOC 的非线性函数，$R_{0}$ 是欧姆内阻，$V_{1}$ 和 $V_{2}$ 是两个 RC 极化支路的电压。极化支路满足：

$$\dot{V}_{k} = -\frac{1}{R_{k}C_{k}}V_{k} + \frac{1}{C_{k}}I_{b}, \quad k=1,2$$

SOC 的动态方程为：

$$\dot{SOC} = -\frac{I_{b}}{C_{nom}}$$

其中 $C_{nom}$ 是电池额定容量。EMT 仿真中，SOC 变化缓慢（秒至分钟级），但电池端电压动态直接影响 PCS 的控制环响应，因此需要在 EMT 时间尺度（微秒至毫秒）内保留电池端口方程。

### 超级电容储能（Supercapacitor Energy Storage）

超级电容（Supercapacitor, SC）具有极高的功率密度和快速充放电能力（毫秒级时间常数），适用于高频功率调节和瞬态支撑。其 EMT 模型通常采用单 RC 支路：

$$V_{sc}(t) = V_{0} + \frac{1}{C_{sc}}\int I_{sc}(t)dt - I_{sc}(t)R_{esr}$$

其中 $C_{sc}$ 是超级电容容量，$R_{esr}$ 是等效串联电阻。与电池相比，超级电容的 SOC 概念被电压直接替代，且其电压-电荷关系近似线性。

朱琼海和肖晃庆（2024）提出了基于模块化多电平换流器的超级电容储能系统高效仿真方法，采用 D-DEM 架构将子模块电容电压用前向欧拉显式离散化，在大步长（50 μs）下保持数值稳定性，同时实现与电池储能相似的建模框架。

### 飞轮储能（Flywheel Energy Storage）

飞轮储能通过旋转动能存储能量，其 EMT 建模需要同时考虑机电动态和电力电子接口。飞轮的机械转子方程为：

$$J_{m}\frac{d\omega_{m}}{dt} = T_{m} - T_{e} - B\omega_{m}$$

其中 $J_{m}$ 是转动惯量，$\omega_{m}$ 是机械角速度，$T_{m}$ 是机械转矩，$T_{e}$ 是电磁转矩，$B$ 是阻尼系数。在 EMT 仿真中，飞轮通常通过双向 DC-DC 变换器并网，其机电时间常数（秒级）远大于 EMT 时间尺度，因此在纯 EMT 仿真中常被简化为恒功率源或等效电压源。

## 变流器层：PCS、MMC 与多端口拓扑

储能系统的功率变换层决定了能量在储能介质与电网之间的转换效率和动态响应。

### 传统 PCS 架构

传统 BESS 采用"电池组 + 单向 DC-DC 升压 + 两电平/三电平 VSC"的集中式架构。电池组通过 DC-DC 变换器升压至直流母线电压，再由 VSC 转换为交流并网。该架构的优点是结构简单、成本低，但缺点是电池组非模块化，无法实现单节电池级的功率均衡和故障隔离。

### MMC-BESS 架构

MMC-BESS 将电池单元嵌入 MMC 子模块中，每个子模块包含一个小容量电池和双向 DC-DC 变换器。Wang（2025）提出的 MMC-BESS EMT 模型覆盖整流、逆变、STATCOM 和闭锁四种工况，其拓扑结构如下：

- 每相臂由多个串联的子模块（SM）组成
- 每个 SM 包含电池、DC-DC 变换器和 SM 电容
- 电池通过 Buck-Boost 变换器连接到 SM 电容，降低直流滤波需求，实现电池电流可控

Wang（2025）的模型改进了传统 DEM，通过引入辅助 PSCAD 开关和内置插值算法模拟换流器闭锁状态，同时通过补充判定公式模拟电池断开。该模型在 PSCAD/EMTDC 中验证了子模块电容电压平衡和功率阶跃响应。

### MMC-STATCOM 与嵌入式储能

Stepanov 等（2026）研究了 Delta 连接的 MMC-BASED STATCOM 与嵌入式储能，比较了四种 MMC 建模方法（详细模型 DM、详细等效模型 DEM、臂等效模型 AEM、平均值模型 AVM）在 STATCOM 应用中的动态性能。该论文提出的泛化建模方法允许任意两端口储能设备模型与任意转换器模型互连，支持超级电容和电池两种储能类型。

Herath 和 Filizadeh（2021）提出了 MMC-ES 的平均值模型（AVM），将多阀级表示为显式的多端口等效电路，保留了子模块级信息的同时支持分析性研究（环流特性、电容电压纹波分析和元件尺寸设计）。该模型在 EMT 仿真中验证了对比详细开关模型的计算加速效果。

### 多端口转换器拓扑

MMC-ES 可视为三端口转换器（交流端口、直流端口、储能端口），这一特性使其在 shipboard 系统（同时存在交流和直流系统）和光伏-储能混合系统中具有独特优势。Nurunnabi 等（2025）研究了混合光伏-电池 Plant 的构网型（Grid-Forming）逆变器控制，展示了储能系统在可再生能源集成中的多端口角色。

## 控制系统架构

储能系统的控制架构决定了其在电网中的动态行为和响应特性。

### 有功-频率控制（虚拟同步机架构）

基于虚拟同步机（VSG）思想的有功-频率控制是储能参与频率支撑的核心方法。Hu 等（2025）建立了并联 VSC-ESS 的小信号模型，其中单台 VSC-ESS 的虚拟转子方程为：

$$J_{i}\frac{d\Delta\omega_{i}}{dt} = \frac{P_{mi}}{\omega_{0}} - \frac{P_{0i}}{\omega_{0}} - D_{i}(\omega_{i} - \omega_{0})$$

其中 $J_{i}$ 是虚拟惯量，$D_{i}$ 是虚拟阻尼，$P_{mi}$ 是等效机械功率，$P_{0i}$ 是输出有功功率。一次调频等效机械功率方程为：

$$P_{mi} = P_{refi} + k_{\omega i}(\omega_{0} - \omega)$$

其中 $k_{\omega i}$ 是频率调制系数（一次调频系数）。有功-功角小信号线性化方程为：

$$P_{0i} \approx K_{i}\delta_{i}, \quad K_{i} = \frac{1.5U_{ci}U_{g}}{X_{i}}$$

其中 $K_{i}$ 是同步功率系数，$U_{ci}$ 是 VSC 端电压幅值，$U_{g}$ 是电网电压幅值，$X_{i}$ 是并网等效电抗。

单台 VSC-ESS 相对于公共母线频率扰动的二阶传递函数为：

$$G_{i}(s) = \frac{K_{i}}{J_{i}\omega_{0}s^{2} + (D_{i}\omega_{0} + k_{\omega i})s + K_{i}}$$

并联系统中，总负荷扰动到第 $i$ 台 VSC 频率响应的闭环传递函数为：

$$\frac{\Delta\omega_{i}(s)}{\Delta P_{L}(s)} = -\frac{G_{i}(s)}{\sum_{m=1}^{n}G_{m}(s)(J_{m}\omega_{0}s + D_{m}\omega_{0} + k_{\omega m})}$$

Hu 等（2025）的关键发现是：并联 VSC 之间的角加速度差异是频率振荡的重要来源，自适应惯量控制根据频率偏差和 RoCoF 动态调整 $J_{i}$，在扰动初期降低最大 RoCoF，在恢复阶段避免惯量过大拖慢响应。

### 无功-电压控制

无功-电压控制通过积分环节模拟同步机励磁特性：

$$E_{i} = \frac{1}{K_{qi}s}\left[Q_{refi} - Q_{0i} + D_{qi}(U_{cni} - U_{c})\right]$$

其中 $K_{qi}$ 是积分系数，$D_{qi}$ 是无功-电压调节系数，$E_{i}$ 是内电势。

### 构网型（Grid-Forming）控制

构网型逆变器不依赖电网 PLL 同步，而是通过虚拟同步机或 droop 控制自主建立电压和频率参考。Nurunnabi 等（2025）展示了 GFM 逆变器在混合光伏-电池 Plant 中的黑启动能力，以及在全黑电力系统场景下的频率和电压支撑。GFM 控制在低惯量电网中尤为重要，储能系统通过虚拟惯量提供短期频率支撑。

### 暂态电磁功率补偿控制

Hu 等（2025）提出的暂态电磁功率补偿控制在频率响应暂态过程中修正电磁功率通道，抵消由并联 VSC 角加速度差异和功率耦合引起的有功功率超调和振荡。自适应惯量系数依据频率偏差和 RoCoF 构造，在线改变 $J_{i}$。

## 大规模并行仿真策略

大规模 BESS 部署（数百至数千台逆变器）对 EMT 仿真构成严峻的计算挑战。

### CPU-GPU 异构并行

Lin 等（2023）提出了面向 AC/DC 电网大规模 BESS 的 CPU-GPU 异构并行建模方法。该方法利用 GPU 的并发多流、多线程能力，实现 EMT 设备级仿真与 TS 机电暂态仿真的异步顺序并行处理。在 IEEE 118 节点系统集成分布式电池的算例中，异构计算实现了超过 200 倍的加速比，使设备级 EMT-TS 联合仿真变得可行。

### 多速率仿真

Hatahet 等（2026）的 D-DEM（解耦详细等效模型）采用多速率仿真架构：CPU 大步长（50 μs）+ GPU 小步长（2.5-5 μs），步长比 10:1 至 20:1。该模型将 MMC 子模块电容电压用前向欧拉显式离散化，节点方程从 4×4 降至 1×1，实现恒定导纳矩阵，在保留闭锁/解锁动态的前提下显著加速仿真。D-DEM 模型相比传统 DEM 模型在 CPU 单实现下加速 2.81 倍，混合 CPU-GPU 求解器相比 CPU 串行实现加速 79 倍。

### 切换插值技术

Hatahet 等（2026）提出的切换插值技术（switching interpolation）精确补偿 MMC 多阀内时间步长的开关事件，弥补多速率仿真中因步长跳跃导致的开关瞬态信息丢失。

## 量化性能边界

BESS 建模的精度-效率权衡已有可核验的量化结果：

| 来源 | 模型 | 加速比 | 验证场景 | 关键发现 |
|------|------|--------|----------|----------|
| Hatahet 等 2026 | D-DEM (CPU) | 2.81× (vs DEM) | MMC-BESS 400 SM/臂 | 节点方程 4×4→1×1，恒定导纳矩阵 |
| Hatahet 等 2026 | D-DEM (CPU-GPU) | 79× (vs CPU串行) | MMC-BESS 400 SM/臂 | 多速率 10:1-20:1，切换插值补偿 |
| Lin 等 2023 | CPU-GPU 异构并行 | >200× | IEEE 118 + 分布式电池 | EMT-TS 联合仿真可行，设备级+系统级精度验证 |
| Wang 等 2025 | 改进 DEM | 未报告 | HVDC 系统 PSCAD/EMTDC | 整流/逆变/STATCOM/闭锁四工况验证 |
| Herath 等 2019 | DEM | 显著减少矩阵维度 | 实验室缩比装置 + Simulink | Thevenin 等效替代开关级，开关节点数大幅降低 |
| Herath 等 2021 | AVM | 支持分析性研究 | 实验验证 | 环流特性分析、电容纹波分析、元件尺寸设计 |
| Stepanov 等 2026 | 四种 MMC 模型对比 | AEM/AVM 加速最高 | EMTP Delta STATCOM | DM→DEM→AEM→AVM 精度递减、加速递增 |

## 关键技术挑战

1. **多时间尺度耦合**：储能系统涵盖微秒（开关瞬变）、毫秒（控制回路）、秒（能量管理）至分钟（SOC 变化）的跨尺度动态。EMT 仿真需要在微秒级时间步长内同时捕捉开关瞬变和缓慢的 SOC 变化，导致计算负担剧增。

2. **大规模可扩展性**：数百至数千台 BESS 逆变器的设备级 EMT 仿真需要并行计算架构。Lin 等（2023）的 CPU-GPU 异构并行实现了 >200× 加速，但模型的可扩展性仍受限于 GPU 内存带宽和通信开销。

3. **闭锁/故障状态建模**：MMC-BESS 在直流故障期间的闭锁状态包含复杂的开关拓扑变化。Wang（2025）通过辅助 PSCAD 开关和插值算法模拟闭锁，但通用 EMT 仿真软件中缺乏标准化的闭锁模型接口。

4. **控制-电磁耦合**：储能变流器的控制环路（PLL、电流环、电压环）与 EMT 电磁暂态存在强耦合。GFM 控制在弱网条件下的稳定性分析需要小信号模型与大扰动 EMT 仿真的交叉验证。

5. **储能介质非线性的 EMT 嵌入**：电池的 $V_{ocv}(SOC)$ 非线性、温度依赖性和老化效应在 EMT 时间尺度上通常被简化，但可能影响长期暂态仿真的准确性。

## 适用边界与选择指南

### 建模方法选择决策表

| 应用场景 | 推荐模型 | 理由 | 失效场景 |
|----------|----------|------|----------|
| 单台 BESS 开关级瞬变分析 | DSM（详细开关模型） | 最高精度，捕捉 IGBT 开关瞬变 | 大规模系统不可行 |
| MMC-BESS 故障/闭锁动态 | D-DEM（解耦详细等效） | 恒定导纳矩阵，支持闭锁状态 | 需要环流/纹波分析时精度不足 |
| MMC-ES 环流/纹波分析 | AVM（平均值模型） | 显式多端口等效，支持解析研究 | 不捕捉开关瞬变 |
| 大规模 BESS 集群 EMT | CPU-GPU 异构并行 + D-DEM | >200× 加速，设备级精度 | GPU 内存受限场景 |
| EMT-TS 联合仿真 | 多速率 + 切换插值 | 10:1-20:1 步长比，信息同步 | 需要微秒级开关精度 |
| 频率支撑/惯量协调 | 小信号模型 + VSG 控制 | 传递函数分析，参数整定 | 大扰动非线性场景 |
| Delta STATCOM + 储能 | AEM/AVM 对比 | 四种模型精度-效率权衡 | 需要子模块级平衡算法时 |

### 储能介质选择指南

| 应用需求 | 推荐介质 | 时间常数 | EMT 建模要点 |
|----------|----------|----------|--------------|
| 频率支撑/调频 | 锂电池 | 秒-分钟 | 二阶 RC ECM + SOC 动态 |
| 高频功率调节/瞬态支撑 | 超级电容 | 毫秒-秒 | 单 RC 模型 + 线性 V-Q |
| 长期能量转移/削峰填谷 | 锂电池（大容量） | 小时级 | 低通滤波等效 + 能量约束 |
| 黑启动/构网型 | 锂电池 + GFM 控制 | 秒级 | VSG 虚拟转子方程 + 黑启动逻辑 |

## 与相关页面的关系

- [[bess-model]]：电池储能设备级模型（ECM、电化学模型）。
- [[energy-storage-converter-model]]：PCS 和并网变流器模型。
- [[dem]]：MMC 详细等效模型（Thevenin 等效）。
- [[average-value-model]]：MMC 平均值模型（分析性研究）。
- [[microgrid-distribution-network]]：微电网中储能的系统角色。
- [[emt-simulation]]：储能 EMT 建模与时域验证背景。
- [[virtual-synchronous-generator]]：VSG 控制是储能参与调频的典型方法。
- [[inertia-control]]：储能提供虚拟惯量的控制策略。
- [[grid-forming-inverter]]：构网型逆变器控制架构。
- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]]：大规模 BESS CPU-GPU 并行仿真。
- [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat]]：D-DEM 解耦等效 + 多速率仿真。
- [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of]]：MMC-STATCOM 嵌入式储能四种建模方法对比。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：并联 VSC-ESS 自适应惯量 + 暂态功率补偿。

## 来源论文

- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]] (Lin 2023) — CPU-GPU 异构并行大规模 BESS 建模，IEEE 118 算例 >200× 加速。
- [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-]] (Wang 2025) — MMC-BESS 四工况 EMT 模型（整流、逆变、STATCOM、闭锁），改进 DEM。
- [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat]] (Hatahet 2026) — D-DEM 解耦等效 + 多速率 CPU-GPU 求解，2.81×/79× 加速。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]] (Hu 2025) — 并联 VSC-ESS 自适应惯量与暂态电磁功率补偿控制。
- [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of]] (Stepanov 2026) — Delta STATCOM 嵌入式储能四种 MMC 建模方法对比。
- [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec]] (Herath 2019) — MMC-ES DEM 建模，Thevenin 等效替代开关级。
- [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage]] (Herath 2021) — MMC-ES AVM 多端口等效，环流/纹波分析。
- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：混合光伏-电池 Plant GFM 逆变器黑启动。
- [[advancing-grid-forming-inverter-technology-comprehensive-pq-capability-and-perfo]] (Nurunnabi 2025) — GFM 逆变器 PQ 能力综合评估。
- 朱琼海, 肖晃庆 (2024) — 基于 MMC 的超级电容储能系统高效仿真方法（中文期刊）。
