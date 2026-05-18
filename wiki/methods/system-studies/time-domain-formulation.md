---
title: "时域公式化 (Time-Domain Formulation)"
type: method
tags: [time-domain, formulation, state-space, differential-equations, emt-simulation, dae, companion-circuit, nodal-analysis]
created: "2026-05-02"
updated: "2026-05-19"
---

# 时域公式化 (Time-Domain Formulation)

## 定义与边界

时域公式化（Time-Domain Formulation）是把 EMT 研究对象写成随时间推进的电压、电流、磁链、机械量、控制状态和离散事件方程。它回答的是"连续物理和控制逻辑如何变成可逐步求解的方程"，不是某一种积分公式、某个软件流程或某篇论文模型的同义词。

典型连续形式可写为

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},\mathbf{u},t), \quad
\mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},\mathbf{u},t),
$$

其中 $\mathbf{x}$ 为动态状态，$\mathbf{y}$ 为代数变量，$\mathbf{u}$ 为输入或离散控制量。对线路、机器、换流器和保护闭环等对象，方程还可能包含时延、分段逻辑、查表非线性、饱和和拓扑切换。

本页讨论 EMT 方程组织方式，不把"时域"写成天然高精度或天然实时。精度和可信度取决于模型频带、步长、积分方法、事件处理、初值一致性和验证参考。

## EMT 中的作用

EMT 仿真直接计算瞬时值，因此适合研究开关暂态、行波、换流器控制、保护动作、故障注入和非线性元件。时域公式化承担三个接口任务：

- 把元件物理关系转成状态方程、代数约束或端口等效。
- 把网络连接写成 KCL/KVL 或节点导纳方程。
- 把开关、限幅、保护和控制采样转成离散事件或分段方程。

在 EMTP 类流程中，动态元件常经 [[companion-circuit]] 离散为等效导纳和历史源，再进入 [[nodal-analysis]] 或 [[nodal-admittance-matrix]]。在方程导向建模中，元件也可以保持 ODE/DAE 表达，由工具链进行方程排序、撕裂和数值求解。两者都是时域公式化的实现路线，差别在于方程何时、由谁、以何种数值结构离散。

## EMT 建模方法

### 方法一：伴随电路/节点导纳法（Companion Circuit — Nodal Admittance）

伴随电路法是 Dommel 于 1969 年提出的经典方法，是商业 EMT 程序的主流底层公式化路线 [[nodal-analysis]]。

基本思想是对每个 R/L/C 分支用数值积分规则（梯形法或后向欧拉）离散，得到等效电阻（伴随电导）与历史电流源的并联结构：

$$
i_{L,n+1} = \frac{\Delta t}{2L}(v_L^{n+1} + v_L^n) - i_{L,n}, \quad
i_{C,n+1} = \frac{\Delta t}{2C}(v_C^{n+1} - v_C^n) + i_{C,n}.
$$

离散后的线性网络写成节点方程：

$$
\mathbf{Y}_{n+1}\mathbf{v}_{n+1} = \mathbf{i}_{src,n+1} + \mathbf{i}_{hist,n+1}.
$$

其中 $\mathbf{Y}_{n+1}$ 由电阻、伴随电导和开关状态决定，$\mathbf{i}_{hist,n+1}$ 来自电感/电容历史项。稀疏矩阵技术使该方法可扩展至数十万节点实时仿真（如 EMTP-Workbench、PSCAD/EMTDC）。

**优点**：大规模网络稀疏矩阵求解效率高；固定步长下网络方程结构不变，矩阵可预分解复用；实时仿真天然适配。
**缺点**：变步长需重构 $\mathbf{Y}$；开关组合爆炸时预计算矩阵内存压力大；状态空间控制器需额外的接口处理。


### 方法二：状态空间公式化（State-Space Formulation）

状态空间法以微分方程组 $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u},t)$ 为入口，状态量对应独立储能元件变量（电容电压、电感电流）。通过数值积分（ODE 求解器）推进状态。

连续状态空间方程：

$$
\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \quad
\dot{\mathbf{y}} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}.
$$

用梯形法离散化（第 $n+1$ 步）：

$$
\mathbf{x}_{n+1} = \mathbf{x}_n + \frac{\Delta t}{2}\left[\mathbf{f}(\mathbf{x}_n,t_n) + \mathbf{f}(\mathbf{x}_{n+1},t_{n+1})\right].
$$

**优点**：积分规则可选（龙格库塔、Gear、多步法）；便于小信号/特征值分析；控制模型自然嵌入；变步长实现灵活。
**缺点**：大规模系统状态空间矩阵合成耗时；开关拓扑变化需重新生成矩阵全集；稀疏性不如节点法。

**EMT 中的关键接口**：状态空间方程经伴随等效后可接入节点方程（见方法三 SSN），实现两者优势互补。


### 方法三：状态空间节点法（State-Space Nodal, SSN）

SSN 方法（Dufour et al., 2011）将状态空间子系统作为"集群"离散化后嵌入全局节点导纳矩阵，实现同步求解 [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|State-Space Nodal Method]]。

**核心机制**：集群内部用状态空间方程描述，端口为集群与外网络的连接节点；用梯形积分把状态空间方程离散为

$$
\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \mathbf{B}\mathbf{u}_n + \mathbf{H}_{n+1},
$$

其中 $\mathbf{H}_{n+1}$ 是由上一时刻历史项构成的长度为 $N$ 的列向量，$\mathbf{A}$ 和 $\mathbf{B}$ 来自梯形积分系数。输出端口电流可写成

$$
\mathbf{i}_{port,n+1} = \mathbf{G}_{port}\mathbf{v}_{port,n+1} + \mathbf{i}_{hist,n+1},
$$

其中 $\mathbf{G}_{port}$ 是端口等效导纳矩阵。这使得状态空间集群等价于一个诺顿（V型）或戴维南（I型）端口等效，可直接装配进全局 $\mathbf{Y}$ 矩阵。

**计算流程**：
1. 各集群根据上一时刻状态计算历史源项 $\mathbf{H}_{n+1}$ 和 $\mathbf{i}_{hist,n+1}$；
2. 把端口等效导纳 $\mathbf{G}_{port}$ 贡献装配到全局节点导纳矩阵 $\mathbf{Y}$；
3. 一次求解 $ \mathbf{Y}\mathbf{v}_{n+1} = \mathbf{i}_{src,n+1} + \mathbf{i}_{hist,n+1}$ 得到所有连接节点电压；
4. 各集群用新电压回代更新内部状态 $\mathbf{x}_{n+1}$。

**优势**：兼具状态空间法的控制器/分组建模便利性和节点法的大规模稀疏求解能力；分组独立处理开关事件，减少全系统矩阵重建开销；适合实时仿真。
**局限**：初值一致性需额外处理；强非线性元件迭代时仍需各集群独立迭代。


### 方法四：描述符状态空间方程法（Descriptor State-Space Equations, DSE）

描述符状态空间方程（Sinkar et al., 2021）允许状态变量线性相关，用修正节点分析（MNA）直接从网表自动生成，避免严格状态变量法的拓扑约束 [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|Descriptor State-Space Equations]]。

**核心方程**：

$$
\mathbf{E}\dot{\mathbf{x}} = -\mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}.
$$

$\mathbf{E}$ 可为奇异矩阵，包含节点电压、电感支路电流和电压源电流等 MNA 变量，使代数约束与动态方程共存。$\mathbf{A}$ 为状态矩阵，$\mathbf{B}$ 为输入矩阵。

用梯形积分离散化：

$$
\left(\mathbf{E} + \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_{n+1} = \left(\mathbf{E} - \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_n + \frac{\Delta t}{2}\mathbf{B}(\mathbf{u}_{n+1} + \mathbf{u}_n).
$$

**与伴随电路接口**：DSE 子网转化为诺顿等效 $\mathbf{i}_p(t) = \mathbf{G}_n\mathbf{v}_p(t) + \mathbf{I}_{HIST}$，嵌入 CC 求解器的全局节点方程，使 DSE 模块可无时间步延迟接入商业 CC 型 EMT 环境。

**优势**：自动网表生成无需拓扑分析；状态变量线性相关避免割集/回路约束；可直接提取系统特征值用于小信号分析；DSE 与 CC 等价（时域精度一致），且可嵌入商业仿真器。
**局限**：大规模纯时域仿真中 CC 因不含电感电流状态矩阵，平均约快 1.3 倍；并行加速需分区、端口同步等额外设计。


### 方法五：半解析状态空间法（Semi-Analytical SS）

半解析方法（Xiong et al., 2024）从状态空间模型出发，用微分变换推导出高阶局部幂级数解，在大步长下同时获得推进、误差估计、步内波形重构和事件定位能力 [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation|Semi-Analytical SS]]。

**核心思想**：状态演化用时间幂级数近似

$$
\mathbf{x}(t) \approx \sum_{k=0}^{N} \mathbf{c}_k t^k, \quad t \in [t_n, t_{n+1}],
$$

其中系数 $\mathbf{c}_k$ 由微分变换递推计算（非线性项通过系数卷积处理）。级数在步内可多次求值（密集输出），高阶项提供截断误差估计用于自适应步长。事件检测用二分搜索定位开关时刻，再用二次插值精确化。

**优势**：大步长下保留步内快变细节；自适应步长无需固定网格；事件定位比简单跨步插值更精确。
**局限**：级数收敛性依赖系统动力学；幂级数求导在高维系统中计算开销增大；尚未在商业 EMT 软件中广泛验证。


### 方法六：分裂状态空间法（Splitting State-Space）

分裂状态空间法（Fu et al., 2025）将时变状态矩阵拆分为常数部分与开关相关时变部分，使常数矩阵的矩阵指数可复用，避免每个开关事件都对完整矩阵求指数 [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Splitting State-Space Method]]。

**核心机制**：原系统 $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$ 的矩阵指数分裂为

$$
\mathbf{A} = \mathbf{A}_1 + \mathbf{A}_2(s), \quad \exp(\Delta t \cdot \mathbf{A}) \approx \prod_k \exp(\alpha_k \Delta t \cdot \mathbf{A}_1) \cdot \exp(\beta_k \Delta t \cdot \mathbf{A}_2(s)),
$$

其中 $\mathbf{A}_1$ 包含不随开关状态变化的网络部分，$\mathbf{A}_2(s)$ 只保留由开关状态 $s$ 决定的最小子电路贡献。通过自动开关分组（Switch-Associated State Variable, SASV）识别定位最小开关相邻变量集。

**优势**：常数矩阵指数只计算一次并缓存；开关相关子矩阵只在状态变化时更新；适用于含大量电力电子开关的系统（如 MMC 子模块阵列、风电场变流器集群）。
**局限**：分裂误差与阶数相关；误差控制机制尚未标准化；主要验证于变流器集成系统，对纯电网拓扑泛化性待确认。

## 形式化表达

### 核心微分代数方程（DAE）

EMT 系统的一般时域形式为 differential-algebraic equation (DAE)：

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x},\mathbf{y},t), \quad
\mathbf{0} = \mathbf{g}(\mathbf{x},\mathbf{y},t),
$$

其中 $\mathbf{x}$ 为动态状态（电感电流/电容电压/磁链/控制状态），$\mathbf{y}$ 为代数状态（节点电压/开关位置）。

### 梯形积分离散化

对 $\dot{x}=f(x,t)$ 应用梯形积分：

$$
x_{n+1} = x_n + \frac{\Delta t}{2}\left[f(x_n,t_n) + f(x_{n+1},t_{n+1})\right].
$$

该隐式关系需对非线性 $f$ 进行迭代求解（Newton-Raphson），每次迭代需重新评估 $\mathbf{f}$ 和雅可比矩阵。

### 后向欧拉离散化

$$
x_{n+1} = x_n + \Delta t \cdot f(x_{n+1},t_{n+1}).
$$

一阶耗散更强，数值阻尼更大，在不连续点附近振荡较轻，但精度低于梯形法。

### SSN 端口等效方程

V型（诺顿）等效：

$$
\mathbf{i}_{port,n+1} = \mathbf{G}_{port}\mathbf{v}_{port,n+1} + \mathbf{i}_{hist,n+1}.
$$

全局节点方程：

$$
\mathbf{Y}\mathbf{v}_{n+1} = \mathbf{i}_{src,n+1} + \mathbf{i}_{hist,n+1}.
$$

### DSE 离散方程

$$
\left(\mathbf{E} + \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_{n+1} = \left(\mathbf{E} - \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_n + \frac{\Delta t}{2}\mathbf{B}(\mathbf{u}_{n+1} + \mathbf{u}_n).
$$

## 关键技术挑战

### 挑战一：开关事件与拓扑突变

含理想开关、阶跃源和分段非线性的网络在事件时刻破坏方程连续性。若历史项重初始化不一致或事件定位不精确，会产生虚假能量注入和数值振荡。处理策略包括：

- **插值定位**：在固定步长网格上检测开关越界，用插值估计事件时刻；
- **变步长策略**：在事件邻域自动缩小步长，检测到开关动作后重新初始化；
- **伴随电路重置**：事件后根据新拓扑重新计算等效导纳和历史源。

### 挑战二：初值一致性（Initialization）

DAE 系统要求初始条件满足代数约束 $\mathbf{g}(\mathbf{x}_0,\mathbf{y}_0,0)=\mathbf{0}$。当初值不一致时，仿真第一步即产生瞬态冲击，影响结果可信度。SSN 和 DSE 方法中，各集群/子网独立初始化后接入全局方程时，尤其需保证接口量（电压/电流）的协调。

### 挑战三：大规模稀疏矩阵管理

大型 EMT 网络节点数可达数十万，节点导纳矩阵 $\mathbf{Y}$ 稀疏但阶数高。LU 分解的fill-in、稀疏存储格式（CSR/CSC）、预条件子和迭代求解器选择是影响仿真效率的关键。SSN 方法通过分组减少全局矩阵重建频率，但组内矩阵更新仍需优化。

### 挑战四：快慢尺度混合

电力电子开关（微秒级）与机电暂态（秒级）在同一系统中共存，统一小步长计算代价极高。常用策略包括：

- **多速率方法**：不同子系统用不同步长，通过接口同步；
- **状态空间模型降阶**：对慢动态部分保留相量或平均值模型；
- **动态等值**：对大规模风电场/换流器站用聚合等效模型替代详细子模块。

### 挑战五：非线性收敛与雅可比病态

Newton-Raphson 迭代求解非线性 DAE 时，雅可比矩阵若病态则收敛缓慢或发散。处理方法包括：

- **线搜索**：在牛顿方向上缩小步长改善收敛性；
- **替代迭代**：对极端非线性元件（如电弧）用分段线性或查表替代牛顿迭代；
- **自适应步长**：在非线性强时缩小步长缓解病态条件。

## 量化性能边界

| 公式化方法 | 计算效率 | 精度 | 适用场景 | 代表论文 |
|---|---|---|---|---|
| 伴随电路/节点导纳 | 高（稀疏矩阵，固定步长最优） | 二阶精度（梯形） | 大规模网络、实时仿真、开关网络 | Dommel 1969 |
| 状态空间公式化 | 中等（矩阵合成开销大） | 取决于积分规则 | 控制设计、小信号分析、变步长 | - |
| SSN（状态空间节点法） | 高（稀疏+分组复用） | 二阶精度 | 含状态空间子网的大规模系统 | Dufour et al. 2011 |
| DSE（描述符状态空间） | 与CC相近（可嵌入CC框架） | 二阶精度（与CC等价） | 自动网表生成、特征值分析、DSE-CC接口 | Sinkar et al. 2021 |
| 半解析状态空间 | 大步长效率高（变步长） | 高阶精度 | 变步长仿真、事件精确定位 | Xiong et al. 2024 |
| 分裂状态空间 | 开关频繁时效率高（矩阵指数复用） | 分裂阶数决定 | 含大量电力电子开关的系统 | Fu et al. 2025 |

**来源论文量化数据**：
- Sinkar 2021：DSE-CC 混合接口在含 LCC-HVDC 的 IEEE 39 节点系统中端口相电流最大绝对误差 0.003 kA，相对误差 0.15%；纯时域 CC 仿真平均比 DSE 快 1.3 倍。
- 半解析法和分裂法的数值验证尚未在 deep-review 中提供可核验的加速比/误差数据，需回到原文表图核验。

## 适用边界与选择指南

| 应用场景 | 推荐公式化方法 | 不推荐方法 | 原因 |
|---|---|---|---|
| 大规模纯电网 EMT（固定步长） | 伴随电路/节点导纳 | 分裂状态空间 | 节点法稀疏效率最优，分裂开销无收益 |
| 含复杂控制器/状态空间子系统 | SSN | 纯伴随电路 | SSN 自然嵌入状态空间模型 |
| 自动网表建模 + 小信号分析 | DSE | 半解析状态空间 | DSE MNA 自动生成，支持特征值提取 |
| 高频变流器详细开关模型（多开关） | 分裂状态空间 | 伴随电路 | 常数矩阵复用，开关子矩阵局部更新 |
| 变步长 + 事件精确定位 | 半解析状态空间 | 固定步长 CC | 大步长下密集输出 + 二分搜索 |
| 实时硬件在环仿真 | 伴随电路/节点导纳 + SSN | 半解析 | 固定步长可预计算，实时确定性高 |

## 分类与变体

| 公式化路线 | 主要未知量 | EMT 用途 | 边界 |
|---|---|---|---|
| 伴随电路/节点导纳 | 节点电压、支路历史源 | 传统固定步长 EMT、实时仿真、线路和 RLC 网络 | 历史项和事件重初始化必须正确 |
| 状态空间公式化 | 状态向量和输入输出矩阵 | 控制、线性开关电路、模态分析、局部模型验证 | 强拓扑切换和非线性约束会复杂化 |
| 完全隐式 DAE | 状态、代数变量和残差 | 方程导向建模、机网联立、混合仿真接口 | 初值一致性和雅可比病态是主要风险 |
| 端口等效公式化 | 端口电压电流、等效导纳/源 | 电机、MMC、FDNE、外部网络等值 | 端口等效不能自动保留所有内部状态 |
| 时延/卷积公式化 | 端口历史量、卷积状态 | 分布参数线路、频率相关模型 | 拟合质量、无源性和步长变化需验证 |

## 与相关页面的关系

- [[algebraic-characterization]]：说明时域方程离散后如何统一成代数残差。
- [[dae-solvers]]：求解隐式时域公式化产生的 DAE 或非线性残差。
- [[companion-circuit]]：EMTP 类时域公式化的关键实现形式。
- [[nodal-analysis]]：节点方程的组装与求解方法。
- [[trapezoidal-rule]] 和 [[backward-euler]]：常见底层积分规则。
- [[gear-method]]：适合 stiff DAE 的多步法。
- [[numerical-oscillation-suppression]]：处理不连续点和积分高频误差。
- [[emt-simulation-verification]]：为时域公式化结果提供可审计验证流程。

## 来源论文

- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|Dufour et al. 2011]] — SSN 方法：状态空间集群离散化为诺顿/戴维南等效，嵌入全局节点导纳矩阵同步求解；适合大规模开关网络和实时仿真
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|Sinkar et al. 2021]] — DSE 方法：描述符状态空间方程 MNA 自动生成，Eẋ=-Ax+Bu 允许线性相关状态；DSE-CC 接口无延迟，误差 0.15%
- [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation|Xiong et al. 2024]] — 半解析法：高阶幂级数解 + 密集输出 + 二分搜索事件定位；IEEE 39 节点验证，优于传统数值方法
- [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Fu et al. 2025]] — 分裂状态空间：开关相邻状态变量定位 + A=A1+A2(s) 分解；配电/风电场/MMC 算例验证
- [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Wang 2010]] — VBR 机器模型：端口等效导纳和历史源形式，便于接入 EMT 网络
- [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-|Modelica 异步机]] — 方程导向时域公式化，DAE/ODE 层面保留磁链状态
- [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st|MSEMT Modelica 库]] — 声明式 DAE 和连接方程表达，模型与求解器解耦
- [[numerical-integration-by-the-2-stage-diagonally|2S-DIRK 积分]] — 有阻尼时域离散路线，振荡抑制优于梯形法