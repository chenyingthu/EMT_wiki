---
title: "Application of Frequency-Partitioning Fitting to the Phase-Domain Frequency-Dependent Modeling of Overhead Transmission Lines"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Transactions on Power Delivery;2015;30;1;10.1109/TPWRD.2014.2329532"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/09/Noda - 2015 - Application of frequency-partitioning fitting to the phase-domain frequency-dependent modeling of ov.pdf"]
---

# Application of Frequency-Partitioning Fitting to the Phase-Domain Frequency-Dependent Modeling of Overhead Transmission Lines

**作者**: 
**年份**: 2015
**来源**: `09/Noda - 2015 - Application of frequency-partitioning fitting to the phase-domain frequency-dependent modeling of ov.pdf`

## 摘要

—This paper shows that a previously proposed linear-system identiﬁcation method based on frequency parti- tioning and adaptive weighting can be successfully applied to the phase-domain frequency-dependent modeling of overhead transmission lines for electromagnetic transient simulations. As the framework of the phase-domain modeling, the universal line model is used, and the frequency responses of the characteristic admittance and propagation function matrices are realized by linear equivalents obtained by the identiﬁcation method men- tioned before, instead of the well-known Vector Fitting method.

## 核心贡献


- 提出将频域分区拟合应用于架空线路相域频变建模，替代传统矢量拟合法
- 改进频域分区拟合数值技术，提升特征导纳与传播函数矩阵的拟合精度
- 将改进算法与通用线路模型结合，实现高效精确的电磁暂态仿真


## 使用的方法


- [[频域分区拟合|频域分区拟合]]
- [[矢量拟合|矢量拟合]]
- [[通用线路模型|通用线路模型]]
- [[矩阵部分分式展开|矩阵部分分式展开]]
- [[相域建模|相域建模]]
- [[transmission-line-model|Bergeron线路模型]]
- [[梯形积分法|梯形积分法]]
- [[numerical-integration|数值积分]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[500kv双回输电线路|500kV双回输电线路]]
- [[特征导纳矩阵|特征导纳矩阵]]
- [[传播函数矩阵|传播函数矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[相域建模|相域建模]]
- [[线性系统辨识|线性系统辨识]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 频域分区拟合有效克服了传统有理函数拟合的病态问题，提升数值稳定性
- 基于该方法的暂态波形与严格拉普拉斯变换法及现场实测结果高度吻合
- 改进的数值技术显著提高了500kV线路特征导纳与传播函数的拟合精度



## 方法细节

### 方法概述

本文提出将频域分区拟合（FpF）方法应用于相域频变架空输电线路建模，以替代传统的矢量拟合（VF）法。该方法基于通用线路模型（ULM）框架，直接在相域处理特征导纳矩阵$Y_c$和传播函数矩阵$H$的频率响应。核心流程包括：首先利用Carson公式计算线路频域参数；随后采用混合误差评估策略（大信号用相对误差、近零信号用绝对误差）进行频域分区，在各子区间内独立辨识极点；针对传播函数矩阵，显式提取模态行波时延并设定拟合上限频率以剔除冗余极点；引入基于采样定理的理论低通滤波器抑制高频数值振荡；最后利用奇异值分解（SVD）求解病态最小二乘问题以获取留数矩阵，最终通过梯形积分法将矩阵部分分式展开（MPFE）转化为时域递归历史电流源，实现高效稳定的EMT仿真。

### 数学公式


**公式1**: $$$Y_c(s) \approx D + \sum_{k=1}^{N} \frac{R_k}{s - p_k}$$$

*特征导纳矩阵的标准矩阵部分分式展开（MPFE）形式，用于时域卷积计算。*


**公式2**: $$$H(s) \approx \sum_{m=1}^{M} e^{-s\tau_m} \left( D_m + \sum_{k=1}^{N_m} \frac{R_{m,k}}{s - p_{m,k}} \right)$$$

*通用线路模型（ULM）中传播函数矩阵的修正MPFE形式，显式包含各模态行波时延$\tau_m$。*


**公式3**: $$$w_i = \begin{cases} 1/|y_i|, & |y_i| > \epsilon \\ 1/\epsilon, & |y_i| \le \epsilon \end{cases}$$$

*混合加权函数，对幅值大于阈值$\epsilon$的频点采用相对误差评估，小于等于阈值的采用绝对误差评估，防止近零区域误差被过度放大。*


**公式4**: $$$F(s) = \frac{1}{1 + s \Delta t / \pi}$$$

*理论一阶低通滤波器，截止频率由EMT仿真步长$\Delta t$决定，用于抑制高频尖峰电压的数值放大。*


**公式5**: $$$\boldsymbol{x} = \boldsymbol{V}_r \boldsymbol{\Sigma}_r^{-1} \boldsymbol{U}_r^T \boldsymbol{b}$$$

*基于SVD截断的最小二乘解，剔除归一化奇异值低于机器精度的低贡献方程，确保留数矩阵辨识的数值稳定性。*


### 算法步骤

1. 频域参数计算：基于Carson和Schelkunoff公式计算线路阻抗矩阵$Z$和导纳矩阵$Y$，进而求得特征导纳矩阵$Y_c$和传播函数矩阵$H$在离散频点上的频率响应。

2. 混合加权与频域分区：设定阈值$\epsilon$，对幅值大于$\epsilon$的频点采用相对误差加权，小于等于$\epsilon$的采用绝对误差加权；将全频带划分为若干子区间，在各子区间内独立进行有理函数拟合以提取左半平面稳定极点。

3. 传播函数时延提取与极点筛选：对$H$进行模态分解，提取各模态行波时延$\tau_m$；设定上限频率$\omega_{max}$（基于阈值$\epsilon_H$），剔除振荡频率高于$\omega_{max}$的极点，避免高频无意义响应增加计算负担。

4. 理论低通滤波：根据仿真步长$\Delta t$确定奈奎斯特频率，对$H$的频响乘以一阶低通滤波器$1/(1+s\Delta t/\pi)$，抑制因模态时差引起的高频尖峰电压在时域反复反射导致的数值发散。

5. SVD留数辨识：构建超定线性方程组，进行奇异值分解；剔除归一化奇异值低于机器精度阈值的低贡献方程，求解截断后的最小二乘问题，获得各极点的留数矩阵。

6. 时域递归实现：利用梯形积分法将MPFE转化为瞬时电导矩阵与历史电流源，嵌入EMT仿真网络方程进行迭代求解，实现全相域频变线路的实时仿真。


### 关键参数

- **epsilon**: 1e-4（混合加权阈值）

- **epsilon_H**: 1e-3（传播函数上限频率判定阈值）

- **alpha**: 2（频域分区自适应权重参数）

- **dt_validation**: 0.5 μs（暂态验证仿真步长）

- **dt_filter_test**: 2 μs（滤波效果测试步长）

- **mode_time_diff_threshold**: 1%（模态时差大于此值视为独立模态）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 500kV双回线路阶跃响应滤波对比 | 在步长2 μs下对线路施加阶跃电压。未加滤波时，模态时差产生的尖峰电压在两端反复反射并累积，导致仿真发散；加入理论低通滤波器后，尖峰电压随传播逐渐衰减，波形稳定收敛。 | 滤波模型成功抑制数值放大，未滤波模型在相同步长下完全发散；当步长增大至10 μs时滤波模型仍出现轻微放大，表明步长需小于模态时差（14.2 μs）。 |

| 现场冲击试验与拉普拉斯法对比 | 在加贺-岭南线中点P点注入冲击电压，两端经50 Ω电阻接地。FpF模型在0.5 μs步长下计算的全相暂态电压波形与严格数值拉普拉斯变换法完全重合，且与现场实测波形在微秒至毫秒级响应高度一致。 | 与VF法相比，在相近拟合精度下FpF极点数为40（VF为28-32），但FpF无需迭代调参，且通过SVD和滤波技术实现了更高的数值鲁棒性。 |



## 量化发现

- 混合加权算法使$Y_c$矩阵拟合的最大绝对偏差降至$1.2 \times 10^{-3}$，显著抑制了近零幅值区的误差放大。
- 设定上限频率$\omega_{max}$后，传播函数矩阵各模态拟合所需极点数量平均减少约15%-20%，且保持相同拟合精度。
- SVD截断算法成功处理了36个矩阵元素中30个出现的病态奇异值（小于$10^{-15}$），避免了传统QR分解导致的计算失败。
- FpF模型全频段输入导纳矩阵实部特征值均严格大于0，满足无源性条件，确保时域仿真绝对稳定。
- 在保守参数设置下，FpF拟合极点数为40；若将拟合容差参数$\delta$调整为0.05，极点数可进一步降至33，计算效率提升约17%。


## 关键公式

### 含时延的传播函数MPFE

$$$H(s) \approx \sum_{m=1}^{M} e^{-s\tau_m} \left( D_m + \sum_{k=1}^{N_m} \frac{R_{m,k}}{s - p_{m,k}} \right)$$$

*用于相域通用线路模型（ULM）中，显式分离模态行波时延，解决传统MPFE无法准确表征阶跃型时域响应的问题。*

### 混合误差加权函数

$$$w_i = \begin{cases} 1/|y_i|, & |y_i| > \epsilon \\ 1/\epsilon, & |y_i| \le \epsilon \end{cases}$$$

*在留数矩阵最小二乘辨识过程中使用，平衡大信号相对精度与小信号绝对精度，防止病态加权。*

### 理论低通滤波器

$$$F(s) = \frac{1}{1 + s \Delta t / \pi}$$$

*在$H$矩阵留数辨识前乘以频响，截止频率由仿真步长决定，用于物理抑制高频数值振荡。*

### SVD截断最小二乘解

$$$\boldsymbol{x} = \boldsymbol{V}_r \boldsymbol{\Sigma}_r^{-1} \boldsymbol{U}_r^T \boldsymbol{b}$$$

*当系数矩阵条件数过大导致常规求解失败时，通过剔除低贡献奇异值方程获得稳定数值解。*



## 验证详情

- **验证方式**: EMT时域仿真 + 严格数值拉普拉斯变换法对比 + 现场冲击试验实测数据验证
- **测试系统**: 日本500kV双回架空输电线路（加贺-岭南线），全长约100km级，中点P点注入冲击电压，两端经50 Ω电阻接地模拟母线波阻抗。
- **仿真工具**: 作者自研EMT仿真程序（与EMTP-RV内置VF模块进行对比），结合Carson公式频域计算与自定义FpF拟合算法。
- **验证结果**: FpF相域模型在微秒至毫秒级暂态过程中与拉普拉斯变换法误差可忽略，与现场实测波形高度吻合；模型严格满足无源性，数值稳定性显著优于未滤波传统方法，验证了频域分区拟合在复杂频变线路建模中的工程适用性与高精度特性。
