---
title: "Algorithms for fast calculation of energization overvoltage of hybrid overhead line-cable transmission lines based on full frequency-dependent parameters"
type: source
authors: ['Borui Gu']
year: 2023
journal: "Electric Power Systems Research, 225 (2023) 109875. doi:10.1016/j.epsr.2023.109875"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans-1.pdf"]
---

# Algorithms for fast calculation of energization overvoltage of hybrid overhead line-cable transmission lines based on full frequency-dependent parameters

**作者**: Borui Gu
**年份**: 2023
**来源**: `06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans-1.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Algorithms for fast calculation of energization overvoltage of hybrid overhead line-cable transmission lines based on full Borui Gu a, Han Li a, Shurong Li a, Xiaoguang Zhu a, Xuefeng Zhao b, Junbo Deng a,*, a State Key Laboratory of Electrical Insulation and Power Equipment, Xi’an Jiaotong University, Xi’an, 710049, China

## 核心贡献


- 提出基于全频域参数的混合线路过电压快速算法，突破传统EMT仿真步长限制
- 结合相模变换与改进数值拉普拉斯逆变换，实现复频域到时域的高效转换
- 构建基于拓扑的频变边界条件模型，简化复杂混合输电系统建模流程


## 使用的方法


- [[相模变换|相模变换]]
- [[数值拉普拉斯逆变换-nilt|数值拉普拉斯逆变换(NILT)]]
- [[全频域参数计算|全频域参数计算]]
- [[复频域边界条件推导|复频域边界条件推导]]
- [[电报方程求解|电报方程求解]]


## 涉及的模型


- [[混合架空线-电缆线路|混合架空线-电缆线路]]
- [[频变相模型-fdpm|频变相模型(FDPM)]]
- [[j-marti模型|J.Marti模型]]
- [[transmission-line-model|Bergeron线路模型]]
- [[π型集中参数模型|π型集中参数模型]]


## 相关主题


- [[合闸过电压计算|合闸过电压计算]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[输电线路模态分析|输电线路模态分析]]
- [[复频域时域转换|复频域时域转换]]


## 主要发现


- 算法计算结果与PSCAD频变相模型对比，最大相对误差低于0.261%
- 计算耗时仅为传统频变相模型的32.6%至58.6%，显著提升仿真效率
- 在330kV混合输电系统验证中，算法兼顾高精度与快速性，满足工程需求



## 方法细节

### 方法概述

本文提出一种基于全频域参数的混合架空线-电缆线路合闸过电压快速计算算法。首先在全频域内精确计算线路的频变串联阻抗与并联导纳矩阵，利用相模变换解耦多导体电报方程。随后根据“架空线-电缆”或“电缆-架空线”拓扑推导复频域边界条件，构建线性方程组求解模态电压表达式的待定系数。最后通过模相变换还原至相域，并采用改进的数值拉普拉斯逆变换（NILT）将复频域结果转换至时域。该算法将NILT拆分为复频域采样与逆变换两部分，有效避免了传统方法中繁重的符号运算，突破了EMT仿真受限于波传播时间步长的计算瓶颈，实现高精度与高效率的统一。

### 数学公式


**公式1**: $$$\frac{d^2 V_p(x,s)}{dx^2} = Z_p(s)Y_p(s)V_p(x,s)$$$

*复频域多导体电报方程，描述相域电压与频变阻抗、导纳矩阵的关系*


**公式2**: $$$\frac{d^2 V_m(x,s)}{dx^2} = \Lambda(s)V_m(x,s)$$$

*经相模变换解耦后的模态电报方程，$\Lambda(s)$为对角矩阵，实现各模态独立求解*


**公式3**: $$$Z_p = \frac{Z_{p0} + C_r Z_{p0} C_r^{-1} + C_r^{-1} Z_{p0} C_r}{3}$$$

*三相单芯交叉互联电缆的等效串联阻抗矩阵计算公式，$C_r$为换位旋转矩阵*


**公式4**: $$$V_{mc}(x_c,s) = E_{nx_c}(s)F_{1c}(s) + E_{px_c}(s)F_{2c}(s)$$$

*模域电压通解表达式，$E_{n/p}$为传播指数对角阵，$F_{1/2}$为待定系数向量*


**公式5**: $$$\tilde{F}_{i-1}(p_{i-1}) = e^{\frac{c_i N_{si} \Delta t_i}{\tau_i}} \sum_{m=-\infty}^{\infty} \tilde{F}_i(p_i) e^{j 2\pi m N_{si} \Delta t_i / \tau_i}$$$

*改进NILT算法的递推公式，结合FFT/IFFT与q-d算法实现高效数值逆变换*


### 算法步骤

1. 全频域参数计算与相模解耦：在复频域内遍历设定采样点，基于线路几何与电气参数计算架空线及交叉互联电缆的频变串联阻抗矩阵$Z_p(s)$和并联导纳矩阵$Y_p(s)$。利用电压/电流变换矩阵$A$和$B$执行相模变换，将相域耦合参数转换为模域对角参数$\Lambda(s)=Z_m(s)Y_m(s)$，完成电磁解耦。

2. 边界条件推导与复频域系数求解：根据断路器合闸时刻$t_0$和电源初相角$\phi$，利用拉普拉斯变换延迟性质构建电源等效复频域电压$V_{Source}(s)$。结合线路拓扑（送端、接头点、受端）的电压电流连续性条件及接地约束，建立包含22个线性方程的复频域方程组，求解模态电压/电流表达式中的待定系数向量$F_{1}(s)$和$F_{2}(s)$。

3. 模相变换与改进NILT时域转换：将求得的模域系数通过变换矩阵还原至相域，得到沿线任意位置的复频域电压表达式。采用改进的NILT算法，将计算流程拆分为复频域离散采样与数值逆变换两部分，直接对采样结果应用FFT/IFFT与q-d算法进行数值积分，高效输出时域过电压波形，彻底规避传统符号运算导致的计算迟滞。


### 关键参数

- **额定电压**: 345 kV (线电压)

- **电源阻抗**: 5.04 + j5.40 Ω

- **架空线长度**: 45 km

- **电缆长度**: 11.8 km

- **电缆主段数**: 7

- **电缆次段数**: 21

- **采样点数**: 2000 / 5000

- **合闸时刻**: 0.02 s

- **总计算耗时**: 0.08 s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 架空线-电缆拓扑（0°合闸相角） | 受端A相合闸过电压峰值计算结果为306.380 kV，基准FDPM模型结果为306.495 kV，相对误差为0.038%。 | 计算耗时仅为FDPM模型的32.654%，精度高度一致。 |

| 架空线-电缆拓扑（15°合闸相角） | 受端A相过电压峰值为353.552 kV，FDPM结果为353.706 kV，相对误差为0.044%。 | 在不同合闸相角下均保持<0.05%的误差，计算速度提升约3倍。 |

| 电缆-架空线拓扑（全相角范围） | 在0°~90°合闸相角范围内，受端过电压峰值最大相对误差控制在0.072%以内。 | 计算耗时为FDPM模型的58.649%，兼顾复杂拓扑下的高精度与快速性。 |



## 量化发现

- 算法计算结果与PSCAD/EMTDC频变相模型（FDPM）对比，最大相对误差低于0.261%，特定工况下低至0.038%。
- 计算耗时仅为传统FDPM模型的32.654%至58.649%，仿真效率提升约1.7至3.1倍。
- 在330 kV混合输电系统（总长56.8 km）验证中，单次完整过电压波形计算仅需0.08秒。
- 改进NILT算法有效消除了复频域符号运算瓶颈，突破了传统EMT仿真步长必须小于波传播时间（$\Delta t < \tau$）的限制。


## 关键公式

### 解耦模态电报方程

$$$\frac{d^2 V_m(x,s)}{dx^2} = \Lambda(s)V_m(x,s)$$$

*用于将多导体耦合系统转化为独立模态回路，是频域解析求解的基础*

### 模域电压通解

$$$V_{mc}(x_c,s) = E_{nx_c}(s)F_{1c}(s) + E_{px_c}(s)F_{2c}(s)$$$

*结合边界条件求解待定系数$F_{1/2}$，用于构建沿线复频域电压分布*

### 交叉互联电缆等效阻抗公式

$$$Z_p = \frac{Z_{p0} + C_r Z_{p0} C_r^{-1} + C_r^{-1} Z_{p0} C_r}{3}$$$

*处理三相单芯电缆交叉互联接地方式，准确反映护套环流对频变参数的影响*

### 改进NILT递推公式

$$$\tilde{F}_{i-1}(p_{i-1}) = e^{\frac{c_i N_{si} \Delta t_i}{\tau_i}} \sum_{m=-\infty}^{\infty} \tilde{F}_i(p_i) e^{j 2\pi m N_{si} \Delta t_i / \tau_i}$$$

*替代传统解析拉普拉斯逆变换，实现复频域离散采样点到时域波形的高效数值转换*



## 验证详情

- **验证方式**: 对比仿真分析（与商业EMT软件基准模型进行精度与耗时对比）
- **测试系统**: 中国西安330 kV混合架空线-电缆输电系统（45 km 2×JL/GIA-300/40架空线 + 11.8 km ZC-YJLW02-Z-190/330单芯交叉互联电缆）
- **仿真工具**: 自研快速计算算法程序（基于MATLAB/Python实现） vs PSCAD/EMTDC (FDPM频变相模型)
- **验证结果**: 验证了算法在不同合闸相角（0°~90°）和两种拓扑结构下的高精度与快速性。峰值过电压误差均<0.072%，计算效率显著提升（耗时降至32.6%~58.6%），完全满足工程快速校核与绝缘配合设计需求。
