---
title: "数值积分"
type: method
tags: [numerical-integration, emt, trapezoidal, dirk, implicit-integration, stability]
created: "2026-04-13"
---

# 数值积分

## 概述

数值积分（Numerical Integration）是EMT仿真中将连续时间微分代数方程（DAE）离散为逐时步代数方程的核心方法。电感、电容、线路、变流器控制和等效网络都需要通过积分公式生成伴随电路、状态更新式或节点注入历史项。

在EMTP类求解器中，数值积分与[[nodal-analysis|节点分析法]]、[[state-space-method|状态空间法]]、开关事件处理以及设备等效模型共同决定仿真精度、数值阻尼和计算成本。不同积分方法（梯形法、后向欧拉法、DIRK、紧凑格式等）面向不同的稳定性与效率需求。

## 核心原理

### 动态元件离散化

典型EMT离散化将动态元件写成等效导纳加历史源形式：

$$
i(t_k) = G_{\mathrm{eq}} v(t_k) + I_{\mathrm{hist}}(t_{k-1})
$$

其中 $G_{\mathrm{eq}}$ 由积分公式、元件参数和步长决定，历史源汇总上一时刻的电压、电流或状态变量。

### 常用积分方法对比

| 方法 | 公式 | 精度阶数 | 稳定性 | 阻尼特性 |
|------|------|---------|--------|---------|
| **前向欧拉 (FE)** | $x_{n+1} = x_n + h f(t_n, x_n)$ | 1阶 | 条件稳定 | 无 |
| **后向欧拉 (BE)** | $x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})$ | 1阶 | A稳定 | 强阻尼 |
| **梯形法 (TR)** | $x_{n+1} = x_n + \frac{h}{2}[f_n + f_{n+1}]$ | 2阶 | A稳定 | 无（可能振荡） |
| **2S-DIRK** | 见下文 | 2-3阶 | L稳定可调 | 可控 |
| **3S-DIRK** | 见下文 | 3-4阶 | L稳定 | 强阻尼 |
| **Gear法** | 多步法 | 2-6阶 | 刚性稳定 | 可调 |

### A稳定性与L稳定性

**A稳定（A-Stable）**：数值方法对所有 $\text{Re}(\lambda) < 0$ 的测试方程 $\dot{x} = \lambda x$ 都稳定。

**L稳定（L-Stable）**：除A稳定外，还满足 $\lim_{\text{Re}(\lambda) \to -\infty} |R(\lambda h)| = 0$，即对无穷大负实部特征值完全阻尼。

**关键区别**：
- 梯形法是A稳定但非L稳定（$R(\infty) = -1$）
- 后向欧拉是L稳定（$R(\infty) = 0$）
- L稳定方法能完全抑制高频数值振荡

### 梯形法的数值振荡问题

梯形法在开关动作或故障后可能产生高频数值振荡：

$$
x_{n+1} = x_n + \frac{h}{2}(\lambda x_n + \lambda x_{n+1})
$$

特征根：

$$
z = \frac{1 + \lambda h/2}{1 - \lambda h/2}
$$

当 $\lambda h \to -\infty$，$z \to -1$，导致符号交替振荡。

**临界阻尼调整（CDA）**：在事件点后使用半步长后向欧拉抑制振荡。

## 主要积分方法详解

### 梯形法（Trapezoidal Rule, TR）

**公式**：

$$
x_{n+1} = x_n + \frac{h}{2}[f(t_n, x_n) + f(t_{n+1}, x_{n+1})]
$$

**局部截断误差**：$O(h^3)$

**在EMT中的应用**：
- 电感：$i_L(t) = \frac{\Delta t}{2L} v_L(t) + [i_L(t-\Delta t) + \frac{\Delta t}{2L} v_L(t-\Delta t)]$
- 电容：$i_C(t) = \frac{2C}{\Delta t} v_C(t) - [\frac{2C}{\Delta t} v_C(t-\Delta t) + i_C(t-\Delta t)]$

**频率畸变**：

梯形法引入的频率畸变：

$$
\omega_{actual} = \frac{2}{\Delta t} \tan\left(\frac{\omega_{sim} \Delta t}{2}\right)
$$

当 $\omega_{sim} \to \omega_{NY} = \pi/\Delta t$（奈奎斯特频率），$\omega_{actual} \to \infty$。

### 后向欧拉法（Backward Euler, BE）

**公式**：

$$
x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})
$$

**特点**：
- L稳定，无数值振荡
- 1阶精度，误差较大
- 等效电导：$G_{eq} = \frac{\Delta t}{L}$（电感），$G_{eq} = \frac{C}{\Delta t}$（电容）

### 2S-DIRK（2-Stage Diagonally Implicit Runge-Kutta）

**一般形式**：

$$
\begin{aligned}
k_1 &= f(t_n + c_1 h, x_n + h a_{11} k_1) \\
k_2 &= f(t_n + c_2 h, x_n + h a_{21} k_1 + h a_{22} k_2) \\
x_{n+1} &= x_n + h(b_1 k_1 + b_2 k_2)
\end{aligned}
$$

**单参数族**（通过参数 $\lambda$ 控制特性）：

| 参数值 | 特性 | 应用场景 |
|--------|------|---------|
| $\lambda = 1-\sqrt{2}/2 \approx 0.293$ | L稳定，强阻尼 | 抑制数值振荡 |
| $\lambda = (3-\sqrt{3})/6 \approx 0.211$ | 3阶精度 | 高精度需求 |
| $\lambda = 1/4$ | 2阶精度，平衡 | 通用仿真 |
| $\lambda = (2\pm\sqrt{2})/4$ | 可调阻尼 | 灵活控制 |

**等效导纳**：$G_{eq} = \lambda \cdot \frac{\Delta t}{L}$（恒定，便于矩阵复用）

### 3S-DIRK（3-Stage DIRK）

**变阶变步长3S-DIRK**：

$$
\begin{aligned}
k_1 &= f(t_n, x_n) \\
k_2 &= f(t_n + c_2 h, x_n + h a_{21} k_1 + h a_{22} k_2) \\
k_3 &= f(t_n + c_3 h, x_n + h(a_{31} k_1 + a_{32} k_2 + a_{33} k_3)) \\
x_{n+1} &= x_n + h(b_1 k_1 + b_2 k_2 + b_3 k_3)
\end{aligned}
$$

**特点**：
- 3阶精度，L稳定
- 支持变阶（2阶/3阶切换）
- 支持变步长，通过局部截断误差估计调整步长

**局部截断误差估计**：

$$
\text{LTE} = \frac{\|x_{n+1}^{(3)} - x_{n+1}^{(2)}\|}{2^p - 1}
$$

### Gear法（向后微分公式, BDF）

**k阶BDF公式**：

$$
\sum_{j=0}^{k} \alpha_j x_{n+j} = h \beta_k f(t_{n+k}, x_{n+k})
$$

**常用阶数**：
- BDF2（2阶）：$\alpha_0 = 1/3, \alpha_1 = -4/3, \alpha_2 = 1, \beta_2 = 2/3$
- 阶数越高精度越高，但稳定性降低

**在EMT中的应用**：
- 用于刚性系统（时间常数差异大）
- 多步法需启动过程（从低阶开始）

## 适用边界

### 适用场景
- 需要逐时步保持电感、电容、频变网络和电力电子开关动态时
- 常规EMT网络（梯形法）
- 含频繁开关、故障切换（L稳定方法）
- 刚性系统（Gear法或DIRK）

### 不适用场景
- 目标频带明确的窄带模型（应采用频率匹配积分）
- 超高速暂态（需极小步长，考虑状态空间或解析解）
- 强非线性系统（需配合迭代或分段线性化）

### 注意事项
- 梯形法在不连续事件后可能保留数值振荡，需配合CDA或L稳定方法
- 大步长提高效率，但应由模型目标、控制带宽、开关频率约束
- 变步长算法需评估计算开销是否值得

## 技术演进脉络

### 1960-1970年代 (经典方法)
- **梯形法确立**
  - EMTP采用梯形法作为标准积分方法
  - 后向欧拉用于初始化
  - 数值振荡问题被发现

### 1980-1990年代 (振荡抑制)
- **临界阻尼调整（CDA）**
  - 在开关时刻插入半步长后向欧拉
  - 抑制梯形法数值振荡
  - 保持整体2阶精度

- **Gear法引入**
  - 用于刚性系统
  - 多步法提高精度
  - 稳定性分析完善

### 2000年代 (DIRK方法)
- **2S-DIRK引入EMT**
  - 可调参数控制阻尼特性
  - L稳定选项抑制振荡
  - 恒定等效导纳便于矩阵复用

### 2010年代 (变阶变步长)
- **3S-DIRK变阶变步长**
  - 自动调整阶数和步长
  - 误差控制自适应
  - 提高计算效率

- **紧凑格式**
  - 兼顾稳定性与突变处理
  - 单步多阶段计算

### 2020年代 (混合与优化)
- **混合积分策略**
  - 按元件类型选择积分方法
  - 正常工况用梯形法
  - 事件点用L稳定方法

- **大步长优化**
  - 3S-DIRK支持大步长
  - 保持精度和稳定性
  - 适用于实时仿真

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally]] | 2008 | 将2S-DIRK用于EMT离散化，讨论精度与振荡抑制 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simulation of dynamic phasors]] | 2009 | 面向动态相量模型的频率匹配积分 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact scheme for electromagnetic transients]] | 2023 | 用紧凑格式兼顾稳定性与突变处理 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration]] | 2023 | 在MMC等效中结合混合积分、解耦和恒导纳思想 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK based EMT simulations]] | 2024 | 讨论2S-DIRK在EMT应用中的补充处理 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step-size electromagnetic transients]] | 2024 | 面向较大步长EMT的隐式积分 |

## 相关方法
- [[discretization-methods|离散化方法]] - 积分方法的电路实现
- [[stiff-system-handling|刚性系统处理]] - 刚性问题的积分策略
- [[nodal-analysis|节点分析法]] - 积分后的网络求解
- [[state-space-method|状态空间法]] - 状态空间积分实现
- [[fixed-admittance|恒导纳模型]] - 固定导纳积分形式
- [[multirate-method|多速率方法]] - 不同步长的积分协调
- [[model-order-reduction|模型降阶方法]] - 降阶后的高效积分

## 相关模型

- [[synchronous-machine-model|同步电机模型]] - 电机暂态数值积分
- [[mmc-model|MMC模型]] - 模块化换流器多速率积分
- [[vsc-model|VSC模型]] - 变流器开关积分策略
- [[transmission-line-model|输电线路模型]] - 线路Bergeron模型积分
- [[transformer-model|变压器模型]] - 变压器暂态积分方法

## 相关主题
- [[dynamic-phasor|动态相量]] - 相量域的积分方法
- [[real-time-simulation|实时仿真]] - 实时约束下的积分选择
- [[parallel-computing|并行计算]] - 并行积分算法

## 来源论文

| 论文 | 年份 |
|------|------|
| [[耦合长线电磁暂态分析的扩展bergeron模型|耦合长线电磁暂态分析的扩展Bergeron模型]] | 1996 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[zfunction-convolution-in-ehv|Z.function convolution in EHV]] | 2002 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power|Using TACS Functions Within EMPT To Teach Protective Relayin]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[第29-卷-第34-期-中-国-电-机-工-程-学-报-vol29-no34-dec-5-2009|考虑任意重事件发生的多步变步长电磁暂态仿真算法]] | 2009 |
| [[第29-卷-第34-期-中-国-电-机-工-程-学-报-vol29-no34-dec-5-2009|考虑任意重事件发生的多步变步长电磁暂态仿真算法]] | 2009 |
| [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14|Saturation in Transient and Stability Phenomena for Cylindri]] | 2012 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[synchronous-machine-exciter-circuit-model-in-a|Synchronous Machine Exciter Circuit Model In A]] | 2013 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 |
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 |
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror|Saturable reactor hysteresis model based on Jiles–Atherton f]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[面向指数积分方法的电磁暂态仿真gpu并行算法|面向指数积分方法的电磁暂态仿真GPU并行算法]] | 2018 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Spurious Power Losses in Modular Multilevel Converter Arm Eq]] | 2019 |
| [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Stability of Algorithms for Electro-Magnetic-Transient Simul]] | 2019 |
| [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Stability of Algorithms for Electro-Magnetic-Transient Simul]] | 2019 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2019 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da|Stability Evaluation of Interpolation, Extrapolation, and Nu]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[time-domain-modeling-of-transmission-line-crossing-using-electromagnetic-scatter|Time-Domain Modeling of Transmission Line Crossing Using Ele]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size el]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报-36|中  国  电  机  工  程  学  报]] | 2022 |
| [[基于umec的双芯sen变压器电磁暂态模型|基于UMEC的双芯Sen变压器电磁暂态模型]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[模块化多电平换流器的高效电磁暂态仿真方法研究|模块化多电平换流器的高效电磁暂态仿真方法研究]] | 2022 |
| [[混合型mmc全状态高效电磁暂态仿真方法研究|混合型MMC全状态高效电磁暂态仿真方法研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法|直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad|Real-Time Simulation of Power System Electromagnetic Transie]] | 2023 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact sc]] | 2023 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact sc]] | 2023 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[the-impact-of-frame-transformations-on-power-system-emt-simulation|The Impact of Frame Transformations on Power System EMT Simu]] | 2023 |
| [[the-impact-of-frame-transformations-on-power-system-emt-simulation|The Impact of Frame Transformations on Power System EMT Simu]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[基于一致性算法的多虚拟同步机功率振荡协调抑制|基于一致性算法的多虚拟同步机功率振荡协调抑制]] | 2023 |
| [[多类型子模块mmc电磁暂态通用建模和实现方法|多类型子模块MMC电磁暂态通用建模和实现方法]] | 2023 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[电力系统风力发电建模与仿真研究综述|电力系统风力发电建模与仿真研究综述]] | 2024 |
| [[reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in|Reduced-order and simultaneous solution of power and control]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[simulation-of-electromagnetic-transients-with-a-family-of-implicit-multi-step-os|Simulation of electromagnetic transients with a family of im]] | 2025 |
| [[simulation-of-electromagnetic-transients-with-a-family-of-implicit-multi-step-os|Simulation of electromagnetic transients with a family of im]] | 2025 |
| [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Splitting State-Space Method for Converter-Integrated Power ]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[type-3-wind-turbine-generator-model-with-generic-high-level-control-for-electrom|Type-3 wind turbine generator model with generic high-level ]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit|Z-Tool: Frequency-domain characterization of EMT models for ]] | 2025 |
| [[中-国-电-机-工-程-学-报-37|中  国  电  机  工  程  学  报]] | 2025 |
| [[基于fpga的变电站实时仿真培训系统|基于FPGA的变电站实时仿真培训系统]] | 2025 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |
| [[基于矩阵对角化的电磁暂态时间并行计算方法|基于矩阵对角化的电磁暂态时间并行计算方法]] | 2026 |
| [[基于矩阵对角化的电磁暂态时间并行计算方法|基于矩阵对角化的电磁暂态时间并行计算方法]] | 2026 |
## 深度增强内容

### 1. 核心原理详解

#### 1.1 稳定性分析框架

**线性测试方程**：

$$
\dot{x} = \lambda x, \quad \text{Re}(\lambda) < 0
$$

应用于数值方法得：

$$
x_{n+1} = R(z) x_n, \quad z = \lambda h
$$

其中 $R(z)$ 为**稳定性函数**。

**各方法的稳定性函数**：

| 方法 | $R(z)$ | $R(\infty)$ |
|------|--------|-------------|
| 前向欧拉 | $1 + z$ | $\infty$（不稳定） |
| 后向欧拉 | $\frac{1}{1-z}$ | 0（L稳定） |
| 梯形法 | $\frac{1+z/2}{1-z/2}$ | -1（A稳定） |
| 2S-DIRK | $\frac{1+(1-2\lambda)z}{(1-\lambda z)^2}$ | $0$（$\lambda=1-\sqrt{2}/2$） |

**稳定区域**：
- A稳定：稳定区域包含整个左半平面
- L稳定：A稳定 + $R(\infty) = 0$

#### 1.2 局部截断误差分析

局部截断误差（LTE）表示单步误差：

$$
\text{LTE} = x(t_{n+1}) - x_{n+1} = C_p h^{p+1} x^{(p+1)}(t_n) + O(h^{p+2})
$$

其中 $p$ 为方法阶数，$C_p$ 为误差常数。

| 方法 | 阶数 $p$ | 误差常数 $C_p$ |
|------|---------|---------------|
| 后向欧拉 | 1 | $-1/2$ |
| 梯形法 | 2 | $-1/12$ |
| 2S-DIRK（$\lambda=1/4$） | 2 | 可调 |
| 3S-DIRK | 3 | 可调 |

#### 1.3 频率响应畸变

数值积分在频域引入的畸变可通过 $s$ 平面映射分析。

**梯形法的双线性变换**：

$$
s = \frac{2}{h} \frac{z-1}{z+1}
$$

对应连续频率 $\omega$ 与离散频率 $\omega_d$ 关系：

$$
\omega = \frac{2}{h} \tan\left(\frac{\omega_d h}{2}\right)
$$

**畸变特性**：
- 低频（$\omega h \ll 1$）：畸变小，$\omega \approx \omega_d$
- 高频（$\omega h \to \pi$）：畸变大，$\omega \to \infty$
- 奈奎斯特频率（$\omega_d = \pi/h$）：$\omega \to \infty$

### 2. 算法流程

#### 阶段一：网络预处理
1. **元件分类**：
   - 线性动态元件（L、C）
   - 非线性元件（饱和电感）
   - 开关器件

2. **积分方法分配**：
   - 常规网络：梯形法
   - 含电力电子：L稳定方法（2S-DIRK/BE）
   - 刚性系统：Gear法

3. **等效导纳计算**：
   - 电感：$G_{eq,L} = \frac{\Delta t}{\alpha L}$
   - 电容：$G_{eq,C} = \frac{C}{\alpha \Delta t}$
   - 其中 $\alpha$ 取决于积分方法

#### 阶段二：时域推进
1. **预测**（多步法）：用历史值预测新值
2. **校正**（隐式法）：求解非线性方程
3. **收敛判断**：检查迭代残差
4. **历史源更新**：为下一步计算历史项

#### 阶段三：事件处理
1. **开关动作检测**：
   - 自然换相（过零点）
   - 强制换相（触发信号）

2. **振荡抑制策略**：
   - CDA：插入半步长BE
   - 方法切换：TR $\to$ L稳定方法
   - 插值修正：精确计算开关时刻

3. **重启动**：
   - 多步法需重新初始化
   - 变步长方法调整步长

### 3. 参数选取指南

#### 3.1 时间步长选择

| 应用场景 | 推荐步长 | 选择依据 | 注意事项 |
|---------|---------|---------|---------|
| **常规输电网络** | 50-100 μs | 工频周期(20ms)的1/200-1/400 | 确保奈奎斯特频率>2kHz |
| **MMC详细建模** | 10-20 μs | 子模块电容电压波动 | 避免虚假损耗 |
| **两电平VSC** | 1-10 μs | IGBT开关暂态 | 捕捉开关细节 |
| **实时仿真** | 20-50 μs | 实时约束 | 配合恒导纳模型 |
| **大步长仿真** | 200-500 μs | 3S-DIRK | 需验证精度 |

#### 3.2 积分方法选择

| 场景 | 推荐方法 | 参数设置 | 理由 |
|------|---------|---------|------|
| **稳态运行** | 梯形法 | 固定步长 | 2阶精度，无耗散 |
| **故障/开关** | 2S-DIRK | $\lambda = 1-\sqrt{2}/2$ | L稳定，抑制振荡 |
| **初始化** | 后向欧拉 | 大步长 | L稳定，快速收敛 |
| **变步长** | 3S-DIRK | 变阶变步长 | 自适应效率 |
| **刚性系统** | Gear法 | 2-3阶 | 刚性稳定 |

#### 3.3 混合积分策略

**元件级混合**：
- 输电线：梯形法（线性）
- 发电机：梯形法（详细模型）
- 换流器：2S-DIRK（开关频繁）

**时间级混合**：
- 正常工况：梯形法
- 事件前1-2步：切换L稳定方法
- 事件后恢复期：切回梯形法

### 4. 性能分析

#### 4.1 计算复杂度

| 方法 | 每步计算量 | 矩阵分解 | 适用规模 |
|------|-----------|---------|---------|
| 梯形法 | $O(n)$ | 每步（变导纳）或一次（恒导纳） | 大规模 |
| 后向欧拉 | $O(n)$ | 同上 | 大规模 |
| 2S-DIRK | $2 \times O(n)$ | 两次求解 | 中等规模 |
| 3S-DIRK | $3 \times O(n)$ | 三次求解 | 中小规模 |
| Gear法 | $O(n)$ | 多步历史存储 | 大规模 |

#### 4.2 精度与效率权衡

| 方法 | 精度 | 效率 | 稳定性 | 综合推荐 |
|------|------|------|--------|---------|
| 梯形法 | ★★★ | ★★★★★ | ★★★ | 通用首选 |
| 2S-DIRK | ★★★ | ★★★★ | ★★★★★ | 电力电子 |
| 3S-DIRK | ★★★★ | ★★★ | ★★★★★ | 高精度 |
| Gear法 | ★★★★ | ★★★★ | ★★★★ | 刚性系统 |

#### 4.3 数值振荡对比

| 工况 | 梯形法 | 2S-DIRK(L) | 3S-DIRK(L) | BE |
|------|--------|-----------|-----------|-----|
| 开关后 | 有振荡 | 无振荡 | 无振荡 | 无振荡 |
| 故障后 | 有振荡 | 无振荡 | 无振荡 | 无振荡 |
| 稳态 | 精确 | 良好 | 精确 | 有阻尼 |

### 5. 最佳实践与注意事项

#### 5.1 数值振荡抑制

**识别数值振荡**：
- 波形出现高频振荡（频率接近奈奎斯特频率）
- 振荡幅值不随时间衰减
- 改变步长后振荡频率改变

**抑制方法**：
1. **CDA（Critical Damping Adjustment）**：
   - 在事件点插入半步长后向欧拉
   - 随后恢复梯形法
   - 整体保持2阶精度

2. **方法切换**：
   - 检测到事件前切换L稳定方法
   - 事件后稳定再切回梯形法

3. **插值技术**：
   - 精确计算开关时刻
   - 线性插值或高阶插值

#### 5.2 步长控制

**固定步长**：
- 简单，适合实时仿真
- 需按最严重要求选择步长

**变步长**：
- 通过LTE估计调整步长
- 公式：$h_{new} = h_{old} \left(\frac{\tau}{\text{LTE}}\right)^{1/(p+1)}$
- 需设置最大/最小步长限制

**步长限制因素**：
- 开关频率
- 控制带宽
- 线路传播时间
- 稳定性约束

#### 5.3 初始化

**稳态初始化**：
- 使用潮流计算结果
- 相量域到瞬时值转换
- 谐波稳态计算

**非初始化方法**：
- 从全零初始开始
- 后向欧拉大步长过渡
- 逐步减小步长至正常值

#### 5.4 误差控制

**局部误差估计**：
- 使用同阶或高阶公式对比
- 嵌入式Runge-Kutta方法
- 3S-DIRK的变阶策略

**全局误差控制**：
- 误差积累监测
- 关键变量检查
- 能量守恒验证

### 6. 与其他方法的协同

#### 6.1 与节点分析法结合

数值积分生成伴随电路后，与节点分析结合：

$$
Y_{eq} v = i_{inj} - i_{hist}
$$

- $Y_{eq}$：等效导纳矩阵（依赖于积分方法）
- $i_{hist}$：历史电流源（依赖于积分方法和前一步状态）

#### 6.2 与状态空间法结合

状态空间离散化：

$$
x_{n+1} = \Phi x_n + \Gamma u_n
$$

其中 $\Phi$、$\Gamma$ 由积分方法决定：
- 梯形法：$\Phi = (I - \frac{h}{2}A)^{-1}(I + \frac{h}{2}A)$
- 后向欧拉：$\Phi = (I - hA)^{-1}$

#### 6.3 与多速率方法结合

不同子系统可采用不同积分方法：
- 快子系统（电力电子）：小步长 + L稳定方法
- 慢子系统（输电网）：大步长 + 梯形法
- 接口处理：插值/外推 + 稳定性保证

---

**注**：以上内容整合了2004-2025年间数值积分在EMT仿真中的最新研究成果，涵盖2S-DIRK、3S-DIRK、紧凑格式、混合积分等前沿进展。
