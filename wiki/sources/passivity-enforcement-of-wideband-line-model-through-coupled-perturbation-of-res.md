---
title: "Passivity enforcement of wideband line model through coupled perturbation of residues and poles"
type: source
authors: ['Juan Becerra']
year: 2020
journal: "Electric Power Systems Research, 190 (2021) 106798. doi:10.1016/j.epsr.2020.106798"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2020.106798.pdf.pdf"]
---

# Passivity enforcement of wideband line model through coupled perturbation of residues and poles

**作者**: Juan Becerra
**年份**: 2020
**来源**: `31/j.epsr.2020.106798.pdf.pdf`

## 摘要

Passivity enforcement of wideband line model through coupled perturbation Juan Becerra⁎, Ilhan Kocar, Keyhan Sheshyekani, Jean Mahseredjian Department of Electrical Engineering, Ecole Polytechnique de Montreal, Montreal, Canada Ensuring stability in transient simulations of power systems requires that intrinsically passive components of the network should be represented with passive models, including transmission lines and cables. Existing research

## 核心贡献


- 提出同时扰动特征导纳留数、极点与常数项的无源性强制方法
- 引入基于相对误差与状态空间Frobenius距离的偏差度量以保持精度
- 建立线性化凸优化框架实现宽频线路模型无源性校正与精度保持联合求解


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[无源性强制|无源性强制]]
- [[凸优化|凸优化]]
- [[频率扫描法|频率扫描法]]
- [[状态空间建模|状态空间建模]]
- [[frobenius范数|Frobenius范数]]


## 涉及的模型


- [[宽频线路模型-ulm|宽频线路模型(ULM)]]
- [[频变电缆模型-fdcm|频变电缆模型(FDCM)]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[特征导纳有理模型|特征导纳有理模型]]


## 相关主题


- [[无源性强制|无源性强制]]
- [[宽频建模|宽频建模]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真稳定性|电磁暂态仿真稳定性]]
- [[有理函数逼近|有理函数逼近]]


## 主要发现


- 联合扰动极点与留数可显著降低校正引起的频响偏差，精度优于传统方法
- 所提偏差度量指标能有效控制模型失真，确保电磁暂态仿真数值稳定性
- 针对近直流频段大幅违规需结合直流校正预处理，以保证线性化算法收敛



## 方法细节

### 方法概述

本文提出了一种宽频线路模型（ULM/FDCM）的无源性强制方法，通过线性化凸优化框架同时扰动特征导纳$Y_C(s)$的留数（residues）、极点（poles）和常数项（constant term），区别于传统仅扰动留数的方法。方法首先通过频率扫描检测无源性违规频段，然后建立包含相对频率偏差和状态空间Frobenius距离的目标函数，在保持模型精度的同时强制正实性条件。对于近直流频段的大幅违规，需先进行DC校正预处理以保证线性化算法的收敛性。

### 数学公式


**公式1**: $$$\lambda_i(\Theta(Y_n(s))) \ge 0; \quad s = j\omega$$$

*正实性条件，用于判断无源性，其中$\Theta(Y_n(s)) = Y_n(s) + Y_n^H(s)$为Hermitian对称部分*


**公式2**: $$$Y_n = \begin{bmatrix} (I - H_I)^{-1} (I + H_I) Y_C & 2(I - H_I)^{-1} H_I Y_C \\ 2(I - H_I)^{-1} H_I Y_C & (I - H_I)^{-1} (I + H_I) Y_C \end{bmatrix}$$$

*线路导纳矩阵，由特征导纳$Y_C$和传播矩阵$H_I$构成*


**公式3**: $$$Y_C(s) = \sum_{i=1}^{n} \frac{\bar{R}_i}{s - \bar{p}_i} + \bar{D}$$$

*特征导纳的有理函数逼近，包含留数矩阵$\bar{R}_i$、极点$\bar{p}_i$和常数矩阵$\bar{D}$*


**公式4**: $$$\lambda_{j,i}(\Theta(Y_j(s))) + d_{\lambda_{j,i}}(s, \mathbf{x}) > 0$$$

*线性化后的无源性约束，$d_{\lambda}$为特征值一阶微分，$\mathbf{x} = [\bar{\mathbf{r}}_R^T, \bar{\mathbf{p}}_R^T, \bar{\mathbf{c}}_R^T]^T$为相对扰动向量*


**公式5**: $$$\mathbf{F} = \text{diag}(\text{vec}(Y_C(s_k)))^{-1} \cdot \text{vec}(dY_C(s_k, \mathbf{x}))$$$

*相对偏差计算，vec(·)为矩阵向量化算子，vech(·)为对称矩阵下三角向量化*


**公式6**: $$$\mathbf{D}_F = \begin{bmatrix} \text{diag}(\text{vec}(A_1))^{-1}\text{vec}(\Delta A) \\ \text{diag}(\text{vec}(B_1))^{-1}\text{vec}(\Delta B) \\ \text{diag}(\text{vec}(C_1))^{-1}\text{vec}(\Delta C) \\ \text{diag}(\text{vec}(D_1))^{-1}\text{vec}(\Delta D) \end{bmatrix}$$$

*状态空间模型间的相对Frobenius距离，用于度量模型失真*


**公式7**: $$$\min_{\mathbf{x}} \left\| \begin{array}{c} \text{vech}(\mathbf{Y}_{CR}(s_1, \mathbf{x})) \\ \vdots \\ \text{vech}(\mathbf{Y}_{CR}(s_K, \mathbf{x})) \\ \mathbf{D}_F(\mathbf{x}) \end{array} \right\|_2 \quad \text{s.t. (10)}$$$

*凸优化目标函数，联合最小化频率响应偏差和状态空间距离，约束为线性化无源性条件*


**公式8**: $$$K_b = \begin{cases} \lfloor K_d / n_b \rfloor & K_d/n_b > 1 \\ 1 & K_d/n_b \leq 1 \end{cases}$$$

*频率采样点分配公式，$n_b$为无源/非无源频带数，$K_d$为期望总采样数*


### 算法步骤

1. 对$Y_n(s)$应用相似变换$JY_n(s)J^{-1}$降维，将其分解为两个较小的子系统$Y_1(s)$和$Y_2(s)$

2. 在0.01 Hz至100 MHz范围内，采用每decade 100个点的精细对数采样计算$\Theta(Y(s))$的特征值

3. 识别无源和非无源频带，确定频带总数$n_b$

4. 按公式(16)分配各频带采样点数$K_b$，确保总采样数$K \approx K_d = 20$

5. 对每个非无源频带，额外添加一个采样点位于该频段内无源性违规最严重处（最小特征值点）

6. 将DC（0 Hz）作为额外频率点加入采样集

7. 构建扰动向量$\mathbf{x}$，根据所选方案R（仅留数）、RP（留数+极点）或RPC（留数+极点+常数项）确定优化变量

8. 计算一阶微分$d_{\lambda}(s, \mathbf{x})$构建线性化约束(10)

9. 构建目标函数(15)，结合相对偏差$\mathbf{Y}_{CR}$和Frobenius距离$\mathbf{D}_F$

10. 求解凸优化问题，获得最优扰动$\mathbf{x}$，更新模型参数

11. 验证修正后模型的无源性，若仍存在违规则迭代或采用DC校正预处理


### 关键参数

- **frequency_range**: 0.01 Hz - 100 MHz

- **dc_point**: 0 Hz（作为额外采样点）

- **desired_samples_Kd**: 20个频率点

- **log_sampling_density**: 每decade 100个点或更多（用于初始违规检测）

- **perturbation_schemes**: ['R: 仅扰动留数', 'RP: 扰动留数和极点', 'RPC: 扰动留数、极点和常数项']

- **cable_parameters**: {'case_1': 'rin,C=3.175mm, rout,C=12.54mm, rin,S=22.73mm, ρC=1.7e-6Ωm, ρS=2.1e-5Ωm', 'case_2': 'ρC=1.7e-8Ωm, ρS=2.1e-7Ωm（低电阻率变体）', 'case_4': 'rin,C=0.1mm, ρSoil=150Ωm, εr,CI=2.85'}



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case #1 - 地下单相电缆（标准参数） | 导体半径3.175mm，护套内径22.73mm，导体电阻率1.7e-6 Ωm，土壤电阻率100 Ωm。对比R、RP、RPC三种扰动方案的无源性强制效果。 | RPC方案在保持相同精度水平下，所需扰动幅度小于R方案，特征导纳频率响应偏差降低 |

| Case #2 - 低电阻率电缆（高频违规） | 导体电阻率降低至1.7e-8 Ωm，护套电阻率2.1e-7 Ωm，导致高频段无源性违规。 | 联合扰动极点可显著改善高频段拟合精度，相比仅扰动留数方法，Frobenius距离减少约30-50% |

| Case #3 - 理想导体（rin,C=0） | 导体半径设为0（理想导体情况），测试极端条件下算法鲁棒性。 | 需配合DC校正预处理，线性化算法成功收敛，而传统方法在近直流频段失效 |

| Case #4 - 薄壁导体与改性绝缘 | 导体半径0.1mm，绝缘层介电常数2.85，损耗角正切0.0001，土壤电阻率150 Ωm。 | RPC方案在处理近直流大幅违规时，通过扰动常数项$D$矩阵，避免了传统方法导致的低频失真 |

| Case #5 - 大直径海底电缆 | 导体半径30mm，护套外径48.47mm，绝缘层介电常数2.85，适用于高压直流输电场景。 | 验证方法在几何大尺寸、低电阻率（1.7e-8 Ωm）电缆模型中的有效性，无源性强制后数值稳定性满足EMT仿真要求 |



## 量化发现

- 频率采样范围：0.01 Hz - 100 MHz，覆盖宽频模型有效带宽
- 目标采样点数：$K_d = 20$个频率点用于优化约束
- 初始检测采样密度：每decade不少于100个对数均匀分布点
- 导体电阻率范围：1.7e-8 Ωm（低损耗）至1.7e-6 Ωm（标准铜）
- 土壤/海水电阻率：100 Ωm或150 Ωm
- 绝缘层相对介电常数：2.0 - 3.5（含2.85交联聚乙烯典型值）
- 损耗角正切值：0至0.0004
- 几何尺寸范围：导体半径0.1mm至30mm，护套外径可达48.47mm
- 优化后特征值满足：$\lambda_i(\Theta(Y_n(s))) \geq 0$在整个频段内成立
- 相对偏差控制：通过Frobenius范数将模型失真限制在原始模型参数的相对变化5%以内


## 关键公式

### 线性化无源性约束

$$$\lambda_{j,i}(\Theta(Y_j(s))) + d_{\lambda_{j,i}}(s, \mathbf{x}) > 0$$$

*在凸优化中作为不等式约束，确保扰动后模型在所有采样频率点满足正实性条件*

### 联合偏差最小化目标函数

$$$\min_{\mathbf{x}} \left\| \begin{array}{c} \text{vech}(\mathbf{Y}_{CR}(s_1, \mathbf{x})) \\ \vdots \\ \text{vech}(\mathbf{Y}_{CR}(s_K, \mathbf{x})) \\ \mathbf{D}_F(\mathbf{x}) \end{array} \right\|_2$$$

*同时优化频率响应相对偏差和状态空间距离，平衡无源性强制与模型精度保持*

### 特征导纳有理逼近

$$$Y_C(s) = \sum_{i=1}^{n} \frac{\bar{R}_i}{s - \bar{p}_i} + \bar{D}$$$

*宽频线路模型(ULM/FDCM)中特征导纳的标准表示形式，为扰动提供参数基础*



## 验证详情

- **验证方式**: 数值仿真与对比分析
- **测试系统**: 地下多导体电缆系统（单相电缆含导体、护套、绝缘层和土壤介质），包含5种不同几何和电磁参数配置
- **仿真工具**: 基于MATLAB实现矢量拟合和无源性强制算法，通过频率扫描法验证正实性条件，状态空间模型用于Frobenius距离计算
- **验证结果**: 在5个测试案例中，RPC（留数-极点-常数联合扰动）方案相比传统R（仅留数）方案，在保持相同无源性强制效果的同时，将特征导纳频率响应偏差降低30-50%，特别是在近直流和超高频段。对于Case #3和Case #4存在近直流大幅违规的情况，结合DC校正预处理后，算法成功收敛且模型失真控制在可接受范围内，确保了EMT仿真中的数值稳定性。
