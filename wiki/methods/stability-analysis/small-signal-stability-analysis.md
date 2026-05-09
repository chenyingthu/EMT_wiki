---
title: "小信号稳定性分析 (Small-signal Stability Analysis)"
type: method
tags: [small-signal-stability, eigenvalue-analysis, oscillation-mode, damping, power-system]
created: "2026-05-02"
---

# 小信号稳定性分析 (Small-signal Stability Analysis)


```mermaid
graph TD
    subgraph Ncmp[小信号稳定性分析 (Small-signal Stabi…]
        N0[输入运行点: 潮流、周期稳态、扰动前后准稳态或 EMT 快照]
        N1[输入模型: DAE、离散采样模型、状态转移矩阵、阻抗/导…]
        N2[输出指标: 特征值、阻尼趋势、频率、参与因子、模态形状、…]
        N3[验证方式: EMT 小扰动响应、频扫、阻抗扫描、残差检查]
    end
```


## 定义与边界

小信号稳定性分析是围绕某个运行点构造线性小扰动模型，并用[[eigenvalue-analysis]]、[[modal-analysis]]、频域矩阵判据或 EMT 扰动响应验证局部稳定性的流程。它服务于[[small-signal-stability]]这一稳定性概念，但不是概念本身。

本页关注“如何分析”：输入是什么、如何线性化、怎样解释结果、何时需要 EMT 时域交叉验证。它不承诺固定阻尼阈值、固定振荡频段或某个软件流程的普遍适用性。

## EMT 中的作用

EMT 小信号稳定性分析常用于以下问题：

- 对电力电子化系统的控制相互作用进行运行点筛查。
- 从 EMT 详细模型中提取可用于模态解释的线性模型。
- 将阻抗扫描、频率响应和状态空间特征值联系起来。
- 在大扰动 EMT 仿真前识别可能的弱阻尼或负阻尼工况。

与只用相量域模型的分析不同，EMT 线性化可能保留控制采样、开关事件、伴随电路历史项、频变线路、dq/abc 坐标变换和端口导纳矩阵。分析报告必须说明这些细节，否则特征值和参与因子没有清晰物理边界。

## 典型输入与输出

| 项目 | 内容 | 边界 |
|---|---|---|
| 输入运行点 | 潮流、周期稳态、扰动前后准稳态或 EMT 快照 | 运行点改变后特征值可能改变 |
| 输入模型 | DAE、离散采样模型、状态转移矩阵、阻抗/导纳矩阵 | 不同模型的特征值含义不同 |
| 输出指标 | 特征值、阻尼趋势、频率、参与因子、模态形状、频域裕度 | 指标需绑定模型和验证方式 |
| 验证方式 | EMT 小扰动响应、频扫、阻抗扫描、残差检查 | 验证不等同于大扰动稳定保证 |

## 核心流程

### 1. 确定运行点

分析应先给出运行方式、控制参数、拓扑、负荷/出力、控制模式和是否处于周期稳态。若系统处于开关周期稳态，单个连续时间 A 矩阵可能不足，应考虑周期状态转移矩阵或 Floquet 框架。

### 2. 建立线性化模型

连续时间 DAE 可写为

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},\mathbf{u}),\quad
\mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},\mathbf{u}).
$$

若 $\partial\mathbf{g}/\partial\mathbf{y}$ 在运行点附近可逆，可消去代数变量，得到

$$
\Delta\dot{\mathbf{x}}=
\left(
\mathbf{f}_x-\mathbf{f}_y\mathbf{g}_y^{-1}\mathbf{g}_x
\right)\Delta\mathbf{x}
+
\left(
\mathbf{f}_u-\mathbf{f}_y\mathbf{g}_y^{-1}\mathbf{g}_u
\right)\Delta\mathbf{u}.
$$

对于 EMT companion-circuit 路线，状态也可以取电感、电容或历史项电流源，形成离散模型

$$
\Delta\mathbf{x}_{k+1}=\mathbf{A}_d\Delta\mathbf{x}_k+\mathbf{B}_d\Delta\mathbf{u}_k.
$$

周期系统则常将一个周期内的步进矩阵连乘为状态转移矩阵 $\mathbf{\Phi}(T)$，再分析其特征值或 Floquet 指数。

### 3. 求解和解释模态

连续时间模型通常分析 $\mathbf{A}$ 的特征值；离散模型通常分析 $\mathbf{A}_d$ 或 $\mathbf{\Phi}(T)$ 的特征值；频域 EMT 识别则可能分析闭环增益、阻抗比或导纳矩阵的频率轨迹。

解释时应分开：

- 特征值实部或离散特征值模值：局部增长/衰减趋势。
- 虚部或角度：振荡频率解释。
- 右特征向量：模态形状和相位关系。
- 左特征向量与参与因子：状态或元件对模态的局部关联。
- 留数或输入输出灵敏度：控制信号和测量信号是否能有效作用于该模态。

### 4. 用 EMT 响应交叉验证

小信号分析应至少用一种独立检查支撑解释，例如：

- 对状态矩阵残差做 $\|\mathbf{A}\mathbf{v}-\lambda\mathbf{v}\|$ 检查。
- 在 EMT 中施加小扰动，比较频率和衰减趋势。
- 用[[frequency-scan]]或[[impedance-measurement]]核对频域交互。
- 在多个运行点复算，检查关键模态是否随控制参数或网络强度移动。

## 变体

| 变体 | 机制 | 适用场景 | 注意事项 |
|---|---|---|---|
| DAE 线性化 | 对方程和代数约束做雅可比线性化 | 同步机、换流器、网络混合模型 | 代数消元可能病态 |
| EMT 伴随电路线性化 | 复用节点导纳、LU 因子、历史源和开关处理 | 电力电子开关或采样数据模型 | 需区分物理模态和数值模态 |
| Floquet 分析 | 对周期轨迹构造单周期状态转移矩阵 | 周期开关、周期稳态 EMT 模型 | 结果依赖周期轨迹和采样窗口 |
| 频域 EMT 表征 | 注入小扰动并识别导纳/阻抗矩阵 | 黑盒 EMT 模型和多端口装置 | 扰动幅值、FFT 窗和步长会影响结果 |
| 参数扫描 | 在多个运行点或控制参数下复算模态 | 风险筛查和控制整定 | 只能覆盖扫描集合 |

## 适用边界与失败模式

- 把[[small-signal-stability]]概念页写成软件功能清单。
- 用未绑定来源的阻尼比门槛或频率分类作为无边界判据。
- 只报告“稳定/不稳定”，不说明运行点、模型阶次、坐标系和状态选择。
- 忽略 EMT 离散化产生的伪特征值或步长依赖误差。
- 将局部线性结果用于故障穿越、保护切换或限幅后的非线性过程。
- 用单篇论文算例的结果支撑一般工程结论。

## 代表性来源

| 来源 | 支撑的分析路线 | 可采信边界 |
|---|---|---|
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 从 EMT companion circuit 和状态转移矩阵自动构建电力电子小信号模型 | 支撑文中典型 PE 电路和 STATCOM 场景；不提供全网普遍结论 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | 用 Modelica 展平 DAE 并在线性化点提取 A/B/C/D 矩阵 | 支撑 PV 场站控制交互筛查流程；大扰动仍需 EMT 验证 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] | 用 EMT 扰动和 FFT 识别多端导纳矩阵以服务小信号稳定判断 | 支撑频域识别流程；精度依赖扰动、步长和频段 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 用 Floquet 参与因子识别目标振荡模态和 EMT 边界 | 支撑周期稳态附近目标模态，不覆盖非周期故障暂态 |

## 与相关页面的关系

- [[small-signal-stability]]：定义局部稳定性概念。
- [[eigenvalue-analysis]]：提供特征值求解和稳定性解释。
- [[modal-analysis]]：解释模态、参与因子和灵敏度。
- [[modal-decomposition]]：解释时域响应如何由多个模态叠加。
- [[generalized-eigenvalue-method]]：处理 DAE、矩阵束和广义谱问题。
- [[dae-solvers]]：说明线性化前的 DAE 建模和求解背景。
