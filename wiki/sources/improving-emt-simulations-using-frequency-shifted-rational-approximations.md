---
title: "Improving EMT simulations using frequency-shifted rational approximations"
type: source
authors: ['A.A. Kida']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112395. doi:10.1016/j.epsr.2025.112395"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kida 等 - 2026 - Improving EMT simulations using frequency-shifted rational approximations.pdf"]
---

# Improving EMT simulations using frequency-shifted rational approximations

**作者**: A.A. Kida
**年份**: 2025
**来源**: `23/Kida 等 - 2026 - Improving EMT simulations using frequency-shifted rational approximations.pdf`

## 摘要

Improving EMT simulations using frequency-shifted rational b Department of Electrical Engineering, COPPE/UFRJ, Federal University of Rio de Janeiro, Rio de Janeiro, Brazil c Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, BA, Brazil Accurate electromagnetic transient (EMT) simulations require accounting for the frequency-dependent behavior of system components and equivalents. Rational approximations derived from curve-ﬁtting techniques such as

## 核心贡献


- 提出基于复矢量拟合与解析信号的频移有理逼近框架，打破传统VF共轭对称约束
- 揭示CVF与VF模型在无源性评估上的差异，完善频变等值模型的稳定性分析
- 引入频移技术优化基带仿真，在保持精度前提下显著放宽EMT仿真步长限制


## 使用的方法


- [[复矢量拟合-cvf|复矢量拟合(CVF)]]
- [[矢量拟合-vf|矢量拟合(VF)]]
- [[解析信号|解析信号]]
- [[频移技术|频移技术]]
- [[有理逼近|有理逼近]]
- [[状态空间实现|状态空间实现]]
- [[无源性评估|无源性评估]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[配电网|配电网]]
- [[频变等值模型-fde|频变等值模型(FDE)]]
- [[导纳矩阵|导纳矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[频移仿真|频移仿真]]
- [[无源性评估|无源性评估]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- CVF模型拟合误差较传统VF降低达八个数量级，且无源性特征存在显著差异
- 频移技术使CVF框架精度再提升两个数量级，并允许仿真步长扩大2.33至5.5倍
- 所提框架在输电线路与配电网验证中有效平衡了仿真精度与计算效率



## 方法细节

### 方法概述

提出一种基于复矢量拟合（CVF）与频移解析信号的电磁暂态（EMT）仿真新框架。传统矢量拟合（VF）强制模型满足共轭对称性以生成实值冲激响应，限制了其在基带仿真中的应用。本方法通过CVF解除该约束，允许极点和留数独立存在，从而构建非厄米对称的有理逼近模型。结合希尔伯特变换将实值激励转换为解析信号，并引入频移因子Δf将频谱中心移至0Hz，实现基带（频移）仿真。模型通过状态空间形式实现，并采用梯形积分法进行时域离散。该框架在保持甚至提升精度的同时，显著放宽了EMT仿真步长限制，并揭示了CVF与VF在无源性评估上的本质差异。

### 数学公式


**公式1**: $$$\mathbf{Y}(s) \approx \sum_{i=1}^{N_p} \frac{\mathbf{R}_i}{s - p_i} + \mathbf{D}$$$

*导纳矩阵的极点-留数有理逼近形式，用于频域建模*


**公式2**: $$$u_A(t) = u(t) + j\mathcal{H}\{u(t)\}$$$

*解析信号定义，通过希尔伯特变换将实信号转换为仅含非负频率分量的复信号*


**公式3**: $$$u_{A,sh}(t) = \exp(-j2\pi\Delta f t)u_A(t)$$$

*频移解析信号公式，将频谱中心平移至基带（0Hz）以降低仿真带宽需求*


**公式4**: $$$Y_E = \sqrt{\frac{\sum_{m=1}^N \sum_{q=1}^N \sum_{k=1}^{N_s} |Y_{mq}(s_k) - \hat{Y}_{mq}(s_k)|^2}{N_s \sum_{m=1}^N \sum_{q=1}^N \sum_{k=1}^{N_s} |Y_{mq}(s_k)|^2}}$$$

*相对均方根误差（RRMSE），用于量化频域拟合精度*


### 算法步骤

1. 获取N端口导纳矩阵Y(s)的频域采样数据（通过测量或全波仿真）。

2. 应用复矢量拟合（CVF）算法进行有理逼近，解除传统VF的共轭对称约束，允许极点和留数独立优化，获得更灵活的极点-留数模型。

3. 将拟合得到的极点-留数模型转换为状态空间形式Y(s)=C(sI-A)^(-1)B+D，构建系统矩阵。

4. 执行无源性评估：构建哈密顿矩阵H并计算其特征值，识别实部为负的频率区域；由于CVF模型不满足厄米对称性，需采用全尺寸奇异值测试而非VF的半尺寸测试。

5. 时域仿真准备：将实值电压激励e(t)通过希尔伯特变换转换为解析信号e_A(t)，消除负频率分量。

6. 应用频移技术：根据目标现象的中心频率Δf，计算频移解析信号e_{A,sh}(t)=exp(-j2πΔf t)e_A(t)，将高频激励下变频至基带。

7. 状态空间时域求解：将频移后的复信号输入状态空间模型，采用梯形积分法进行离散化迭代，计算复电流响应i_{A,sh}(t)。

8. 信号还原：对仿真输出的复电流进行逆频移操作并提取实部，恢复为物理可观测的实值时域电流i(t)。


### 关键参数

- **频移量_Δf**: 0 Hz, 50 kHz, 90 kHz

- **激励频率_f_e**: 50 kHz, 90 kHz

- **模型阶数_N_p**: 与VF保持一致以确保公平对比

- **积分方法**: 梯形积分法

- **硬件环境**: Intel i5-1240P, 16GB RAM



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case A: 132 kV三相输电线路（12 km） | 在50 kHz和90 kHz高频激励下，CVF模型拟合误差较传统VF降低达8个数量级。引入频移技术后，CVF框架精度进一步提升2个数量级。在相同目标精度下，仿真步长可扩大2.33至5.5倍。 | 相比传统VF，CVF+频移框架在保持精度的同时显著降低计算负担，步长提升2.33~5.5倍 |

| Case B: 配电网系统 | 验证了CVF在复杂网络等值中的适用性。CVF模型展现出与VF显著不同的无源性特征，部分频段无源性表现更优。频移仿真同样实现精度提升与步长放宽。 | 在配电网场景下复现了Case A的精度与效率优势，证明框架具有通用性 |



## 量化发现

- CVF拟合误差较传统VF降低最高达8个数量级（10^8倍）
- 频移技术使CVF框架精度再提升最高达2个数量级（10^2倍）
- 在相同目标精度下，EMT仿真步长可扩大2.33至5.5倍
- CVF模型因解除共轭对称约束，无法使用VF的半尺寸无源性测试，需采用全尺寸哈密顿矩阵奇异值测试
- 频移量Δf与激励频率f_e匹配时（如Δf=f_e），频移后信号退化为直流分量，极大降低高频动态仿真带宽需求


## 关键公式

### 状态空间实现方程

$$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$$

*将频域有理逼近模型转换为时域可求解的微分/差分方程组，用于EMT步进仿真*

### 频移解析信号方程

$$$u_{A,sh}(t) = \exp(-j2\pi\Delta f t)u_A(t)$$$

*在基带仿真中，将高频激励频谱平移至0Hz附近，使EMT求解器可使用更大步长*

### 无源性评估哈密顿矩阵

$$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}')^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}')^{-1}\mathbf{B}' \\ -\mathbf{C}'(\mathbf{D}+\mathbf{D}')^{-1}\mathbf{C} & -\mathbf{A}' + \mathbf{C}'(\mathbf{D}+\mathbf{D}')^{-1}\mathbf{B}' \end{bmatrix}$$$

*用于解析识别有理逼近模型的无源性违规频段，确保时域仿真稳定性*



## 验证详情

- **验证方式**: 数值仿真与对比分析（基于公开基准数据）
- **测试系统**: Case A: 132 kV三相输电线路（长12 km，相导线直径21.66 mm，地线直径12.33 mm）；Case B: 配电网系统
- **仿真工具**: MATLAB 2018a, 梯形积分法离散化, 硬件: Intel i5-1240P/16GB RAM
- **验证结果**: 在输电线路与配电网两个标准测试系统中，CVF框架在拟合精度上全面超越传统VF（误差降低8个数量级），且频移技术进一步将精度提升2个数量级。在同等精度要求下，仿真步长成功扩大2.33~5.5倍，显著降低计算成本。同时揭示了CVF与VF在无源性特征上的本质差异，验证了所提框架在电力系统EMT分析中的高效性与可靠性。
