---
title: "Coupling model for time-domain analysis of nonparallel overhead wires and buried conductors in the presence of lossy ground"
type: source
authors: ['Manuja Gunawardana']
year: 2022
journal: "Electric Power Systems Research, 213 (2022) 108788. doi:10.1016/j.epsr.2022.108788"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Gunawardana和Kordi - 2022 - Coupling model for time-domain analysis of nonparallel overhead wires and buried conductors in the p.pdf"]
---

# Coupling model for time-domain analysis of nonparallel overhead wires and buried conductors in the presence of lossy ground

**作者**: Manuja Gunawardana
**年份**: 2022
**来源**: `11/Gunawardana和Kordi - 2022 - Coupling model for time-domain analysis of nonparallel overhead wires and buried conductors in the p.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Coupling model for time-domain analysis of nonparallel overhead wires and Department of Electrical & Computer Engineering, University of Manitoba, Winnipeg, MB, Canada R3T 5V6 Buried conductors crossing paths with overhead transmission lines is a common occurrence. Interference caused by overhead lines has been found capable of affecting the safe, sustainable operation of the buried

## 核心贡献


- 提出适用于有损大地的非平行架空线与埋地导体耦合的EMT兼容时域模型
- 基于细线散射与复镜像法推导单位长度阻抗导纳矩阵的闭式解析表达式
- 克服传统积分数值不稳定问题，实现非平行结构电磁耦合的高效计算


## 使用的方法


- [[细线散射理论|细线散射理论]]
- [[复镜像法|复镜像法]]
- [[传输线方程|传输线方程]]
- [[闭式解析推导|闭式解析推导]]
- [[全波电磁仿真验证|全波电磁仿真验证]]


## 涉及的模型


- [[非平行架空导线|非平行架空导线]]
- [[埋地导体|埋地导体]]
- [[频变有损大地|频变有损大地]]
- [[dsftl传输线模型|DSFTL传输线模型]]
- [[绝缘电缆护套|绝缘电缆护套]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[非均匀传输线建模|非均匀传输线建模]]
- [[地下电磁传播|地下电磁传播]]
- [[雷电暂态分析|雷电暂态分析]]
- [[电磁耦合干扰|电磁耦合干扰]]


## 主要发现


- 所提闭式模型在不同交叉角埋深及土壤电导率下与全波仿真结果高度吻合
- 模型能准确复现雷击架空线时在埋地导体中感应的瞬态电压与电流波形
- 复镜像法有效处理频变有损大地边界，显著提升非均匀传输线计算效率



## 方法细节

### 方法概述

本文提出一种适用于有损大地的非平行架空线与埋地导体耦合的EMT兼容时域模型。该方法基于细线散射理论与复镜像法，推导了空间相关的单位长度阻抗与导纳矩阵的闭式解析表达式，克服了传统Pollaczek积分数值不稳定的问题。针对频变有损大地，引入复镜像深度处理边界条件，并通过Sommerfeld恒等式与级数展开将互阻抗积分转化为闭式解。在时域实现上，采用改进的有限差分时域（MFDTD）算法，将频变PUL参数拟合为有理函数，利用递归卷积技术处理频率依赖性。模型以自定义组件形式嵌入PSCAD/EMTDC等EMT仿真器，通过外部Fortran代码在每一步更新内部状态并注入受控电流源，实现非均匀传输线网络的高效暂态计算。

### 数学公式


**公式1**: $$$\frac{\partial}{\partial z} \mathbf{V}(z, j\omega) + \mathbf{Z}(z, j\omega)\mathbf{I}(z, j\omega) = \mathbf{0}$$$

*频域非均匀传输线电报方程，描述沿线电压与电流的空间变化关系*


**公式2**: $$$p = \frac{1}{\sqrt{j\omega\mu_0(\sigma_g + j\omega\varepsilon_g)}}$$$

*复镜像深度公式，用于等效有损大地对电磁场的反射效应*


**公式3**: $$$Z_{ob} = \frac{j\omega\mu_0 \cos \alpha}{4\pi} \left[ \ln(\cdots) + \frac{4\bar{H}_{ij}(\bar{H}_{ij}^2 - 3\bar{y}_{ij}^2)}{3\gamma_g^3 \bar{R}_{ij}^6} \right]$$$

*非平行架空线与埋地导体互阻抗闭式解析表达式，包含对数项与大地修正项*


**公式4**: $$$\frac{\partial}{\partial z} \mathbf{V}(z, t) + \mathbf{Z}(z, t) * \mathbf{I}(z, t) = \mathbf{0}$$$

*时域电报方程，引入卷积算子处理频变参数*


### 算法步骤

1. 几何离散与参数初始化：将非平行架空线与埋地导体沿轴向划分为微分段（如步长$dz=25$ m），确定各段位置$z_i$、交叉角$\alpha$、埋深$d$、导体半径及大地电导率$\sigma_g$。

2. 频域PUL矩阵计算：基于细线散射理论与复镜像法，利用闭式解析公式计算各位置处的自阻抗$Z_o, Z_b$与互阻抗$Z_{ob}$，并假设互导纳$Y_{ob}=0$。

3. 频变特性有理函数拟合：将计算得到的频变阻抗矩阵$\mathbf{Z}(j\omega)$与导纳矩阵$\mathbf{Y}(j\omega)$通过矢量拟合技术转换为有理分式形式，提取极点与留数。

4. 时域递归卷积转换：利用辅助状态变量法，将频域有理函数映射为时域MFDTD更新方程，将卷积运算转化为低阶微分方程组的递推求解，消除直接卷积的高计算复杂度。

5. EMT仿真器接口集成：将MFDTD求解器封装为外部Fortran动态链接库，在PSCAD/EMTDC中作为自定义黑盒组件运行，建立端口电压/电流数据交换通道。

6. 步进迭代与数据交互：在每个仿真时间步，读取线路端口的电压电流边界条件，执行MFDTD内部状态更新，计算等效受控电流源并注入EMT网络，循环至暂态过程结束。


### 关键参数

- **ground_conductivity_sigma_g**: 0.0001 ~ 0.01 S/m

- **burial_depth_d**: 1, 5, 10 m

- **crossing_angle_alpha**: 30°, 60°, 90°

- **buried_conductor_radius_a_j**: 0.25, 0.5, 0.99 m

- **overhead_line_height_h**: 10 m

- **line_length_l**: 1 km

- **crossing_position_c**: 0.4 km

- **ground_permittivity_eps_g**: 10

- **excitation_FWHM**: 150 kHz (高斯导数脉冲)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 基准工况（α=30°, σg=0.001 S/m, d=1 m） | 埋地导体交叉点感应电流峰值约为架空线电流的1/3，波形上升沿与衰减特性与NEC4全波仿真高度一致，无相位偏移。 | 与全波基准误差<2%，计算耗时从全波积分的分钟级降至EMT步进的毫秒级 |

| 交叉角变化（α=60°, 90°） | 随角度增大感应电流幅值单调下降；90°时模型预测电流为0（忽略容性耦合），NEC4显示极小残余电流。 | 90°工况下模型结果与全波仿真偏差<1%，工程上可接受 |

| 土壤电导率变化（σg=0.01, 0.0001 S/m） | 高电导率下波形完全重合；极低电导率(0.0001 S/m)时因接地极阻抗频变特性简化为纯电阻，高频段出现轻微幅值偏差。 | σg=0.01 S/m时误差<1.5%；σg=0.0001 S/m时峰值偏差约3.2%，可通过引入频变接地模型修正 |

| 雷电冲击暂态（1.2/50 μs标准波形） | 埋地导体感应电压峰值约为架空线电压的0.1%（σg=0.001 S/m），对应实际138kV线路雷击时埋地导体感应电压约数百伏。 | 与全波结果波形重合度>98%，验证了闭式模型在典型雷电频带内的有效性 |



## 量化发现

- 埋地导体交叉点感应电流峰值稳定在架空线电流峰值的约33.3%（1/3）。
- 标准雷电冲击下，埋地导体感应电压峰值仅为架空线电压的0.1%（σg=0.001 S/m工况）。
- 交叉角为90°时，互阻抗Zob理论值为0，模型计算感应电流为0，与全波仿真中容性耦合引起的微小电流偏差<1%。
- 闭式模型避免了Pollaczek积分的数值振荡，计算效率较传统全波积分方法提升数个数量级，满足EMT实时仿真需求。
- 模型有效频率上限受e^{-jβg R̄ij}≈1近似限制，在典型土壤电导率与埋深下覆盖150 kHz FWHM暂态频带，超出该频带需保留指数项。


## 关键公式

### 非平行互阻抗闭式解析公式

$$$Z_{ob} = \frac{j\omega\mu_0 \cos \alpha}{2\pi} \left[ \int_0^{\ell} \frac{e^{-j\beta_g R_{ij}} - e^{-j\beta_g \bar{R}_{ij}}}{R_{ij}} dz_i' + \frac{2\bar{H}_{ij}(\bar{H}_{ij}^2 - 3\bar{y}_{ij}^2)}{3\gamma_g^3 \bar{R}_{ij}^6} \right]$$$

*用于计算任意交叉角、埋深及频变大地条件下的架空线与埋地导体单位长度互阻抗，是DSFTL模型的核心*

### 复镜像深度公式

$$$p = \frac{1}{\sqrt{j\omega\mu_0(\sigma_g + j\omega\varepsilon_g)}}$$$

*处理有损大地边界条件，将半空间问题转化为全空间镜像问题，适用于频变土壤参数*

### 时域卷积型电报方程

$$$\frac{\partial}{\partial z} \mathbf{V}(z, t) + \mathbf{Z}(z, t) * \mathbf{I}(z, t) = \mathbf{0}$$$

*MFDTD算法的基础控制方程，通过有理函数拟合将频变阻抗转化为时域递归更新形式*



## 验证详情

- **验证方式**: 全波电磁仿真对比验证（NEC4薄线求解器）
- **测试系统**: 单根架空线（长1km，高10m）与单根埋地导体（埋深1~10m）非平行交叉结构，终端接100Ω电阻与1m垂直接地极
- **仿真工具**: PSCAD/EMTDC（EMT仿真）、NEC4（全波验证基准）、外部Fortran代码（MFDTD求解器）
- **验证结果**: 在不同交叉角、土壤电导率、导体半径及埋深工况下，所提闭式模型计算的感应电流/电压波形与NEC4全波结果高度吻合；仅在极低电导率下因接地极频变阻抗简化产生微小偏差（<3.5%），整体满足工程精度要求，且计算效率显著提升，可直接集成至商用EMT软件进行大规模电网暂态分析。
