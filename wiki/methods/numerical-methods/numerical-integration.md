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

## 来源论文

| 论文 | 年份 |
|------|------|
| [[耦合长线电磁暂态分析的扩展bergeron模型|耦合长线电磁暂态分析的扩展Bergeron模型]] | 1996 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix|Analysis and estimation of truncation errors in modeling com]] | 2002 |
| [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix|Analysis and estimation of truncation errors in modeling com]] | 2002 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[zfunction-convolution-in-ehv|Z.function convolution in EHV]] | 2002 |
| [[37s0142-061528962900045-2|37/s0142-0615%2896%2900045-2]] | 2003 |
| [[37s0142-061528962900045-2|37/s0142-0615%2896%2900045-2]] | 2003 |
| [[creating-an-electromagnetic-transients-program-in-matlab-matemtp-power-delivery-|Creating An Electromagnetic Transients Program In Matlab: Ma]] | 2004 |
| [[creating-an-electromagnetic-transients-program-in-matlab-matemtp-power-delivery-|Creating An Electromagnetic Transients Program In Matlab: Ma]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[improved-control-systems-simulation-in-the-emtp-through-compensation|Improved control systems simulation in the EMTP through comp]] | 2004 |
| [[improved-control-systems-simulation-in-the-emtp-through-compensation|Improved control systems simulation in the EMTP through comp]] | 2004 |
| [[modelling-of-circuit-breakers-in-the-electromagnetic-transients-program-power-sy|Modelling of circuit breakers in the Electromagnetic Transie]] | 2004 |
| [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow|Multiprocessor based generator module for a real-time power ]] | 2004 |
| [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow|Multiprocessor based generator module for a real-time power ]] | 2004 |
| [[power-converter-simulation-module-connected-to-the-emtp-power-systems-ieee-trans|Power converter simulation module connected to the EMTP - Po]] | 2004 |
| [[power-converter-simulation-module-connected-to-the-emtp-power-systems-ieee-trans|Power converter simulation module connected to the EMTP - Po]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power|Using TACS Functions Within EMPT To Teach Protective Relayin]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[on-a-new-approach-for-the-simulation-of-transients|On a new approach for the simulation of transients]] | 2007 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[earth-return-impedances-of-conductor-arrangements-13&14|Earth Return Impedances of Conductor Arrangements]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[第29-卷-第34-期-中-国-电-机-工-程-学-报-vol29-no34-dec-5-2009|考虑任意重事件发生的多步变步长电磁暂态仿真算法]] | 2009 |
| [[第29-卷-第34-期-中-国-电-机-工-程-学-报-vol29-no34-dec-5-2009|考虑任意重事件发生的多步变步长电磁暂态仿真算法]] | 2009 |
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas|Chen 等 | A hybrid parallel computation algorithm and its app]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Modeling of ac machines using a voltage-behind-reactance for]] | 2010 |
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Modeling of ac machines using a voltage-behind-reactance for]] | 2010 |
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|A combined state-space nodal method for the simulation of po]] | 2011 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati|Photovoltaic generator modelling to improve numerical robust]] | 2012 |
| [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14|Saturation in Transient and Stability Phenomena for Cylindri]] | 2012 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Comparison between electromechanical transient model and ele]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[multi-fpga-digital-hardware-design-iet-gtd|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[synchronous-machine-exciter-circuit-model-in-a|Synchronous Machine Exciter Circuit Model In A]] | 2013 |
| [[fast-voltage-balancing-control-and-fast-19、20、21|Fast Voltage-Balancing Control and Fast]] | 2014 |
| [[fast-voltage-balancing-control-and-fast|Fast Voltage-Balancing Control and Fast Numerical Simulation]] | 2014 |
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model|Fitting the frequency-dependent parameters in the Bergeron l]] | 2014 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK-based EMT simulations]] | 2014 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK-based EMT simulations]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[29tpwrd20162590569-2|29/TPWRD.2016.2590569]] | 2016 |
| [[31tpwrd20162529662-2|31/tpwrd.2016.2529662]] | 2016 |
| [[current-source-modular-multilevel-converter-modeling-and-control|Current Source Modular Multilevel Converter Modeling and Con]] | 2016 |
| [[duality-based-transformer-modeling-for-low-frequency-transients|Duality-Based Transformer Modeling for Low-Frequency Transie]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 |
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[real-time-fpga-rtds-co-simulator-for-power-systems|Real-Time FPGA-RTDS Co-Simulator for Power Systems]] | 2018 |
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror|Saturable reactor hysteresis model based on Jiles–Atherton f]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[面向指数积分方法的电磁暂态仿真gpu并行算法|面向指数积分方法的电磁暂态仿真GPU并行算法]] | 2018 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Spurious Power Losses in Modular Multilevel Converter Arm Eq]] | 2019 |
| [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Stability of Algorithms for Electro-Magnetic-Transient Simul]] | 2019 |
| [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Stability of Algorithms for Electro-Magnetic-Transient Simul]] | 2019 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2019 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo|An Inverter Model Simulating Accurate Harmonics with Low Com]] | 2020 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo|An Inverter Model Simulating Accurate Harmonics with Low Com]] | 2020 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo|Interpolation for power electronic circuit simulation revisi]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da|Stability Evaluation of Interpolation, Extrapolation, and Nu]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[time-domain-modeling-of-transmission-line-crossing-using-electromagnetic-scatter|Time-Domain Modeling of Transmission Line Crossing Using Ele]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations]] | 2021 |
| [[accurate-time-domain-simulation-of-power-electronic-circuits|Accurate time-domain simulation of power electronic circuits]] | 2021 |
| [[accurate-time-domain-simulation-of-power-electronic-circuits|Accurate time-domain simulation of power electronic circuits]] | 2021 |
| [[accurate-time-domain-simulation-of-power-electronic-circuits|Accurate time-domain simulation of power electronic circuits]] | 2021 |
| [[accurate-time-domain-simulation-of-power-electronic-circuits|Accurate time-domain simulation of power electronic circuits]] | 2021 |
| [[accurate-time-domain-simulation-of-power-electronic-circuits|Accurate time-domain simulation of power electronic circuits]] | 2021 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[an-efficient-analytical-based-technique-to-numerical-calculation-of-extended-ear|An efficient analytical based technique to numerical calcula]] | 2021 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[compact-matrix-formulation-for-calculating-lightning-induced-voltages-on-electro|Compact Matrix Formulation for Calculating Lightning-Induced]] | 2021 |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient|Comparison and Selection of Grid-Tied Inverter Models for Ac]] | 2021 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[laplace-transform-inversion-through-the-theta-algorithm-for-power-system-emt-ana|Laplace transform inversion through the theta algorithm for ]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size el]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-testing-tool-for-converter-dominated-power-system-stochastic-electromagnetic-t|A Testing Tool for Converter-Dominated Power System: Stochas]] | 2022 |
| [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms|Accuracy Evaluation of Electromagnetic Transients Simulation]] | 2022 |
| [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms|Accuracy Evaluation of Electromagnetic Transients Simulation]] | 2022 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl|Electromechanical transient-electromagnetic transient hybrid]] | 2022 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[full-state-arm-average-value-model-for-simulation-of-active-modular-multilevel-c|Full-state Arm Average Value Model for Simulation of Active ]] | 2022 |
| [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte|Multi-timescale simulator of nonlinear electrical elements b]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报-36|中  国  电  机  工  程  学  报]] | 2022 |
| [[基于umec的双芯sen变压器电磁暂态模型|基于UMEC的双芯Sen变压器电磁暂态模型]] | 2022 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[模块化多电平换流器的高效电磁暂态仿真方法研究|模块化多电平换流器的高效电磁暂态仿真方法研究]] | 2022 |
| [[混合型mmc全状态高效电磁暂态仿真方法研究|混合型MMC全状态高效电磁暂态仿真方法研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法|直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-|An Automatable Approach for Small-Signal Stability Analysis ]] | 2023 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[fast-electromagnetic-transient-simulation-of-modular-multilevel-converter-based-|Fast electromagnetic transient simulation of modular multile]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us|Inaccuracies due to the frequency warping in simulation of e]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us|Inaccuracies due to the frequency warping in simulation of e]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us|Inaccuracies due to the frequency warping in simulation of e]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad|Real-Time Simulation of Power System Electromagnetic Transie]] | 2023 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact sc]] | 2023 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact sc]] | 2023 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[the-impact-of-frame-transformations-on-power-system-emt-simulation|The Impact of Frame Transformations on Power System EMT Simu]] | 2023 |
| [[the-impact-of-frame-transformations-on-power-system-emt-simulation|The Impact of Frame Transformations on Power System EMT Simu]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[基于一致性算法的多虚拟同步机功率振荡协调抑制|基于一致性算法的多虚拟同步机功率振荡协调抑制]] | 2023 |
| [[多类型子模块mmc电磁暂态通用建模和实现方法|多类型子模块MMC电磁暂态通用建模和实现方法]] | 2023 |
| [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga|A waveform-dependence lightning impulse corona model in PSCA]] | 2024 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy--16|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[fixed-admittance-modeling-method-of-pmsg-based-on-compensation-of-impedance-基于虚拟|Fixed-admittance Modeling Method of PMSG Based on Compensati]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[电力系统风力发电建模与仿真研究综述|电力系统风力发电建模与仿真研究综述]] | 2024 |
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul|A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Con]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[adaptive-grained-exponential-integrator-algorithm-for-efficient-simulation-of-po|Adaptive-Grained Exponential Integrator Algorithm for Effici]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[compact-scheme-challenges-in-emt-type-simulations|Compact scheme challenges in EMT-Type simulations]] | 2025 |
| [[compact-scheme-challenges-in-emt-type-simulations|Compact scheme challenges in EMT-Type simulations]] | 2025 |
| [[compact-scheme-challenges-in-emt-type-simulations|Compact scheme challenges in EMT-Type simulations]] | 2025 |
| [[compact-scheme-challenges-in-emt-type-simulations|Compact scheme challenges in EMT-Type simulations]] | 2025 |
| [[discretized-impedance-based-modeling-of-converter-interfaced-energy-resources-fo|Discretized Impedance-Based Modeling of Converter-Interfaced]] | 2025 |
| [[electromagnetic-transient-model-reconstruction-of-generalized-power-transmission|Electromagnetic Transient Model Reconstruction of Generalize]] | 2025 |
| [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w|Enhancements to Terminal Duality-based models for three-phas]] | 2025 |
| [[equivalent-modelling-method-of-single-active-network-for-fast-electromagnetic-tr|Equivalent Modelling Method of Single Active Network for Fas]] | 2025 |
| [[equivalent-modelling-method-of-single-active-network-for-fast-electromagnetic-tr|Equivalent Modelling Method of Single Active Network for Fas]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
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
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
| [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-|Analytical Modeling of the Half-Bridge Leg Using an Associat]] | 2026 |
| [[equivalent-modeling-of-electromagnetic-transient-for-mmc-hvdc-based-on-semi-impl|Equivalent modeling of electromagnetic transient for MMC-HVD]] | 2026 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |
| [[基于矩阵对角化的电磁暂态时间并行计算方法|基于矩阵对角化的电磁暂态时间并行计算方法]] | 2026 |
| [[基于矩阵对角化的电磁暂态时间并行计算方法|基于矩阵对角化的电磁暂态时间并行计算方法]] | 2026 |
