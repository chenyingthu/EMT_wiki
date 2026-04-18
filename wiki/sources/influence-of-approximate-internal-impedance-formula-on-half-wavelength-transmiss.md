---
title: "Influence of approximate internal impedance formula on half-wavelength transmission lines"
type: source
authors: ['J.E.', 'Guevara', 'Asorza']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112229. doi:10.1016/j.epsr.2025.112229"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/24/Rojas Varela 等 - 2025 - Influence of Approximate Internal Impedance Formula on Half-Wavelength Transmission Lines.pdf"]
---

# Influence of approximate internal impedance formula on half-wavelength transmission lines

**作者**: J.E., Guevara, Asorza
**年份**: 2025
**来源**: `24/Rojas Varela 等 - 2025 - Influence of Approximate Internal Impedance Formula on Half-Wavelength Transmission Lines.pdf`

## 摘要

Influence of approximate internal impedance formula on half-wavelength School of Electrical and Computer Engineering, University of Campinas - UNICAMP, Campinas, Brazil This paper evaluates the impact of using approximate versus exact internal impedance formulations in Overhead Transmission Lines (OHTL), focusing on Half-Wavelength Transmission lines (HWTL) and high-surge impedance loading applications, where multiple conductors per phase are employed. Approximate formulations

## 核心贡献


- 对比评估了线路内部阻抗精确与近似公式在稳态及暂态下的计算差异
- 揭示了近似公式对半波长线路波阻抗负载及暂态过电压预测精度的影响
- 量化了近似模型在多分裂导线配置下统计开关操作产生的过电压预测偏差


## 使用的方法


- [[贝塞尔函数精确计算|贝塞尔函数精确计算]]
- [[双曲余切近似公式|双曲余切近似公式]]
- [[carson大地返回阻抗模型|Carson大地返回阻抗模型]]
- [[统计开关操作分析|统计开关操作分析]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[半波长输电线路|半波长输电线路]]
- [[多分裂导线模型|多分裂导线模型]]
- [[高波阻抗负载线路|高波阻抗负载线路]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[波阻抗负载计算|波阻抗负载计算]]
- [[暂态过电压分析|暂态过电压分析]]
- [[长距离输电|长距离输电]]
- [[线路参数精确建模|线路参数精确建模]]


## 主要发现


- 近似公式使波阻抗负载计算偏差随分裂数增加而增大，最高达百分之零点零七
- 暂态统计开关分析表明近似模型预测过电压偏高，且C相偏差最为显著
- 近似内部阻抗模型会引入额外电压降落，显著降低半波长线路稳态电压精度



## 方法细节

### 方法概述

本文采用对比分析方法，系统评估了架空输电线路（OHTL）内部阻抗精确公式（基于修正贝塞尔函数）与近似公式（基于双曲余切函数）在稳态与电磁暂态（EMT）条件下的建模差异。研究聚焦于半波长输电线路（HWTL）及高波阻抗负载（HSIL）应用场景，针对三种不同分裂导线配置（4、6、8分裂）的线路模型，分别计算其串联阻抗与并联导纳矩阵。通过Carson模型处理大地返回阻抗，在60Hz工频下提取正序/零序参数、波阻抗及波阻抗负载（SIL），并基于统计开关操作进行暂态过电压仿真。最终量化近似模型在功率传输能力、焦耳损耗及暂态过电压预测中的累积误差，验证精确建模在超长距离输电分析中的必要性。

### 数学公式


**公式1**: $$$\mathbf{Z} = \mathbf{Z}_{\text{int}} + \mathbf{Z}_{\text{ext}} + \mathbf{Z}_{g}$$$

*总串联阻抗矩阵计算公式，叠加导体内部阻抗、外部空气阻抗及大地返回阻抗*


**公式2**: $$$\mathbf{Y} = j\omega\mathbf{P}^{-1} = \mathbf{Y}_0 + \mathbf{Y}_{g}$$$

*并联导纳矩阵计算公式，包含恒定项与高频相关的大地导纳项*


**公式3**: $$$\mathbf{Z}_{\text{int}(i)} = \frac{p_i \gamma_i}{2\pi r_i} \left[ \frac{I_0(\gamma_i r_i)K_1(\gamma_i q_i) + I_1(\gamma_i q_i)K_0(\gamma_i r_i)}{I_1(\gamma_i r_i)K_1(\gamma_i q_i) - I_1(\gamma_i q_i)K_1(\gamma_i r_i)} \right]$$$

*基于修正贝塞尔函数的精确内部阻抗公式，完整表征集肤效应与电磁场分布*


**公式4**: $$$\mathbf{Z}_{\text{int}(i)} = \frac{p_i \gamma_i}{2\pi r_i} \coth\left(0.733\gamma_i r_i + \frac{0.3179\rho_i}{\pi r_i^2}\right)$$$

*实心导体近似内部阻抗公式，引入常数k=0.733优化低频计算效率*


### 算法步骤

1. 定义三种OHTL拓扑（TL1/TL2/TL3），输入导线几何尺寸、材料电导率、分裂数及杆塔空间坐标；

2. 基于频率扫描，利用修正贝塞尔函数（式3）精确计算各导体内部阻抗矩阵$\mathbf{Z}_{\text{int}}$，完整捕捉频变集肤效应；

3. 采用双曲余切近似公式（式5/6，常数k=0.733）计算近似内部阻抗，模拟PSCAD/EMTDC的LCP模块行为；

4. 结合Carson大地返回模型计算外部阻抗$\mathbf{Z}_{\text{ext}}$与大地阻抗$\mathbf{Z}_{g}$，叠加得到总串联阻抗矩阵$\mathbf{Z}$；

5. 计算并联导纳矩阵$\mathbf{Y}$，构建完整频变多导体传输线模型；

6. 在60Hz工频下提取正序/零序阻抗、波阻抗$Z_c$及波阻抗负载SIL，进行稳态参数对比；

7. 设定线路运行于各自SIL工况，计算不同长度（350km/450km/2600km）下的焦耳损耗差异；

8. 搭建EMT仿真模型，执行统计开关操作（Statistical Switching）以获取暂态过电压概率分布；

9. 对比精确与近似模型在稳态参数、损耗及暂态过电压峰值上的偏差，进行误差量化与工程影响评估。


### 关键参数

- **系统频率**: 60 Hz

- **近似公式常数k**: 0.733

- **TL1配置**: 440 kV / 4分裂 / 350 km

- **TL2配置**: 765 kV / 6分裂 / 450 km

- **TL3配置**: 800 kV / 8分裂 / 2600 km (HWTL)

- **导线内/外半径**: TL1: 4.64/12.57 mm; TL2/TL3: 4.135/16.56 mm

- **20°C直流电阻**: TL1: 0.08989 Ω/km; TL2/TL3: 0.0478 Ω/km



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| TL1稳态参数对比 | 4分裂440kV线路在SIL工况下，近似模型计算的SIL偏差为0.0374%，正序电阻偏高导致理论传输功率略低。 | 与精确模型相比，近似模型引入的稳态误差较小，但在长线路累积效应下仍不可忽略。 |

| TL3(HWTL)稳态参数对比 | 8分裂800kV半波长线路（2600km）SIL偏差达0.0717%，近似模型导致额外电压降落，显著降低稳态电压精度。 | 相比短线路，超长HWTL的阻抗误差被显著放大，近似模型预测的功率传输能力受限。 |

| 统计开关暂态过电压分析 | 三相统计开关操作下，近似模型预测的暂态过电压峰值普遍高于精确模型，其中C相过电压偏差最为显著。 | 近似模型高估了过电压水平，可能导致绝缘配合设计过于保守或保护定值误判。 |



## 量化发现

- 近似公式在中频段（mid-range frequencies）的内部阻抗计算误差约为0.5%
- SIL计算偏差随分裂导线数量增加而单调递增：4分裂为0.0374%，6分裂为0.0579%，8分裂为0.0717%
- 精确模型计算的正序电阻始终低于近似模型，表明实际线路具备更高的有功传输能力与更低的焦耳损耗
- 统计开关暂态仿真中，近似模型预测的过电压峰值系统性偏高，且C相偏差幅度最大
- 对于2600km半波长线路，近似内部阻抗模型引入的额外压降显著影响稳态电压分布精度


## 关键公式

### 精确内部阻抗公式

$$$\mathbf{Z}_{\text{int}(i)} = \frac{p_i \gamma_i}{2\pi r_i} \left[ \frac{I_0(\gamma_i r_i)K_1(\gamma_i q_i) + I_1(\gamma_i q_i)K_0(\gamma_i r_i)}{I_1(\gamma_i r_i)K_1(\gamma_i q_i) - I_1(\gamma_i q_i)K_1(\gamma_i r_i)} \right]$$$

*基于修正贝塞尔函数，用于ATP等程序的高精度频变线路建模*

### 实心导体近似内部阻抗公式

$$$\mathbf{Z}_{\text{int}(i)} = \frac{p_i \gamma_i}{2\pi r_i} \coth\left(0.733\gamma_i r_i + \frac{0.3179\rho_i}{\pi r_i^2}\right)$$$

*PSCAD/EMTDC的LCP模块采用，常数k=0.733以优化低频计算效率*

### 总串联阻抗矩阵

$$$\mathbf{Z} = \mathbf{Z}_{\text{int}} + \mathbf{Z}_{\text{ext}} + \mathbf{Z}_{g}$$$

*叠加内部、外部及大地返回阻抗，构建完整线路频变阻抗模型*



## 验证详情

- **验证方式**: 对比仿真分析（稳态参数计算与EMT暂态统计开关仿真）
- **测试系统**: 三种典型架空输电线路配置：TL1(440kV/4分裂/350km)、TL2(765kV/6分裂/450km)、TL3(800kV/8分裂/2600km半波长线路)
- **仿真工具**: PSCAD/EMTDC (Line Constants Program), ATP (参考精确计算), 自定义数值计算脚本(贝塞尔函数求解)
- **验证结果**: 验证表明近似内部阻抗公式虽提升计算效率，但在多分裂、超长距离及高波阻抗负载工况下会引入不可忽略的累积误差。精确模型在SIL计算、损耗评估及暂态过电压预测中均表现出更高精度，尤其对C相过电压及稳态压降的修正至关重要，为HWTL绝缘设计与保护整定提供了更可靠的建模依据。
