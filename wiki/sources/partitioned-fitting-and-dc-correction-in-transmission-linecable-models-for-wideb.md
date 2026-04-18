---
title: "Partitioned fitting and DC correction in transmission line/cable models for wideband EMT studies"
type: source
authors: ['Miguel Cervantes']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106809. doi:10.1016/j.epsr.2020.106809"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2020.106809.pdf.pdf"]
---

# Partitioned fitting and DC correction in transmission line/cable models for wideband EMT studies

**作者**: Miguel Cervantes
**年份**: 2020
**来源**: `31/j.epsr.2020.106809.pdf.pdf`

## 摘要

Partitioned ﬁtting and DC correction in transmission line/cable models for Miguel Cervantesa,⁎, Ilhan Kocara, Jean Mahseredjiana, Abner Ramirezb b CINVESTAV Campus Guadalajara, Guadalajara, Mexico This paper extends the applications of and provides further insights about partitioned ﬁtting procedure. At the ﬁrst stage of this procedure, the ﬁtting is performed at a high frequency band by excluding frequency samples close to DC. The second stage ﬁnds a correction term for those excluded samples.

## 核心贡献


- 提出分频段拟合与直流校正的两阶段方法，显著提升宽频带线路模型低频精度
- 消除传播函数拟合中的大留数极点比问题，有效解决时域仿真数值不稳定难题
- 给出完整的时域状态空间实现细节，并验证了不同积分与插值方案下的稳定性


## 使用的方法


- [[分频段拟合|分频段拟合]]
- [[直流校正|直流校正]]
- [[有理函数逼近|有理函数逼近]]
- [[模态分解|模态分解]]
- [[状态空间实现|状态空间实现]]
- [[时域卷积|时域卷积]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[通用线路模型|通用线路模型]]
- [[频率相关电缆模型|频率相关电缆模型]]
- [[高压直流输电线路|高压直流输电线路]]


## 相关主题


- [[宽频电磁暂态仿真|宽频电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[数值稳定性|数值稳定性]]
- [[高压直流输电|高压直流输电]]
- [[时域实现|时域实现]]


## 主要发现


- 两阶段拟合方法在保证高频精度的同时，实现了准确的直流稳态电压电流响应
- 有效避免了大留数极点比问题，相比传统通用线路模型显著提升了时域仿真稳定性
- 在不同积分与插值方案下均保持良好稳定性，验证了该模型在宽频暂态研究中的可靠性



## 方法细节

### 方法概述

本文提出FDM/DC（Frequency Dependent Model with DC correction）分频段拟合方法，专门针对宽频EMT仿真中输电线路和电缆模型在直流附近频率的精度问题。该方法通过将频率范围划分为高频段（HF）和低频段（LF），首先在高频段（排除接近DC的样本）进行标准ULM或FDCM拟合以获得主要动态特性，然后针对被排除的低频段计算拟合误差，并通过附加的低阶有理函数校正项补偿直流附近的拟合偏差。这种分区策略避免了传统方法中为捕捉DC响应而产生的大留数/极点比问题，显著提高了时域数值稳定性，同时保证了从直流到高频的宽频带建模精度。

### 数学公式


**公式1**: $$$H = e^{-\Gamma L}$$$

*传播函数定义，其中Γ为传播常数矩阵，L为线路长度*


**公式2**: $$$Y_c = \Gamma Z^{-1}$$$

*特征导纳定义，Z为单位长度串联阻抗矩阵*


**公式3**: $$$I_k = Y_c V_k - H(I_m + Y_c V_m) = I_{shk} - I_{ki}$$$

*线路k端电流方程，描述多端电压电流关系*


**公式4**: $$$H \cong \sum_{i=1}^{N_{gr}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}}{s - p_{i,m}} \right) e^{-s\tau_i}$$$

*ULM中有理函数逼近形式，Ngr为模态组数，Mi为逼近阶数，τi为模态时延*


**公式5**: $$$Y_c \cong G_0 + \sum_{i=1}^{N_y} \frac{G_i}{s - q_i}$$$

*特征导纳在相域的有理逼近，Ny为逼近阶数，qi为拟合极点，Gi为留数矩阵*


**公式6**: $$$\tilde{H}_{HF} \cong \sum_{i=1}^{N_{gr}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}}{s_{HF} - p_{i,m}^{HF}} \right) e^{-s_{HF}\tau_i}$$$

*第一阶段高频段拟合结果，sHF = jωHF为高频段复频率变量*


**公式7**: $$$\Delta H_{LF} = H_{LF} - \tilde{H}_{HF}(s_{LF})$$$

*低频段误差计算，HLF为实际传播函数在低频段的值，H̃HF(sLF)为高频模型在低频处的计算值*


**公式8**: $$$\tilde{H}_{LF} \cong \sum_{k=1}^{N_{dc}} \frac{R_k^{dc}}{s - p_k^{dc}}$$$

*第二阶段直流校正项，Ndc为低阶校正函数阶数（通常很小）*


**公式9**: $$$H_{final} = \tilde{H}_{HF} + \tilde{H}_{LF}$$$

*最终合成传播函数，结合高频主模型和低频校正项*


### 算法步骤

1. 频率范围划分：将目标频带划分为低频段（LF，典型范围0.001 Hz - 1 Hz）和高频段（HF，典型范围1 Hz - 1 MHz或更高，可扩展至线路/电缆常数程序支持的最高频率）

2. 高频段拟合：使用标准ULM或FDCM方法对HF段进行拟合，完全排除LF段（接近DC）的频率样本，获得高频传播函数H̃HF（包含极点p_i,m^HF、留数R_i,m和时延τi）

3. 低频误差提取：在LF频率样本点sLF = jωLF处，计算高频模型的响应值H̃HF(sLF)，与实际传播函数值HLF比较，得到误差函数ΔHLF = HLF - H̃HF(sLF)

4. 直流校正拟合：对误差函数ΔHLF进行低阶有理函数拟合（通常阶数Ndc远小于主模型阶数），获得校正函数H̃LF的极点和留数，确保在DC处的精确匹配

5. 模型合成：将高频模型与低频校正项相加，得到最终宽频传播函数H = H̃HF + H̃LF，实现从直流到高频的精确建模

6. 特征导纳拟合：独立地对Yc在相域进行有理函数拟合（公式6），获得G0、Gi和qi参数

7. 时域实现：基于状态空间实现，采用离散卷积计算历史电流源，支持不同积分方法（如梯形法、后向欧拉）和插值方案（双段插值）


### 关键参数

- **低频段范围**: 0.001 Hz - 1 Hz（典型值，可调）

- **高频段范围**: 1 Hz - 1 MHz（可扩展至更高频率）

- **Ngr**: 模态传播组数（modal propagation groups）

- **Mi**: 第i个模态组的逼近阶数

- **τi**: 第i个模态组的传播时延（与模态速度相关）

- **Ndc**: 直流校正项阶数（低阶，通常1-3阶）

- **Ny**: 特征导纳Yc的逼近阶数

- **Δt**: 时域仿真积分步长



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| HVDC输电线路直流稳态验证 | 在HVDC输电系统测试中，FDM/DC模型能够准确复现直流稳态电压和电流，而传统ULM方法由于低频拟合不良导致直流稳态解错误 | 消除了传统ULM中因强制拟合DC点而产生的大留数/极点比（large residue/pole ratios）问题，数值稳定性显著提高 |

| 宽频暂态响应测试 | 覆盖从直流到高频（1MHz）的宽频带暂态仿真，验证了模型在不同频率下的精度 | 在保证高频精度（与ULM/FDCM相当）的同时，实现了准确的低频/直流响应 |

| 不同数值积分与插值方案稳定性测试 | 应用不同的积分方法（梯形积分、后向欧拉等）和插值方案（包括双段插值two-segment interpolation）进行时域仿真 | FDM/DC在各种积分和插值方案下均保持良好的数值稳定性，而传统ULM在大留数/极点比情况下容易出现数值不稳定 |



## 量化发现

- 低频段频率范围：0.001 Hz - 1 Hz（第一阶段排除的频段）
- 高频段频率范围：1 Hz - 1 MHz（第一阶段拟合频段，可扩展）
- 直流校正项采用低阶有理函数（low-order fitting），通常阶数远小于主模型阶数
- 消除了大留数/极点比（large residue/pole ratios）导致的数值不稳定问题
- 实现了准确的直流（DC）稳态电压和电流响应，解决了传统方法中DC fitting不良的问题
- 模型适用于任意暂态研究（any transient study），频率范围可扩展至线路/电缆常数程序支持的最高频率


## 关键公式

### 低频误差计算方程

$$$\Delta H_{LF} = H_{LF} - \tilde{H}_{HF}(s_{LF})$$$

*在分阶段拟合的第二阶段，计算高频模型在低频段的拟合误差，用于确定所需的直流校正量*

### 传播函数有理逼近

$$$H \cong \sum_{i=1}^{N_{gr}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}}{s - p_{i,m}} \right) e^{-s\tau_i}$$$

*ULM/FDCM中传播函数的标准状态空间实现形式，是高频段拟合的基础*

### 线路端口特性方程

$$$I_k = Y_c V_k - H(I_m + Y_c V_m)$$$

*描述线路两端电压电流关系的基本方程，是EMT仿真中实现诺顿等效的基础*



## 验证详情

- **验证方式**: 时域仿真验证，通过对比不同积分和插值方案下的数值稳定性，以及直流稳态和宽频暂态响应的精度分析
- **测试系统**: HVDC（高压直流）输电线路和电缆系统，包括多端直流输电配置
- **仿真工具**: 基于EMT-type程序实现（参考ULM在PSCAD/EMTDC等工具中的实现细节），使用状态空间实现和离散卷积计算
- **验证结果**: FDM/DC方法在保持宽频建模能力的同时，成功消除了传统ULM中的大留数/极点比问题，在各种数值积分和插值方案下均表现出优异的数值稳定性，并实现了准确的直流稳态响应。具体数值指标（如误差百分比、计算时间等）在提供的文本片段中未明确给出。
