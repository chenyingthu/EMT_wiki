---
title: "数值积分 (Numerical Integration)"
type: method
tags: [numerical-integration, emt, trapezoidal-rule, dirk, implicit-integration, stability]
created: "2026-04-13"
updated: "2026-05-10"
---

# 数值积分 (Numerical Integration)

## 1. 物理背景与工程需求

### 为什么需要数值积分？

电力系统的电磁暂态过程由微分方程描述。但在数字计算机上，无法直接求解连续时间微分方程，只能一步一步地推进离散时间。

数值积分的作用就是：

$$
\text{已知 } x(t_n) \xrightarrow{\text{数值积分}} \text{求出 } x(t_{n+1})
$$

### 数值积分在 EMT 中的角色

数值积分不是孤立存在的——它与 [[companion-circuit]] 和 [[nodal-analysis]] 紧密耦合：

```text
数值积分（微分方程 → 差分方程）
    ↓
伴随电路（差分方程 → 诺顿等效：G_eq + I_hist）
    ↓
节点分析（诺顿等效 → 全局线性方程组 Y_n · v = i）
```

积分公式的选择直接决定了：
- 等效电导 $G_{eq}$ 的值（梯形法 vs 后向欧拉完全不同）
- 历史电流源的递推方式
- 数值稳定性的边界
- 是否需要特殊的开关后处理（如 CDA）

EMT 仿真的特殊性在于：它不仅要求积分公式能处理刚性方程（时间常数相差几个数量级），还要能处理频繁发生的开关、故障等非连续事件。

---

## 2. 数学描述

### 核心分类：显式 vs 隐式

对一阶 ODE $\dot{x} = f(t, x)$，数值积分方法首先分为两类：

- **显式**：$x_{n+1}$ 由已知量直接算出，计算量小但条件稳定
- **隐式**：$x_{n+1}$ 出现在方程两边，需要求解方程组，但稳定区域大

EMT 仿真中几乎全部使用隐式方法，因为电网的刚性特性使显式方法的步长受限到无法接受的程度。

### 三种核心方法

**梯形法（Trapezoidal Rule）：**

$$
x_{n+1} = x_n + \frac{h}{2}[f(t_n, x_n) + f(t_{n+1}, x_{n+1})]
$$

二阶精度、A-稳定。这是 EMT 中使用最广泛的积分公式，因为它能形成简单的伴随电路。但 A-稳定的代价是 $R(z) \to -1$（见下文），突变后可能产生数值振荡。

**后向欧拉（Backward Euler）：**

$$
x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})
$$

一阶精度，但 L-稳定。后向欧拉在开关突变后能快速衰减高频分量，但作为长期主积分器时会过度阻尼物理暂态。

**2S-DIRK：**

$$
\begin{aligned}
x_{n+\gamma} &= x_n + h[\gamma f(t_n, x_n) + \gamma f(t_{n+\gamma}, x_{n+\gamma})] \\
x_{n+1} &= x_{n+\gamma} + h[(1-\gamma) f(t_{n+\gamma}, x_{n+\gamma}) + \gamma f(t_{n+1}, x_{n+1})]
\end{aligned}
$$

$\gamma = 1 \pm \sqrt{2}/2$ 时二阶 L-稳定。综合了梯形法的精度和后向欧拉的阻尼特性，代价是每步两次隐式求解。

### 稳定性函数

对测试方程 $\dot{x} = \lambda x$（$z = \lambda h$），各个方法的稳定性函数 $R(z)$：

| 方法 | $R(z)$ | $z \to -\infty$ | 稳定类型 |
|------|--------|-----------------|----------|
| 梯形法 | $(1+z/2)/(1-z/2)$ | $-1$ | A-稳定（非 L-稳定） |
| 后向欧拉 | $1/(1-z)$ | $0$ | L-稳定 |
| 2S-DIRK | 取决于 $\gamma$ | $0$ | L-稳定 |

梯形法 $R(z) \to -1$ 意味着高频模态不会被衰减，而是步间换号——这是数值振荡的数学根源。后向欧拉 $R(z) \to 0$ 意味着高频模态一步内被完全衰减。

---

## 3. 计算模型与离散化

### 从微分方程到伴随电路

积分公式直接决定了伴随电路的形式。以电容 $i = C\,dv/dt$ 为例：

$$
\begin{array}{c|cc}
\text{积分方法} & \text{等效电导 } G_{eq} & \text{特性} \\ \hline
\text{后向欧拉} & C/\Delta t & \text{L-稳定，无数值振荡} \\
\text{梯形法} & 2C/\Delta t & \text{A-稳定，可能有数值振荡} \\
\text{Gear-2} & 3C/(2\Delta t) & \text{L-稳定，精度较低} \\
\text{2S-DIRK} & \text{取决于 } \gamma & \text{L-稳定，二阶}
\end{array}
$$

同一物理元件用不同积分公式得到不同的 $G_{eq}$，进而影响节点导纳矩阵的条件数。这是选择积分公式时需要考虑的工程因素：$G_{eq}$ 过大会恶化矩阵条件数。

### 步长约束

$
\Delta t$ 的选择受限于：
- **奈奎斯特频率**：$\Delta t < 1/(2f_{max})$，否则无法正确表示最高频分量
- **开关事件精度**：PWM 载波周期内至少 10-20 步
- **实时仿真**：每步计算时间必须小于 $\Delta t$

---

## 4. 实现方法与算法细节

### CDA（Critical Damping Adjustment）

CDA 是 EMTP 中最经典的数值振荡抑制技术：

```text
正常步进：... → 梯形法 → 梯形法 → 梯形法 → ...
突变时刻：... → 梯形法 → [开关动作] → 后向欧拉(1步) → 梯形法 → ...
```

检测到突变后自动切换为后向欧拉一步，利用其 L-稳定特性一步衰减高频分量，然后恢复梯形法。

### 多步法的启动问题

Gear-2、BDF 等多步法需要前 $k$ 步的历史值才能启动：
- 仿真开始时需要用单步法（如后向欧拉）启动
- 步长变化后也需要重启
- 开关事件后历史值可能不再适用

这使多步法在开关频繁的电力电子仿真中不如单步法灵活。

### 刚性系统的步长困境

EMT 系统中常见的时间常数跨度极大（从 $\mu$s 的开关暂态到 100ms 的机电振荡）。显式方法要求步长受限于最快动态，而隐式方法可以用接近最慢感兴趣动态来选步长。这正是隐式方法在 EMT 中占主导地位的根本原因。

---

## 5. 适用边界与失效模式

### 什么条件下好用？

- 梯形法是 EMT 中精度/效率的最佳折中，适合绝大多数场景
- 后向欧拉适合事件后临时过渡（CDA 模式）
- 2S-DIRK 适合需要 L-稳定又希望二阶精度的场景
- 隐式方法的 A-/L-稳定特性使大步长在刚性系统中可行

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 开关后数值振荡 | 波形出现交替毛刺 | 梯形法 $R(z) \to -1$，高频不衰减 | CDA 或后向欧拉 |
| 大步长精度不足 | 幅值和相位误差明显 | 梯形法采样不足 | 减小步长或高阶方法 |
| 多步法启动发散 | 仿真初始阶段失败 | 缺乏足够历史步 | 后向欧拉启动 |
| 非线性迭代发散 | 隐式方程不收敛 | 初始猜测不好 | 阻尼牛顿法 |
| 变步长后误差膨胀 | 精度骤降 | 历史值与新步长不匹配 | 重启积分器 |

### 工程经验值

- 默认选择：梯形法 + CDA
- 步长选系统最快暂态周期的 1/20 ~ 1/50
- 2S-DIRK 典型 $\gamma = 1 - \sqrt{2}/2 \approx 0.2929$
- 实时仿真：梯形法 + 固定步长最保险

---

## 6. 应用说明

考虑一阶 RC 电路零输入响应：$RC \cdot dv/dt + v = 0$，$v(0) = V_0$。解析解 $v(t) = V_0 e^{-t/(RC)}$。

梯形法离散：

$$
v_{n+1} = \frac{1 - h/(2RC)}{1 + h/(2RC)} v_n
$$

$h \ll RC$ 时 $v_{n+1} \approx (1 - h/(RC)) v_n$，接近一阶近似。$h$ 较大时递推会偏离解析解。

取 $R=1k\Omega$，$C=1\mu\text{F}$（$\tau = 1$ms），$h = 0.1$ms 计算前 10 步，与 $V_0 e^{-t/RC}$ 对比即可评估梯形法的实际误差。

如需验证数值振荡：在上例中 $t = \tau$ 处将电容短路，观察梯形法是否出现步间交替的电流波形。

---

## 7. 延伸阅读

### 核心参考文献

- [[numerical-integration-by-the-2-stage-diagonally]] — 2S-DIRK 在 EMT 中的伴随电路推导和稳定性分析
- [[supplementary-techniques-for-2s-dirk-based-emt-simulations]] — 2S-DIRK 的补充实现技术
- [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] — 三阶段隐式积分在移频 EMT 中的应用
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — 系统比较不同积分公式对精度和效率的影响
- [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn]] — 紧凑格式在 EMT 数值积分中的应用

### 相关页面

- [[trapezoidal-rule]] — 梯形法的具体推导和特性
- [[backward-euler]] — 后向欧拉的数值特性
- [[gear-method]] — Gear 法的多步特性
- [[companion-circuit]] — 数值积分如何转化为伴随电路
- [[stiff-system-handling]] — 刚性系统的处理策略
- [[numerical-oscillation-suppression]] — 数值振荡抑制方法
