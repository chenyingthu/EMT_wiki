---
title: "代数表征法 (Algebraic Characterization)"
type: method
tags: [algebraic, characterization, implicit, equation, dae, sparse-matrix]
created: "2026-05-02"
---

# 代数表征法 (Algebraic Characterization)

## 定义与边界

代数表征法（Algebraic Characterization）是把 EMT 模型在某一时间步或某一接口处整理成可求解的代数关系。它不是把动态过程“静态化”，而是通过隐式积分、端口等效、变量消去或约束组装，把连续方程和网络约束转成残差形式：

$$
\mathbf{R}(\mathbf{z}_{n+1};\mathbf{z}_{n},\mathbf{p},t_{n+1})=\mathbf{0},
$$

其中 $\mathbf{z}_{n+1}$ 可包含节点电压、支路电流、设备状态、控制变量和接口量，$\mathbf{p}$ 表示参数、拓扑和开关状态。若残差为线性，问题可直接进入稀疏矩阵求解；若残差为非线性，则通常需要 [[newton-raphson-method]] 或其他非线性求解器。

本页关注“方程如何被组织成代数求解问题”，不把某种稀疏矩阵格式、某个 DAE 工具或某个商业程序写成唯一标准。

## EMT 中的作用

EMT 主循环在每个时间步都要把元件历史、网络拓扑和控制状态合并。代数表征法使这些异质模型能够进入同一个求解接口：

- 动态元件经积分后成为等效电导和历史源。
- 线路、FDNE 和电缆模型经时延或递归卷积生成当前步注入量。
- 电机、换流器和外部网络可通过 Norton、Thevenin 或多端口等效暴露端口关系。
- 非线性元件通过局部线性化或残差方程联立求解。

因此，代数表征是 [[time-domain-formulation]] 与 [[sparse-matrix-solver]]、[[dae-solvers]] 之间的中间层。

## 核心机制

### 隐式离散

若连续模型为

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{y},t), \quad
\mathbf{0}=\mathbf{g}(\mathbf{x},\mathbf{y},t),
$$

用隐式积分替换 $\dot{\mathbf{x}}$ 后，可形成

$$
\mathbf{R}_{n+1}=
\begin{bmatrix}
\mathbf{r}_x(\mathbf{x}_{n+1},\mathbf{y}_{n+1}) \\
\mathbf{g}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})
\end{bmatrix}
=\mathbf{0}.
$$

梯形积分下，状态残差的一般形式为

$$
\mathbf{r}_x =
\mathbf{x}_{n+1}-\mathbf{x}_n
-\frac{\Delta t}{2}\left[
\mathbf{f}(\mathbf{x}_n,\mathbf{y}_n,t_n)
+\mathbf{f}(\mathbf{x}_{n+1},\mathbf{y}_{n+1},t_{n+1})
\right].
$$

### 节点导纳表征

对线性或已线性化支路，端口关系常写成

$$
\mathbf{i}_{port,n+1}
=\mathbf{G}_{eq}\mathbf{v}_{port,n+1}
+\mathbf{i}_{hist,n+1}.
$$

组装到网络后得到

$$
\mathbf{Y}\mathbf{v}=\mathbf{i}_{inj}.
$$

这里的 $\mathbf{Y}$ 不是纯拓扑对象，而是包含电阻、伴随电导、端口等效、开关状态和部分控制接口的代数结果。

### 变量消去

当模型包含内部节点和外部端口时，可按分块矩阵表示：

$$
\begin{bmatrix}
\mathbf{Y}_{ee} & \mathbf{Y}_{ei} \\
\mathbf{Y}_{ie} & \mathbf{Y}_{ii}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}_e \\
\mathbf{v}_i
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{i}_e \\
\mathbf{i}_i
\end{bmatrix}.
$$

若 $\mathbf{Y}_{ii}$ 可逆，消去内部节点得到端口等效

$$
\mathbf{Y}_{eq}
=\mathbf{Y}_{ee}-\mathbf{Y}_{ei}\mathbf{Y}_{ii}^{-1}\mathbf{Y}_{ie}.
$$

这类 Schur 补或补偿消去可以降低主网络规模，但必须保留回代信息，否则内部状态、能量和测量量可能丢失。

## 分类与变体

| 表征形式 | 机制 | 典型用途 | 风险 |
|---|---|---|---|
| 线性代数网络 | 固定 $\mathbf{Y}$ 与历史源 | RLC 网络、固定拓扑实时仿真 | 事件后历史源不一致会产生误差 |
| 非线性残差 | 残差加雅可比迭代 | 饱和、避雷器、电力电子约束 | 收敛依赖初值和雅可比质量 |
| 端口 Norton/Thevenin | 把子网络暴露为端口源和导纳/阻抗 | 外部网络、电机、MMC、FDNE | 等值范围之外的动态不可外推 |
| Schur 补/节点消去 | 消去内部节点形成低维端口矩阵 | 多端口子模块、网络分解 | 病态内部矩阵会放大误差 |
| 方程导向 DAE | 保持隐式方程，由工具链排序求解 | Modelica、FMI、跨域建模 | 工具事件处理和求解器设置必须记录 |

## 适用边界与失败模式

- 代数表征依赖变量尺度和方程独立性；约束冗余或奇异会导致矩阵病态。
- 开关拓扑变化会改变 $\mathbf{Y}$ 或残差结构，若仍复用旧分解和历史项，结果可能不守恒。
- 用端口等效替代完整子网络时，必须说明端口频带、线性化点和内部状态恢复方式。
- 非线性局部线性化只在当前工作区附近有效，跨饱和段、限幅器或开关边界时需重建。
- 稀疏求解效率不能用无来源复杂度公式概括；实际填充、重排序和矩阵结构取决于网络拓扑。

## 代表性证据

| 来源 | 支持的认识 | 证据边界 |
|---|---|---|
| [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us]] | 多端口 MMC 子模块可通过 Schur 补递归消去内部节点，形成广义 Norton 等效并回代内部状态 | 支持端口代数表征和节点消去机制；加速量需绑定原文算例 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga]] | 非线性元件可被补偿法分离为 Thevenin 端口，再对非线性端口电流求残差 | 支持非线性端口代数求解；案例不足以覆盖所有强耦合设备 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]] | 状态变量消去可服务于 EMTP 型恒定导纳等效和历史源结构 | 支持状态消去路线；具体模型范围需原文核验 |
| [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]] | 方程导向 EMT 把元件和连接关系组织为隐式 DAE，再交由工具链处理 | 支持高层代数/DAE 表征；不替代具体求解器验证 |

## 与相关页面的关系

- [[time-domain-formulation]]：提供连续时域方程来源。
- [[dae-solvers]]：求解代数表征形成的隐式残差。
- [[newton-raphson-method]]：非线性代数表征的常用迭代内核。
- [[compensation-method]]：通过端口等值和接口变量实现分离求解。
- [[norton-equivalent]]、[[thevenin-equivalent]] 和 [[thevenin-norton-equivalent]]：端口代数表征的基础形式。
- [[sparse-matrix-solver]]：大规模线性代数表征的计算后端。

## 修订与证据使用注意事项

不要把“代数化”写成丢失动态，也不要把“稀疏矩阵”写成固定复杂度收益。涉及矩阵规模、加速比、容差、实时 deadline 或收敛次数时，应同时给出来源、算例、硬件/软件平台和基线。
