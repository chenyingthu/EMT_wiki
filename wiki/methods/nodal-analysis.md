---
title: "节点分析与伴随电路 (Nodal Analysis / Companion Circuit)"
type: method
tags: [nodal-analysis, companion-circuit, emtp, admittance, conductance]
created: "2026-04-13"
---

# 节点分析与伴随电路 (Nodal Analysis / Companion Circuit)

## 定义与边界

节点分析在 EMT 中通常指把网络元件离散为诺顿型或增广节点型等效后，按节点电压和必要的附加支路变量形成代数方程。它不是单独的积分算法，也不是某一仿真软件的专有实现；积分公式、开关处理、非线性迭代和矩阵求解器会共同决定最终的数值行为。

典型节点方程可写为：

$$
\mathbf{Y}_n \mathbf{v} = \mathbf{i}
$$

其中 $\mathbf{Y}_n$ 为离散时刻的节点导纳矩阵，$\mathbf{v}$ 为节点电压向量，$\mathbf{i}$ 为独立电流源与历史电流源形成的注入向量。含电压源、理想开关、受控源或强约束元件时，常需要采用增广节点形式，而不是只依赖纯导纳矩阵。

## EMT 中的作用

节点分析把元件模型和网络求解分离：元件侧给出等效导纳、历史源和状态更新规则；网络侧组装 [[nodal-admittance-matrix]] 并调用 [[sparse-matrix-solver]] 或局部补偿算法求解节点电压。这样可以让电感、电容、线路、变压器、电力电子等模型在统一接口下接入 EMT 步进过程。

在 EMTP 类算法中，[[companion-circuit]] 是节点分析的关键接口。动态元件经过 [[numerical-integration]] 离散后转化为本时步导纳和历史源；求得节点电压后，再回代更新支路电流、磁链、电荷或控制状态。

## 核心机制

线性支路 $(p,q)$ 的导纳 $g$ 对矩阵的贡献为：

$$
Y_{pp} \mathrel{+}= g,\quad
Y_{qq} \mathrel{+}= g,\quad
Y_{pq} \mathrel{-}= g,\quad
Y_{qp} \mathrel{-}= g
$$

电容在梯形积分下的诺顿等效可写为：

$$
i_C(t_k)=\frac{2C}{\Delta t}v_C(t_k)+I_{C,hist}(t_{k-1})
$$

电感可写为：

$$
i_L(t_k)=\frac{\Delta t}{2L}v_L(t_k)+I_{L,hist}(t_{k-1})
$$

这些公式说明伴随电路中的等效导纳依赖步长和积分方法，历史源依赖上一时刻状态。若使用后向欧拉、Gear 或 DIRK 类方法，等效导纳和历史项会改变；因此“节点分析”本身不保证某种精度或阻尼特性。

含附加约束时，可使用改进或增广节点方程：

$$
\begin{bmatrix}
\mathbf{Y}_n & \mathbf{A}\\
\mathbf{B} & \mathbf{C}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}\\
\mathbf{x}
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{j}\\
\mathbf{e}
\end{bmatrix}
$$

其中 $\mathbf{x}$ 可代表电压源电流、开关约束变量或其他模型接口变量。[[state-space-method]] 可与节点方程组合使用，但其边界是设备内部状态方程；节点分析主要承担网络连接和代数约束。

## 分类与变体

| 变体 | 主要对象 | 边界 |
|------|----------|------|
| 纯节点导纳法 | 由电阻、诺顿等效源和导纳支路组成的网络 | 难以直接表示理想电压源和某些强约束元件 |
| 改进/增广节点分析 | 电压源、受控源、互感、开关约束 | 矩阵可能非对称或更病态 |
| 伴随电路节点法 | 含电感、电容、线路的时域 EMT 网络 | 数值特性取决于积分公式和步长 |
| 恒导纳节点法 | 高频开关或实时仿真中的固定矩阵需求 | 常以等效源、延迟或插值换取矩阵复用 |
| 分网节点法 | 大规模或并行 EMT | 边界延迟、接口阻抗和迭代协调会影响稳定性 |

## 适用边界与失败模式

节点分析适合拓扑清晰、网络稀疏、可用等效导纳和注入源描述的 EMT 系统。它在开关频繁动作、理想元件形成奇异回路、非线性元件雅可比变化剧烈、步长与最快暂态不匹配时容易暴露数值问题。

常见失败模式包括：

- 梯形积分在开关或强刚性 LC 网络中出现数值振荡，需要切换阻尼积分、插值或局部损耗建模。
- 断路支路用极小导纳、闭合支路用极大导纳时可能导致 [[nodal-admittance-matrix]] 病态。
- 恒导纳模型若未说明延迟、插值和等效假设，不能外推为“精确”详细开关模型。
- 分网或混合仿真接口若只交换上一时步量，可能引入接口延迟；应与 [[electromechanical-electromagnetic-hybrid-simulation]] 的边界条件一起评估。

## 代表性来源

- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 代表状态空间与节点方程结合的路线，适合作为复杂设备接入节点框架的来源。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] 可用于比较伴随电路离散策略；其中结论应按其算例和积分设置限定。
- [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat]] 涉及嵌套或预计算思路，适合作为矩阵复用和开关状态处理的个案来源。
- [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul]] 支撑固定导纳思想在变换器等值中的应用，但不能替代所有电力电子拓扑的详细验证。

## 与相关页面的关系

- [[nodal-admittance-matrix]] 描述矩阵对象本身；本页描述如何由 EMT 元件和伴随电路形成并使用该矩阵。
- [[sparse-matrix-solver]] 关注线性方程求解和重排序；本页只说明求解器在节点分析流程中的位置。
- [[iterative-solvers]] 处理非线性或大型线性系统的逐步求解；本页中的节点方程可作为迭代过程的内层线性问题。
- [[fixed-admittance]] 是固定矩阵复用的建模策略，不等同于所有节点分析。
- [[companion-model]] 和 [[companion-circuit]] 是动态元件离散到节点方程的接口层。
