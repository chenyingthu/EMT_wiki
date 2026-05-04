---
title: "广义特征根法 (Generalized Eigenvalue Method)"
type: method
tags: [eigenvalue, generalized, stability, oscillation, modal-analysis, small-signal]
created: "2026-05-02"
updated: "2026-05-03"
---

# 广义特征根法 (Generalized Eigenvalue Method)

## 定义与边界

广义特征根法求解矩阵束

$$
\mathbf{A}\mathbf{v}=\lambda \mathbf{B}\mathbf{v}
$$

或等价的广义 Schur 问题，用于分析线性化系统、约束系统或带质量/电容/导纳矩阵的模态结构。它与标准特征值问题 $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ 的区别在于右侧包含矩阵 $\mathbf{B}$；当 $\mathbf{B}$ 可逆时可转为 $\mathbf{B}^{-1}\mathbf{A}$ 的标准问题，但显式求逆通常不是数值上稳健的实现方式。

在 EMT Wiki 中，本页覆盖广义特征值作为方法的定义、数值机制和证据边界。它不等同于所有[[methods/eigenvalue-analysis.md]]，也不自动给出稳定裕度、阻尼要求或控制器设计结论。稳定性解释必须说明线性化点、模型阶次、坐标系、矩阵构造和验证方式。

## EMT 中的作用

广义特征根法在 EMT 相关研究中常承担三类角色：

- 分析线性化模型的固有模态、振荡频率和阻尼趋势，服务于[[methods/small-signal-analysis.md]]和[[methods/modal-analysis.md]]。
- 分析频变线路、导纳矩阵或模型降阶中的矩阵谱结构，辅助识别病态拟合、模态耦合或尺度差异。
- 分析动态相量、离散化或时滞模型中的特征值移动，判断步长、频移或延时近似是否改变关键模态。

例如，[[sources/revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits.md]]用状态空间特征值说明频移只移动特征值虚部而不消除固有暂态模态。[[sources/an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-.md]]则把阻抗/导纳矩阵闭环增益的特征值轨迹用于小扰动稳定判断。二者都使用特征值思想，但证据范围和模型对象不同。

## 核心机制

广义特征值 $\lambda$ 表示矩阵束 $\mathbf{A}-\lambda\mathbf{B}$ 奇异的点：

$$
\det(\mathbf{A}-\lambda\mathbf{B})=0.
$$

右特征向量满足 $\mathbf{A}\mathbf{v}=\lambda\mathbf{B}\mathbf{v}$，左特征向量可写为

$$
\mathbf{w}^H\mathbf{A}=\lambda \mathbf{w}^H\mathbf{B}.
$$

当矩阵束来自连续时间线性化系统时，若 $\lambda=\sigma+j\omega$，实部 $\sigma$ 通常对应模态增长或衰减趋势，虚部 $\omega$ 对应振荡角频率。该解释只在模型、平衡点和线性化假设成立时有效。

数值上，稠密中小规模问题常用 QZ 或广义 Schur 分解；大规模稀疏问题常用 Arnoldi、Lanczos、Jacobi-Davidson 或 shift-invert 等子空间方法计算感兴趣的部分特征值。实际选择取决于矩阵规模、稀疏性、目标谱区和矩阵束是否病态。

## 分类与变体

| 类型 | 适用对象 | 机制 | 边界 |
|---|---|---|---|
| 标准特征值分析 | 已消去代数变量的状态空间模型 | 求 $\mathbf{A}$ 的特征值和特征向量 | 消元可能放大病态或改变稀疏结构 |
| 广义特征值分析 | 保留质量矩阵、代数约束或端口导纳矩阵的模型 | 直接处理 $(\mathbf{A},\mathbf{B})$ 矩阵束 | $\mathbf{B}$ 奇异或近奇异时需特别解释 |
| 闭环增益矩阵特征值 | 阻抗/导纳扫描和 MIMO 稳定判据 | 对频率点上的矩阵增益求特征值轨迹 | 属于小扰动频域判断，不覆盖大扰动和限幅行为 |
| 离散特征值映射 | 数值积分或采样系统 | 分析连续模态映射到离散模态后的误差 | 结论依赖积分公式和步长 |
| 模态参与分析 | 线性化状态空间模型 | 结合左右特征向量计算参与因子 | 参与因子受变量缩放和归一化影响 |

## 适用边界与失败模式

广义特征根法适合研究运行点附近的小扰动和线性化模型。它不适合直接替代 EMT 时域故障仿真、保护动作验证或强非线性暂态分析。

常见失败模式包括：

- 在线性化点没有说明或运行点不可复现时解释特征值。
- 把单个测试系统的阻尼、频率或稳定边界写成一般电网规律。
- 忽略代数变量消元、单位缩放、变量归一化对参与因子的影响。
- 对奇异或病态矩阵束直接求逆，造成虚假模态或数值噪声。
- 把频率扫描矩阵的特征值轨迹和连续时间状态矩阵特征值混为一谈。
- 在存在限幅、饱和、保护切换或控制模式切换时仍用小信号特征值外推大扰动行为。

## 代表性来源

| 来源 | 特征值相关作用 | 可采信边界 |
|---|---|---|
| [[sources/revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits.md]] | 用状态空间特征值和平移关系解释动态相量大步长收益的条件性 | 可用于说明频移不消除固有暂态；不提供通用加速结论 |
| [[sources/an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-.md]] | 对阻抗/导纳闭环增益矩阵求特征值并作稳定裕度判断 | 适用于所述小扰动频扫框架；不应外推到故障穿越或多机强非线性 |
| [[sources/a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat.md]] | 用导纳矩阵谱尺度解释有理拟合难度和折叠线等效的作用 | 可说明谱尺度影响建模；量化拟合收益需原文核验 |
| [[sources/assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen.md]] | 在参考频率下通过特征值/特征向量构造模态变换 | 可说明模态域线路模型依赖变换矩阵选择；不代表全频段恒定精度 |
| [[sources/fast-realization-of-the-modal-vector-fitting.md]] | 利用导纳矩阵特征值和模态变换辅助多端口有理拟合 | 可作为频域网络等值中谱分析的来源 |

## 与相关页面的关系

- [[methods/eigenvalue-analysis.md]]：更广的页面，覆盖标准特征值、根轨迹、模态解释等。
- [[methods/modal-analysis.md]]和[[methods/modal-decomposition.md]]：强调特征向量、模态形状和变量参与关系。
- [[methods/small-signal-analysis.md]]、[[methods/small-signal-stability-analysis.md]]：把线性化模型的特征值用于稳定判断。
- [[methods/state-space-method.md]]：广义特征值矩阵通常来自状态空间或 DAE 线性化。
- [[methods/vector-fitting.md]]与[[methods/frequency-dependent-soil.md]]：特征值可用于解释频域矩阵拟合和模态变换问题。

## 修订与证据使用注意事项

- 删除或降级无来源的固定振荡频率范围、阻尼比合格阈值和“工业标准”表述。
- 若页面引用某论文的临界短路比、振荡频率或延时裕度，应在来源条目中保留原文算例、控制策略和验证基线。
- 写“广义特征根法适合处理质量矩阵非单位阵”可以作为方法定义；写“比标准特征值法更准确”需要具体数值例证和矩阵构造。
