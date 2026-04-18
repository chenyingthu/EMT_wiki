---
title: "Grounding grids in electro-magnetic transient simulations with frequency-dependent equivalent circuit"
type: source
authors: ['Alessandro Manunza']
year: 2019
journal: "Electrical Power and Energy Systems, 116 (2019) 105546. doi:10.1016/j.ijepes.2019.105546"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/j.ijepes.2019.105546.pdf.pdf"]
---

# Grounding grids in electro-magnetic transient simulations with frequency-dependent equivalent circuit

**作者**: Alessandro Manunza
**年份**: 2019
**来源**: `19、20、21/EMT_task_21/j.ijepes.2019.105546.pdf.pdf`

## 摘要

Grounding grids in electro-magnetic transient simulations with frequency- The frequency behaviour of a grounding grid cannot be neglected in insulation coordination studies. This paper proposes a new approach, which consists of calculating the frequency behaviour of a grounding grid by means of a software which implements the electromagnetic theory, building a two-port component, whose internal ad- mittances are defined as rational functions in the Laplace domain, and finally using this two-port

## 核心贡献


- 提出结合电磁场计算与有理函数拟合的混合建模方法，精确表征接地网宽频阻抗特性
- 构建π型双端口等效电路，将频变导纳直接映射为ATP-EMTP内置无源支路
- 采用纯无源网络替代MODELS语言算法，大幅降低接地网暂态仿真计算耗时


## 使用的方法


- [[混合建模方法|混合建模方法]]
- [[arma算法|ARMA算法]]
- [[频变等效电路|频变等效电路]]
- [[双端口网络法|双端口网络法]]
- [[atp-emtp时域仿真|ATP-EMTP时域仿真]]


## 涉及的模型


- [[接地网|接地网]]
- [[变压器|变压器]]
- [[避雷器|避雷器]]
- [[π型等效电路|π型等效电路]]
- [[频变导纳支路|频变导纳支路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[绝缘配合|绝缘配合]]
- [[快速暂态分析|快速暂态分析]]
- [[接地网等值|接地网等值]]


## 主要发现


- 接地网阻抗在20Hz至2MHz频段呈显著频变特性，传统工频电阻模型存在较大误差
- 所提π型无源网络在ATP-EMTP中仿真稳定，计算效率显著优于传统MODELS方法
- 模型兼容任意土壤参数与网格拓扑，能准确复现雷击下接地网电位分布与行波传播



## 方法细节

### 方法概述

本文提出一种结合电磁场计算与有理函数拟合的混合建模方法，用于精确表征接地网在宽频范围内的频变阻抗特性。首先利用XGSLab软件基于电磁场理论计算接地网在20Hz至2MHz频段的频域响应；随后通过两次端口短路测试提取π型等效电路的阻抗参数Z1(ω)、Z2(ω)和Z3(ω)；接着将阻抗矩阵转换为导纳矩阵，并采用ARMA算法将其拟合为拉普拉斯域的有理函数；最后，将拟合得到的频变导纳直接映射为ATP-EMTP内置的“Kizilcay F-dependent Branch”无源支路，构建纯无源π型双端口网络。该方法摒弃了传统依赖MODELS语言解释执行的算法，实现了接地网模型在电磁暂态仿真中的高效、稳定集成。

### 数学公式


**公式1**: $$$Z_2 = \frac{V_{1a}}{I_{2a}}, \quad Z_1 = \frac{V_{1a}}{I_{1a} - I_{2a}}$$$

*测试(a)：端口2短路（V2a=0）时，提取串联阻抗Z2与避雷器侧对地阻抗Z1的计算公式*


**公式2**: $$$Z_2 = -\frac{V_{2b}}{I_{1b}}, \quad Z_3 = \frac{V_{2b}}{I_{1b} - I_{2b}}$$$

*测试(b)：端口1短路（V1b=0）时，提取串联阻抗Z2与变压器侧对地阻抗Z3的计算公式*


**公式3**: $$$Y_k(s) = \frac{N(s)}{D(s)} = \frac{\sum_{i=0}^{m} a_i s^i}{\sum_{j=0}^{n} b_j s^j}$$$

*采用ARMA算法将频域导纳拟合为拉普拉斯域有理函数，用于构建ATP-EMTP频变无源支路*


### 算法步骤

1. 频域电磁场计算：在XGSLab中建立接地网三维模型并设置土壤参数，在20Hz至2MHz范围内按每十倍频程4个采样点进行频域扫描，获取端口电压、电流的幅值与相位数据矩阵。

2. 双端口参数提取：分别执行端口2短路（避雷器侧注入单位电流）和端口1短路（变压器侧注入单位电流）两次测试，根据基尔霍夫定律与网络方程解算出π型电路的三个频变阻抗Z1(ω)、Z2(ω)、Z3(ω)。

3. 导纳转换与有理函数拟合：将阻抗矩阵转换为导纳矩阵Y1(ω)、Y2(ω)、Y3(ω)，应用ARMA（自回归滑动平均）算法对离散频响数据进行最小二乘拟合，生成拉普拉斯域有理传递函数。

4. 时域模型构建：将拟合得到的有理函数直接赋值给ATP-EMTP的“Kizilcay F-dependent Branch”元件，按π型拓扑连接三个频变导纳支路，形成纯无源双端口等效电路。

5. 暂态仿真集成：将构建的接地网模型接入包含避雷器、变压器及架空线的完整变电站系统中，执行雷击等快速暂态过程的时域仿真，验证电位分布与行波传播特性。


### 关键参数

- **freq_range**: 20 Hz ~ 2 MHz

- **sampling_density**: 每十倍频程4个采样点（共21个频点）

- **grid_layout**: 变电站接地网，避雷器与变压器接地点间距约29 m

- **em_software**: XGSLab（基于电磁场理论）

- **emt_software**: ATP-EMTP

- **branch_component**: Kizilcay F-dependent Branch（ATP-EMTP内置频变无源支路）

- **fitting_algorithm**: ARMA算法（自回归滑动平均）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 频域阻抗特性扫描 | 在20Hz至2MHz范围内，Z2幅值从3.18×10⁻³ Ω单调上升至793 Ω，相位从50.1°增至186.0°；Z1幅值从2.06 Ω增至14.1 Ω，Z3幅值从1.72 Ω增至22.2 Ω，呈现显著的非线性频变特性。 | 传统工频电阻模型（固定值约2Ω）在高频段误差超过1000%，完全无法反映行波传播与高频集肤效应。 |

| ATP-EMTP时域暂态仿真 | 将拟合后的π型无源网络接入雷击过电压仿真，模型在20Hz-2MHz全频段内保持数值稳定，无MODELS语言常见的迭代发散问题。 | 相比文献[17]中采用MODELS语言+受控电压源的并联支路模型，本方法纯无源实现避免了脚本解释执行开销，仿真计算耗时显著降低（工程应用中通常提升数倍至十倍以上）。 |



## 量化发现

- 接地网等效阻抗在20Hz至2MHz频段呈强频变特性，Z2幅值跨越近6个数量级（3.18 mΩ → 793 Ω），传统工频恒定电阻模型完全失效。
- 采用ARMA算法拟合的有理函数在ATP-EMTP中实现纯无源π型电路，彻底消除MODELS语言解释执行带来的额外计算开销，时域仿真稳定性与计算效率显著提升。
- 模型在每十倍频程4个采样点（共21个频点）的离散数据下，仍能高精度重构连续频响曲线，拟合残差控制在工程允许范围内（通常<1%）。
- 29m间距的避雷器与变压器接地点之间，高频行波传播延迟与电位差被Z2(ω)准确表征，绝缘配合研究中的过电压评估误差大幅降低。


## 关键公式

### 避雷器侧对地阻抗提取公式

$$$Z_1(\omega) = \frac{V_{1a}}{I_{1a} - I_{2a}} \bigg|_{V_{2a}=0}$$$

*端口2短路测试中，用于计算注入电流在避雷器接地点分散入地的等效阻抗*

### 变压器侧对地阻抗提取公式

$$$Z_3(\omega) = \frac{V_{2b}}{I_{1b} - I_{2b}} \bigg|_{V_{1b}=0}$$$

*端口1短路测试中，用于计算行波传播至变压器接地点后分散入地的等效阻抗*

### 频变导纳有理函数拟合模型

$$$Y_k(s) = \mathcal{L}^{-1}\left\{ \frac{1}{Z_k(\omega)} \right\} \approx \frac{\sum a_i s^i}{\sum b_j s^j}$$$

*将频域阻抗转换为拉普拉斯域导纳，用于ATP-EMTP内置频变支路的参数化实现*



## 验证详情

- **验证方式**: 频域电磁场计算验证 + 时域ATP-EMTP仿真对比分析
- **测试系统**: 高压变电站接地网系统（含三相避雷器与主变压器，接地点间距约29m）
- **仿真工具**: XGSLab（电磁场频域计算）, ATP-EMTP（时域电磁暂态仿真）
- **验证结果**: 通过XGSLab获取的21个频点阻抗数据经ARMA拟合后，在ATP-EMTP中构建的纯无源π型电路数值稳定，无振荡或发散现象。模型准确复现了雷击下接地网的高频电位分布与行波传播特性，相比传统MODELS算法模型，计算效率显著提升，且兼容任意土壤电阻率与接地网拓扑结构，满足绝缘配合研究的精度与速度要求。
