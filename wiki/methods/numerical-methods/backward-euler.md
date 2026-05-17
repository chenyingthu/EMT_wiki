---
title: "后向欧拉法 (Backward Euler Method)"
type: method
tags: [backward-euler, gear-method, bdf, numerical-integration, l-stable, cda, numerical-oscillation]
created: "2026-05-02"
updated: "2026-05-17"
---

# 后向欧拉法 (Backward Euler Method)

## 1. 物理背景与工程需求

### 为什么需要后向欧拉法？

后向欧拉法（Backward Euler, BE）是最简单的一阶隐式 L-稳定积分方法，也是 BDF1 的形式。在 EMT 仿真中，它从不作为主积分器使用，而是作为**事件后临时过渡**的标准工具。

[[trapezoidal-rule]] 是 EMT 默认的主积分器（二阶 A-稳定），但其 $R(z) \to -1$ 的特性在开关/故障事件后会产生持续数值振荡。后向欧拉的 $R(z) \to 0$ 意味着高频数值模态一步内被完全衰减——这正是 CDA（Critical Damping Adjustment）机制选择 BE 作为临时替换的原因。

后向欧拉法的定位：
- **不是**：长期主积分器（一阶精度，过度阻尼真实高频）
- **而是**：事件后 1-2 步的临时过渡、CDA 组合、刚性子系统的稳定推进

### 后向欧拉法在 EMT 方法体系中的位置

数值积分方法按稳定性分类：

| 方法 | 精度阶数 | A-稳定 | L-稳定 | EMT 定位 |
|------|----------|--------|--------|----------|
| 梯形法 (TR) | 二阶 | 是 | **否** | 默认主积分器 |
| **后向欧拉 (BE)** | **一阶** | **是** | **是** | **CDA 过渡、事件后阻尼** |
| BDF2 | 二阶 | 是 | 是 | 变阶变步长 Gear |
| 2S-DIRK | 二阶 | 是 | 是 | 高质量仿真（第一阶段等价于 BE） |
| TR-BDF2 | 二阶 | 是 | 是 | BDF 类单步复合方法 |

BE 是 BDF 族中唯一 A-稳定兼 L-稳定的一阶方法（BDF1 = BE）。它的 L-稳定性使其在高频区域（$z \to -\infty$）完全不产生数值振荡，这是 EMT 中消除开关事件后虚假振荡的理论基础。

---

## 2. 数学描述

### 公式

对一阶 ODE $\dot{x} = f(t, x)$，后向欧拉法的递推公式为：

$$x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})$$

用下一时刻的导数近似当前步的积分。局部截断误差 $O(h^2)$，全局误差 $O(h)$。

### 稳定性函数

对测试方程 $\dot{x} = \lambda x$（$z = \lambda h$）：

$$R(z) = \frac{1}{1 - z}$$

关键性质：
- $z \to 0$：$R(z) \to 1$（低频准确）
- $z \to -\infty$：$R(z) \to 0$（高频完全衰减——L-稳定的核心）
- $z = j\omega$：$|R(j\omega)| = 1/\sqrt{1 + (\omega h)^2} < 1$（虚轴上有阻尼）

**BE 与 TR 的稳定性对比**：

$$R_{\text{TR}}(z) = \frac{1 + z/2}{1 - z/2} \xrightarrow{z \to -\infty} -1 \quad \text{（步间交替振荡）}$$

$$R_{\text{BE}}(z) = \frac{1}{1 - z} \xrightarrow{z \to -\infty} 0 \quad \text{（高频完全衰减）}$$

这就是数值振荡的数学根源：梯形法在 $z \to -\infty$ 时 $R(z) \to -1$，使高频分量在相邻步之间交替换号但不衰减；后向欧拉的 $R(z) \to 0$ 使高频分量一步内被完全阻尼。

### A-稳定 vs L-稳定

| 性质 | 含义 | 后向欧拉 | 梯形法 |
|------|------|----------|--------|
| A-稳定 | $\text{Re}(z) < 0$ 时 $|R(z)| \leq 1$ | 是 | 是 |
| L-稳定 | A-稳定且 $z \to -\infty$ 时 $R(z) \to 0$ | **是** | **否** |

后向欧拉同时满足 A-稳定和 L-稳定。$R(z) \to 0$ 意味着高频数值模态一步内被完全阻尼——不会出现梯形法的步间交替振荡。

### 后向欧拉与 BDF 族的关系

后向欧拉法是后向微分公式（Backward Differentiation Formula, BDF）族的第一个成员（BDF1）：

$$\text{BDF-}k: \quad \sum_{j=0}^{k} \alpha_j x_{n+1-j} = h \beta_0 f(t_{n+1}, x_{n+1})$$

BDF 系数表（常数步长）：

| BDF 阶数 | $\alpha_0$ | $\alpha_1$ | $\alpha_2$ | $\beta_0$ |
|----------|-----------|-----------|-----------|-----------|
| BDF1 (BE) | $-1$ | $1$ | — | $1$ |
| BDF2 | $-3/2$ | $2$ | $-1/2$ | $1$ |
| BDF3 | $-11/6$ | $3$ | $-3/2$ | $1/3$ |
| BDF4 | $-25/12$ | $4$ | $-3$ | $4/3$ |

BDF1（BE）和 BDF2 同时满足 A-稳定和 L-稳定；BDF3+ 不再 A-稳定，实际 EMT 中主要使用 BDF2。

---

## 3. 计算模型与离散化

### 伴随电路形式

对电感 $v = L\,di/dt$，后向欧拉离散：

$$i_{n+1} = i_n + \frac{h}{L} v_{n+1}$$

整理为诺顿等效 $i_{n+1} = G_{\text{eq}} v_{n+1} + I_{\text{hist}}$：

$$G_{\text{eq},L} = \frac{h}{L}, \quad I_{\text{hist},L} = i_n$$

对电容 $i = C\,dv/dt$：

$$i_{n+1} = \frac{C}{h} v_{n+1} - \frac{C}{h} v_n$$

诺顿等效：

$$G_{\text{eq},C} = \frac{C}{h}, \quad I_{\text{hist},C} = -\frac{C}{h} v_n$$

### 伴随电路等效电导对比表

| 元件 | 梯形法 $G_{\text{eq}}$ | 后向欧拉 $G_{\text{eq}}$ | 比值（BE/TR） |
|------|------------------------|--------------------------|---------------|
| 电感 | $\Delta t/2L$ | $\Delta t/L$ | **2:1** |
| 电容 | $2C/\Delta t$ | $C/\Delta t$ | **1:2** |

后向欧拉的电容等效导纳是梯形法的一半，电感等效导纳是梯形法的 2 倍。这会改变节点导纳矩阵的条件数——BE 的等效阻抗更小（对电容而言），数值阻尼更强。

### 与其它隐式方法的对比

| 方法 | 精度阶数 | L-稳定 | 每步求解次数 | EMT 定位 |
|------|----------|--------|-------------|----------|
| 梯形法 | 二阶 | **否** | 1 | 默认主积分器 |
| 后向欧拉 | 一阶 | **是** | 1 | CDA 过渡、事件后阻尼 |
| BDF2 | 二阶 | 是 | 1 | 多步法场景 |
| 2S-DIRK | 二阶 | 是 | 2 | 高质量仿真（第一阶段等价于 BE） |
| TR-BDF2 | 二阶 | 是 | 2 | BDF 类单步复合 |

2S-DIRK 的第一阶段在 $\gamma = 1 - 1/\sqrt{2}$ 处等价于一个后向欧拉步（Noda, 2014），说明 BE 可作为高阶 L-稳定方法的构建块。

---

## 4. 实现方法与算法细节

### CDA（Critical Damping Adjustment）

CDA 是 Marti 和 Lin 于 1989 年提出的经典方法，也是 BE 在 EMT 中最核心的应用场景：

```text
正常步进：... 梯形法 -> 梯形法 -> 梯形法 -> ...
突变时刻：... 梯形法 -> [开关动作] -> BE(半步) -> BE(半步) -> 梯形法 -> ...
```

CDA 的机制（Marti, 2004）：
1. 检测到不连续事件（电感电流开断、电容电压突加等）
2. 将当前步长拆为两个 $\Delta t/2$ 半步
3. 每个半步用后向欧拉更新伴随电路的历史项
4. 两个半步完成后恢复梯形法

BE 在两个半步内提供完全临界阻尼，且 CDA 只改变事件附近的局部响应，不改变全局梯形法的低频精度。

### TR-BE 组合方法族（Nzale et al., 2021）

Nzale 等系统分析了 TR-BE 组合的八种变体，核心区别在于事件定位（Interpolation, I）和同时换相（Simultaneous Switching, SS）的组合顺序：

| 方法 | 事件定位 | 同时换相 | 精度 | 计算代价 |
|------|----------|----------|------|----------|
| TR_BE | 无 | 无 | 最低 | 无额外求解 |
| TR_BE_I | 线性插值 | 无 | 中等 | 每次事件 1 次额外求解 |
| TR_BE_SS | 无 | 有 | 中等 | 每次事件 1 次额外求解 |
| TR_BE_I_SS_p | 先 SS 后插值 | 有 | 较高（有额外误差） | 每次事件 1-2 次求解 |
| TR_BE_SS_I | 先 SS 后插值 | 有 | **最高** | 每次事件 2 次额外求解 |
| TR_BE_I_SS_m | 先插值后 SS | 有 | **最高** | 每次事件 2 次额外求解 |
| TR_I_SS_m_BE | 先插值后 SS | 有 | **最高** | 每次事件 2 次额外求解 |
| TR_DICR | 插值+去噪 | 无 | 较高 | 每次事件 2 次额外求解 |

**Nzale 2021 量化数据**（RL 电路，$\Delta t = 10\,\mu$s）：

| 方法组合 | 振荡幅值降低 | 额外计算代价 |
|----------|-------------|-------------|
| 仅 TR + BE（CDA） | 中等 | 无 |
| TR + BE + 线性插值（TR_BE_I） | **约 3000 倍** | 每次事件 1 次额外求解 |
| TR + BE + 插值 + 外推重初始化（TR_BE_I_SS_m） | **约 3000 倍** | 每次事件 2 次额外求解 |

仅靠 TR+BE 切换（CDA）能提供中等程度的振荡抑制，但若要显著降低振荡幅值，需要配合**事件定位插值**。BE 只解决 $R(z) \to -1$ 造成的历史项振荡，不解决事件定位误差（开关时刻落在网格之间）。

**Nzale 2021 STATCOM 算例**（6 IGBT，PWM 1980 Hz，100 ms 仿真）：

| 方法 | 1 μs | 2 μs | 5 μs | 10 μs |
|------|------|------|------|-------|
| TR_BE（BE 单独） | 误差最大 | 误差最大 | 误差最大 | 误差最大 |
| TR_BE_I | 较低 | 较低 | 中等 | 中等 |
| TR_BE_I_SS_m | **最低，不随 Δt 变化** | **最低** | **最低** | **最低** |
| TR_I_SS_m_BE | 与 TR_BE_I_SS_m 重合 | 与 TR_BE_I_SS_m 重合 | 与 TR_BE_I_SS_m 重合 | 与 TR_BE_I_SS_m 重合 |

关键发现：**TR_BE_I_SS_m 和 TR_I_SS_m_BE 的相对 RMS 误差（RRE）不随步长显著变化**，这意味着可以使用更大的时间步长而不损失精度。

### BE 在事件处理中的局限性

Nzale et al. (2021) 的研究表明：

| 方法组合 | 振荡幅值降低 | 额外计算代价 |
|----------|-------------|-------------|
| 仅 TR + BE（无插值） | 中等 | 无 |
| TR + BE + 线性插值 | 约 3000 倍 | 每次事件 1 次额外求解 |
| TR + BE + 插值 + 外推重初始化 | 约 3000 倍 | 每次事件 2 次额外求解 |

仅靠 TR+BE 切换（CDA）能提供中等程度的振荡抑制，但若要显著降低振荡幅值，需要配合**事件定位插值**。BE 只解决 $R(z) \to -1$ 造成的历史项振荡，不解决事件定位误差（开关时刻落在网格之间）。

### 启动与重启

后向欧拉作为单步法，不需要多步法所需的历史值启动。这使它在以下场景中特别方便：
- 仿真开始时需要初始化
- 步长变化后积分器重启
- CDA 中与梯形法的来回切换

---

## 5. 适用边界与失效模式

### 什么条件下好用？

- 开关/故障事件后 1-2 步的临时过渡（CDA 标准用法）
- 需要快速阻尼高频数值振荡的历史项重初始化
- 刚性子系统中推进快速衰减模态（稳定但不必精确跟踪波形）
- 对精度要求集中在低频或慢变量的大步长近似
- 作为 2S-DIRK 第一阶段的构建块

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 长期主积分器 | 波形幅值衰减、相位滞后过大 | 一阶截断误差 + 过度高频阻尼 | 恢复梯形法或 2S-DIRK |
| 真实高频暂态研究 | 行波波头、开关纹波被抹平 | BE 的 $R(z) \to 0$ 无差别衰减所有高频 | 改用梯形法或高阶方法 |
| 未事件定位仅靠 BE | 振荡降低但仍有明显误差 | 只处理了历史项污染，未处理事件定位误差 | 配合插值定位（Nzale 方案） |
| 谐振电路长期仿真 | 阻尼过大，Q 值偏低 | BE 在虚轴上也有数值阻尼 | 不要单独用 BE 做长时间谐振分析 |
| 非线性迭代中 | 收敛速度受限 | 一阶精度导致初值估计偏差大 | CDA 窗口内使用即可 |
| STATCOM 等多开关场合 | TR_BE_I_SS_m 表现最佳 | 需要同时处理事件定位和同时换相 | 选用 TR_BE_I_SS_m 或 TR_I_SS_m_BE |

### 工程经验值

- BE 的 CDA 窗口通常为 1 步（拆为 2 个 $\Delta t/2$ 半步），不宜延长
- CDA 检测阈值：$|x_{n+1} - x_n| > K \cdot \max(|x_n|, |x_{n-1}|)$，$K$ 通常取 3-5
- BE 单独作为主积分器只在极少数特殊场景下使用（如某些实时仿真的最简积分器）
- 在 EMTP 类软件中，用户通常不需要手动介入 CDA 切换
- 对于需要高精度的事件后响应，推荐 TR_BE_I_SS_m（先插值定位事件，再用同时换相检测，最后用两个 BE 半步阻尼），其误差不随步长变化

---

## 6. 应用案例

### RL 电路：BE 与 TR 的振荡抑制对比

考虑 RL 电路 $L = 50$ mH，$R = 10$ $\Omega$，$\tau = L/R = 5$ ms。投入直流电压源 $V_s = 100$ V 后的电流解析解：

$$i(t) = \frac{V_s}{R}(1 - e^{-t/\tau}) = 10(1 - e^{-t/0.005})$$

后向欧拉离散（固定步长 $h = 0.5$ ms）：

$$i_{n+1} = \frac{h/L}{1 + Rh/L} v_{n+1} + \frac{1}{1 + Rh/L} i_n$$

代入数值：$h/L = 10$，$1 + Rh/L = 6$，得递推关系：

$$i_{n+1} = \frac{10}{6} v_{n+1} + \frac{1}{6} i_n$$

### 验证步骤

如需验证 BE 与 TR 的数值振荡差异：

1. 用 BE 和 TR 分别仿真 RL 电路从零状态启动的电流响应
2. 在 $t = 10$ ms 处将电压源短路（模拟故障）
3. 对比两种积分器的故障后波形：TR 是否出现步间交替振荡，BE 是否一步内完全阻尼
4. 观察 BE 的 CDA 窗口（切换到 BE 再恢复 TR）能否消除 TR 的振荡

数值试验请使用 EMTP 类软件或自行编程实现对比。

---

## 7. 延伸阅读

### 核心参考文献

- [[numerical-oscillation-suppression]] — Marti (2004)：CDA 算法与 BE 在 EMTP 中的核心应用
- [[accurate-time-domain-simulation-of-power-electronic-circuits]] — Nzale et al. (2021)：BE + 插值组合的量化分析，TR-BE 方法族系统对比
- [[supplementary-techniques-for-2s-dirk-based-emt-simulations]] — Noda (2014)：2S-DIRK 第一阶段等价于 BE
- [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] — Gao et al. (2021)：大步长场景下的 L-稳定方法

### 相关页面

- [[trapezoidal-rule]] — 默认主积分器，BE 常作为其事件后补充
- [[gear-method]] — BE 即 BDF1；BDF2（二阶 L-稳定）作为多步法进阶选择
- [[numerical-integration]] — 数值积分方法总览
- [[numerical-oscillation-suppression]] — 数值振荡抑制技术，包含 CDA 详细对比表
- [[companion-circuit]] — 伴随电路中的 BE 等效导纳推导
- [[bilinear-transform]] — Tustin 变换（与 BE 离散化的联系）
- [[state-space-method]] — 状态空间离散化与 BE 的关联

---

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Nzale 等 - Accurate time-domain simulation of power electronic circuits | 2021 | 系统分析 TR-BE 组合的 8 种变体，3000 倍振荡抑制量化数据，STATCOM 100ms 仿真对比 |
| Melgoza-Vázquez 等 - Simulation of electromagnetic transients with a family of implicit multi-step oscillation-free formulas | 2026 | BDF 族（BDF1-BDF5）系数表，A-稳定/L-稳定特性，多步公式实现 |
| Gao 等 - Three-stage implicit integration for large time step size | 2021 | 3S-SDIRK 与 TR-BDF2 对比，大步长 L-稳定方法 |
| Noda - Supplementary techniques for 2S-DIRK based EMT simulations | 2014 | 2S-DIRK 第一阶段等价于 BE 的理论证明 |
| Marti 和 Lin - Suppression of numerical oscillations in the EMTP | 1989 | CDA 原始论文，BE 作为事件后临时过渡的核心机制 |