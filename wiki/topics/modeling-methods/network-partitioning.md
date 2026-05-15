---
title: "网络分区 (Network Partitioning)"
type: topic
tags: [network-partitioning, decomposition, parallel, co-simulation, latency, domain-decomposition, schur-complement, task-allocation, load-balancing]
created: "2026-05-02"
updated: "2026-05-16"
---

# 网络分区 (Network Partitioning)

## 定义

网络分区（Network Partitioning）是把大规模 EMT 仿真问题按电气边界、计算负载或时间尺度拆分为若干子系统独立求解的核心技术。其数学本质是在网络方程层级引入边界条件，使得子系统内部方程与接口方程可分别处理，从而支持并行计算、多速率仿真、实时任务分配、EMT-相量混合仿真和局部详细建模。

网络分区不是单一算法，而是一类**元方法框架**——具体分区策略（电气边界选址、接口等效形式、同步机制）由仿真目标决定。按分割层次，网络分区可分为**拓扑分割**（按电气距离划分物理边界）、**矩阵分割**（Schur 补、节点撕裂、边界消元）和**计算分割**（任务分配到多核/多机/FPGA/GPU）。具体接口方程和同步协议见 [[interface-technique]] 和 [[direct-interface-technique]]；多步长耦合见 [[multirate-method]]；分区后计算实现见 [[parallel-computing]] 和 [[multithreaded-parallel-computing]]。

## EMT 中的角色

EMT 的微秒级步长和稀疏网络求解使分区具有双重价值：

**计算价值**：降低单个矩阵维度、并行化元件更新、将任务映射到多核、多机或 FPGA 资源。在含数百至数千节点的电网 EMT 仿真中，节点导纳矩阵的直接LU分解复杂度为 $O(n^3)$，即使稀疏矩阵技术可降低常数因子，大规模系统的单步求解时间仍可能超过实时步长约束。网络分区通过把大矩阵拆解为若干子系统独立求逆/求解，理论上可将每步计算复杂度从 $O(n^3)$ 降至 $O(\sum_p n_p^3)$（当子系统规模 $n_p$ 远小于 $n$ 时效果显著），同时天然支持子系统的并行时间推进。

**建模价值**：把研究区域保留为详细 EMT，把外部系统等值、降阶或放到相量域。在大型交直流系统中，MMC-HVDC 或新能源换流站附近的电磁暂态需要微秒级精度，而远端交流网络可能只需要毫秒级机电动态相量描述。网络分区使得 "精细区域 EMT + 粗略区域等值" 的联合仿真成为可能，从而在精度与效率之间取得工程上可接受的平衡。

分区同时也引入新的挑战：边界电压/电流是否连续、接口延迟是否可接受、快慢步长是否稳定、故障和保护事件是否在两侧同步、并行任务映射是否贴合硬件拓扑。这些挑战决定了接口算法的设计必须作为分区框架的核心部分。

## 核心机制：四类分区原理

### 1. 图分区与负载均衡

把电网拓扑表示为图 $G=(V,E)$ 后，可将节点集合划分为 $V_1, \ldots, V_P$。常见优化目标是最小化割边权重，同时控制各分区计算负载不均衡度：

$$
\min \sum_{(i,j)\in E_{\mathrm{cut}}} w_{ij}, \qquad
\left|L_p - \bar{L}\right| \le \epsilon \bar{L}
$$

其中 $w_{ij}$ 是边权重（对应支路导纳或通信流量），$L_p$ 是分区 $p$ 的计算负载，$\bar{L}$ 是平均负载，$\epsilon$ 是允许的不平衡率。负载估计需要考虑节点导纳矩阵阶数、子模块/开关数量和非线性迭代成本，而非仅计节点数——含 MMC 子模块的节点计算成本远高于普通 LCC 节点。

在实时 EMT 中，还需要把源图任务映射到目标处理器图。[[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Bruned 等 2020]] 提出两阶段框架：**Task Separation** 按电气边界划分网络后，**Task Mapping** 再将源图顶点映射到目标处理器拓扑，使通信强的任务尽量放在同一处理器或通信代价较低的相邻处理器上。该文在 HYPERSIM 上测试法国 400 kV/225 kV 网络（3486 母线、1056 条线路、274 台变压器），步长 40 μs，平台为 96 处理器 SGI UV100；图划分启发式在工业规模网络上能在可接受时间内给出可执行映射，用线性规划精确解验证了启发式解质量接近最优。

### 2. 电气边界与物理分区原则

电气距离、弱联络线、长传输线、变压器直流接口和区域边界常被用作候选分区位置。**长线路**（传播延迟 $\tau = l/v$ 大于仿真步长）可用 Bergeron 传输线的自然延迟特性作为物理解耦边界——此时接口方程为 $h_M(t) = 2v_K(t-\tau)/Z_C - h_K(t-\tau)$，无需额外数值延迟即可实现子系统间的近似显式解耦。低阻抗短连接和强控制闭环通常不是安全边界，因为切断强耦合支路会引入较大的等效误差。

分区边界的选取应明确服务于**物理可解释性、计算负载均衡、接口稳定性和工具/平台约束**四个目标中的一个或多个。[[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|Li 等 2020]] 按长线路、弱耦合节点和最少连接母线原则把实际交直流网络拆分为直流子系统和多个交流子系统，交流部分再通过 MATE 形成独立子网络——这一分区策略服务于控制设计场景，需要同时保留换流器附近电磁动态和远端机电动态。

### 3. Schur 补与等效接口

对线性化网络方程执行节点撕裂（node-tearing），将外部节点消去后可得到端口等值阻抗：

$$
Y_{\mathrm{eq}} = Y_{aa} - Y_{ab} Y_{bb}^{-1} Y_{ba}
$$

这一操作在数学上等价于 **Schur 补**。从物理角度理解：$Y_{bb}^{-1} Y_{ba}$ 是外部网络对端口电流的贡献等效，$Y_{\mathrm{eq}}$ 是外部网络在端口处呈现的等效导纳。进一步展开可得戴维南等效电压源：

$$
e_{\mathrm{th}} = Y_{bb}^{-1} i_b, \qquad
Z_{\mathrm{th}} = Y_{\mathrm{eq}}^{-1}
$$

该框架解释了 [[network-equivalent]]、Thevenin/Norton 接口和多端口等值的关系。频率相关外部网络还需要 [[fdne-model]]（Frequency-Dependent Network Equivalent）、[[vector-fitting]] 构造宽频有理近似和 [[passivity-enforcement]] 确保时域稳定性——若等值网络存在无源性违规，可能在 EMT 时域仿真中引入不稳定极点。

[[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|LDE 分解法]] 从线性方程右端项出发，把网络矩阵拆解为 $A = D_{\mathrm{BM}} + L_{\mathrm{DM}}$（对角块矩阵 + 连接域矩阵），利用 Woodbury 恒等式构造全局逆矩阵的直接并行计算公式：

$$
A^{-1} = (D_{\mathrm{BM}} + L_{\mathrm{DM}})^{-1} = D_{\mathrm{BM}}^{-1} - D_{\mathrm{BM}}^{-1} L_{\mathrm{DM}} (I + D_{\mathrm{BM}}^{-1} L_{\mathrm{DM}})^{-1} D_{\mathrm{BM}}^{-1}
$$

该方法的核心洞察是：**连接域矩阵 $L_{\mathrm{DM}}$ 具有由网络支路连接决定的低维稀疏结构**，而非任意稠密耦合，从而在 FPGA 和 GPU 并行架构上实现网络矩阵求逆的直接并行计算，理论上可替代 SC 方法中更重的耦合求解过程。

### 4. 延迟、多速率与小步综合

传输线延迟、离散电感/电容或人工延迟可用于解耦当前步方程，但会改变接口动态。多速率分区中，快区步长 $h_f$ 与慢区步长 $h_s = N h_f$ 需要插值、保持、平均或迭代校正以在接口处维持精度。

**时变 Thevenin/Norton 接口**（[[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|Shu 等 2018]]）的核心接口量包括端口 Thevenin 电压、等效阻抗、连接支路电流和端口节点电压；关键设计包括：移动窗口预测（减少接口延迟）、逐步校正（修正预测误差）、平均技术（压缩快尺度波动向慢网格传递时的混叠）和数值振荡抑制离散化。

**补偿法无延迟并行**（[[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Bruned 等 2026]]）把被切开的连接支路视为需要补偿的边界约束：每个子网在断开补偿支路后独立求解得到端口 Thevenin 等效，主进程再求解小规模边界方程获得补偿电流，使被切开的支路两端满足原网络拓扑连续性。在线性网络中这等价于 Schur 补/边界消元；在非线性 MANA 牛顿迭代框架中，每次迭代都按补偿流程更新。该方法在改进 IEEE-34 节点高渗透率风电配电网（473 节点）中达到约 3.30× 加速，在 3619 节点详细风电场并网系统中达到约 6.02× 加速，且不依赖线路物理延迟——这对于短线路密集或IBR高渗透率网络尤为重要。

**small-step synthesis model**（[[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Zhao 等 2026]]）将半隐式蛙跳法（SILM）形式化为网络分区框架，在接口支路内部用更小步长综合等效：设综合阶数为 $k$，全局步长为 $h$，则内部小步长为 $h/k$。通过 Lyapunov 判据和谱半径分析可推导稳定边界——该方法的核心洞察是：基于储能元件的网络分割接口，其离散稳定性本身可能成为限制步长和并行效率的关键瓶颈，而非仅仅是子系统矩阵规模问题。

## 形式化表达

### 图分区优化模型

$$
\begin{aligned}
\min_{V_1,\ldots,V_P} \ & \sum_{e=(i,j)\in E_{\mathrm{cut}}} c_{ij} \\
\mathrm{s.t.} \ & \bigcup_{p=1}^{P} V_p = V, \quad V_p \cap V_q = \varnothing \ (p\neq q) \\
& \left| L_p - \bar{L} \right| \le \epsilon \bar{L}, \quad \forall p
\end{aligned}
$$

其中 $c_{ij}$ 为边权重（支路导纳或任务间通信量），$L_p = \sum_{i\in V_p} \omega_i$ 为分区 $p$ 的加权负载。

### Schur 补端口等值

对划分子系统 $(a)$ 与外部系统 $(b)$ 的网络方程：

$$
\begin{bmatrix} Y_{aa} & Y_{ab} \\ Y_{ba} & Y_{bb} \end{bmatrix}
\begin{bmatrix} v_a \\ v_b \end{bmatrix} =
\begin{bmatrix} i_a \\ i_b \end{bmatrix}
$$

消去外部节点 $b$ 后端口等值阻抗为：

$$
Y_{\mathrm{eq}} = Y_{aa} - Y_{ab} Y_{bb}^{-1} Y_{ba}
$$

戴维南等效电压源为：

$$
e_{\mathrm{th}} = Y_{bb}^{-1} i_b, \qquad Z_{\mathrm{th}} = Y_{\mathrm{eq}}^{-1}
$$

### 多速率接口同步

快子系统（步长 $h_f$）与慢子系统（步长 $h_s = N h_f$）在一个慢步长内的接口变量传递可用**平均技术**压缩：

$$
\bar{i}_{f\to s}(t) = \frac{1}{N} \sum_{k=0}^{N-1} i_f(t - k h_f)
$$

或**线性插值**重建中间值：

$$
i_s(t + kh_f) \approx i_s(t) + \frac{k}{N} \left[ i_s(t + h_s) - i_s(t) \right], \quad k = 1,\ldots,N-1
$$

### LDE 分解与 Woodbury 恒等式

$$
A^{-1} = (D_{\mathrm{BM}} + L_{\mathrm{DM}})^{-1} = D_{\mathrm{BM}}^{-1} - D_{\mathrm{BM}}^{-1} L_{\mathrm{DM}} (I + D_{\mathrm{BM}}^{-1} L_{\mathrm{DM}})^{-1} D_{\mathrm{BM}}^{-1}
$$

其中 $D_{\mathrm{BM}}$ 沿对角线排列各子系统内部矩阵，可完全并行求逆；$L_{\mathrm{DM}}$ 的低维结构使修正项 $(I + D_{\mathrm{BM}}^{-1} L_{\mathrm{DM}})^{-1}$ 规模远小于原系统。

### 补偿法界面方程

设子系统 $p$ 在断开补偿支路后独立求解，得端口 Thevenin 等效 $(e_p, Z_p)$。主进程组装边界方程：

$$
\sum_{p} i_p(e_p, Z_p) = 0 \quad \Rightarrow \quad v_{\mathrm{bus}} = \left( \sum_p Z_p^{-1} \right)^{-1} \left( \sum_p Z_p^{-1} e_p \right)
$$

补偿电流为：

$$
i_{\mathrm{comp}} = Z_{\mathrm{eq}}^{-1} (v_{\mathrm{bus}} - e_{\mathrm{th}})
$$

## 关键技术挑战

### 挑战 1：接口稳定性

分区后接口处若只用零阶保持（ZOH）或显式延迟，可能在弱阻尼系统中注入虚假能量，导致数值振荡或不稳定。特别是在 Thevenin/Norton 等效阻抗与实际网络阻抗不匹配时，接口等效电路可能产生"虚拟谐振"。多速率接口的数值振荡抑制离散化设计（如 [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|Shu 2018]] 中针对接口模型的专用离散化算法）是关键技术。

### 挑战 2：最优分区边界自动判据

最小割并不等于最佳 EMT 分区。强电气耦合、控制闭环和事件同步可能比割边数量更重要。当前分区边界选择仍依赖经验（如"长线路优先"、"弱联络线优先"），缺乏把拓扑割边、计算负载、接口稳定性、事件同步和硬件通信拓扑统一量化的可审核分区指标体系。

### 挑战 3：IBR 网络的虚假延迟问题

传统基于传输线模型延迟的并行解耦依赖物理传播延迟。在短线路、无合适线路延迟或高 IBR 比例网络中，若人为插入虚假延迟来解耦，会改变暂态波形甚至引入数值振荡。[[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Bruned 2026]] 的补偿法（CM）通过在 MANA 框架内构造边界补偿，在任意支路处实现无延迟解耦，为这一问题提供了解决路线。

### 挑战 4：频率相关等值的无源性

多端口 FDNE（Frequency-Dependent Network Equivalent）若未进行无源性强制（[[passivity-enforcement]]），可能在外推时域响应时产生不稳定极点。需要检查等值阻抗矩阵在全线频率范围内的无源性，并在非无源区域通过并联或修正使其满足无源性约束。

### 挑战 5：实时仿真的任务-硬件映射

实时 EMT 仿真的任务分配不仅要把网络分区，还要把任务贴合到硬件处理器拓扑上。[[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Bruned 2020]] 指出：若忽略处理器间通信代价，即使负载均衡也可能在某个处理器上因等待数据而产生时间步超限（overrun），威胁 HIL 实验的实时性。解决路径包括：图划分时将通信密集任务优先映射到相邻处理器，或采用 FPGA 的细粒度并行架构匹配电力系统稀疏矩阵的结构特性。

## 量化性能边界

| 场景 | 方法 | 规模 | 加速比 | 接口误差 | 来源 |
|------|------|------|--------|----------|------|
| 风电并网并行 | 补偿法 CM5 | 473 节点 | 3.30× | 7.2×10⁻³ % | Bruned 2026 |
| 风电场详细模型并行 | 补偿法 CM8 | 3619 节点 | 6.02× | 0.040 % | Bruned 2026 |
| LCC-HVDC 实时 | MATE-TLM | 2412 母线 | 150–160× | 0.0084–0.0116 | Li 2020 |
| 模块化 SST | 割集-Schur 补 | CHB-MAB-MSST | 950× | ARE < 1 % | Feng 2023 |
| 移频-EMT 混合 | SFA-MATE | IEEE 39 | — (大步长节省) | 与全 EMT 可比 | SFA-EMT 2024 |

注：加速比数据来自原文报告，受测试系统、仿真工具、硬件平台和接口设置影响，不应外推为所有拓扑的通用上限。Zhao 2026 的 small-step synthesis 方法原文未报告可核验的量化加速数据。

## 适用边界与选择指南

| 场景 | 推荐方法 | 接口类型 | 步长策略 |
|------|----------|----------|----------|
| 大规模交流电网 EMT-TS 混合仿真 | MATE + 动态相量接口 | 时变 Thevenin/Norton | AC: 较大步长；DC: 微秒步长 |
| IBR 高渗透率配电网并行加速 | 补偿法（CM）+ MANA | 无延迟边界补偿 | 子网独立 |
| MMC-HVDC 系统多速率 | 时变 Thevenin + 预测校正 + 平均 | 端口等效 + 移动窗口 | 快区: Δt；慢区: NΔt |
| 短线路密集网络 | 补偿法（CM）| 无延迟 | 任意支路解耦 |
| 换流器内部模块化等值 | 割集 + Schur 补 + 子模块诺顿等效 | 端口诺顿支路 | 模块独立并行 |
| 实时 EMT 任务分配 | 图划分启发式 + 负载均衡 | Task Mapping 到处理器拓扑 | 步长 ≤ 实时约束 |
| 需要宽频暂态的分区等值 | FDNE + Vector Fitting + Passivity Enforcement | 频变阻抗 | 预计算 + 时域卷积 |
| 稳定性敏感的储能支路分区 | small-step synthesis（SILM） | 半隐式蛙跳 | 综合阶数 k 决定稳定性边界 |

选择原则：**物理延迟优先**（长线路自然解耦）→ **无延迟补偿法**（短线路/IBR 网络）→ **多速率接口**（不同时尺度子系统）→ **频率相关等值**（宽频外区）→ **图划分+任务映射**（实时硬件平台）。

## 相关方法与相关主题

**EMT 耦合方法**：
- [[interface-technique]]：定义分区之间交换什么变量以及如何同步
- [[direct-interface-technique]]：讨论强耦合或矩阵层面的直接接口
- [[multirate-method]]：专门讨论多步长耦合
- [[hybrid-modeling]]：混合建模仿真

**计算加速**：
- [[parallel-computing]]：分区后并行计算的整体框架
- [[multithreaded-parallel-computing]]：多核 CPU 并行
- [[gpu-parallel-acceleration]]：GPU 加速
- [[fpga-real-time-simulation]]：FPGA 实时仿真

**网络等值与矩阵方法**：
- [[network-equivalent]]：外部网络等值的基础理论
- [[fdne-model]]：频变网络等值
- [[sparse-matrix-techniques]]：分区后矩阵结构与稀疏求解
- [[nodal-admittance-matrix]]：网络方程的矩阵表示

**大规模仿真应用**：
- [[large-scale-grid-simulation]]：使用分区作为大电网可计算性的手段
- [[fast-system-simulation]]：把分区作为加速路线之一
- [[electromechanical-electromagnetic-hybrid-simulation]]：机电-电磁混合仿真

## 来源论文

- [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Bruned 等 2020]]：两阶段任务分离与映射框架，图划分启发式，HYPERSIM 实时仿真，3486 母线 French 电网
- [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|Li 等 2020]]：MATE-TLM 接口，LCC-HVDC 多速率协同仿真，2412 母线系统，150–160× 加速
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|Shu 等 2018]]：时变 Thevenin/Norton + 移动窗口预测 + 逐步校正 + 平均技术，AC/MTDC 多速率
- [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Bruned 等 2026]]：无延迟补偿法（CM）推广到 MANA 框架，FMI 协同仿真，473–3619 节点，3.30–6.02× 加速
- [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|Feng 等 2023]]：CHB-MAB-MSST 割集解耦 + Schur 补，950× 加速，ARE < 1 %
- [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|LDE 分解 2024]]：Linking-Domain Extraction + Woodbury 恒等式，FPGA/GPU 并行矩阵逆
- [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Zhao 等 2026]]：SILM 小步综合模型，储能支路分区稳定性边界
- [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid EMT-TS 2024]]：动态相量接口，buffer sizing 无功扰动法，78,682 母线 Eastern Interconnection
- [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|SFA-EMT 多速率 2024]]：移频分析 + MATE 双 EMTP 副本，IEEE 39 节点，SFA 复包络与 EMT 瞬时值解析一致性
- [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|PET 多速率 2024]]：CHB-DAB 电力电子变压器多速率，跨速率数据传输与交错等效交互算法