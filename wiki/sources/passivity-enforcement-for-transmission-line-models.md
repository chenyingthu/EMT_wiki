---
title: "Passivity Enforcement for Transmission Line Models"
type: source
authors: ['未知']
year: 2008
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2008.919034.pdf.pdf"]
---

# Passivity Enforcement for Transmission Line Models

**作者**: 
**年份**: 2008
**来源**: `31/TPWRD.2008.919034.pdf.pdf`

## 摘要

—The Universal Line Model (ULM) has been imple- mented in several EMT programs for simulation of electromag- netic transients. In some cases, instability problems have been encountered. This paper shows that the current approach for ra- tional function approximation adopted in ULM can lead to large out-of-band passivity violations, thereby causing an unstable sim- ulation. An approach is introduced which prevents the occurrence of large passivity violations. Low-frequency violations are avoided by adding an artiﬁcial shunt conductance to the diagonal elements of the shunt admittance matrix while high-frequency violations are avoided by introducing artiﬁcial attenuation using a low-pass ﬁlter. In addition, high-frequency asymptotic passivity is enforced for the characteristic admittance. An

## 核心贡献


- 提出在并联导纳矩阵对角线添加人工电导，消除低频无源性违规
- 引入低通滤波器与高频渐近无源性约束，抑制高频无源性违规
- 通过端口二阶校正项消除剩余违规，保障EMT仿真稳定性


## 使用的方法


- [[特征线法|特征线法]]
- [[矢量拟合|矢量拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[迹拟合|迹拟合]]
- [[低通滤波|低通滤波]]
- [[无源性强制|无源性强制]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[输电线路|输电线路]]
- [[电缆系统|电缆系统]]
- [[频变线路模型|频变线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[无源性强制|无源性强制]]
- [[频变建模|频变建模]]
- [[仿真稳定性|仿真稳定性]]
- [[有理逼近|有理逼近]]


## 主要发现


- 传统ULM有理逼近易引发带外无源性违规，导致仿真发散
- 所提方法有效消除电缆系统仿真中的数值不稳定现象
- 校正后模型在宽频带内保持高精度，未牺牲原有仿真质量



## 方法细节

### 方法概述

本文提出了一种针对通用线路模型(ULM)的无源性强制方法，用于解决因带外(out-of-band)有理函数逼近误差导致的数值不稳定问题。该方法采用三层防御策略：首先，在低频段，通过对并联导纳矩阵对角线元素添加人工并联电导(artificial shunt conductance)来消除直流附近的无源性违规，确保特性导纳在直流处非零；其次，在高频段，通过引入二阶低通滤波器产生人工衰减，并强制执行特性导纳的高频渐近无源性条件；最后，对于残余的带内无源性违规，采用基于模态分解的二阶校正项(second-order correction term)进行端口补偿。该方法确保了在宽频带内模型的无源性，从而保证EMT仿真的数值稳定性。

### 数学公式


**公式1**: $$$$Y_c = \sqrt{Y/Z}$$$$

*特性导纳矩阵计算公式，由单位长度并联导纳矩阵Y和串联阻抗矩阵Z计算得到*


**公式2**: $$$$H = e^{-\sqrt{ZY}\cdot l}$$$$

*传播函数矩阵，l为线路长度*


**公式3**: $$$$\text{trace}(Y_c) = \sum_{m=1}^{N} \frac{r_m}{s-a_m} + d + se$$$$

*基于矢量拟合的迹拟合公式，用于确定极点集*


**公式4**: $$$$Y_c = \sum_{m=1}^{N} \frac{R_m}{s-a_m} + D + sE$$$$

*相域中的有理函数拟合，在迹拟合确定的极点基础上计算留数矩阵*


**公式5**: $$$$Y_{mod} = Y + G_{add}, \quad G_{add} = \text{diag}(g_{add})$$$$

*修改后的并联导纳矩阵，通过对角线添加人工电导消除低频违规*


**公式6**: $$$$R_{add} = \tau/C, \quad \tau = 1\text{s}$$$$

*人工电导计算公式，基于预定时间常数(1秒)和电容参数*


**公式7**: $$$$f_0 = \frac{1}{2\pi\tau} = 0.159\text{Hz}$$$$

*由时间常数决定的零点频率，用于确定拟合下边界*


**公式8**: $$$$Y_c(\infty) = D = |Y_c(j\omega_{high})|, \quad \omega_{high} \gg \omega_{max}$$$$

*高频渐近无源性强制条件，确保有理模型在无限频率处为正实数*


**公式9**: $$$$F_{lp}(s) = \frac{1}{(1+s/\omega_1)(1+s/\omega_2)}, \quad \omega_1 = 2\pi \cdot 10^7 \text{rad/s}$$$$

*二阶低通滤波器传递函数，截止频率位于拟合上界一个数量级以上(约1.6MHz)*


**公式10**: $$$$Y_{nodal} = Y_c(I+H)^{-1}(I-H)$$$$

*节点导纳矩阵计算公式，用于无源性检查*


**公式11**: $$$$\lambda(\text{real}(Y_{nodal} + Y_{nodal}^H)) \geq 0$$$$

*无源性判定条件，要求Hermitian部分的特征值非负*


**公式12**: $$$$\Delta Y(s) = \frac{R_1}{s-a_1} + \frac{R_2}{s-a_2}$$$$

*二阶校正项，以极点-留数形式表示，用于消除残余违规*


### 算法步骤

1. 计算单位长度电缆参数(串联阻抗Z和并联导纳Y)，基于电缆几何结构和材料特性

2. 低频处理：计算人工并联电导 $G_{add} = C/\tau$ (其中$\tau=1$s)，添加到Y矩阵对角线，确保$Y_c$在直流处非零

3. 确定修正后的有理拟合频带：下边界取为 $f_{low} = 1/(2\pi\tau) \approx 0.16$ Hz，上边界根据需求设定

4. 高频渐近处理：计算高频渐近值 $D = |Y_c(j\omega_{high})|$，强制作为有理逼近的常数项，确保高频无源性

5. 传播函数处理：将低通滤波器$F_{lp}(s)$与传播函数H及其模态相乘，引入人工衰减，抑制高频违规

6. 执行矢量拟合(VF)：对迹进行拟合获得极点，对相域进行最终拟合获得留数矩阵

7. 构建节点导纳矩阵 $Y_{nodal} = Y_c(I+H)^{-1}(I-H)$，在宽频带内检查无源性

8. 残余违规校正：若存在特征值为负的频率点，计算校正矩阵$\Delta Y = -V_{neg}\Lambda_{neg}V_{neg}^T$，并通过带通滤波器限制校正带宽

9. 迭代优化：使用因子1.1放大校正量，重复检查直至所有特征值非负，确保模型完全无源

10. 将最终模型参数(极点、留数、延时)导出至EMT仿真环境(PSCAD/EMTDC)进行暂态仿真


### 关键参数

- **低频时间常数**: $\tau = 1$ s

- **人工电导计算公式**: $G_{add} = C/\tau$

- **零点频率**: $f_0 = 0.159$ Hz

- **低通滤波器截止频率**: $f_c = 10^7$ Hz (10 MHz，对应$\omega_1 = 2\pi \times 10^7$ rad/s)

- **滤波器阻尼系数**: $\zeta > 1$ (过阻尼，避免双极点)

- **拟合频带扩展**: 上界扩展一个数量级以捕捉滤波器特性

- **校正迭代因子**: $\alpha = 1.1$

- **校正极点位置**: 分别位于$f_{low}/10$和$10f_{high}$

- **电缆长度**: 1000 m

- **电缆电压等级**: 145 kV



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三芯同轴电缆系统暂态仿真 | 采用三根145kV单芯同轴电缆，长度1000m，使用原始ULM建模方法时出现数值发散，采用本文方法后仿真稳定。传播函数H的六个模态被聚合为四个模态进行拟合，在宽频带(包含高频段)内保持了无源性 | 原始ULM方法导致仿真不稳定(unstable simulation)，本文方法消除了不稳定性，且未损害模型精度 |



## 量化发现

- 人工电导引入的时间常数取值为1秒，对应零点频率0.159 Hz
- 低通滤波器截止频率设置为$10^7$ Hz (10 MHz)，比典型拟合上界(约1 MHz)高一个数量级
- 校正算法中使用1.1倍的放大因子确保收敛，通常只需少量迭代即可消除残余违规
- 对于电缆系统，原始ULM方法在带外(out-of-band)产生大的无源性违规，导致特征值实部为负
- 通过添加人工电导，特性导纳在直流处的极限值从0变为非零值$\sqrt{G_{add}/R}$
- 高频渐近处理确保当$s \to \infty$时，$Y_c(s) \to D > 0$，满足正实条件


## 关键公式

### 节点导纳矩阵

$$$$Y_{nodal} = Y_c(I+H)^{-1}(I-H)$$$$

*用于无源性检查和校正，在频域内计算线路的等效节点导纳*

### 低频电导计算

$$$$R_{add} = \frac{\tau}{C}, \quad f_0 = \frac{1}{2\pi\tau} = 0.159\text{Hz}$$$$

*确定人工并联电导值，确保直流处特性导纳非零，消除低频无源性违规*

### 低通滤波器

$$$$F_{lp}(s) = \frac{1}{(1+s/\omega_1)(1+s/\omega_2)}, \quad \omega_1 = 2\pi \cdot 10^7$$$$

*引入人工衰减以抑制高频无源性违规，截止频率位于$10^7$ Hz*

### 高频渐近约束

$$$$D = |Y_c(j\omega_{high})|$$$$

*强制执行特性导纳的高频渐近无源性，确保有理模型在无限频率处为正实数*



## 验证详情

- **验证方式**: 仿真验证，对比分析原始ULM方法与改进方法的稳定性
- **测试系统**: 三根单芯同轴电缆系统，145kV电压等级，电缆长度1000m，几何参数包括导体半径、绝缘层厚度、护套半径等详细数据
- **仿真工具**: MATLAB用于计算单位长度参数和有理函数拟合(矢量拟合)，PSCAD/EMTDC用于电磁暂态仿真验证
- **验证结果**: 在电缆系统暂态仿真中，原始ULM方法因带外无源性违规导致数值不稳定，本文提出的三重防御策略(低频电导、高频滤波、端口校正)成功消除了仿真发散现象，同时保持了模型在目标频带内的精度，未对仿真质量产生负面影响
