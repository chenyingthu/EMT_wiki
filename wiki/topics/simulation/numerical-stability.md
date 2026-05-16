---
title: "数值稳定性 (Numerical Stability)"
type: topic
tags: [numerical-stability, integration, simulation, accuracy, error, a-stable, l-stable, stiff]
created: "2026-05-02"
updated: "2026-05-16"
---

# 数值稳定性 (Numerical Stability)

## 定义与边界

数值稳定性（Numerical Stability）描述离散算法在时间推进、开关切换、非线性迭代和接口耦合中是否将误差保持有界、是否引入非物理能量增长，以及是否将真实稳定系统误判为发散或产生虚假振荡。它是 EMT 仿真质量的核心维度，但不等同于精度：稳定的算法仍可能因步长过大、模型过简或事件处理错误而不准确。

**稳定性 ≠ 精度**：即使数值稳定，收敛的 EMT 解仍可能因截断误差积累而偏离真实物理量。步长选择必须同时满足稳定性条件和目标频带精度要求，不可偏废其一。

本页是 topics/simulation 的综合页，涵盖 EMT 数值稳定性的理论框架、典型积分方法的稳定性特性、误差传播机制和失败模式。具体积分公式详见 [[numerical-integration]]；梯形法与后向欧拉的对比详见 [[trapezoidal-rule]] 和 [[backward-euler]]；Gear 多步法及其历史项边界详见 [[gear-method]]；开关后虚假振荡的处理详见 [[numerical-oscillation-suppression]]；刚性多时间尺度策略详见 [[stiff-system-handling]]。

## EMT 中的作用

EMT 仿真将电感、电容、线路、机器、变流器和控制器离散为逐步代数方程。数值稳定性决定这些方程在长时段、强开关、不连续和刚性模态下是否可信。关键作用包括：

- **选择积分方法和步长**：避免稳定系统被算法误放大——A 稳定方法保证左半平面极点对应稳定数值解，但不能防止步间振荡
- **抑制开关后数值振荡**：梯形法在不连续事件后可能产生交替数值误差（CDA 方法通过两个 Δt/2 后向欧拉步抑制）
- **处理非线性状态切换**：控制限幅、二极管换相和保护动作带来的状态切换可能激发非物理数值模态
- **评估接口能量注入**：多速率、分区和 EMT-TS 混合接口若不稳定，会将人工能量注入真实系统响应
- **支撑验证流程**：为 [[emt-simulation-verification]] 提供步长敏感性、事件日志和误差诊断依据

## 核心机制

### 稳定函数与稳定区域

对测试方程：

$$
\dot{x} = \lambda x, \qquad \lambda \in \mathbb{C}
$$

一步法离散后常写成：

$$
x_{n+1} = R(z) x_n, \qquad z = \lambda \Delta t
$$

其中 $R(z)$ 是**稳定函数**（stability function），$z$ 是无量纲乘积。**绝对稳定区域**定义为：

$$
\mathcal{S} = \{z \in \mathbb{C} : |R(z)| \leq 1\}
$$

若连续系统满足 $\mathrm{Re}(\lambda) < 0$（稳定），但 $z = \lambda \Delta t$ 落在 $\mathcal{S}$ 之外，则数值解随时间发散。稳定区域的形状直接决定方法的刚性处理能力：

- **A 稳定**（A-stable）：稳定区域覆盖整个左半平面 $\mathrm{Re}(z) < 0$，即对所有稳定连续系统都用步长保证数值稳定。梯形法是典型 A 稳定方法。
- **L 稳定**（L-stable）：在 A 稳定的基础上，还满足 $\lim_{z \to -\infty} R(z) = 0$。后向欧拉法是典型 L 稳定方法。
- **强 A 稳定**（Strong A-stable）：A 稳定且 $|R(z)| \to 0$ 当 $|z| \to \infty$。

稳定区域的几何差异带来的实际影响：高刚性系统（$\lambda$ 远离原点）若用梯形法，$z$ 虽在左半平面但模很大，可能接近稳定区域边界而产生步间振荡；后向欧拉法因 $R_{BE}(z) \to 0$ 能完全阻尼这些模态。

### 积分方法的稳定函数

#### 梯形法（Trapezoidal Rule / TR）

$$
R_{TR}(z) = \frac{1 + z/2}{1 - z/2}
$$

梯形法 A 稳定（$\mathrm{Re}(z) < 0$ 时 $|R_{TR}(z)| = 1$），但 $\lim_{z \to -\infty} R_{TR}(z) = -1$。这意味着当不连续事件使 $\lambda$ 对应的离散传递函数进入 $z \to -\infty$ 区域时，数值模态不会衰减而是换号——形成持续的交替振荡，这是梯形法数值振荡的根本原因。

#### 后向欧拉法（Backward Euler / BE）

$$
R_{BE}(z) = \frac{1}{1 - z}
$$

后向欧拉法 L 稳定：$|R_{BE}(z)| < 1$ 当 $\mathrm{Re}(z) < 0$，且 $\lim_{z \to -\infty} R_{BE}(z) = 0$。在 $z \to -\infty$ 时 $R_{BE} \to 0$，故对不连续激发的高频数值模态有完全阻尼。但一阶精度导致数值耗散，可能衰减真实高频暂态。

#### 隐式 Runge-Kutta 方法（SDIRK）

单对角隐式 Runge-Kutta（SDIRK）的稳定函数为：

$$
R(z) = 1 + \frac{z}{1 - \alpha z} + \frac{z^2}{(1 - \alpha z)^2} + \cdots + \frac{z^s}{(1 - \alpha z)^s}
$$

其中 $s$ 为阶段数，$\alpha$ 是 Butcher 表中的对角系数。取 $\alpha \approx 0.435866$ 可使 3S-SDIRK（三阶段 SDIRK）达到三阶精度并满足 L 稳定性（Tanaka & Baba 2023）。2S-DIRK（二阶段 SDIRK）在 $\alpha$ 取特定值时二阶 L 稳定，常用于移频 EMT（SFEMT）中替代梯形法以消除数值振荡。

#### Gear / BDF 方法

Gear 方法（后向微分公式，BDF）的稳定函数随步数 $k$ 变化。$k$ 步 BDF 的稳定函数为：

$$
R_{BDF,k}(z) = \frac{\sum_{j=0}^{k-1} \alpha_j z^j}{z^k + \sum_{j=0}^{k-1} \beta_j z^j}
$$

BDF-1 即后向欧拉（L 稳定），BDF-2 在 $\mathrm{Re}(z) < 0$ 时 $|R| \leq 1$ 但非 L 稳定，高阶 BDF（$k \geq 3$）在左半平面有稳定区域边界缺口，仅条件稳定。在 EMT 中的主要用途是处理含历史项的 Maxwell 型方程和宽频等值模型。

### 误差传播机制

局部截断误差、舍入误差、事件定位误差和非线性迭代残差沿离散系统传播。简化误差传播模型为：

$$
e_{n+1} = R(z) e_n + \tau_n
$$

其中 $e_n$ 是第 $n$ 步的误差，$\tau_n$ 是当前步误差源。若 $|R(z)| < 1$，误差在传播中被衰减，但以下情况可能破坏这一结论：

- **事件处理注入**：不连续点附近梯形法将误差放大（$R_{TR} \approx -1$），一个 $\Delta t$ 内注入的误差不衰减反而换号
- **非线性迭代残差**：Newton-Raphson 迭代未收敛时，残差作为额外激励注入，与 $R(z)$ 相互作用可能导致振荡
- **接口能量注入**：EMT-TS 接口若误差协调不当，会在接口变量上注入非物理能量

Kocar 等（2010）指出，宽频线路模型的时域卷积离散化引入截断误差，模态延迟非整数倍步长时产生插值误差，二者共同造成误差传播。当使用 ULM（通用线路模型）的部分分式展开（PFE）时，留数/极点比值 $r/P$ 过大将导致时域递归计算发散——这解释了为什么"频域拟合良好但时域仿真发散"的现象。

### 切换系统的稳定性（CQLF 框架）

对于含电力电子开关的网络，Martinez-Velasco 等（2021）证明：梯形法对切换网络的稳定性依赖**物理无源性**和**Lyapunov 能量函数不变性**，而非仅依赖 A-stability。分析框架如下：

设网络有 $s$ 个双值电阻开关，每种开关状态对应一个线性子电路，其状态方程为：

$$
\dot{\mathbf{x}} = \mathbf{A}_i \mathbf{x}, \qquad i = 1, 2, \ldots, 2^s
$$

若存在同一正定二次型 $V(\mathbf{x}) = \mathbf{x}^\top \mathbf{P} \mathbf{x}$ 使得对所有开关状态满足 $\mathbf{A}_i^\top \mathbf{P} + \mathbf{P} \mathbf{A}_i \preceq 0$，则 $V$ 是**公共二次 Lyapunov 函数**（CQLF），保证任意切换序列下能量不增长。梯形法离散化后，离散状态转移矩阵 $\mathbf{R}_i$ 继承 $V$ 不变性的条件为：

$$
\mathbf{R}_i^\top \mathbf{P} \mathbf{R}_i \preceq \mathbf{P}, \quad \forall i
$$

这一条件要求开关状态的切换不增加 $V$ 对应的能量度量。**工程含义**：梯形法在开关网络上"看起来 A 稳定"，但若网络不满足无源性（如有源电力电子控制器持续向网络注入能量），即使每个开关状态单独稳定，切换序列仍可能导致数值不稳定。

### 谐振电路的截断误差

对于 RLC 谐振电路，EMTP 中梯形积分引入的**表观阻抗误差**可解析表示为（Zhong et al. 2018）：

$$
\tilde{Z}_{EMTP}(\omega) = Z_{actual}(\omega) \cdot \left[1 + \frac{(\omega \Delta t)^2}{12} + O((\omega \Delta t)^4)\right]
$$

误差随频率 $\omega$ 增加而增加，随步长 $\Delta t$ 减小而降低。在谐振点附近，由于品质因数 $Q$ 的放大作用，阻抗幅值偏差约为 $(\omega \Delta t)^2 Q / 12$。对于复杂电路（含相邻谐振），需用"表观角频率"数值过程估计误差，而非简单解析式。

## 边界与失败模式

### A 稳定的局限

- A 稳定不等于所有 EMT 工况可靠：开关事件、历史项重置和非线性切换仍可能产生伪振荡（梯形法在 $z \to -\infty$ 时 $R \to -1$，交替换号不衰减）
- L 稳定不等于高精度：真实行波、开关纹波和高频谐振可能被过度阻尼，后向欧拉的一阶耗散会扭曲真实高频暂态

### 步长与精度的耦合

- 步长满足稳定性条件不代表满足目标频带精度：应做步长收敛性测试或与基准结果对比
- 对同一系统，梯形法在 $f_{max}$ 频率处的阻抗误差约为 $(\omega_{max} \Delta t)^2/12$，而后向欧拉为 $(\omega_{max} \Delta t)/2$——高频下梯形法精度更高，但可能伴随振荡

### 接口与混合仿真

- 多速率接口、混合仿真边界和外部控制 DLL 可能破坏单个子系统的稳定性结论：接口误差不衰减会向另一子系统注入能量
- EMT-TS 接口若接口变量的数值特性（$R$ 函数）与物理系统稳定域不匹配，可能在接口处激发非物理振荡

### 非线性迭代与模型误差

- 非线性迭代未收敛、雅可比冻结过久或限幅逻辑顺序错误，可能表现为数值稳定问题而非建模问题
- 宽频线路模型 PFE 拟合中留数/极点比值失控（$r/P > P_{max}$）会导致时域递归计算发散，即使频域拟合误差看起来很小

### 事件定位精度

- 开关动作时刻若未精确对齐步长边界，会在插值/外推中引入额外误差源，可能激发数值振荡
- 任何固定"最大步长""误差百分比"或"稳定频段"都必须绑定模型、工具、步长和来源，不能无边界引用

## 量化性能边界

### 积分方法稳定区域对比

| 方法 | 稳定类型 | $R(\infty)$ | 精度阶数 | 数值阻尼 |
|------|----------|-------------|---------|---------|
| 梯形法（TR） | A 稳定 | $-1$ | 二阶 | 无（交替换号） |
| 后向欧拉（BE） | L 稳定 | $0$ | 一阶 | 完全阻尼 |
| 2S-DIRK | L 稳定 | $0$ | 二阶 | 完全阻尼 |
| 3S-SDIRK | L 稳定 | $0$ | 三阶 | 完全阻尼 |
| BDF-2 | 条件稳定 | $|\beta_0| < 1$ | 二阶 | 弱阻尼 |
| Gear-2 | L 稳定 | $0$ | 二阶 | 完全阻尼 |

### 典型步长范围

基于 EMT 工程实践的经验步长范围（非理论证明）：

| 场景 | 典型步长 | 说明 |
|------|----------|------|
| 输电线路工频暂态 | $10$–$50$ $\mu$s | 步长 $\ll T_{base}/10$（$T_{base}=1/50$ 或 $1/60$ s） |
| 开关动作暂态 | $1$–$10$ $\mu$s | 需捕捉快瞬态，开关前后可能触发 CDA |
| 电力电子 PWM | $1$–$100$ $\mu$s | PWM 载波周期决定分辨率需求 |
| 移频 EMT（SFEMT） | $0.5$–$2$ ms | 基频移至零频后可用大步长 |
| 机电暂态混合接口 | $1$–$10$ ms | TS 步长远大于 EMT，接口稳定性关键 |

> **量化数据来源说明**：上表为工程经验范围，来源于 EMTP 用户手册和文献算例惯例，非单一论文的可控实验数据。原文未报告可核验的精确步长—误差—系统组合数值结果时，应写明"原文未报告可核验的数值结果"。

### 数值振荡抑制效果

CDA（临界阻尼调整）方法在不连续点附近的数值振荡抑制效果（定性描述，无精确量化数据）：

- 后向欧拉对不连续超调的完全阻尼性质，在一个 Δt 内消除持续振荡
- 对电感电流开断后电感端电压振荡的抑制效果已有 UBC-EMTP 实现验证（原文未报告具体幅值降低比例）
- 对电容电压投入后电容电流振荡的抑制效果已在 DCG/EPRI EMTP 生产代码中实现（原文未报告具体误差数值）

**证据边界**：当前来源论文未给出具体测试系统拓扑、元件参数、故障场景、误差曲线或 CPU 时间等可核验数值，不得将"有效抑制"扩展为具体百分比或倍数。

### 宽频线路模型稳定性约束

Kocar 等（2010）对 ULM 模型的稳定性约束为：

$$
P_{min} \leq \frac{r}{P} \leq P_{max}
$$

其中 $r$ 是 PFE 留数，$P$ 是极点，$P_{min}$ 和 $P_{max}}$ 是保证时域递归卷积稳定的阈值范围。违反此约束将导致时域发散，即使频域拟合误差在可接受范围内。

## 适用边界与选择指南

### 积分器选择决策表

| 场景 | 推荐方法 | 原因 |
|------|----------|------|
| 高频振荡主导（开关纹波、故障尖峰） | 后向欧拉或 2S-DIRK | 完全阻尼高频数值模态 |
| 基频及低频主导（工频暂态） | 梯形法 | 二阶精度，低频畸变小 |
| 强刚性系统（远端极点模态） | 3S-SDIRK 或 Gear-2 | L 稳定且精度高于一阶 |
| 开关频繁切换的网络 | 梯形法 + CDA | CDA 在不连续点局部施加阻尼 |
| 移频 EMT（SFEMT）大步长 | 3S-SDIRK | L 稳定消除大步长下的数值振荡 |
| 含频率相关线路的宽频仿真 | ULM + PFE 稳定性约束 | 防止卷积计算发散 |

### 稳定性问题的诊断流程

1. **检查 $R(z)$ 函数**：对目标系统估计 $\lambda$ 范围，计算 $|R(\lambda \Delta t)|$ 是否 $< 1$
2. **检查开关事件后是否产生交替振荡**：若振荡频率约为 $1/(2\Delta t)$，是梯形法在 $z \to -\infty$ 区域的典型症状 → 引入 CDA
3. **检查非线性迭代收敛性**：若残差在某些步突然增大，可能是限幅逻辑或雅可比冻结问题，而非积分器问题
4. **检查宽频模型 PFE 参数**：验证 $r/P$ 比值是否在稳定范围内（Kocar 2010 方法）
5. **检查接口变量协调**：EMT-TS 接口或分区边界是否在接口处注入非物理能量

## 相关方法与模型

- [[numerical-integration]]：积分方法总入口，含 Runge-Kutta、Adams、gear 等方法
- [[trapezoidal-rule]]：A 稳定但非 L 稳定的常用 EMT 积分器，$R_{TR}(\infty) = -1$
- [[backward-euler]]：L 稳定、强阻尼的一阶隐式方法
- [[gear-method]]：BDF/Gear 多步方法及其历史项边界条件
- [[numerical-integration-error]]：截断误差、舍入误差和事件误差背景
- [[numerical-oscillation-suppression]]：开关后伪振荡识别与处理，含 CDA 方法
- [[stiff-system-handling]]：刚性多时间尺度处理策略
- [[multirate-method]]：多步长接口可能带来的稳定性问题与接口阻尼
- [[emt-simulation-verification]]：步长敏感性分析与误差诊断方法

## 来源论文

- [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Tanaka & Baba 2023]] — 3S-SDIRK 三阶 L 稳定积分，用于移频 EMT 大步长仿真，$\alpha \approx 0.435866$，L 稳定性消除梯形法数值振荡
- [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Numerical Oscillations CDA]] — 临界阻尼调整（CDA）：不连续点后两个 Δt/2 后向欧拉步消除梯形法数值振荡，UBC-EMTP 和 DCG/EPRI EMTP 实现
- [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Kocar et al. 2010]] — 宽频线路 ULM 时域卷积稳定性与 PFE 留数/极点比值约束
- [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix|Zhong et al. 2018]] — 梯形法在谐振电路中引入的表观阻抗误差解析表达，误差 $\propto (\omega \Delta t)^2/12$
- [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Martinez-Velasco et al. 2021]] — 切换网络稳定性的 CQLF 框架：梯形法稳定性依赖物理无源性与 Lyapunov 能量函数不变性，而非单纯 A-stability
- [[numerical-integration-2s-dirk-iet-gtd.md]] — 2S-DIRK 二阶 L 稳定方法，SDIRK 对角参数消除线性系统瓶颈