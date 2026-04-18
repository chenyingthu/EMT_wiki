---
title: "Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Transients in Transmission Lines/Cables"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2018.2849854"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2018.2849854.pdf.pdf"]
---

# Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Transients in Transmission Lines/Cables

**作者**: 
**年份**: 2018
**来源**: `31/TPWRD.2018.2849854.pdf.pdf`

## 摘要

—This letter proposes a two-stage fitting procedure for transmission line/cable functions in which low frequency samples are exclusively considered. At the first stage, fitting is performed for a reduced band by excluding frequencies close to DC. Reducing the fitting range improves the numerical conditioning of the overall system of equations and relieves fitting. The second stage consists of finding a correction term for the out-of-band samples close to DC. The procedure, when used with the recently introduced frequency-dependent cable model (FDCM) approach, allows modeling transmission lines and cables with improved fitting precision at low frequencies. Overall, the new approach is called FDM (Frequency Dependent Model) with DC correction, i.e., FDM/DC. It can be used to complement the p

## 核心贡献


- 提出两阶段分区拟合策略，分离高低频段改善有理逼近数值条件
- 引入低频误差校正项，显著提升线路电缆模型在直流附近的拟合精度
- 兼容FDCM与ULM框架，消除大留极比引发的时域积分数值不稳定


## 使用的方法


- [[两阶段分区拟合|两阶段分区拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[直流误差校正|直流误差校正]]
- [[模态分组拟合|模态分组拟合]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电力电缆|电力电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[频变电缆模型-fdcm|频变电缆模型(FDCM)]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[直流响应校正|直流响应校正]]
- [[数值稳定性分析|数值稳定性分析]]
- [[高压直流输电|高压直流输电]]


## 主要发现


- 新模型在不同最高拟合频率下均能精确复现直流稳态电压与电流值
- 分区拟合避免大留极比，彻底消除传统ULM时域仿真的数值振荡
- 低频校正补偿高频拟合直流偏差，保持无源性并确保时域仿真稳定



## 方法细节

### 方法概述

本文提出FDM/DC（带直流校正的频变模型）两阶段分区拟合方法，用于输电线路和电缆的电磁暂态仿真。该方法通过将频率范围划分为高频段（HF，如1 Hz至1 MHz）和低频段（LF，如0.001 Hz至1 Hz），先对高频段进行标准有理函数拟合（使用FDCM或ULM方法），然后专门对低频段 excluded 的频率样本计算拟合误差，并对该误差函数进行独立的有理逼近作为校正项。这种分区策略避免了传统ULM在宽频带拟合时出现的大留极比（large residue/pole ratios）问题，显著改善了数值条件，消除了时域仿真中的数值振荡，同时确保直流稳态响应的精确性。

### 数学公式


**公式1**: $$$$H_{high} \cong \sum_{i=1}^{N_{gr}}\left(\sum_{j=1}^{M_i}\frac{R_{i,j}}{s_{high}-p_{i,j}}e^{-s\tau_i}\right)$$$$

*高频段传播函数的有理函数逼近，其中Ngr为模态传播组数，Mi为第i组的逼近阶数，pi,j为极点，Ri,j为留数矩阵，τi为第i模态组的时延*


**公式2**: $$$$\Delta H_{low} = H_{low} - H_{high}(s_{low}) = H_{low} - H_{low}^{fitted}$$$$

*计算低频段拟合误差，即解析传播函数Hlow与高频拟合函数在低频段取值之间的差值*


**公式3**: $$$$\Delta H_{low} \cong \sum_{j=1}^{M_{low}}\frac{R_{low,j}}{s_{low}-p_{low,j}}e^{-s\tau_1}$$$$

*低频误差校正项的有理函数逼近，使用最小传播时延τ1（因低频时延影响可忽略），Mlow为低频校正极点数*


**公式4**: $$$$H \approx H_{high} + \Delta H_{low}$$$$

*最终传播函数的合成公式，将高频拟合结果与低频校正项相加获得全频段精确模型*


### 算法步骤

1. Step 1 - 频段划分：将频率范围划分为低频段LF（0.001 Hz至1 Hz）和高频段HF（1 Hz至1 MHz），明确分界点（文中示例为1 Hz）

2. Step 2 - 高频拟合：对HF段使用FDCM或ULM方法进行有理函数拟合，获得H_high（极点、留数和时延），通常使用12个极点每模态组，拟合范围排除极低频样本

3. Step 3 - 误差计算：将步骤2得到的拟合函数H_high在LF段（s_low）处求值，计算与解析解H_low的偏差ΔH_low = H_low - H_high(s_low)

4. Step 4 - 低频校正拟合：对误差函数ΔH_low在LF段进行独立的有理函数逼近，使用8个极点，采用系统中最小的传播时延τ1（89.9 µs）作为延迟项，因低频时延差异可忽略

5. Step 5 - 模型合成：将高频拟合结果与低频校正项相加，得到最终传播函数H ≈ H_high + ΔH_low，用于时域仿真


### 关键参数

- **HF_fitting_range**: 1 Hz 至 1 MHz（或100 kHz）

- **LF_correction_range**: 0.001 Hz 至 1 Hz

- **poles_per_group_HF**: 12 poles per modal group

- **poles_LF_correction**: 8 poles

- **simulation_time_step**: 10 µs

- **minimum_propagation_delay**: 89.9 µs

- **frequency_boundary**: 1 Hz（高低频分界点）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 两端HVDC输电系统阶跃响应（27km架空线+44km电缆+97km架空线） | 施加单位阶跃电压于送端，受端经1Ω电阻接地。FDM/DC方法在不同最高拟合频率（10^5 Hz和10^6 Hz）下均获得一致的稳态值：V2=0.8659 p.u.（中间点电压），I4=0.3084 p.u.（受端电流），与精确解完全吻合。仿真时间步长10 µs，无数值振荡。 | 相比传统ULM：当fmin=0.1Hz时，ULM的V2误差达10.1%（0.7783 vs 0.8659），I4误差达27.6%（0.2233 vs 0.3084）；即使fmin降至0.001Hz，ULM仍出现时域数值振荡且稳态值不准确（V2=0.8691，I4=0.3242，偏差1.8%） |

| 125km混合AC/DC线路配置（数值稳定性测试） | 用于验证FDM/DC在避免大留极比导致的数值不稳定性方面的性能，通过分区拟合消除了传统ULM在时域积分中产生的放大误差和振荡现象。 | 传统ULM因宽频带拟合产生的大留极比（large residue/pole ratios）会导致时域积分数值不稳定，而FDM/DC通过限制HF段拟合范围（>1Hz）避免了该问题 |



## 量化发现

- FDM/DC在Fmax=10^5 Hz和Fmax=10^6 Hz两种设置下，稳态电压V2均为0.8659 p.u.，电流I4均为0.3084 p.u.，与理论精确解一致，误差<0.1%
- 传统ULM在fmin=0.1 Hz时，稳态电压V2=0.7783 p.u.（偏差10.1%），电流I4=0.2233 p.u.（偏差27.6%）
- 传统ULM在fmin=0.001 Hz时，稳态电流I4=0.3242 p.u.，仍存在5.1%偏差，且时域波形出现持续振荡
- FDM/DC方法使用10 µs仿真步长，最小传播延迟为89.9 µs
- 高频段拟合使用12极点/模态组，低频校正使用8极点，有效避免留极比>10^3的刚性条件
- 低频校正频段限定在0.001-1 Hz，确保直流（0 Hz）附近特性精确捕获


## 关键公式

### 高频传播函数拟合

$$$$H_{high} \cong \sum_{i=1}^{N_{gr}}\left(\sum_{j=1}^{M_i}\frac{R_{i,j}}{s_{high}-p_{i,j}}e^{-s\tau_i}\right)$$$$

*第一阶段对1 Hz至1 MHz频段进行标准ULM或FDCM拟合，使用模态分组技术*

### 低频误差函数定义

$$$$\Delta H_{low} = H_{low} - H_{high}(s_{low})$$$$

*计算被排除的极低频样本（0.001-1 Hz）与高频模型外推值之间的偏差*

### 低频校正项逼近

$$$$\Delta H_{low} \cong \sum_{j=1}^{M_{low}}\frac{R_{low,j}}{s_{low}-p_{low,j}}e^{-s\tau_1}$$$$

*第二阶段对误差函数进行低阶有理逼近（8极点），使用最小传播时延τ1，最终与高频部分相加构成完整模型*



## 验证详情

- **验证方式**: 数值仿真对比分析（与精确解及传统ULM对比）
- **测试系统**: 两端HVDC测试系统（含27km架空线、44km电缆、97km架空线串联）及125km混合AC/DC线路
- **仿真工具**: 基于EMTDC/PSCAD或类似电磁暂态仿真平台（文中提及使用Method of Characteristics精确解作为基准）
- **验证结果**: FDM/DC在不同最高拟合频率（10^5 Hz和10^6 Hz）下均精确复现直流稳态值（误差<0.1%），彻底消除了传统ULM在低频拟合时的数值振荡和稳态偏差（ULM误差可达27.6%），同时避免了因大留极比导致的时域积分数值不稳定问题
