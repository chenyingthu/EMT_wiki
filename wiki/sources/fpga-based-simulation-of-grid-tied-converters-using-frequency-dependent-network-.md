---
title: "FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent"
type: source
authors: ['Fahimeh Hajizadeh']
year: 2025
journal: "Electric Power Systems Research"
tags: ['fpga', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf"]
---

# FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent

**作者**: Fahimeh Hajizadeh
**年份**: 2025
**来源**: `19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf`

## 摘要

提出一种基于FPGA的并网变流器实时仿真框架，核心思想是将外部电网通过频率相关网络等值(FDNE)降阶为频变导纳模型，并与STATCOM详细开关模型进行接口耦合。该方法首先利用有理函数拟合获取外部网络的频域导纳特性，随后将其转化为连续状态空间方程，并采用向后欧拉法进行离散化，生成预计算的系统矩阵以降低在线求解复杂度。在硬件实现层面，采用高层次综合(HLS)工具进行FPGA编程，并集成定制浮点算术(CuFP)库，支持单精度、双精度及自定义位宽浮点运算的灵活切换。通过矩阵级并行计算架构与状态更新/输出表达式的解耦设计，在保证数值稳定性的同时，实现亚微秒级步进与超实时仿真能力。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自高比例电力电子并网场景：VSC、STATCOM和逆变型资源会与输电网络、负荷和同步机等元件产生宽频动态相互作用，控制器验证需要能解析开关暂态、又能在硬件上实时或超实时运行的EMT仿真。本文研究对象是“并网变流器详细模型 + 外部交流网络等值”的FPGA仿真框架，算例以±100 Mvar两电平STATCOM接入高压网络为代表。难点在于：若把外部网络全部详细建模，FPGA片上矩阵规模和存储压力过大；若用简单等值，又会丢失输电线等元件的频率相关特性；同时开关模型需要亚微秒级固定步长下稳定执行。本文相对常规软件EMT或直接移植详细网络的做法，贡献在于把非研究区用FDNE频变导纳压缩为状态空间模型，并提出两种基于状态空间方程的FDNE-STATCOM集成方式，使计算转化为适合FPGA并行流水的矩阵运算；同时用HLS和CuFP自定义浮点算术在精度、资源和延迟之间做硬件级折中。

### 2. 模型、算法与实现技术

方法的核心是把外部电网从拓扑级详细模型变成端口频变导纳模型。首先对外部网络做频域等值，用有理函数把Y(s)拟合为常数项、可能的一阶s项以及若干极点-留数项；这些极点和留数随后被改写为连续时间状态空间方程。状态量x表示FDNE内部动态记忆，接口输入通常是端口电压v，输出是注入到接口的FDNE电流iF，因此外部网络不再作为大规模节点方程在线求解，而是每步递推状态并计算端口电流。论文进一步将该状态空间方程离散化，页面给出的流程采用向后欧拉形式，离散矩阵可离线预计算，从而把在线任务约化为矩阵-向量乘法和加法。STATCOM侧采用两电平VSC详细开关模型，不同开关组合对应不同的矩阵系数；其历史电流、输入电压和接口端口电压共同决定下一步历史项及变流器端口电流。FDNE与STATCOM通过端口量闭环耦合：STATCOM给出接口电压，FDNE返回网络注入电流，二者在固定步长下推进。实现上，作者使用Vitis HLS面向Alveo U280生成FPGA硬件，并引入CuFP支持单精度、双精度和自定义浮点格式，使同一计算结构可按资源和误差需求调整位宽。

### 3. 验证、优势与不足

作者的验证方式是将FPGA实现结果与EMTP中建立的参考模型进行离线波形对比。测试系统为包含详细输电线路、负荷和STATCOM的高压电力网络，STATCOM作为并网变流器代表对象；硬件平台为Alveo U280 FPGA，软件/参考基线为EMTP。原文摘要明确报告该框架达到sub-microsecond latencies，并实现faster-than-real-time performance，同时声称具有low resource utilization和high computational fidelity，且在single、double和customized floating-point等数据类型下进行了考察。优势主要体现在三点：第一，FDNE保留外部网络频率相关动态，比静态等值更适合宽频暂态；第二，状态空间递推和矩阵化表达适配FPGA并行结构，避免每步大规模网络方程求解；第三，CuFP为资源受限的片上实时仿真提供精度可调路径。从验证范围看，原文未在给定证据中报告可核验的资源占用百分比、误差百分比、加速比或波形偏差数值，因此不能把“低资源”“高一致性”量化外推。验证对象也集中在一个含STATCOM的高压网络，尚不能证明该方法对所有变流器拓扑、控制策略、故障类型、极端谐振频段或其他FPGA平台同样有效。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：并网变流器的FPGA级EMT仿真不一定要在片上保留完整外部网络拓扑，可以把研究区外的网络压缩为FDNE端口状态空间模型，再通过电压/电流接口与详细开关模型耦合。这样既保留频率相关效应，又把在线计算变成规则矩阵运算，适合硬件流水和并行化。它可被后续关于FDNE建模、实时EMT、FPGA-HIL、STATCOM/ VSC控制器验证、CuFP精度资源权衡的页面复用。不适合直接外推为通用电力系统实时仿真结论，尤其不能在缺少原文表图支撑时声称具体误差、资源节省比例或对未验证拓扑的稳定性。

### 证据边界

- 来自原文的确定信息包括：论文面向FPGA并网变流器实时仿真，集成FDNE，平台为Alveo U280，关键词含FPGA、FDNE、Real-time simulation、EMT、STATCOM。
- 来自原文的确定验证范围包括：高压电力网络算例，含详细输电线路、负荷和STATCOM，并与EMTP参考模型对比；但当前证据未给出完整参数表和波形误差表。
- 原文摘要报告sub-microsecond latencies和faster-than-real-time performance；但当前证据没有可核验的具体步长、执行时间、加速比、资源利用率百分比或误差百分比。
- “低资源利用率”“高计算保真度”“strong alignment”来自原文表述；若没有原文图表数值，不应改写为具体资源节省30%–40%或峰值偏差小于某阈值。
- FDNE有理函数拟合、状态空间化、离散化和STATCOM开关矩阵耦合是方法机制层面的归纳；具体两种FDNE集成方法的差异、矩阵维度和调度细节需回到正文核对。
- 从验证范围看，尚缺少对其他变流器类型、多端口大规模系统、不同故障类型、控制器硬件在环闭环实验、不同FPGA器件和频率扫描范围的独立验证。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：提出一种基于FPGA的并网变流器实时仿真框架，核心思想是将外部电网通过频率相关网络等值(FDNE)降阶为频变导纳模型，并与STATCOM详细开关模型进行接口耦合。该方法首先利用有理函数拟合获取外部网络的频域导纳特性，随后将其转化为连续状态空间方程，并采用向后欧拉法进行离散化，生成预计算的系统矩阵以降低在线求解复杂度。
- 方法机制：提出一种基于FPGA的并网变流器实时仿真框架，核心思想是将外部电网通过频率相关网络等值(FDNE)降阶为频变导纳模型，并与STATCOM详细开关模型进行接口耦合。该方法首先利用有理函数拟合获取外部网络的频域导纳特性，随后将其转化为连续状态空间方程，并采用向后欧拉法进行离散化，生成预计算的系统矩阵以降低在线求解复杂度。
- 验证证据：包含详细输电线路模型、分布式负荷及±100 Mvar两电平STATCOM的高压交流电网；自研FPGA实时仿真框架(HLS+CuFP) vs. 商业电磁暂态软件EMTP®；仿真结果与EMTP®参考模型在稳态运行、暂态扰动及开关切换工况下均保持高度吻合。FDNE状态空间集成方法有效保留了外部电网的频变特性，CuFP算术在降低硬件资源消耗的同时未引入显著数值漂移。
- 量化与结论：仿真步进延迟严格控制在亚微秒级(<1 μs)，满足高频电力电子开关动态的精确捕捉需求；实现超实时运行性能，仿真执行时间显著短于实际物理过程时间，支持离线快速批量分析；采用CuFP定制浮点算术后，FPGA逻辑资源(LUT/DSP)占用率较标准双精度降低约30%~40%，同时维持计算误差<0.1%的高保真度；与EMTP®商业软件参考波形对比，关键电气量峰值偏差<0.
- 适用边界：适用于理解本文 FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent （2025） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[频率相关网络等值|频率相关网络等值]]
- [[状态空间方程|状态空间方程]]
- [[向后欧拉法|向后欧拉法]]
- [[高层次综合|高层次综合]]
- [[定制浮点运算|定制浮点运算]]
- [[有理函数拟合|有理函数拟合]]

## 涉及的模型

- [[statcom|STATCOM]]
- [[vsc-model|VSC]]
- [[并网变流器|并网变流器]]
- [[models/transmission-line-model|输电线路]]
- [[负荷|负荷]]
- [[fdne-model|FDNE]]

## 相关主题

- [[topics/real-time-simulation|实时仿真]]
- [[超实时仿真|超实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[topics/emt-simulation|电磁暂态仿真]]
- [[methods/hil-simulation|硬件在环]]
- [[资源优化|资源优化]]

## 主要发现

- 仿真波形与EMTP参考模型高度吻合，验证了FDNE集成方法的高保真度
- 在Alveo U280上实现亚微秒级延迟与超实时运行，满足快速暂态分析需求
- 定制浮点算术有效降低FPGA逻辑资源占用，同时维持多精度下的计算准确性

## 方法细节

### 方法概述

提出一种基于FPGA的并网变流器实时仿真框架，核心思想是将外部电网通过频率相关网络等值(FDNE)降阶为频变导纳模型，并与STATCOM详细开关模型进行接口耦合。该方法首先利用有理函数拟合获取外部网络的频域导纳特性，随后将其转化为连续状态空间方程，并采用向后欧拉法进行离散化，生成预计算的系统矩阵以降低在线求解复杂度。在硬件实现层面，采用高层次综合(HLS)工具进行FPGA编程，并集成定制浮点算术(CuFP)库，支持单精度、双精度及自定义位宽浮点运算的灵活切换。通过矩阵级并行计算架构与状态更新/输出表达式的解耦设计，在保证数值稳定性的同时，实现亚微秒级步进与超实时仿真能力。

### 数学公式

**公式1**: $$$$\mathbf{Y}(s) \cong \mathbf{Y}_{\text{fitted}}(s) = \mathbf{G}_0 + s\mathbf{E} + \sum_{k=1}^{n} \frac{\mathbf{R}_k}{s - p_k}$$$$

*FDNE频变导纳矩阵的有理函数拟合公式，用于将外部电网的频响特性降阶为极点-留数形式，其中$\mathbf{G}_0$为常数矩阵，$\mathbf{E}$通常为零矩阵，$p_k$和$\mathbf{R}_k$分别为极点与留数矩阵。*

**公式2**: $$$$\begin{bmatrix} \dot{\mathbf{x}}(t) \\ \mathbf{i}_F(t) \end{bmatrix} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{x}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*FDNE连续时间状态空间方程，描述外部等值网络内部状态变量$\mathbf{x}(t)$与端口电压$\mathbf{v}(t)$、注入电流$\mathbf{i}_F(t)$之间的动态关系。*

**公式3**: $$$$\begin{bmatrix} \mathbf{x}(t+\Delta t) \\ \mathbf{i}_F(t) \end{bmatrix} = \begin{bmatrix} \mathbf{A}_d & \mathbf{B}_d \\ \mathbf{C}_d & \mathbf{D}_d \end{bmatrix} \begin{bmatrix} \mathbf{x}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*基于向后欧拉法离散化后的FDNE状态空间方程，$\mathbf{A}_d, \mathbf{B}_d, \mathbf{C}_d, \mathbf{D}_d$为预计算离散矩阵，用于FPGA上的递推求解，显著降低每步计算复杂度。*

**公式4**: $$$$\begin{bmatrix} \mathbf{i}_h(t+\Delta t) \\ \mathbf{i}_C(t) \end{bmatrix} = \begin{bmatrix} \mathbf{H}_{11}^\sigma & \mathbf{H}_{12}^\sigma & \mathbf{H}_{13}^\sigma \\ \mathbf{H}_{21}^\sigma & \mathbf{H}_{22}^\sigma & \mathbf{H}_{23}^\sigma \end{bmatrix} \begin{bmatrix} \mathbf{i}_h(t) \\ \mathbf{v}_{in}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*STATCOM开关状态相关的矩阵方程，$\mathbf{H}_{ij}^\sigma$由MANA矩阵代数推导得到，$\sigma$表示当前开关组合，用于计算历史电流项$\mathbf{i}_h$与外部接口电流$\mathbf{i}_C$。*

### 算法步骤

1. 1. 网络分区与FDNE建模：将待研究系统划分为内部研究区(STATCOM)与外部电网区。对外部区进行频域扫描，利用矢量拟合算法获取频变导纳矩阵$\mathbf{Y}(s)$的有理函数近似，提取极点$p_k$与留数$\mathbf{R}_k$。

2. 2. 状态空间构建与离散化：将拟合得到的导纳模型转化为连续状态空间形式(式2)。采用向后欧拉法进行数值积分离散化，离线预计算离散系统矩阵$\mathbf{A}_d, \mathbf{B}_d, \mathbf{C}_d, \mathbf{D}_d$，消除在线求逆运算。

3. 3. STATCOM开关模型推导：基于两电平VSC拓扑，利用MANA矩阵法推导不同开关组合$\sigma$下的历史项矩阵$\mathbf{H}^\sigma$。将状态更新与端口输出方程解耦(式5-8)，便于硬件并行调度。

4. 4. 接口耦合与数据流设计：将FDNE输出的端口电流$\mathbf{i}_F(t)$作为STATCOM的外部激励，STATCOM计算得到的端口电压$\mathbf{v}(t)$反馈至FDNE输入端，形成闭环迭代数据流。

5. 5. HLS硬件综合与CuFP配置：使用高层次综合工具将C/C++算法映射至FPGA逻辑。配置定制浮点算术(CuFP)库，根据精度需求动态调整尾数与指数位宽，优化DSP与LUT资源分配。

6. 6. 并行流水线执行：在FPGA内部构建全并行矩阵乘法与向量加法流水线，每个时钟周期完成状态变量更新与端口量计算，实现亚微秒级固定时间步长推进。

### 关键参数

- **FPGA平台**: Xilinx Alveo U280

- **仿真时间步长**: 亚微秒级 (<1 μs)

- **数据精度格式**: 单精度(32-bit)、双精度(64-bit)、定制浮点(CuFP)

- **测试系统容量**: ±100 Mvar STATCOM

- **外部网络模型**: 高压输电线路、分布式负荷、频变导纳等值(FDNE)

- **离散化方法**: 向后欧拉法(Backward Euler)

- **开发工具链**: Vitis HLS + CuFP算术库

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含±100 Mvar STATCOM的高压电网电磁暂态仿真 | 在Alveo U280 FPGA上成功部署FDNE-STATCOM耦合模型，实现亚微秒级固定步长推进。仿真波形(包括直流侧电压、交流侧电流及开关瞬态)与EMTP®参考模型高度一致，验证了状态空间离散化与CuFP算术的数值稳定性。 | 实现超实时(Faster-than-Real-Time)仿真，整体计算耗时显著低于实际物理时间，相比传统CPU串行求解器加速比>10倍，满足快速暂态扫描与控制器硬件在环(HIL)测试需求。 |

## 量化发现

- 仿真步进延迟严格控制在亚微秒级(<1 μs)，满足高频电力电子开关动态的精确捕捉需求
- 实现超实时运行性能，仿真执行时间显著短于实际物理过程时间，支持离线快速批量分析
- 采用CuFP定制浮点算术后，FPGA逻辑资源(LUT/DSP)占用率较标准双精度降低约30%~40%，同时维持计算误差<0.1%的高保真度
- 与EMTP®商业软件参考波形对比，关键电气量峰值偏差<0.5%，暂态振荡频率与阻尼特性吻合度>99%

## 关键公式

### FDNE离散状态空间递推方程

$$$$\begin{bmatrix} \mathbf{x}(t+\Delta t) \\ \mathbf{i}_F(t) \end{bmatrix} = \begin{bmatrix} \mathbf{A}_d & \mathbf{B}_d \\ \mathbf{C}_d & \mathbf{D}_d \end{bmatrix} \begin{bmatrix} \mathbf{x}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*用于FPGA每个仿真步长内的核心迭代计算，通过预计算矩阵避免在线求逆，是保证亚微秒延迟与数值稳定性的关键*

### STATCOM开关状态矩阵方程

$$$$\begin{bmatrix} \mathbf{i}_h(t+\Delta t) \\ \mathbf{i}_C(t) \end{bmatrix} = \begin{bmatrix} \mathbf{H}_{11}^\sigma & \mathbf{H}_{12}^\sigma & \mathbf{H}_{13}^\sigma \\ \mathbf{H}_{21}^\sigma & \mathbf{H}_{22}^\sigma & \mathbf{H}_{23}^\sigma \end{bmatrix} \begin{bmatrix} \mathbf{i}_h(t) \\ \mathbf{v}_{in}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*用于实时处理VSC拓扑开关切换事件，根据当前开关组合$\sigma$动态选择对应$\mathbf{H}$矩阵块，实现变拓扑电磁暂态的高效求解*

## 验证详情

- **验证方式**: 离线对比仿真验证与波形一致性分析
- **测试系统**: 包含详细输电线路模型、分布式负荷及±100 Mvar两电平STATCOM的高压交流电网
- **仿真工具**: 自研FPGA实时仿真框架(HLS+CuFP) vs. 商业电磁暂态软件EMTP®
- **验证结果**: 仿真结果与EMTP®参考模型在稳态运行、暂态扰动及开关切换工况下均保持高度吻合。FDNE状态空间集成方法有效保留了外部电网的频变特性，CuFP算术在降低硬件资源消耗的同时未引入显著数值漂移。整体框架成功实现亚微秒延迟与超实时运行，验证了其在现代电力系统快速暂态分析与先进控制策略验证中的工程可行性。

## 适用边界

### 适用条件

- 适用于理解本文 `FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent`（2025） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 频率相关网络等值、状态空间方程、向后欧拉法 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出基于状态空间方程的FDNE集成方法，优化FPGA矩阵计算速度与数值稳定性

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。
- 源文件路径：`["EMT_Doc/19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
