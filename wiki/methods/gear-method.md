---
title: "吉尔方法 (Gear Method)"
type: method
tags: [gear-method, numerical-integration, stiff-system, multistep, ode-solver, bdf-method]
created: "2026-05-02"
updated: "2026-05-03"
---

# 吉尔方法 (Gear Method)


```mermaid
graph TD
    N0[吉尔方法 (Gear Method)]
    N1[固定阶 BDF：例如 BDF2，…]
    N0 --> N1
    N2[变阶变步长 Gear：根据局部误…]
    N0 --> N2
    N3[TR-BDF2：先用梯形/中间阶…]
    N0 --> N3
    N4[ImEx Gear：把线性刚性部…]
    N0 --> N4
```


## 概述

吉尔方法（Gear Method）在 EMT 语境中通常指向后微分公式（Backward Differentiation Formula, BDF）一类隐式线性多步积分法。它用多个历史步的状态近似当前导数，并在当前步隐式求解微分-代数方程。与 [[trapezoidal-rule]] 相比，BDF/Gear 方法通常引入更强的数值阻尼；与 [[backward-euler]] 相比，高阶 BDF 可提高平滑区间内的精度，但会带来启动、事件后重启和稳定域缩小问题。

Gear 方法不应被写成 EMT 的通用替代积分器。它更适合刚性、事件不太频繁、状态历史连续的子问题；对含大量理想开关、电力电子不连续和固定导纳矩阵复用要求很强的 EMT 网络，需要额外处理历史项、阶数切换和事件定位。

## EMT 中的作用

在 EMT 和相关电路仿真中，Gear/BDF 方法主要承担三类角色：

- 刚性系统积分：当快速衰减模态限制显式步长，而研究目标是慢变量时，隐式 BDF 可减弱稳定性约束。
- 数值阻尼控制：BDF1 即 [[backward-euler]]，具有强阻尼；BDF2 也比梯形法更能衰减高频数值误差。
- 大步长或包络仿真候选：在 [[large-timestep-simulation]]、移频 EMT 或动态相量框架中，BDF/TR-BDF2 常作为与 DIRK、梯形法比较的隐式积分器。

其工程代价是多步历史依赖。每次拓扑突变、限幅、故障插入或模型切换后，都可能需要降阶、重建历史项或用单步隐式法重新启动。

## 核心公式

对初值问题

$$
\dot{\mathbf{x}}=f(t,\mathbf{x})
$$

$k$ 步 BDF 的典型形式为：

$$
\sum_{j=0}^{k}\alpha_j\mathbf{x}_{n+1-j}
=
\Delta t\,\beta_0 f(t_{n+1},\mathbf{x}_{n+1})
$$

其中 $\mathbf{x}_{n+1}$ 同时出现在左端和右端，因此需要解隐式代数方程。若写成残差形式：

$$
\mathbf{F}(\mathbf{x}_{n+1})
=
\sum_{j=0}^{k}\alpha_j\mathbf{x}_{n+1-j}
-
\Delta t\,\beta_0 f(t_{n+1},\mathbf{x}_{n+1})
=0
$$

非线性系统通常用 [[newton-raphson-method]] 求解。在线性 EMT 网络中，储能元件离散后仍可进入 [[companion-circuit]]，但历史源会依赖多个历史步，而不是只依赖上一时刻。

常用低阶形式为：

$$
\text{BDF1:}\quad \mathbf{x}_{n+1}-\mathbf{x}_n
=
\Delta t f(t_{n+1},\mathbf{x}_{n+1})
$$

$$
\text{BDF2:}\quad
\frac{3}{2}\mathbf{x}_{n+1}-2\mathbf{x}_{n}
+\frac{1}{2}\mathbf{x}_{n-1}
=
\Delta t f(t_{n+1},\mathbf{x}_{n+1})
$$

等价地，BDF2 也常写成：

$$
\mathbf{x}_{n+1}-\frac{4}{3}\mathbf{x}_{n}
+\frac{1}{3}\mathbf{x}_{n-1}
=
\frac{2}{3}\Delta t f(t_{n+1},\mathbf{x}_{n+1})
$$

## 稳定性与数值阻尼

对测试方程 $\dot{x}=\lambda x$，线性多步法的稳定性由特征根决定。BDF1 和 BDF2 是 A 稳定方法；更高阶 BDF 的稳定域不再覆盖整个左半平面，因此不能简单认为“阶数越高越稳”。

数值阻尼是 Gear 方法在 EMT 中的核心差异。BDF1 的稳定函数为：

$$
R(z)=\frac{1}{1-z},\quad z=\lambda\Delta t
$$

当 $z\to-\infty$ 时 $R(z)\to0$，高频刚性模态被快速阻尼。BDF2 对高频模态也有阻尼，但其多步特征根需要结合历史误差分析。相比之下，[[trapezoidal-rule]] 在刚性极限下趋向 $-1$，可能保留交替误差。

这种阻尼既是优点也是风险：它可以抑制非物理数值振荡，也可能衰减真实高频暂态。因此 Gear 方法的“稳定”不等于“精确”，步长仍需由目标频带和误差容差约束。

## 变体与实现策略

常见实现包括：

- 固定阶 BDF：例如 BDF2，用于历史连续、模型变化较少的子系统。
- 变阶变步长 Gear：根据局部误差估计调整阶数和步长，适用于一般 ODE/DAE 求解器；在固定步长 EMT 程序中实现成本较高。
- TR-BDF2：先用梯形/中间阶段，再用 BDF2 终结，常作为兼顾二阶精度和阻尼的单步复合方法。
- ImEx Gear：把线性刚性部分隐式处理，把部分开关函数或控制项显式处理；需要单独验证稳定性和误差。

对 EMT 网络而言，若目标是固定导纳矩阵复用，则应检查 BDF 系数和步长是否使等效导纳在仿真过程中保持常数。变步长或变阶虽然有利于误差控制，但会增加矩阵重构和历史项管理成本。

## 适用边界

较适合的场景包括：

- 刚性但事件不频繁的电磁-机电混合模型。
- 平滑区间内的大步长包络模型或 [[dynamic-phasor]] 模型。
- 需要比梯形法更强数值阻尼、但又希望高于一阶精度的子问题。

需要谨慎的场景包括：

- 高频开关密集的电力电子详细模型；事件后多步历史不再一致。
- 需要严格保留波头、高频振荡或电磁行波细节的暂态。
- 每步都发生拓扑或控制限幅切换的仿真；Gear 的历史项可能频繁失效。
- 只凭大步长稳定性判定结果可信的场景；精度仍需与小步长参考或解析解比较。

## 代表性证据

[[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] 将 TR、2S-DIRK、TR-BDF2 和 3S-SDIRK 放在移频 EMT 的大步长积分背景下比较。该来源支撑“BDF 类方法常作为大步长隐式积分候选”，但其主要贡献是 3S-SDIRK，不应把其中关于大步长效率的论证直接归功于普通 Gear 方法。

[[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] 说明动态相量或频移模型不会消除系统固有暂态模态，步长仍受特征值和目标暂态精度约束。该证据可用于限制 Gear/大步长叙述：频移或隐式稳定性不能自动保证暂态准确。

[[numerical-integration-methods]] 汇总了梯形法、后向欧拉、BDF/Gear、DIRK 和指数积分在 EMT 中的稳定性和阻尼差异，可作为本页的综述入口。

## 与相关页面的关系

- [[backward-euler]]：BDF1，是 Gear 方法族的最低阶成员。
- [[trapezoidal-rule]]：二阶 A 稳定但非 L 稳定；与 BDF 的主要差异在数值阻尼和历史依赖。
- [[numerical-integration-error]]：用于解释 Gear 的截断误差、历史误差和事件后误差传播。
- [[stiff-system-handling]]：Gear 方法常用于刚性问题，但不是唯一选择。
- [[large-timestep-simulation]]：大步长仿真可使用 BDF 类方法，但必须绑定模型简化和验证边界。

## 开放问题

- 在固定步长 EMT 中，Gear 历史项如何与开关事件、插值回退和同时换相机制一致，需要具体算法验证。
- BDF 阻尼对真实高频模态的影响应通过频域误差或小步长参考解量化。
- 变阶变步长 Gear 与实时仿真、固定导纳矩阵和并行分区求解之间存在工程权衡，不能只按阶数评价。
