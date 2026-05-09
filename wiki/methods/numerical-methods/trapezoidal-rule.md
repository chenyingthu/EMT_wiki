---
title: "梯形法则 (Trapezoidal Rule)"
type: method
tags: [trapezoidal, integration, numerical, a-stable, emt, companion-circuit, oscillation]
created: "2026-05-02"
---

# 梯形法则 (Trapezoidal Rule)


```mermaid
graph TD
    subgraph Ncmp[梯形法则 (Trapezoidal Rule)]
        N0[阶数: 二阶]
        N1[稳定性: A 稳定]
        N2[高频数值阻尼: 刚性极限不衰减]
        N3[平滑区间精度: 通常较好]
        N4[事件后风险: 历史项污染和交替误差]
    end
```


## 概述

梯形法则（Trapezoidal Rule）是 EMT 中最常见的隐式二阶积分方法之一。它用当前步两端的导数平均值近似积分，并把电感、电容等储能元件转换为 [[companion-circuit]]，再与 [[nodal-analysis]] 组合形成逐步网络方程。

梯形法的关键优点是二阶精度、A 稳定和实现相对简单；关键风险是非 L 稳定。在开关、故障、限幅或拓扑突变后，高频数值误差可能以交替形式保留下来，表现为非物理数值振荡。因此，梯形法在 EMT 中通常需要配合事件定位、历史项重置、[[backward-euler]] 或其他阻尼技术。

## 核心公式

对微分方程

$$
\dot{\mathbf{x}}=f(t,\mathbf{x})
$$

梯形法离散为：

$$
\mathbf{x}_{n+1}
=
\mathbf{x}_n+\frac{\Delta t}{2}\left[
f(t_n,\mathbf{x}_n)+f(t_{n+1},\mathbf{x}_{n+1})
\right]
$$

这是隐式方法，因为 $\mathbf{x}_{n+1}$ 出现在右端。局部截断误差为 $O(\Delta t^3)$，全局误差为 $O(\Delta t^2)$。二阶精度只在解足够平滑、事件处理正确、非线性迭代收敛的条件下成立。

## EMT 伴随电路

对电感 $v=L\,di/dt$，梯形法给出：

$$
i_{n+1}=G_L v_{n+1}+I_{hist}
$$

其中：

$$
G_L=\frac{\Delta t}{2L},\quad
I_{hist}=i_n+\frac{\Delta t}{2L}v_n
$$

对电容 $i=C\,dv/dt$，梯形法给出：

$$
i_{n+1}=G_C v_{n+1}+I_{hist}
$$

其中：

$$
G_C=\frac{2C}{\Delta t},\quad
I_{hist}=-\left(i_n+G_C v_n\right)
$$

符号方向取决于支路电流和节点电压参考方向；实现时必须与网络方程约定一致。固定步长、线性元件和固定拓扑下，$G_L$ 与 $G_C$ 不变，可复用导纳矩阵分解，这是梯形法在 EMTP 类程序中具有工程吸引力的重要原因。

## 稳定性与数值振荡

对测试方程 $\dot{x}=\lambda x$，梯形法稳定函数为：

$$
R(z)=\frac{1+z/2}{1-z/2},\quad z=\lambda\Delta t
$$

当 $\mathrm{Re}(z)<0$ 时，$|R(z)|<1$，因此梯形法 A 稳定。但在刚性极限：

$$
\lim_{z\to-\infty}R(z)=-1
$$

这说明高频刚性模态不会被衰减，而是可能以符号交替的方式延续。事件后若历史源携带切换前状态，误差序列可能表现为 $e_{n+1}\approx -e_n$，即数值振荡。

这种振荡不是物理不稳定，也不必然导致发散；但它会污染局部电压、电流、谐波和控制输入，尤其在电力电子、理想开关和刚性支路中明显。

## 事件处理与阻尼策略

常见处理包括：

- 事件插值：用 [[interpolation-method]] 定位开关、二极管换相或阈值交叉的步内时刻，而不是把事件推迟到下一个网格点。
- 历史项重初始化：事件后重建电感、电容的历史源，避免把切换前拓扑的历史信息带入切换后网络。
- 临界阻尼调整：事件附近临时使用 [[backward-euler]] 半步或子步，以阻尼梯形法保留的高频误差。
- 同时开关处理：对多个瞬时联动器件在同一物理时刻收敛，而不是逐个网格点切换。
- 改用 L 稳定主积分器：如 DIRK 或 TR-BDF2 类方法，但需要额外阶段计算和实现验证。

这些策略解决的是不同误差来源。仅仅“切换到后向欧拉”并不能修复事件定位错误或同时换相遗漏。

## 与后向欧拉的边界

| 维度 | 梯形法 | [[backward-euler]] |
|------|--------|--------------------|
| 阶数 | 二阶 | 一阶 |
| 稳定性 | A 稳定 | A 稳定且 L 稳定 |
| 高频数值阻尼 | 刚性极限不衰减 | 强阻尼 |
| 平滑区间精度 | 通常较好 | 相位和幅值阻尼较大 |
| 事件后风险 | 历史项污染和交替误差 | 真实高频衰减和一阶误差 |

因此，梯形法适合作为平滑区间的主积分器；后向欧拉适合事件点附近的阻尼和重初始化。具体组合需要通过目标算例验证。

## 代表性证据

[[accurate-time-domain-simulation-of-power-electronic-circuits]] 将梯形积分、后向欧拉、插值和同时开关机制组合起来分析功率电子不连续点。该来源支撑“梯形法事件后振荡需要事件定位和历史项修正共同处理”，但其量化结论绑定文中算例、步长和开关模型。

[[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] 说明在移频 EMT 大步长仿真中，传统梯形法虽二阶且 A 稳定，但变量突变时可能出现持续数值振荡，因此与 L 稳定隐式方法比较。该证据支撑梯形法的非 L 稳定边界，不应被写成梯形法不适合所有大步长场景。

[[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] 使用梯形积分离散特征值映射分析动态相量步长误差，说明即使变量被频移，暂态模态精度仍受积分步长影响。

## 适用边界

适合使用梯形法的场景包括：

- 线性或弱非线性网络的平滑暂态过程。
- 固定步长、固定导纳矩阵复用要求强的 EMTP 类计算。
- 目标频带能被当前步长充分解析，且事件处理机制可靠的仿真。

需要谨慎的场景包括：

- 理想开关、电力电子换相、故障插入和控制限幅频繁发生。
- 高频行波、开关纹波或局部尖峰是核心研究对象，但步长不足以解析。
- 历史项重置和事件定位未实现或未验证。

## 与相关页面的关系

- [[backward-euler]]：常用于梯形法事件后的阻尼和历史项重初始化。
- [[gear-method]]：BDF/Gear 方法提供另一类带阻尼的隐式多步积分。
- [[numerical-integration-error]]：说明截断误差、事件误差和数值振荡的来源。
- [[numerical-oscillation-suppression]]：包含梯形法振荡的处理策略。
- [[companion-circuit]]：梯形法在 EMT 中的主要实现形式。
- [[numerical-integration]]：更广义的数值积分方法入口。
