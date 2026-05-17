---
title: "EMT 数学基础 (EMT Mathematical Foundation)"
type: topic
tags: [mathematical-foundation, differential-equations, numerical-analysis, circuit-theory, laplace-transform, dae, nodal-analysis, state-space, trapezoidal-rule, gear-method]
created: "2026-05-01"
book-chapter: "1"
---

# EMT 数学基础 (EMT Mathematical Foundation)

## 定义

电磁暂态（Electromagnetic Transient, EMT）仿真的数学基础是理解和实现高精度仿真的根基。EMT仿真本质上是求解由电路拓扑约束形成的微分-代数方程组（DAEs），涉及常微分方程（ODEs）理论、数值分析方法、频域变换和矩阵计算等多个数学领域。

在EMT语境下，数学基础包括：电路元件的伏安特性建模、网络拓扑的图论表示、微分方程的数值积分、频域与时域的转换方法，以及大规模方程组的稀疏矩阵技术。这些数学工具共同构成了从物理现象到数值实现的桥梁。

## EMT 中的角色

EMT数学基础在整个EMT仿真体系中处于**底层支撑**位置：

1. **电路方程建立**：所有EMT仿真程序都从电路方程出发，数学基础决定了如何将物理电路转换为可求解的数学形式
2. **数值积分选择**：不同积分方法（梯形法/Gear法/DIRK方法）的精度、稳定性特性直接影响仿真结果的可信度
3. **开关不连续处理**：数值振荡抑制（CDA）和开关插值方法都是基于数学基础理论的工程应用
4. **大规模系统求解**：稀疏矩阵技术、节点分析法、状态空间法都是为了高效求解大规模方程组

**核心挑战**：
- 梯形积分法在开关不连续点产生持续数值振荡（Marti 2004）
- 刚性系统对数值积分方法的稳定性要求严苛
- 大规模网络的计算效率瓶颈

**关键需求**：
- A-稳定或L-稳定的数值积分方法
- 局部数值阻尼技术（CDA）在不连续点快速衰减高频模态
- 稀疏矩阵技术充分利用网络稀疏性

## EMT 建模方法与核心机制

### 2.1 电磁暂态的数学描述

电力系统的电磁暂态本质上是电磁场能量在元件间的快速交换过程。从数学角度，可以用**微分方程组**描述：

$$\frac{d\mathbf{x}}{dt} = \mathbf{f}(\mathbf{x}, \mathbf{u}, t)$$

其中$\mathbf{x}$为状态变量（电感电流、电容电压），$\mathbf{u}$为输入变量（电源电压、开关状态），$t$为时间。

**集总参数电路的基本约束**：
- **KCL（基尔霍夫电流定律）**：$\sum i_k = 0$
- **KVL（基尔霍夫电压定律）**：$\sum v_k = 0$
- **元件特性**：$v = Ri$（电阻），$v = L\frac{di}{dt}$（电感），$i = C\frac{dv}{dt}$（电容）

### 2.2 微分-代数方程组（DAEs）

EMT网络可表示为**微分-代数方程组（DAEs）**：

$$\begin{cases} \mathbf{E}\frac{d\mathbf{x}}{dt} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u} \\ \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u} \end{cases}$$

**微分指数（Differential Index）**：
- 指数-1系统：通过一次微分可转化为ODEs，最常见
- 指数-2系统：需要两次微分，含约束条件
- EMT网络通常为指数-1或-2

### 2.3 节点法（Nodal Analysis）

**核心思想**：以节点电压为未知量，KCL列方程

$$\mathbf{Y}\mathbf{V} = \mathbf{I}$$

**等效电导与历史电流源**（梯形积分）：
- 电感：$G_{L} = \frac{\Delta t}{2L}$，$h_{L}(t) = i(t-\Delta t) + \frac{\Delta t}{2L}v(t-\Delta t)$
- 电容：$G_{C} = \frac{2C}{\Delta t}$，$h_{C}(t) = i(t-\Delta t) - \frac{2C}{\Delta t}v(t-\Delta t)$

**节点法优缺点**：

| 特性 | 说明 |
|------|------|
| 方程规模 | 节点数（较少） |
| 稀疏性 | 高度稀疏 |
| 开关处理 | 需重分解导纳矩阵 |
| 实时仿真 | 更适合固定步长 |

### 2.4 状态空间法（State-Space Method）

**核心思想**：以状态变量（电感电流、电容电压）为未知量

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

**状态空间-节点联合法（SSN）**（Dufour 2011）：
- 将状态空间电气集群通过梯形积分离散化，转化为离散伴随支路等效形式
- 灵活映射至全局节点导纳矩阵，支持V型（诺顿）/I型（戴维南）及混合型集群
- 开关组合预计算矩阵数量从$2^6=64$降至$2^4=16$，内存需求降低75%

### 2.5 数值积分方法

#### 梯形积分法（Trapezoidal Rule）

差分方程：
$$i(t) - i(t-\Delta t) = \frac{\Delta t}{2L}[u(t) + u(t-\Delta t)]$$

Z域传递函数：
$$H(z) = \frac{\Delta t}{2L} \cdot \frac{z+1}{z-1}$$

**特性**：
- 二阶精度，局部截断误差$O(\Delta t^3)$
- A-稳定（A-stable），整个左半平面
- **问题**：在开关不连续点可能产生持续数值振荡

#### 后向欧拉法（Backward Euler）

差分方程：
$$i(t) - i(t-\Delta t) = \frac{\Delta t}{L}u(t)$$

Z域传递函数：
$$H(z) = \frac{\Delta t}{L} \cdot \frac{z}{z-1}$$

**特性**：
- 一阶精度
- L-稳定（L-stable），极点在$z=1$处提供完全临界阻尼
- **优势**：在恰好两个时间步长内提供完全阻尼（$\zeta=1.0$，超调量0%）

#### 临界阻尼调整（CDA）算法

**核心机制**（Marti 2004）：
1. 检测到不连续点（电感电流开断或电容电压突加）时，临时切换为后向欧拉法
2. 执行两个半步长（$\Delta t/2$）的积分步骤
3. 利用后向欧拉的L-稳定特性，在一个时间步长内消除数值振荡
4. 自动恢复梯形法继续仿真

**计算开销**：CDA仅在检测到不连续点时触发（通常<1%的时间步），整体计算开销增加<2%

#### 三阶单对角隐式Runge-Kutta法（3S-SDIRK）

**核心参数**（Gao 2021）：
- $\alpha = 0.435866521508459$（单对角元值）
- 三阶精度，局部截断误差$O(\Delta t^4)$
- L-稳定，稳定性函数在无穷远处为零

**Butcher表**：

$$\begin{array}{c|ccc} \alpha & \alpha & 0 & 0 \\ (1+\alpha)/2 & (1-\alpha)/2 & \alpha & 0 \\ 1 & b_1 & b_2 & \alpha \\ \hline & b_1 & b_2 & \alpha \end{array}$$

### 2.6 频域分析与复频域变换

**拉普拉斯变换（Laplace Transform）**：
- 定义：$F(s) = \int_0^{\infty} f(t)e^{-st}dt$
- 微分特性：$\mathcal{L}[\frac{df}{dt}] = sF(s) - f(0)$
- 应用：频变参数建模、传递函数分析

**频域阻抗建模**：
- 电阻：$Z_R = R$
- 电感：$Z_L = sL$
- 电容：$Z_C = \frac{1}{sC}$
- 频变元件：$Z(s)$通过测量或解析公式获得

**傅里叶变换（Fourier Transform）**：
- 稳态谐波分析
- 频谱特性评估
- 与拉普拉斯变换的关系：$s = j\omega$

## 形式化表达

### 核心方程汇总

**时域状态方程**：
$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

**梯形法离散伴随支路**：
$$i_k = \underbrace{\frac{\Delta t}{2L}}_{G_L} v_k + \underbrace{\left[i_{k-1} + \frac{\Delta t}{2L}v_{k-1}\right]}_{h_L(k)}$$

**后向欧拉半步长（用于CDA）**：
$$i_{n+\frac{1}{2}} = \frac{\Delta t/2}{L}v_{n+\frac{1}{2}} + i_n$$

**节点导纳方程**：
$$[\mathbf{G}]\mathbf{v}(t) = \mathbf{i}_s(t) + \mathbf{h}(t)$$

**CQLF稳定性判据**（Zhao 2020）：
$$V(x) = x^T P x, \quad \dot{V}(x) = x^T(A_i^T P + P A_i)x < 0, \forall i \in \mathcal{P}$$

## 关键技术挑战

### 挑战1：数值振荡抑制

梯形积分法在开关不连续点处可能被迫表现为"纯微分器"，产生有界但持续的数值振荡。传统全局阻尼方法会引入相位误差（0.5°-1.2°）。CDA方法通过在不连续点局部切换为后向欧拉法，在不损失正常响应精度的前提下彻底抑制振荡。

**量化边界**：CDA在2-3个步长内将振荡衰减至机器精度（$<10^{-12}$），而纯梯形法振幅约为稳态值的±15-30%

### 挑战2：刚性系统数值稳定性

EMT系统的时间常数跨度极大（从微秒级开关到秒级暂态），形成高度刚性系统。Gear方法族通过变阶数自适应平衡精度与稳定性，是处理刚性系统的标准选择。

**量化边界**：刚性比可达$10^3$至$10^6$（最大/最小时间常数比）

### 挑战3：开关时刻定位精度

开关动作时刻通常不落在固定时间步长网格上。强制将开关推到最近的网格点会产生电流截断或非特征谐波。插值方法可精确定位开关时刻，但需要正确更新历史项。

**量化边界**：线性插值具有$O(\Delta t^2)$局部误差阶；两阶段插值方法可将精度提升至二阶，误差系数约为标准方法的0.25-0.3倍

### 挑战4：大规模稀疏矩阵求解

EMT网络方程组规模可达数千至数万节点。稀疏矩阵技术的选择（LDL分解、LU分解、迭代法）直接影响计算效率。

**量化边界**：节点法在大规模网络（>1000节点）比状态空间法快5-10倍

### 挑战5：频变参数的时域卷积

频变传输线参数（如大地回路阻抗）需要在时域中以卷积形式处理。瞬态电阻矩阵方法将频变性集中到$R'(s)$，避免同时拟合特性导纳和传播函数。

**量化边界**：瞬态电阻矩阵有理拟合仅需实极点，避免了数值振荡

## 量化性能边界

### 数值积分方法对比

| 方法 | 精度阶数 | 稳定区域 | 数值阻尼 | 计算开销 | 典型应用 |
|------|---------|---------|---------|---------|---------|
| 梯形法（TR） | 2阶 | A-稳定 | 无 | 低 | 常规EMT仿真 |
| 后向欧拉（BE） | 1阶 | L-稳定 | 完全 | 低 | CDA阻尼步骤 |
| Gear法 | 自适应1-6阶 | A(α)-稳定 | 可调 | 高 | 刚性系统 |
| 3S-SDIRK | 3阶 | L-稳定 | 完全 | 中 | SFEMT大步长 |
| 2S-DIRK | 2阶 | L-稳定 | 完全 | 中 | 开关不连续 |

### CDA性能数据

| 指标 | 数值 | 说明 |
|------|------|------|
| 振荡衰减时间 | 2个时间步长 | 完成临界阻尼 |
| 计算开销增加 | <2% | 仅在不连续点触发 |
| 相位误差 | <0.1° | 恢复正常后 |
| 阻尼比 | ζ=1.0 | 完全临界阻尼 |

### SSN方法性能数据

| 指标 | 数值 | 说明 |
|------|------|------|
| 预计算矩阵缩减 | 75% | 从$2^6$降至$2^4$ |
| 内存降低 | 75% | 三相示例 |
| 最坏计算步长 | 10-21 μs | HVDC/断路器测试 |
| 并行加速比 | ~2.5倍 | 多核架构 |

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 关键考量 |
|---------|---------|---------|
| 大规模线性网络 | 节点法+稀疏矩阵 | 稀疏性利用，效率高 |
| 含电力电子开关 | 梯形法+CDA | 抑制数值振荡，保持精度 |
| 刚性系统 | Gear法/3S-SDIRK | 变阶数自适应，L-稳定 |
| 实时仿真 | 节点法+固定导纳 | 确定性延迟，固定步长 |
| 控制器分析与设计 | 状态空间法 | 特征值分析，便于控制设计 |
| 频率扫描 | 频域法+拉普拉斯变换 | 稳态谐波分析 |
| 宽频建模 | 频域法+有理函数拟合 | 精度与效率平衡 |

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入层：物理系统 -->
  <rect x="300" y="20" width="300" height="70" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">物理系统输入</text>
  <text x="450" y="65" text-anchor="middle" font-size="11" fill="#3b82f6">电路拓扑 + 元件参数 + 初始条件</text>

  <!-- 箭头1 -->
  <line x1="450" y1="90" x2="450" y2="120" stroke="#333" stroke-width="2"/>
  <polygon points="450,125 445,115 455,115" fill="#333"/>

  <!-- 第一层：方程建立 -->
  <rect x="300" y="130" width="300" height="70" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="155" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">第一层：方程建立</text>
  <text x="450" y="175" text-anchor="middle" font-size="11" fill="#b45309">KCL/KVL约束 → 微分方程组</text>

  <!-- 箭头2 -->
  <line x1="450" y1="200" x2="450" y2="230" stroke="#333" stroke-width="2"/>
  <polygon points="450,235 445,225 455,225" fill="#333"/>

  <!-- 第二层：数学形式 -->
  <rect x="300" y="240" width="300" height="70" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="265" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534">第二层：数学形式</text>
  <text x="450" y="285" text-anchor="middle" font-size="11" fill="#15803d">DAEs / ODEs / 状态空间 / 节点方程</text>

  <!-- 三个方法卡片 -->
  <line x1="450" y1="310" x2="450" y2="340" stroke="#333" stroke-width="2"/>
  <polygon points="450,345 445,335 455,335" fill="#333"/>

  <!-- 三列方法 -->
  <rect x="50" y="350" width="250" height="100" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="175" y="375" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">节点法</text>
  <text x="175" y="395" text-anchor="middle" font-size="10" fill="#92400e">YV = I</text>
  <text x="175" y="415" text-anchor="middle" font-size="10" fill="#b45309">高度稀疏</text>
  <text x="175" y="435" text-anchor="middle" font-size="10" fill="#b45309">实时仿真</text>

  <rect x="325" y="350" width="250" height="100" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="375" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">状态空间法</text>
  <text x="450" y="395" text-anchor="middle" font-size="10" fill="#92400e">ẋ = Ax + Bu</text>
  <text x="450" y="415" text-anchor="middle" font-size="10" fill="#b45309">积分器选择灵活</text>
  <text x="450" y="435" text-anchor="middle" font-size="10" fill="#b45309">控制设计友好</text>

  <rect x="600" y="350" width="250" height="100" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="725" y="375" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">SSN联合法</text>
  <text x="725" y="395" text-anchor="middle" font-size="10" fill="#92400e">梯形离散伴随</text>
  <text x="725" y="415" text-anchor="middle" font-size="10" fill="#b45309">分组并行</text>
  <text x="725" y="435" text-anchor="middle" font-size="10" fill="#b45309">内存降低75%</text>

  <!-- 输出箭头 -->
  <line x1="450" y1="450" x2="450" y2="480" stroke="#333" stroke-width="2"/>
  <polygon points="450,485 445,475 455,475" fill="#333"/>

  <!-- 第三层：数值积分 -->
  <rect x="300" y="490" width="300" height="70" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="515" text-anchor="middle" font-size="14" font-weight="bold" fill="#6d28d9">第三层：数值积分</text>
  <text x="450" y="535" text-anchor="middle" font-size="11" fill="#7c3aed">TR / BE / Gear / 3S-SDIRK / CDA</text>

  <!-- 底部量化性能 -->
  <line x1="450" y1="560" x2="450" y2="580" stroke="#333" stroke-width="2"/>
  <polygon points="450,585 445,575 455,575" fill="#333"/>

  <rect x="200" y="590" width="500" height="50" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="610" text-anchor="middle" font-size="11" fill="#6d28d9">量化输出：节点电压 / 支路电流 / 时域波形 / 频域阻抗</text>
  <text x="450" y="628" text-anchor="middle" font-size="10" fill="#8b5cf6">精度误差 / 仿真时间 / 内存占用 / 数值稳定性</text>

  <!-- 图例 -->
  <rect x="50" y="560" width="15" height="15" fill="#dbeafe" stroke="#2563eb"/>
  <text x="70" y="572" font-size="10" fill="#333">输入</text>
  <rect x="130" y="560" width="15" height="15" fill="#fef3c7" stroke="#d97706"/>
  <text x="150" y="572" font-size="10" fill="#333">方法</text>
  <rect x="200" y="560" width="15" height="15" fill="#dcfce7" stroke="#16a34a"/>
  <text x="220" y="572" font-size="10" fill="#333">数学形式</text>
  <rect x="290" y="560" width="15" height="15" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="310" y="572" font-size="10" fill="#333">数值求解</text>
  <rect x="380" y="560" width="15" height="15" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="400" y="572" font-size="10" fill="#333">输出</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EMT数学基础三层架构：物理系统 → 数学形式 → 数值积分 → 量化输出。节点法/状态空间法/SSN联合法为三种核心求解范式，CDA和3S-SDIRK为关键数值技术。</p>

## 相关方法

- [[state-space-method]] - 状态空间建模与分析
- [[nodal-analysis]] - 节点导纳矩阵方法
- [[numerical-integration]] - 梯形法、Gear法等
- [[vector-fitting]] - 频域有理函数逼近
- [[sparse-matrix-solver]] - 大规模方程组求解
- [[companion-circuit]] - 离散伴随电路方法

## 相关模型

- [[transmission-line-model]] - 分布参数电路
- [[transformer-model]] - 磁耦合元件
- [[synchronous-machine-model]] - 旋转电机
- [[vsc-model]] - 电力电子设备

## 相关主题

- [[numerical-integration-methods]] - 积分算法详解
- [[frequency-dependent-modeling]] - 宽频建模
- [[model-order-reduction]] - 简化与加速
- [[parallel-computing]] - 高效求解
- [[real-time-simulation]] - 实时仿真

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第一篇第1章"电磁暂态的数学基础"*

## 来源论文

| 论文 | 年份 | 关联要点 |
|------|------|---------|
| Marti 2004 - Suppression of numerical oscillations in the EMTP power systems | 2004 | CDA临界阻尼调整算法，系统性解决梯形法数值振荡问题 |
| Dufour 2011 - A combined state-space nodal method for the simulation of power system transients | 2011 | SSN联合求解法，状态空间集群与节点法自然耦合 |
| Gao 2021 - Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling | 2021 | 3S-SDIRK三阶隐式Runge-Kutta，移频大步长EMT |
| Zhao 2020 - Stability Evaluation of Interpolation, Extrpolation, and Numerical Oscillation Damping Methods Applied in EMT Simulation | 2020 | CQLF公共二次李雅普诺夫函数稳定性理论 |