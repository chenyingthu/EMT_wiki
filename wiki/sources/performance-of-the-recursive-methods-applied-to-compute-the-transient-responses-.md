---
title: "Performance of the recursive methods applied to compute the transient responses on grounding systems"
type: source
authors: ['J.S.L. Colqui']
year: 2021
journal: "Electric Power Systems Research, 196 (2021) 107281. doi:10.1016/j.epsr.2021.107281"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2021.107281.pdf.pdf"]
---

# Performance of the recursive methods applied to compute the transient responses on grounding systems

**作者**: J.S.L. Colqui
**年份**: 2021
**来源**: `31/j.epsr.2021.107281.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Performance of the recursive methods applied to compute the transient J.S.L. Colqui a,*, A.R.J. de Araújo b, Claudiner M. de Seixas c, S. Kurokawa a, J. Pissolato Filho b a S˜ao Paulo State University-UNESP, Ilha Solteira, Brazil c Federal Institute of S˜ao Paulo-IFSP, Votuporanga, Brazil

## 核心贡献


- 提出两种时域递归算法直接计算接地系统暂态地电位升，无需雷电流解析式。
- 结合矢量拟合将频域接地阻抗转为极点留数形式，实现高效时域递归求解。
- 验证递归方法处理实测雷电流时精度优于ATP等效电路，且无需搭建软件模型。


## 使用的方法


- [[递归卷积法|递归卷积法]]
- [[递归梯形积分法|递归梯形积分法]]
- [[矢量拟合|矢量拟合]]
- [[矩量法|矩量法]]
- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[频时变换|频时变换]]


## 涉及的模型


- [[接地系统|接地系统]]
- [[水平接地极|水平接地极]]
- [[网格接地极|网格接地极]]
- [[雷电流源|雷电流源]]
- [[频变土壤模型|频变土壤模型]]
- [[atp等效电路|ATP等效电路]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[地电位升|地电位升]]
- [[接地系统|接地系统]]
- [[频率相关建模|频率相关建模]]
- [[雷击暂态分析|雷击暂态分析]]
- [[时域仿真|时域仿真]]


## 主要发现


- 递归方法计算的地电位升波形与数值拉普拉斯变换基准高度吻合，误差低于ATP。
- 该方法可直接处理实测雷电流数据，避免解析积分困难，适用于复杂土壤条件。
- 递归算法无需依赖电磁暂态软件搭建电路，具备独立编程实现的高效性与灵活性。



## 方法细节

### 方法概述

本文提出一种基于矢量拟合(VF)和递归算法的接地系统暂态地电位升(GPR)计算方法。首先利用全波电磁软件FEKO基于矩量法(MoM)计算接地系统在100 Hz至5 MHz频带内的频域接地阻抗$Z_h(s)$；随后采用矢量拟合技术将阻抗曲线拟合为极点-留数有理函数形式$Z_{h,fit}(s)$；最后分别通过递归卷积法(M1)和递归梯形积分法(M2)直接在时域计算GPR，无需依赖电磁暂态软件搭建等效电路。该方法可直接处理实测雷电流数据，克服了传统频-时变换方法需要解析积分雷电流表达式的限制。

### 数学公式


**公式1**: $$$Z_h(s) = \frac{V_S(s)}{I_S(s)} = \frac{1}{4\pi} \int_{\ell_j} \left( \frac{1}{\sigma_e + s\varepsilon_e} + s\mu_e \right) f_j(\ell_j) G(r_{Sj}) d\ell_j$$$

*接地系统阻抗的定义式，通过矩量法计算，其中$G(r_{Sj})$为半空间导电介质的格林函数，$\sigma_e$、$\varepsilon_e$、$\mu_e$分别为土壤电导率、介电常数和磁导率*


**公式2**: $$$Z_{h,fit}(s) = \sum_{k=1}^{n} \frac{c_k}{s+a_k} + d + sh$$$

*矢量拟合后的有理函数形式，其中$c_k$和$a_k$为留数和极点（实数或共轭复数对），$d$和$h$为实常数*


**公式3**: $$$V_p(s) = Z_h(s) I_p(s)$$$

*频域地电位升(GPR)计算公式，$I_p(s)$为注入的雷电流频域表达式*


**公式4**: $$$v_p(t) = \frac{e^{\psi n\Delta t}}{2\pi j N} \sum_{k=0}^{N-1} V_p(\psi + jk\Delta\omega) \sigma(k\Delta\omega) e^{j2\pi kn/N}$$$

*数值拉普拉斯变换(NLT)的离散形式，用于将频域GPR转换到时域作为参考解，其中$\psi$为人工阻尼系数，$\sigma$为窗函数*


### 算法步骤

1. 使用FEKO软件基于矩量法(MoM)计算接地电极在100 Hz至5 MHz频带内的频域阻抗$Z_h(s)$，电极离散为长度小于$\lambda/10$的线段（$\lambda$为最高频率对应的波长）

2. 应用矢量拟合(VF)技术将离散的阻抗数据拟合为连续的有理函数$Z_{h,fit}(s)$，确保极点为实数或共轭复数对，满足稳定性条件

3. 对于递归卷积法(M1)：利用极点-留数形式构造时域卷积的递归计算公式，通过历史状态变量的递推更新计算当前时刻的GPR，避免存储完整的电流历史数据

4. 对于递归梯形积分法(M2)：采用梯形积分规则离散化卷积积分，结合极点-留数形式建立递归关系，实现高效时域求解

5. 输入雷电流数据（解析表达式或实测离散数据），通过递归公式逐步计算各时间步长的暂态GPR响应

6. 将递归方法计算结果与NLT方法（作为基准）和ATP软件（基于等效电路）的结果进行对比验证


### 关键参数

- **frequency_range**: 100 Hz - 5 MHz

- **soil_conductivity**: $\sigma_e$ (频变或常数)

- **soil_permittivity**: $\varepsilon_e = \varepsilon_0\varepsilon_r$

- **segment_length**: < $\lambda/10$ (矩量法离散)

- **fitting_order**: n (极点数量，根据阻抗曲线复杂度确定)

- **time_step**: $\Delta t$ (递归计算时间步长)

- **damping_coefficient**: $\psi$ (NLT方法人工阻尼系数，通常取$\psi = 1/T$，T为总仿真时间)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 水平接地极（单根导体） | 在电阻率$\rho = 100\ \Omega\cdot m$和$1000\ \Omega\cdot m$的土壤中，分别注入Heidler波形和双指数波形的雷电流，计算得到的GPR峰值与NLT基准结果的偏差小于ATP软件方法 | 递归方法与NLT参考解吻合良好，百分比误差显著低于ATP等效电路方法 |

| 网格接地极（矩形网格） | 针对复杂网格结构（如图1b所示），在频变土壤模型下计算暂态GPR，递归方法成功处理了土壤电离效应和频变参数的影响 | 无需在ATP等软件中搭建复杂等效电路，计算效率优于传统电磁暂态软件建模方法 |



## 量化发现

- 递归方法(M1和M2)计算的GPR波形与数值拉普拉斯变换(NLT)基准结果具有良好的一致性(agreement)
- 与ATP软件相比，递归方法产生的百分比误差(percentage errors)更低
- 频率覆盖范围：接地阻抗计算覆盖100 Hz至5 MHz，涵盖雷电流频谱的主要能量范围
- 空间离散精度：矩量法离散满足$\lambda/10$准则，确保电磁场计算精度
- 矢量拟合精度：有理函数$Z_{h,fit}(s)$在目标频带内与原始阻抗数据$Z_h(s)$的拟合误差可控制在工程精度要求内


## 关键公式

### 矢量拟合有理函数

$$$Z_{h,fit}(s) = \sum_{k=1}^{n} \frac{c_k}{s+a_k} + d + sh$$$

*将频域接地阻抗拟合为极点-留数形式，是递归时域计算的基础*

### 接地阻抗积分方程

$$$Z_h(s) = \frac{1}{4\pi} \int_{\ell_j} \left( \frac{1}{\sigma_e + s\varepsilon_e} + s\mu_e \right) f_j(\ell_j) G(r_{Sj}) d\ell_j$$$

*基于矩量法的频域接地阻抗计算，考虑土壤频率相关参数*



## 验证详情

- **验证方式**: 对比验证：与数值拉普拉斯变换(NLT)结果（作为参考基准）和ATP-EMTP软件（基于等效电路）进行定量对比
- **测试系统**: 测试系统包括：(1)水平接地极（长度L，半径a，埋深H）；(2)矩形网格接地极（3D mesh结构）。土壤条件涵盖电阻率$100-1000\ \Omega\cdot m$，考虑频率无关和频率相关土壤模型
- **仿真工具**: FEKO（基于MoM计算频域阻抗）、MATLAB/FORTRAN（实现递归算法M1和M2）、ATP-EMTP（等效电路仿真）、NLT算法（频-时变换参考解）
- **验证结果**: 递归卷积法(M1)和递归梯形积分法(M2)在各种测试场景下均与NLT参考解吻合良好，验证了算法的准确性；同时证明递归方法在处理实测雷电流数据（无解析表达式）时具有优势，且避免了在EMT软件中搭建复杂等效电路的需求
