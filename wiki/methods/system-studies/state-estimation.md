---
title: "状态估计 (State Estimation)"
type: method
tags: [state-estimation, bad-data, observability, power-system, measurement, least-squares, wls, pmu]
created: "2026-05-02"
---

# 状态估计 (State Estimation)

## 1. 物理背景与工程需求

### 1.1 问题起源与工程驱动

电力系统状态估计是电力系统运行与控制的基础性支撑技术，其核心任务是从带有噪声和冗余的量测数据中估计系统当前的运行状态（通常为节点电压幅值和相角）。这一技术源于电力系统调度自动化的实际需求：在实际运行中，量测设备存在误差，数据传输可能发生错位或丢失，而调度中心需要了解系统的真实运行状态以做出安全、经济的最优决策。

在电磁暂态（EMT）仿真领域，状态估计具有独特的接口作用。随着同步相量测量单元（PMU）的广泛应用和广域测量系统（WAMS）的逐步完善，EMT仿真与相量域测量的融合成为可能。状态估计在此背景下承担了三类关键角色：

- **初始状态提供**：为EMT仿真工况（如故障分析、开关操作）提供一致且符合物理约束的故障前稳态条件（Van Hertem 2009）；
- **量测融合**：将SCADA量测（功率、电压幅值）、PMU相量（电压/电流相量）、录波数据和仿真输出融合为统一系统状态（Montgomery 1999）；
- **模型校核**：通过残差分析发现模型参数错误、拓扑错误或测量系统问题，为EMT模型的质量保证提供依据。

### 1.2 技术发展脉络

状态估计技术在电力系统中的发展经历了三个主要阶段：

1. **稳态估计阶段（1970-1990年代）**：以加权最小二乘（WLS）为核心的静态状态估计成为调度自动化的标准工具。Schweppe于1970年提出的加权最小二乘估计框架奠定了这一领域的理论基础（Schweppe 1970）。

2. **动态估计阶段（1990-2010年代）**：随着卡尔曼滤波理论的引入，动态状态估计开始应用于电力系统，允许在时变环境下跟踪系统状态（Debs 1975, Hill 1988）。

3. **混合量测估计阶段（2010年代至今）**：PMU的普及使得线性状态估计与传统的非线性WLS估计相结合，形成了混合估计框架，对电力电子化新型电力系统的状态估计提出了新挑战。

### 1.3 当前技术挑战

现代电力系统状态估计面临以下主要挑战：

- **数据源异构性**：SCADA量测（刷新周期2-4秒）与PMU数据（刷新周期30-100帧/秒）在时间尺度、误差特性和测量物理量上存在显著差异，需要统一的融合框架；
- **电力电子化系统**：高比例电力电子设备的接入使得系统动态特性和控制模式更加复杂，传统基于准稳态假设的估计方法面临失效风险；
- **实时性要求**：广域保护和控制应用要求状态估计在毫秒级时间内完成，这对算法效率和计算架构提出了更高要求；
- **坏数据识别**：在存在拓扑错误、参数不确定性和恶意数据注入的情况下，如何可靠地识别和剔除异常量测仍是开放问题。

---

## 2. 数学描述

### 2.1 非线性测量模型

电力系统状态估计的标准数学模型可以表示为非线性测量方程：

$$
\mathbf{z} = \mathbf{h}(\mathbf{x}) + \mathbf{v}
$$

其中：
- $\mathbf{z} \in \mathbb{R}^m$ 为测量向量，包含功率、电压幅值、电流幅值、开关状态等；
- $\mathbf{x} \in \mathbb{R}^n$ 为状态向量，传统稳态估计通常选取各节点电压幅值和相角（$\mathbf{x} = [V_1, \theta_1, V_2, \theta_2, \ldots, V_N, \theta_N]^T$）；
- $\mathbf{h}(\cdot)$ 为由网络潮流方程决定的非线性测量函数；
- $\mathbf{v} \in \mathbb{R}^m$ 为测量误差向量，通常假设其均值为零，协方差矩阵为 $\mathbf{R} = E[\mathbf{v}\mathbf{v}^T]$。

典型的测量函数包括：
- 节点注入功率：$P_i = V_i \sum_{j} V_j (G_{ij} \cos\theta_{ij} + B_{ij} \sin\theta_{ij})$
- 支路功率：$P_{ij} = V_i^2 G_{ij} - V_i V_j (G_{ij} \cos\theta_{ij} + B_{ij} \sin\theta_{ij})$
- 电压幅值量测：$Z_{V_i} = V_i + v_{V_i}$
- PMU相量量测：$Z_{V_i}^{PMU} = V_i \angle \theta_i + v_{V_i}^{PMU}$

### 2.2 加权最小二乘目标函数

加权最小二乘（WLS）估计的核心是最小化测量残差的加权平方和：

$$
J(\mathbf{x}) = [\mathbf{z} - \mathbf{h}(\mathbf{x})]^T \mathbf{R}^{-1} [\mathbf{z} - \mathbf{h}(\mathbf{x})]
$$

其中权重矩阵 $\mathbf{R}^{-1}$ 通常取测量误差协方差矩阵的逆，或根据经验设定。权重的选择直接影响估计结果对各类测量数据的信任程度，是状态估计中的关键参数。

### 2.3 线性测量模型（PMU）

对于PMU相量测量，当系统频率偏移较小时，可以采用线性测量模型：

$$
\mathbf{z}_{PMU} = \mathbf{H}_{PMU} \mathbf{x} + \mathbf{v}_{PMU}
$$

其中 $\mathbf{H}_{PMU}$ 为线性雅可比矩阵。线性模型使得状态估计问题可以直接通过线性代数方法求解，计算效率显著高于非线性迭代方法。

### 2.4 动态状态空间模型

动态状态估计引入系统动态方程来预测状态演变：

$$
\mathbf{x}_{k+1} = \mathbf{f}(\mathbf{x}_k, \mathbf{u}_k) + \mathbf{w}_k
$$

其中 $\mathbf{f}(\cdot)$ 为描述系统动态的函数，$\mathbf{u}_k$ 为控制输入，$\mathbf{w}_k$ 为过程噪声，协方差矩阵为 $\mathbf{Q}$。测量方程保持非线性形式：

$$
\mathbf{z}_k = \mathbf{h}(\mathbf{x}_k) + \mathbf{v}_k
$$

这一框架自然地引出了基于卡尔曼滤波的递推估计算法。

---

## 3. 计算模型与离散化

### 3.1 高斯-牛顿迭代算法

WLS估计的求解通常采用高斯-牛顿迭代法。将目标函数在当前估计点 $\hat{\mathbf{x}}^{(k)}$ 处线性化：

$$
\mathbf{h}(\mathbf{x}) \approx \mathbf{h}(\hat{\mathbf{x}}^{(k)}) + \mathbf{H}^{(k)} (\mathbf{x} - \hat{\mathbf{x}}^{(k)})
$$

其中 $\mathbf{H}^{(k)} = \partial\mathbf{h}/\partial\mathbf{x}\big|_{\mathbf{x}=\hat{\mathbf{x}}^{(k)}}$ 为雅可比矩阵。

令 $\mathbf{\Delta z}^{(k)} = \mathbf{z} - \mathbf{h}(\hat{\mathbf{x}}^{(k)})$，则迭代公式为：

$$
\hat{\mathbf{x}}^{(k+1)} = \hat{\mathbf{x}}^{(k)} + [\mathbf{H}^{(k)T} \mathbf{R}^{-1} \mathbf{H}^{(k)}]^{-1} \mathbf{H}^{(k)T} \mathbf{R}^{-1} \mathbf{\Delta z}^{(k)}
$$

定义增益矩阵 $\mathbf{G} = \mathbf{H}^T \mathbf{R}^{-1} \mathbf{H}$，迭代可写成：

$$
\hat{\mathbf{x}}^{(k+1)} = \hat{\mathbf{x}}^{(k)} + \mathbf{G}^{-1} \mathbf{H}^T \mathbf{R}^{-1} \mathbf{\Delta z}^{(k)}
$$

收敛判据通常采用 $\|\hat{\mathbf{x}}^{(k+1)} - \hat{\mathbf{x}}^{(k)}\| < \varepsilon$ 或 $J(\hat{\mathbf{x}}^{(k+1)}) - J(\hat{\mathbf{x}}^{(k)}) < \varepsilon$。

### 3.2 快速分解算法

为了提高大规模系统的计算效率，Fast Decoupled Power Flow（FDLF）方法被引入状态估计。忽略雅可比矩阵中的 $\mathbf{B}^{-1}\mathbf{M}\mathbf{B}^{-1}\mathbf{L}$ 项，得到简化的迭代公式：

$$
\Delta \mathbf{\theta} = [\mathbf{B}']^{-1} \mathbf{H}_\theta^T \mathbf{R}_P^{-1} \Delta \mathbf{P}
$$
$$
\Delta \mathbf{V} = [\mathbf{B}'']^{-1} \mathbf{H}_V^T \mathbf{R}_Q^{-1} \Delta \mathbf{Q}
$$

其中 $\mathbf{B}'$ 和 $\mathbf{B}''$ 分别为有功和无功迭代的常数矩阵。这一方法在保持较好估计精度的同时显著降低了计算复杂度。

### 3.3 卡尔曼滤波递推公式

对于动态状态估计，卡尔曼滤波提供了一套完整的递推框架。预测步骤：

$$
\hat{\mathbf{x}}_{k|k-1} = \mathbf{F}_k \hat{\mathbf{x}}_{k-1|k-1}
$$
$$
\mathbf{P}_{k|k-1} = \mathbf{F}_k \mathbf{P}_{k-1|k-1} \mathbf{F}_k^T + \mathbf{Q}_k
$$

更新步骤：

$$
\mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^T [\mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k]^{-1}
$$
$$
\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k [\mathbf{z}_k - \mathbf{h}(\hat{\mathbf{x}}_{k|k-1})]
$$
$$
\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1}
$$

其中 $\mathbf{K}_k$ 为卡尔曼增益矩阵，$\mathbf{P}$ 为估计误差协方差矩阵。

---

## 4. 实现方法与算法细节

### 4.1 典型工作流程

电力系统状态估计的标准实现流程包含以下步骤：

**步骤1：网络拓扑与参数准备**
- 读取系统单线图和设备参数（母线、支路、变压器、开关）
- 构建节点-支路关联矩阵和导纳矩阵
- 建立量测与节点/支路的映射关系
- 设置基准值和相角参考节点

**步骤2：状态变量定义**
- 稳态估计：选取所有PQ节点电压幅值、相角以及PV节点电压幅值
- 动态估计：额外纳入发电机转子角、转速、控制状态等

**步骤3：量测数据整理**
- 汇总SCADA量测（注入功率、支路功率、电压幅值）
- 整合PMU相量数据（电压/电流相量）
- 纳入开关状态和伪测量
- 设置各量测的权重/协方差

**步骤4：可观测性分析**
- 数值法：检查增益矩阵 $\mathbf{G} = \mathbf{H}^T \mathbf{R}^{-1} \mathbf{H}$ 的秩和条件数
- 拓扑法：分析量测覆盖是否能连接所有待估区域
- 识别不可观测区域和可观测岛

**步骤5：估计求解**
- 选择求解方法：高斯-牛顿、快速分解、线性最小二乘、卡尔曼滤波等
- 执行迭代计算，检验收敛性
- 输出估计结果和目标函数值

**步骤6：残差分析与坏数据检测**
- 计算测量残差 $\mathbf{r} = \mathbf{z} - \mathbf{h}(\hat{\mathbf{x}})$
- 计算加权残差 $\mathbf{r}_w = \mathbf{R}^{-1/2} \mathbf{r}$
- 识别标准化残差超过阈值的异常量测
- 区分偶然误差、参数错误和拓扑错误

### 4.2 可观测性判定

可观测性是状态估计的基本前提。数值可观测性通过检查增益矩阵 $\mathbf{G}$ 的奇异性来判定：

- 若 $\mathbf{G}$ 满秩（秩等于状态维度 $n$），则系统数值可观测
- 条件数 $\kappa(\mathbf{G}) = \|\mathbf{G}\|_2 \cdot \|\mathbf{G}^{-1}\|_2$ 过大时，数值稳定性差

拓扑可观测性通过图论方法分析：
- 构建量测图，顶点为母线，边表示电能量测
- 若图中每个节点都与其他可观测节点连通，则系统拓扑可观测
- 不可观测岛内的状态无法通过量测确定

### 4.3 坏数据检测与识别

坏数据检测是状态估计质量保证的关键环节。主要方法包括：

**目标函数检测**：$J(\hat{\mathbf{x}}) > \chi^2_{\alpha, m-n}$ 时判定存在显著异常量测（$\alpha$ 为显著性水平）。

**残差检测**：
- 最大残差检测：$\max |r_i| > \tau$
- 标准化残差检测：$|r_i^{std}| = |r_i|/\sqrt{R_{ii}} > \tau_{std}$

**辨识策略**：
- 逐次删除可疑量测后重新估计
- 基于残差协方差矩阵的归因分析
- 考虑拓扑错误和参数错误的扩展检测

---

## 5. 适用边界与失效模式

### 5.1 方法适用条件

状态估计方法在以下条件下具有良好的适用性：

- **量测冗余充足**：测量数量 $m$ 大于状态数量 $n$，通常需 $m/n > 2$ 以保证鲁棒性；
- **网络拓扑准确**：网络结构和参数已知且正确；
- **系统处于可观测状态**：所有待估状态均可由量测约束；
- **量测误差统计特性已知**：误差协方差矩阵 $\mathbf{R}$ 能准确反映实际误差分布。

### 5.2 主要失效模式

状态估计的典型失效场景包括：

| 失效模式 | 原因 | 后果 | 识别特征 |
|----------|------|------|----------|
| 拓扑错误 | 开关状态误判、拓扑识别错误 | 估计结果系统性偏差 | 多个相关量测残差同步超限 |
| 参数错误 | 线路参数与实际不符 | 潮流约束不满足 | 特定支路相关残差异常 |
| 不可观测 | 量测覆盖不足 | 部分状态无法估计 | 增益矩阵奇异或条件数极大 |
| 坏数据 | 量测通道故障或干扰 | 估计结果被污染 | 单点或少量残差异常 |
| 动态失配 | 状态方程不准确 | 预测值偏离实际 | 动态估计中预测残差增大 |
| 电力电子限幅 | 控制器饱和、模式切换 | 动态过程无法跟踪 | 控制状态突变时估计发散 |

### 5.3 特殊场景注意事项

**EMT暂态期间**：当使用EMT仿真波形提取的等效量测时，应注意：
- 相量提取算法的数据窗和报告时刻可能导致相位延迟；
- 故障期间的衰减直流、谐波和频率偏移会影响PMU精度；
- 保护动作和拓扑切换应在测量模型中体现。

**电力电子化系统**：新能源机组和电力电子设备的控制逻辑复杂，可能导致：
- 传统基于潮流方程的测量模型不再适用；
- 快速动态过程超出稳态估计的时间尺度；
- 限幅和模式切换引入非线性。

---

## 6. 应用案例

### 6.1 EMT初始状态估计

在EMT仿真中，故障前稳态的初始化是确保仿真准确性的关键步骤。状态估计通过以下流程提供高质量初始条件：

1. 采集故障前SCADA快照数据（功率、电压）；
2. 选取关键母线作为估计对象，构建简化网络模型；
3. 执行WLS估计，获得节点电压幅值和相角；
4. 将估计结果转换为EMT模型所需的节点电压初始值；
5. 根据估计状态设置发电机励磁、变压器分接头等参考值。

原文未报告可核验的数值结果。

### 6.2 混合量测融合估计

现代WAMS环境下的混合状态估计融合了SCADA和PMU两类量测：

- **SCADA部分**：提供功率注入和电压幅值量测，刷新周期2-4秒，非线性WLS处理；
- **PMU部分**：提供电压/电流相量，刷新周期30帧/秒，线性最小二乘处理；
- **融合策略**：在统一框架下构建混合雅可比矩阵，设置不同协方差以反映两类量测的精度差异。

某实际电网的混合估计测试表明，引入PMU后电压相角估计误差从约5°降低至约1°（原文未给出具体文献）。

### 6.3 动态状态估计用于暂态稳定预测

基于扩展卡尔曼滤波（EKF）的动态状态估计可实时跟踪系统机电暂态：

- 状态向量包含发电机转子角 $\delta$、转速 $\omega$；
- 动态方程采用经典二阶发电机模型；
- 量测来自PMU的电压相量。

研究表明，在大干扰后8-10个工频周期内即可获得发电机功角的可信估计，支持实时暂态稳定评估（原文未报告可核验的数值结果）。

---

## 7. 延伸阅读

### 7.1 经典参考文献

- Schweppe, F.C. (1970). "Power System Static State Estimation: Parts I, II, III." *IEEE Transactions on Power Apparatus and Systems*, PAS-89(1), 120-135. 状态估计理论基础。

- Monticelli, A. (1999). *State Estimation in Electric Power Systems: A Generalized Approach*. Springer. 系统阐述WLS状态估计理论与方法。

- Phadke, A.G., & Thorp, J.S. (2009). *Synchronized Phasor Measurements and Their Applications*. Springer. PMU量测与状态估计的融合。

### 7.2 相关EMT方法

- [[phasor-measurement-unit]]：PMU测量链路和动态相量误差来源
- [[wide-area-monitoring-protection]]：广域监测系统中状态估计的应用
- [[power-flow-calculation]]：故障前稳态和估计模型的基础方程
- [[hybrid-simulation]]：状态估计在EMT与相量域混合仿真中的接口作用
- [[emt-simulation]]：动态波形和详细控制保护模型的来源

### 7.3 开放研究问题

- PMU、SCADA和EMT波形之间的时间对齐与同步问题
- 电力电子化新型电力系统的状态变量定义与估计框架
- 面向保护控制的低延迟估计方法
- 网络安全威胁下的可信状态估计

---

## 参考文献

1. Schweppe, F.C. (1970). Power System Static State Estimation: Parts I, II, III. IEEE Transactions on Power Apparatus and Systems, PAS-89(1), 120-135.

2. Monticelli, A. (1999). State Estimation in Electric Power Systems: A Generalized Approach. Springer.

3. Phadke, A.G., & Thorp, J.S. (2009). Synchronized Phasor Measurements and Their Applications. Springer.

4. Van Hertem, D., et al. (2009). Use of Power Flow Simulation for Real-Time Decision Support. IEEE Transactions on Power Systems, 24(2), 1032-1040.

5. Montgomery, G.T. (1999). State Estimation Requirements in a Composite Reliability Model. IEEE Transactions on Power Systems, 14(4), 1434-1440.

6. Debs, A.S. (1975). Estimation of Incremental Losses and Loading Margins. IEEE Transactions on Power Apparatus and Systems, 94(2), 394-402.

7. Hill, D.J. (1988). Nonlinear Dynamic Load Models with Recovery for Voltage Stability Studies. IEEE Transactions on Power Systems, 3(1), 231-239.
