---
title: "集总参数模型 (Lumped Parameter Model)"
type: method
tags: [lumped-parameter, pi-model, equivalent-circuit, short-line, medium-line, long-line, transmission-line]
created: "2026-05-02"
---

# 集总参数模型 (Lumped Parameter Model)

## 定义与边界

集总参数模型（Lumped Parameter Model）把空间分布的电阻、电感、电导和电容替换为有限个集中元件。在线路、电缆、变压器漏抗、滤波器和等效支路中，它把连续场问题或传输线问题转化为可由 [[nodal-analysis]]、[[state-space-method]] 或 [[companion-circuit]] 求解的电路模型。

本页讨论 EMT 方法中的集总化原则，而不是给出固定工程长度表。集总近似是否成立取决于线路电气长度、目标频带、波头陡度、参数频变性和研究指标。不能把某一电压等级或某一长度阈值当作全局规则。

## EMT 中的作用

集总参数模型在 EMT 中的作用包括：

- 把短线路、滤波器、支路阻抗和变压器等对象转化为 R、L、C、G 元件。
- 作为多段线路模型或 π 型等效的基本单元。
- 为控制器、设备模型和网络等值提供低阶端口电路。
- 通过 [[companion-model]] 把电感、电容离散为当前导纳和历史源。

它的主要收益是模型结构简单、可直接装配进导纳矩阵；主要风险是丢失传播延时、分布谐振和频率相关损耗。

## 核心机制

均匀传输线的分布参数形式为：

$$
\frac{\partial v}{\partial x}=-(r+l\frac{\partial}{\partial t})i
$$

$$
\frac{\partial i}{\partial x}=-(g+c\frac{\partial}{\partial t})v
$$

若研究频带内线路电气长度较小，可用总参数近似：

$$
R=r\ell,\quad L=l\ell,\quad G=g\ell,\quad C=c\ell
$$

常见 π 型等效把串联阻抗 $Z$ 放在中间，并把并联导纳 $Y$ 分到两端：

$$
Z=(r+j\omega l)\ell
$$

$$
Y=(g+j\omega c)\ell
$$

在 EMT 时域中，$R$ 和 $G$ 直接进入导纳矩阵，$L$ 和 $C$ 通过积分公式转化为伴随支路。例如电容在梯形法下可写成：

$$
i_{n+1}=\frac{2C}{\Delta t}v_{n+1}+I_{hist}^{n}
$$

其中历史源由上一时间步的电压、电流和符号约定决定。

## 分类与变体

| 变体 | 结构 | 典型用途 | 边界 |
|------|------|----------|------|
| 串联 RL | 忽略并联电容和电导 | 短支路、低频阻抗 | 不能表示充电电流和行波 |
| π 型等效 | 串联 $Z$，两端 $Y/2$ | 工频或较低频线路等效 | 高频传播和分布谐振不足 |
| 修正 π 型 | 用双曲函数修正 $Z$ 和 $Y$ | 较长均匀线路的频域端口等效 | 参数仍绑定频率点或模型假设 |
| 多段 π 型 | 多个 π 段级联 | 需要有限传播近似的 EMT | 段数、步长和目标频带需验证 |
| 集总设备模型 | 变压器漏抗、滤波器、负荷支路 | 设备端口建模 | 不保留设备内部场分布 |

## 适用边界与失败模式

集总参数模型适合用于电气尺寸相对目标波长较小、端口量是主要研究对象、且频率相关效应不主导结果的场景。常见失败模式包括：

- 用单个 π 型支路分析雷电、陡波开关或电缆高频振荡。
- 只根据物理长度选择模型，而不检查波速、频率范围和目标误差。
- 把集总线路的端口电压结果外推为沿线过电压或绝缘应力分布。
- 对长电缆忽略频率相关参数和多模传播。
- 用过多 π 段模拟行波，却没有检查数值步长、阻尼和矩阵条件数。

## 代表性证据

[[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss]] 提供了集总近似与分布参数线路的边界对照：传统 TNA 使用许多 π/T 无源节段表示线路，而实时数字线路模型改用 Bergeron 行波和集中电阻近似。该来源说明集总段模型在工程中有历史用途，但不能替代对分布传播的建模。

[[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 支撑“集总 RLC 或状态空间集群经积分离散后可作为伴随等效装配到节点方程”的机制。该来源的具体加速、实时和误差结论应限于其原文算例；在本页只作为集总模型进入节点求解器的代表证据。

## 与相关页面的关系

- [[distributed-parameter-model]]：连续分布参数模型入口，适合行波和宽频传播。
- [[distributed-parameter-line]]：线路分布参数的具体建模页面。
- [[lumped-resistance-approximation]]：只集中线路电阻损耗，通常与 Bergeron 线结合。
- [[companion-model]]：说明集总电感、电容如何离散为导纳和历史源。
- [[frequency-dependent-line-model]]：当参数随频率变化显著时，应使用频变线路模型。
- [[transmission-line-model]]、[[cable-model]] 和 [[transformer-model]] 是集总化最常见的对象页面。

## 开放问题

- 多段 π 型的段数选择应绑定目标频带、传播速度、步长和误差指标，而不是固定长度表。
- 对电缆、接地系统和宽频变压器，低阶集总模型与有理函数模型之间需要明确验证边界。
- 在自动建模工具中，应记录集总化假设、端口定义和源参数来源，避免模型可复核性丢失。

## 来源论文

参见 [[index]] 获取更多集总参数模型相关文献。
