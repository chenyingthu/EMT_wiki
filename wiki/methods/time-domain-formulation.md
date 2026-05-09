---
title: "时域公式化 (Time-Domain Formulation)"
type: method
tags: [time-domain, formulation, state-space, differential-equations, emt-simulation]
created: "2026-05-02"
---

# 时域公式化 (Time-Domain Formulation)


```mermaid
graph TD
    subgraph Ncmp[时域公式化 (Time-Domain Formulati…]
        N0[伴随电路/节点导纳: 节点电压、支路历史源]
        N1[状态空间公式化: 状态向量和输入输出矩阵]
        N2[完全隐式 DAE: 状态、代数变量和残差]
        N3[端口等效公式化: 端口电压电流、等效导纳/源]
        N4[时延/卷积公式化: 端口历史量、卷积状态]
    end
```


## 定义与边界

时域公式化（Time-Domain Formulation）是把 EMT 研究对象写成随时间推进的电压、电流、磁链、机械量、控制状态和离散事件方程。它回答的是“连续物理和控制逻辑如何变成可逐步求解的方程”，不是某一种积分公式、某个软件流程或某篇论文模型的同义词。

典型连续形式可写为

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},\mathbf{u},t), \quad
\mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},\mathbf{u},t),
$$

其中 $\mathbf{x}$ 为动态状态，$\mathbf{y}$ 为代数变量，$\mathbf{u}$ 为输入或离散控制量。对线路、机器、换流器和保护闭环等对象，方程还可能包含时延、分段逻辑、查表非线性、饱和和拓扑切换。

本页讨论 EMT 方程组织方式，不把“时域”写成天然高精度或天然实时。精度和可信度取决于模型频带、步长、积分方法、事件处理、初值一致性和验证参考。

## EMT 中的作用

EMT 仿真直接计算瞬时值，因此适合研究开关暂态、行波、换流器控制、保护动作、故障注入和非线性元件。时域公式化承担三个接口任务：

- 把元件物理关系转成状态方程、代数约束或端口等效。
- 把网络连接写成 KCL/KVL 或节点导纳方程。
- 把开关、限幅、保护和控制采样转成离散事件或分段方程。

在 EMTP 类流程中，动态元件常经 [[companion-circuit]] 离散为等效导纳和历史源，再进入 [[nodal-analysis]] 或 [[nodal-admittance-matrix]]。在方程导向建模中，元件也可以保持 ODE/DAE 表达，由工具链进行方程排序、撕裂和数值求解。两者都是时域公式化的实现路线，差别在于方程何时、由谁、以何种数值结构离散。

## 核心机制

### 元件方程

基本储能元件给出最小的时域关系：

$$
v_L(t)=L\frac{di_L(t)}{dt}, \quad
i_C(t)=C\frac{dv_C(t)}{dt}, \quad
i_R(t)=Gv_R(t).
$$

这些方程本身不是完整 EMT 网络。只有与端口方向、节点连接、初始状态和数值积分规则结合后，才能形成每个时间步可求解的网络方程。

### 网络方程

以节点电压为未知量时，离散后的线性网络常写成

$$
\mathbf{Y}_{n+1}\mathbf{v}_{n+1}
=\mathbf{i}_{src,n+1}+\mathbf{i}_{hist,n+1}.
$$

$\mathbf{Y}_{n+1}$ 来自电阻、伴随电导、开关状态和网络拓扑；$\mathbf{i}_{hist,n+1}$ 来自电感、电容、线路时延、递归卷积或动态等值的历史项。若存在非线性元件或隐式控制约束，上式会成为 [[dae-solvers]] 中的残差方程。

### 离散化

以一般状态方程 $\dot{x}=f(x,t)$ 为例，常见隐式公式包括

$$
x_{n+1}=x_n+\frac{\Delta t}{2}\left[f(x_n,t_n)+f(x_{n+1},t_{n+1})\right]
$$

和

$$
x_{n+1}=x_n+\Delta t f(x_{n+1},t_{n+1}).
$$

前者对应 [[trapezoidal-rule]]，后者对应 [[backward-euler]]。梯形积分常用于保持二阶精度，但在不连续点可能产生持续的高频数值振荡；后向欧拉具有更强数值阻尼，但一阶耗散更明显。选用何种公式应绑定模型目标和验证结果，而不是按“更稳定”或“更精确”单独决定。

## 分类与变体

| 公式化路线 | 主要未知量 | EMT 用途 | 边界 |
|---|---|---|---|
| 伴随电路/节点导纳 | 节点电压、支路历史源 | 传统固定步长 EMT、实时仿真、线路和 RLC 网络 | 历史项和事件重初始化必须正确 |
| 状态空间公式化 | 状态向量和输入输出矩阵 | 控制、线性开关电路、模态分析、局部模型验证 | 强拓扑切换和非线性约束会复杂化 |
| 完全隐式 DAE | 状态、代数变量和残差 | 方程导向建模、机网联立、混合仿真接口 | 初值一致性和雅可比病态是主要风险 |
| 端口等效公式化 | 端口电压电流、等效导纳/源 | 电机、MMC、FDNE、外部网络等值 | 端口等效不能自动保留所有内部状态 |
| 时延/卷积公式化 | 端口历史量、卷积状态 | 分布参数线路、频率相关模型 | 拟合质量、无源性和步长变化需验证 |

## 适用边界与失败模式

- 时域公式化可保留瞬时暂态，但不保证所有高频物理过程都被解析；模型频带和步长仍是上限。
- 理想开关、阶跃源和分段非线性会破坏连续性，若事件定位或历史项重置不一致，会产生虚假能量和数值振荡。
- 固定步长有利于实时同步和矩阵复用，但会把事件限制到网格或插值策略中。
- 变步长 DAE 有利于离线精度控制，但对递归卷积、时延线路和离散控制同步提出额外要求。
- 端口等效和恒导纳技术可降低主网络规模，但必须说明被消去内部状态如何恢复、哪些动态被近似。

## 代表性证据

| 来源 | 支持的认识 | 证据边界 |
|---|---|---|
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat]] | VBR 机器模型把内部电磁状态整理为端口等效导纳和历史源，便于接入 EMT 网络 | 支持机器-网络接口机制；不能外推为所有电机模型都无需迭代 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-]] | Modelica 异步机以连续 DAE/ODE 层面保留磁链状态，由求解器处理步长和方程排序 | 支持方程导向时域公式化；具体效率和稳定性限于原文算例 |
| [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]] | EMT 元件可通过声明式 DAE 和连接方程表达，而不是手工嵌入固定伴随电路流程 | 支持模型与求解器解耦的路线；工具能力需以原文和实现为准 |
| [[numerical-integration-by-the-2-stage-diagonally]] | 积分稳定函数解释了梯形法突变后虚假振荡，2S-DIRK 给出另一种有阻尼时域离散路线 | 支持积分公式对时域结果的影响；不证明所有高频暂态都应被阻尼 |

## 与相关页面的关系

- [[algebraic-characterization]]：说明时域方程离散后如何统一成代数残差。
- [[dae-solvers]]：求解隐式时域公式化产生的 DAE 或非线性残差。
- [[companion-circuit]]：EMTP 类时域公式化的关键实现形式。
- [[trapezoidal-rule]]、[[backward-euler]] 和 [[gear-method]]：常见底层积分规则。
- [[numerical-oscillation-suppression]]：处理不连续点和积分高频误差。
- [[emt-simulation-verification]]：为时域公式化结果提供可审计验证流程。

## 修订与证据使用注意事项

后续扩展本页时，应把公式、步长、误差、运行时间和适用对象绑定到具体来源。不要新增未核验的“典型 EMT 步长”“软件默认算法”“实时可行规模”或“完全捕捉暂态”等强断言。
