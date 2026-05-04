---
title: "模态分析 (Modal Analysis)"
type: method
tags: [modal-analysis, eigenvalue, stability, oscillation, mode, participation-factor, small-signal-stability]
created: "2026-05-02"
updated: "2026-05-03"
---

# 模态分析 (Modal Analysis)

## 定义与边界

模态分析是在特征值结果之上解释“哪个动态模态在起作用、哪些状态或设备参与、哪些输入输出能观测或控制该模态”的方法。它依赖[[eigenvalue-analysis]]，但比单纯求特征值多了特征向量、参与因子、模态形状、留数和灵敏度解释。

本页讨论电力系统和 EMT 小信号研究中的模态解释。它不等同于[[modal-decomposition]]的响应展开，也不等同于[[modal-domain-decoupling]]中线路相域到模域的坐标解耦。

## EMT 中的作用

在 EMT 语境中，模态分析常用于：

- 识别电力电子控制、网络阻抗、同步机和线路频变环节共同形成的弱阻尼模态。
- 解释某个振荡模态主要由哪些状态变量、设备或端口参与。
- 选择控制器输入、输出和参数调整方向。
- 为 EMT 详细建模边界选择提供目标模态层面的依据。

例如，[[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]]把 Modelica 线性化得到的 A 矩阵用于 PV 场站控制交互风险筛查；[[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]]则把 Floquet 参与因子用于识别目标振荡模式中应保留为 EMT 详细模型的元件。

## 核心机制

连续时间线性模型

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x}+\mathbf{B}\Delta\mathbf{u},\quad
\Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}+\mathbf{D}\Delta\mathbf{u}
$$

的右、左特征向量满足

$$
\mathbf{A}\mathbf{v}_i=\lambda_i\mathbf{v}_i,\quad
\mathbf{w}_i^H\mathbf{A}=\lambda_i\mathbf{w}_i^H.
$$

若采用双正交归一化 $\mathbf{w}_i^H\mathbf{v}_j=\delta_{ij}$，模态坐标可写为

$$
\mathbf{z}=\mathbf{W}^H\Delta\mathbf{x}.
$$

第 $i$ 个模态的自然响应由 $e^{\lambda_i t}$ 控制。右特征向量 $\mathbf{v}_i$ 给出该模态在状态空间中的形状；左特征向量 $\mathbf{w}_i$ 给出状态扰动投影到该模态的权重。

## 模态解释工具

### 模态形状

模态形状通常来自右特征向量。对同步机转子角或速度状态，幅值和相位可用于识别同调摆动或区域间相对运动。对电力电子控制状态，模态形状可提示 PLL、电流环、电压环、直流母线或网络状态是否共同参与。

模态形状受状态单位、归一化和坐标系影响，不能不加说明地比较不同模型。

### 参与因子

参与因子常写为

$$
p_{ki}=w_{ik}v_{ki},
$$

或使用其绝对值/归一化形式进行排序。它衡量状态 $k$ 与模态 $i$ 的局部关联，而不是能量、因果责任或工程故障根因的直接证明。

对设备级解释时，可把同一设备的相关状态参与因子聚合，但聚合规则必须说明。例如把某台变流器的 PLL、滤波器和电流环状态合并为设备参与度，与只看单个状态变量会得到不同排序。

### 留数与输入输出可控可观性

对传递函数

$$
\mathbf{H}(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D},
$$

第 $i$ 个简单极点的留数可写为

$$
\mathbf{R}_i=\mathbf{C}\mathbf{v}_i\mathbf{w}_i^H\mathbf{B}.
$$

留数把模态、输入和输出联系起来，比单独参与因子更适合讨论控制器输入选择、测量信号和阻尼通道。

### 灵敏度

特征值对参数 $\alpha$ 的局部灵敏度为

$$
\frac{\partial\lambda_i}{\partial\alpha}
=
\mathbf{w}_i^H
\frac{\partial\mathbf{A}}{\partial\alpha}
\mathbf{v}_i.
$$

该公式可用于解释某个参数调整对模态移动的局部方向，但不能替代重新线性化和 EMT 时域验证。

## 变体

| 变体 | 机制 | 适用对象 | 边界 |
|---|---|---|---|
| LTI 模态分析 | 对运行点线性化 A 矩阵求左右特征向量 | 机电振荡、控制交互、状态空间模型 | 仅覆盖运行点附近 |
| 离散模态分析 | 对采样矩阵或状态转移矩阵求模态 | EMT companion circuit、数字控制、周期映射 | 需说明采样周期和连续域映射 |
| Floquet 模态分析 | 对周期轨迹的单周期状态转移矩阵求乘子和向量 | 周期开关 EMT 模型 | 依赖周期稳态和相位参考 |
| 频域模态解释 | 对导纳/阻抗矩阵或闭环增益矩阵分析谱结构 | 黑盒 EMT 模型和 MIMO 阻抗分析 | 不等同于状态矩阵模态 |
| 测量驱动模态辨识 | 从 PMU/EMT 响应估计频率、阻尼和形状 | 事后分析和在线监测 | 受噪声、扰动可观性和窗口长度影响 |

## 适用边界与失败模式

- 把参与因子最大者写成“振荡源”，但没有控制实验、扰动注入或因果验证。
- 忽略变量尺度，直接比较电压、电流、控制器积分状态和机械状态的参与因子。
- 只看右特征向量，不检查左特征向量、留数或输入输出通道。
- 对重特征值、近重特征值或病态特征向量做过度物理解释。
- 将周期系统的 Floquet 参与因子与 LTI 参与因子混用。
- 在限幅和保护逻辑参与的工况下，把线性模态解释扩展到大扰动全过程。

## 代表性来源

| 来源 | 模态分析作用 | 可采信边界 |
|---|---|---|
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 用 Floquet 参与因子识别目标模态相关元件并服务 EMT 边界划分 | 支撑周期稳态附近目标模态；阈值和量化结果需回到原文 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 从 EMT companion-circuit 状态转移矩阵进入特征值和模态分析 | 支撑文中 PE 电路场景；不同 EMT 数值算法需另行验证 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | 用特征值和模态信息定位 PV 场站控制交互风险 | 支撑所述 Modelica/MSEMT 工作流；不覆盖所有控制策略 |
| [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti]] | 作为大系统模态筛查和降阶相关来源入口 | 具体算法收益和误差需从来源页和原文核验 |

## 与相关页面的关系

- [[eigenvalue-analysis]]：提供模态分析的谱计算基础。
- [[modal-decomposition]]：把模态分析结果用于响应叠加和时域解释。
- [[small-signal-stability-analysis]]：把模态分析放入运行点线性化和验证流程。
- [[generalized-eigenvalue-method]]：处理矩阵束和 DAE 场景下的模态问题。
- [[power-system-stabilizer]]：模态、留数和灵敏度可用于 PSS 参数整定，但必须经多工况验证。
