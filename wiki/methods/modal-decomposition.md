---
title: "模态分解 (Modal Decomposition)"
type: method
tags: [modal, decomposition, eigenvalue, oscillation, mode-shape, participation-factor, coherency]
created: "2026-05-02"
---

# 模态分解 (Modal Decomposition)

## 定义与边界

模态分解是把线性系统的状态或输出响应表示为多个模态响应叠加的过程。它回答“某段响应可由哪些指数衰减、增长或振荡分量组成”。它依赖[[eigenvalue-analysis]]和[[modal-analysis]]，但重点是响应展开，而不是稳定性概念或参与因子排序本身。

本页讨论状态空间和 EMT 小扰动响应中的模态分解。它不等同于[[modal-domain-decoupling]]的线路相域/模域坐标变换，也不应被写成任意非线性 EMT 波形都可精确拆成固定模态。

## EMT 中的作用

在 EMT 研究中，模态分解可用于：

- 将小扰动响应拆成若干频率和阻尼分量，辅助解释振荡来源。
- 将特征值分析结果与 EMT 时域波形对齐。
- 识别某个输出中哪些模态被扰动或测量通道激发。
- 在周期稳态或采样系统中比较离散模态与连续频率解释。

若响应来自大扰动、保护切换或非线性限幅，模态分解只能作为局部或辨识近似，不能自动代表系统全过程。

## 核心机制

对自由响应

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x},
$$

若 $\mathbf{A}$ 可对角化，设 $\mathbf{A}\mathbf{v}_i=\lambda_i\mathbf{v}_i$，则

$$
\Delta\mathbf{x}(t)=\sum_i c_i\mathbf{v}_i e^{\lambda_i t},
$$

其中系数 $c_i$ 由初始扰动在左特征向量上的投影决定：

$$
c_i=\mathbf{w}_i^H\Delta\mathbf{x}(0).
$$

对输出 $\Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}$，输出模态分量为

$$
\Delta\mathbf{y}(t)=\sum_i c_i\mathbf{C}\mathbf{v}_i e^{\lambda_i t}.
$$

因此同一个系统模态是否能在某个测量量中看到，取决于初始扰动、输出矩阵和模态形状，而不仅取决于特征值是否存在。

## 与强迫响应和留数的关系

若有输入 $\Delta\mathbf{u}$，传递函数

$$
\mathbf{H}(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}
$$

在简单极点 $\lambda_i$ 附近可展开为

$$
\mathbf{H}(s)\approx \frac{\mathbf{R}_i}{s-\lambda_i}+\cdots,
$$

其中

$$
\mathbf{R}_i=\mathbf{C}\mathbf{v}_i\mathbf{w}_i^H\mathbf{B}.
$$

留数说明输入和输出通道对该模态的耦合强弱。它常比只看状态参与因子更适合解释某个 EMT 扰动波形中为何出现或不出现某个模态。

## 数据驱动分解

当没有显式状态矩阵时，可从波形估计模态参数，例如将单个输出近似为

$$
y(t)\approx \sum_{i=1}^{m} a_i e^{\sigma_i t}\cos(\omega_i t+\phi_i).
$$

这种辨识式模态分解可用于 EMT 小扰动响应、PMU 波形或仿真事后分析。它的可信度取决于采样率、窗口长度、噪声、扰动是否充分激发目标模态，以及模态是否在窗口内近似线性时不变。

## 变体

| 变体 | 输入 | 输出 | 适用边界 |
|---|---|---|---|
| 特征向量模态分解 | 状态矩阵、初始扰动 | 状态响应的模态叠加 | 需要线性模型和可解释状态 |
| 输出模态分解 | 状态矩阵、输出矩阵、扰动 | 测量量中的模态贡献 | 受可观性和输出选择影响 |
| 留数分解 | 输入输出传递函数 | 模态在通道中的极点/留数 | 适合控制信号和测量通道分析 |
| 时域辨识分解 | 波形数据 | 估计频率、阻尼、幅值、相位 | 受噪声、窗口和非线性影响 |
| Floquet 模态分解 | 周期状态转移矩阵 | 周期系统的跨周期模态分量 | 依赖周期稳态参考和采样映射 |

## 适用边界与失败模式

- 短窗口波形中存在多个接近频率模态时，分解结果可能不唯一。
- 大扰动后的限幅、保护切换和拓扑变化会改变模型，固定模态叠加不再成立。
- 初始扰动没有激发某个模态时，该模态可能在波形中不可见。
- 输出通道不可观时，即使状态中存在模态，测量波形也可能看不到。
- 重特征值或不可对角化矩阵需要 Jordan 或子空间解释，不能简单写成独立一阶模态。
- 数据驱动分解得到的频率和阻尼需要与状态空间、阻抗扫描或 EMT 重复扰动交叉验证。

## 代表性证据

| 来源 | 对模态分解的支撑 | 可采信边界 |
|---|---|---|
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 状态转移矩阵特征值可解释 EMT companion-circuit 模态响应 | 支撑文中周期/采样数据框架；数值伪模态需识别 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | Floquet 模态和参与因子可用于解释周期 EMT 模型目标动态 | 支撑目标模态边界选择；不覆盖非周期大扰动 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] | EMT 扰动响应可经 FFT 转为频域矩阵，用于小信号模态或交互解释 | 支撑频域响应识别；不是状态空间分解的直接替代 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | Modelica 线性化后的 A 矩阵提供可分解的模态响应基础 | 支撑所述 PV 场站模型；结论受运行点约束 |

## 与相关页面的关系

- [[modal-analysis]]：解释模态形状、参与因子和灵敏度。
- [[eigenvalue-analysis]]：提供模态分解所需的特征值和特征向量。
- [[small-signal-stability-analysis]]：把模态分解用于稳定性分析验证。
- [[generalized-eigenvalue-method]]：处理矩阵束下的模态展开问题。
- [[frequency-scan]]和[[impedance-measurement]]：提供无显式状态矩阵时的频域响应证据。
