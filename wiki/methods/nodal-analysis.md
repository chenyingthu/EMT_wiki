---
title: "节点分析与伴随电路 (Nodal Analysis / Companion Circuit)"
type: method
tags: [nodal-analysis, companion-circuit, emtp, admittance, conductance]
created: "2026-04-13"
---

# 节点分析与伴随电路 (Nodal Analysis / Companion Circuit)

## 定义与边界

节点分析在 EMT 中通常指把网络元件离散为诺顿型或增广节点型等效后，按节点电压和必要的附加支路变量形成代数方程。它不是单独的积分算法，也不是某一仿真软件的专有实现；积分公式、开关处理、非线性迭代和矩阵求解器会共同决定最终的数值行为。

典型节点方程可写为：

$$
\mathbf{Y}_n \mathbf{v} = \mathbf{i}
$$

其中 $\mathbf{Y}_n$ 为离散时刻的节点导纳矩阵，$\mathbf{v}$ 为节点电压向量，$\mathbf{i}$ 为独立电流源与历史电流源形成的注入向量。含电压源、理想开关、受控源或强约束元件时，常需要采用增广节点形式，而不是只依赖纯导纳矩阵。

## EMT 中的作用

节点分析把元件模型和网络求解分离：元件侧给出等效导纳、历史源和状态更新规则；网络侧组装 [[nodal-admittance-matrix]] 并调用 [[sparse-matrix-solver]] 或局部补偿算法求解节点电压。这样可以让电感、电容、线路、变压器、电力电子等模型在统一接口下接入 EMT 步进过程。

在 EMTP 类算法中，[[companion-circuit]] 是节点分析的关键接口。动态元件经过 [[numerical-integration]] 离散后转化为本时步导纳和历史源；求得节点电压后，再回代更新支路电流、磁链、电荷或控制状态。

```mermaid
graph TD
    subgraph 离散前
        L[动态元件: L/C/R/线路]
        V[独立电压源/电流源]
    end
    subgraph 伴随电路转化
        L -->|数值积分| Norton[诺顿等效]
        Norton --> Geq[等效电导 G_eq]
        Norton --> Ihist[历史电流源 I_hist]
        V -->|受控源处理| MANA[增广矩阵行]
    end
    subgraph 节点方程求解
        Geq --> Yn[装配 Y_n 矩阵]
        Ihist --> In[装配 I_n 向量]
        Yn --> Solve[求解 Y_n·v_n = I_n]
        In --> Solve
        MANA --> Solve
    end
    subgraph 回代
        Solve --> Update[更新支路电压/电流]
        Update --> State[更新状态变量 x_n→x_{n+1}]
        State -->|下一时步| Norton
    end

    style L fill:#e1f5fe
    style V fill:#e1f5fe
    style Norton fill:#fff3e0
    style Solve fill:#c8e6c9
    style State fill:#f3e5f5
```

## 核心机制

线性支路 $(p,q)$ 的导纳 $g$ 对矩阵的贡献为：

$$
Y_{pp} \mathrel{+}= g,\quad
Y_{qq} \mathrel{+}= g,\quad
Y_{pq} \mathrel{-}= g,\quad
Y_{qp} \mathrel{-}= g
$$

电容在梯形积分下的诺顿等效可写为：

$$
i_C(t_k)=\frac{2C}{\Delta t}v_C(t_k)+I_{C,hist}(t_{k-1})
$$

电感可写为：

$$
i_L(t_k)=\frac{\Delta t}{2L}v_L(t_k)+I_{L,hist}(t_{k-1})
$$

这些公式说明伴随电路中的等效导纳依赖步长和积分方法，历史源依赖上一时刻状态。若使用后向欧拉、Gear 或 DIRK 类方法，等效导纳和历史项会改变；因此“节点分析”本身不保证某种精度或阻尼特性。

含附加约束时，可使用改进或增广节点方程：

$$
\begin{bmatrix}
\mathbf{Y}_n & \mathbf{A}\\
\mathbf{B} & \mathbf{C}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}\\
\mathbf{x}
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{j}\\
\mathbf{e}
\end{bmatrix}
$$

其中 $\mathbf{x}$ 可代表电压源电流、开关约束变量或其他模型接口变量。[[state-space-method]] 可与节点方程组合使用，但其边界是设备内部状态方程；节点分析主要承担网络连接和代数约束。

## 分类与变体

| 变体 | 主要对象 | 边界 |
|------|----------|------|
| 纯节点导纳法 | 由电阻、诺顿等效源和导纳支路组成的网络 | 难以直接表示理想电压源和某些强约束元件 |
| 改进/增广节点分析 | 电压源、受控源、互感、开关约束 | 矩阵可能非对称或更病态 |
| 伴随电路节点法 | 含电感、电容、线路的时域 EMT 网络 | 数值特性取决于积分公式和步长 |
| 恒导纳节点法 | 高频开关或实时仿真中的固定矩阵需求 | 常以等效源、延迟或插值换取矩阵复用 |
| 分网节点法 | 大规模或并行 EMT | 边界延迟、接口阻抗和迭代协调会影响稳定性 |

## 适用边界与失败模式

节点分析适合拓扑清晰、网络稀疏、可用等效导纳和注入源描述的 EMT 系统。它在开关频繁动作、理想元件形成奇异回路、非线性元件雅可比变化剧烈、步长与最快暂态不匹配时容易暴露数值问题。

常见失败模式包括：

- 梯形积分在开关或强刚性 LC 网络中出现数值振荡，需要切换阻尼积分、插值或局部损耗建模。
- 断路支路用极小导纳、闭合支路用极大导纳时可能导致 [[nodal-admittance-matrix]] 病态。
- 恒导纳模型若未说明延迟、插值和等效假设，不能外推为“精确”详细开关模型。
- 分网或混合仿真接口若只交换上一时步量，可能引入接口延迟；应与 [[electromechanical-electromagnetic-hybrid-simulation]] 的边界条件一起评估。

## 代表性来源

- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 代表状态空间与节点方程结合的路线，适合作为复杂设备接入节点框架的来源。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] 可用于比较伴随电路离散策略；其中结论应按其算例和积分设置限定。
- [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat]] 涉及嵌套或预计算思路，适合作为矩阵复用和开关状态处理的个案来源。
- [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul]] 支撑固定导纳思想在变换器等值中的应用，但不能替代所有电力电子拓扑的详细验证。

## 与相关页面的关系

- [[nodal-admittance-matrix]] 描述矩阵对象本身；本页描述如何由 EMT 元件和伴随电路形成并使用该矩阵。
- [[sparse-matrix-solver]] 关注线性方程求解和重排序；本页只说明求解器在节点分析流程中的位置。
- [[iterative-solvers]] 处理非线性或大型线性系统的逐步求解；本页中的节点方程可作为迭代过程的内层线性问题。
- [[fixed-admittance]] 是固定矩阵复用的建模策略，不等同于所有节点分析。
- [[companion-model]] 和 [[companion-circuit]] 是动态元件离散到节点方程的接口层。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[耦合长线电磁暂态分析的扩展bergeron模型|耦合长线电磁暂态分析的扩展Bergeron模型]] | 1996 |
| [[电磁暂态计算中新的变压器模型|电磁暂态计算中新的变压器模型]] | 1999 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[37s0142-061528962900045-2|37/s0142-0615%2896%2900045-2]] | 2003 |
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS V]] | 2004 |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP - Power Deli]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[improved-control-systems-simulation-in-the-emtp-through-compensation|Improved control systems simulation in the EMTP through comp]] | 2004 |
| [[modelling-of-circuit-breakers-in-the-electromagnetic-transients-program-power-sy|Modelling of circuit breakers in the Electromagnetic Transie]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee|Multiphase power flow solutions using EMTP and Newtons metho]] | 2004 |
| [[power-converter-simulation-module-connected-to-the-emtp-power-systems-ieee-trans|Power converter simulation module connected to the EMTP - Po]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power|Using TACS Functions Within EMPT To Teach Protective Relayin]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat|Nested fast and simultaneous solution for time-domain simula]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[on-a-new-approach-for-the-simulation-of-transients|On a new approach for the simulation of transients]] | 2007 |
| [[on-a-new-approach-for-the-simulation-of-transients|On a new approach for the simulation of transients]] | 2007 |
| [[re-examination-of-synchronous-machine|Re-examination of Synchronous Machine]] | 2007 |
| [[re-examination-of-synchronous-machine|Re-examination of Synchronous Machine]] | 2007 |
| [[re-examination-of-synchronous-machine|Re-examination of Synchronous Machine]] | 2007 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[a-link-between-emtp-rv-and-flux3d-for-transformer-energization-studies|A link between EMTP-RV and FLUX3D for transformer energizati]] | 2009 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[a-time-domain-harmonic-power-flow-algorithm|A Time-Domain Harmonic Power-Flow Algorithm]] | 2010 |
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Efﬁcient Modeling of Modular Multilevel HVDC]] | 2010 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[a-robust-and-efficient-iterative-scheme-for-the-emt-simulations-of-nonlinear-cir-fix|A Robust and Efficient Iterative Scheme for the EMT Simulati]] | 2011 |
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|A combined state-space nodal method for the simulation of po]] | 2011 |
| [[magnetically-saturable-voltage-behind-reactance-model-for-induction-machines|Magnetically Saturable Voltage Behind Reactance Model for In]] | 2011 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati|Photovoltaic generator modelling to improve numerical robust]] | 2012 |
| [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14|Saturation in Transient and Stability Phenomena for Cylindri]] | 2012 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Comparison between electromechanical transient model and ele]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[synchronous-machine-exciter-circuit-model-in-a|Synchronous Machine Exciter Circuit Model In A]] | 2013 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[parallel-massive-thread-electromagnetic-transient-simulation-on-gpu|Parallel Massive-Thread Electromagnetic Transient Simulation]] | 2014 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[29tpwrd20162518676-2|29/TPWRD.2016.2518676]] | 2016 |
| [[29tpwrd20162590569-2|29/TPWRD.2016.2590569]] | 2016 |
| [[31tpwrd20162529662-2|31/tpwrd.2016.2529662]] | 2016 |
| [[31tpwrd20162529662-2|31/tpwrd.2016.2529662]] | 2016 |
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|An automated FPGA real-time simulator for power electronics ]] | 2016 |
| [[current-source-modular-multilevel-converter-modeling-and-control|Current Source Modular Multilevel Converter Modeling and Con]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路电磁暂态分析的状态方程法]] | 2016 |
| [[30tpwrd20172714639-2|30/TPWRD.2017.2714639]] | 2017 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a|A Novel Interfacing Technique for Distributed Hybrid Simulat]] | 2017 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[general-approach-for-accurate-resonance-analysis-in-transformer-windings|General approach for accurate resonance analysis in transfor]] | 2018 |
| [[real-time-fpga-rtds-co-simulator-for-power-systems|Real-Time FPGA-RTDS Co-Simulator for Power Systems]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror|Saturable reactor hysteresis model based on Jiles–Atherton f]] | 2018 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified High-Speed EMT Equivalent and Implementation Method ]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[双端口子模块mmc电磁暂态通用等效建模方法|双端口子模块MMC电磁暂态通用等效建模方法]] | 2018 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm|An Efficient Phase Domain Synchronous Machine Model With Con]] | 2019 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm|An Efficient Phase Domain Synchronous Machine Model With Con]] | 2019 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm|An Efficient Phase Domain Synchronous Machine Model With Con]] | 2019 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Spurious Power Losses in Modular Multilevel Converter Arm Eq]] | 2019 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-hierarchical-low-rank-approximation-based-network-solver-for-emt-simulation|A Hierarchical Low-Rank Approximation Based Network Solver f]] | 2020 |
| [[a-hierarchical-low-rank-approximation-based-network-solver-for-emt-simulation|A Hierarchical Low-Rank Approximation Based Network Solver f]] | 2020 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-|A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro]] | 2020 |
| [[development-of-a-voltage-dependent-line-model-to-represent-the-corona-effect-in-|Development of a Voltage-Dependent Line Model to Represent t]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[high-performance-computing-engines-for-the-fpga-based-simulation-of-the-ulm|High performance computing engines for the FPGA-based simula]] | 2020 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[parallel-in-time-object-oriented-electromagnetic-transient-simulation-of-power-s|Parallel-in-Time Object-Oriented Electromagnetic Transient S]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[a-parallelization-in-time-approach-for-accelerating-emt-simulations|A parallelization-in-time approach for accelerating EMT simu]] | 2021 |
| [[an-fpga-based-electromagnetic-transient-analysis-of-power-distribution-network|An FPGA based electromagnetic transient analysis of power di]] | 2021 |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient|Comparison and Selection of Grid-Tied Inverter Models for Ac]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[implementation-of-the-universal-line-model-in-the-alternative-transients-program|Implementation of the universal line model in the alternativ]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[a-testing-tool-for-converter-dominated-power-system-stochastic-electromagnetic-t|A Testing Tool for Converter-Dominated Power System: Stochas]] | 2022 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems W]] | 2022 |
| [[co-simulation-applied-to-power-systems-with-high-penetration-of-distributed-ener|Co-simulation applied to power systems with high penetration]] | 2022 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using|Fast Simulation Model of Voltage Source Converters With Arbi]] | 2022 |
| [[full-state-arm-average-value-model-for-simulation-of-active-modular-multilevel-c|Full-state Arm Average Value Model for Simulation of Active ]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[neural-electromagnetic-transients-program|Neural Electromagnetic Transients Program]] | 2022 |
| [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation|Phase-domain model of twelve-phase synchronous machine for E]] | 2022 |
| [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation|Phase-domain model of twelve-phase synchronous machine for E]] | 2022 |
| [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb|The Averaged-value Model of a Flexible Power Electronics Bas]] | 2022 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报-36|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报|中  国  电  机  工  程  学  报]] | 2022 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[模块化多电平换流器的高效电磁暂态仿真方法研究|模块化多电平换流器的高效电磁暂态仿真方法研究]] | 2022 |
| [[混合型mmc全状态高效电磁暂态仿真方法研究|混合型MMC全状态高效电磁暂态仿真方法研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[级联h桥型电力电子变压器的电磁暂态等效建模方法|级联H桥型电力电子变压器的电磁暂态等效建模方法]] | 2022 |
| [[高频隔离型电力电子变压器电磁暂态加速仿真方法与展望|高频隔离型电力电子变压器电磁暂态加速仿真方法与展望]] | 2022 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-|An Automatable Approach for Small-Signal Stability Analysis ]] | 2023 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[fast-electromagnetic-transient-simulation-method-for-mmc-hvdc-system|Fast electromagnetic transient simulation method for MMC-HVD]] | 2023 |
| [[fast-electromagnetic-transient-simulation-of-modular-multilevel-converter-based-|Fast electromagnetic transient simulation of modular multile]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-|Generalized Electromagnetic Transient Equivalent Modeling an]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e|Optimized high-frequency white-box transformer model for imp]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Sparse solver application for parallel real-time electromagn]] | 2023 |
| [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids|Unified MANA-based load-flow for multi-frequency hybrid AC/D]] | 2023 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[交直流电力系统分割并行电磁暂态数字仿真方法|交直流电力系统分割并行电磁暂态数字仿真方法]] | 2023 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[多类型子模块mmc电磁暂态通用建模和实现方法|多类型子模块MMC电磁暂态通用建模和实现方法]] | 2023 |
| [[大功率链式statcom电磁暂态快速等效建模和误差评估|大功率链式STATCOM电磁暂态快速等效建模和误差评估]] | 2023 |
| [[新能源高占比电力系统电磁暂态并行仿真的优化分网方法|新能源高占比电力系统电磁暂态并行仿真的优化分网方法]] | 2023 |
| [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga|A waveform-dependence lightning impulse corona model in PSCA]] | 2024 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[基于fpga的电力电子恒导纳开关模型修正算法及实时仿真架构|基于FPGA的电力电子恒导纳开关模型修正算法及实时仿真架构]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[大规模海上风电场电磁暂态受控源解耦加速模型|大规模海上风电场电磁暂态受控源解耦加速模型]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[非隔离型直流变压器的快速电磁暂态等效建模方法|非隔离型直流变压器的快速电磁暂态等效建模方法]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener-1|A Component-Level Modeling and Fine-Grained Simulation Metho]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State Variables Elimination-Based EMTP-Type Constant Admit]] | 2025 |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based|A state-variable-preserving method for the efficient modelli]] | 2025 |
| [[accelerating-electromagnetic-transient-simulations-using-graphical-processing-un|Accelerating electromagnetic transient simulations using gra]] | 2025 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|An Electromagnetic Transient Simulation Model of MMC-BESS fo]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[compact-scheme-challenges-in-emt-type-simulations|Compact scheme challenges in EMT-Type simulations]] | 2025 |
| [[discretized-impedance-based-modeling-of-converter-interfaced-energy-resources-fo|Discretized Impedance-Based Modeling of Converter-Interfaced]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[partial-refactorization-techniques-for-electromagnetic-transient-simulations|Partial Refactorization Techniques for Electromagnetic Trans]] | 2025 |
| [[partial-refactorization-techniques-for-electromagnetic-transient-simulations|Partial Refactorization Techniques for Electromagnetic Trans]] | 2025 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[simulation-of-electromagnetic-transients-with-a-family-of-implicit-multi-step-os|Simulation of electromagnetic transients with a family of im]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[基于fpga的变电站实时仿真培训系统|基于FPGA的变电站实时仿真培训系统]] | 2025 |
| [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map|Dead-time effect modeling for hybrid modular multilevel conv]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[equivalent-modeling-of-electromagnetic-transient-for-mmc-hvdc-based-on-semi-impl|Equivalent modeling of electromagnetic transient for MMC-HVD]] | 2026 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability|RMS&#x002B;: Augmenting the Traditional Circuit Model to Cap]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |
