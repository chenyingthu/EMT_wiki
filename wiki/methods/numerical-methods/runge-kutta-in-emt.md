---
title: "Runge-Kutta 方法在 EMT 中的适用性与局限"
type: method
tags: [runge-kutta, dirk, numerical-integration, stability, emt-limitation]
created: "2026-05-10"
updated: "2026-05-14"
---

# Runge-Kutta 方法在 EMT 中的适用性与局限

## 定义

Runge-Kutta（RK）方法是一类基于 Butcher 矩阵描述的单步数值积分方法族。对于测试方程 $\dot{y} = f(t, y)$，$s$ 级 RK 方法的一般形式为：

$$
\begin{cases}
k_i = f\left(t_n + c_i h, \; y_n + h \sum_{j=1}^{s} a_{ij} k_j\right), \quad i = 1, 2, \dots, s \\[10pt]
y_{n+1} = y_n + h \sum_{i=1}^{s} b_i k_i
\end{cases}
$$

用 Butcher 矩阵表示为：

$$
\begin{array}{c|c}
\mathbf{c} & \mathbf{A} \\
\hline
& \mathbf{b}^\mathrm{T}
\end{array}
$$

其中 $\mathbf{A} = [a_{ij}]$ 为 $s \times s$ 系数矩阵，$\mathbf{c} = [c_1, \dots, c_s]^\mathrm{T}$ 为节点向量，$\mathbf{b} = [b_1, \dots, b_s]^\mathrm{T}$ 为权重向量。RK 方法的阶数由以下代数条件决定：

- 1 阶精度：$\mathbf{b}^\mathrm{T} \mathbf{e} = 1$
- 2 阶精度：$\mathbf{b}^\mathrm{T} \mathbf{C} \mathbf{e} = \frac{1}{2}$
- 3 阶精度：$\mathbf{b}^\mathrm{T} \mathbf{C}^2 \mathbf{e} = \frac{1}{3}, \quad \mathbf{b}^\mathrm{T} \mathbf{A} \mathbf{C} \mathbf{e} = \frac{1}{6}$

其中 $\mathbf{e}$ 为全 1 向量，$\mathbf{C} = \mathrm{diag}(c_1, \dots, c_s)$。

稳定函数定义为 $R(z) = \det(\mathbf{I} - z\mathbf{A} + z\mathbf{e}\mathbf{b}^\mathrm{T}) / \det(\mathbf{I} - z\mathbf{A})$，其中 $z = h\lambda$。稳定性判据为：

- **A 稳定**：$|R(z)| \leq 1$ 对所有 $\mathrm{Re}(z) < 0$ 成立
- **L 稳定**：A 稳定且 $\lim_{\mathrm{Re}(z) \to -\infty} |R(z)| = 0$

L 稳定是 EMT 仿真的关键属性——它保证在开关突变等刚性事件后，高频数值误差在一步内被完全阻尼，不会产生持续振荡。

## EMT 中的角色

EMT 仿真对数值积分方法提出两个核心约束：

1. **刚性系统稳定性**：EMT 网络包含纳秒级开关瞬态到毫秒级机电振荡的跨尺度动态，积分器必须具备 A 稳定或 L 稳定性，否则必须采用极小步长，使仿真不可行。
2. **非连续事件处理**：开关动作、故障、控制限幅导致状态变量突变。梯形法（Trapezoidal Rule）的 $R(\infty) = -1$ 在突变后产生交替振荡（$y_n/y_{n-1} \to -1$），而 L 稳定方法的 $R(\infty) = 0$ 则能一步阻尼消除。

传统 EMTP 类程序（EMTP、PSCAD、RTDS）主要采用梯形法 + CDA（临界阻尼调整）的组合策略——在检测到突变时临时切换为后向欧拉法。然而 CDA 的突变检测并非总是可行（如控制器限幅引起的突变），且切换过程引入额外误差。DIRK 方法从积分器层面实现无振荡，无需事件检测和切换逻辑。

## 核心机制

### 显式 RK 的刚性限制

经典显式 RK 方法（如 RK4）的稳定函数为多项式：

$$
R(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24}
$$

其稳定区域在复平面上为有限区域。EMT 系统中，电感/电容的刚性模态满足 $|h\lambda| \gg 1$，显式 RK 的稳定函数值 $|R(z)| > 1$，导致数值发散。因此显式 RK 仅适用于机电暂态仿真等非刚性场景，不能作为 EMT 主积分器。

### DIRK 方法的解耦优势

对角隐式 RK（DIRK）方法要求系数矩阵 $\mathbf{A}$ 为下三角矩阵，即 $a_{ij} = 0$ 当 $j > i$。这使得每阶段只需求解一个 $n$ 维隐式方程，而非全隐式 IRK 的 $s \times n$ 维耦合方程组。两阶段 DIRK 每步需解两个 $n$ 维方程组，计算量约为梯形法的 2 倍，但避免了矩阵耦合。

若进一步要求主对角元相等（$a_{ii} = \gamma$），则每阶段的线性系统矩阵相同，LU 分解只需执行一次，大幅降低计算开销。满足此条件的称为 SDIRK（单对角隐式 RK）。

### 2S-DIRK：Noda 等人的无振荡积分器

Noda 等人（2014）系统提出了 2S-DIRK 在 EMT 仿真中的应用，其 Butcher 矩阵为：

$$
\begin{array}{c|cc}
a & a & 0 \\
\hline
& 1-a & a
\end{array}
\quad \text{其中 } a = 1 - \frac{1}{\sqrt{2}} \approx 0.2929
$$

中间计算时间点为：

$$
\tilde{t}_n = t_{n-1} + ah
$$

两阶段公式分别为后向欧拉形式：

$$
\tilde{y}_n = y_{n-1} + \tilde{h} f(\tilde{t}_n, \tilde{y}_n)
$$

$$
\tilde{y}_{n-1} = \alpha y_{n-1} + \beta \tilde{y}_n \quad (\alpha = -\sqrt{2}, \; \beta = 1 + \sqrt{2})
$$

$$
y_n = \tilde{y}_{n-1} + \tilde{h} f(t_n, y_n)
$$

其中 $\tilde{h} = ah$。关键点在于：(1) 两阶段均为后向欧拉形式，编码只需复用后向欧拉代码；(2) 阶段间通过 $\tilde{y}_{n-1}$ 解耦，可顺序求解；(3) 二阶精度，L 稳定（$R(\infty) = 0$）。

与 CDA 的核心区别在于：CDA 在检测到振荡后临时切换为后向欧拉再切回，而 2S-DIRK 在积分器层面本身就是无振荡的，无需任何事件检测。

### 3S-DIRK：叶小晖等人的变阶变步长方案

叶小晖等人（2020）从 Butcher 矩阵出发，系统分析了 CDA 算法的精度缺陷，提出了三级 DIRK（3S-DIRK）方案。CDA 使用梯形法（2 阶）+ 后向欧拉（1 阶）+ 一阶线性插值，在算法切换期间精度降至 1 阶，在电力电子频繁开关时产生大量误差。

3S-DIRK 的 Butcher 矩阵含参数 $\lambda$：

$$
\begin{array}{c|ccc}
0 & 0 & 0 & 0 \\
\lambda & \lambda & \lambda & 0 \\
\frac{1}{6\lambda-4\lambda^2-1} & 1-2\lambda & \frac{4\lambda}{6\lambda-4\lambda^2-1} & \lambda \\
\hline
b_1 & b_2 & b_3 & \lambda
\end{array}
$$

通过选择不同 $\lambda$ 值，获得 4 种分算法：

| 分算法 | $\lambda$ | 精度 | 稳定性 | 用途 |
|--------|-----------|------|--------|------|
| 算法 A | $\frac{1 \pm \sqrt{3}}{2}$ | 3 阶 | A 稳定 | 正常运行，高精度 |
| 算法 B | $1 \pm \frac{1}{\sqrt{2}}$ | 2 阶 | L 稳定 | 故障期间，消除振荡 |
| 算法 C | $\lambda_{\text{插}} = \lambda/k$ | 2 阶 | A 稳定 | 主动插值 |
| 算法 D | 被动插值 | 2 阶 | — | 被动插值 |

正常运行时采用 3 阶算法 A，故障发生后切换至 L 稳定算法 B，整个仿真过程精度不低于 2 阶。算法切换时保证元件等值导纳不变（通过调整步长而非修改 $\lambda$），实现真正的变步长计算。

### Compact Scheme：Tanaka 的单阶段无振荡方法

Tanaka 和 Baba（2023）提出了一种基于紧凑格式的单阶段无振荡积分方法。该方法不仅处理离散函数值，还处理其导数值，对测试方程的离散格式为：

$$
y_n = y_{n-1} + \frac{h}{2}(y'_n + y'_{n-1}) - \frac{h^2}{12}(y''_n - y''_{n-1})
$$

代入 $y' = f(t, y)$，得到：

$$
y_n = y_{n-1} + \frac{h}{2}(f_n + f_{n-1}) - \frac{h^2}{12}(f'_n - f'_{n-1})
$$

其中 $f' = \partial f/\partial t$ 为时间导数。稳定函数为：

$$
|R(z)| = \left| \frac{1 + \frac{h\lambda}{2} + \frac{(h\lambda)^2}{12}}{1 - \frac{h\lambda}{2} + \frac{(h\lambda)^2}{12}} \right| \leq 1
$$

因此 Compact Scheme 是 A 稳定的。虽然常规状态下不是 L 稳定（$x_n/x_{n-1} \to 1$ 当 $\mathrm{Re}(\lambda) \to -\infty$），但在开关突变时刻，当 $\lambda$ 从 $\lambda_1$ 突变到 $\lambda_2$（$|\lambda_1| \ll |\lambda_2|$），有：

$$
\frac{x_n}{x_{n-1}} \to 0, \quad \frac{x'_{n+1}}{x'_n} \to 0
$$

即在突变后一步内达到 L 稳定状态。与 2S-DIRK 和 TR-BDF2 相比，Compact Scheme 的优势在于：(1) 单阶段方法，不产生非线性元件引起的虚假尖峰；(2) A 稳定 + 突变后 L 稳定。缺点是每步矩阵的非零元素约为梯形法的 2 倍，计算开销增加。

### 稳定函数对比

| 方法 | 稳定函数 $R(\infty)$ | 稳定性 | EMT 适用性 |
|------|---------------------|--------|-----------|
| 显式 RK（RK4） | 无界（多项式） | 条件稳定 | 仅机电暂态 |
| 梯形法 | $-1$ | A 稳定，非 L 稳定 | 常用，突变后振荡 |
| 后向欧拉 | $0$ | L 稳定 | 强阻尼，1 阶精度 |
| 2S-DIRK | $0$ | L 稳定 | 无振荡，2 阶，计算量≈2×梯形法 |
| 3S-DIRK | $0$ | L 稳定（故障态） | 无振荡，3→2 阶变精度 |
| Compact Scheme | 常规 1，突变后 0 | A 稳定 + 突变 L 稳定 | 无振荡，4 阶，无虚假尖峰 |
| TR-BDF2 | $0$ | L 稳定 | 无振荡，2 阶，两阶段 |

### 混合数值积分：Gao 等人的中点-梯形混合

Gao 等人（2024）在 MMC 的 EMTP 仿真中提出了中点规则与梯形规则的混合数值积分方法。核心思想是将 MMC 臂电感采用梯形规则离散，而子模块（SM）电容采用中点规则离散，两者以 leapfrog 方式交替求解：

**臂电感方程（梯形规则）**：

$$
i_{\text{arm}}(t) = i_{\text{arm}}(t-\Delta t) + \frac{\Delta t}{2L_0}\left(v_{\text{arm}}(t) - R_{\text{eq}} i_{\text{arm}}(t) + v_{\text{arm}}(t-\Delta t) - R_{\text{eq}} i_{\text{arm}}(t-\Delta t)\right) - \frac{\Delta t}{2L_0}\left(\mathbf{K}_1 \mathbf{v}_c(t-\tfrac{\Delta t}{2}) + \mathbf{K}_2 \mathbf{v}_{\text{ceq}}(t-\tfrac{\Delta t}{2})\right)
$$

等效导纳为：

$$
G = \frac{\Delta t}{2L_0 + R_{\text{eq}}\Delta t}
$$

**SM 电容方程（中点规则）**：

$$
v_{ci}\left(t + \frac{\Delta t}{2}\right) = v_{ci}\left(t - \frac{\Delta t}{2}\right) + \frac{\Delta t}{C_{smi}} i_{\text{arm}}(t)
$$

leapfrog 求解流程：(1) 先计算 $t-\Delta t/2$ 时刻的 SM 电容电压；(2) 再计算 $t$ 时刻的臂电流；(3) 最后计算 $t+\Delta t/2$ 时刻的 SM 电容电压。由于电容和电感方程之间间隔 $\Delta t/2$，两者完全解耦，且 SM 电容之间也相互独立。

此混合策略使 MMC 臂等效为具有恒定导纳的两节点 Norton 等效电路，避免了传统方法中因开关状态频繁变化导致的导纳矩阵频繁 LU 分解。

## 形式化表达

### RK 方法通用框架

$$
\mathbf{k} = \mathbf{f}\left(t_n + \mathbf{c}h, \; \mathbf{y}_n + h\mathbf{A}\mathbf{k}\right)
$$

$$
\mathbf{y}_{n+1} = \mathbf{y}_n + h(\mathbf{b}^\mathrm{T} \otimes \mathbf{I})\mathbf{k}
$$

### DIRK 的稳定性函数

对于 $s$ 级 DIRK，稳定函数由 Gramer 法则给出：

$$
R(z) = \frac{\det(\mathbf{I} - z\mathbf{A} + z\mathbf{e}\mathbf{b}^\mathrm{T})}{\det(\mathbf{I} - z\mathbf{A})}
$$

### 2S-DIRK 稳定函数

$$
R(z) = \frac{2\lambda^2(2\lambda^2-4\lambda+1)z^2 - (4\lambda^2+2\lambda-1)z}{4\lambda^2(1-\lambda z)^2}
$$

### 3S-DIRK 的精度条件

$$
\mathbf{b}^\mathrm{T}\mathbf{e} = 1, \quad \mathbf{b}^\mathrm{T}\mathbf{C}\mathbf{e} = \frac{1}{2}, \quad \mathbf{b}^\mathrm{T}\mathbf{C}^2\mathbf{e} = \frac{1}{3}, \quad \mathbf{b}^\mathrm{T}\mathbf{A}\mathbf{C}\mathbf{e} = \frac{1}{6}
$$

### Compact Scheme 的元件等效电路

**线性电感**：

$$
i_n = i_{n-1} + \frac{h}{2L}(v_n + v_{n-1}) - \frac{h^2}{12L}(v'_n - v'_{n-1})
$$

等效导纳：$G_L = \frac{h}{2L}, \quad G_{LT} = \frac{h^2}{12L}$

**线性电容**：

$$
v_n = v_{n-1} + \frac{h}{2C}(i_n + i_{n-1}) - \frac{h^2}{12C}(i'_n - i'_{n-1})
$$

等效导纳：$G_C = \frac{h}{2C}, \quad R_{CT} = \frac{h}{6}$

## 关键技术挑战

### 数值振荡的 Lyapunov 理论分析

Zhao、Fan 和 Gole（2019）从 Lyapunov 能量函数角度严格分析了含开关和非线性电感网络的 EMT 仿真稳定性。他们将含开关的电路建模为集总严格无源开关电路（LSPSC），证明：只有当无源性和 Lyapunov 能量函数的不变性同时满足时，梯形法才能保证任意时间步长下的稳定仿真。这与线性时不变（LTI）系统不同——在 LTI 系统中，A 稳定方法即可保证稳定仿真，但在含开关的非线性系统中，A 稳定不足以保证稳定性。

能量函数定义为：

$$
E(t) = \frac{1}{2} \mathbf{x}^\mathrm{T} \mathbf{V} \mathbf{x}
$$

其中 $\mathbf{x} = [u_1, \dots, u_{n_C}, i_1, \dots, i_{n_L}]^\mathrm{T}$ 为状态向量，$\mathbf{V}$ 为正定对角矩阵（电容和电感倒数）。无源性条件要求：

$$
\mathbf{u}(t)^\mathrm{T} \mathbf{y}(t) \geq \dot{E}(\mathbf{x}(t))
$$

### 算法切换期间的精度保持

CDA 方法在算法切换（梯形法→后向欧拉→梯形法）过程中，使用一阶线性插值连接不同算法的计算结果，导致精度从 2 阶降至 1 阶。叶小晖等人的 3S-DIRK 方案通过 Butcher 矩阵分析证实：梯形法的 Butcher 矩阵为 2 阶，后向欧拉为 1 阶，一阶线性插值不满足 2 阶条件，因此在电力电子频繁开关时产生累积误差。3S-DIRK 的 4 种分算法在切换时保证等值导纳不变，通过步长调整而非导纳修改实现无缝切换，整个仿真过程精度不低于 2 阶。

### 非线性元件的虚假尖峰

Tanaka 和 Baba 指出，2S-DIRK 和 TR-BDF2 作为两阶段方法，在包含非线性元件的电路中，由于中间阶段计算了非线性元件的电流/电压，会在电压波形上叠加虚假尖峰。Compact Scheme 作为单阶段方法，不产生此类虚假尖峰。在 77 kV 系统励磁涌流仿真中，2S-DIRK 和 TR-BDF2 的电压波形在 1 ns 时间尺度上出现虚假尖峰，而 Compact Scheme 和梯形法（无振荡时）无此现象。

### Jacobian 矩阵的恒定性问题

传统方法中，开关状态变化导致等效导纳矩阵频繁变化，需要反复进行 LU 分解。Gao 等人的混合积分方法通过中点规则离散 SM 电容方程，使 MMC 臂的等效导纳在正常运行期间保持恒定，显著减少了 LU 分解次数。但该方法的前提是 IGBT 和二极管的导通电阻相等；若考虑不等导通电阻，等效导纳将不再恒定。

## 量化性能边界

| 对比维度 | 梯形法 | 2S-DIRK | 3S-DIRK | Compact Scheme |
|----------|--------|---------|---------|----------------|
| 精度 | 2 阶 | 2 阶 | 3→2 阶变阶 | 4 阶（α=0.5） |
| 稳定性 | A 稳定 | L 稳定 | L 稳定（故障态） | A 稳定 + 突变 L 稳定 |
| 计算量 | 1 次隐式求解 | 2 次隐式求解 | 3 次隐式求解 | 1 次隐式求解 + 导数计算 |
| 虚假尖峰 | 无 | 有（非线性元件） | 有（非线性元件） | 无 |
| CDA 需求 | 需要 | 不需要 | 不需要 | 不需要 |
| 矩阵非零元素 | $N$ | $2N$ | $3N$ | $2N$ |

Compact Scheme 与 2S-DIRK 的计算时间几乎相同——虽然 Compact Scheme 每步矩阵的非零元素是梯形法的 2 倍，但 2S-DIRK 需要求解两次 $n$ 维方程组，综合计算开销相当（Tanaka & Baba, 2023）。

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 理由 |
|----------|----------|------|
| 传统 EMTP 仿真（含开关） | 梯形法 + CDA | 成熟实现，计算量最小 |
| 电力电子转换器仿真 | 2S-DIRK | 无振荡，无需 CDA 切换逻辑 |
| 高精度 EMT 仿真 | 3S-DIRK | 正常运行 3 阶精度，故障 2 阶 |
| 含强非线性元件的仿真 | Compact Scheme | 无虚假尖峰，4 阶精度 |
| MMC 详细模型仿真 | 混合积分（中点+梯形） | 恒定导纳，leapfrog 解耦 |
| 机电暂态仿真 | 显式 RK（RK4） | 非刚性系统，4 阶精度高 |

### 选择决策树

```
EMT 仿真需求
├── 系统是否刚性？
│   ├── 否 → 显式 RK（RK4）
│   └── 是 → 继续
├── 是否有开关/非线性元件？
│   ├── 否 → 梯形法
│   └── 是 → 继续
├── 是否要求无振荡？
│   ├── 否 → 梯形法 + CDA
│   └── 是 → 继续
├── 精度要求？
│   ├── 2 阶足够 → 2S-DIRK
│   ├── 3 阶 → 3S-DIRK
│   └── 4 阶 + 无尖峰 → Compact Scheme
└── 是否为 MMC 详细模型？
    └── 是 → 混合积分（中点+梯形）
```

## 相关方法

- [[numerical-integration]] — EMT 积分方法总览
- [[backward-euler]] — 后向欧拉法，L 稳定基准
- [[trapezoidal-rule]] — 梯形法，EMTP 标准积分器
- [[stiff-system-handling]] — 刚性系统处理策略
- [[numerical-oscillation-suppression]] — 数值振荡抑制
- [[companion-circuit]] — 伴随电路，DIRK 的 EMTP 实现
- [[numerical-integration-methods]] — 数值积分方法分类
- [[numerical-stability]] — 数值稳定性理论
- [[emt-mathematical-foundation]] — EMT 数学基础

## 来源论文

- **Noda, Kikuma & Yonezawa (2014)** — "Supplementary techniques for 2S-DIRK-based EMT simulations" *Electric Power Systems Research*。系统提出 2S-DIRK 在 EMT 中的应用，推导了电感和电容的 2S-DIRK 等效电路（线性和非线性），分析了电压源/电流源/开关的补充数值技术，并与 CDA 进行了数值对比。
- **叶小晖, 汤涌, 宋强 等 (2020)** — "适用于电磁暂态仿真的变阶变步长 3S-DIRK 算法" *中国电机工程学报*。从 Butcher 矩阵出发分析 CDA 的精度缺陷，提出 3S-DIRK 方案，包含 4 种分算法的切换策略，保证切换期间等值导纳不变，支持真正的变步长计算。
- **Tanaka & Baba (2023)** — "Study of a numerical integration method using the compact scheme for electromagnetic transient simulations" *Electric Power Systems Research*。提出基于紧凑格式的单阶段无振荡积分方法，推导了非线性元件的等效电路，与梯形法、CDA、2S-DIRK、TR-BDF2 进行了系统对比，证明了无虚假尖峰优势。
- **Zhao, Fan & Gole (2019)** — "Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors" *IEEE Transactions on Power Delivery*。基于 Lyapunov 能量函数和 CQLF 理论，严格分析了含开关和非线性电感网络的 EMT 仿真稳定性，证明梯形法的稳定性依赖于无源性和 Lyapunov 能量函数不变性。
- **Gao, Chen, Song 等 (2024)** — "An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration" *IEEE Transactions on Power Systems*。提出中点规则与梯形规则的混合积分方法，将 MMC 臂电感用梯形规则离散、SM 电容用中点规则离散，实现 leapfrog 求解和恒定导纳 Norton 等效。
