---
title: "无源性保证 (Passivity Enforcement)"
type: method
tags: [passivity-enforcement, positive-real, stability, frequency-dependent, vector-fitting]
created: "2026-05-04"
updated: "2026-05-12"
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

## 量化性能边界

**Zhang 2012 FDNE无源性保证（IEEE 39节点多端口等值）**:
- 针对IEEE 39节点系统，提出基于矢量拟合的频变网络等值（FDNE）方法
- 采用"先拟合总和提取公共极点，再逐元素拟合留数"的公共极点策略，确保多端口模型极点一致性
- FDNE模型在1~2 kHz频段内拟合误差（Error 1）低于1%，高精度还原原始网络宽频响应
- 无源性强制算法引入的附加误差（Error 2）可忽略不计，模型精度损失<0.5%
- 半尺寸无源性测试矩阵精准定位违规频段，参数扰动法消除非无源极点
- 验证系统：New England IEEE 39节点系统（10机39节点）
- 数据缺口：原文未报告扫描频段上限（1~2 kHz）之外的拟合性能，更宽频段或更高阶数下的无源性检查复杂度未讨论

**Gustavsen & Semlyen 2001 无源性强制基础方法**:
- 针对矢量拟合有理函数逼近的导纳矩阵，提出后处理无源性修正框架
- 通过特征值检验识别非无源频段，对非无源极点进行局部扰动修正
- 方法适用于多端口网络，可保证修正后模型的整体无源性
- 数据缺口：原文未报告不同系统规模和端口数下方法的计算复杂度和收敛性

**Triverio 2015 无源性保证综合评述**:
- 系统总结了频域响应有理模型的无源性保证方法，包括约束拟合法和后处理修正法
- 比较了基于线性矩阵不等式（LMI）、 Hamiltonian矩阵特征值检验和频域采样三种非无源频段识别方案
- 指出后处理修正法在保持拟合精度与实现无源性之间存在根本性权衡
- 数据缺口：评述未给出不同方法在统一测试基准上的横向性能对比

**设计参数约束（据方法推断）**:
- 无源性强制后的模型精度损失与原始非无源程度正相关：轻微非无源（最小特征值接近零）可通过小幅扰动修复；严重非无源需要较大修正，精度损失可能超过5%
- 多端口系统的无源性检查维度随端口数平方增长，端口数>10时半尺寸测试矩阵方法可显著降低计算量
- 无源性强制应在矢量拟合之后立即执行，作为有理模型时域实现的前置条件
- 对非无源极点的扰动应优先选择实部修正而非留数修正，以保持模型的频域拟合精度

**数据缺口声明**：无源性保证的量化数据来自三个独立方向（FDNE应用、基础方法、综合评述），各自使用不同的测试系统和评估指标。不同无源性保证方法（约束拟合 vs 后处理修正）在统一测试基准下的横向对比数据缺乏。高端口数（>20）和大频宽（DC-1MHz）场景下的无源性检查计算复杂度和可扩展性未系统评估。

## 代表性来源

- Gustavsen, B. and Semlyen, A., "Enforcing Passivity for Admittance Matrices Approximated by Rational Functions," *IEEE TPWRD*, 2001.
- Triverio, P., "Passivity Enforcement of Rational Models of Frequency Domain Responses," *IEEE TCPMT*, 2015.

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