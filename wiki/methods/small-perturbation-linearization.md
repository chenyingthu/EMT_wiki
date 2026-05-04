---
title: "小扰动线性化 (Small-Perturbation Linearization)"
type: method
tags: [linearization, small-signal, perturbation, jacobian, stability, eigenvalue]
created: "2026-05-02"
---

# 小扰动线性化 (Small-Perturbation Linearization)

## 定义与边界

小扰动线性化是在给定运行点附近对非线性微分方程、代数方程或离散步进映射做一阶近似的方法。它把“运行点附近的增量响应”写成线性模型，便于使用[[eigenvalue-analysis]]、[[modal-analysis]]、[[frequency-scan]]和控制设计工具。

本页讨论方法本身：如何选运行点、如何构造雅可比、如何解释线性模型。它不等同于[[small-signal-stability]]概念页，也不保证故障、限幅、保护切换或大信号暂态中的非线性行为。

## EMT 中的作用

EMT 模型通常包含电感电容状态、节点电压、开关逻辑、控制器积分器、PLL、采样延时和频率相关网络。小扰动线性化可用于：

- 从详细 EMT 模型提取局部状态空间模型。
- 解释换流器控制、弱网、频变网络和机电模式之间的局部耦合。
- 为[[small-signal-stability-analysis]]提供运行点相关的矩阵。
- 用小幅 EMT 扰动响应核对线性模型的频率、阻尼和输入输出通道。

若 EMT 对象是周期切换系统，线性化对象可能不是单个连续时间矩阵，而是一个周期轨迹附近的离散状态转移矩阵。

## 核心形式

对连续时间非线性系统

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u}),\quad
\mathbf{y}=\mathbf{g}(\mathbf{x},\mathbf{u}),
$$

在运行点 $(\mathbf{x}_0,\mathbf{u}_0)$ 附近令 $\Delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$，$\Delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$。若 $\mathbf{f}$ 和 $\mathbf{g}$ 在该点可微，一阶近似为

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x}+\mathbf{B}\Delta\mathbf{u},
\quad
\Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}+\mathbf{D}\Delta\mathbf{u},
$$

其中

$$
\mathbf{A}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_0,\quad
\mathbf{B}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{u}}\right|_0,\quad
\mathbf{C}=\left.\frac{\partial\mathbf{g}}{\partial\mathbf{x}}\right|_0,\quad
\mathbf{D}=\left.\frac{\partial\mathbf{g}}{\partial\mathbf{u}}\right|_0.
$$

对 DAE

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{z},\mathbf{u}),\quad
\mathbf{0}=\mathbf{h}(\mathbf{x},\mathbf{z},\mathbf{u}),
$$

若 $\mathbf{h}_z$ 非奇异，可局部消去代数变量：

$$
\Delta\dot{\mathbf{x}}=
\left(\mathbf{f}_x-\mathbf{f}_z\mathbf{h}_z^{-1}\mathbf{h}_x\right)\Delta\mathbf{x}
+
\left(\mathbf{f}_u-\mathbf{f}_z\mathbf{h}_z^{-1}\mathbf{h}_u\right)\Delta\mathbf{u}.
$$

对离散 EMT 步进器，则常写为

$$
\Delta\mathbf{x}_{k+1}=\mathbf{A}_d\Delta\mathbf{x}_k+\mathbf{B}_d\Delta\mathbf{u}_k.
$$

连续时间特征值与离散时间特征值不能混用；解释时必须说明模型域和采样步长。

## 工作流

1. 固定运行点：记录拓扑、控制模式、潮流或周期稳态、步长、坐标系和初值来源。
2. 定义状态和输入：区分物理状态、控制状态、代数变量和数值历史项。
3. 计算雅可比：优先使用解析求导、自动微分或模型导出的雅可比；黑盒 EMT 可用小扰动差分或频域识别。
4. 形成线性模型：处理 DAE 消元、离散化、周期映射或输入输出选择。
5. 验证残差：检查 $\|\mathbf{A}\mathbf{v}-\lambda\mathbf{v}\|$、小扰动时域响应和频域响应。
6. 报告边界：绑定运行点、扰动幅值、模型阶次、状态定义和验证方式。

## 变体

| 变体 | 机制 | 适用场景 | 注意事项 |
|---|---|---|---|
| 解析线性化 | 对模型方程显式求导 | 白盒控制器、机器模型、网络方程 | 容易受坐标和符号约定影响 |
| 数值差分线性化 | 对状态或输入施加小扰动并差分 | 黑盒 EMT 模型、软件模型 | 步长太小受舍入影响，太大受非线性影响 |
| DAE 线性化 | 同时线性化微分和代数约束 | 节点网络、伴随模型、控制网络耦合 | 代数雅可比奇异时解释失效 |
| 离散线性化 | 线性化一步或多步映射 | 固定步长 EMT、采样控制 | 特征值依赖步长和事件处理 |
| Floquet 线性化 | 围绕周期轨迹构造单周期转移矩阵 | 周期开关系统 | 需可靠的周期稳态轨迹 |

## 适用边界与失败模式

- 运行点未收敛或初始化不一致时，线性化矩阵会描述启动伪暂态而非目标系统。
- 限幅、死区、保护动作、换相失败、拓扑切换和饱和会破坏单一光滑雅可比假设。
- 在强不平衡或谐波稳态下，正序相量模型的线性化不能替代 EMT 相域或周期模型。
- 数值差分会受扰动幅值、仿真步长、插值和噪声影响。
- 固定阻尼比阈值或频率分类若未绑定标准、工程规则或来源，不应写成通用判据。

## 代表性证据

- [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] 支撑从 EMT 伴随电路或状态转移结构提取小信号模型的路线；其结论应限于文中算例和建模假设。
- [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t]] 展示动态相量和小信号模型在换流器分析中的用途；不能据此替代全 EMT 开关验证。
- [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] 支撑用 EMT 扰动识别频域特性的流程；精度依赖扰动、窗口和频段设置。

这些来源提供方法样例，不构成“线性化对所有 EMT 模型可靠”的领域性证明。

## 与相关页面的关系

- [[small-signal-stability-analysis]]：使用线性化模型开展稳定分析。
- [[eigenvalue-analysis]]：解释线性矩阵谱和稳定趋势。
- [[modal-analysis]]：解释模态形状、参与因子和留数。
- [[generalized-eigenvalue-method]]：处理矩阵束和 DAE 谱问题。
- [[dae-solvers]]：提供微分-代数方程求解背景。
- [[steady-state-initialization]]：提供可信运行点来源。
