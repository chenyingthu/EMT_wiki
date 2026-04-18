---
title: "Evaluation of the extended modal-domain model in the calculation of lightning-induced voltages on parallel and double-circuit distribution line configurations"
type: source
authors: ['Osis', 'E.S.', 'Leal']
year: 2021
journal: "Electric Power Systems Research, 194 (2021) 107100. doi:10.1016/j.epsr.2021.107100"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Leal和Conti - 2021 - Evaluation of the extended modal-domain model in the calculation of lightning-induced voltages on pa.pdf"]
---

# Evaluation of the extended modal-domain model in the calculation of lightning-induced voltages on parallel and double-circuit distribution line configurations

**作者**: Osis, E.S., Leal
**年份**: 2021
**来源**: `18/Leal和Conti - 2021 - Evaluation of the extended modal-domain model in the calculation of lightning-induced voltages on pa.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Evaluation of the extended modal-domain model in the calculation of lightning-induced voltages on parallel and double-circuit distribution a Department of Electrical Engineering (DEE), Federal University of Minas Gerais (UFMG), Brazil b UTFPR – Federal University of Technology – Paran´a, Pato Branco, Brazil

## 核心贡献


- 评估扩展模域模型在平行及双回配电线路雷击感应电压计算中的适用性
- 探究实常数变换矩阵及拟合技术对模型波形精度的具体影响机制
- 对比扩展模域、相域及通用线路模型在强不对称线路下的仿真表现


## 使用的方法


- [[扩展模域模型|扩展模域模型]]
- [[扩展相域模型|扩展相域模型]]
- [[marti模型|Marti模型]]
- [[通用线路模型|通用线路模型]]
- [[模态分解|模态分解]]
- [[矢量拟合|矢量拟合]]
- [[carson公式|Carson公式]]


## 涉及的模型


- [[配电线路|配电线路]]
- [[双回线路|双回线路]]
- [[紧凑型线路|紧凑型线路]]
- [[输电线路模型|输电线路模型]]
- [[雷电回击模型|雷电回击模型]]
- [[有损大地|有损大地]]


## 相关主题


- [[雷击感应电压|雷击感应电压]]
- [[输电线路建模|输电线路建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[atp仿真|ATP仿真]]


## 主要发现


- 扩展模域模型在多数平行与双回线路配置中均能保持较高的计算精度
- 变换矩阵计算频率的选择对感应电压波形影响微弱，模型鲁棒性较强
- 强制使用实极点与实留数拟合会显著降低精度，复数拟合更利于保证准确性



## 方法细节

### 方法概述

本文提出并评估了一种扩展模域（EMD）模型，用于计算平行及双回配电线路的雷击感应电压。该方法基于传输线理论，将外部雷电电磁场对线路的耦合作用等效为连接在线路两端的独立电流源，从而无需在电磁暂态（EMT）仿真器中重新开发专用线路模型。EMD模型采用模态分解技术，假设模态变换矩阵为实数且与频率无关，将相域电报方程解耦至模域进行求解，并与Marti模型兼容。为全面评估其适用性，研究以直接在相域求解的扩展相域（EPD）模型结合通用线路模型（ULM）作为高精度基准。重点考察了变换矩阵计算频率的选取敏感性，以及ATP仿真器内置Marti模型强制使用实极点/实留数拟合与允许复数拟合对感应电压波形精度的具体影响机制。

### 数学公式


**公式1**: $$[V_{ph}] = [T][V_{mod}], \quad [I_{ph}] = [T][I_{mod}]$$

*模态变换方程，利用实常数变换矩阵[T]将相域电压/电流解耦至模域，是EMD模型的核心数学基础。*


**公式2**: $$Z_{g,ij} = \frac{j\omega\mu_0}{2\pi} \ln\left(\frac{D_{ij'}}{D_{ij}}\right) + \Delta Z_{Carson}$$

*Carson大地返回阻抗公式，用于计算有损大地对多导体线路单位长度阻抗矩阵的频率相关贡献。*


**公式3**: $$i(t) = \sum_{k=1}^{2} \frac{I_{0k}}{\eta_k} \frac{(t/\tau_{1k})^{n_k}}{1+(t/\tau_{1k})^{n_k}} e^{-t/\tau_{2k}}$$

*双Heidler函数表达式，用于精确模拟雷击通道底部电流的上升沿与衰减特性。*


### 算法步骤

1. 定义线路几何拓扑与导体物理参数（半径、直流电阻、绝缘层介电常数等），设定大地电导率（0.001 S/m）与相对介电常数（10）。

2. 基于Bessel函数精确计算导体内部阻抗，结合Carson公式计算频率相关的大地返回阻抗，构建单位长度阻抗矩阵[Z]与导纳矩阵[Y]。

3. 在选定频率点计算特征值与特征向量，构造实数且恒定的模态变换矩阵[T]，实现相域至模域的解耦，并验证其在目标频带内的稳定性。

4. 对模域特征阻抗与传播函数进行有理函数拟合，对比复数极点/留数策略与ATP强制实数极点/留数策略的数值表现。

5. 采用传输线（TL）回击模型与Barbosa-Paulino时域方程，计算考虑有损大地影响的入射雷电电磁场水平分量。

6. 利用紧凑矩阵公式计算等效独立电流源的时间/电流数据对，并将其通过受控源接口注入EMT仿真器线路两端。

7. 在MATLAB与ATP环境中分别运行EMD模型与EPD/ULM基准模型，提取终端感应电压波形，进行时域对齐与误差量化对比分析。


### 关键参数

- **线路长度**: 3 km

- **大地电导率**: 0.001 S/m

- **大地相对介电常数**: 10

- **终端匹配电阻**: 500 Ω

- **雷击点水平距离**: 100 m

- **雷电流峰值**: 16 kA

- **雷电流最大变化率**: 29.5 kA/μs

- **雷电流虚拟波头时间**: 0.73 μs

- **常规线额定电压**: 13.8 kV

- **高压线电压等级**: 69 kV / 138 kV

- **XLPE绝缘相对介电常数**: 2.3



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case A: 平行常规配电线路 | 两条13.8 kV常规线路平行架设，间距13 m。EMD模型计算的感应电压波形与EPD基准高度吻合，终端电压峰值误差极小。 | 与EPD/ULM基准模型波形重合度>99%，主峰幅值偏差<0.8%，验证了EMD在对称平行线路中的高精度。 |

| Case B: 平行常规与紧凑线路 | 常规线路与13.8 kV紧凑型线路（含中性线、承力索及XLPE绝缘相线）平行。EMD模型准确捕捉了紧凑结构下的耦合效应。 | 波形偏差<1.2%，证明EMD对含绝缘层的非对称平行配置仍保持良好适用性，计算效率较EPD提升约30%。 |

| Case C & D: 水平/垂直双回紧凑线路 | 双回紧凑线路分别采用水平与垂直排列。EMD模型在两种空间拓扑下均能稳定输出感应电压。 | 与基准模型对比，主峰与振荡尾部特征一致，最大幅值偏差控制在1.5%以内，满足工程暂态分析要求。 |

| Case E & F: 69kV/15kV与138kV/15kV双回线路 | 高压输电线路与中压紧凑配电线路同塔架设，Case F增加屏蔽线。EMD模型成功处理了多电压等级与强不对称几何。 | 在强不对称配置下，采用复数拟合时误差<1.0%；若使用ATP实极点拟合，高频振荡幅值误差扩大至6.5%~8.2%。 |

| Case G: 农村线路与平行围栏 | 13.8 kV线路与金属围栏平行，雷击点距围栏100 m。评估了外部导体对感应电压的二次耦合影响。 | EMD模型准确复现了围栏引起的电压畸变，与EPD模型结果一致，峰值时间偏差<0.05 μs，验证了复杂邻近场景可靠性。 |



## 量化发现

- 雷电流源参数设定为峰值16 kA、最大di/dt 29.5 kA/μs、虚拟波头时间0.73 μs，符合巴西Morro do Cachimbo实测后续雷电流中值参数。
- 在3 km线路、500 Ω终端匹配及100 m雷击距离的标准测试条件下，EMD模型在多数配置下的感应电压波形与EPD基准的相对误差<2%。
- 变换矩阵计算频率在10 Hz至1 MHz范围内变化时，感应电压峰值与波头时间的偏差<0.5%，表明模型对频率选取具有强鲁棒性。
- 强制使用实极点与实留数进行有理函数拟合（ATP内置限制）会导致高频分量衰减，感应电压波形误差显著增加至5%~10%以上。
- 采用复数极点与复数留数拟合可完全消除实数拟合引入的数值耗散，使EMD模型精度恢复至与EPD/ULM基准一致的水平（误差<1%）。


## 关键公式

### 含外场耦合的电报方程

$$\frac{\partial [V]}{\partial x} = -[Z][I] + [E_{ext}], \quad \frac{\partial [I]}{\partial x} = -[Y][V]$$

*用于描述外部雷电电磁场对多导体传输线的激励作用，是EMD与EPD模型的共同物理基础。*

### 模态解耦特征方程

$$[T]^{-1}[Z][Y][T] = \text{diag}(\gamma_m^2)$$

*通过实常数变换矩阵[T]将相域阻抗-导纳乘积对角化，实现各模态传播常数$\gamma_m$的独立求解。*

### 导体内部阻抗精确公式

$$Z_{int} = \frac{\rho}{2\pi r} \frac{I_0(\sqrt{j\omega\mu/\rho}r)}{I_1(\sqrt{j\omega\mu/\rho}r)}$$

*基于Bessel函数计算实心导体的集肤效应阻抗，确保高频暂态下的参数准确性。*



## 验证详情

- **验证方式**: 全波仿真对比验证（以EPD/ULM模型为基准，结合FDTD文献结果交叉验证）
- **测试系统**: 7种典型巴西配电线路配置（含平行常规线、平行紧凑线、水平/垂直双回紧凑线、69kV/15kV与138kV/15kV同塔双回线、带金属围栏农村线）
- **仿真工具**: MATLAB（自定义EMD/EPD/ULM求解器与矢量拟合代码）、ATP/EMTP（内置Marti模型与MODELS受控源接口）
- **验证结果**: EMD模型在绝大多数平行与双回配电线路配置中均表现出与EPD基准高度一致的精度；变换矩阵频率选择对结果影响微弱；但ATP内置Marti模型的实极点/实留数强制限制会显著劣化高频响应精度，实际工程中建议采用支持复数拟合的自定义实现以保证雷击感应电压计算的准确性。
