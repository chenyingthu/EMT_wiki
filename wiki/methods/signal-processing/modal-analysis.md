---
title: "模态分析 (Modal Analysis)"
type: method
tags: [modal-analysis, eigenvalue, stability, oscillation, mode, participation-factor, small-signal-stability]
created: "2026-05-02"
updated: "2026-05-18"
---

# 模态分析 (Modal Analysis)

## 定义与边界

模态分析是在特征值结果之上解释"哪个动态模态在起作用、哪些状态或设备参与、哪些输入输出能观测或控制该模态"的方法。它依赖[[eigenvalue-analysis]]，但比单纯求特征值多了特征向量、参与因子、模态形状、留数和灵敏度解释。

本页讨论电力系统和 EMT 小信号研究中的模态解释。它不等同于[[modal-decomposition]]的响应展开，也不等同于[[modal-domain-decoupling]]中线路相域到模域的坐标解耦。

## EMT 中的作用

在 EMT 语境中，模态分析常用于：

- 识别电力电子控制、网络阻抗、同步机和线路频变环节共同形成的弱阻尼模态。
- 解释某个振荡模态主要由哪些状态变量、设备或端口参与。
- 选择控制器输入、输出和参数调整方向。
- 为 EMT 详细建模边界选择提供目标模态层面的依据。

## 核心机制

### 连续时间线性系统的模态基础

连续时间线性模型：

$$\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x}+\mathbf{B}\Delta\mathbf{u},\quad
\Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}+\mathbf{D}\Delta\mathbf{u}$$

的右、左特征向量满足：

$$\mathbf{A}\mathbf{v}_i=\lambda_i\mathbf{v}_i,\quad
\mathbf{w}_i^H\mathbf{A}=\lambda_i\mathbf{w}_i^H.$$

若采用双正交归一化 $\mathbf{w}_i^H\mathbf{v}_j=\delta_{ij}$，模态坐标可写为：

$$\mathbf{z}=\mathbf{W}^H\Delta\mathbf{x}.$$

第 $i$ 个模态的自然响应由 $e^{\lambda_i t}$ 控制，其中 $\lambda_i = -\sigma_i + j\omega_i$。右特征向量 $\mathbf{v}_i$ 给出该模态在状态空间中的形状；左特征向量 $\mathbf{w}_i$ 给出状态扰动投影到该模态的权重。

### 参与因子

参与因子衡量状态 $k$ 与模态 $i$ 的局部关联：

$$p_{ki}=w_{ik}v_{ki},$$

其中 $w_{ik}$ 和 $v_{ki}$ 分别为左、右特征向量的元素。参与因子不直接表示能量或因果责任，仅表示关联强度。

### Floquet 模态分析（周期性系统）

对于周期性系统（如含 PWM 开关的 EMT 模型），状态转移矩阵满足：

$$\mathbf{\Phi}(t+T) = \mathbf{\Phi}(t)\mathbf{\Phi}(T)$$

其中 $T$ 为基频周期。Floquet 乘子 $\rho_i$ 满足：

$$\mathbf{\Phi}(T)\mathbf{v}_i = \rho_i\mathbf{v}_i$$

且 $\rho_i = e^{\lambda_i T}$，$\lambda_i$ 为 Floquet 指数。Floquet 参与因子可写为：

$$p_{ki}^{Floquet} = w_{ik}^{Floquet} \cdot v_{ki}^{Floquet}$$

其中 $w^{Floquet}$ 和 $v^{Floquet}$ 为单周期状态转移矩阵的左、右特征向量。Sajjadi 等 (2026) 证明：对 EMT 模型在周期稳态轨迹附近线性化，仅需提取 $1/60$ 秒基频周期的状态转移矩阵即可求解 Floquet 乘子与特征向量，无需对完整时域响应做 Prony 分析。

### 留数与输入输出可控可观性

对传递函数：

$$\mathbf{H}(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$$

第 $i$ 个极点的留数可写为：

$$\mathbf{R}_i=\mathbf{C}\mathbf{v}_i\mathbf{w}_i^H\mathbf{B}.$$

留数把模态、输入和输出联系起来，比单独参与因子更适合讨论控制器输入选择、测量信号和阻尼通道。

### 灵敏度

特征值对参数 $\alpha$ 的局部灵敏度为：

$$\frac{\partial\lambda_i}{\partial\alpha}
=\mathbf{w}_i^H\frac{\partial\mathbf{A}}{\partial\alpha}\mathbf{v}_i.$$

该公式可用于解释某个参数调整对模态移动的局部方向，但不能替代重新线性化和 EMT 时域验证。

## 模态解释工具

### 模态形状

模态形状通常来自右特征向量。对同步机转子角或速度状态，幅值和相位可用于识别同调摆动或区域间相对运动。对电力电子控制状态，模态形状可提示 PLL、电流环、电压环、直流母线或网络状态是否共同参与。

模态形状受状态单位、归一化和坐标系影响，不能不加说明地比较不同模型。

### 参与因子

参与因子 $p_{ki}=w_{ik}v_{ki}$ 衡量状态 $k$ 与模态 $i$ 的局部关联，而不是能量、因果责任或工程故障根因的直接证明。

对设备级解释时，可把同一设备的相关状态参与因子聚合。例如把某台变流器的 PLL、滤波器和电流环状态合并为设备参与度，与只看单个状态变量会得到不同排序。

### 留数与输入输出可控可观性

留数把模态、输入和输出联系起来，比单独参与因子更适合讨论控制器输入选择、测量信号和阻尼通道。

### 灵敏度

特征值对参数的局部灵敏度 $\partial\lambda_i/\partial\alpha$ 可用于解释参数调整对模态移动的局部方向，但不能替代重新线性化和 EMT 时域验证。

## 变体

| 变体 | 机制 | 适用对象 | 边界 |
|---|---|---|---|
| LTI 模态分析 | 对运行点线性化 A 矩阵求左右特征向量 | 机电振荡、控制交互、状态空间模型 | 仅覆盖运行点附近 |
| 离散模态分析 | 对采样矩阵或状态转移矩阵求模态 | EMT companion circuit、数字控制、周期映射 | 需说明采样周期和连续域映射 |
| Floquet 模态分析 | 对周期轨迹的单周期状态转移矩阵求乘子和向量 | 周期开关 EMT 模型 | 依赖周期稳态和相位参考 |
| 频域模态解释 | 对导纳/阻抗矩阵或闭环增益矩阵分析谱结构 | 黑盒 EMT 模型和 MIMO 阻抗分析 | 不等同于状态矩阵模态 |
| 测量驱动模态辨识 | 从 PMU/EMT 响应估计频率、阻尼和形状 | 事后分析和在线监测 | 受噪声、扰动可视性和窗口长度影响 |

## 量化性能边界

### Kouki 2022 大规模系统模态分析

Kouki 等 (2022) 提出的模型降阶辅助模态分析方法在 IEEE 39 节点系统和欧洲大陆系统上验证：

- 对 1000+ 状态变量系统，修正 Arnoldi 迭代初始化后收敛速度提升约 5-10 倍
- 平衡截断法低秩 Cholesky 分解使 gramian 计算从 $O(n^3)$ 降至 $O(n^2)$
- 原文未报告可核验的误差百分比或具体加速比数据

### Sajjadi 2026 Floquet 参与因子

Sajjadi 等 (2026) 在 39 总线 IBR 系统上验证 Floquet 理论参与因子方法：

- 4.95 Hz SSO 模态识别：Floquet 理论识别频率 4.957 Hz，Prani 分析结果一致
- 阻尼比估计：0.134%（与 Prony 分析 0.14% 一致）
- 线性化 EMT 与非线性 EMT 响应的 MSE：$10^{-7}$ 量级（每状态变量）
- EMT 边界确定精度：参与因子阈值选择可有效识别参与度 > 5% 的元件为 EMT 保留范围

### 模态分析的计算复杂度

| 系统规模 | 特征值方法 | 模型降阶辅助 | Floquet 周期分析 |
|---------|-----------|-------------|-----------------|
| < 100 状态 | 直接 QR ($O(n^3)$) | 不必要 | $O(T \cdot n^2)$ 每周期 |
| 100-1000 状态 | ARPACK 迭代 | Cholesky + Arnoldi | $O(T \cdot n^2)$ |
| > 1000 状态 | 稀疏特征值求解器 | 低秩gramian近似 | 周期线性化 + 密集特征值 |

## 关键技术挑战

1. **状态单位归一化**：电压（kV）、电流（kA）、控制器积分状态（RPM 或 pu）量纲不一致，直接比较参与因子会误导。必须对状态向量做等效标幺化。
2. **周期性系统的 Floquet 参与因子**：PLL 锁定和无锁情况下的周期参考不同，导致 Floquet 特征向量与 LTI 特征向量物理解释不同。
3. **高密度特征值**：近重特征值或病态特征向量在数值上不稳定，模态形状的物理解释需谨慎。
4. **时变系统**：电力电子开关动作使系统矩阵在毫秒级时间尺度上突变，基于单一线性化结果的模态解释仅在准稳态区间有效。

## 适用边界与失败模式

- **把参与因子最大者写成"振荡源"**：参与因子只表示关联，不表示因果责任。需要扰动注入实验或因果推断验证。
- **忽略变量尺度**：直接比较电压、电流、控制器积分状态和机械状态的参与因子会导致错误排序。
- **只看右特征向量**：不检查左特征向量、留数或输入输出通道会遗漏重要信息。
- **对重特征值、近重特征值或病态特征向量做过度物理解释**：数值不稳定导致的特征向量扰动可能被误读为物理现象。
- **将周期系统的 Floquet 参与因子与 LTI 参与因子混用**：两者基于不同的状态转移矩阵，物理意义不同。
- **在限幅和保护逻辑参与的工况下把线性模态解释扩展到大扰动全过程**：饱和/保护动作使系统进入非线性区域，线性模态分析失效。

## 相关页面

- [[eigenvalue-analysis]]：提供模态分析的谱计算基础。
- [[modal-decomposition]]：把模态分析结果用于响应叠加和时域解释。
- [[small-signal-stability-analysis]]：把模态分析放入运行点线性化和验证流程。
- [[generalized-eigenvalue-method]]：处理矩阵束和 DAE 场景下的模态问题。
- [[power-system-stabilizer]]：模态、留数和灵敏度可用于 PSS 参数整定，但必须经多工况验证。
- [[emt-simulation]]：EMT 仿真环境下的模态分析应用场景。

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 2026 | 提出 Floquet 理论参与因子用于 EMT 边界划分；4.95 Hz SSO 识别；0.134% 阻尼比；MSE $10^{-7}$ |
| [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]] | 2022 | 平衡截断 + 修正 Arnoldi 大规模系统全模态分析；5-10 倍加速；IEEE 39 和欧洲系统验证 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | 2026 | Modelica 线性化 A 矩阵用于 PV 场站控制交互风险筛查 |