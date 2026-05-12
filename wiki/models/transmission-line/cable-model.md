---
title: "电缆模型 (Cable)"
type: model
tags: [cable, underground, submarine, frequency-dependent, multi-core]
created: "2026-04-13"
updated: "2026-05-12"
---

# 电缆模型 (Cable)



## 概述

电力电缆（地下电缆、海底电缆）的EMT建模需要考虑集肤效应、邻近效应、绝缘层、护套接地等复杂因素。相比架空线路，电缆的电磁耦合更强，频率相关特性更显著。

## 主要特性

### 频率相关阻抗
- 导体集肤效应
- 邻近效应（多芯电缆）
- 护套涡流效应
- 螺线管效应（三芯铠装电缆）

### 导纳参数
- 绝缘层电容
- 护套接地
- 半导体层影响

### 暂态特性
- 行波传播
- 反射与折射
- 截断电荷
-  trapped charge放电

## 建模方法

### 相域模型
- 直接多导体建模
- 考虑相间耦合

### 模域模型
- 模态变换解耦
- 频率相关变换矩阵

### 频变模型
- 矢量拟合阻抗
- 无源性强制
- 递归卷积计算

## 特殊问题

- 海底电缆长距离暂态
- 多芯电缆螺线管效应
- 土壤电离化（接地故障）
- 混合架空线-电缆线路

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]

## 相关模型
- [[transmission-line-model|输电线路模型]] - 架空线与电缆对比
- [[fdne-model|频变网络等值(FDNE)]] - 电缆网络等值
- [[transformer-model|变压器模型]] - 电缆-变压器接口
- [[grounding-system-model|接地系统模型]] - 电缆护套接地

## 相关主题
- [[frequency-dependent-modeling]]
- [[transmission-line-model]]
- [[real-time-simulation]]
- [[parallel-computing]]
- [[network-equivalent]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[parametric-study-of-transient-electromagnetic-fields|Parametric Study of Transient Electromagnetic Fields]] | 2011 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[high-performance-computing-engines-for-the-fpga-based-simulation-of-the-ulm|High performance computing engines for the FPGA-based simula]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[extension-of-vances-closed-form-approximation-to-calculate-the-ground-admittance|Extension of Vance]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |

## 量化性能边界

**Partitioned Fitting + DC Correction (2020)** — 分频段拟合与直流校正宽频电缆模型:
- 采用两阶段有理逼近：高频主模型在1 Hz–1 MHz拟合（阶数20–50），低频校正项使用低阶有理函数（阶数2–4）
- 约束线性最小二乘法控制留数/极点比 < 10³，避免时域卷积不稳定
- 宽频覆盖范围 0.001 Hz – 1 MHz，适用于长电缆充电到雷电冲击的全频谱暂态
- 数据缺口：加速比vs标准ULM未在原文中定量报告

**Advanced Wideband Line/Cable Modeling (2024)** — 自适应模式分组宽频模型:
- 96导体电缆系统：传播模式分组数从36组降至8组（>75% 压缩率），双回架空线从10组降至4组
- 快速衰减模式截断阈值 |H(jω)| < 10⁻³，有效抑制高频相位振荡（>90% 振荡抑制）
- 矢量拟合容差 0.5%，RMS拟合误差 < 0.1%
- 数据缺口：具体加速比数值和波形精度（如相关系数）在原文中未量化报告

**Measurement-Based Coaxial Model (2023)** — 实测同轴特性融合模型:
- 高频同轴模态衰减修正：绞线效应+半导电层损耗在1 MHz处提供 40–60% 增量修正
- 实测融合截止频率 500 kHz，高于此频率时传统几何模型误差显著
- 同轴模态时延精度：实测值 ±5%（vs 纯解析计算的 10–20% 误差）
- 阻抗计算误差 < 2%（MoM-SO方法，考虑邻近效应和螺线管效应）
- 数据缺口：修正系数 δ_sk, δ_sc 的通用性（不同电缆截面/材料下验证不足）

**All-Pass Delay Estimation for ULM (2026)** — 全通函数时延估计模型:
- 基于全通滤波器迭代的因果性强制：保证传播速度 v < c，消除非物理前驱波
- 迭代收敛容差 10⁻⁸（NLT参考值），最大迭代 20–50 次
- 相位振荡抑制：通过相位解缠+延迟均衡，降低高频段相位拟合残差
- 数据缺口：与标准时延提取方法（如Bode图法）的精度对比在原文中未给出

**Time-Domain Subsea Buried Cable Model (2024)** — 海底埋设电缆时域模型:
- 将土壤电离化非线性效应（σ(E) = σ₀ + k|E|^β）纳入频变电缆模型
- 数据缺口：土壤参数(k, β)的典型值范围和对暂态波形精度的量化影响未系统报告

**数据缺口声明**：电缆模型的性能边界高度依赖于电缆截面结构（单芯/三芯/同轴）、土壤分层特性和频率范围。上述模型参数主要来自各自文献的独立验证案例，缺乏统一基准（如CIGRE标准电缆模型）下的横向对比。特别是绞线效应修正系数和高频衰减增量的通用性尚未在不同电缆类型上充分验证。

---
## EMT中的作用

电缆模型 (Cable) 在EMT仿真中主要用于：

- **建模对象**：描述电缆模型 (Cable)在电力系统中的物理角色和电气特性
- **仿真场景**：适用于电缆模型 (Cable)相关的电磁暂态分析、故障响应、控制交互等场景
- **模型接口**：提供电缆模型 (Cable)的端口变量、状态方程和边界条件
- **验证基准**：可作为电缆模型 (Cable)仿真模型正确性的验证基准

## 数学模型

### 基本方程

电缆模型 (Cable)的数学模型基于以下基本物理定律：

$$
\text{待补充：基于电缆模型 (Cable)的物理特性建立数学描述}
$$

### 状态空间表示

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})
$$

$$
\mathbf{y} = \mathbf{g}(\mathbf{x}, \mathbf{u})
$$

其中 $\mathbf{x}$ 为状态向量，$\mathbf{u}$ 为输入向量，$\mathbf{y}$ 为输出向量。


*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*