---
title: "状态空间法"
type: method
tags: [state-space, emt, model-reduction, matrix-exponential, descriptor-system]
created: "2026-04-13"
---

# 状态空间法

## 定义与边界

状态空间法（State-Space Method）以状态向量 $\mathbf{x}$ 的一阶微分或差分方程描述电气、控制和接口动态，典型形式为 $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$，$\mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}$。在 EMT 语境中，状态通常来自电感电流、电容电压、控制器积分量、线路递推量或拟合模型内部状态。

它不是 [[nodal-analysis]] 的替代总框架。节点分析以网络节点电压为未知量，适合大规模稀疏网络；状态空间法更适合内部动态强、端口数有限、需要控制/模态/降阶解释的子系统。工程实现中常把设备内部写成状态空间，外部仍接入节点导纳方程。

## EMT 中的作用

状态空间法在 EMT 中有三类作用：一是把变流器、控制器和机器模型组织成可离散推进的状态方程；二是把 [[vector-fitting]]、[[prony-analysis]] 或 [[fdne-model]] 生成的极点-留数模型转成时域递推；三是支撑 [[model-order-reduction]]、[[small-signal-analysis]] 和实时仿真中的模型压缩。

它特别适合描述“输入、输出、内部状态和端口变量之间的关系”。若研究重点是含大量开关事件的全网络拓扑重构，则直接状态矩阵重建可能比伴随电路和节点法更重。

## 核心机制

连续线性系统可写为 $\dot{\mathbf{x}}(t)=\mathbf{A}\mathbf{x}(t)+\mathbf{B}\mathbf{u}(t)$，$\mathbf{y}(t)=\mathbf{C}\mathbf{x}(t)+\mathbf{D}\mathbf{u}(t)$。其中 $\mathbf{x}$ 是状态，$\mathbf{u}$ 是端口电压、控制指令或注入量，$\mathbf{y}$ 是端口电流或观测量。

离散 EMT 步进需要把连续模型变成 $\mathbf{x}_{n+1}=\mathbf{\Phi}\mathbf{x}_n+\mathbf{\Gamma}\mathbf{u}_n$ 或含 $\mathbf{u}_{n+1}$ 的隐式形式。$\mathbf{\Phi}$ 可来自矩阵指数、[[trapezoidal-rule]]、[[backward-euler]] 或其他 [[numerical-integration]]。刚性系统、病态矩阵和事件时刻插值都会影响稳定性。

对含代数约束的系统，可写成描述符形式 $\mathbf{E}\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$。这对电感割集、电容回路和端口约束有用，但接入 EMT 求解器前要检查指数、可解性和离散化后的代数一致性。

## 分类与变体

| 形式 | 主要用途 | 适用边界 |
|------|----------|----------|
| 直接状态空间 | 小规模电路、控制器、设备内部模型 | 开关拓扑频繁变化时矩阵更新成本高 |
| 描述符状态空间 | 含代数约束的电路或多端口模型 | 需处理奇异 $\mathbf{E}$ 和一致初值 |
| 状态空间-节点混合 | 设备内部状态接入外部节点网络 | 端口变量方向、历史项和迭代顺序必须一致 |
| 分段/广义状态空间平均 | 变流器开关周期平均、低频动态 | 不保留完整开关纹波 |
| 极点-留数状态实现 | FDNE、线路/电缆宽频模型 | 需无源性和稳定性检查 |

## 适用边界与失败模式

- 大规模稀疏网络：若系统主要是线性 RLC 网络，[[nodal-analysis]] 和稀疏矩阵求解通常更直接。
- 频繁开关：每个开关状态对应不同 $\mathbf{A}$ 或端口矩阵时，预计算、分组或混合法不可少。
- 非线性：状态空间表达非线性并不困难，但线性矩阵形式和模态解释只对工作点或分段范围成立。
- 数值稳定：矩阵指数、Padé/Krylov 近似和隐式积分的误差不能只用“精确”概括，应按步长、矩阵谱和实现说明。
- 降阶风险：降阶后状态不一定保留原始物理含义；电容电压、能量和保护相关峰值需要单独验证。

## 代表性来源

| 来源 | 支撑内容 | 证据边界 |
|------|----------|----------|
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] | 比较伴随电路与描述符状态空间的 EMT 表达 | 适合作为建模形式对比，不是所有网络的性能结论 |
| [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti]] | 分段广义状态空间用于变流器 EMT 模型 | 适用对象限于原文变流器算例 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete]] | 频变线路参数可通过状态空间时域实现 | 频率范围和线路参数需按原文设置 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte]] | MMC 加速仿真中的状态空间建模 | 加速量不得外推到任意 MMC 拓扑 |
| [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati]] | 变流器集成系统的分裂状态空间求解 | 需要核查分裂误差和接口稳定性 |

## 与相关页面的关系

- [[nodal-analysis]]：节点分析负责全局网络代数方程；状态空间法负责内部动态或端口等效。
- [[companion-circuit]]：伴随电路把动态元件离散成等效导纳和历史源；状态空间法保留显式状态递推。
- [[vector-fitting]]：矢量拟合输出的极点-留数模型通常转成状态空间接入 EMT。
- [[model-order-reduction]]：许多降阶算法以状态空间模型为输入，但降阶误差需通过频域和时域双重检查。
- [[small-signal-analysis]]：小信号分析依赖线性化状态矩阵，但不能直接代表大扰动 EMT 行为。
