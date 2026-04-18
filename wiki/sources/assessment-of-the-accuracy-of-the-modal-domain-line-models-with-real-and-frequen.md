---
title: "Assessment of the accuracy of the modal-domain line models with real and frequency-independent transformation matrix for electromagnetic transient simulation in lines with underbuilt cables"
type: source
authors: ['Lucas', 'A.', 'Rezende']
year: 2024
journal: "Electric Power Systems Research, 234 (2024) 110500. doi:10.1016/j.epsr.2024.110500"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Rezende 等 - 2024 - Assessment of the accuracy of the modal-domain line models with real and frequency-independent trans.pdf"]
---

# Assessment of the accuracy of the modal-domain line models with real and frequency-independent transformation matrix for electromagnetic transient simulation in lines with underbuilt cables

**作者**: Lucas, A., Rezende
**年份**: 2024
**来源**: `09/Rezende 等 - 2024 - Assessment of the accuracy of the modal-domain line models with real and frequency-independent trans.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Assessment of the accuracy of the modal-domain line models with real and frequency-independent transformation matrix for electromagnetic transient Lucas A. Rezende a, Naiara Duarte b, Rafael Alipio b,c,*, Alberto De Conti d a Graduate Program of Electrical Engineering (PPGEL), Federal Center of Technological Education of Minas Gerais (CEFET-MG), Belo Horizonte,

## 核心贡献


- 评估含地线架空线采用实数频不变变换矩阵模域模型的电磁暂态仿真精度
- 量化地线数量与土壤电阻率对模域模型电压峰值误差的影响规律
- 验证相域模型在不对称线路暂态过电压计算中的必要性与优越性


## 使用的方法


- [[模域模型|模域模型]]
- [[相域模型|相域模型]]
- [[通用线路模型|通用线路模型]]
- [[频域分析|频域分析]]
- [[时域仿真|时域仿真]]
- [[频率相关土壤参数建模|频率相关土壤参数建模]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[下挂地线|下挂地线]]
- [[避雷线|避雷线]]
- [[多导体传输线|多导体传输线]]
- [[fdline模型|fdLine模型]]
- [[通用线路模型|通用线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[雷电过电压评估|雷电过电压评估]]
- [[土壤电阻率影响|土壤电阻率影响]]
- [[线路几何不对称性|线路几何不对称性]]
- [[模域与相域模型对比|模域与相域模型对比]]


## 主要发现


- 地线数量增加与土壤电阻率升高显著加剧模域模型电压仿真误差
- 模域模型计算的暂态电压峰值误差最高可达约百分之二十四
- 含地线线路暂态仿真推荐采用通用线路模型等相域方法以保证精度



## 方法细节

### 方法概述

本文采用频域解析求解与数值拉普拉斯反变换相结合的方法，系统评估了采用实数且频率无关变换矩阵的模域线路模型（fdLine类）在含下挂地线架空线电磁暂态仿真中的精度。研究以精确的相域模型为基准，首先基于多导体传输线（MTL）理论构建单位长度阻抗与导纳矩阵，其中大地返回阻抗采用Sunde积分公式计算，并引入Alipio-Visacro模型表征土壤电导率与介电常数的频率依赖性。在相域中，直接利用频域电报方程的精确解构建2n×2n节点导纳矩阵进行求解；在模域中，则在参考频率（10 kHz）下计算特征值与特征向量，提取实数且恒定的模变换矩阵以实现系统解耦。随后，在1 kHz至1 MHz频段内计算两端电压频响，并通过相对误差与归一化均方根误差（NRMSE）量化频域偏差。最后，利用数值拉普拉斯变换将频域结果转换为时域阶跃响应，对比两种模型在波前峰值与波形上的差异，从而揭示几何不对称性与高土壤电阻率对模域模型精度的影响机制。

### 数学公式


**公式1**: $$$\frac{d^2}{dz^2}V(z) = ZYV(z)$$$

*多导体传输线电压频域二阶微分方程，描述沿线电压分布与单位长度阻抗导纳矩阵的关系*


**公式2**: $$$Z = Z_i + j\omega L + Z_g$$$

*单位长度串联阻抗矩阵，包含导体内部阻抗、外部电感及大地返回阻抗*


**公式3**: $$$Z_{gii} = \frac{j\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-2h_i\lambda}}{\sqrt{\lambda^2+\gamma_g^2}+\lambda} d\lambda$$$

*Sunde大地返回自阻抗积分公式，用于精确计算高频下的大地回流效应*


**公式4**: $$$\sigma_g(f) = \sigma_0 \left\{1 + 4.7 \times 10^{-6} \times \sigma_0^{-0.73} \times f^{0.54}\right\}$$$

*Alipio-Visacro土壤电导率频变模型，反映高频下土壤参数的动态变化*


**公式5**: $$$NRMSE = \frac{100}{\max|V_{ph}(\omega)|} \sqrt{\frac{1}{N_s} \sum_{k=1}^{N_s} [V_{mod}(\omega_k) - V_{ph}(\omega_k)]^2}$$$

*归一化均方根误差公式，用于在特定频段内量化模域模型相对于相域基准的整体偏差*


### 算法步骤

1. 定义线路几何拓扑（500kV杆塔、相导线、避雷线及0/1/2根下挂地线坐标）与土壤直流电阻率（200~10000 Ωm）参数。

2. 基于Bessel函数计算导体内部阻抗，利用几何坐标计算外部电感与电容矩阵，并采用Sunde积分公式计算大地返回阻抗矩阵。

3. 若启用频变土壤模型，则根据Alipio-Visacro公式在目标频率点更新土壤电导率与介电常数，重新计算导纳矩阵。

4. 相域求解：直接组合阻抗Z与导纳Y矩阵，代入频域精确解公式构建2n×2n节点导纳矩阵Yn，结合终端边界条件（10Ω接地、430Ω匹配负载）求解相电压频响。

5. 模域求解：在10 kHz参考频率下对ZY矩阵进行特征值分解，提取实数且频率无关的模变换矩阵Tv与Ti，将耦合方程解耦为独立模态方程，分别求解后反变换回相域。

6. 在1 kHz至1 MHz范围内以离散频率点扫描，计算两种模型的电压幅值，并逐点计算相对误差E(%)及分段NRMSE（1k-1MHz与100k-1MHz）。

7. 应用数值拉普拉斯反变换算法，将频域电压传递函数转换为时域阶跃响应波形（1kV阶跃激励）。

8. 提取时域波前峰值电压，计算模域与相域峰值的相对偏差，分析地线数量与土壤电阻率对误差的放大效应。


### 关键参数

- **线路长度**: 550 m

- **档距与弧垂**: 档距550 m，相导线弧垂24.34 m，避雷线弧垂20.95 m

- **相导线参数**: 等效半径3.75 cm，直流电阻0.0711 Ω/km

- **避雷线参数**: 3/8'' EHS，半径0.457 cm，直流电阻3.81 Ω/km

- **终端接地电阻**: 避雷线/下挂地线10 Ω，相导线匹配负载430 Ω

- **土壤电阻率测试值**: 200, 1000, 5000, 10000 Ωm

- **频域扫描范围**: 1 kHz ~ 1 MHz

- **模域参考频率**: 10 kHz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 无下挂地线配置（频域100k-1MHz，FD-S，10000Ωm） | 模域模型与相域基准的NRMSE为2.03%，频域电压幅值偏差较小，谐振峰处略有差异。 | 作为基准对照组，误差控制在5%以内，满足常规工程精度要求。 |

| 单根下挂地线配置（时域阶跃响应，FD-S，10000Ωm） | 模域模型计算的相C末端感应电压波前峰值误差达20.2%，波形在初始上升沿出现明显畸变。 | 相比无下挂地线配置，峰值误差放大4倍以上，表明单根地线引入的几何不对称性显著降低模域模型精度。 |

| 双根下挂地线配置（时域阶跃响应，FD-S，10000Ωm） | 模域模型峰值误差进一步攀升至23.8%，频域100k-1MHz NRMSE达7.00%，高频分量衰减与相位偏移严重。 | 误差较单根地线配置提升约3.6%，验证了下挂地线数量与仿真误差呈正相关，模域模型在此场景下已不适用。 |



## 量化发现

- 模域模型在含下挂地线线路中的频域NRMSE（100k-1MHz）随土壤电阻率升高而增大，在10000Ωm时，0/1/2根地线配置的NRMSE分别为2.03%、5.35%和7.00%。
- 时域阶跃响应峰值电压最大相对误差可达23.8%（双下挂地线，10000Ωm土壤），远超常规雷电过电压评估允许的5%误差阈值。
- 误差主要集中在100 kHz至1 MHz频段，该频段恰好对应雷击过电压波前的高频能量集中区，直接影响绝缘配合评估。
- 考虑土壤参数频率依赖性（FD-S）时，模域模型的NRMSE较恒定土壤参数（C-S）平均增加约0.2%~0.4%，高频段误差放大效应更显著。
- 无下挂地线对称线路的峰值误差始终低于5%，证实fdLine模型在常规对称线路中仍具备工程适用性。


## 关键公式

### 相域节点导纳矩阵

$$$Y_n = \begin{bmatrix} Y_c(1_n+A^2)(1_n-A^2)^{-1} & -2Y_c A(1_n-A^2)^{-1} \\ -2Y_c A(1_n-A^2)^{-1} & Y_c(1_n+A^2)(1_n-A^2)^{-1} \end{bmatrix}$$$

*用于相域模型精确求解，直接整合线路传播矩阵A与特征导纳Yc，无需模态解耦，适用于任意不对称拓扑。*

### 模态解耦特征方程

$$$T_V^{-1} ZY T_V = \lambda$$$

*模域模型核心，通过变换矩阵Tv将耦合的ZY矩阵对角化为特征值矩阵λ，实现多导体系统解耦为独立单相线路。*

### 频域相对误差公式

$$$E(\%) = \frac{|V_{mod}(\omega) - V_{ph}(\omega)|}{V_{ph}(\omega)} \times 100$$$

*逐频点对比模域与相域电压幅值偏差，用于定位误差集中的谐振频率与高频段。*



## 验证详情

- **验证方式**: 频域解析对比与时域数值反变换验证（相域模型作为高精度基准）
- **测试系统**: 巴西典型500kV拉线塔架空输电线路（550m档距），配置0、1、2根下挂地线，土壤电阻率覆盖200~10000 Ωm
- **仿真工具**: 基于频域电报方程精确解的自定义计算程序与数值拉普拉斯变换算法（等效于PSCAD/EMTDC底层频域求解器逻辑）
- **验证结果**: 验证表明，传统模域模型（fdLine）在含下挂地线的不对称线路中会产生不可忽略的暂态电压误差，误差随地线数量与土壤电阻率增加而显著放大，峰值偏差最高达23.8%。研究强烈建议在此类场景下采用相域模型（如通用线路模型ULM）以确保雷电过电压评估的准确性。
