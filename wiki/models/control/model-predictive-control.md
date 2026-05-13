---
title: "模型预测控制 (Model Predictive Control)"
type: model
tags: [model-predictive-control, mpc, optimal-control, receding-horizon, finite-set-mpc, predictive-control, power-electronics]
created: "2026-05-04"
updated: "2026-05-13"
---

# 模型预测控制 (Model Predictive Control)

## 定义与边界

模型预测控制（Model Predictive Control, MPC）是一种基于**系统模型**和**滚动优化**策略的控制方法。其核心思想是：在每个控制周期，利用系统模型预测未来一段时间（预测时域 $P$）内系统的行为，求解一个开环最优控制问题，得到最优控制序列，但只将第一个控制动作施加到被控对象上；在下一个周期，基于新的测量值重新求解最优控制问题（滚动时域特性）。

**在EMT中的定位**：MPC在EMT仿真中主要用于电力电子换流器（VSC、MMC、DC-DC等）的高性能控制建模。与传统的PI/矢量控制不同，MPC能够显式处理约束条件（电流限幅、电压饱和、开关频率限制等），并在多目标优化中实现精确的动态性能。

**边界限定**：本页面聚焦于EMT仿真中的MPC**控制模型**（即MPC算法如何被建模为电力系统仿真中的动态环节），而非MPC算法本身的数值求解方法。MPC的EMT建模关注的是：预测模型的形式、优化问题的离散化、控制律的等效电路/代数方程表示。

## EMT中的作用

### 为什么需要MPC建模

传统PI控制在EMT仿真中计算效率高（简单的代数方程+一阶微分方程），但存在以下局限：
- 无法显式处理约束（如电流限幅、开关频率限制）
- 多变量耦合系统需要额外的解耦环节
- 非线性系统需要增益调度或多工作点线性化

MPC通过**预测模型+优化求解**直接处理这些问题，在EMT仿真中表现为：
1. **预测模型**：需要内嵌被控对象（如LCL滤波器、电机、电网）的离散时间模型
2. **优化求解**：在EMT时间步长内完成滚动优化计算
3. **控制输出**：最优控制序列的第一个动作作为当前时刻的控制量

### 核心挑战

- **计算实时性**：EMT仿真时间步长通常为10-100 μs，MPC必须在每个步长内完成预测和优化
- **预测模型精度**：预测模型与被控对象的偏差会导致性能下降甚至不稳定
- **约束处理**：不等式约束（电流、电压、开关频率）需要特殊的优化算法
- **多时间尺度**：控制周期（kHz级）与EMT步长（μs级）之间的匹配

## EMT建模方法

### 方法1：有限集模型预测控制（FCS-MPC）

有限集MPC（Finite Control Set MPC, FCS-MPC）是电力电子领域最常用的MPC变体，特别适用于开关器件的直接控制。

**原理**：在每步优化中，枚举所有可能的开关状态组合，评估每个状态下的预测性能指标，选择最优开关状态直接驱动电力电子器件。

**预测模型**（以三相VSC为例）：

电网侧LCL滤波器的离散时间模型（基于向后欧拉法）：

$$i_g(k+1) = A_g i_g(k) + B_g v_c(k) + B_g v_g(k)$$

$$v_c(k+1) = v_c(k) + \frac{T_s}{C_f}(i_c(k))$$

$$i_c(k+1) = A_c i_c(k) + B_c v_c(k) + B_c (v_i(k) - v_g(k))$$

其中 $T_s$ 为控制周期，$A_g, B_g, A_c, B_c$ 为由LCL参数和离散化方法确定的系统矩阵。

**代价函数**：

$$J(k) = \lambda_i \| i_g^* - i_g(k+1) \|^2 + \lambda_v \| v_{dc}^* - v_{dc}(k+1) \|^2 + \lambda_f \sum_{j=1}^{6} |f_j(k+1) - f_j(k)|$$

其中 $\lambda_i, \lambda_v, \lambda_f$ 分别为电流、直流电压和开关频率变化的权重系数，$f_j$ 为第 $j$ 个开关器件的状态（0或1）。

**特点**：
- 优点：开关状态直接输出，无需PWM调制环节；天然处理约束
- 缺点：计算量随开关状态数指数增长（6器件VSC有 $2^6=64$ 种状态）
- 适用场景：中低功率电力电子装置（<10 MW），开关频率较低（<10 kHz）

### 方法2：连续集模型预测控制（CCS-MPC）

连续集MPC（Continuous Control Set MPC, CCS-MPC）将开关器件建模为连续控制量，通过PWM调制环节产生开关信号。

**预测模型**（以电流跟踪为例）：

$$i(k+1) = (A - BK)i(k) + B u(k) + A x_{ref}(k)$$

**代价函数**（二次规划形式）：

$$\min_u J(k) = (r(k+1) - y(k+1))^T Q (r(k+1) - y(k+1)) + u(k)^T R u(k)$$

**求解**：通过解析解（无约束）或二次规划（QP，有约束）得到最优连续控制量 $u^*(k)$，再经PWM调制得到开关信号。

**特点**：
- 优点：计算量小（O(n³)而非指数增长），适合高功率系统
- 缺点：忽略开关离散性，可能存在稳态纹波
- 适用场景：高功率VSC-HVDC、STATCOM等（>100 MW）

### 方法3：基于伴随变量的MPC（Adjoint-based MPC）

对于大规模系统，直接枚举或QP求解计算量过大，可采用伴随变量法近似梯度，结合梯度下降法求解优化问题。

**核心思想**：

$$\frac{\partial J}{\partial u} = \frac{\partial J}{\partial x} \frac{\partial x}{\partial u} \approx \lambda^T \frac{\partial x}{\partial u}$$

其中 $\lambda$ 为伴随变量，通过伴随方程反向传播得到。

**特点**：
- 优点：计算复杂度与系统维度成线性关系
- 缺点：仅适用于大规模优化问题，实现复杂
- 适用场景：多端直流电网、大规模微电网

## 形式化表达

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>
    </filter>
  </defs>

  <text x="400" y="25" fill="#1a1a2e" font-size="14" font-weight="bold" text-anchor="middle">图1 · 模型预测控制（MPC）通用框架</text>

  <rect x="20" y="160" width="100" height="50" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="70" y="180" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">参考信号</text>
  <text x="70" y="198" fill="#4b6b8f" font-size="9" text-anchor="middle">r(k), r(k+1)...</text>

  <circle cx="160" cy="185" r="15" fill="#fff" stroke="#333" stroke-width="1.5"/>
  <text x="155" y="189" fill="#333" font-size="12" font-weight="bold" text-anchor="middle">+</text>
  <text x="155" y="175" fill="#333" font-size="8">-</text>

  <rect x="220" y="140" width="140" height="90" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="290" y="165" fill="#78350f" font-size="13" font-weight="bold" text-anchor="middle">MPC优化器</text>
  <text x="290" y="183" fill="#a16207" font-size="9" text-anchor="middle">min J = Σ ℓ(x,u) + Vf</text>
  <text x="290" y="197" fill="#a16207" font-size="9" text-anchor="middle">s.t. 预测模型 + 约束</text>
  <text x="290" y="215" fill="#a16207" font-size="9" text-anchor="middle">预测时域: Np</text>

  <rect x="400" y="140" width="140" height="90" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="470" y="165" fill="#14532d" font-size="13" font-weight="bold" text-anchor="middle">预测模型</text>
  <text x="470" y="183" fill="#3a7a5a" font-size="9" text-anchor="middle">x(k+1) = f(x(k),u(k))</text>
  <text x="470" y="197" fill="#3a7a5a" font-size="9" text-anchor="middle">离散化: ZOH/Tustin</text>
  <text x="470" y="215" fill="#3a7a5a" font-size="9" text-anchor="middle">步长: Ts = 10-100μs</text>

  <rect x="600" y="140" width="120" height="90" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="660" y="165" fill="#3b0764" font-size="13" font-weight="bold" text-anchor="middle">被控对象</text>
  <text x="660" y="183" fill="#6b21a8" font-size="9" text-anchor="middle">LCL滤波器/VSC/电机</text>
  <text x="660" y="197" fill="#6b21a8" font-size="9" text-anchor="middle">x(k+1) = Ax(k) + Bu(k)</text>
  <text x="660" y="215" fill="#6b21a8" font-size="9" text-anchor="middle">y(k) = Cx(k)</text>

  <line x1="120" y1="185" x2="143" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="175" y1="185" x2="218" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="360" y1="185" x2="398" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="185" x2="598" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <line x1="660" y1="230" x2="660" y2="300" stroke="#333" stroke-width="1.5"/>
  <line x1="660" y1="300" x2="160" y2="300" stroke="#333" stroke-width="1.5"/>
  <line x1="160" y1="300" x2="160" y2="202" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="380" y="295" fill="#555" font-size="9" text-anchor="middle">反馈 y(k)</text>

  <rect x="220" y="330" width="500" height="40" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="470" y="355" fill="#7f1d1d" font-size="11" font-weight="bold" text-anchor="middle">滚动时域特性：每步重新优化</text>

  <text x="30" y="390" fill="#333" font-size="11" font-weight="bold">图例</text>
  <rect x="30" y="398" width="14" height="10" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="50" y="407" fill="#555" font-size="9">参考信号</text>
  <rect x="120" y="398" width="14" height="10" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="140" y="407" fill="#555" font-size="9">MPC优化器</text>
  <rect x="230" y="398" width="14" height="10" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="250" y="407" fill="#555" font-size="9">预测模型</text>
  <rect x="340" y="398" width="14" height="10" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="360" y="407" fill="#555" font-size="9">被控对象</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 模型预测控制（MPC）通用框架</p>


### 通用MPC框架

**预测模型**（离散时间状态空间）：

$$x(k+1) = f(x(k), u(k), d(k))$$

$$y(k) = h(x(k), u(k), d(k))$$

其中 $x$ 为状态向量，$u$ 为控制输入，$d$ 为扰动，$y$ 为输出。

**滚动优化问题**：

$$\min_{u(k), \dots, u(k+N_p-1)} J = \sum_{i=0}^{N_p-1} \ell(x(k+i|k), u(k+i|k)) + V_f(x(k+N_p|k))$$

$$\text{s.t. } x(k+i+1|k) = f(x(k+i|k), u(k+i|k), \hat{d}(k+i|k))$$

$$x_{min} \leq x(k+i|k) \leq x_{max}$$

$$u_{min} \leq u(k+i|k) \leq u_{max}$$

$$y_{min} \leq y(k+i|k) \leq y_{max}$$

其中 $N_p$ 为预测时域，$N_c$ 为控制时域（$N_c \leq N_p$），$\ell(\cdot)$ 为运行代价，$V_f(\cdot)$ 为终端代价。

**反馈控制律**：

$$u_{MPC}(k) = u^*(k|k)$$

在下一个时刻 $k+1$，基于新的状态测量 $x(k+1)$ 重新求解优化问题（滚动时域特性）。

### EMT中的离散化

EMT仿真中，MPC的预测模型需要与EMT求解器同步。常用的离散化方法包括：

**零阶保持（ZOH）**：

$$x(k+1) = e^{AT_s} x(k) + \int_0^{T_s} e^{A\tau} B d\tau \cdot u(k) = A_d x(k) + B_d u(k)$$

**一阶泰勒近似**：

$$A_d \approx I + AT_s, \quad B_d \approx BT_s$$

**Tustin变换**（双线性变换）：

$$A_d = (I - \frac{T_s}{2}A)^{-1}(I + \frac{T_s}{2}A)$$

$$B_d = (I - \frac{T_s}{2}A)^{-1}BT_s$$

## 关键技术挑战

### 计算实时性

EMT仿真步长通常为10-100 μs，而MPC优化问题求解需要更多时间。解决策略包括：
1. **显式MPC**：离线求解多参数二次规划（mp-QP），将控制律表示为分段仿射函数
2. **近似优化**：使用迭代QP的早期停止或近似梯度
3. **并行计算**：GPU加速枚举（FCS-MPC）或并行QP求解器

### 扰动观测与补偿

MPC性能高度依赖于预测模型的准确性。实际系统中存在参数漂移、未建模动态和外部扰动。常用方法：
1. **扰动观测器（DOB）**：估计总扰动并补偿
2. **扩展状态观测器（ESO）**：将扰动作为扩展状态估计
3. **鲁棒MPC**：考虑最坏情况扰动，采用min-max优化

### 多时间尺度匹配

MPC控制周期（通常1-10 kHz）与EMT仿真步长（通常10-100 μs）之间存在多时间尺度问题。解决策略：
1. **多速率仿真**：MPC在控制周期更新，EMT在更细步长内保持控制量不变
2. **内插法**：在控制周期内对控制量进行线性或高阶插值
3. **等效电路法**：将MPC控制律表示为EMT兼容的代数/微分方程

## 量化性能边界

MPC在EMT仿真中的性能优势主要体现在以下方面（来自文献）：

- **电流跟踪精度**：FCS-MPC相比传统PI控制在瞬态响应中可将电流误差降低30-50%（基于LCL滤波器的VSC仿真，Ts=50 μs）
- **约束处理能力**：MPC可显式处理电流限幅约束，在故障穿越过程中避免过流保护触发，而PI控制需要额外的抗饱和设计
- **计算时间**：GPU加速的FCS-MPC（64种开关状态）可在5 μs内完成优化，满足10 kHz控制周期的实时性要求
- **多目标权衡**：通过权重系数调节，MPC可在电流跟踪精度和开关频率之间实现灵活权衡，PI控制需要重新设计解耦环节

**数据缺口声明**：MPC在EMT仿真中的量化性能数据高度依赖于具体的应用场景（VSC、MMC、DC-DC等）、预测模型精度和求解器选择。上述数据来自典型文献报道，实际性能可能因具体实现而异。

## 适用边界与选择指南

| 应用场景 | 推荐MPC类型 | 理由 |
|----------|------------|------|
| 低功率VSC（<1 MW） | FCS-MPC | 开关状态少（8种），计算量小 |
| 中功率VSC（1-10 MW） | FCS-MPC + GPU加速 | 开关状态增多（64种），需并行计算 |
| 高功率VSC-HVDC（>100 MW） | CCS-MPC | 计算量小，适合高开关频率 |
| MMC调制 | FCS-MPC（子模块级） | 直接选择子模块状态，无需载波调制 |
| DC-DC变换器 | FCS-MPC | 开关状态少（4-8种），约束处理重要 |
| 多端直流电网 | CCS-MPC + 鲁棒MPC | 多变量耦合，需处理不确定性 |

**不推荐MPC的场景**：
- 大规模电力系统稳定性分析（计算量过大，PI/线性控制足够）
- 电磁暂态与机电暂态混合仿真中的机电侧（时间尺度不匹配）
- 实时数字仿真（RTDS）中计算资源受限的节点

## 相关模型

- [[pi-controller-model]] - PI控制器基础（MPC的对比基准）
- [[vector-control-model]] - 矢量控制模型（MPC的常见应用场景）
- [[pll-model]] - 锁相环模型（MPC的同步参考）
- [[droop-control-model]] - 下垂控制模型（MPC的分布式控制场景）
- [[pwm-modulator-model]] - PWM调制模型（CCS-MPC的输出环节）
- [[vsc-model]] - VSC换流器模型（MPC的典型被控对象）
- [[mmc-model]] - MMC模型（MPC的子模块选择）

## 来源论文

- **Cortigiano等 - 2020** - FCS-MPC在VSC-HVDC中的应用，比较了FCS-MPC与传统PI控制在电流跟踪和约束处理方面的性能
- **Kouro等 - 2009** - 有限集MPC在电力电子中的开创性综述，奠定了FCS-MPC的理论基础
- **Darvish等 - 2018** - CCS-MPC在高功率VSC中的应用，展示了QP求解器在EMT仿真中的实时性
