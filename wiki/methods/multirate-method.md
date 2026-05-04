---
title: "多速率方法 (Multi-Rate Method)"
type: method
tags: [multirate, time-step, partitioning, interface]
created: "2026-04-13"
---

# 多速率方法 (Multi-Rate Method)

## 定义与边界

多速率方法是在同一仿真任务中为不同子系统、变量或模型层级使用不同时间步长的数值方法。它的前提是系统存在可利用的时间尺度差异，例如局部电力电子开关需要小步长，而远端交流网络或移频包络可用较大步长描述。

本页讨论 EMT 内部或紧耦合框架中的多速率数值方法。它不同于任意软件间松耦合 [[co-simulation]]，也不同于单纯的模型降阶或平均值模型；多速率方法必须显式说明分区、接口变量、采样规则和稳定性边界。

## EMT 中的作用

单速率 EMT 往往由最快暂态决定全网步长。多速率方法试图把小步长限制局部化，从而降低大规模系统的计算负担。典型用途包括：

- MMC、VSC、HVDC 局部小步长与外部电网大步长耦合。
- 移频、动态相量或包络模型与详细 EMT 子区交换接口量。
- 实时仿真中把硬件可承载的小步长区域限制在 FPGA 或局部处理器内。
- 分区并行 EMT 中减少不同区域之间的同步频率。

## 核心机制

设快子系统步长为 $h_f$，慢子系统步长为 $h_s=N h_f$，则一个慢步长内快子系统推进 $N$ 次。抽象形式为

$$
\dot{x}_f=f(x_f,x_s,u_f,t),
$$

$$
\dot{x}_s=g(x_s,x_f,u_s,t).
$$

慢到快方向通常需要保持、线性插值或高阶插值：

$$
x_s(t_m+r h_f)\approx \mathcal{I}(x_s(t_m),x_s(t_{m+1}),r/N).
$$

快到慢方向通常需要采样、平均、滤波或等效源构造。接口算法的选择会改变整体离散系统，不能只检查每个子系统的 [[numerical-integration]] 是否稳定。

## 分类与变体

| 类型 | 机制 | 边界 |
|------|------|------|
| 同步整数步长比多速率 | $h_s=N h_f$，在慢步长边界同步 | 易分析，但接口误差集中在同步点 |
| 非迭代分区多速率 | 子系统按既定顺序交换接口量 | 计算成本低，但接口延迟可能导致不稳定 |
| 迭代多速率 | 每个大步长内对接口量迭代校正 | 稳定性更好但实时性和成本受限 |
| MATE 或等效接口 | 用多端口 Thevenin/Norton 等效连接子区 | 等效频带和端口选择决定误差边界 |
| 动态相量/移频多速率 | 慢区用包络或相量变量，快区保留 EMT | 适合窄带或基频附近动态；宽频突变需谨慎 |
| 硬件实时多速率 | 不同处理器或 FPGA 任务使用不同步长 | deadline、通信延迟和量化误差成为方法边界 |

## 适用边界与失败模式

- 多速率分区应避开强非线性、频繁开关或强耦合的边界；否则接口误差可能主导结果。
- 步长比不是越大越好。稳定性取决于接口规则、系统频带、分区阻抗和采样延迟。
- A 稳定积分器在单个子系统内稳定，不保证周期性多速率整体稳定。
- 快到慢反馈若未滤除高频开关分量，可能把混叠或虚拟能量注入慢系统。
- 对故障、闭锁、保护动作等跨区突变，可能需要临时同步、降步长或切回单速率。

## 代表性来源

| 来源 | 支撑内容 | 证据边界 |
|------|----------|----------|
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations]] | 将 LTI 多速率 EMT 离散系统识别为周期时变系统，并用 lifting 特征值判据评估稳定性 | 适用范围主要是 LTI、整数步长比和被建模的非迭代接口 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems]] | SFA-EMTP 多速率把移频包络区与 EMT 区通过接口等效耦合 | 结论不应外推到所有宽频暂态或详细开关区 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]] | 大 AC 系统与 MMC-MTDC 分区仿真体现了快慢区域协同需求 | 具体精度和效率取决于原文算例、接口和步长 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne]] | 网络分区与并行多速率算法可降低部分 EMT 计算负担 | 不等同于任意分区都有稳定或加速收益 |

## 与相关页面的关系

- [[interpolation-method]] 是慢到快和事件同步的关键接口技术。
- [[numerical-integration]] 决定每个子系统内部离散推进。
- [[stiff-system-handling]] 说明为什么多时间尺度会带来刚性和局部小步长需求。
- [[fixed-admittance]] 可用于减少快区频繁开关造成的矩阵重构。
- [[dynamic-phasor]] 和 [[average-value-model]] 是多速率慢区建模的常见候选，但会牺牲部分宽频细节。
- [[network-equivalent]] 和 [[fdne-model]] 为分区接口提供等效网络表达。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[magnetically-saturable-voltage-behind-reactance-model-for-induction-machines|Magnetically Saturable Voltage Behind Reactance Model for In]] | 2011 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution|A Hybrid Simulation Tool for the Study of PV Integration Imp]] | 2016 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[基于rtds和fpga联合仿真平台的多速率实时仿真方法|基于RTDS和FPGA联合仿真平台的多速率实时仿真方法]] | 2016 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo|An Inverter Model Simulating Accurate Harmonics with Low Com]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg|Interfacing real-time and offline power system simulation to]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Real-Time HIL Emulation of DRM With Machine Learning Acceler]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation|A Semi-Analytical Approach for State-Space Electromagnetic T]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |
