---
title: "详细等效模型 (Detailed Equivalent Model)"
type: method
tags: [detailed-equivalent, modeling, reduction, port, accuracy, wideband]
created: "2026-05-02"
---

# 详细等效模型 (Detailed Equivalent Model)


```mermaid
graph TD
    subgraph Ncmp[详细等效模型 (Detailed Equivalent …]
        N0[频变网络等值: 外部网络频率扫描或解析导纳]
        N1[设备端口等值: 测量、黑箱扰动或内部物理模型]
        N2[结构保持聚合: 详细设备状态方程]
        N3[开关网络详细等值: 子模块或桥臂等效]
        N4[分布式磁路等值: 几何和材料参数]
    end
```


## 定义与边界

详细等效模型是在不展开全部内部节点的前提下，尽量保持原系统在指定端口、频段和运行点附近动态行为的等值模型。它比工频戴维南或诺顿等值更强调宽频响应、端口耦合、状态空间实现和无源性，但仍然是等值模型，不是原系统的完整复制。

本页中的“详细”只表示相对于简单等值保留更多端口动态。它不自动意味着高精度、实时可用或适用于所有故障。每个详细等值都必须说明端口、频率范围、运行点、拟合方法、验证基线和不能外推的边界。

## EMT 中的作用

详细等效模型在 EMT 中常用于：

- 将外部大网络压缩为频率相关多端口等值，保留对局部暂态有影响的宽频导纳。
- 将变压器、线路、风电场、MMC 或固态变压器等设备压缩为端口模型，减少详细开关或内部节点数量。
- 在机电-电磁混合仿真中为 EMT 边界提供动态外部网络。
- 为实时仿真或批量暂态研究降低计算规模，但仍保留目标端口行为。

它的适用前提是研究问题主要由端口响应决定，而不是内部单元、内部保护或局部绝缘应力决定。

## 核心机制

### 端口等效目标

对多端口线性或线性化系统，详细等效通常保持：

$$
\mathbf{i}(s)=\mathbf{Y}_{\mathrm{orig}}(s)\mathbf{v}(s)
$$

并构造较小模型：

$$
\mathbf{i}(s)\approx \mathbf{Y}_{\mathrm{eq}}(s)\mathbf{v}(s)
$$

误差必须绑定频率集合 $\Omega$、端口方向和矩阵范数：

$$
\epsilon(\omega)=
\frac{\left\|\mathbf{Y}_{\mathrm{eq}}(j\omega)-\mathbf{Y}_{\mathrm{orig}}(j\omega)\right\|}
{\left\|\mathbf{Y}_{\mathrm{orig}}(j\omega)\right\|}
,\quad \omega\in\Omega
$$

没有来源和基线时，不应写固定误差阈值。

### 有理函数与状态空间

频率相关端口模型常写成：

$$
\mathbf{Y}_{\mathrm{eq}}(s)=\mathbf{D}+s\mathbf{H}+\sum_{k=1}^{r}\frac{\mathbf{R}_k}{s-p_k}
$$

其中 $p_k$ 是极点，$\mathbf{R}_k$ 是留数矩阵。该形式可转成状态空间：

$$
\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{v}
$$

$$
\mathbf{i}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{v}
$$

进入 EMT 后，再由梯形积分、递归卷积或伴随电路更新历史项。

### 降阶与端口保真

若从详细状态空间模型降阶，可用投影形式：

$$
\mathbf{x}\approx \mathbf{V}_r \mathbf{x}_r
$$

得到低阶模型：

$$
\dot{\mathbf{x}}_r=\mathbf{A}_r\mathbf{x}_r+\mathbf{B}_r\mathbf{v}
$$

降阶目标不只是减少阶数，还要保持端口响应、稳定性和物理可实现性。若模型包含无源网络，降阶后还应检查 [[passivity-enforcement]]。

### 无源性

对导纳型端口模型，常用频域无源性条件可写成：

$$
\mathbf{Y}(j\omega)+\mathbf{Y}^{H}(j\omega)\succeq 0
$$

无源性不是拟合精度的一部分，而是时域互联稳定性的约束。一个拟合误差较小的有理模型仍可能因非无源而在 EMT 仿真中发散。

## 分类与变体

| 类型 | 输入证据 | EMT 实现 | 适用边界 |
|------|----------|----------|----------|
| 频变网络等值 | 外部网络频率扫描或解析导纳 | RLC 网络、状态空间、诺顿历史项 | 线性端口、固定拓扑或分段拓扑 |
| 设备端口等值 | 测量、黑箱扰动或内部物理模型 | 多端口 $\mathbf{Y}(s)$ | 端口现象，不含内部节点解释 |
| 结构保持聚合 | 详细设备状态方程 | 降阶后保留原模型接口 | 适合系统级动态，不适合个体保护 |
| 开关网络详细等值 | 子模块或桥臂等效 | 固定导纳加历史源 | 需说明开关状态和平均化边界 |
| 分布式磁路等值 | 几何和材料参数 | 电路化磁阻网络 | 成本高，验证范围通常较窄 |

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
- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]] 与 [[parallelization-of-mmc-detailed-equivalent-model]]：可作为 MMC 详细等效模型的代表来源，使用时应区分子模块级等效、桥臂级等效和开关细节保留程度。
- [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based]]：说明“详细”也可以来自电路化磁路网格，但该类模型的验证范围和参数需求不同于普通端口等值。

## 与相关页面的关系

- [[network-equivalent]] 是外部系统等值的主题入口。
- [[norton-equivalent]] 和 [[equivalent-circuit-method]] 是详细等值进入 EMT 节点方程的常见实现形式。
- [[vector-fitting]] 用于把频域样本转化为有理函数模型。
- [[passivity-enforcement]] 是频变详细等值的重要稳定性检查。
- [[frequency-scan]] 和 [[impedance-measurement]] 提供端口导纳或阻抗样本。
- [[model-order-reduction]] 处理状态空间降阶方法。
- [[transformer-network]] 和 [[converter-transformer-model]] 是设备级详细等值的相邻入口。

## 开放问题

- 对含强非线性控制和保护动作的对象，单个线性详细等值往往不足，需要多运行点、事件触发或混合模型。
- 宽频端口模型与实时仿真步长之间的可实现性，需要同时检查阶数、离散化和硬件资源。
- 测量型黑箱等值的可解释性有限，不能替代需要内部状态的故障诊断或设备设计模型。

## 来源论文

参见 [[index]] 获取更多详细等效模型相关文献。
