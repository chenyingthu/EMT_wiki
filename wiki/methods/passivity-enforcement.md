---
title: "无源性保证 (Passivity Enforcement)"
type: method
tags: [passivity-enforcement, positive-real, stability, frequency-dependent, vector-fitting]
created: "2026-05-04"
---

# 无源性保证 (Passivity Enforcement)

## 定义与边界

无源性保证是指在频变参数建模过程中，确保所得模型满足无源性条件的技术。无源系统不产生能量，仅消耗或传输能量，其传递函数满足正实性条件。在EMT仿真中，无源性保证是确保频变模型（如输电线路、电缆模型）数值稳定性的关键。

**边界限定**：本方法适用于线性时不变系统的频变参数建模，非线性系统需分段线性化处理。

## EMT中的作用

- **保证EMT仿真数值稳定性**：无源模型保证仿真不会发散
- **确保模型物理可实现**：无源系统符合能量守恒定律
- **无源子系统级联保持整体无源性**：便于构建复杂系统模型
- **频变线路建模**：保证宽频模型的稳定性

## 主要分支与机制

### 1. 基于约束的拟合

在矢量拟合中直接施加无源性约束：
- 限制极点位置（左半平面）
- 约束留数保证正实性
- 优化问题带不等式约束

### 2. 后处理修正

对非无源模型进行扰动修正：
- 识别非无源频段
- 局部扰动修正
- 保持拟合精度

## 形式化表达

### 传递函数正实性条件

$$Re\{H(s)\} \geq 0, \quad \forall Re\{s\} > 0$$

### 多端口导纳矩阵无源性

$$\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega) \geq 0$$

### 频域检验条件

$$Re\{H(j\omega)\} \geq 0, \quad \forall \omega$$

## 适用边界与失败模式

### 适用条件

- 系统线性时不变
- 频响数据充分
- 原始系统本身无源

### 失效边界

- **严格非无源系统**：有源系统无法强制无源
- **数据不足**：频响数据稀疏导致无法准确判断
- **高精度要求**：强制无源可能降低拟合精度

## 与相关页面的关系

- [[vector-fitting]] - 矢量拟合方法
- [[frequency-dependent-line-model]] - 频变线路模型
- [[wideband-modeling]] - 宽频建模
- [[transmission-line-model]] - 输电线路模型
- [[cable-model]] - 电缆模型
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法

## 代表性来源

- Gustavsen, B. and Semlyen, A., "Enforcing Passivity for Admittance Matrices Approximated by Rational Functions," *IEEE TPWRD*, 2001.
- Triverio, P., "Passivity Enforcement of Rational Models of Frequency Domain Responses," *IEEE TCPMT*, 2015.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[zfunction-convolution-in-ehv|Z.function convolution in EHV]] | 2002 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Stability of Algorithms for Electro-Magnetic-Transient Simul]] | 2019 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da|Stability Evaluation of Interpolation, Extrapolation, and Nu]] | 2020 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit|Z-Tool: Frequency-domain characterization of EMT models for ]] | 2025 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |
