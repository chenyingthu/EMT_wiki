---
title: "Robust Passivity Enforcement Scheme for"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/34/tpwrd.2009.2035916.pdf.pdf"]
---

# Robust Passivity Enforcement Scheme for

**作者**: 
**年份**: 2010
**来源**: `34/tpwrd.2009.2035916.pdf.pdf`

## 摘要

—This paper proposes an algorithm to enforce passivity on the time-domain simulation model for a multi-conductor cable or transmission line. The model is ﬁrst reformulated in a form which reduces the severity of passivity violations. The frequency sweep method is then used to identify any remaining passivity violating regions of the model’s frequency response. These small passivity violations are then removed using a linear constrained least squares algorithm to perturb the diagonal elements of propagation matrix. The passivity enforcement algorithm is ap- plied to the Universal Line Model (ULM), a widely used robust phase domain formulation implemented in many commercial electromagnetic transients simulation programs. Two examples of multi-conductor underground cable systems, one for ac a

## 核心贡献



- 提出了一种针对多导体电缆与输电线路时域仿真模型的鲁棒无源性强制算法
- 通过线性约束最小二乘法扰动传播矩阵对角元素，有效消除曲线拟合模型中的无源性违规，并成功集成于通用线路模型(ULM)

## 使用的方法


- [[passivity]]
- [[vector-fitting]]
- [[frequency-dependent]]

## 涉及的模型


- [[transmission-line]]
- [[cable]]

## 相关主题


- [[hvdc]]
- [[passivity]]

## 主要发现



- 所提算法能有效识别并消除多导体线路时域模型中的无源性违规，避免非物理能量生成导致的仿真数值不稳定
- 在交流与高压直流(HVDC)地下电缆系统中的应用验证表明，该方法在保证计算效率的同时显著提升了电磁暂态仿真的鲁棒性与准确性

## 方法细节

### 方法概述

该论文提出了一种两阶段鲁棒无源性强制算法，专门针对多导体电缆和输电线路的时域仿真模型。第一阶段采用修改的函数形式方法（modified functional form method）重新表述传输线的特征导纳和传播函数，通过改进有理函数拟合的数学形式从根本上降低无源性违规的严重程度。第二阶段首先使用频率扫描法（frequency sweep method）在宽频带内（0 Hz至10 MHz）以精细步长扫描识别剩余的无源性违规区域，特别是标记特征值接近零的可疑频段进行局部细化扫描；随后采用线性约束最小二乘算法（linear constrained least squares）对传播矩阵的对角元素引入微小扰动，在保持模型整体精度的同时消除无源性违规，确保传递导纳矩阵H(s)在所有频率下均为正定。该方法适用于相位域模型（phase domain model），特别是基于ULM（Universal Line Model）的 formulations，不局限于常数变换矩阵的模态域方法。

### 数学公式


**公式1**: $$$V_s = Z_c I_s + A(V_r + Z_c I_r)$$$

*多导体传输线频域方程，描述送端电压与电流、受端电压电流的关系，其中Zc为特征阻抗矩阵，A为传播矩阵*


**公式2**: $$$V_r = Z_c I_r + A(V_s + Z_c I_s)$$$

*对应的受端电压方程，与送端方程构成传输线的双端口网络表示*


**公式3**: $$$Z_c = \sqrt{Z/Y}$$$

*特征阻抗矩阵定义，由单位长度串联阻抗矩阵Z和并联导纳矩阵Y计算得到*


**公式4**: $$$A = e^{-\sqrt{ZY} \cdot l}$$$

*传播矩阵定义，l为线路长度，包含信号的衰减和相位变化*


**公式5**: $$$Y_c \approx \sum_{k=1}^{N} \frac{R_k}{s-p_k} + D + sE$$$

*特征导纳矩阵Yc的有理函数近似（矢量拟合），Rk为留数，pk为极点，D和E为实数矩阵*


**公式6**: $$$A \approx e^{-s\tau} \cdot \sum_{k=1}^{N} \frac{R_k}{s-p_k}$$$

*传播矩阵A的传统有理函数近似形式，包含时延τ和有理函数部分*


**公式7**: $$$A \approx \sum_{m=1}^{M} e^{-s\tau_m} \cdot \sum_{k=1}^{N_m} \frac{R_{m,k}}{s-p_{m,k}}$$$

*ULM采用的修改形式，考虑多模态时延τm，每个模态对应一组极点和留数，减少对角元素拟合误差*


**公式8**: $$$\begin{bmatrix} I_s \\ -I_r \end{bmatrix} = H(s) \begin{bmatrix} V_s \\ V_r \end{bmatrix}$$$

*多端口网络表示，H(s)为传递导纳矩阵，将线路两端电压映射到电流*


**公式9**: $$$H(s) = Y_c \begin{bmatrix} (I-A^2)^{-1} & -(I-A^2)^{-1}A \\ -(I-A^2)^{-1}A & (I-A^2)^{-1} \end{bmatrix}$$$

*传递导纳矩阵的显式表达式，基于特征导纳和传播矩阵计算，用于无源性检验*


**公式10**: $$$\lambda_i(H(j\omega) + H^H(j\omega)) > 0, \quad \forall \omega$$$

*无源性判据：H(s)为正实矩阵的充要条件，要求H(jω)的Hermitian部分的所有特征值在所有频率下均为正*


### 算法步骤

1. 使用修改的函数形式方法重新表述传输线模型：将传播矩阵A从传统单一时延形式(6)转换为ULM的多模态时延形式(7)，通过对每个对角元素使用多个模态延迟，显著降低低频段（<1 Hz）拟合误差，从根本上减少无源性违规的严重程度

2. 频率扫描识别违规区域：在0 Hz至10 MHz（或更高）频率范围内，以较小步长（如对数坐标下密集采样）计算传递导纳矩阵H(s)的Hermitian部分的所有特征值，绘制特征值随频率变化曲线

3. 局部细化扫描：对于特征值接近零（ suspicious regions）的频率区间，标记为可疑区域，并在这些特定频段内进行更小步长的局部精细化频率扫描，确保不遗漏窄带无源性违规

4. 违规定位与量化：确定无源性违规频段的确切位置和深度，记录负特征值的最小值及其对应频率（如图4(b)所示在约40 Hz处出现约-40的显著负特征值）

5. 线性约束最小二乘修正：建立约束优化问题，以原始拟合参数为基准，通过最小二乘法计算传播矩阵A对角元素的微小扰动ΔA，约束条件为修正后H(s)的所有特征值在违规频段内≥0，目标函数为最小化参数变化量

6. 迭代验证：应用修正后的参数重新计算H(s)特征值，验证无源性违规是否消除；如仍存在违规，重复步骤4-5直至所有频率下特征值均为正

7. 时域模型实现：将修正后的有理函数参数（极点、留数、时延）输入PSCAD/EMTDC等电磁暂态仿真软件，构建被动式时域仿真模型


### 关键参数

- **frequency_fitting_range**: [1 Hz, 1 MHz]

- **frequency_sweep_range**: 0 Hz to 10 MHz

- **line_length**: 100 km

- **number_of_conductors**: 4 (双电缆系统，每电缆包含芯线和护套)

- **passivity_violation_magnitude**: 约-40 (在40 Hz处，图4(b))

- **optimization_method**: 线性约束最小二乘法 (Linear Constrained Least Squares)

- **time_delay_estimation**: 拟合前预先估计(Pre-estimation before curve fitting)

- **violation_frequency_characteristic**: 低频段(≤1 Hz)通常出现大幅度违规，高频段违规幅度较小



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 100 km双HVDC地下电缆系统（交流系统验证） | 采用表I所示参数的双电缆系统（每电缆含芯线和护套，共4导体），使用ULM模型进行建模。原始拟合在1 Hz以下频段存在显著误差，导致约40 Hz处出现深度约-40的负特征值（严重无源性违规）。应用所提算法后，通过扰动传播矩阵对角元素，成功消除该违规，特征值在全频段保持正值 | 与传统非约束拟合相比，所提方法消除了约-40的负特征值违规，避免了时域仿真中的数值不稳定；与需要非线性优化的方法相比，线性约束最小二乘法计算效率显著提升，收敛性更可靠 |

| 多导体交流地下电缆系统 | 针对交流输电应用的地下电缆系统，验证了算法在交流工况下的有效性，确保模型在工频及其谐波频段（50/60 Hz及其倍频）保持无源性 | 与频域理论解对比，修正后的模型在宽频带（1 Hz-1 MHz）内保持高精度，同时确保无源性，适用于开关暂态等电磁暂态研究 |



## 量化发现

- 原始有理函数拟合在约40 Hz频率处产生深度约为-40的负特征值（图4(b)），表明存在严重无源性违规，可能导致时域仿真发散
- 低频段（1 Hz或更低）的拟合不良是导致大幅度无源性违规（大负特征值）的主要原因，而高频段（>1 MHz）的违规通常幅度较小（接近零的负值）
- 频率扫描覆盖范围需达到10 MHz或更高，远超实际仿真带宽（通常1 MHz），以确保捕获所有潜在的高频无源性违规
- 通过仅扰动传播矩阵A的对角元素（而非全矩阵），在消除无源性违规的同时，将模型参数修改量最小化，保持了原始拟合的精度
- 与基于哈密顿矩阵（Hamiltonian matrices）的解析方法相比，频率扫描法虽计算量稍大，但可适用于含传输时延的非线性系统，通用性更强
- ULM的修改函数形式（多模态时延）相比传统单一时延形式，可将低频拟合误差降低一个数量级以上，显著减少初始无源性违规的严重程度


## 关键公式

### 传递导纳矩阵

$$$H(s) = Y_c \begin{bmatrix} (I-A^2)^{-1} & -(I-A^2)^{-1}A \\ -(I-A^2)^{-1}A & (I-A^2)^{-1} \end{bmatrix}$$$

*用于无源性检验的核心矩阵，通过特征导纳Yc和传播矩阵A构建，需在全部频率范围内保持正实性（特征值>0）*

### ULM传播矩阵修改形式

$$$A \approx \sum_{m=1}^{M} e^{-s\tau_m} \cdot \sum_{k=1}^{N_m} \frac{R_{m,k}}{s-p_{m,k}}$$$

*降低无源性违规严重性的关键改进，通过多模态时延τm分别拟合各模式，提高低频拟合精度*

### 线性约束最小二乘优化

$$$\min \|\Delta A\|_2 \quad \text{s.t.} \quad \lambda_i(H_{perturbed}(j\omega)) \geq 0, \forall \omega$$$

*无源性强制步骤的数学表述，目标是最小化传播矩阵的扰动ΔA，同时确保修正后H矩阵在所有频率ω下特征值非负*



## 验证详情

- **验证方式**: 仿真验证（与频域理论解对比）
- **测试系统**: 两个多导体地下电缆系统：(1) 100 km双HVDC电缆系统（4导体，含芯线和护套，图1和表I）；(2) 交流地下电缆系统。系统包含不对称排列的电缆，具有强频率依赖的变换矩阵
- **仿真工具**: PSCAD/EMTDC电磁暂态仿真软件，MATLAB（用于矢量拟合和矩阵计算）
- **验证结果**: 所提算法成功应用于ULM模型，在两个测试案例中均消除了无源性违规（特别是将-40的负特征值修正为正）。修正后的模型在宽频范围（1 Hz-1 MHz）内与频域理论解吻合，验证了算法的准确性和鲁棒性。该方法适用于常数变换矩阵失效的复杂电缆排列（如非对称布置），为HVDC和交流电缆系统的电磁暂态仿真提供了可靠的被动式模型
