---
title: "数值积分方法 (Numerical Integration Methods)"
type: topic
tags: [numerical-integration, trapezoidal-rule, backward-euler, gear-method, dirk, exponential-integrator, stability]
created: "2026-05-01"
book-chapter: "2"
---

# 数值积分方法 (Numerical Integration Methods)


<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 820 420" xmlns="http://www.w3.org/2000/svg">
  <rect x="300" y="8" width="220" height="36" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="410" y="30" text-anchor="middle" font-family="Arial" font-size="13" fill="#1e40af">数值积分方法选择决策树</text>

  <rect x="270" y="58" width="280" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="410" y="83" text-anchor="middle" font-family="Arial" font-size="13" fill="#92400e">是否含频繁开关/电力电子？</text>

  <line x1="270" y1="78" x2="150" y2="78" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="190" y="72" text-anchor="middle" font-family="Arial" font-size="12" fill="#333">是</text>

  <line x1="550" y1="78" x2="670" y2="78" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="620" y="72" text-anchor="middle" font-family="Arial" font-size="12" fill="#333">否</text>

  <rect x="40" y="102" width="220" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="150" y="127" text-anchor="middle" font-family="Arial" font-size="13" fill="#92400e">是否需求大步长？</text>

  <line x1="40" y1="122" x2="40" y2="172" stroke="#333" stroke-width="1.5"/>
  <line x1="40" y1="172" x2="40" y2="192" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="55" y="166" font-family="Arial" font-size="12" fill="#333">是</text>
  <rect x="0" y="196" width="80" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="40" y="218" text-anchor="middle" font-family="Arial" font-size="11" fill="#166534">3S-SDIRK</text>
  <text x="40" y="232" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534">三阶L稳定</text>

  <line x1="260" y1="122" x2="260" y2="172" stroke="#333" stroke-width="1.5"/>
  <line x1="260" y1="172" x2="260" y2="192" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="275" y="166" font-family="Arial" font-size="12" fill="#333">否</text>
  <rect x="220" y="196" width="80" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="260" y="218" text-anchor="middle" font-family="Arial" font-size="11" fill="#166534">2S-DIRK</text>
  <text x="260" y="232" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534">二阶L稳定</text>

  <rect x="560" y="102" width="220" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="670" y="127" text-anchor="middle" font-family="Arial" font-size="13" fill="#92400e">是否为刚性系统？</text>

  <line x1="560" y1="122" x2="560" y2="172" stroke="#333" stroke-width="1.5"/>
  <line x1="560" y1="172" x2="560" y2="192" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="575" y="166" font-family="Arial" font-size="12" fill="#333">是</text>
  <rect x="520" y="196" width="80" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="560" y="218" text-anchor="middle" font-family="Arial" font-size="11" fill="#166534">Gear/BDF</text>
  <text x="560" y="232" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534">变阶变步长</text>

  <line x1="780" y1="122" x2="780" y2="172" stroke="#333" stroke-width="1.5"/>
  <line x1="780" y1="172" x2="780" y2="192" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="795" y="166" font-family="Arial" font-size="12" fill="#333">否</text>
  <rect x="740" y="196" width="80" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="780" y="218" text-anchor="middle" font-family="Arial" font-size="11" fill="#166534">梯形法</text>
  <text x="780" y="232" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534">二阶A稳定</text>

  <rect x="280" y="290" width="260" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="410" y="310" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#334155">图例 Legend</text>
  <rect x="295" y="320" width="18" height="14" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="320" y="331" font-family="Arial" font-size="11" fill="#334155">定义/标题</text>
  <rect x="295" y="342" width="18" height="14" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="320" y="353" font-family="Arial" font-size="11" fill="#334155">判断节点</text>
  <rect x="295" y="364" width="18" height="14" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="320" y="375" font-family="Arial" font-size="11" fill="#334155">推荐方法</text>
  <line x1="295" y1="390" x2="313" y2="390" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="320" y="394" font-family="Arial" font-size="11" fill="#334155">决策流向</text>

  <text x="410" y="415" text-anchor="middle" font-family="Arial" font-size="11" fill="#64748b">* CDA/指数积分器等作为特殊场景补充，见正文适用边界章节</text>

  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 数值积分方法选择决策树</p>


## 概述

数值积分方法是电磁暂态(EMT)仿真的核心算法，负责将连续时间的微分-代数方程组(DAEs)离散化为逐时步的代数方程组求解。在EMT仿真中，电感、电容、输电线路、电力电子开关等动态元件的行为都需要通过数值积分方法转换为等效伴随电路，进而形成节点导纳矩阵进行求解。

EMT仿真对数值积分方法有独特要求：必须处理开关事件引起的拓扑突变、刚性系统(时间常数差异大)的稳定求解、实时仿真的确定性延迟，以及多速率仿真的步长协调。不同的积分方法在精度阶数、数值稳定性、阻尼特性和计算复杂度之间存在权衡，选择合适的方法是仿真成功的关键。

## 作用机制

### 2.1 梯形法(Trapezoidal Rule)：原理与导纳等效

**数学原理**

梯形法通过当前步和上一时刻的斜率加权平均来求解微分方程：

$$
x_{n+1} = x_n + \frac{\Delta t}{2}[f(t_n, x_n) + f(t_{n+1}, x_{n+1})]
$$

**电感导纳等效**：

$$
i_L(t) = G_L v_L(t) + I_{hist,L}, \quad G_L = \frac{\Delta t}{2L}
$$

$$
I_{hist,L} = i_L(t-\Delta t) + \frac{\Delta t}{2L}v_L(t-\Delta t)
$$

**电容导纳等效**：

$$
i_C(t) = G_C v_C(t) + I_{hist,C}, \quad G_C = \frac{2C}{\Delta t}
$$

$$
I_{hist,C} = -\left[\frac{2C}{\Delta t}v_C(t-\Delta t) + i_C(t-\Delta t)\right]
$$

**稳定性分析**

- **A稳定**：对所有 $\text{Re}(\lambda) < 0$ 的测试方程 $\dot{x} = \lambda x$ 稳定
- **非L稳定**：$\lim_{z \to -\infty} R(z) = -1$，在刚性极限处高频误差不衰减
- **数值振荡**：电感电流或电容电压突变后，误差序列表现为 $e_n = (-1)^n e_0$

**频率响应畸变**

梯形法引入的双线性变换：

$$
s = \frac{2}{\Delta t}\frac{z-1}{z+1}
$$

离散频率与真实频率的关系：

$$
\omega_{actual} = \frac{2}{\Delta t}\tan\left(\frac{\omega_{sim}\Delta t}{2}\right)
$$

| 频率范围 | 畸变特性 | 工程意义 |
|---------|---------|---------|
| $\omega \Delta t \ll 1$ | 畸变小，$\omega \approx \omega_d$ | 低频段精度高 |
| $\omega \Delta t \to \pi$ | 畸变大，$\omega \to \infty$ | 接近奈奎斯特频率时失真 |

### 2.2 后向欧拉法(Backward Euler)：阻尼特性与适用场景

**数学原理**

$$
x_{n+1} = x_n + \Delta t \cdot f(t_{n+1}, x_{n+1})
$$

**导纳等效**

- **电感**：$G_L = \frac{\Delta t}{L}$（梯形法的2倍）
- **电容**：$G_C = \frac{C}{\Delta t}$（梯形法的1/4）

**阻尼特性**

- **L稳定**：$\lim_{z \to -\infty} R(z) = 0$，高频误差完全阻尼
- **1阶精度**：局部截断误差为 $O(\Delta t^2)$，精度低于梯形法
- **强数值阻尼**：适合抑制数值振荡，但会衰减真实高频分量

**临界阻尼调整(CDA)**

EMTP采用的振荡抑制技术：

1. 检测到开关事件或状态突变
2. 在事件点插入半步长后向欧拉(时间步长$\Delta t/2$)
3. 随后恢复梯形法继续积分

**问题**：CDA依赖对突变事件的准确检测，控制系统限幅、非线性元件工作点变化等突变可能难以完全捕获。

### 2.3 Gear方法族与可变阶数积分

**向后微分公式(BDF)**

k阶Gear方法的通用形式：

$$
\sum_{j=0}^{k}\alpha_j x_{n+j} = \Delta t \cdot \beta_k f(t_{n+k}, x_{n+k})
$$

**常用阶数系数**

| 阶数 | $\alpha_0$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\beta_k$ |
|------|-----------|-----------|-----------|-----------|-----------|
| 1阶(BE) | 1 | -1 | - | - | 1 |
| 2阶(BDF2) | 1/3 | -4/3 | 1 | - | 2/3 |
| 3阶(BDF3) | 2/11 | -9/11 | 18/11 | -1 | 6/11 |

**变阶变步长策略**

1. **阶数自适应**：低阶启动，逐步提高阶数至稳定极限
2. **步长控制**：$\Delta t_{\text{new}} = \Delta t_{\text{old}}(\tau/\text{LTE})^{1/(p+1)}$
3. **稳定性监控**：检测特征根位置，必要时降阶

**在EMT中的应用**

- 适用于刚性系统(时间常数比$10^3$-$10^6$)
- 多步法需启动过程（从低阶开始）
- 阶数越高稳定性越差，通常不超过3阶

### 2.4 Runge-Kutta方法在EMT中的局限

**显式Runge-Kutta的局限性**

- **条件稳定**：稳定性受CFL条件限制，步长必须小于最小时间常数
- **刚性问题**：对刚性系统需极小步长，效率极低
- **不适合EMT**：电力系统普遍存在刚性，显式RK不实用

**隐式Runge-Kutta的优势**

- **无条件稳定**：适合刚性系统
- **阶段计算**：每步需多次求解隐式方程
- **对角隐式结构**：DIRK方法可顺序求解各阶段

### 2.5 对角隐式Runge-Kutta(DIRK)方法

**2S-DIRK(二阶)**

核心参数：$\gamma = 1 - 1/\sqrt{2} \approx 0.2929$

两阶段公式：

$$
\begin{aligned}
\tilde{x} &= x_{n-1} + \gamma \Delta t \cdot f(t_{n-1} + \gamma \Delta t, \tilde{x}) \\
\bar{x} &= (1+\sqrt{2})\tilde{x} - \sqrt{2}x_{n-1} \\
x_n &= \bar{x} + \gamma \Delta t \cdot f(t_n, x_n)
\end{aligned}
$$

**关键优势**：
- 二阶精度，L稳定（无持续数值振荡）
- 线性L/C两阶段导纳相同，矩阵不需重新分解
- 相比CDA无需突变检测

**3S-SDIRK(三阶)**

核心参数：$\alpha = 0.4358665215$

- 三阶精度，L稳定
- 三个阶段时间点：$t + 0.4359\Delta t$、$t + 0.7179\Delta t$、$t + \Delta t$
- 适合大步长EMT仿真

**Butcher表**

$$
\begin{array}{c|ccc}
\alpha & \alpha & 0 & 0 \\
(1+\alpha)/2 & (1-\alpha)/2 & \alpha & 0 \\
1 & b_1 & b_2 & \alpha \\ \hline
& b_1 & b_2 & \alpha
\end{array}
$$

### 2.6 指数积分器(Exponential Integrator)

**基本原理**

利用矩阵指数精确传播线性部分：

$$
x_{n+1} = e^{\Delta t \cdot A}x_n + \Delta t \cdot \varphi(\Delta t \cdot A)B u_n
$$

其中$\varphi(z) = (e^z - 1)/z$为指数积分函数。

**在EMT中的应用**

- 适用于线性时不变(LTI)网络
- 对刚性系统可放宽步长限制10-100倍
- 计算瓶颈：大规模矩阵指数的高效计算

**Krylov子空间方法**

使用Arnoldi迭代近似矩阵指数：

$$
e^{hA}v \approx V_m e^{hH_m}e_1
$$

其中$V_m$为Krylov子空间基，$H_m$为上Hessenberg矩阵。

### 2.7 数值积分方法的对比与选择准则

**方法综合对比**

| 方法 | 阶数 | 稳定性 | 阻尼 | 计算量 | 推荐场景 |
|------|-----|--------|------|--------|---------|
| 梯形法 | 2 | A稳定 | 无 | 1× | 通用EMT首选 |
| 后向欧拉 | 1 | L稳定 | 强 | 1× | 初始化、CDA |
| 2S-DIRK | 2 | L稳定 | 强 | 2× | 电力电子 |
| 3S-SDIRK | 3 | L稳定 | 强 | 3× | 大步长需求 |
| Gear/BDF | 2-3 | 刚性稳定 | 可调 | 1× | 刚性系统 |
| 指数积分 | - | 精确 | - | - | LTI子系统 |

**选择决策树**

```
是否含频繁开关/电力电子？
├─ 是 → 是否需求大步长？
│  ├─ 是 → 3S-SDIRK
│  └─ 否 → 2S-DIRK
└─ 否 → 是否刚性系统？
   ├─ 是 → Gear/BDF
   └─ 否 → 梯形法
```

### 2.8 步长选择的理论与实践

**理论约束**

| 约束类型 | 公式 | 工程取值 |
|---------|------|---------|
| 奈奎斯特准则 | $\Delta t \leq 1/(2f_{max})$ | $\Delta t \leq \pi/\omega_{max}$ |
| 精度要求 | LTE < τ | 相对误差<1% |
| 开关频率 | $\Delta t < 1/(10f_{sw})$ | IGBT: $\Delta t$<100 μs |
| 控制带宽 | $\Delta t < 1/(10f_{bw})$ | 快速控制: $\Delta t$<50 μs |
| 行波传播 | $\Delta t < \tau_d$ | 线长<波长/10 |

**典型步长配置**

| 应用场景 | 步长 | 选择依据 |
|---------|------|---------|
| 工频输电网络 | 50-100 μs | 工频周期1/200-1/400 |
| MMC详细建模 | 10-20 μs | 子模块电容电压波动 |
| 两电平VSC | 1-10 μs | 开关暂态细节 |
| 实时仿真 | 20-50 μs | 实时约束 |
| 大步长仿真 | 200-500 μs | 3S-SDIRK |

**自适应步长控制**

误差估计与步长调整：

$$
\text{LTE} = \frac{\|x_{n+1}^{(p+1)} - x_{n+1}^{(p)}\|}{2^p - 1}
$$

$$
\Delta t_{\text{new}} = \Delta t_{\text{old}}\left(\frac{\tau}{\text{LTE}}\right)^{1/(p+1)}
$$

## 适用边界

- 梯形法不适合含频繁开关的电力电子仿真，需配合CDA或改用L稳定方法
- 后向欧拉1阶精度限制，不适合高精度长期仿真
- DIRK方法每步多阶段计算，适合离线仿真而非硬实时
- Gear多步法在事件后需重新启动，不适合开关频繁场景
- 指数积分器目前仅适用于线性子系统，非线性扩展仍在研究

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[numerical-integration-by-the-2-stage-diagonally]] | 2008 | 将2S-DIRK引入EMT，提出L稳定二阶积分方法 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] | 2021 | 3S-SDIRK用于移频EMT，实现三阶L稳定大步长仿真 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations]] | 2014 | 2S-DIRK在EMT中的补充技术，电源与开关处理 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] | 2025 | 动态相量数值积分与步长选择理论 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn]] | 2023 | 紧凑格式兼顾稳定性与突变处理 |

## 技术演进脉络

### 1969-1980年代：经典方法确立
- **梯形法确立** (1969)
  - Dommel提出梯形法作为EMTP标准积分方法
  - 二阶精度、A稳定、计算简单
- **后向欧拉应用** (1970s)
  - 用于初始化求解稳态
  - L稳定特性抑制振荡

### 1980-2000年代：振荡抑制研究
- **CDA方法** (1980s)
  - 临界阻尼调整技术
  - 事件点后插入半步长BE
- **Gear法引入** (1990s)
  - 刚性系统求解
  - 变阶变步长策略

### 2000-2015年：DIRK方法引入
- **2S-DIRK** (2008)
  - T.Noda引入EMT仿真
  - L稳定二阶精度
  - 无需事件检测
- **混合积分策略** (2010s)
  - 梯形法+DIRK组合
  - 按元件类型选择方法

### 2015-2026年：高阶与大步长
- **3S-SDIRK** (2020-2021)
  - 三阶L稳定
  - 适合移频EMT大步长仿真
- **紧凑格式** (2023)
  - 兼顾精度与稳定性
  - 突变处理能力

## 关键发现汇总

### 数值稳定性理论
- **[1969]** 梯形法A稳定但非L稳定，突变后产生持续数值振荡
- **[2008]** 2S-DIRK同时实现二阶精度与L稳定，从根本上消除振荡
- **[2021]** 3S-SDIRK达到三阶L稳定，允许更大步长同时保持精度

### 方法对比结论
- **[2008]** 2S-DIRK计算量为梯形法2倍，但无需振荡检测，综合效率相当
- **[2014]** CDA依赖突变检测，控制系统限幅导致的突变可能遗漏；2S-DIRK无需检测
- **[2021]** 在相同精度要求下，3S-SDIRK可比二阶方法采用大1.5-2倍步长

### 步长选择准则
- **[2025]** 步长选择需综合考虑：奈奎斯特准则、精度要求、开关频率、控制带宽
- **[2023]** 梯形法在步长$\Delta t < T_{sw}/10$时可较好表示开关暂态
- **[2021]** 移频EMT结合3S-SDIRK可使用500μs级步长，效率提升5-10倍

### 前沿研究方向
- **指数积分器**：利用矩阵指数精确传播，适合线性子系统大步长仿真
- **自适应混合积分**：根据局部刚性自动选择积分方法
- **机器学习步长控制**：基于系统状态预测最优步长
- **量子计算积分**：利用量子优势加速大规模DAE求解

## 深度增强内容

### 1. 稳定性函数详解

**线性测试方程**

$$
\dot{x} = \lambda x, \quad \text{Re}(\lambda) < 0
$$

应用数值方法得离散形式：

$$
x_{n+1} = R(z)x_n, \quad z = \lambda \Delta t
$$

**各方法稳定性函数**

| 方法 | $R(z)$ | $R(-\infty)$ | 稳定性类型 |
|------|--------|--------------|-----------|
| 梯形法 | $\frac{1+z/2}{1-z/2}$ | -1 | A稳定 |
| 后向欧拉 | $\frac{1}{1-z}$ | 0 | L稳定 |
| 2S-DIRK | $\frac{1+(1-2\gamma)z}{(1-\gamma z)^2}$ | 0 | L稳定 |
| 3S-SDIRK | 有理函数 | 0 | L稳定 |

**稳定区域图示**

- A稳定：稳定区域包含整个左半平面
- L稳定：A稳定 + $R(-\infty) = 0$

### 2. 局部截断误差分析

**定义**

局部截断误差(LTE)表示单步引入的误差：

$$
\text{LTE} = x(t_{n+1}) - x_{n+1} = C_p \Delta t^{p+1} x^{(p+1)}(t_n) + O(\Delta t^{p+2})
$$

**误差常数**

| 方法 | 阶数$p$ | 误差常数$C_p$ |
|------|--------|---------------|
| 后向欧拉 | 1 | $-1/2$ |
| 梯形法 | 2 | $-1/12$ |
| 2S-DIRK | 2 | 可调(依赖$\gamma$) |
| 3S-SDIRK | 3 | 可调(依赖$\alpha$) |

**误差估计方法**

嵌入式方法：使用$p$阶和$p+1$阶公式对比

$$
\text{LTE} \approx \|x_{n+1}^{(p+1)} - x_{n+1}^{(p)}\|
$$

### 3. 混合积分策略实现

**元件级混合**

```
网络分区：
├─ 线性输电网：梯形法(大步长)
├─ 发电机：梯形法(详细模型)
├─ 换流器：2S-DIRK(开关频繁)
└─ 控制系统：前向欧拉(显式)
```

**时间级混合**

- 正常工况：梯形法(二阶精度)
- 事件前1-2步：切换2S-DIRK(L稳定)
- 事件后恢复期：切回梯形法

**接口处理**

不同积分方法子系统间的数据交换：
- 插值：从大步长系统获取小步长时刻值
- 外推：预测小步长系统未来值
- 稳定性保证：接口处需特殊处理防止失稳

### 4. 数值振荡识别与抑制

**振荡识别准则**

- 波形出现高频振荡(频率接近奈奎斯特频率)
- 振荡幅值不随时间衰减
- 改变步长后振荡频率改变

**抑制方法对比**

| 方法 | 原理 | 精度影响 | 实现复杂度 |
|------|------|---------|-----------|
| CDA | 事件后插入半步长BE | 保持2阶 | 需事件检测 |
| 2S-DIRK | L稳定格式本身阻尼 | 2阶 | 标准实现 |
| 人工阻尼 | 增加虚拟电阻 | 降低精度 | 简单 |
| 滤波后处理 | 低通滤波 | 可能失真 | 额外计算 |

### 5. 实时仿真特殊考量

**确定性要求**

- 每步计算时间必须小于步长
- 避免迭代(使用预测-校正或直接法)
- 固定导纳矩阵减少分解开销

**实时积分方法选择**

| 方法 | 实时适用性 | 原因 |
|------|-----------|------|
| 梯形法 | ★★★★★ | 单步、确定 |
| 2S-DIRK | ★★★ | 两阶段、计算量大 |
| 3S-SDIRK | ★★ | 三阶段、开销大 |

### 6. 步长优化算法

**变步长控制流程**

```
每步执行：
1. 用当前步长计算新状态
2. 估计局部截断误差LTE
3. 若LTE > τ_max：拒绝该步，减小步长重算
4. 若LTE < τ_min：接受该步，增大步长
5. 否则：接受该步，保持步长
```

**步长限制**

```
Δt_min ≤ Δt_new ≤ Δt_max
Δt_new ≤ c·Δt_old  (变化率限制，通常c=2)
```

## 相关方法
- [[numerical-integration]] - 基础方法详细说明
- [[nodal-analysis]] - 积分后的网络求解
- [[state-space-method]] - 状态空间积分实现
- [[fixed-admittance]] - 固定导纳积分形式
- [[multirate-method]] - 不同步长的积分协调
- [[stiff-system-handling]] - 刚性问题的积分策略
- [[discretization-methods]] - 积分方法的电路实现

## 相关模型
- [[synchronous-machine-model]] - 电机暂态数值积分
- [[mmc-model]] - 模块化换流器多速率积分
- [[vsc-model]] - 变流器开关积分策略
- [[transmission-line-model]] - 线路Bergeron模型积分
- [[transformer-model]] - 变压器暂态积分方法

## 相关主题
- [[emt-mathematical-foundation]] - 数值积分数学背景
- [[dynamic-phasor]] - 相量域的积分方法
- [[real-time-simulation]] - 实时约束下的积分选择
- [[parallel-computing]] - 并行积分算法
- [[frequency-dependent-modeling]] - 频变模型积分

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第一篇第2章"数值积分方法"*
