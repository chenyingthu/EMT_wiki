---
title: "小信号稳定性 (Small-Signal Stability)"
type: method
tags: [small-signal, stability, oscillation, eigenvalue, damping, power-system]
created: "2026-05-02"
---

# 小信号稳定性 (Small-Signal Stability)

## 定义与边界

小信号稳定性指系统在某个运行点附近受到小扰动后，扰动量是否衰减、保持有界或增长。这里的“小”不是固定幅值，而是指扰动足够接近线性化点，使一阶模型能够代表局部动态。

本页讨论稳定性概念本身：它回答“这个运行点附近的微小扰动是否会衰减”。它不等同于[[small-signal-stability-analysis]]的建模流程，也不等同于[[eigenvalue-analysis]]或[[modal-analysis]]的计算操作。若扰动触发限幅、保护动作、控制模式切换、拓扑改变或强非线性暂态，应回到 EMT 时域仿真和场景验证，不能只凭小信号结论外推。

## EMT 中的作用

在 EMT 研究中，小信号稳定性常用于解释运行点附近的振荡、负阻尼和控制相互作用。与传统机电暂态小信号分析相比，EMT 模型可能包含开关、采样控制、PLL、多环控制、线路频变特性和电力电子装置的宽频动态。因此 EMT 语境下的小信号稳定性需要明确模型来源：

- 从 EMT 伴随电路和离散状态转移矩阵提取的采样数据模型。
- 从 Modelica 或其他方程建模环境提取的 DAE 线性化模型。
- 从周期稳态轨迹提取的 Floquet 或状态转移矩阵模型。
- 从 EMT 扫频得到的导纳/阻抗矩阵，再用频域稳定判据分析。

这些路线都可以支撑小信号稳定判断，但它们的状态、特征值位置、频率解释和验证边界并不相同。

## 核心机制

若非线性系统在运行点 $(\mathbf{x}_0,\mathbf{u}_0)$ 附近可线性化，可写为

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x}+\mathbf{B}\Delta\mathbf{u}, \quad
\Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}+\mathbf{D}\Delta\mathbf{u}.
$$

当只看自由响应时，稳定性由状态矩阵 $\mathbf{A}$ 的特征值决定：

$$
\mathbf{A}\mathbf{v}_i=\lambda_i\mathbf{v}_i,\quad \lambda_i=\sigma_i+j\omega_i.
$$

在连续时间 LTI 模型中，若所有相关特征值满足 $\sigma_i<0$，对应模态局部衰减；若存在 $\sigma_i>0$，该线性化模型显示扰动会增长。复特征值的虚部可换算为振荡频率：

$$
f_i=\frac{|\omega_i|}{2\pi}.
$$

阻尼比常写为

$$
\zeta_i=-\frac{\sigma_i}{\sqrt{\sigma_i^2+\omega_i^2}}.
$$

这些公式给出局部数学判据，不自动给出工程合格阈值。任何阻尼比门槛、频率范围或风险等级都应绑定标准、调度规程、论文算例或项目要求。

## 类型与对象

| 对象 | 小信号稳定性问题 | EMT 关注点 |
|---|---|---|
| 同步机与励磁/PSS | 机电振荡是否有足够阻尼 | [[swing-equation]]、[[excitation-system]]和[[power-system-stabilizer]]的参数共同影响模态 |
| 电力电子并网装置 | PLL、电流环、电压环和网络阻抗是否形成负阻尼 | 状态空间、阻抗扫描和 EMT 时域扰动需要交叉解释 |
| 周期开关系统 | 周期稳态附近扰动是否跨周期衰减 | 状态转移矩阵或 Floquet 乘子比单一连续 A 矩阵更贴近问题 |
| 线路和频变网络 | 频变传播、端口导纳和控制器是否耦合出弱阻尼模式 | 与[[frequency-scan]]、[[impedance-measurement]]和[[frequency-dependent-line-model]]相关 |

## 适用边界与失败模式

小信号稳定性适合解释运行点附近的微小扰动，不适合替代大扰动 EMT 验证。常见失败模式包括：

- 线性化点未说明，导致特征值无法复现。
- 将单个运行方式下的弱阻尼模态外推到所有负荷、拓扑和控制参数。
- 忽略状态缩放、代数变量消元或离散化映射，误把数值模态当作物理模态。
- 把频域导纳矩阵的稳定判断与连续时间状态矩阵特征值混写。
- 在存在限幅、饱和、保护闭锁、故障穿越或开关事件时仍使用局部小信号结论解释大扰动。
- 用固定频率范围或阻尼比阈值替代来源明确的工程准则。

## 代表性证据

| 来源 | 对小信号稳定性的支撑 | 证据边界 |
|---|---|---|
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 说明可复用 EMT 伴随电路、历史项和状态转移矩阵构造电力电子系统的小信号模型 | 支撑 buck 变换器和并网 STATCOM 等文中算例；不证明所有 EMT 平台或拓扑均适用 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | 说明 Modelica DAE 线性化和特征值扫描可用于 PV 场站控制交互风险筛查 | 结论受 PV 场站模型、运行点和交叉验证场景约束 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 说明周期稳态 EMT 模型可用 Floquet 乘子和参与因子分析目标振荡模式 | 适用于文中关注的周期轨迹和目标模态，不覆盖非周期强暂态 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] | 说明可从 EMT 时域扰动识别频域导纳矩阵并服务小信号稳定研究 | 频域识别误差依赖步长、扰动幅值和频段设置 |

## 与相关页面的关系

- [[small-signal-stability-analysis]]：把本页概念转化为建模、线性化、求解和验证流程。
- [[eigenvalue-analysis]]：提供判断局部模态增长/衰减的数学操作。
- [[modal-analysis]]：解释特征向量、参与因子和模态形状。
- [[modal-decomposition]]：说明线性响应如何展开为多个模态的叠加。
- [[generalized-eigenvalue-method]]：处理矩阵束、DAE 或导纳矩阵中的广义特征值问题。
- [[transient-stability]]：面向大扰动后同步保持问题，不能与小信号稳定性互相替代。
