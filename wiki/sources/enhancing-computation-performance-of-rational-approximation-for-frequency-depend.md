---
title: "Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting"
type: source
authors: ['Alexandre', 'A.', 'Kida']
year: 2024
journal: "Electric Power Systems Research, 234 (2024) 110778. doi:10.1016/j.epsr.2024.110778"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf"]
---

# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

**作者**: Alexandre, A., Kida
**年份**: 2024
**来源**: `17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c

## 核心贡献


- 提出复数矢量拟合用于FDNE导纳矩阵综合，解除极点共轭约束
- 基于C语言实现VF与CVF并行化算法，摆脱商业软件依赖
- 构建多端口网络等值有理逼近框架，显著提升大规模系统拟合效率


## 使用的方法


- [[复数矢量拟合-cvf|复数矢量拟合(CVF)]]
- [[矢量拟合-vf|矢量拟合(VF)]]
- [[有理逼近|有理逼近]]
- [[并行计算|并行计算]]
- [[频域实现|频域实现]]
- [[状态空间综合|状态空间综合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[多端口导纳矩阵|多端口导纳矩阵]]
- [[有理模型-rm|有理模型(RM)]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[并行计算|并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[模型降阶|模型降阶]]


## 主要发现


- 并行化C语言实现显著降低多端口拟合耗时，计算效率优于传统MATLAB脚本
- CVF成功应用于导纳矩阵综合，解除共轭约束后仍保持宽频带高精度拟合
- 算法性能随端口数与阶数增加呈良好扩展性，验证了大规模等值建模可行性



## 方法细节

### 方法概述

本文针对频率相关网络等值(FDNE)有理逼近计算效率低及商业软件依赖问题，提出结合复数矢量拟合(CVF)与底层C语言并行化实现的优化框架。CVF通过解除传统矢量拟合(VF)的极点与留数共轭约束，直接适用于导纳/阻抗矩阵综合，避免强制共轭带来的拟合失真。算法底层采用Intel oneAPI MKL(LAPACK)库实现高性能线性代数运算，并针对VF/CVF中最耗时的QR分解步骤（占总执行时间>95%）设计并行策略。利用极点识别矩阵的近似对角块结构，将大规模多端口系统划分为独立子系统进行并行求解，最终组装为稀疏状态空间模型，实现宽频带、多端口FDNE的高效、高精度综合。

### 数学公式


**公式1**: $$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*多端口传递函数的有理逼近模型（极点-留数形式），其中$N_p$为极点阶数，$\mathbf{R}_n$为留数矩阵，$\mathbf{D}$和$\mathbf{E}$为正定常数矩阵。*


**公式2**: $$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}^T \mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) + \mathbf{E}\dot{\mathbf{u}}(t)$$$

*有理模型的状态空间实现形式，用于EMT仿真器的时域积分求解。*


**公式3**: $$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} + s\mathbf{E}$$$

*由状态空间矩阵推导出的频域导纳传递函数表达式。*


**公式4**: $$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*用于无源性校验的Hamiltonian矩阵，通过求解其纯虚数特征值可精确定位无源性破坏的交叉频率。*


### 算法步骤

1. 1. 频域数据采集：通过外部电磁暂态或频域扫描工具获取边界端口的多端口导纳矩阵频率响应数据$\mathbf{Y}(j\omega)$。

2. 2. 初始极点设置与过定系统构建：设定初始极点分布，构建用于极点重定位的过定线性方程组，矩阵维度与$N \cdot N_p$成正比。

3. 3. 并行QR分解与极点迭代：利用矩阵的近似对角块结构划分计算任务，调用并行化LAPACK例程执行QR分解，求解极点更新量。CVF在此步骤中不强制极点/留数共轭配对。

4. 4. 留数与常数项求解：固定更新后的极点，通过最小二乘法求解各阶留数矩阵$\mathbf{R}_n$及常数项$\mathbf{D}$、$\mathbf{E}$。

5. 5. 状态空间矩阵组装：将极点-留数形式转换为状态空间矩阵$(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}, \mathbf{E})$，其中$\mathbf{A}$为对角极点矩阵，$\mathbf{B}$为0-1选择矩阵。

6. 6. 无源性校验与修正：计算实部矩阵$\mathbf{G}(s)=\Re(\mathbf{Y}(s))$的特征值，构建Hamiltonian矩阵$\mathbf{H}$检测无源性破坏区域，必要时进行极点扰动或阶数调整以确保时域仿真稳定性。


### 关键参数

- **端口数_N**: 测试系统为8端口，算法复杂度与$N^2$相关

- **模型阶数_Np**: 极点数量，直接影响拟合精度与计算规模

- **频率采样点数**: 频域扫描数据密度，影响过定方程组规模

- **并行策略**: 基于QR分解的块对角矩阵划分，利用Intel MKL多线程加速

- **无源性阈值**: 要求$\Re(\mathbf{Y}(s))$正定，即特征值$\lambda(s) > 0$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 8端口FDNE宽频带拟合 | 针对具有大量峰谷特性的8端口网络等值模型进行有理逼近，QR分解步骤占总计算时间>95%，并行化C实现有效突破该瓶颈。 | 相比传统MATLAB®串行脚本，C语言并行实现显著降低多端口拟合耗时，摆脱商业软件依赖，计算效率随端口数与阶数增加呈良好线性扩展。 |

| CVF与VF导纳矩阵综合对比 | CVF解除共轭约束后直接应用于导纳矩阵拟合，在宽频带内保持高精度，极点分布更灵活，适用于基带等效与频移分析(SFA)框架。 | CVF在保持与VF同等拟合精度的前提下，避免了强制共轭配对导致的冗余极点，模型阶数利用率更高，复数运算开销被并行化有效抵消。 |



## 量化发现

- QR分解步骤占VF/CVF算法总执行时间>95%，是并行化优化的核心目标。
- 算法计算复杂度不低于$O(N^2)$，其中$N$为端口数，状态空间矩阵维度为$N \cdot N_p \times N \cdot N_p$。
- 针对8端口FDNE验证，频响特性含大量峰谷，CVF解除共轭约束后仍保持宽频带高精度拟合。
- 并行化C语言实现结合Intel MKL库，显著降低多端口拟合耗时，验证了大规模等值建模的可行性。
- 无源性破坏可通过Hamiltonian矩阵纯虚数特征值精确识别，避免传统频率扫描法的漏检风险。


## 关键公式

### 多端口有理逼近模型

$$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*用于将频域扫描得到的导纳矩阵数据拟合为极点-留数形式，是FDNE综合的基础表达式。*

### 状态空间频域传递函数

$$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} + s\mathbf{E}$$$

*将拟合得到的极点-留数参数转换为EMT求解器可直接调用的状态空间形式，便于时域积分。*

### 无源性校验Hamiltonian矩阵

$$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*用于解析计算无源性破坏的交叉频率，确保有理模型在任意频率下均吸收有功功率，保障时域仿真稳定性。*



## 验证详情

- **验证方式**: 频域扫描数据拟合对比与数值性能基准测试
- **测试系统**: 8端口频率相关网络等值(FDNE)模型，其频响特性具有大量谐振峰谷，用于验证多端口拟合能力
- **仿真工具**: C语言 + Intel oneAPI Math Kernel Library (MKL/LAPACK) 并行实现，对比基线为MATLAB®官方VF/CVF脚本
- **验证结果**: 验证了CVF在导纳矩阵综合中的首次应用可行性，并行化C实现有效解决多端口系统计算瓶颈。算法在宽频带内保持高精度拟合，解除共轭约束未引入稳定性问题，且性能随端口数与阶数增加具备良好扩展性，为大规模电力系统EMT等值建模提供了高效开源实现路径。
