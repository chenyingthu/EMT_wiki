---
title: "电压源换流器 (VSC)"
type: model
tags: [vsc, hvdc, two-level, three-level, pwm]
created: "2026-04-13"
---

# 电压源换流器 (VSC)

## 概述

电压源换流器（Voltage Source Converter, VSC）是柔性直流输电和新能源并网的核心设备。相比传统的线路换相换流器（LCC），VSC具有可控性强、谐波小、可向无源网络供电等优势。

## 主要拓扑

### 1. 两电平VSC
- 最基本的VSC拓扑
- 6个IGBT/IGCT开关
- PWM调制
- 适用于中小容量应用

### 2. 三电平VSC（NPC）
- 中点箝位拓扑
- 减少开关应力
- 改善谐波特性
- 适用于风电并网

### 3. 多电平VSC
- 级联H桥
- 飞跨电容
- 接近正弦波输出

## EMT建模方法

### 详细开关模型
- 每个开关器件单独建模
- 精确表征开关动态
- 计算量大

### 平均值模型
- 开关周期平均化
- 保留基频动态
- 系统级仿真适用

### 固定导纳模型
- ADC建模
- 实时仿真适用

### 动态相量模型
- 频域VSC建模
- 混合仿真适用

## 控制系统

- 内外环控制器
- 锁相环（PLL）
- 直流电压控制
- 无功功率控制
- 故障穿越控制

## 相关方法
- [[average-value-model]]
- [[fixed-admittance]]
- [[dynamic-phasor]]

## 相关主题
- [[vsc-hvdc]]
- [[mmc-model]]
- [[real-time-simulation]]


## 论文方法分析
> 基于 19 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 电磁暂态(EMT)仿真 | 2 | Average-Value Models for Modular Multilevel Converters Operating in a  |
| 状态空间法 | 2 | High Frequency Stability Analysis and Suppression Strategy of MMC-HVDC |
| 谐波相量域(HPD)建模 | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
| EMT-HPD协同仿真 | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
| HPD输电线路模型(HPD-TLM) | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
| 解耦协调时间序列 | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
| 行波保护原理 | 1 | A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-b |
| 模电压行波分析 | 1 | A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-b |
| 二进小波变换 | 1 | A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-b |
| 小波变换模极大值(WTMM)提取 | 1 | A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-b |
| 脉冲电压-电流源对建模 | 1 | A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Mu |
| 单向松耦合求解算法 | 1 | A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Mu |
| AC/DC交互仿真技术 | 1 | A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Mu |
| 动态平均值建模 | 1 | A VSC-HVDC Model with Reduced Computational Intensity |
| 受控电流源与电压源等效 | 1 | A VSC-HVDC Model with Reduced Computational Intensity |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| VSC-HVDC系统 | 4 |
| 电压源换流器(VSC) | 3 |
| 模块化多电平换流器(MMC) | 3 |
| 直流输电线路 | 2 |
| VSC-MMC换流器 | 1 |
| 大规模交直流电网 | 1 |
| EMT交流电网模型 | 1 |
| HPD直流电网模型 | 1 |
| 输电线路 | 1 |
| 四端环形VSC直流电网电磁暂态模型 | 1 |
| VSC直流输电线路 | 1 |
| 限流电抗器 | 1 |
| 多VSC交直流电网 | 1 |
| 理想开关器件 | 1 |
| VSC（电压源换流器） | 1 |
### 验证方式分布
- **仿真**: 5 篇
- **仿真/对比**: 5 篇
- **仿真对比**: 3 篇
- **与详细电磁暂态模型进行仿真对比验证**: 1 篇
- **对比仿真**: 1 篇
- **仿真与对比**: 1 篇
- **硬件在环(HIL)实时仿真与双方法对比**: 1 篇
- **仿真与对比验证**: 1 篇
- **仿真/实验**: 1 篇
## 技术演进脉络
### 2004年 (1篇)
- **Modeling Synchronous Voltage Source Converters in Transmission System Planning S**
  - 💡 首次系统化整合VSC的EMTP、潮流与暂态稳定模型，并提出适用于规划研究的逐步初始化与模型简化方法。
  - 构建了适用于EMTP、潮流和暂态稳定研究的统一VSC建模框架。
  - 提出了带逐步初始化流程的详细暂态稳定模型及相应的简化模型。
### 2012年 (1篇)
- **A VSC-HVDC Model with Reduced Computational Intensity**
  - 💡 提出一种基于受控源的动态平均值VSC模型，通过灵活切换全频谱/基波输出模式，在保持高精度的同时大幅降低电磁暂态仿真的计算负担。
  - 提出基于动态平均值建模的简化VSC模型，有效降低含换流器电力系统的仿真计算强度。
  - 实现灵活的电压输出配置，支持用户按需生成全开关频谱或仅基波频率分量。
### 2014年 (1篇)
- **Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC G**
  - 💡 通过修正平均值模型的拓扑结构，克服了传统AVM在直流故障暂态仿真中的精度缺陷，实现了HVDC电网高效准确的电磁暂态分析。
  - 系统评估了平均值模型在VSC-HVDC电网中的适用性，并与详细电磁暂态模型进行了基准对比。
  - 揭示了现有MMC平均值模型在直流故障工况下无法准确模拟暂态过程的局限性。
### 2015年 (3篇)
- **Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems**
  - 💡 通过三项接口协议与阻抗重构创新，实现了高精度、高效率的VSC-HVDC混合暂态稳定与EMT协同仿真。
  - 提出故障后交流系统等效阻抗重构方法以提升接口计算精度。
  - 改进EMT仿真内部的戴维南等效源更新交互协议。
- **Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes**
  - 💡 首次系统对比主流MMC详细建模技术并提出改进方案，为不同应用场景提供模型选择依据。
  - 首次客观对比了三种主流MMC详细建模技术在精度与仿真速度方面的表现。
  - 提出了一种改进的建模方法，进一步提升了现有等效模型的计算效率。
- **Modulation Index Dependent Thévenin Equivalent Circuit Model of VSC and APDR**
  - 💡 提出了一种结合调制指数依赖性与变压器类比的VSC戴维南等效模型，有效解决了直流故障仿真中精度与计算效率难以兼顾的问题。
  - 提出了一种依赖于调制指数的VSC及反并联二极管整流器戴维南等效电路模型。
  - 利用正交变换和变压器类比法将交流侧阻抗准确映射至直流侧。
### 2017年 (1篇)
- **含VSC-HVDC交直流系统多尺度暂态建模与仿真研究**
  - 💡 利用希尔伯特变换进行移频分析，通过移除或保留基频载波实现单一模型在不同仿真参数下对快变电磁暂态与慢变机电暂态的统一高效仿真。
  - 建立了基于移频分析的VSC相量模型
  - 推导了移频域与控制系统dq域之间的数学转换关系
### 2019年 (2篇)
- **A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-based DC Gr**
  - 💡 将模电压行波特性与二进小波变换相结合，实现了无需通信的超高速直流线路故障区段识别与选线。
  - 提出了一种基于模电压行波特性的新型超高速直流线路保护原理。
  - 利用1模电压行波幅值变化绝对值构建了保护启动元件。
- **Modeling a voltage source converter assisted resonant current DC breaker for rea**
  - 💡 提出了一种兼顾计算效率与外部电气特性精度的VARC直流断路器系统级实时仿真建模方法，适用于未来多端直流电网的保护性能评估。
  - 在RTDS环境中建立了VARC直流断路器的详细实时仿真模型。
  - 确保模型的外部伏安特性能够准确复现真实设备的电气行为，适用于系统级研究。
### 2020年 (2篇)
- **A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analy**
  - 💡 提出了一种基于HPD与EMT协同的交直流电网仿真新架构，通过HPD-TLM接口实现跨域解耦，支持大规模电网瞬时值与谐波相量的同步输出与宽频振荡分析。
  - 提出了适用于电力电子直流电网的谐波相量域(HPD)建模方法，可同时输出瞬时值与谐波相量波形。
  - 设计了HPD输电线路模型(HPD-TLM)作为接口，实现了EMT交流电网与HPD直流电网的高效协同仿真。
- **A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Multiple-VSC**
  - 💡 利用脉冲源对表征与松耦合求解策略实现VSC开关暂态与主网络的解耦，突破了多VSC电网EMT仿真效率低下的瓶颈。
  - 提出基于脉冲电压-电流源对的VSC等效模型，从根本上避免了开关动作引发的网络矩阵频繁修改。
  - 设计了单向松耦合求解算法，实现了交直流子系统的高效解耦与交互计算。
### 2021年 (1篇)
- **High Frequency Stability Analysis and Suppression Strategy of MMC-HVDC Systems (**
  - 💡 提出了一种融合MMC全动态过程与大延时Pade近似的统一高频状态空间建模方法，并结合参与因子与根轨迹法系统揭示了柔性直流系统高频振荡的内在机理。
  - 建立了集成MMC内部动态、控制内外环、锁相环、环流抑制及大延时环节的换流站高频状态空间模型。
  - 构建了采用多π模型精确模拟线路分布参数特性的交流系统通用高频状态空间模型。
### 2022年 (2篇)
- **Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using**
  - 💡 提出两步开关状态预测机制，彻底规避了传统EMT仿真中确定可行开关组合所需的迭代计算，实现了任意拓扑VSC的快速高精度仿真。
  - 提出了一种适用于任意拓扑电压源换流器的快速电磁暂态仿真模型。
  - 设计了包含初步预测与同时开关预测的两步机制，有效避免了传统仿真中求解可行开关组合的迭代计算。
- **Modeling and electromagnetic transient simulation of VSC-HVDC system**
  - 💡 将UMEC模型参数折算方法应用于特高压自耦变压器建模，并定量阐明了特高压涌流与故障电流谐波特征对传统差动保护可靠性的影响机制。
  - 基于EMTDC平台的UMEC模型成功构建了特高压三绕组自耦变压器的电磁暂态等效模型。
  - 揭示了特高压条件下变压器三相励磁涌流二次谐波含量普遍低于10%的分布规律。
### 2023年 (3篇)
- **Fast Electromagnetic Transient Modeling Method for Half-bridge-Type Voltage Sour**
  - 💡 提出同步开关预判方法，通过逻辑判断直接得出稳定开关状态组合，彻底消除开关状态迭代计算，结合内节点收缩实现高效建模。
  - 提出基于半桥子电路的同步开关预判方法，通过逻辑判断直接获取稳定开关状态，消除传统迭代计算。
  - 结合内节点收缩方法构建适用于正常、短路、闭锁等多种工况的快速仿真模型。
- **Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation**
  - 💡 首次将常规EMT与小时间步长法并行应用于混合SVC-VSC的HIL实时仿真，并系统验证了其在电网设备改造中的工程适用性与结果一致性。
  - 提出了适用于混合SVC-VSC的两种实时HIL建模方法（常规EMT与小时间步长法）。
  - 验证了两种建模方法在合理处理仿真细节时可产生高度一致的结果。
- **Modeling and simulation of VSC-HVDC with dynamic phasors**
  - 💡 将动态相量法引入VSC-HVDC建模，通过合理截断高频傅立叶级数项，实现了仿真精度与计算效率的有效平衡。
  - 提出了基于时变傅立叶级数的VSC-HVDC动态相量建模方法。
  - 通过保留开关函数的直流与基频分量及线路直流分量，有效简化了高频开关过程。
### 2024年 (1篇)
- **Initializing EMT models of grid forming VSCs in MTDC systems**
  - 💡 提出了一种不依赖模型内部细节的通用解耦接口(DI)初始化技术，有效解决了黑盒构网型VSC在MTDC系统中的EMT仿真初始化难题。
  - 提出了一种用于构网型VSC的稳态初始化方法，有效提升了EMT仿真的数值稳定性。
  - 针对内部细节不可知的黑盒GVSC模型，提出了一种通用的解耦接口(DI)初始化方法。
### 2025年 (1篇)
- **Transient Electromagnetic Power Compensation‐Based Adaptive Inertia Control Stra**
  - 💡 将暂态电磁功率补偿机制与自适应惯量控制相融合，针对性解决了并联储能VSC因角加速度差异导致的频率振荡与超调问题。
  - 推导了并联VSC-ESS的状态空间方程与传递函数，明确了关键控制参数对系统稳定性及频率响应的影响规律。
  - 提出暂态电磁功率补偿控制策略，有效抑制了频率调节过程中的有功功率超调与振荡。
## 关键发现汇总
- [2004] **Modeling Synchronous Voltage Source Converters in Transmissi**: 所开发的暂态稳定模型在动态响应上与详细EMTP仿真结果高度一致。
- [2004] **Modeling Synchronous Voltage Source Converters in Transmissi**: 简化稳定模型在保持工程精度的同时显著降低了计算复杂度。
- [2004] **Modeling Synchronous Voltage Source Converters in Transmissi**: 提出的控制模式与额定值计算方法有效支持了输电系统规划中的电压稳定性评估。
- [2012] **A VSC-HVDC Model with Reduced Computational Intensity**: 简化模型在稳态和暂态运行条件下的仿真波形与详细模型高度吻合。
- [2012] **A VSC-HVDC Model with Reduced Computational Intensity**: 所提模型相比传统详细开关模型显著降低了CPU计算时间消耗。
- [2012] **A VSC-HVDC Model with Reduced Computational Intensity**: 模型在对称与不对称故障条件下均能保持准确的动态响应与稳定性。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: AVM仅在子模块电容足够大以维持电压近似恒定时才有效。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 传统MMC平均值模型在直流故障暂态下仿真精度严重不足。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 改进拓扑后的AVM在直流故障下仿真精度显著提升，且计算效率大幅提高。
- [2015] **Advanced Hybrid Transient Stability and EMT Simulation for V**: 所提改进接口方法显著提升了交流/VSC-HVDC系统暂态稳定评估的准确性。
- [2015] **Advanced Hybrid Transient Stability and EMT Simulation for V**: 新方法有效克服了传统接口在故障期间的相量计算误差与等效源更新延迟问题。
- [2015] **Comparison of Detailed Modeling Techniques for MMC Employed **: 传统详细模型因开关器件和电容数量庞大导致导纳矩阵求逆计算负担极重。
- [2015] **Comparison of Detailed Modeling Techniques for MMC Employed **: 详细等效模型在保持高精度的同时显著降低了仿真时间。
- [2015] **Comparison of Detailed Modeling Techniques for MMC Employed **: 改进模型在特定工况下实现了计算效率的进一步优化。
- [2015] **Modulation Index Dependent Thévenin Equivalent Circuit Model**: 模型对极间(PP)故障电流的预测几乎完全匹配，对极对地(PG)故障电流存在轻微低估。
- [2015] **Modulation Index Dependent Thévenin Equivalent Circuit Model**: 在5μs仿真步长下，等效模型计算速度比全开关模型快约3倍。
- [2015] **Modulation Index Dependent Thévenin Equivalent Circuit Model**: 当步长增大至750μs时，计算速度提升126倍且仍保持较高精度。
- [2017] **含VSC-HVDC交直流系统多尺度暂态建模与仿真研究**: 所提模型能够准确描述VSC-HVDC系统的多尺度暂态过程
- [2017] **含VSC-HVDC交直流系统多尺度暂态建模与仿真研究**: 通过调整时间步长等参数显著节省了仿真计算时间
- [2017] **含VSC-HVDC交直流系统多尺度暂态建模与仿真研究**: 有效增强了交直流系统电磁与机电暂态混合仿真的灵活性
- [2019] **A Novel Ultra-High-Speed Traveling-Wave Protection Principle**: 该保护原理在多种故障条件下均表现出优异的速动性、可靠性和鲁棒性。
- [2019] **A Novel Ultra-High-Speed Traveling-Wave Protection Principle**: 基于WTMM的算法能够准确区分区内与区外故障并完成故障选线。
- [2019] **A Novel Ultra-High-Speed Traveling-Wave Protection Principle**: 该原理可作为VSC直流电网的优秀主保护方案。
- [2019] **Modeling a voltage source converter assisted resonant curren**: 所提RTDS模型的外部电流-电压特性与真实VARC直流断路器高度一致。
- [2019] **Modeling a voltage source converter assisted resonant curren**: 在含频率相关参数的多端直流电网案例中，模型成功展示了保护算法的动作性能与断路器的快速开断能力。
- [2020] **A Harmonic Phasor Domain Co-Simulation Method and New Insigh**: 所提方法在保证瞬时值与谐波相量波形精度的同时，显著提升了大规模交直流电网的仿真计算效率。
- [2020] **A Harmonic Phasor Domain Co-Simulation Method and New Insigh**: 能够准确捕捉并复现由多换流器不同开关频率引发的宽频带谐波耦合振荡场景。
- [2020] **A Harmonic Phasor Domain Co-Simulation Method and New Insigh**: 在中国实际工程规模电网模型中验证了该方法在稳态与动态响应下波形输出的一致性与可靠性。
- [2020] **A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro**: 所提方法成功将VSC开关事件与主网络计算解耦，消除了传统EMTP中因开关动作导致的矩阵重构与LU分解瓶颈。
- [2020] **A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro**: 仿真验证表明，该方法在保持与传统详细模型同等精度的前提下，显著缩短了多VSC系统的单步计算时间。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s|Modeling Synchronous Voltage Source Converters in Transmissi]] | 2004 |
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[modulation-index-dependent-thevenin-equivalent-circuit-model-of-vsc-and-apdr|Modulation Index Dependent Thévenin Equivalent Circuit Model]] | 2015 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr|A Novel Ultra-High-Speed Traveling-Wave Protection Principle]] | 2019 |
| [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea|Modeling a voltage source converter assisted resonant curren]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-|A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro]] | 2020 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using|Fast Simulation Model of Voltage Source Converters With Arbi]] | 2022 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVD]] | 2022 |
| [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour|Fast Electromagnetic Transient Modeling Method for Half-brid]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat|Transient Electromagnetic Power Compensation‐Based Adaptive ]] | 2025 |