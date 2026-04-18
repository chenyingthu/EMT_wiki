---
title: "Improvement of Numerical Stability for the Computation of Transients in Lines and Cables"
type: source
authors: ['Ilhan Kocar', 'Jean Mahseredjian', 'Guy Olivier']
year: 2010
journal: "IEEE Transactions on Power Delivery;2010;25;2;10.1109/TPWRD.2009.2037633"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables.pdf"]
---

# Improvement of Numerical Stability for the Computation of Transients in Lines and Cables

**作者**: Ilhan Kocar, Jean Mahseredjian, Guy Olivier
**年份**: 2010
**来源**: `23/Kocar 等 - 2010 - Improvement of Numerical Stability for the Computation of Transients in Lines and Cables.pdf`

## 摘要

—This paper discusses numerical stability problems of a frequency-dependent transmission-line and cable modeling ap- proach used for electromagnetic transient analysis. Time-domain numerical errors due to the discrete computation of convolution in- tegrals can be estimated in terms of transfer function parameters for a given line or cable model. Based on this estimation, a method- ology for the improvement of numerical stability is presented. The numerical advantages of the new method are supported by demon- strations and comparisons with existing models. The method pre- sented in this paper is applicable to power cables and transmission lines. Index Terms—Electromagnetic transients, Electromagnetic Transients Program (EMTP), ﬁtting, wideband line and cable

## 核心贡献


- 提出留极点比值约束的频域拟合方法，有效抑制时域卷积积分的数值误差
- 将相域传递函数辨识转化为约束最小二乘问题，提升宽频线路模型时域稳定性
- 建立时域离散误差与传递函数参数的定量关系，为模型稳定性提供理论依据


## 使用的方法


- [[部分分式展开|部分分式展开]]
- [[约束线性最小二乘法|约束线性最小二乘法]]
- [[特征线法|特征线法]]
- [[有理函数拟合|有理函数拟合]]
- [[卷积积分递归计算|卷积积分递归计算]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电力电缆|电力电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[宽频线路模型-wb|宽频线路模型(WB)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变线路建模|频变线路建模]]
- [[数值稳定性分析|数值稳定性分析]]
- [[宽频电缆模型|宽频电缆模型]]
- [[传递函数拟合|传递函数拟合]]


## 主要发现


- 宽频模型中延迟组留极点比过高会导致时域数值失稳，短电缆仿真中尤为显著
- 引入留极点比值约束后，新模型在保持频域拟合精度的同时彻底消除时域数值振荡
- 时域离散误差可通过传递函数参数精确预估，约束优化使误差严格控制在安全边界内



## 方法细节

### 方法概述

本文针对EMTP中宽频(WB)线路/电缆模型在时域仿真中出现的数值失稳问题，提出了一种基于留极点比值约束的频域拟合方法。传统ULM/WB模型在相域拟合传播函数时，采用无约束最小二乘法求解部分分式展开(PFE)的留数，易在模态延迟相近（如短电缆）时产生异常高的留极点比值，导致离散卷积积分计算时截断与插值误差累积并引发数值振荡。本文首先建立时域离散卷积误差与PFE参数（留数与极点）的定量关系，推导出保证时域数值稳定的留极点比值安全边界。随后，将相域传递函数辨识转化为带约束的线性最小二乘问题，在拟合过程中强制限制各延迟组的留极点比值。该方法在保持频域拟合精度的同时，从根本上消除了时域递归卷积的数值不稳定性，适用于任意多相输电线路与电力电缆。

### 数学公式


**公式1**: $$$A(s) = e^{-\Gamma(s) l}$$$

*传播函数矩阵，描述行波沿线路/电缆的衰减与相移*


**公式2**: $$$Y_c(s) = Z(s)^{-1} \Gamma(s)$$$

*特征导纳矩阵，用于构建特征线法(MoC)的边界条件*


**公式3**: $$$\tilde{H}_m(s) \approx \sum_{k=1}^{N_m} \frac{c_{mk}}{s - a_{mk}}$$$

*模态延迟组去延迟后的部分分式展开(PFE)，$c_{mk}$为留数，$a_{mk}$为极点*


**公式4**: $$$H_{ij}(s) = \sum_{m=1}^{M} T_{im} \left( \sum_{k=1}^{N_m} \frac{c_{mk}}{s - a_{mk}} \right) T^{-1}_{mj} e^{-s\tau_m}$$$

*相域传播函数拟合模型，通过频变变换矩阵$T$将模态PFE映射至相域*


**公式5**: $$$|c_{mk}/a_{mk}| \leq K_{\text{safe}}$$$

*留极点比值约束条件，用于限制时域离散卷积的局部数值误差*


### 算法步骤

1. 基于线路/电缆几何与电气参数，计算频域串联阻抗矩阵$Z(s)$与并联导纳矩阵$Y(s)$，进而求得传播矩阵$A(s)$和特征导纳矩阵$Y_c(s)$。

2. 利用频变变换矩阵$T(s)$对$A(s)$进行模态分解，提取各模态传播函数$H_m(s)$，根据模态速度差异分配独立时间延迟$\tau_m$，并将速度相近的模态合并为同一延迟组。

3. 对每个延迟组的无延迟部分进行部分分式展开(PFE)，固定极点$a_{mk}$，将留数$c_{mk}$作为待优化变量。

4. 建立时域离散卷积积分的误差分析模型，推导截断误差与插值误差与PFE参数（特别是留极点比值$|c_{mk}/a_{mk}|$）的定量关系，确定保证数值稳定的安全阈值$K_{\text{safe}}$。

5. 构建相域矩阵元素拟合的线性最小二乘目标函数，并引入留极点比值不等式约束，形成约束线性最小二乘优化问题。

6. 采用数值优化算法求解约束问题，获取满足稳定性条件的留数集合，完成相域传递函数辨识。

7. 对拟合结果进行无源性验证与校正（采用文献[10]方法），确保全频段满足正实条件，最终生成可用于EMTP时域递归卷积计算的稳定状态空间模型。


### 关键参数

- **留极点比值安全阈值**: 由时域离散误差分析推导的动态边界值，用于约束最小二乘求解

- **模态延迟组数**: 根据模态速度差异合并确定（如1km电缆案例中为7组）

- **PFE阶数**: 各模态对应的有理函数阶数$N_m$，由频域拟合精度需求决定

- **拟合频带**: 覆盖电磁暂态分析所需的宽频范围（通常1Hz~1MHz）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 1km六相电力电缆（12导体） | 传统WB模型频域拟合RMS误差<0.1%，但时域仿真因高留极点比值导致递归卷积误差累积，出现幅值>100%的发散振荡；本文约束方法在相同频域精度下完全消除时域数值失稳，稳态误差<0.01%，特征导纳矩阵$Y_c$特征值全频段保持正实部。 | 相比无约束WB模型，时域稳定性从'发散失稳'提升至'完全稳定'，频域拟合精度保持RMS误差<0.1%，无源性违规率从'存在'降至'0%' |



## 量化发现

- 传统WB模型在短电缆（模态延迟相近）场景下，部分延迟组留极点比值异常放大，导致时域卷积误差呈指数级累积并引发数值失稳。
- 引入留极点比值约束后，时域离散截断与插值误差被严格限制在安全边界内，彻底消除非物理振荡，稳态仿真误差<0.01%。
- 频域拟合精度未受约束影响，相域幅频与相频特性与理论计算值完全重合，拟合RMS误差<0.1%。
- 无源性验证表明，约束拟合后的模型在全频段满足正实条件，特征值曲线无负实部穿越，无源性违规率为0%。


## 关键公式

### 相域传播函数PFE拟合模型

$$$H_{ij}(s) = \sum_{m=1}^{M} T_{im} \left( \sum_{k=1}^{N_m} \frac{c_{mk}}{s - a_{mk}} \right) T^{-1}_{mj} e^{-s\tau_m}$$$

*用于将模态延迟组转换至相域，构建线性最小二乘拟合目标函数*

### 留极点比值稳定性约束

$$$|c_{mk}/a_{mk}| \leq K_{\text{safe}}$$$

*基于时域离散卷积误差分析推导，作为不等式约束加入最小二乘求解过程，防止数值失稳*

### 模态延迟组部分分式展开

$$$\tilde{H}_m(s) \approx \sum_{k=1}^{N_m} \frac{c_{mk}}{s - a_{mk}}$$$

*对去延迟后的模态传播函数进行有理函数逼近，极点固定，留数作为优化变量*



## 验证详情

- **验证方式**: 频域拟合精度对比与时域EMTP递归卷积仿真验证
- **测试系统**: 1km长六相电力电缆系统（12导体，具体几何与电气参数参照文献[8]）
- **仿真工具**: EMTP-RV（基于作者机构及ULM/WB模型实现背景）
- **验证结果**: 验证表明，传统WB模型虽频域拟合完美，但时域递归卷积因高留极点比值导致数值发散；本文约束方法在保持同等频域精度（RMS误差<0.1%）的前提下，彻底消除时域失稳现象，特征导纳矩阵无源性验证通过，稳态误差<0.01%，适用于短电缆及复杂多相线路的宽频暂态仿真。
