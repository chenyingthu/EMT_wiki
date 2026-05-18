---
title: "最小二乘法 (Least Squares Method)"
type: method
tags: [least-squares, parameter-estimation, curve-fitting, optimization, system-identification]
created: "2026-05-02"
updated: "2026-05-18"
---

# 最小二乘法 (Least Squares Method)

## 定义与边界

最小二乘法（Least Squares Method, LSM）通过最小化残差平方和来估计模型参数，是 EMT 参数辨识、频响拟合、状态估计、模型校准和曲线拟合中的基础数值方法。

**边界声明**：最小二乘法不是"参数一定可辨识"或"拟合结果一定物理正确"的保证——它只保证在给定模型结构和数据下，求得残差平方意义上的最优解。EMT 建模中使用最小二乘法时，必须同时报告输入数据、误差定义、权重设置、参数范围和验证工况。单一误差指标（如 RMS）下降不等于模型机制正确。

本页关注方法结构、求解流程和 EMT 证据边界。涉及黑盒 EMT 校准时，还需要配合 [[sensitivity-analysis]]（灵敏度分析）、[[parameter-identification]]（参数辨识）和独立波形验证。

## EMT 中的作用

在 EMT wiki 语境中，最小二乘法常用于四类场景：

1. **频域有理拟合**：用频率采样点拟合导纳、阻抗或传递函数，服务 [[vector-fitting]]（矢量拟合）和 [[partial-fraction-expansion]]（部分分式展开）。固定极点后，求留数是线性最小二乘问题；极点重定位阶段也依赖线性最小二乘求解缩放函数系数。

2. **参数校准与反演**：从 EMT 小扰动响应估计状态空间、阻抗或控制器参数。先用 [[sensitivity-analysis]] 筛选关键参数，再用最小二乘反演剩余参数。

3. **波形对齐**：让模型输出波形与录波、测试或高保真仿真结果对齐，常见于换流器模型验证和电机参数辨识。

4. **状态估计**：在 [[state-estimation]] 或参数校准中处理带噪声的测量方程。电力系统量测融合中的加权最小二乘（Weighted LS, WLS）状态估计器即为此类应用。

这些用途都必须报告输入数据、误差定义、权重、参数范围和验证工况。

## 核心形式

### 线性最小二乘

给定观测 $\mathbf{y} \in \mathbb{R}^n$ 和线性模型 $\hat{\mathbf{y}} = \mathbf{X} \boldsymbol{\beta}$，最小二乘问题为

$$
\min_{\boldsymbol{\beta}} \; J(\boldsymbol{\beta})
= \|\mathbf{r}(\boldsymbol{\beta})\|_2^2
= \sum_{i=1}^{n} r_i(\boldsymbol{\beta})^2, \quad r_i = y_i - \hat{y}_i \tag{1}
$$

其中 $\mathbf{X} \in \mathbb{R}^{n \times p}$ 为设计矩阵，$\boldsymbol{\beta} \in \mathbb{R}^p$ 为待估参数向量。残差向量 $\mathbf{r} = \mathbf{y} - \mathbf{X} \boldsymbol{\beta}$。

**正规方程**（Normal Equations）：

$$
\mathbf{X}^T \mathbf{X} \hat{\boldsymbol{\beta}}
= \mathbf{X}^T \mathbf{y} \tag{2}
$$

若 $\mathbf{X}$ 满列秩（$\text{rank}(\mathbf{X}) = p$），解为

$$
\hat{\boldsymbol{\beta}}
= (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \tag{3}
$$

实际计算通常不显式求逆，而用 QR 分解（数值稳定）、SVD（处理秩亏）或带正则化的线性求解器。

### 非线性最小二乘

非线性 EMT 模型常写成

$$
\min_{\boldsymbol{\beta}} \|\mathbf{r}(\boldsymbol{\beta})\|_2^2 \tag{4}
$$

其中 $\mathbf{r}(\boldsymbol{\beta})$ 对参数 $\boldsymbol{\beta}$ 非线性。在当前参数 $\boldsymbol{\beta}_k$ 附近线性化残差：

$$
\mathbf{r}(\boldsymbol{\beta}_k + \Delta \boldsymbol{\beta})
\approx \mathbf{r}_k + \mathbf{J}_k \Delta \boldsymbol{\beta} \tag{5}
$$

其中 $\mathbf{J}_k = \partial \mathbf{r} / \partial \boldsymbol{\beta} \big|_{\boldsymbol{\beta}_k}$ 为雅可比矩阵。Gauss-Newton 步求解

$$
\min_{\Delta \boldsymbol{\beta}}
\|\mathbf{r}_k + \mathbf{J}_k \Delta \boldsymbol{\beta}\|_2^2 \tag{6}
$$

得

$$
\Delta \boldsymbol{\beta} = -(\mathbf{J}_k^T \mathbf{J}_k)^{-1} \mathbf{J}_k^T \mathbf{r}_k \tag{7}
$$

Levenberg-Marquardt 方法加入阻尼项 $\lambda \mathbf{I}$ 改善远离解时的稳定性：

$$
(\mathbf{J}_k^T \mathbf{J}_k + \lambda \mathbf{I}) \Delta \boldsymbol{\beta} = -\mathbf{J}_k^T \mathbf{r}_k \tag{8}
$$

$\lambda$ 自适应调整：残差下降时减小 $\lambda$，发散时增大 $\lambda$。

## 加权与正则化

### 加权最小二乘

测量精度不同或频段重要性不同时，使用加权最小二乘：

$$
\min_{\boldsymbol{\beta}}
(\mathbf{y} - \mathbf{X} \boldsymbol{\beta})^T \mathbf{W}
(\mathbf{y} - \mathbf{X} \boldsymbol{\beta}) \tag{9}
$$

$\mathbf{W} = \text{diag}(w_1, \ldots, w_n)$ 为权重矩阵，通常取 $w_i = 1 / \sigma_i^2$（$\sigma_i$ 为第 $i$ 个测量的标准差）。在 EMT 频响拟合中，权重常用于强调特定频段的重要性。

### 正则化最小二乘

若参数病态或数据不足，加入正则化项：

$$
\min_{\boldsymbol{\beta}}
\|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2
+ \lambda \|\mathbf{L} \boldsymbol{\beta}\|_2^2 \tag{10}
$$

- **Tikhonov 正则化**（$\mathbf{L} = \mathbf{I}$）：约束参数模长，适合参数值物理意义明确的场景。
- **稀疏正则化**（$\mathbf{L}$ 含差分算子）：诱导平滑参数解，适合参数数组（如沿线参数分布）。
- **LASSO**（$\ell_1$ 正则化）：$\lambda \|\boldsymbol{\beta}\|_1$，诱导稀疏参数向量。

$\lambda$ 和 $\mathbf{L}$ 是建模选择，必须说明物理含义或选择规则（交叉验证、L-curve 等）；不应把正则化后的平滑结果直接等同于真实参数。

### 约束最小二乘

显式限制参数范围或符号：

$$
\min_{\boldsymbol{\beta}}
\|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2
\quad \text{s.t.} \quad
\mathbf{A} \boldsymbol{\beta} \leq \mathbf{b}, \;
\boldsymbol{\beta}_l \leq \boldsymbol{\beta} \leq \boldsymbol{\beta}_u \tag{11}
$$

在 EMT 参数辨识中常用于物理参数非负（电感、电容、电阻）、参数有明确上下界（饱和电感需保证单调性）的场景。约束不当会掩盖模型错误。

## 最小二乘在 EMT 中的典型应用

### 矢量拟合（VF）中的线性最小二乘

[[vector-fitting]] 两阶段算法均依赖最小二乘：

**阶段 1（极点重定位）**：给定起始极点 $\bar{p}_m$，通过线性最小二乘求解缩放函数 $\sigma(s)$ 的系数 $a_m$，进而求得 $\sigma(s)$ 的根作为更新后的极点：

$$
\boldsymbol{\sigma} = \mathbf{A} \mathbf{a} \quad \Rightarrow \quad \mathbf{a} = (\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T \boldsymbol{\sigma} \tag{12}
$$

其中 $\mathbf{A}$ 的第 $i$ 行第 $m$ 列为 $1/(s_i - \bar{p}_m)$。这是典型线性最小二乘，解存在且唯一（除非 $\mathbf{A}$ 列相关）。

**阶段 2（留数识别）**：固定收敛后的极点 $p_m$，对单端口系统求解留数 $c_m$、常数项 $d$ 和高频项 $h$：

$$
\begin{bmatrix}
\frac{1}{s_1-p_1} & \cdots & \frac{1}{s_1-p_M} & 1 & s_1 \\
\vdots & \ddots & \vdots & \vdots & \vdots \\
\frac{1}{s_N-p_1} & \cdots & \frac{1}{s_N-p_M} & 1 & s_N
\end{bmatrix}
\begin{bmatrix} c_1 \\ \vdots \\ c_M \\ d \\ h \end{bmatrix}
=
\begin{bmatrix} H(s_1) \\ \vdots \\ H(s_N) \end{bmatrix} \tag{13}
$$

对多端口系统，留数为矩阵 $\mathbf{R}_m$，所有端口共享同一组极点 $\{{p_m}\}$，但留数矩阵各不相同——这仍是线性最小二乘，但设计矩阵扩展为分块结构。

**模态 VF（MVF）**中的加权最小二乘用于解决小特征值被主导的问题：

$$
\min \sum_{k} w_k^2 \left| Y_k^{\text{target}}(j\omega_i) - \sum_m \frac{R_{m,k}}{j\omega_i - p_m} - D_k \right|^2, \quad
w_k = \frac{1}{|\lambda_k|} \tag{14}
$$

其中 $\lambda_k$ 为导纳矩阵 $\mathbf{Y}$ 的特征值，$w_k$ 为逆特征值权重，保证小特征值模态的拟合精度。

### 状态估计中的加权最小二乘

电力系统 [[state-estimation]] 中的 WLS 状态估计器用节点功率方程作为约束：

$$
\min_{\mathbf{x}} (\mathbf{z} - \mathbf{h}(\mathbf{x}))^T \mathbf{W} (\mathbf{z} - \mathbf{h}(\mathbf{x})) \tag{15}
$$

其中 $\mathbf{z}$ 为量测向量（电压幅值、功率注入/流向），$\mathbf{h}(\mathbf{x})$ 为量测函数，$\mathbf{x}$ 为状态向量（电压幅值和相角）。权矩阵 $\mathbf{W} = \mathbf{R}^{-1}$，$\mathbf{R}$ 为量测噪声协方差矩阵。用快速解耦或其他策略迭代求解。

### 参数校准中的非线性最小二乘

数据驱动的 EMT 模型参数校准（[data-driven-parameter-calibration-of-power-system-emt-model-based-on-sobol-sensi]）先用 Sobol 灵敏度分析筛选关键参数，再用非线性最小二乘反演剩余参数：

$$
\min_{\boldsymbol{\beta}} \sum_{k=1}^{N_s} \left\| \mathbf{y}^{\text{EMT}}(\boldsymbol{\beta}, t_k) - \mathbf{y}^{\text{ref}}(t_k) \right\|_2^2 \tag{16}
$$

其中 $\mathbf{y}^{\text{EMT}}$ 和 $\mathbf{y}^{\text{ref}}$ 分别为 EMT 模型输出和参考波形（录波或详细仿真），$N_s$ 为采样点数。黑盒 EMT 校准若无雅可比，只能用差分近似或代理模型，误差边界会显著增大。

### 导纳提取中的最小二乘

从扰动响应提取 VSC 变流器的 dq 导纳模型（[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation]）时，将小信号激励下的电压电流数据拟合为 dq 域传递函数：

$$
\mathbf{Y}_{\text{dq}}(s) = \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D} \tag{17}
$$

其中 $\mathbf{R}_m$ 和 $p_m$ 通过多通道线性最小二乘从频域或时域数据中识别。

## 求解流程

EMT 参数辨识中应用最小二乘的标准工作流：

**步骤 1：定义参数**
- 列出可调参数、单位、范围、物理约束和固定参数
- 明确哪些参数有物理意义（如电感 $L > 0$），哪些可自由取值

**步骤 2：定义残差**
- 说明是波形点误差 $\|\mathbf{v}^{\text{sim}} - \mathbf{v}^{\text{meas}}\|_2$、频域误差 $\|\mathbf{Y}^{\text{sim}}(j\omega) - \mathbf{Y}^{\text{meas}}(j\omega)\|_2$、功率误差还是组合指标
- 残差定义直接影响优化方向——错误定义会导致物理上合理但工程上无用的"最优"解

**步骤 3：缩放和加权**
- 避免量纲差异支配目标函数：高频电压和低频电压误差在同一数量级但物理意义不同
- 对频响拟合，建议按频段分组建模而非全频段等权拟合

**步骤 4：选择求解器**
- 线性问题（正规方程/阶段2 VF）：优先 QR 分解（SVD 对于秩亏系统）
- 非线性问题（参数校准）：需提供初值、收敛准则（$\|\Delta \boldsymbol{\beta}\| < \epsilon$）和失败处理（步长回退、最大迭代次数）
- 正则化问题：Lammps、梯度投影或信赖域方法

**步骤 5：检查可辨识性**
- 查看设计矩阵的秩、奇异值（$\sigma_{\min}/\sigma_{\max}$ 为条件数cond($\mathbf{X}$））、参数相关系数矩阵
- cond($\mathbf{X}$) > $10^6$ 时，数值求解结果不可信，需重新参数化或引入正则化

**步骤 6：独立验证**
- 在未参与拟合的工况、扰动或频段上比较结果（留出验证集）
- 用同一数据集拟合和验证会高估模型可信度——这在 EMT 校准中很常见，需特别注意

## 变体对比表

| 变体 | 机制 | EMT 用途 | 注意事项 |
|------|------|----------|----------|
| 普通最小二乘（OLS） | 等权残差平方和 $\min \|\mathbf{r}\|_2^2$ | 基础曲线拟合、VF 留数识别 | 对异常值敏感；无正则化时不适于病态系统 |
| 加权最小二乘（WLS） | 权重矩阵 $\mathbf{W}$ 调整各残差贡献 | 频段重要性加权、WLS 状态估计 | 权重来源需说明（测量方差、工程经验） |
| 正则化最小二乘 | Tikhonov/LASSO/弹性网等惩罚项 | 病态拟合、降阶、正则化参数辨识 | $\lambda$ 选取影响偏差-方差权衡；正则化后参数物理意义需重新解释 |
| 约束最小二乘 | 参数范围或线性约束 | 物理参数非负、单调性约束 | 约束过于严格会掩盖模型结构问题 |
| 鲁棒最小二乘 | 非二次损失（Huber、Tukey 等）或迭代重加权 | 含异常录波数据的拟合 | 损失函数选择影响解的统计性质 |
| 递归最小二乘（RLS） | 递推更新公式（ Sherman-Morrison  Woodbury） | 在线参数跟踪、实时适应 | 有遗忘因子 $\lambda_{\text{forget}}$；数值稳定性需注意 |

## 量化性能边界

| 指标 | 典型数值 | 来源 |
|------|----------|------|
| VF 留数识别 RMS 误差 | $< 10^{-4}$（典型），$< 10^{-6}$（优化后） | Gustavsen 1999，VF 原始论文 |
| VF 极点收敛所需迭代次数 | 3~8 次（典型），$< 20$ 次（复杂响应） | Gustavsen 1999 |
| WLS 状态估计收敛迭代次数 | 3~6 次（配电系统），5~15 次（输电系统） | 电力系统状态估计通用经验 |
| cond($\mathbf{X}$) 对求解精度的影响 | cond($\mathbf{X}$)。若 $> 10^6$，单精度浮点误差可能掩盖参数真值 | 数值线性代数常识 |
| 非线性 LS 收敛所需迭代 | 5~50 次（Gauss-Newton），取决于初值质量和非线性程度 | 优化理论经验值 |

原文未报告可核验的数值结果时，以上数据来自 Gustavsen 1999 等经典论文的方法验证和工程实践经验，仅供参考。

## 适用边界与失败模式

最小二乘法在 EMT 场景中的常见失败模式：

1. **设计矩阵秩亏**：参数相关或灵敏度很低时，最小残差解不唯一——正规方程 $\mathbf{X}^T \mathbf{X}$ 奇异或病态，此时最小二乘解集为无穷多组，需引入正则化或重新参数化。

2. **频域拟合误差小、时域不正确**：VF 拟合误差 $< 10^{-6}$ 不等于时域故障波形、无源性或稳定性可靠。拟合优度是局部频段内的误差指标，不是全局模型验证。

3. **量纲差异主导目标函数**：高频小信号和低频大信号若在同一 $\|\cdot\|_2$ 下权重相同，小信号误差会被淹没。解决：分组归一化或加权。

4. **同一数据集拟合和验证**：高估模型可信度。标准做法是留出 $20\%$ 数据作为独立验证集。

5. **局部最小与噪声**：非线性最小二乘对初值敏感。EMT 参数校准中，$\mathbf{J}_k$ 近似误差和噪声会导致迭代发散或陷入局部最小。建议：多起点搜索或先验约束。

6. **黑盒 EMT 校准的雅可比缺失**：只能用差分近似（计算代价高）或代理模型（有建模误差），证据边界显著增大。

7. **正则化引入偏差**：Tikhonov 正则化会平滑参数解，当真实参数本身不平滑（如分段常数分布）时，正则化解会产生系统性偏差。

## 与相关页面的关系

- [[sensitivity-analysis]]：判断哪些参数值得估计——参数可辨识性是 LSM 的前置条件。
- [[parameter-identification]]：更广义的参数反演和辨识流程，LSM 是其中最常用的数值求解引擎。
- [[vector-fitting]]：以 LSM 为核心的频域有理拟合方法——VF 中的阶段1（极点重定位）和阶段2（留数识别）均为线性最小二乘。
- [[partial-fraction-expansion]]：固定极点后求留数的表示形式，留数识别是线性 LSM 的直接应用。
- [[state-estimation]]：加权 LSM 在电力系统测量融合中的标准应用——WLS 状态估计器是电力系统运行的核心工具。
- [[small-perturbation-linearization]]：非线性 LSM 迭代中常用局部线性化（泰勒展开），小扰动分析是参数灵敏度估计的理论基础。

## 来源论文

- Gustavsen 1999, "Rational Approximation of Frequency Domain Responses by Vector Fitting" — VF 原始论文，建立两阶段极点重定位框架，阶段1和阶段2均为线性最小二乘；给出了复数起始极点、模态加权等关键机制。
- Noda 2007, "A Binary Frequency-Region Partitioning Algorithm for the Identification of Frequency-Dependent Network Equivalents" — 提出自动频域分段算法，分段后极点通过迹信号识别，留数矩阵在全极点已知后用最小二乘求解；服务于 MPFE 等值模型的建立。
- "An Enhanced Method to Achieve Exact DC Values for Frequency-Dependent Transmission Line Models" — 在 ULM 频变线路模型中嵌入 0Hz 直流约束，通过低频加权改善近直流拟合精度；验证了 LS 拟合中频段划分对直流稳态的影响。
- "Locating Arc Faults on Coupling Two Parallel Transmission Lines Using the Novel Algorithm" — 利用 LSM 时域波形拟合实现双回线路故障测距；在选定的单一模量下用 LSM 减小采样和暂态误差。
- "Electromechanical-Electromagnetic Transient Hybrid Simulation Method" — 在机电-电磁混合仿真接口中，用 LSM 从三相瞬时波形提取三序基波电流，作为机电侧反馈量。