---
title: "节点导纳矩阵 (Nodal Admittance Matrix)"
type: method
tags: [nodal-admittance, ybus, matrix-solution, power-flow, circuit-analysis]
created: "2026-05-02"
---

# 节点导纳矩阵 (Nodal Admittance Matrix)

## 定义与边界

节点导纳矩阵是把网络支路导纳、对地导纳和元件等效导纳按节点关联关系组装成的线性算子。在线性时不变网络中，它描述节点注入电流与节点电压的关系；在 EMT 中，它通常是每个离散时刻或每类开关状态下的网络矩阵。

基本关系为：

$$
\mathbf{i}=\mathbf{Y}\mathbf{v}
$$

其中 $\mathbf{i}$ 是节点注入电流，$\mathbf{v}$ 是节点电压，$\mathbf{Y}$ 是节点导纳矩阵。该矩阵不是潮流方程的雅可比，也不直接表示频率相关网络等值的全部动态；频变、延迟和历史项通常由外部状态或伴随源承担。

## EMT 中的作用

在 [[nodal-analysis]] 中，节点导纳矩阵是网络联立求解的核心对象。元件模型把本时步的电阻、电感、电容、线路、变压器和开关等效为矩阵贡献；历史项、独立源和控制注入进入右端项。

EMT 中的矩阵可能随以下因素变化：

- 开关状态改变支路连接或等效导纳。
- 非线性元件在牛顿迭代中更新局部增量导纳。
- 变步长积分改变伴随电路等效导纳。
- 分网或等值模型改变边界节点的自导纳和互导纳。

## 核心机制

一条连接节点 $p$ 与 $q$ 的导纳支路 $y_{pq}$ 对矩阵的贡献为：

$$
\begin{bmatrix}
 y_{pq} & -y_{pq}\\
-y_{pq} &  y_{pq}
\end{bmatrix}
$$

写入全局矩阵即：

$$
Y_{pp}\mathrel{+}=y_{pq},\quad
Y_{qq}\mathrel{+}=y_{pq},\quad
Y_{pq}\mathrel{-}=y_{pq},\quad
Y_{qp}\mathrel{-}=y_{pq}
$$

节点 $p$ 的对地导纳 $y_{p0}$ 只贡献到 $Y_{pp}$。若用关联矩阵 $\mathbf{A}$ 和支路导纳矩阵 $\mathbf{Y}_b$ 表示，则可写为：

$$
\mathbf{Y}=\mathbf{A}\mathbf{Y}_b\mathbf{A}^T+\mathbf{Y}_{shunt}
$$

多相线路、互感和不对称元件会形成块矩阵。理想电压源、理想变压器和某些受控源可能需要增广变量，而不是强行写成普通导纳支路。

## 分类与变体

| 类型 | 用途 | 注意事项 |
|------|------|----------|
| 单相或序分量导纳矩阵 | 平衡或近似平衡网络分析 | 不适合直接表示强不平衡相域暂态 |
| 三相块导纳矩阵 | 不平衡、互感、相间耦合 EMT | 维度扩大，块稀疏结构应保留 |
| 伴随电路导纳矩阵 | 动态元件离散后的时域求解 | 依赖步长和积分公式 |
| 固定导纳矩阵 | 矩阵因子复用和实时仿真 | 开关影响转移到等效源或补偿项 |
| 等值端口导纳矩阵 | [[fdne-model]]、外部网络等值 | 频率相关性需由有理函数或状态空间实现 |

## 适用边界与失败模式

节点导纳矩阵适合稀疏、局部连接明显的电网网络。它的数值质量依赖接地参考、支路参数尺度、开关等效值和矩阵排序策略。

常见风险包括：

- 无参考节点、孤岛网络或理想源冲突会导致矩阵奇异或约束不一致。
- 极大/极小开关电阻会放大条件数，影响 [[sparse-matrix-solver]] 的主元选择和舍入误差。
- 把长线路或电缆直接用单个工频 $\pi$ 型支路表示，可能遗漏传播时延和频率相关效应；这类问题应转向 [[transmission-line-theory]]、[[bergeron-line-model]] 或 [[frequency-dependent-line-model]]。
- 将阻抗矩阵 $\mathbf{Z}=\mathbf{Y}^{-1}$ 当作显式稀疏对象通常会破坏稀疏性；只需要端口响应时可用 [[compensation-method]] 或局部求解。

## 代表性来源

- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 支撑节点方程与设备状态方程的耦合表述。
- [[accelerated-sparse-matrix-based-computation-of-electromagnetic-transients]] 可作为 EMT 稀疏矩阵计算加速的来源，性能结论应绑定其测试系统和实现。
- [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat]] 展示嵌套和预计算求解思路，适合说明矩阵结构复用。
- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] 代表端口导纳等值的应用边界，不能简化成普通静态 Ybus。

## 与相关页面的关系

- [[nodal-analysis]] 说明节点导纳矩阵如何进入 EMT 时间步进流程。
- [[sparse-matrix-solver]] 说明矩阵因子化、重排序、前代回代和迭代精化。
- [[iterative-solvers]] 处理非线性或大型线性矩阵方程的迭代求解。
- [[symmetrical-components]] 可在对称三相条件下把相域问题转为序分量问题；对不平衡 EMT 应谨慎使用。
- [[network-partitioning]] 和 [[fixed-admittance]] 分别关注矩阵分块和矩阵复用策略。
