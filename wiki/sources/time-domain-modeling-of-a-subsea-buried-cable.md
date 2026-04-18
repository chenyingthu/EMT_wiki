---
title: "Time-domain modeling of a subsea buried cable"
type: source
authors: ['Felipe Camara']
year: 2024
journal: "Electric Power Systems Research, 233 (2024) 110444. doi:10.1016/j.epsr.2024.110444"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/38/Camara 等 - 2024 - Time-domain modeling of a subsea buried cable.pdf"]
---

# Time-domain modeling of a subsea buried cable

**作者**: Felipe Camara
**年份**: 2024
**来源**: `38/Camara 等 - 2024 - Time-domain modeling of a subsea buried cable.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Felipe Camara a, Antonio C.S. Lima b,∗, Maria Teresa Correia de Barros c, Filipe M. Faria da Silva d, b Federal University of Rio de Janeiro (UFRJ), Rio de Janeiro, Brazil Traditionally, electromagnetic transient (EMT) programs in the time domain cannot deal with submarine cables buried in the seabed, as available routines demand one medium to be lossless to de

## 核心贡献



- 提出了一种适用于海底埋设电缆的时域建模方法，克服了传统EMT程序因海水与海床双介质均有损耗而无法处理的限制
- 开发了基于特征线法（MoC）/通用线路模型（ULM）与基于折叠线等效（FLE）节点导纳矩阵有理拟合的两种时域实现方案

## 使用的方法


- [[vector-fitting]]
- [[nodal-analysis]]

## 涉及的模型


- [[cable]]
- [[transmission-line]]

## 相关主题


- [[hvdc]]
- [[frequency-dependent]]

## 主要发现



- 基于准TEM近似推导的每单位长度阻抗与导纳矩阵能够准确表征厚铠装海底埋设电缆的电磁暂态特性
- 所提两种时域建模方法的仿真结果与数值拉普拉斯变换（NLT）基准高度一致，验证了其在EMT程序中的高精度与工程适用性

## 方法细节

### 方法概述

本文提出了一种适用于海底埋设电缆的时域建模方法，解决了传统EMT程序无法处理海水与海床双损耗介质的问题。方法基于准TEM（准横电磁）近似对全波公式进行简化，推导了考虑双有损介质（海水和海底土壤）的单位长度参数。针对时域实现，提出了两种distinct方案：第一种基于特征线法（MoC），采用通用线路模型（ULM）结构，通过Vector Fitting对特征导纳和传播函数进行有理拟合并提取模态时延；第二种基于折叠线等效（FLE），对节点导纳矩阵进行分块有理拟合，将Yn分解为开路导纳Yoc和短路导纳Ysc分别处理，以提高低频段小特征值的拟合精度。两种方法均通过状态空间方程或伴随电路模型在EMT程序中实现。

### 数学公式


**公式1**: $$$Z = Z_{in} + Z_0$$$

*单位长度总阻抗矩阵，由内部阻抗和外部介质阻抗组成*


**公式2**: $$$Z_0 = z_0 \mathbf{1}$$$

*外部介质阻抗矩阵，对于单芯铠装电缆为单位矩阵与标量z0的乘积*


**公式3**: $$$Y = (Y_{in}^{-1} + \frac{1}{y_0}\mathbf{1})^{-1}$$$

*单位长度总导纳矩阵，由绝缘层导纳和外部介质导纳并联组成*


**公式4**: $$$z_0 = \frac{j\omega\mu}{2\pi}[\Lambda + S_1]$$$

*外部串联阻抗，基于Sommerfeld积分和准TEM近似*


**公式5**: $$$y_0 = 2\pi(\sigma_1 + j\omega\varepsilon_1)[\Lambda - S_3]^{-1}$$$

*外部并联导纳，考虑海水或土壤的导电率和介电常数*


**公式6**: $$$Y_c = \sqrt{Z^{-1} \cdot Y}$$$

*特征导纳矩阵*


**公式7**: $$$H = \exp(-\ell\sqrt{Y \cdot Z})$$$

*传播函数矩阵，ℓ为线路长度*


**公式8**: $$$Y_n = \begin{bmatrix} Y_s & Y_m \\ Y_m & Y_s \end{bmatrix}$$$

*节点导纳矩阵，其中Ys为自导纳，Ym为互导纳*


**公式9**: $$$Y_s = Y_c(I_n + H^2)(I_n - H^2)^{-1}$$$

*自导纳子矩阵表达式*


**公式10**: $$$Y_m = -2Y_c H(I_n - H^2)^{-1}$$$

*互导纳子矩阵表达式*


**公式11**: $$$Y_n = K \begin{bmatrix} Y_{oc} & 0 \\ 0 & Y_{sc} \end{bmatrix} K^{-1}$$$

*FLE分解形式，Yoc为开路导纳，Ysc为短路导纳，K为变换矩阵*


### 算法步骤

1. 计算电缆内部单位长度参数Z_in和Y_in：采用改进的EMT程序内部参数计算方法，考虑芯导体、护套、铠装的三层结构，铠装磁导率μa=90，电阻率ρa=11×10^-8 Ωm，护套电阻率ρs=22×10^-8 Ωm，芯导体电阻率ρc=1.723×10^-8 Ωm

2. 计算外部介质参数z0和y0：基于准TEM近似，求解Sommerfeld积分S1和S3，考虑海水（介质1）和海底土壤（介质2）的双有损特性，传播常数γ1和γ2均为复数，通过Bessel函数K0和数值积分计算Λ项

3. 构建总阻抗Z和导纳Y矩阵：按公式(1)和(3)叠加内部和外部参数，得到频变单位长度参数

4. 计算传播参数：通过特征值分解求解特征导纳Yc和传播函数H，采用公式(6)的矩阵平方根和指数运算

5. 模态分解与时延提取（MoC方法）：对传播函数H进行特征值分解H = Tv·Hm·Tv^-1，识别各模态的传播时延τi，利用Vector Fitting对模态传播函数进行有理拟合，拟合形式为∑(Ri/(s-pi))·e^(-sτi)

6. FLE分解与拟合（FLE方法）：将节点导纳矩阵Yn通过公式(10)分解为Yoc和Ysc，分别对这两个n×n矩阵进行有理拟合，避免直接拟合2n×2n矩阵导致的低频小特征值精度损失

7. 时域模型实现：MoC方法通过ULM结构实现，利用历史电流源和频变支路模型；FLE方法通过状态空间方程或伴随电路实现，将拟合的有理函数转换为等效电路元件


### 关键参数

- **core_radius**: 18.95 mm (R1)

- **insulation1_radius**: 28.95 mm (R2), εr=2.5

- **sheath_radius**: 30.65 mm (R3), ρ=22×10^-8 Ωm

- **insulation2_radius**: 33.15 mm (R4), εr=2.5

- **armor_radius**: 35.65 mm (R5), μr=90, ρ=11×10^-8 Ωm

- **outer_insulation_radius**: 44.10 mm (R6), εr=2.5

- **nominal_voltage**: 75 kV DC

- **cable_configuration**: 单极单芯厚铠装HVDC海底电缆

- **burial_depth**: 1 m (典型值)，最深可达5 m以上

- **seawater_depth**: 平均17 m，最大30 m (海上风电场景)

- **fitting_method**: Vector Fitting (VF)

- **reference_method**: Numerical Laplace Transform (NLT)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 75 kV HVDC海底电缆电磁暂态响应 | 针对长度为数公里的海底电缆，对比了MoC/ULM方法、FLE方法与NLT基准的时域响应。结果显示三种方法在芯导体、护套、铠装层的电压和电流波形上具有高度一致性，特别是在开关操作和故障暂态过程中 | 与NLT基准相比，两种 proposed 方法在整个频域范围内（特别是低频段）均保持了极高的精度，克服了传统EMT程序因强制设定一个无损耗介质而产生的误差 |

| 双有损介质外部场验证 | 验证了在 burial depth=1 m 时，电磁场在到达海表之前已完全衰减，确认无需三层介质模型（海水-海床-空气），但双有损介质（海水和海床）的精确建模对返回路径阻抗至关重要 | 传统EMT程序（要求一个介质无损耗）无法处理此场景，而本文方法可准确建模，场衰减计算显示在典型风电场景（水深17-30m，埋深1m）下，外部场不会穿透至海水表面 |



## 量化发现

- 电缆芯导体电阻率：1.723×10^-8 Ωm（铜导体标准值）
- 铠装层相对磁导率：90（钢材料典型值），电阻率：11×10^-8 Ωm
- 护套电阻率：22×10^-8 Ωm（铅或铝护套典型值）
- 绝缘层相对介电常数：2.5（XLPE典型值）
- 铠装层厚度：2.5 mm（R5-R4），外绝缘层厚度：8.45 mm（R6-R5）
- 模态传播时延提取精度：通过Vector Fitting准确识别了各传播模式的频变时延，确保了MoC方法的数值稳定性
- FLE分解后矩阵条件数改善：将Yn分解为Yoc和Ysc分别拟合，显著提高了低频段（<1 Hz）小特征值的拟合精度，避免了直接拟合导致的数值病态
- 与NLT基准的一致性：两种时域方法（MoC和FLE）的仿真结果与NLT基准在全时间尺度上呈现excellent agreement，误差水平与常规架空线或地下电缆模型相当


## 关键公式

### 双有损介质外部串联阻抗

$$$z_0 = \frac{j\omega\mu}{2\pi}\left[K_0(\gamma_1 r_j) + K_0(\gamma_1\sqrt{4h^2+r_j^2}) + S_1\right]$$$

*用于计算海底电缆在海水和海床中的外部阻抗，其中S1为Sommerfeld积分，考虑了两层有损介质的反射效应，是本文克服传统EMT限制的核心公式*

### 折叠线等效(FLE)分解

$$$Y_n = K \begin{bmatrix} Y_{oc} & \mathbf{0} \\ \mathbf{0} & Y_{sc} \end{bmatrix} K^{-1}$$$

*用于节点导纳矩阵的有理拟合，通过将Yn分解为开路和短路导纳，分别进行低阶有理拟合，解决了直接拟合大矩阵时低频精度不足的问题*

### 准TEM近似核心项

$$$\Lambda = K_0(\gamma_1 r_j) + K_0(\gamma_1\sqrt{4h^2+r_j^2})$$$

*计算外部介质阻抗时的主导项，包含直接路径和镜像路径的Bessel函数，γ1为海水中的复传播常数，h为埋深，rj为导体半径*



## 验证详情

- **验证方式**: 与数值拉普拉斯变换（NLT）基准对比验证，NLT被视为频域仿真的高精度参考方法
- **测试系统**: 75 kV单极单芯HVDC海底电缆，具体参数：芯径18.95mm，铠装外径35.65mm，总外径44.10mm，埋设于海床下1m，海水深度17-30m（典型海上风电场景）
- **仿真工具**: 基于MATLAB或类似科学计算环境实现算法原型，通过自定义代码实现Vector Fitting、Sommerfeld积分计算和NLT变换，可与PSCAD/EMTP/ATP等EMT程序接口
- **验证结果**: MoC/ULM方法和FLE方法的时域响应与NLT基准呈现excellent agreement，验证了准TEM近似在厚铠装海底电缆建模中的有效性。两种方法均成功处理了海水和海床的双有损特性，其中FLE方法在数值稳定性方面表现更优，特别适用于长电缆和低频暂态分析
