---
title: "详细等效模型 (Detailed Equivalent Model)"
type: method
tags: [detailed-equivalent, modeling, reduction, port, accuracy, wideband]
created: "2026-05-02"
updated: "2026-05-18"
---

# 详细等效模型 (Detailed Equivalent Model)

## 定义与边界

详细等效模型（Detailed Equivalent Model, DEM）是在不展开全部内部节点的前提下，尽量保持原系统在指定端口、频段和运行点附近动态行为的等值模型。它比工频戴维南或诺顿等值更强调宽频响应、端口耦合、状态空间实现和无源性，但仍然是等值模型，不是原系统的完整复制。

本页中的"详细"只表示相对于简单等值保留更多端口动态。它不自动意味着高精度、实时可用或适用于所有故障。每个详细等值都必须说明端口、频率范围、运行点、拟合方法、验证基线和不能外推的边界。

## EMT 中的作用

详细等效模型在 EMT 中常用于：

- 将外部大网络压缩为频率相关多端口等值，保留对局部暂态有影响的宽频导纳。
- 将变压器、线路、风电场、MMC 或固态变压器等设备压缩为端口模型，减少详细开关或内部节点数量。
- 在机电-电磁混合仿真中为 EMT 边界提供动态外部网络。
- 为实时仿真或批量暂态研究降低计算规模，但仍保留目标端口行为。

它的适用前提是研究问题主要由端口响应决定，而不是内部单元、内部保护或局部绝缘应力决定。

## EMT 建模方法

### 方法一：戴维南等效电阻法（Time-Varying Thevenin）

MMC 的详细等效模型最早由 [[Gnanarathna 2011 efficient-mmc|Gnanarathna et al. 2011]] 提出，将桥臂中 $N_{\text{sub}}$ 个子模块等效为一个戴维南串联支路：

$$v_{\text{arm}}(t) = \sum_{k=1}^{N_{\text{sub}}} v_{ck}(t) = R_{\text{eq}}(t) \cdot i_{\text{arm}}(t) + v_{\text{eq}}(t)$$

其中 $R_{\text{eq}}(t)$ 是时变等效电阻（梯形积分离散化产生），$v_{\text{eq}}(t)$ 是等效电压源。该方法将 $N_{\text{sub}}$ 个详细开关节点压缩为 1 个端口节点，导纳矩阵阶数降低 $N_{\text{sub}}$ 倍。

**问题**：每当子模块开关闭换状态变化，$R_{\text{eq}}(t)$ 必须更新，导致网络导纳矩阵频繁重新分解（re-triangularization）。在大规模系统中（含多台 MMC），这是主要的计算瓶颈。

### 方法二：常导纳矩阵加速法（Parvari 等 2023）

Parvari 等 2023 针对 MMC 的 DEM 提出改进策略：在正常运行时保持**恒定导纳矩阵**（时变电阻并入历史源），只在换流器闭锁（blocking）事件时更新导纳矩阵。由于闭锁是稀有事件（只在直流故障时触发），该方法大幅减少矩阵分解次数：

$$\mathbf{Y}_{\text{MMC}} = \text{const}, \quad \text{仅在 } \text{blocking} \to \mathbf{Y}_{\text{MMC}}^{\text{blocked}}$$

实现方式是将时变电阻 $R_{\text{eq}}(t)$ 的变化体现在诺顿历史源 $i_{\text{hist}}(t)$ 中：

$$i_{\text{hist}}(t) = \frac{v_{\text{eq}}(t-\Delta t)}{R_{\text{eq}}(t-\Delta t)} + i_{\text{hist}}(t-\Delta t)$$

量化加速效果：HBSM MMC 效率提升 **30%**，FBSM MMC 效率提升 **60%**（相比传统 DEM，PSCAD/EMTDC 验证）。

### 方法三：频域响应拟合法（Vector Fitting + State Space）

对于宽频端口等值（覆盖 DC 至数百 kHz），使用矢量拟合将端口导纳矩阵转换为有理函数形式：

$$\mathbf{Y}_{\mathrm{eq}}(s) = \mathbf{D} + s\mathbf{H} + \sum_{k=1}^{r}\frac{\mathbf{R}_k}{s-p_k}$$

其中 $p_k$ 是极点，$\mathbf{R}_k$ 是留数矩阵。该形式可转成状态空间：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{v}, \quad \mathbf{i} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{v}$$

进入 EMT 后，通过梯形积分或递归卷积更新历史项。拟合阶数 $r$ 决定精度和计算复杂度。

### 方法四：模型降阶（Model Order Reduction）

若从详细状态空间模型降阶，可用投影形式：

$$\mathbf{x} \approx \mathbf{V}_r \mathbf{x}_r, \quad \dot{\mathbf{x}}_r = \mathbf{A}_r \mathbf{x}_r + \mathbf{B}_r \mathbf{v}$$

降阶目标不只是减少阶数，还要保持端口响应、稳定性和物理可实现性。若模型包含无源网络，降阶后还应检查无源性（passivity enforcement）。

## 核心机制

### 端口等效目标

对多端口线性或线性化系统，详细等效通常保持：

$$\mathbf{i}(s) = \mathbf{Y}_{\mathrm{orig}}(s)\mathbf{v}(s)$$

并构造较小模型：

$$\mathbf{i}(s) \approx \mathbf{Y}_{\mathrm{eq}}(s)\mathbf{v}(s)$$

误差必须绑定频率集合 $\Omega$、端口方向和矩阵范数：

$$\epsilon(\omega) = \frac{\|\mathbf{Y}_{\mathrm{eq}}(j\omega) - \mathbf{Y}_{\mathrm{orig}}(j\omega)\|}{\|\mathbf{Y}_{\mathrm{orig}}(j\omega)\|}, \quad \omega \in \Omega$$

没有来源和基线时，不应写固定误差阈值。

### 有理函数与状态空间

频率相关端口模型常写成：

$$\mathbf{Y}_{\mathrm{eq}}(s) = \mathbf{D} + s\mathbf{H} + \sum_{k=1}^{r}\frac{\mathbf{R}_k}{s-p_k}$$

该形式可转成状态空间，进入 EMT 后通过梯形积分、递归卷积或伴随电路更新历史项。

### 无源性条件

对导纳型端口模型，频域无源性条件为：

$$\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega) \succeq 0$$

无源性不是拟合精度的一部分，而是时域互联稳定性的约束。一个拟合误差较小的有理模型仍可能因非无源而在 EMT 仿真中发散。

## 分类与变体

| 类型 | 输入证据 | EMT 实现 | 适用边界 |
|------|----------|----------|----------|
| 频变网络等值（FDNE） | 外部网络频率扫描或解析导纳 | RLC 网络、状态空间、诺顿历史项 | 线性端口、固定拓扑或分段拓扑 |
| 设备端口等值 | 测量、黑箱扰动或内部物理模型 | 多端口 $\mathbf{Y}(s)$ | 端口现象，不含内部节点解释 |
| 结构保持聚合 | 详细设备状态方程 | 降阶后保留原模型接口 | 适合系统级动态，不适合个体保护 |
| 开关网络详细等值 | 子模块或桥臂等效 | 固定导纳加历史源 | 需说明开关状态和平均化边界 |
| 分布式磁路等值 | 几何和材料参数 | 电路化磁阻网络 | 成本高，验证范围通常较窄 |
| DEM+AVM 混合 | 部分运行点用 AVM，切换点用 DEM | 双模型并行，事件触发切换 | 正常运行时加速，故障时保精度 |

## 量化性能边界

| 方法 | 加速比 | 精度损失 | 适用场景 |
|------|--------|----------|----------|
| 详细开关模型（DSM） | 1×（基准） | 无 | 子模块级分析 |
| 传统 DEM（Gnanarathna 2011） | 5–10× | <5% | 大规模系统 |
| 加速 DEM（Parvari 2023，HBSM） | 7–13× | <5% | 含多台 MMC 的网络 |
| 加速 DEM（Parvari 2023，FBSM） | 10–16× | <5% | 含 FB 子模块的 MMC |
| AVM（稳态运行） | 50–100× | 5–20% | 控制验证、系统级暂态 |

*数据来源：Parvari et al. 2023, PSCAD/EMTDC 验证；Gnanarathna et al. 2011*

## 关键技术挑战

**挑战一：矩阵频繁重新分解（传统 DEM 的计算瓶颈）**

时变电阻导致每次开关闭换时导纳矩阵更新，在大规模系统中（含多台 MMC，每台数百至上千个子模块）矩阵分解成为主要瓶颈。**解法**：Parvari 2023 的常导纳矩阵策略，将时变电阻并入历史源，仅在闭锁事件时更新矩阵。

**挑战二：无源性保持（拟合后可能发散）**

有理函数拟合后的模型可能在某些频段失去无源性，即使拟合误差很小。**解法**：使用半无源约束优化（semidefinite programming）或后处理无源性补偿（passivity enforcement）。

**挑战三：多运行点切换（非线性系统的单一等值不足）**

当 MMC 运行在正常模式和故障闭锁模式时，戴维南等效参数完全不同。单一等值无法同时覆盖两种模式。**解法**：多运行点 DEM 或 DEM-AVM 混合模型（Parvari 2023 方案：正常模式用常导纳 DEM，闭锁时切换拓扑）。

**挑战四：宽频等值的拟合阶数与实时性矛盾**

宽频等值（DC–100 kHz）需要高阶有理函数拟合（$r = 20\text{–}50$），但实时仿真要求低阶模型。**解法**：使用渐进拟合或分段拟合（低频用低阶，高频用附加修正项）。

## 适用边界与失败模式

详细等效模型的主要风险包括：

- 端口选错，导致被等值掉的内部状态正是研究目标。
- 频率扫描范围不足，却将模型用于范围之外的高频或低频暂态。
- 用单运行点小信号等值表示大扰动故障、限流、保护动作或拓扑切换。
- 只报告波形相似，没有说明对照基线、误差指标、时间步长和端口方向。
- 拟合后没有检查稳定性、实极点位置和无源性。
- 把计算加速或误差数字从单篇论文算例外推为通用性能。

## 代表性证据

- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]：支撑多端口 FDNE 的端口导纳矩阵、内部节点消去和 EMTP 可实现 RLC 等效网络。其大型 500 kV 网络证据应限定在原文算例和频率范围。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：支撑机电-电磁混合仿真中用共享极点有理函数和无源性处理构建外部网络详细等值。当前来源页明确提醒不能保留无来源误差百分比。
- [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions]]：支撑变压器端口导纳矩阵的宽频等值方法，适合说明详细等值可以是设备端口模型，而非内部绕组模型。
- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|Parvari 等 2023]]：加速 MMC 详细等效模型（30%/60% 加速），常导纳矩阵策略的核心来源。
- [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based]]：说明"详细"也可以来自电路化磁路网格，但该类模型的验证范围和参数需求不同于普通端口等值。

## 相关页面

- [[network-equivalent]] 是外部系统等值的主题入口。
- [[norton-equivalent]] 和 [[equivalent-circuit-method]] 是详细等值进入 EMT 节点方程的常见实现形式。
- [[vector-fitting]] 用于把频域样本转化为有理函数模型。
- [[passivity-enforcement]] 是频变详细等值的重要稳定性检查。
- [[frequency-scan]] 和 [[impedance-measurement]] 提供端口导纳或阻抗样本。
- [[model-order-reduction]] 处理状态空间降阶方法。
- [[mmc-model]] 是 MMC 详细等效模型的主要应用对象。
- [[transformer-network]] 和 [[converter-transformer-model]] 是设备级详细等值的相邻入口。

## 来源论文

- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|Parvari 等 2023]] — 《An accelerated detailed equivalent model for modular multilevel converters》，*Electric Power Systems Research*，提出常导纳矩阵 MMC DEM，消除正常运行时矩阵重分解，HBSM 效率提升 30%、FBSM 效率提升 60%
- [[gnanarathna-2011-efficient-mmc|Gnanarathna 等 2011]] — 《Efficient modeling of modular multilevel HVDC converters on electromagnetic transient simulator》，首个 MMC DEM 戴维南等效模型框架
- [[loewner-matrix-approach-for-modelling-fdnes|Gurrala 2015]] — 《Loewner matrix approach for modelling FDNEs of power systems》，Loewner 矩阵方法构建频域依赖网络等值