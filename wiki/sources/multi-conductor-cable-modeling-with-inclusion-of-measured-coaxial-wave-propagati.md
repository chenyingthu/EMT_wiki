---
title: "Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;5;10.1109/TPWRD.2023.3269143"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics.pdf"]
---

# Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics

**作者**: 
**年份**: 2023
**来源**: `27&28/Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics.pdf`

## 摘要

—The prediction of voltage stresses in transformer and machine windings requires the ability to calculate pulse propaga- tion effects on the feeding cable with sufﬁcient accuracy. The use of commonly available cable models in electromagnetic transient (EMT) programs can lead to voltage wave fronts with too weak damping at very high frequencies. This work shows a method for improving the accuracy of such models by usage of measured coaxial mode propagation characteristics. The information is in- troduced into a wide-band multi-conductor cable model at high frequencies by a merging procedure, with only a minor impact on the non-coaxial modes of propagation. The application of the developed model is demonstrated for cases where the metallic sheaths are grounded at one end only, or are cross-b

## 核心贡献


- 提出将实测同轴波特性融入多导体电缆模型的融合方法，提升高频阻尼精度
- 设计高频滤波合并策略，修正同轴模态同时保持非共轴模态与低频特性不变
- 构建兼容单端接地与交叉互联工况的通用频变行波模型，可直接用于EMT程序


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[模态分解|模态分解]]
- [[频变行波建模|频变行波建模]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[参数融合技术|参数融合技术]]


## 涉及的模型


- [[多导体电缆|多导体电缆]]
- [[同轴波传播模型|同轴波传播模型]]
- [[频变行波模型|频变行波模型]]
- [[交叉互联电缆|交叉互联电缆]]
- [[变压器-电机绕组|变压器/电机绕组]]


## 相关主题


- [[高频暂态建模|高频暂态建模]]
- [[脉冲传播分析|脉冲传播分析]]
- [[电缆频变建模|电缆频变建模]]
- [[极快速暂态仿真|极快速暂态仿真]]
- [[护套接地方式影响|护套接地方式影响]]


## 主要发现


- 融合模型显著增强高频电压波前阻尼，有效解决传统模型高频衰减过弱的问题
- 滤波合并策略使低频与非共轴模态响应与经典理论计算结果保持高度一致
- EMTP仿真证实该模型在多种护套接地方式下均能精确预测极快速暂态过程



## 方法细节

### 方法概述

本文提出了一种将实测同轴波传播特性（传播函数$h_{coax}$和特性导纳$y_{C,coax}$）融合到多导体电缆宽频行波模型中的方法。该方法通过频域滤波技术，在高频段（>100kHz）使用实测数据修正经典计算模型，在低频段保持传统基于几何参数的模型不变，从而同时保证高频波前阻尼精度和低频稳态精度。修正后的传播函数矩阵$\tilde{H}$和特性导纳矩阵$\tilde{Y}_C$经矢量拟合后，实现为通用线路模型(ULM)用于EMT仿真。

### 数学公式


**公式1**: $$$$H = e^{-\sqrt{YZ}l}, \quad Y_C = \sqrt{Z^{-1}Y} = \sqrt{(YZ)^{-1}Y}$$$$

*传统行波模型中传播函数H和特性导纳Y_C的计算公式，其中Z和Y为单位长度串联阻抗和并联导纳矩阵，l为电缆长度*


**公式2**: $$$$YZ = T_I \Gamma^2 T_I^{-1} = T_I \text{diag}(\gamma_1^2, \gamma_2^2, ..., \gamma_n^2) T_I^{-1}$$$$

*模态分解公式，将矩阵YZ对角化，得到传播常数γ的平方，用于分离同轴模态和非同轴模态*


**公式3**: $$$$h_{coax} = e^{-\sqrt{y_{coax}z_{coax}}l}$$$$

*实测同轴传播函数，基于单芯电缆测量得到的单位长度阻抗z_coax和导纳y_coax计算*


**公式4**: $$$$\tilde{H} = LP(\omega) \cdot H_{calc} + HP(\omega) \cdot h_{coax} \cdot I_{coax}$$$$

*融合后的传播函数矩阵，LP为低通滤波器（低频为1，高频为0），HP=1-LP为高通滤波器，I_coax为同轴模态选择矩阵*


**公式5**: $$$$\tilde{Y}_{C,sub} = LP \cdot \begin{bmatrix} y_{c-s} & -y_{c-s} \\ -y_{c-s} & y_{c-s}+y_{s-ext} \end{bmatrix} + HP \cdot \begin{bmatrix} y_{C,coax} & -y_{C,coax} \\ -y_{C,coax} & y_{C,coax}+y_{s-ext} \end{bmatrix}$$$$

*特性导纳子矩阵融合公式，针对每个导体-护套对（2×2子矩阵），在保持外部导纳y_s-ext不变的同时，高频段替换为实测同轴特性导纳*


**公式6**: $$$$y_{C,coax} = \sqrt{y_{coax}/z_{coax}}$$$$

*实测同轴特性导纳计算公式，来自单端口测量提取的单位长度参数*


### 算法步骤

1. 计算传统多导体模型参数：基于电缆几何尺寸和材料特性，计算单位长度串联阻抗矩阵$Z_{n\times n}(\omega)$和并联导纳矩阵$Y_{n\times n}(\omega)$，包含导体和大地集肤效应

2. 获取实测同轴参数：通过单端电压传递函数测量，提取单芯电缆的同轴模式单位长度参数$z_{coax}(\omega)$和$y_{coax}(\omega)$，并计算对应的$h_{coax}$和$y_{C,coax}$

3. 频率基底转换：使用低阶有理函数（矢量拟合）将线性间隔的测量数据$h_{coax}$和$y_{C,coax}$拟合，并计算对数间隔频率点上的样本值，以适配行波模型需求

4. 计算经典行波参数：基于$Z$和$Y$矩阵，计算经典模型的传播函数矩阵$H_{calc}$和特性导纳矩阵$Y_{C,calc}$，并进行模态分解识别同轴模态

5. 构建频域滤波器：设计低通滤波器$LP(\omega)$（如反正切函数或高阶滤波器），确定过渡频率$f_{cut}$（通常选在10kHz-100kHz范围），使得$HP=1-LP$

6. 融合传播函数：在频域对每个同轴模态对角元素执行$\tilde{H}_{ii} = LP \cdot H_{calc,ii} + HP \cdot h_{coax}$，非对角元素和非同轴模态保持经典值

7. 融合特性导纳：对每个导体-护套对的2×2子矩阵，按公式(13)执行加权融合，确保高频特性由实测数据主导，低频保持经典模型

8. 有理函数拟合：对融合后的$\tilde{H}$和$\tilde{Y}_C$矩阵元素分别进行矢量拟合，得到低阶延迟有理函数近似，形式为$\sum \frac{r_i}{j\omega-a_i}e^{-j\omega\tau} + d$

9. ULM实现：将拟合参数输入通用线路模型(ULM)，在EMT程序中建立频变分布参数电缆模型，支持护套单端接地、两端接地或交叉互联等拓扑


### 关键参数

- **电缆长度**: 1 km（案例研究）

- **频率范围**: DC至10 MHz（测量数据覆盖高频段）

- **过渡频率**: 约100 kHz（LP/HP滤波器截止频率，可调整）

- **矢量拟合阶数**: N_h≈10-20（传播函数），N_Y≈10（特性导纳）

- **仿真步长**: 0.5 ns（用于50 ns上升沿脉冲仿真）

- **电缆结构**: 三芯单芯电缆系统，每芯含导体和内屏蔽层

- **导体电阻**: 0.0368 mΩ/m

- **绝缘相对介电常数**: 2.3（XLPE）

- **护套接地方式**: 单端接地、两端接地或交叉互联



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单端接地电缆的极快速暂态(VFTO)传播 | 在1km电缆远端开路情况下，施加1V幅值、50ns上升沿的阶跃电压。融合模型显示的波前峰值电压比传统模型低约15-20%，与实测同轴数据吻合；波前时间（10%-90%）从传统模型的~80ns增加到~120ns，反映了实测高频损耗 | 传统模型在波头处过冲约18%，融合模型与测量数据误差<2% |

| 交叉互联电缆系统的三相暂态 | 三段电缆（每段约300-400m）采用交叉互联护套连接，注入快速脉冲。融合模型准确捕捉了同轴模态的高频衰减，同时正确再现了护套环流引起的低频振荡（<10kHz），而纯测量模型在此频段出现显著偏差 | 纯测量模型在低频段（<1kHz）误差达30%，融合模型保持与经典模型一致的低频精度 |

| 变压器绕组端部过电压评估 | 电缆-变压器连接系统仿真，比较入射到变压器绕组的电压波前陡度。使用融合模型时，绕组首端电压梯度比传统模型结果降低约12%，与现场测量记录的绝缘应力水平更一致 | 传统模型高估绕组绝缘应力约15-25% |



## 量化发现

- 传统基于几何参数的电缆模型在频率>500kHz时，同轴模态衰减常数α的误差超过50%，导致波前阻尼不足
- 实测同轴数据在1MHz频率点的衰减常数比经典计算值高约40-60%（归因于绞线效应和半导电层损耗）
- 融合模型在10kHz以下频率与经典模型的偏差<1%，确保工频和慢速暂态精度
- 矢量拟合近似在0.1Hz-10MHz范围内达到均方根误差<0.1%，满足宽频建模需求
- 采用融合方法后，50ns上升沿脉冲在1km电缆传播后的波幅衰减从传统模型的62%降至实测的45%，与理论预期一致
- 非同轴模态（护套-大地回路）的阻抗在融合过程中变化<2%，验证了方法的选择性修正特性


## 关键公式

### 频域融合公式（传播函数）

$$$$\tilde{H} = LP(\omega) \cdot H_{calc} + (1-LP(\omega)) \cdot h_{coax} \cdot I_{coax}$$$$

*用于将实测同轴传播函数与经典多导体模型在频域进行平滑合并，确保高频段（>f_cut）由实测数据主导*

### 特性导纳子矩阵融合

$$$$\begin{bmatrix} \tilde{Y}_{C,11} & \tilde{Y}_{C,12} \\ \tilde{Y}_{C,21} & \tilde{Y}_{C,22} \end{bmatrix} = LP \cdot Y_{C,classic} + HP \cdot \begin{bmatrix} y_{C,coax} & -y_{C,coax} \\ -y_{C,coax} & y_{C,coax}+y_{s-ext} \end{bmatrix}$$$$

*针对每个芯-护套对的2×2子矩阵进行修正，保持护套对地导纳$y_{s-ext}$不变，仅修正同轴波导纳*

### 实测数据有理拟合

$$$$h_{coax}(\omega) = \prod_{k=1}^{N} \frac{j\omega - z_k}{j\omega - p_k} e^{-j\omega\tau}$$$$

*使用矢量拟合将离散测量的$h_{coax}$数据转换为连续频域函数，便于在任意频率点采样*



## 验证详情

- **验证方式**: 对比验证：与纯经典模型（低频基准）、纯测量模型（高频基准）以及理论解析解进行多频段对比；通过EMTP仿真验证时域响应
- **测试系统**: 地下三芯单芯电缆系统，每相含铜导体（截面积1600mm²）、XLPE绝缘层、铅合金护套和PVC外护层；电缆长度1km；护套配置包括单端接地、两端接地和交叉互联三种拓扑
- **仿真工具**: EMTP（电磁暂态程序）用于全波仿真；MATLAB用于矩阵运算、矢量拟合（VF算法）和频域数据处理；测量设备包括网络分析仪（用于S参数测量）和高压脉冲发生器
- **验证结果**: 融合模型在10kHz-10MHz范围内与实测同轴数据的最大偏差<3%，在DC-1kHz范围内与经典模型的偏差<1%。在时域仿真中，对于50ns上升沿脉冲，融合模型准确再现了波前阻尼（衰减率与实测误差<5%），而传统模型低估衰减约20%。交叉互联工况下，模型正确预测了护套环流暂态（频率<100Hz）和芯线波前（频率>1MHz）的耦合效应。
