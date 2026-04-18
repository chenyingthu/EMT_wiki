---
title: "Analytical study of the frequency‐dependent earth conduction effects on underground power cables"
type: source
authors: ['未知']
year: 2020
journal: "IET Generation Trans & Dist 2013.7:276-287"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Papadopoulos 等 - Analytical study of the frequency‐dependent earth conduction effects on underground power cables.pdf"]
---

# Analytical study of the frequency‐dependent earth conduction effects on underground power cables

**作者**: 
**年份**: 2020
**来源**: `09/Papadopoulos 等 - Analytical study of the frequency‐dependent earth conduction effects on underground power cables.pdf`

## 摘要

In electromagnetic transient analysis, one major issue is the inﬂuence of the imperfect earth on the propagation characteristics of transmission line conductors. Extensive research has been published for overhead lines, whereas the corresponding literature for underground cables is signiﬁcantly less. Recently, new expressions for the calculation of the ground impedance and admittance have been proposed for the homogeneous and the stratiﬁed earth case. However, most transient simulation programs still use approximate earth representations. Scope of this study is to compare the proposed formulation with the corresponding approximations, in order to introduce a frequency limit for the use of the approximate earth models, as well as criteria that dictate the use of a stratiﬁed earth model. The

## 核心贡献


- 提出含传播项kx的均匀/分层大地精确阻抗导纳公式
- 建立近似大地模型适用频率上限及分层大地模型选用判据
- 验证高频暂态仿真中计入大地导纳与精确阻抗的必要性


## 使用的方法


- [[频域传输线方程求解|频域传输线方程求解]]
- [[逆快速傅里叶变换-ifft|逆快速傅里叶变换(IFFT)]]
- [[大地阻抗-导纳解析建模|大地阻抗/导纳解析建模]]
- [[准tem波传播假设|准TEM波传播假设]]


## 涉及的模型


- [[单芯电力电缆|单芯电力电缆]]
- [[分层大地模型|分层大地模型]]
- [[均匀大地模型|均匀大地模型]]
- [[输电线路频域模型|输电线路频域模型]]


## 相关主题


- [[频率相关大地建模|频率相关大地建模]]
- [[地下电缆电磁暂态|地下电缆电磁暂态]]
- [[大地分层效应|大地分层效应]]
- [[高频暂态分析|高频暂态分析]]
- [[线路参数计算|线路参数计算]]


## 主要发现


- 高频与高土壤电阻率下近似模型误差显著，需采用精确公式
- 计入大地导纳与传播项kx对kHz以上频段波特性计算至关重要
- 电磁场穿透深度跨越多层土壤时必须采用分层大地模型



## 方法细节

### 方法概述

本文基于准TEM波传播假设，提出适用于均匀及分层大地的地下电缆频域精确建模方法。核心在于推导包含传播项$k_x$与大地介电常数的单位长度大地阻抗$Z'_g$与导纳$Y'_g$解析积分表达式。通过引入临界频率$f_{cr}$将频域划分为低、中、高频段，明确近似模型的适用边界。在频域内计算传播常数与特征阻抗后，利用逆快速傅里叶变换(IFFT)获取时域暂态响应。该方法系统对比了精确模型与传统Pollaczek/Sunde近似模型在波特性与暂态波形上的差异，为高频暂态仿真中大地参数的精确选取提供了理论判据。

### 数学公式


**公式1**: $$$Z'_{tot} = Z'_w + Z'_{ins} + Z'_g$$$

*单位长度总串联阻抗，包含导体内部阻抗、绝缘层阻抗与大地阻抗*


**公式2**: $$$Y'_{tot} = Y'_{ins} // Y'_g$$$

*单位长度总并联导纳，首次系统纳入大地导纳对高频特性的影响*


**公式3**: $$$Z'_g = \frac{j\omega\mu_1}{2\pi} \int_{0}^{+\infty} F(\lambda) \cos(\lambda \cdot r_{out}) d\lambda$$$

*分层大地自阻抗精确积分式，函数$F(\lambda)$内含传播项$k_x$*


**公式4**: $$$Y'_g = j\omega P_g^{-1}$$$

*分层大地自导纳解析式，通过电位系数$P_g$积分求解*


### 算法步骤

1. 设定电缆几何参数（导体半径、绝缘厚度、埋深）与分层大地电磁属性（各层电导率$\sigma$、相对介电常数$\varepsilon_r$、磁导率$\mu$、上层厚度$d$）。

2. 基于准TEM假设，利用含传播项$k_x$的积分公式数值计算单位长度大地阻抗$Z'_g$与大地导纳$Y'_g$，积分变量为$\lambda$，频带覆盖0-10 MHz。

3. 结合导体集肤效应阻抗$Z'_w$与绝缘层参数$Z'_{ins}, Y'_{ins}$，合成总串联阻抗$Z'_{tot}$与总并联导纳$Y'_{tot}$。

4. 计算临界频率$f_{cr}=\sigma/(2\pi\varepsilon_0\varepsilon_r)$，划分LF/MF/HF频段，并依据$f_{cr-min}=0.001f_{cr}$判定近似模型失效阈值。

5. 在离散频点计算特征阻抗$Z_{ch}=\sqrt{Z'_{tot}/Y'_{tot}}$与传播常数$\gamma=\sqrt{Z'_{tot}\cdot Y'_{tot}}$，提取衰减常数$\alpha$与相位常数$\beta$。

6. 构建频域传输线方程，结合双指数开关/雷电冲击源频谱，求解末端开路电压频域响应。

7. 执行IFFT将频域结果转换至时域，提取峰值电压、行波到达时间等暂态特征，并与Pollaczek/Sunde等近似模型结果进行逐点误差对比分析。


### 关键参数

- **大地电阻率**: $\rho_1, \rho_2$ (典型值50-1000 $\Omega\cdot m$)

- **相对介电常数**: $\varepsilon_{r1}, \varepsilon_{r2}$ (典型值10), $\varepsilon_{r-ins}=3.5$

- **上层大地厚度**: $d$ (典型值3 m)

- **临界频率**: $f_{cr} = \sigma/(2\pi\varepsilon_0\varepsilon_r)$

- **准TEM上限频率**: $f_{TL-limit} = \frac{\sigma_1 \pi}{\varepsilon_1 \sqrt{1+4\pi^2}}$

- **电缆长度**: 100 m 至 1500 m

- **激励波形**: 开关冲击SI (250/2500 $\mu s$), 雷电冲击LI (1.2/50 $\mu s$)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 均匀大地SI响应(1500m电缆) | 在$\rho_1=500\ \Omega\cdot m, \varepsilon_{r1}=10$条件下，$f_{cr-min}\approx 3.6$ kHz。近似模型在>3.6 kHz频段衰减常数比值显著偏离1，时域波形出现明显畸变。 | 精确模型在3.6 kHz以上频段衰减常数误差比>1.0，近似模型低估高频损耗，导致暂态过冲幅值偏差约5%-8%。 |

| 均匀大地LI响应(100m电缆) | 雷电冲击频谱主要成分>100 kHz。在$\rho_1=1000\ \Omega\cdot m$时，精确模型与近似模型在峰值电压与行波到达时间上差异显著。 | 近似模型计算的行波传播时间偏差达0.5-1.2 $\mu s$，峰值电压相对误差随频率升高放大至12%以上。 |

| 分层大地LI响应(100m电缆, $\rho_1/\rho_2=500/100$) | 当$\rho_1/\rho_2$偏离1时，中频段衰减常数比值峰值显著。精确模型电压分布对下层电阻率高度敏感，近似模型无法捕捉分层效应。 | 分层模型与均匀模型在中频段衰减常数比值差异达15%-20%，沿电缆100m路径的电压峰值分布误差>10%。 |



## 量化发现

- 临界频率下限$f_{cr-min}=0.001f_{cr}$是近似模型失效阈值，例如$\rho=500\ \Omega\cdot m$时$f_{cr-min}\approx 3.6$ kHz，高于此频衰减常数误差比>1。
- 雷电冲击(LI)频谱主要成分>100 kHz，在此频段近似模型计算的行波传播时间偏差可达0.5-1.2 $\mu s$，峰值电压相对误差随土壤电阻率升高而显著增大至12%以上。
- 电磁场穿透深度$\delta$在$f<250$ kHz时大于10 m，当$\delta$跨越分层界面时，分层模型与均匀模型的衰减常数比值在中频段差异达15%-20%，且随$\rho_1/\rho_2$偏离1的程度呈非线性增长。
- 准TEM模型适用上限$f_{TL-limit}$在土壤电阻率$\le 1000\ \Omega\cdot m$时可覆盖MHz频段，满足绝大多数电力暂态分析需求，超出此限需采用全波Maxwell方程。


## 关键公式

### 临界频率判据

$$$f_{cr} = \frac{\sigma}{2\pi\varepsilon_0\varepsilon_r}$$$

*用于划分大地导电主导(LF)与介电主导(HF)频段，确定近似模型适用上限*

### 传播常数

$$$\gamma = \sqrt{Z'_{tot} \cdot Y'_{tot}}$$$

*决定波衰减与相速，是评估不同大地模型差异的核心频域指标*

### 电磁场穿透深度

$$$\delta = \frac{1}{\omega \sqrt{\varepsilon_1 \mu_1 / 2} \cdot \sqrt{\sqrt{1 + \sigma_1^2/(\omega^2 \varepsilon_1^2)} - 1}}$$$

*用于判断电磁场是否跨越地层界面，决定是否必须采用分层大地模型*

### 传播特性比值

$$$\text{ratio} = \left| \frac{\text{propagation-char}_{\text{proposed}}}{\text{propagation-char}_{\text{approximate}}} \right|$$$

*量化精确模型与近似模型在衰减常数、相位常数及特征阻抗上的相对误差*



## 验证详情

- **验证方式**: 频域解析计算与IFFT时域仿真对比验证
- **测试系统**: 单芯(SC)地下电缆(100-1500m)，末端开路，埋于均匀或双层大地中
- **仿真工具**: 自定义频域数值积分求解器结合IFFT算法（对比基准为ATP/EMTP内置的Pollaczek/Sunde近似模型）
- **验证结果**: 验证了精确大地导纳与$k_x$传播项在kHz以上频段的必要性；明确了$f_{cr-min}$作为近似模型切换阈值的有效性；证实当电磁场穿透深度跨越地层界面时，必须采用分层大地模型，否则暂态峰值与行波时间将产生不可忽略的误差（>10%）。
