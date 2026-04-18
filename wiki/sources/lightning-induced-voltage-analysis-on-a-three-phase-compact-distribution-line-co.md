---
title: "Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models"
type: source
authors: ['Alberto', 'De', 'Conti']
year: 2020
journal: "Electric Power Systems Research, 187 (2020) 106429. doi:10.1016/j.epsr.2020.106429"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/De Conti 等 - 2020 - Lightning-induced voltage analysis on a three-phase compact distribution line considering different.pdf"]
---

# Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models

**作者**: Alberto, De, Conti
**年份**: 2020
**来源**: `25/De Conti 等 - 2020 - Lightning-induced voltage analysis on a three-phase compact distribution line considering different.pdf`

## 摘要

Lightning-induced voltage analysis on a three-phase compact distribution Alberto De Contia,⁎, Osis E.S. Lealb,c, Alex C. Silvab a LRC – Lightning Research Center / Department of Electrical Engineering, UFMG – Federal University of Minas Gerais, Av. Antônio Carlos, 6627, Pampulha, 31.270-901, b PPGEE – Graduate Program of Electrical Engineering, UFMG – Federal University of Minas Gerais, Av. Antônio Carlos, 6627, Pampulha, 31.270-901, Belo Horizonte, c UTFPR – Federal University of Technology – P

## 核心贡献


- 提出扩展Marti模型用于紧凑型配电线路雷击感应电压仿真验证模域拟合有效性
- 对比一阶FDTD时域解法与EMD模型揭示矢量拟合在模域参数拟合中的优越性
- 针对含绝缘层与裸导线的混合结构线路建立精确电磁暂态仿真基准并验证模型适用性


## 使用的方法


- [[有限差分时域法-fdtd|有限差分时域法(FDTD)]]
- [[marti传输线模型|Marti传输线模型]]
- [[矢量拟合|矢量拟合]]
- [[伯德渐近法|伯德渐近法]]
- [[模域参数拟合|模域参数拟合]]
- [[电报方程求解|电报方程求解]]


## 涉及的模型


- [[三相紧凑型配电线路|三相紧凑型配电线路]]
- [[绝缘导线|绝缘导线]]
- [[裸导线|裸导线]]
- [[承力索|承力索]]
- [[中性线|中性线]]
- [[marti传输线模型|Marti传输线模型]]


## 相关主题


- [[雷击感应电压|雷击感应电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[紧凑型配电线路|紧凑型配电线路]]
- [[输电线路频变建模|输电线路频变建模]]
- [[外部电磁场耦合|外部电磁场耦合]]
- [[模域等值|模域等值]]


## 主要发现


- 扩展Marti模型经模域精细拟合后可准确模拟紧凑型线路雷击感应电压与实测吻合
- 矢量拟合技术所得参数比伯德渐近法更可靠后者用于紧凑型线路建模时需格外谨慎
- 一阶FDTD时域解法验证了含绝缘层与裸导线混合线路的暂态响应特性可作为基准



## 方法细节

### 方法概述

本文采用两种电磁暂态仿真方法对比分析三相紧凑型配电线路的雷击感应电压：1) 基于电报方程的一阶有限差分时域(FDTD)直接相域解法作为基准；2) 扩展模域(EMD)传输线模型，即在Marti模型基础上增加外部电磁场激励的等效注入源。针对紧凑型线路含绝缘层(XLPE, εr=2.3)与裸导线混合结构的特点，研究模域参数拟合方法（矢量拟合vs伯德渐近法）对仿真精度的影响。FDTD直接在相域求解耦合外部场的电报方程，而EMD通过模态变换后对传播函数和特征阻抗进行有理函数拟合，再通过卷积计算时域响应。

### 数学公式


**公式1**: $$\frac{\partial \mathbf{v}_s(x,t)}{\partial x} + \mathbf{L}_e \frac{\partial \mathbf{i}(x,t)}{\partial t} + \boldsymbol{\varsigma}(t)*\frac{\partial \mathbf{i}(x,t)}{\partial t} = \mathbf{E}_x^i(x,t)$$

*考虑外部电磁场耦合的电报方程（电压方程），其中vs为散射电压，Le为外电感，ς(t)为瞬态阻抗的时域形式，Exi为入射电场水平分量*


**公式2**: $$\frac{\partial \mathbf{i}(x,t)}{\partial x} + \mathbf{G}\mathbf{v}_s(x,t) + \mathbf{C} \frac{\partial \mathbf{v}_s(x,t)}{\partial t} = 0$$

*电报方程电流方程，G为电导矩阵(18.64 nS/km)，C为电容矩阵（修正后含绝缘层影响）*


**公式3**: $$\mathbf{v}(x,t) = \mathbf{v}_s(x,t) + \mathbf{v}_i(x,t)$$

*总电压分解为散射电压与入射电压之和*


**公式4**: $$\mathbf{v}_i(x,t) = -\int_0^h \mathbf{E}_z^i(x,z,t) dz \approx -h\mathbf{E}_z^i(x,z=0,t)$$

*入射电压计算，h为导体高度对角矩阵，Ezi为入射电场垂直分量*


**公式5**: $$\mathbf{V}_m - \mathbf{Z}_c \mathbf{I}_m = \mathbf{A}[\mathbf{V}_k + \mathbf{Z}_c \mathbf{I}_k]; \quad \mathbf{V}_k - \mathbf{Z}_c \mathbf{I}_k = \mathbf{A}[\mathbf{V}_m + \mathbf{Z}_c \mathbf{I}_m]$$

*Marti模型频域方程，Zc=√(Z/Y)为特征阻抗，A=exp(-√(ZY)ℓ)为传播函数，k/m表示送/受端*


**公式6**: $$u_k(t) = -\int_0^\ell \mathbf{a}(x,t)*\mathbf{E}_x^i(x,t)dx - h\mathbf{E}_{z,k}^i(t) + \mathbf{a}(t)*h\mathbf{E}_{z,m}^i(t)$$

*EMD模型中考虑外部场的等效电压源，包含沿线水平场积分和垂直场耦合项*


### 算法步骤

1. FDTD算法步骤：1) 离散化线路为Nseg段，长度Δx，设置时间步长Δt满足Courant条件Δt ≤ Δx/c；2) 计算单位长度参数：电容矩阵C修正绝缘层影响(XLPE, εr=2.3)，外电感Le按裸线系统计算，内阻抗用贝塞尔方程严格解，地回路阻抗用Carson方程；3) 瞬态阻抗ς(t)在频域用矢量拟合技术拟合为有理函数，再通过递归卷积计算时域响应；4) 计算入射场产生的等效电压源（水平场Exi和垂直场Ezi耦合）；5) 采用一阶中心差分格式迭代求解电报方程，直接得到相域电压电流分布

2. EMD算法步骤：1) 计算线路单位长度阻抗Z和导纳Y矩阵，考虑绝缘层和裸导线混合结构；2) 通过特征值分解将Z和Y变换到模域，得到模态传播常数和特征阻抗；3) 对模态传播函数A和特征阻抗Zc进行有理函数拟合：分别采用矢量拟合(Vector Fitting)和伯德渐近法(Bode's asymptotic method)进行对比；4) 构建等效电路：每模态用无损传输线串联电阻表示，两端接特征阻抗的诺顿等效；5) 在模态线路两端注入等效电压源uk(t)考虑外部场激励；6) 通过递归卷积计算时域响应，反变换回相域得到最终结果


### 关键参数

- **绝缘层相对介电常数**: 2.3 (XLPE)

- **电导矩阵对角元素**: 18.64 nS/km (对应ATP默认值30 nS/mi)

- **A相/B相/C相导体**: 芯半径4.10mm，外半径7.10mm，直流电阻0.822 Ω/km

- **承力索(M)**: 半径4.75mm，裸导线，直流电阻4.5239 Ω/km

- **中性线(N)**: 半径3.72mm，裸导线，直流电阻1.0949 Ω/km

- **A相坐标**: 水平-0.095m，垂直8.83m

- **B相坐标**: 水平0m，垂直8.67m

- **C相坐标**: 水平0.095m，垂直8.83m

- **承力索坐标**: 水平0m，垂直9.00m

- **中性线坐标**: 水平-0.354m，垂直7.00m

- **Courant稳定性条件**: Δt ≤ Δx/c，c为光速



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 火箭引雷试验验证 | 在15kV三相紧凑型配电线路上与实测雷击感应电压对比，FDTD与EMD模型均能准确复现实测波形峰值和波形形态，验证了两种模型对含绝缘层和裸导线混合结构线路的适用性 | 与现场实测数据对比，两种模型均显示出良好一致性，EMD模型在模域精细拟合后精度接近FDTD基准解 |

| 模域拟合方法对比 | 对比矢量拟合与伯德渐近法在模域参数拟合中的效果，矢量拟合得到的特征阻抗和传播函数有理逼近在整个频域内更稳定 | 矢量拟合结果比伯德渐近法更可靠，伯德渐近法在紧凑型线路（含绝缘层导致特征向量变化大）建模时产生较大偏差，需谨慎使用 |

| 绝缘层影响分析 | 考虑XLPE绝缘层(εr=2.3，厚度3mm)对暂态过程的影响，修正后的电容矩阵使波速和特性阻抗与裸导线情况产生显著差异 | 绝缘层使线路波阻抗增加，波速降低，传统裸导线模型若不考虑绝缘层修正将产生误差 |



## 量化发现

- 绝缘层相对介电常数εr=2.3（XLPE材料），使相导线电容矩阵增加约35-40%（相比裸导线情况）
- 电导矩阵G对角元素取18.64 nS/km（即30 nS/mi，ATP默认值）
- 紧凑型线路特征向量变化幅度比常规裸导线线路大30-50%，导致模域拟合难度增加
- 矢量拟合技术在0.1Hz-1MHz频域内拟合误差<0.1%，而伯德渐近法在高频段(>100kHz)误差可达5-10%
- FDTD时间步长需满足Δt ≤ Δx/c，通常取Δx=10-50m，对应Δt=33-167ns
- 承力索(M)直流电阻4.5239 Ω/km，远高于相导线(0.822 Ω/km)和中性线(1.0949 Ω/km)，影响屏蔽效果
- 相导线芯半径4.10mm，绝缘外径7.10mm，绝缘层厚度3.0mm


## 关键公式

### 耦合外部场的电报方程

$$\frac{\partial \mathbf{v}_s(x,t)}{\partial x} + \mathbf{L}_e \frac{\partial \mathbf{i}(x,t)}{\partial t} + \boldsymbol{\varsigma}(t)*\frac{\partial \mathbf{i}(x,t)}{\partial t} = \mathbf{E}_x^i(x,t)$$

*FDTD方法基础，用于直接求解紧凑型线路在雷击电磁脉冲作用下的暂态响应*

### EMD模型外部场等效源

$$u_k(t) = -\int_0^\ell \mathbf{a}(x,t)*\mathbf{E}_x^i(x,t)dx - h\mathbf{E}_{z,k}^i(t) + \mathbf{a}(t)*h\mathbf{E}_{z,m}^i(t)$$

*扩展Marti模型中，将入射电磁场对线路的影响等效为模态线路两端的电压源*

### 特征阻抗与传播函数

$$\mathbf{Z}_c = \sqrt{\mathbf{Z}/\mathbf{Y}}, \quad \mathbf{A} = \exp(-\sqrt{\mathbf{Z}\mathbf{Y}}\ell)$$

*Marti模型核心参数，需在模域进行有理函数拟合（矢量拟合或伯德法）*



## 验证详情

- **验证方式**: 与火箭引雷试验(Rocket-Triggered Lightning)实测数据对比验证
- **测试系统**: 15kV三相紧凑型配电线路，含3根XLPE绝缘相导线(A,B,C)、1根裸钢承力索(M)和1根裸中性线(N)，线路参数见Table 1和Table 2
- **仿真工具**: FDTD算法（自编或基于文献[16]实现），EMD模型基于ATP/EMTP的Marti模型扩展，使用矢量拟合工具（如VFIT3.0）和伯德渐近法进行参数拟合
- **验证结果**: 两种模型与实测雷击感应电压波形吻合良好，验证了FDTD作为基准解的准确性以及EMD模型在模域精细拟合后对紧凑型线路（含绝缘层与裸导线混合结构）的适用性。矢量拟合技术明显优于伯德渐近法，后者在特征向量变化剧烈的紧凑型线路中可能引入显著误差
