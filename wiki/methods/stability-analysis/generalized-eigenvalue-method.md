---
title: "广义特征根法 (Generalized Eigenvalue Method)"
type: method
tags: [eigenvalue, generalized, stability, oscillation, modal-analysis, small-signal, arnoldi, balanced-truncation]
created: "2026-05-02"
updated: "2026-05-18"
---

# 广义特征根法 (Generalized Eigenvalue Method)

## 定义与边界

广义特征根法求解矩阵束

$$\mathbf{A}\mathbf{v} = \lambda \mathbf{B}\mathbf{v} \tag{1}$$

或等价的广义 Schur 问题，用于分析线性化系统、约束系统或带质量/电容/导纳矩阵的模态结构。当矩阵 $\mathbf{B}$ 可逆时，可转为标准特征值问题 $(\mathbf{B}^{-1}\mathbf{A})\mathbf{v} = \lambda\mathbf{v}$，但显式求逆通常不是数值稳健的实现方式。

在 EMT Wiki 中，本页覆盖广义特征值作为方法的定义、数值机制及其在 EMT 仿真中的适用边界。它不等同于所有 [[eigenvalue-analysis]]，也不自动给出稳定裕度、阻尼要求或控制器设计结论。

## EMT 中的角色

广义特征根法在 EMT 相关研究中承担三类核心角色：

1. **分析线性化系统的固有模态**：对电力系统 DAE 线性化后得到的状态矩阵 $\mathbf{A}$ 求广义特征值，服务于 [[small-signal-analysis]] 和 [[modal-analysis]]。
2. **分析频变网络的谱结构**：对导纳/阻抗矩阵或模型降阶中的矩阵束求特征值，辅助识别病态拟合、模态耦合或尺度差异。
3. **分析离散化系统的数值稳定性**：判断步长、频移或延时近似是否改变关键模态。

## 核心机制

### 广义特征值定义

广义特征值 $\lambda$ 定义为矩阵束 $\mathbf{A}-\lambda\mathbf{B}$ 奇异的点：

$$\det(\mathbf{A}-\lambda\mathbf{B}) = 0 \tag{2}$$

右特征向量满足 $\mathbf{A}\mathbf{v} = \lambda\mathbf{B}\mathbf{v}$，左特征向量满足

$$\mathbf{w}^H\mathbf{A} = \lambda \mathbf{w}^H\mathbf{B} \tag{3}$$

当 $\lambda = \sigma + j\omega$ 时，实部 $\sigma$ 对应模态衰减/增长趋势，虚部 $\omega$ 对应振荡角频率。该解释只在模型、平衡点和线性化假设成立时有效。

### DAE 线性化与状态矩阵

电力系统数学模型通常表述为微分-代数方程组（DAE）：

$$\dot{\mathbf{x}} = \mathbf{G}(\mathbf{x}, \mathbf{z}) \tag{4a}$$
$$0 = \mathbf{H}(\mathbf{x}, \mathbf{z}) \tag{4b}$$

其中 $\mathbf{x} \in \mathbb{R}^n$ 为微分变量（状态量），$\mathbf{z} \in \mathbb{R}^q$ 为代数变量。在平衡点 $(\mathbf{x}_0, \mathbf{z}_0)$ 处线性化：

$$\dot{\mathbf{x}} = \mathbf{G}_\mathbf{x}\mathbf{x} + \mathbf{G}_\mathbf{z}\mathbf{z} \tag{5a}$$
$$0 = \mathbf{H}_\mathbf{x}\mathbf{x} + \mathbf{H}_\mathbf{z}\mathbf{z} \tag{5b}$$

消去代数变量后得到状态矩阵：

$$\mathbf{A} = \mathbf{G}_\mathbf{x} - \mathbf{G}_\mathbf{z}\mathbf{H}_\mathbf{z}^{-1}\mathbf{H}_\mathbf{x} \tag{6}$$

系统振荡模式对应 $\mathbf{A}$ 的共轭复特征值：

$$\lambda_i = \sigma_i \pm j\omega_i \tag{7}$$

### 参与因子

结合左右特征向量计算参与因子 $p_{ki}$，衡量第 $k$ 个状态变量对第 $i$ 个模态的参与程度：

$$p_{ki} = \frac{\phi_{ki}\psi_{ik}}{\phi_i^T\psi_i} \tag{8}$$

其中 $\phi_{ki}$ 为右特征向量 $\boldsymbol{\phi}_i$ 的第 $k$ 个元素，$\psi_{ik}$ 为左特征向量 $\boldsymbol{\psi}_i$ 的第 $k$ 个元素。参与因子受变量缩放和归一化方式影响。

## EMT 数值求解方法

### 稠密中小规模：QZ 分解

对于稠密中小规模问题，广义特征值问题通过广义 Schur 分解（即 QZ 分解）求解：

$$Q^T A Z = T, \quad R^T B Z = S \tag{9}$$

其中 $Q$、$R$ 为正交矩阵，$T$、$S$ 为上三角矩阵，$T - \lambda S$ 的对角元素给出特征值。QZ 分解的计算复杂度为 $O(n^3)$，适合 $n < 5000$ 的问题。

### 大规模稀疏问题：子空间迭代法

对于大规模稀疏系统（如欧洲电网万阶模型），通常只需求解目标谱区（如低频振荡区 $[0.1, 2]$ Hz）的部分特征值。常用方法包括：

| 方法 | 原理 | 适用场景 |
|------|------|---------|
| **Arnoldi 方法** | Krylov 子空间迭代，逐步正交化 | 非对称矩阵 Lanczos 推广 |
| **Lanczos 方法** | 三对角化 $\mathbf{A}$，隐式重启 | 对称/反对称矩阵，存储高效 |
| **Jacobi-Davidson** | 预处理的子空间投影，收敛快 | 求解单特征值/特征簇 |
| **Shift-Invert** | 算子变换 $(\mathbf{A} - \sigma\mathbf{B})^{-1}$ | 定位特定谱区附近特征值 |

### 模型阶数降阶：平衡截断（BT）

[[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]] 提出的穷举模态分析方法将平衡截断（Balanced Truncation, BT）融入模态分析，用于处理大规模电力系统的耦合类识别：

**BT 核心步骤**：
1. 求可控性gramian $\mathbf{P}$ 和可观性gramian $\mathbf{Q}$（Lyapunov 方程）
$$\mathbf{A}\mathbf{P} + \mathbf{P}\mathbf{A}^T + \mathbf{B}\mathbf{B}^T = 0 \tag{10}$$
$$\mathbf{A}^T\mathbf{Q} + \mathbf{Q}\mathbf{A} + \mathbf{C}^T\mathbf{C} = 0 \tag{11}$$
2. 计算 Cholesky 因子 $\mathbf{P} = \mathbf{U}\mathbf{U}^T$，$\mathbf{Q} = \mathbf{L}\mathbf{L}^T$
3. SVD 分解 $\mathbf{U}^T\mathbf{L}$，提取主导奇异值
4. 构造投影矩阵 $\mathbf{T}_L = \mathbf{L}\mathbf{Y}_1\boldsymbol{\Sigma}_1^{-1/2}$，$\mathbf{T}_R = \mathbf{U}\mathbf{W}_1\boldsymbol{\Sigma}_1^{-1/2}$
5. 得到降阶模型 $\mathbf{A}_r = \mathbf{T}_L^T\mathbf{A}\mathbf{T}_R$，$\mathbf{B}_r = \mathbf{T}_L^T\mathbf{B}$，$\mathbf{C}_r = \mathbf{C}\mathbf{T}_R$

**量化性能数据**（[[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]]）：
- 西班牙-法国互联系统（1011 阶）：全模型 1011 阶 → 降阶模型 200 阶，阶跃响应在全频段与原系统高度一致（原文图 1 验证）
- 欧洲互联系统（44,143 阶）：降阶至 3500 阶，计算时间约 3597.5 秒；经典 BT 方法需"数天"，增强 BT 利用稀疏低秩 Cholesky 因式分解将计算时间缩短 2-3 个数量级
- 奇异值范围：西班牙-法国系统 $[10^{1181}, 10^{-14}]$，欧洲系统 $[0.021, 10^{-10}]$

## 分类与变体

| 类型 | 适用对象 | 机制 | 边界 |
|------|---------|------|------|
| 标准特征值分析 | 已消去代数变量的状态空间模型 | 求 $\mathbf{A}$ 的特征值和特征向量 | 消元可能放大病态或改变稀疏结构 |
| 广义特征值分析 | 保留质量矩阵、代数约束或端口导纳矩阵的模型 | 直接处理 $(\mathbf{A}, \mathbf{B})$ 矩阵束 | $\mathbf{B}$ 奇异或近奇异时需特别处理 |
| 闭环增益矩阵特征值 | 阻抗/导纳扫描和 MIMO 稳定判据 | 对频率点上的矩阵增益求特征值轨迹 | 属于小扰动频域判断，不覆盖大扰动和限幅行为 |
| 离散特征值映射 | 数值积分或采样系统 | 分析连续模态映射到离散模态后的误差 | 结论依赖积分公式和步长选择 |
| 模态参与分析 | 线性化状态空间模型 | 结合左右特征向量计算参与因子 | 参与因子受变量缩放和归一化影响 |
| 穷举模态分析 | 大规模互联电力系统 | BT 降阶 + Modified Arnoldi 精确求解 | 需预估降阶阶次和模态截断阈值 |

## 关键技术挑战

1. **大规模 DAE 的数值困难**：大规模电力系统 DAE 线性化后状态矩阵阶数可达数万，QZ 分解 $O(n^3)$ 复杂度不可接受。
2. **矩阵束奇异性处理**：当 $\mathbf{B}$ 奇异（如含纯代数约束）时，广义特征值问题可能退化为 $\mathbf{A}$ 的标准特征值，需显式检测并处理。
3. **广义特征值与 DAE 指标的兼容性**：DAE 阶跃响应和初始条件求解需与广义特征值计算协调，避免虚假高频模态。
4. **特征值-参与因子解释的唯一性**：同一模态可能因变量缩放、归一化方式不同而给出不同参与因子排序。
5. **离散化系统的谱映射精度**：连续时间状态矩阵 $\mathbf{A}$ 的特征值经数值积分离散化后，映射精度与步长和积分方法相关。

## 量化性能边界

| 场景 | 系统规模 | 方法 | 降阶阶次 | 计算时间 | 精度 |
|------|---------|------|---------|---------|------|
| 西班牙-法国互联 [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]] | 1011 阶 | BT + Modified Arnoldi | 200 阶 | 数十秒 | 阶跃响应高度一致 |
| 欧洲互联电网 [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]] | 44,143 阶 | 稀疏低秩 BT | 3500 阶 | 3597.5 s | 全频段频率响应良好 |
| MMC-HVDC 小扰动 [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]] | — | dq0 阻抗矩阵特征值 | — | — | CSCR ≈ 3.7，振荡频率 ≈ 1.15 Hz |
| 动态相量大步长 [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] | — | DP 伴随电路特征值分析 | — | — | 频移仅平移特征值虚部，不消除固有模态 |

**数值稳定性边界**：
- 步长 $\Delta t$ 与连续特征值 $\lambda$ 的关系：隐式梯形积分 $z = (1+\lambda\Delta t/2)/(1-\lambda\Delta t/2)$，要求 $|z| \leq 1$ 以保证数值阻尼
- 广义特征值条件数 $\kappa(\mathbf{A}, \mathbf{B}) = \|\mathbf{A}\|_2 \cdot \|\mathbf{B}^{-1}\|_2$，条件数过大时数值结果不可靠

## 适用边界与失败模式

**适用场景**：
- 线性化点已知且可复现的小扰动稳定分析
- 大规模系统的低频振荡模态扫描（需配合降阶技术）
- 含代数约束的 DAE 系统模态分析
- 阻抗/导纳矩阵的 MIMO 闭环稳定性判断

**失败模式**：
- 在线性化点没有说明或运行点不可复现时解释特征值
- 把单个测试系统的阻尼、频率或稳定边界写成一般电网规律
- 忽略代数变量消元、单位缩放、变量归一化对参与因子的影响
- 对奇异或病态矩阵束直接求逆，造成虚假模态或数值噪声
- 把频率扫描矩阵的特征值轨迹和连续时间状态矩阵特征值混为一谈
- 在存在限幅、饱和、保护切换或控制模式切换时仍用小信号特征值外推大扰动行为

## 相关方法与模型

- [[eigenvalue-analysis]]：更广的页面，覆盖标准特征值、根轨迹、模态解释等
- [[modal-analysis]] 和 [[modal-decomposition]]：强调特征向量、模态形状和变量参与关系
- [[small-signal-analysis]] 和 [[small-signal-stability-analysis]]：把线性化模型的特征值用于稳定判断
- [[state-space-method]]：广义特征值矩阵通常来自状态空间或 DAE 线性化
- [[vector-fitting]] 与 [[frequency-dependent-soil]]：特征值可用于解释频域矩阵拟合和模态变换问题
- [[model-order-reduction]]：BT 等降阶技术是大规模系统模态分析的关键辅助手段

## 来源论文

- [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]] — 提出 BT 增强实现，用稀疏低秩 Cholesky 因式分解加速 gramian 计算，将欧洲电网 44,143 阶系统降至 3500 阶，3597.5 秒完成穷举模态分析
- [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] — 用状态空间特征值和平移关系解释动态相量大步长收益的条件性；频移只移动特征值虚部，不消除固有暂态模态
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]] — 对阻抗/导纳闭环增益矩阵求特征值并作稳定裕度判断；MMC-GFM 并网系统 CSCR ≈ 3.7，振荡频率 ≈ 1.15 Hz
- [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat]] — 用导纳矩阵谱尺度解释有理拟合难度和折叠线等效的作用
- [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen]] — 在参考频率下通过特征值/特征向量构造模态变换，说明模态域线路模型依赖变换矩阵选择
- [[fast-realization-of-the-modal-vector-fitting]] — 利用导纳矩阵特征值和模态变换辅助多端口有理拟合，用于 FDNE 频域网络等值