---
title: "EMT Simulation (电磁暂态仿真)"
type: topic
tags: [emt, electromagnetic-transient, time-domain, simulation, power-system]
created: "2026-05-02"
---

# EMT Simulation (电磁暂态仿真)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[主要分支与机制]
    N1 --> N2
    N3[形式化表达]
    N2 --> N3
    N4[适用边界与失败模式]
    N3 --> N4
    N5[代表性来源]
    N4 --> N5
    N6[与相关页面的关系]
    N5 --> N6
    N7[形式化表达补充]
    N6 --> N7
```


## 定义与边界

电磁暂态仿真是对电力系统相域网络、元件微分方程、开关事件和控制系统进行时域求解的仿真范式。它主要用于研究 [[electromagnetic-transient]]、开关暂态、雷电冲击、故障波形、电力电子控制和保护动作等快速过程。

EMT 仿真不是所有动态仿真的最高保真替代品。若研究对象是长期经济调度、慢速频率恢复或市场出清，正序潮流、机电暂态或优化模型可能更合适；若使用平均值模型或等值模型，结论应随模型层级降级。

## EMT 中的作用

EMT 的价值在于保留对相别、瞬时波形、开关时刻、非线性元件和控制采样敏感的动态。典型问题包括：

- [[switching-transient]]、[[lightning-overvoltage]] 和 [[fault-analysis]] 中的峰值、波前、暂态能量和保护判据。
- [[vsc-hvdc]]、[[mmc-model]]、[[facts]]、[[pv-power-plant]] 等电力电子系统的控制交互和限流行为。
- [[frequency-domain-analysis]] 或 [[harmonic-analysis]] 发现风险后，用时域波形交叉验证振荡、谐波和非线性触发。
- [[real-time-simulation]] 与 [[hil-simulation]] 中的控制保护闭环验证。

## 主要分支与机制

- 网络方程：常以 [[nodal-admittance-matrix]] 组织相域节点电压和支路电流，配合伴随电路或状态方程形成离散步进。
- 状态方程：[[state-space-method]] 适合连续状态、控制器和多端口元件建模，可与节点方程组合。
- 数值积分：[[trapezoidal-rule]]、[[backward-euler]] 和其他 [[numerical-integration]] 方法决定数值阻尼、稳定性和事件后振荡风险。
- 开关与非线性：[[ideal-switch-model]]、[[detailed-switch-model]]、[[magnetic-saturation-modeling]] 和非线性迭代决定模型能否反映关键物理过程。
- 多尺度扩展：[[average-value-model]]、[[dynamic-phasor]]、[[multirate-method]]、[[co-simulation]] 和 [[parallel-computing]] 用于在计算负担和保真度之间折中。

## 形式化表达

EMT 步进通常可以写成离散化后的网络代数方程和元件状态更新：

$$
Y_k v_k = i^{\mathrm{hist}}_k + i^{\mathrm{src}}_k,\qquad
x_{k+1}=F_h(x_k,v_k,u_k,s_k)
$$

其中 $Y_k$ 是可能随拓扑或等值改变的节点导纳矩阵，$v_k$ 是节点电压，$i^{\mathrm{hist}}_k$ 是伴随电路历史源，$x_k$ 是元件或控制状态，$s_k$ 表示开关和事件状态。不同 EMT 工具和方法的差别，主要体现在 $Y_k$ 的组装方式、$F_h$ 的积分公式和事件处理策略。

## 适用边界与失败模式

- 时间步长不能用单一经验比例代替验证；需要根据最高关注频率、开关事件、控制采样和数值稳定性选择。
- EMT 详细波形依赖参数质量。线路频变参数、变压器饱和、控制器限幅和保护定值缺失时，结果只能作为场景分析。
- 梯形积分在开关事件和刚性系统中可能产生数值振荡；后向欧拉或阻尼处理会改变高频响应，需要说明取舍。
- 大规模 EMT 可能因初始化、非线性迭代、矩阵重构和事件密度而失败；加速方法必须报告基准和误差边界。

## 代表性来源

- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]] 是 EMT 建模传统的来源入口，适合追踪 EMTP 型时域建模思想。
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 支撑状态空间与节点方法组合的机制讨论。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] 可用于比较伴随电路 EMT 实现的数值差异。
- [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms]] 提醒算法精度需要绑定测试系统和指标，而不是用”高精度”概括。

## 与相关页面的关系

- [[electromagnetic-transient]] 定义现象对象；本页定义仿真范式。
- [[emt-mathematical-foundation]] 更适合承载 KCL/KVL、微分代数方程和离散化推导。
- [[real-time-simulation]] 讨论实时 deadline；它是 EMT 的一种执行约束，不是所有 EMT 的默认形态。
- [[frequency-domain-analysis]] 提供频域识别和阻抗视角；EMT 提供时域非线性和事件验证。

## 形式化表达补充

### 数值积分稳定性

梯形法则的局部截断误差：
$$\tau_n = -\frac{h^3}{12}y^{(4)}(\xi), \quad \xi \in [t_n, t_{n+1}]$$

后向欧拉法的绝对稳定区域覆盖整个左半平面，适合刚性系统。

### 开关事件处理

开关时刻 $t_{sw}$ 的插值：
$$v(t_{sw}) = v(t_n) + \frac{t_{sw} - t_n}{h}(v(t_{n+1}) - v(t_n))$$

临界点检测：$i(t_n) \cdot i(t_{n+1}) < 0$ 表示二极管在区间内导通。

### 误差控制

相对误差和绝对误差控制：
$$\text{err} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}\left(\frac{|y_i - \hat{y}_i|}{\text{atol} + \text{rtol} \cdot |y_i|}\right)^2}$$

## 开放问题

- 如何为黑盒电力电子设备建立既可共享又可验证的 EMT 模型。
- 如何在大规模系统中系统报告模型层级、参数来源、步长、误差和计算性能。
- 如何把频域稳定性、机电暂态和 EMT 波形验证组织成一致的证据链。
- 如何在保证精度的前提下将 EMT 仿真扩展到大规模系统（>10000节点）。
- 如何处理高比例电力电子设备接入带来的新暂态特性。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[new-multiphase-mode-domain-transmission-line-model|New multiphase mode domain transmission line model]] | 1999 |
| [[a-systematical-method-for-suppressing-ferroresonance-at-neutral-grounded-substat|A systematical method for suppressing ferroresonance at neut]] | 2001 |
| [[a-wavelet-transform-based-method-for-improved-modeling-of-transmission-lines-pow|A wavelet transform-based method for improved modeling of tr]] | 2001 |
| [[a-wavelet-transform-based-method-for-improved-modeling-of-transmission-lines-pow|A wavelet transform-based method for improved modeling of tr]] | 2001 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[37s0142-061528962900045-2|37/s0142-0615%2896%2900045-2]] | 2003 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS V]] | 2004 |
| [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-|A Z-transform model of transformers for the study of electro]] | 2004 |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP - Power Deli]] | 2004 |
| [[a-transformer-model-for-winding-fault-studies-power-delivery-ieee-transactions-o|A transformer model for winding fault studies - Power Delive]] | 2004 |
| [[creating-an-electromagnetic-transients-program-in-matlab-matemtp-power-delivery-|Creating An Electromagnetic Transients Program In Matlab: Ma]] | 2004 |
| [[decision-tree-based-methodology-for-high-impedance-fault-detection|Decision tree-based methodology for high impedance fault det]] | 2004 |
| [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on|EMTP Modeling Of Electromagnetic Transients - Power Delivery]] | 2004 |
| [[error-in-propagation-velocity-due-to-staircase-approximation-of-an-inclined-thin|Error in propagation velocity due to staircase approximation]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[mode-domain-multiphase-transmission-line-model-use-in-transient-studies-power-de|Mode domain multiphase transmission line model - use in tran]] | 2004 |
| [[modeling-a-mixed-residential-commercial-load-for-simulations-involving-large-dis|Modeling A Mixed Residential-commercial Load  For Simulation]] | 2004 |
| [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s|Modeling Synchronous Voltage Source Converters in Transmissi]] | 2004 |
| [[modelling-of-single-phase-nonuniform-transmission-lines-in-electromagnetic-trans|Modelling of Single-Phase Nonuniform Transmission Lines in E]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow|Multiprocessor based generator module for a real-time power ]] | 2004 |
| [[protection-system-representation-in-the-electromagnetic-transients-program-power|Protection system representation in the Electromagnetic Tran]] | 2004 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[a-systematic-approach-to-the-evaluation|A Systematic Approach to the Evaluation]] | 2005 |
| [[a-systematic-approach-to-the-evaluation|A Systematic Approach to the Evaluation]] | 2005 |
| [[a-new-procedure-to-derive-transmission-line-parameters-applications-and-restrict|A new procedure to derive transmission-line parameters Appli]] | 2005 |
| [[a-new-procedure-to-derive-transmission-line-parameters-applications-and-restrict|A new procedure to derive transmission-line parameters Appli]] | 2005 |
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[application-of-emtp-in-the-research-of-uhv-ac-power-transmission|Application of EMTP in the research of UHV AC power transmis]] | 2006 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat|Nested fast and simultaneous solution for time-domain simula]] | 2006 |
| [[potential-risk-of-failures-in-switching-ehv-shunt-reactors|Potential risk of failures in switching EHV shunt reactors]] | 2006 |
| [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation|Application of EMTP-RV graphic software of electromagnetic t]] | 2007 |
| [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation|Application of EMTP-RV graphic software of electromagnetic t]] | 2007 |
| [[noda-a-binary-frequency-region-partitioning-algorithm-for-the-identification-of-|Noda | A Binary Frequency-Region Partitioning Algorithm for ]] | 2007 |
| [[on-a-new-approach-for-the-simulation-of-transients|On a new approach for the simulation of transients]] | 2007 |
| [[re-examination-of-synchronous-machine|Re-examination of Synchronous Machine]] | 2007 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[earth-return-impedances-of-conductor-arrangements-13&14|Earth Return Impedances of Conductor Arrangements]] | 2008 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[a-time-domain-ac-electric-arc-furnace-model-for-flicker-planning-studies|A Time-Domain AC Electric Arc Furnace Model for Flicker Plan]] | 2009 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[fast-realization-of-the-modal-vector-fitting|Fast Realization of the Modal Vector Fitting]] | 2009 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas|Chen 等 | A hybrid parallel computation algorithm and its app]] | 2010 |
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Efﬁcient Modeling of Modular Multilevel HVDC]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Modeling of ac machines using a voltage-behind-reactance for]] | 2010 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[a-robust-and-efficient-iterative-scheme-for-the-emt-simulations-of-nonlinear-cir-fix|A Robust and Efficient Iterative Scheme for the EMT Simulati]] | 2011 |
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|A combined state-space nodal method for the simulation of po]] | 2011 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[magnetically-saturable-voltage-behind-reactance-model-for-induction-machines|Magnetically Saturable Voltage Behind Reactance Model for In]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri|Proposal of an alternative transmission line model for symme]] | 2011 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 |
| [[modal-domain-based-modeling-of-parallel-transmission-lines|Modal Domain Based Modeling of Parallel Transmission Lines]] | 2012 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati|Photovoltaic generator modelling to improve numerical robust]] | 2012 |
| [[基于数字混合仿真的电网一次时间常数计算方法|基于数字混合仿真的电网一次时间常数计算方法]] | 2012 |
| [[damping-multimodal-subsynchronous-resonance-using-a-generator-terminal-subsynchr|Damping multimodal subsynchronous resonance using a generato]] | 2013 |
| [[dynamic-averaged-and-simplified-models-for|Dynamic Averaged and Simplified Models for]] | 2013 |
| [[fast-and-efficient-calculation-of-lightning-induced-voltages-in-frequency-depend|Fast and efficient calculation of lightning-induced voltages]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[published-in-iet-generation-transmission-distribution-27&28|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2013 |
| [[published-in-iet-generation-transmission-distribution-27&28|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2013 |
| [[ahmed-等-a-computationally-efficient-continuous-model-for-the-modular-multilevel-|Ahmed 等 | A Computationally Efficient Continuous Model for t]] | 2014 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g|Comparative study on electromechanical and electromagnetic t]] | 2014 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio|EMTP model of a bidirectional multilevel solid state transfo]] | 2014 |
| [[fast-voltage-balancing-control-and-fast-19、20、21|Fast Voltage-Balancing Control and Fast]] | 2014 |
| [[fast-voltage-balancing-control-and-fast|Fast Voltage-Balancing Control and Fast Numerical Simulation]] | 2014 |
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model|Fitting the frequency-dependent parameters in the Bergeron l]] | 2014 |
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model|Fitting the frequency-dependent parameters in the Bergeron l]] | 2014 |
| [[on-fixed-point-iterations-for-the-solution-of-control-equations-in-power-systems|On fixed-point iterations for the solution of control equati]] | 2014 |
| [[parallel-massive-thread-electromagnetic-transient-simulation-on-gpu|Parallel Massive-Thread Electromagnetic Transient Simulation]] | 2014 |
| [[parallel-massive-thread-electromagnetic-transient-simulation-on-gpu|Parallel Massive-Thread Electromagnetic Transient Simulation]] | 2014 |
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an undergr]] | 2014 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[an-extended-habedanks-equation-based-emtp-model-of-pantograph-arcing-considering-fix|An Extended Habedank]] | 2015 |
| [[analysing-a-power-transformers-internal-response-to-system-transients-using-a-hy|Analysing a power transformer⠒s internal response to system ]] | 2015 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[duality-based-transformer-model-including-13&14|Duality-Based Transformer Model Including]] | 2015 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method|Frequency-dependent multiconductor line model based on the B]] | 2015 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method|Frequency-dependent multiconductor line model based on the B]] | 2015 |
| [[implementation-of-an-integrated-online-instantaneous-discrete-wavelet|Implementation of an integrated online instantaneous discret]] | 2015 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[29tpwrd20162518676-2|29/TPWRD.2016.2518676]] | 2016 |
| [[29tpwrd20162590569-2|29/TPWRD.2016.2590569]] | 2016 |
| [[31tpwrd20162529662-2|31/tpwrd.2016.2529662]] | 2016 |
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies|A Wideband Equivalent Model of Type-3 Wind Power Plants for ]] | 2016 |
| [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu|An Efficient and Accurate Calculation of Electric Field and ]] | 2016 |
| [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu|An Efficient and Accurate Calculation of Electric Field and ]] | 2016 |
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|An automated FPGA real-time simulator for power electronics ]] | 2016 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[current-source-modular-multilevel-converter-modeling-and-control|Current Source Modular Multilevel Converter Modeling and Con]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe|Extension of a modal-domain transmission line model for incl]] | 2016 |
| [[extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe|Extension of a modal-domain transmission line model for incl]] | 2016 |
| [[extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe|Extension of a modal-domain transmission line model for incl]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o|Influence of frequency characteristics of soil on lightning ]] | 2016 |
| [[基于rtds和fpga联合仿真平台的多速率实时仿真方法|基于RTDS和FPGA联合仿真平台的多速率实时仿真方法]] | 2016 |
| [[30tpwrd20172714639-2|30/TPWRD.2017.2714639]] | 2017 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a|A Novel Interfacing Technique for Distributed Hybrid Simulat]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[lightning-impulse-voltage-distribution-over-voltage-transformer-windings-simulat|Lightning impulse voltage distribution over voltage transfor]] | 2017 |
| [[modal-decoupling-of-overhead-transmission-lines-using-real-and-constant-matrices|Modal decoupling of overhead transmission lines using real a]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[32tpwrd20182812753-2|32/TPWRD.2018.2812753]] | 2018 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[accurate-simulation-model-for-a-three-phase-ferroresonant-circuit-in-emtpatp|Accurate simulation model for a three-phase ferroresonant ci]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[electromagnetic-disturbances-in-gas-insulated-substations-and-vft-calculations|Electromagnetic disturbances in gas-insulated substations an]] | 2018 |
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[field-validated-generic-emt-type-model-of-a-full-converter-wind-turbine-based-on|Field Validated Generic EMT-Type Model of a Full Converter W]] | 2018 |
| [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio|Functional Mock-up Interface Based Approach for Parallel and]] | 2018 |
| [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio|Functional Mock-up Interface Based Approach for Parallel and]] | 2018 |
| [[general-approach-for-accurate-resonance-analysis-in-transformer-windings|General approach for accurate resonance analysis in transfor]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[38tpwrd20182794887|Time-Window Based Discrete-Time Fourier Series for Electroma]] | 2018 |
| [[大规模交直流电网电磁暂态数模混合仿真平台构建及验证|大规模交直流电网电磁暂态数模混合仿真平台构建及验证]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr|A Novel Ultra-High-Speed Traveling-Wave Protection Principle]] | 2019 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[accelerated-sparse-matrix-based-computation-of-electromagnetic-transients|Accelerated Sparse Matrix-Based Computation of Electromagnet]] | 2019 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm|An Efficient Phase Domain Synchronous Machine Model With Con]] | 2019 |
| [[distance-protection-scheme-for-dc-distribution-systems-based-on-the-high-frequen|Distance Protection Scheme for DC Distribution Systems Based]] | 2019 |
| [[distance-protection-scheme-for-dc-distribution-systems-based-on-the-high-frequen|Distance Protection Scheme for DC Distribution Systems Based]] | 2019 |
| [[dual-band-reduced-order-model-of-an-hvdc-link-embedded-into-a-power-network-for-|Dual-Band Reduced-Order Model of an HVDC Link Embedded into ]] | 2019 |
| [[dynamic-model-reduction-of-power-electronic-interfaced-generators-based-on-singu|Dynamic model reduction of power electronic interfaced gener]] | 2019 |
| [[effects-of-cable-insulations-physical-and-geometrical-parameters-on-sheath-trans|Effects of cable insulations’ physical and geometrical param]] | 2019 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre|Functional Mock-Up Interface Based Parallel Multistep Approa]] | 2019 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[mmc-upfc电磁-机电混合仿真技术研究|MMC-UPFC电磁-机电混合仿真技术研究]] | 2019 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[multi-layer-earth-structure-approximation-by-a-homogeneous-conductivity-soil-for|Multi-layer Earth Structure Approximation by a Homogeneous C]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[考虑换流器内部故障的lcc-hvdc动态平均化建模方法-13&14|考虑换流器内部故障的LCC-HVDC动态平均化建模方法]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|A Novel Linking-Domain Extraction Decomposition Method for P]] | 2020 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-|A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro]] | 2020 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo|An Inverter Model Simulating Accurate Harmonics with Low Com]] | 2020 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co|Analysis of low frequency interactions of DFIG wind turbine ]] | 2020 |
| [[analytical-study-of-the-frequencydependent-earth-conduction-effects-on-undergrou|Analytical study of the frequency‐dependent earth conduction]] | 2020 |
| [[application-of-duality-based-equivalent-circuits-for-modeling-multilimb-transfor|Application of Duality-Based Equivalent Circuits for Modelin]] | 2020 |
| [[characteristics-and-optimal-configuration-of-capacitive-current-limiter-consider|Characteristics and Optimal Configuration of Capacitive Curr]] | 2020 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[development-of-a-voltage-dependent-line-model-to-represent-the-corona-effect-in-|Development of a Voltage-Dependent Line Model to Represent t]] | 2020 |
| [[dynamic-equivalence-method-of-ddpmsg-wind-farm-for-sub-synchronous-oscillation-a|Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synch]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo|Interpolation for power electronic circuit simulation revisi]] | 2020 |
| [[lightning-induced-voltage-analysis-on-a-three-phase-compact-distribution-line-co|Lightning-induced voltage analysis on a three-phase compact ]] | 2020 |
| [[parallel-in-time-object-oriented-electromagnetic-transient-simulation-of-power-s|Parallel-in-Time Object-Oriented Electromagnetic Transient S]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations]] | 2021 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[a-parallelization-in-time-approach-for-accelerating-emt-simulations|A parallelization-in-time approach for accelerating EMT simu]] | 2021 |
| [[accurate-time-domain-simulation-of-power-electronic-circuits|Accurate time-domain simulation of power electronic circuits]] | 2021 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[an-efficient-analytical-based-technique-to-numerical-calculation-of-extended-ear|An efficient analytical based technique to numerical calcula]] | 2021 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a|Assessment of dynamic phasor extraction methods for power sy]] | 2021 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With ]] | 2021 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters W]] | 2021 |
| [[compact-matrix-formulation-for-calculating-lightning-induced-voltages-on-electro|Compact Matrix Formulation for Calculating Lightning-Induced]] | 2021 |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient|Comparison and Selection of Grid-Tied Inverter Models for Ac]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Control and Simulation of a Grid-Forming Inverter for Hybrid]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[development-and-validation-of-a-new-detailed-emt-type-component-based-load-model|Development and Validation of a New Detailed EMT-type Compon]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[equivalent-circuit-model-of-a-transmission-tower-considering-a-lightning-struck-|Equivalent Circuit Model of a Transmission Tower Considering]] | 2021 |
| [[evaluation-of-the-extended-modal-domain-model-in-the-calculation-of-lightning-in|Evaluation of the extended modal-domain model in the calcula]] | 2021 |
| [[extension-of-vances-closed-form-approximation-to-calculate-the-ground-admittance|Extension of Vance]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth-19、20、21|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[grid-forming-converters-sufficient-conditions-for-rms-modeling|Grid-forming converters: Sufficient conditions for RMS model]] | 2021 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[implementation-of-the-universal-line-model-in-the-alternative-transients-program|Implementation of the universal line model in the alternativ]] | 2021 |
| [[laplace-transform-inversion-through-the-theta-algorithm-for-power-system-emt-ana|Laplace transform inversion through the theta algorithm for ]] | 2021 |
| [[laplace-transform-inversion-through-the-theta-algorithm-for-power-system-emt-ana|Laplace transform inversion through the theta algorithm for ]] | 2021 |
| [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable|Modal propagation characteristics and transient analysis of ]] | 2021 |
| [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable|Modal propagation characteristics and transient analysis of ]] | 2021 |
| [[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat|Modelica-based simulation of electromagnetic transients usin]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti|A Piecewise Generalized State Space Model of Power Converter]] | 2022 |
| [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien|A Transformer Model With Hysteresis Characteristics for Elec]] | 2022 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Accelerated Electromagnetic Transient (EMT) Equivalent Model]] | 2022 |
| [[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-|Acceleration of electromagnetic transient simulations in mod]] | 2022 |
| [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms|Accuracy Evaluation of Electromagnetic Transients Simulation]] | 2022 |
| [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution|Active Damping Control and Parameter Calculation for Resonan]] | 2022 |
| [[algorithm-for-fast-calculating-the-energization-overvoltages-along-a-power-cable|Algorithm for fast calculating the energization overvoltages]] | 2022 |
| [[analysis-on-induced-voltages-in-wind-farms-close-to-distribution-lines-on-freque|Analysis on Induced Voltages in Wind Farms Close to Distribu]] | 2022 |
| [[analysis-on-non-characteristic-harmonic-circulating-current-in-parallel-inverter|Analysis on non-characteristic harmonic circulating current ]] | 2022 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems W]] | 2022 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir|Characteristic Analysis of High-frequency Resonance of Flexi]] | 2022 |
| [[coupling-model-for-time-domain-analysis-of-nonparallel-overhead-wires-and-buried|Coupling model for time-domain analysis of nonparallel overh]] | 2022 |
| [[design-of-hybrid-series-converter-valve-considering-device-switching-characteris|Design of hybrid series converter valve considering device s]] | 2022 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode|Efficient steady state analysis of the grid using electromag]] | 2022 |
| [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based|Electromagnetic Modeling of Transformers in EMT-Type Softwar]] | 2022 |
| [[electromagnetic-modeling-of-inductors-in-emt-type-software-by-three-circuit-base|Electromagnetic modeling of inductors in EMT-type software b]] | 2022 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using|Fast Simulation Model of Voltage Source Converters With Arbi]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[full-state-arm-average-value-model-for-simulation-of-active-modular-multilevel-c|Full-state Arm Average Value Model for Simulation of Active ]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio|Influence of a lossy ground on the lightning performance of ]] | 2022 |
| [[interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg|Interfacing real-time and offline power system simulation to]] | 2022 |
| [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st|MSEMT: An Advanced Modelica Library for Power System Electro]] | 2022 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVD]] | 2022 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVD]] | 2022 |
| [[2728modeling|Modeling_of_LCC_HVDC_Systems_Using_Dynam]] | 2022 |
| [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte|Multi-timescale simulator of nonlinear electrical elements b]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation|Phase-domain model of twelve-phase synchronous machine for E]] | 2022 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-|A Thévenin-Type Version of the Extended Modal-Domain Model f]] | 2023 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth|A new sequence domain EMT-level multi-input multi-output fre]] | 2023 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transm]] | 2023 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-|An Automatable Approach for Small-Signal Stability Analysis ]] | 2023 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech|An aggregation method of permanent magnet synchronous wind f]] | 2023 |
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|An improved high-accuracy interpolation method for switching]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[analytical-and-measurement-based-wideband-two-port-modeling-of-dc-dc-converters-|Analytical and measurement-based wideband two-port modeling ]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation|DQ Admittance Model Extraction for IBRs via Gaussian Pulse E]] | 2023 |
| [[electrical-power-and-energy-systems-148-2023-108967|Electrical Power and Energy Systems 148 (2023) 108967]] | 2023 |
| [[electromagnetic-transient-emt-simulation-algorithms-for-evaluation-of-large-scal|Electromagnetic Transient (EMT) Simulation Algorithms for Ev]] | 2023 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati|Equivalent grid-following inverter-based generator model for]] | 2023 |
| [[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-|Equivalent model of nearest level modulation for fast electr]] | 2023 |
| [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour|Fast Electromagnetic Transient Modeling Method for Half-brid]] | 2023 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-|Generalized Electromagnetic Transient Equivalent Modeling an]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi|Improved methods for optimization of power systems with rene]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us|Inaccuracies due to the frequency warping in simulation of e]] | 2023 |
| [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Lessons learned in porting offline large-scale power system ]] | 2023 |
| [[locating-arc-faults-on-coupling-two-parallel-transmission-lines-using-the-novel-|Locating arc faults on coupling two parallel transmission li]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|Modeling of MMC-based STATCOM with embedded energy storage f]] | 2023 |
| [[on-site-measurement-of-the-hysteresis-curve-for-improved-modelling-of-transforme|On-site measurement of the hysteresis curve for improved mod]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[多有源桥型电力电子变压器简化电磁暂态等效模型|多有源桥型电力电子变压器简化电磁暂态等效模型]] | 2023 |
| [[a-bidirectional-interleaved-totem-pole-pfc-based-integrated-on-board-charger-for|A Bidirectional Interleaved Totem Pole PFC-Based Integrated ]] | 2024 |
| [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation|A Semi-Analytical Approach for State-Space Electromagnetic T]] | 2024 |
| [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga|A waveform-dependence lightning impulse corona model in PSCA]] | 2024 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
| [[data-driven-parameter-calibration-of-power-system-emt-model-based-on-sobol-sensi|Data-Driven Parameter Calibration of Power System EMT Model ]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic Transient Analysis Using a Frequency Depende]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy--16|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[high-efficiency-modeling-of-multi-layer-cascaded-dual-active-bridge-dab-units-on|High Efficiency Modeling of Multi-Layer Cascaded Dual-Active]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[inverter-based-resources-model-verification-using-electromagnetic-transient-play|Inverter-Based Resources Model Verification Using Electromag]] | 2024 |
| [[inverter-based-resources-model-verification-using-electromagnetic-transient-play|Inverter-Based Resources Model Verification Using Electromag]] | 2024 |
| [[machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc|Machine-Learning-Reinforced Massively Parallel Transient Sim]] | 2024 |
| [[modelling-of-electromagnetic-transients-in-multi-unit-high-voltage-circuit-break|Modelling of electromagnetic transients in multi-unit high-v]] | 2024 |
| [[modelling-of-electromagnetic-transients-in-multi-unit-high-voltage-circuit-break|Modelling of electromagnetic transients in multi-unit high-v]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[基于fpga的电力电子恒导纳开关模型修正算法及实时仿真架构|基于FPGA的电力电子恒导纳开关模型修正算法及实时仿真架构]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[非隔离型直流变压器的快速电磁暂态等效建模方法|非隔离型直流变压器的快速电磁暂态等效建模方法]] | 2024 |
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul|A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Con]] | 2025 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener-1|A Component-Level Modeling and Fine-Grained Simulation Metho]] | 2025 |
| [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-new-model-of-trapped-charge-sources-in-switching-transient-studies-in-the-pres|A New Model of Trapped Charge Sources in Switching Transient]] | 2025 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State Variables Elimination-Based EMTP-Type Constant Admit]] | 2025 |
| [[a-computationally-efficient-approach-for-power-semiconductor-loss-estimation-of-|A computationally efficient approach for power semiconductor]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based|A state-variable-preserving method for the efficient modelli]] | 2025 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algori]] | 2025 |
| [[accelerating-electromagnetic-transient-simulations-using-graphical-processing-un|Accelerating electromagnetic transient simulations using gra]] | 2025 |
| [[acceleration-strategies-for-emt-simulation-of-hvdc-systems|Acceleration strategies for EMT Simulation of HVDC systems]] | 2025 |
| [[acceleration-strategies-for-emt-simulation-of-hvdc-systems|Acceleration strategies for EMT Simulation of HVDC systems]] | 2025 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[adaptive-grained-exponential-integrator-algorithm-for-efficient-simulation-of-po|Adaptive-Grained Exponential Integrator Algorithm for Effici]] | 2025 |
| [[advancing-grid-forming-inverter-technology-comprehensive-pq-capability-and-perfo|Advancing Grid-Forming Inverter Technology: Comprehensive PQ]] | 2025 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|An Electromagnetic Transient Simulation Model of MMC-BESS fo]] | 2025 |
| [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o|An enhanced K-means two-step clustering method for dynamic e]] | 2025 |
| [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc|Analysis on dynamic characteristic of control mode for +/-80]] | 2025 |
| [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-|Calculation of lightning-induced voltages on a large-scale d]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[compact-scheme-challenges-in-emt-type-simulations|Compact scheme challenges in EMT-Type simulations]] | 2025 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-|Comprehensive Full-Scale Converter Wind Park Initialization ]] | 2025 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-|Comprehensive Full-Scale Converter Wind Park Initialization ]] | 2025 |
| [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel|Double-Ended Fault-Locating Method for Parallel Lines Withou]] | 2025 |
| [[emu-traction-network-modeling-of-high-speed-railway-and-electromagnetic-transien|EMU-traction network modeling of high speed railway and elec]] | 2025 |
| [[electromagnetic-transient-model-reconstruction-of-generalized-power-transmission|Electromagnetic Transient Model Reconstruction of Generalize]] | 2025 |
| [[electromagnetic-transient-modeling-and-surge-analysis-of-overhead-power-lines-ab|Electromagnetic transient modeling and surge analysis of ove]] | 2025 |
| [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w|Enhancements to Terminal Duality-based models for three-phas]] | 2025 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana|Fast investigation of control interaction risks in PV parks ]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va|Frequency and transient responses of A 275 kV pressure oil-f]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[huang-等-a-heterogeneous-multiscale-method-for-efficient-simulation-of-power-syst|Huang 等 | A Heterogeneous Multiscale Method for Efficient Si]] | 2025 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
| [[improving-emt-simulations-using-frequency-shifted-rational-approximations|Improving EMT simulations using frequency-shifted rational a]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss|Influence of approximate internal impedance formula on half-]] | 2025 |
| [[integrating-dynamic-soil-ionization-models-in-emtp-for-time-domain-simulation-of|Integrating dynamic soil ionization models in EMTP for time-]] | 2025 |
| [[integrating-dynamic-soil-ionization-models-in-emtp-for-time-domain-simulation-of|Integrating dynamic soil ionization models in EMTP for time-]] | 2025 |
| [[low-dimensional-equivalent-models-and-multithreading-based-parallel-emt-simulati|Low-Dimensional Equivalent Models and Multithreading-Based P]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati-27&28|Modeling of inductive constant power load for electromagneti]] | 2025 |
| [[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati|Modeling of inductive constant power load for electromagneti]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[大规模交直流电网电磁暂态数模混合仿真平台构建及验证-40|大规模交直流电网电磁暂态数模混合仿真平台构建及验证]] | 2025 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
| [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-|Analytical Modeling of the Half-Bridge Leg Using an Associat]] | 2026 |
| [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map|Dead-time effect modeling for hybrid modular multilevel conv]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[electromagnetic-transient-emt-and-quasi-static-time-series-qsts-co-simulation-fo|Electromagnetic transient (EMT) and quasi static time series]] | 2026 |
| [[equivalent-modeling-of-electromagnetic-transient-for-mmc-hvdc-based-on-semi-impl|Equivalent modeling of electromagnetic transient for MMC-HVD]] | 2026 |
| [[fast-electromagnetic-transient-simulation-models-of-modular-multilevel-converter|Fast electromagnetic transient simulation models of modular ]] | 2026 |
| [[gpu-parallel-rate-exponential-integrator-algorithm-for-efficient-simulation-of-p|GPU Parallel-Rate Exponential Integrator Algorithm for Effic]] | 2026 |
| [[gpu-parallel-rate-exponential-integrator-algorithm-for-efficient-simulation-of-p|GPU Parallel-Rate Exponential Integrator Algorithm for Effic]] | 2026 |
| [[harmonic-preserved-average-value-model-for-converters-in-electromagnetic-transie|Harmonic-Preserved Average-Value Model for Converters in Ele]] | 2026 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[vsc-hvdc-系统的动态相量法建模仿真分析|VSC-HVDC 系统的动态相量法建模仿真分析]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
