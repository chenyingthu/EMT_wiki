---
title: "后向欧拉法 (Backward Euler Method)"
type: method
tags: [backward-euler, integration, numerical, l-stable, implicit, stiff-system-handling]
created: "2026-05-02"
---

# 后向欧拉法 (Backward Euler Method)

## 概述

后向欧拉法（Backward Euler Method）是一阶隐式数值积分方法，也是 [[gear-method]] 中 BDF1 的形式。它用下一时刻的导数近似当前步积分，因此具有强数值阻尼和 L 稳定性。在 EMT 中，后向欧拉法常用于刚性模态阻尼、开关事件后的历史项重初始化、临界阻尼调整，以及某些需要稳定优先于波形高阶精度的子步骤。

后向欧拉法不应被描述为“更准确”的通用 EMT 方法。它的核心优势是稳定和阻尼；主要代价是一阶截断误差和对真实高频分量的人工衰减。

## 核心公式

对常微分方程

$$
\dot{\mathbf{x}}=f(t,\mathbf{x})
$$

后向欧拉离散为：

$$
\mathbf{x}_{n+1}
=
\mathbf{x}_n+\Delta t\,f(t_{n+1},\mathbf{x}_{n+1})
$$

残差形式为：

$$
\mathbf{F}(\mathbf{x}_{n+1})
=
\mathbf{x}_{n+1}-\mathbf{x}_n-\Delta t f(t_{n+1},\mathbf{x}_{n+1})
=0
$$

线性系统可直接形成代数方程；非线性元件通常需要 [[newton-raphson-method]] 或等价迭代求解。

局部截断误差为 $O(\Delta t^2)$，全局误差为 $O(\Delta t)$。因此，步长减小仍是精度控制的必要手段，即使该方法在稳定性意义上允许较大步长。

## EMT 伴随电路

对电感 $v=L\,di/dt$，后向欧拉给出：

$$
v_{n+1}=L\frac{i_{n+1}-i_n}{\Delta t}
$$

可写成 Norton 形式：

$$
i_{n+1}=G_L v_{n+1}+I_{hist},\quad
G_L=\frac{\Delta t}{L},\quad I_{hist}=i_n
$$

对电容 $i=C\,dv/dt$，后向欧拉给出：

$$
i_{n+1}=C\frac{v_{n+1}-v_n}{\Delta t}
$$

即：

$$
i_{n+1}=G_C v_{n+1}+I_{hist},\quad
G_C=\frac{C}{\Delta t},\quad I_{hist}=-\frac{C}{\Delta t}v_n
$$

这些伴随模型与 [[nodal-analysis]] 结合后形成节点导纳矩阵。若 $\Delta t$ 固定且元件参数不变，线性储能元件的等效导纳保持常数，有利于矩阵分解复用。

## 稳定性与数值阻尼

对测试方程 $\dot{x}=\lambda x$，后向欧拉稳定函数为：

$$
R(z)=\frac{1}{1-z},\quad z=\lambda\Delta t
$$

当 $\mathrm{Re}(z)<0$ 时，$|R(z)|<1$，因此方法 A 稳定。并且：

$$
\lim_{z\to-\infty}R(z)=0
$$

所以后向欧拉也是 L 稳定。物理含义是，刚性极限中的快速衰减模态会在离散系统中被强烈阻尼。这可以抑制 [[trapezoidal-rule]] 在不连续点后可能保留的交替误差，但也可能把真实高频暂态一起衰减。

因此，后向欧拉适合“阻尼数值误差”的步骤，而不适合把高频波形精度作为主要目标的长期主积分器，除非该频段已经不在研究目标内。

## 在 EMT 中的典型用法

### 开关事件后的重初始化

固定步长 EMT 中，开关时刻往往落在网格点之间。若直接在网格点切换拓扑，历史源可能携带切换前网络信息，导致数值振荡或相位误差。常见处理是：

1. 用 [[interpolation-method]] 定位事件时刻。
2. 在事件时刻更新拓扑或开关状态。
3. 使用后向欧拉半步或若干子步重建历史源。
4. 恢复 [[trapezoidal-rule]] 或其他主积分器。

这种用法体现的是“历史项重初始化”，不是后向欧拉本身能自动解决所有开关误差。

### 临界阻尼调整

临界阻尼调整（Critical Damping Adjustment, CDA）常把事件附近的积分从梯形法临时切换为后向欧拉，以阻尼高频数值模态。CDA 的有效性依赖事件检测、插值回退和历史项更新；若突变来自控制限幅、隐含二极管换相或未检测的非线性工作点变化，单纯切换积分器可能不足。

### 刚性子系统

在含快慢时间尺度的系统中，后向欧拉可以稳定推进快速衰减模态。但若快模态的波形本身是研究对象，例如雷电波头、电力电子开关纹波或行波反射，则不能仅凭 L 稳定性放大步长。

## 与梯形法的边界

| 维度 | 后向欧拉 | [[trapezoidal-rule]] |
|------|----------|----------------------|
| 阶数 | 一阶 | 二阶 |
| 稳定性 | A 稳定且 L 稳定 | A 稳定但非 L 稳定 |
| 高频数值阻尼 | 强 | 刚性极限不衰减 |
| 事件后表现 | 适合重初始化和阻尼 | 可能产生交替数值误差 |
| 主要风险 | 衰减真实高频、相位滞后 | 不连续点后振荡和历史项污染 |

实际 EMT 程序常混合使用两者：平滑区间用梯形法保持二阶精度，事件点附近用后向欧拉或相关 L 稳定方法做阻尼和重初始化。

## 代表性证据

[[accurate-time-domain-simulation-of-power-electronic-circuits]] 讨论了固定步长功率电子 EMT 中梯形积分、后向欧拉重初始化、事件插值和同时开关的组合。该来源支撑“后向欧拉常用于不连续点后的历史项重置和振荡抑制”，但其具体量化结果绑定文中 RL、STATCOM 和变换器算例，不应外推为所有拓扑通用。

[[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] 将 L 稳定隐式积分用于移频 EMT 大步长仿真，说明大步长场景中数值阻尼机制很重要。该来源的主方法是 3S-SDIRK，不应被写成后向欧拉优于所有高阶方法。

[[numerical-integration-methods]] 给出后向欧拉、梯形法、BDF/Gear 和 DIRK 在稳定性、阻尼和事件处理上的比较，可作为本页的综述入口。

## 适用边界

适合使用后向欧拉的情况包括：

- 开关事件、故障插入或拓扑突变后的短暂重初始化。
- 需要抑制非物理高频数值误差的刚性子步骤。
- 对精度要求主要集中在低频或慢变量上的大步长近似。

不宜单独依赖后向欧拉的情况包括：

- 需要二阶或更高阶波形精度的长时间主仿真。
- 真实高频暂态、行波波头、开关纹波或谐波幅相是研究对象。
- 事件时刻未被准确定位；此时后向欧拉只能阻尼误差，不能修正事件时间偏差。

## 与相关页面的关系

- [[trapezoidal-rule]]：常规 EMT 主积分器之一，后向欧拉常作为事件附近补充。
- [[gear-method]]：后向欧拉是 BDF1。
- [[numerical-integration-error]]：解释一阶误差、阻尼误差和事件误差。
- [[numerical-oscillation-suppression]]：后向欧拉是数值振荡抑制手段之一。
- [[companion-circuit]]：后向欧拉在 EMT 中通过伴随电路进入网络方程。
