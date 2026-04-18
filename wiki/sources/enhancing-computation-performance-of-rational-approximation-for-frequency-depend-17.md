---
title: "Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting"
type: source
authors: ['Alexandre', 'A.', 'Kida']
year: 2024
journal: "Electric Power Systems Research, 234 (2024) 110778. doi:10.1016/j.epsr.2024.110778"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf"]
---

# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

**作者**: Alexandre, A., Kida
**年份**: 2024
**来源**: `17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c

## 核心贡献


- 提出复数矢量拟合用于导纳矩阵综合，解除极点共轭约束
- 基于C语言与底层线性代数库实现算法并行化，摆脱商业软件依赖
- 系统评估模型阶数、端口数与频点数量对多端口FDNE计算性能的影响


## 使用的方法


- [[复数矢量拟合|复数矢量拟合]]
- [[矢量拟合|矢量拟合]]
- [[有理逼近|有理逼近]]
- [[并行计算|并行计算]]
- [[频域实现|频域实现]]
- [[状态空间综合|状态空间综合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[多端口导纳矩阵|多端口导纳矩阵]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[并行计算|并行计算]]
- [[有理逼近|有理逼近]]
- [[无源性校验|无源性校验]]


## 主要发现


- CVF成功应用于导纳矩阵综合，有效解除极点共轭约束并提升拟合灵活性
- 并行C语言实现显著加速有理逼近计算，验证了多端口FDNE建模的可行性
- 算法性能随模型阶数、端口数与频点增加保持稳定，计算效率优于传统串行实现



## 方法细节

### 方法概述

本文提出一种结合复数矢量拟合（CVF）与底层并行计算的高效有理逼近策略，用于频率相关网络等值（FDNE）的导纳矩阵综合。传统矢量拟合（VF）强制极点与留数满足复共轭对称约束，限制了建模灵活性。CVF通过解除该约束，允许独立拟合复极点，特别适用于基带等效或具有复杂频响特性的多端口系统。为突破商业软件（如MATLAB）的性能瓶颈，算法采用C语言结合Intel oneAPI MKL（LAPACK）底层线性代数库进行重构。针对VF/CVF中QR分解占据超95%计算时间的瓶颈，利用极点识别矩阵的近似分块对角结构，将大规模MIMO系统分解为多个子系统进行并行求解，最终集成得到稀疏状态空间模型，显著提升多端口FDNE的拟合效率与数值稳定性。

### 数学公式


**公式1**: $$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*多端口导纳矩阵的极点-留数有理逼近表达式，用于频域响应拟合*


**公式2**: $$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}^T \mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) + \mathbf{E}\dot{\mathbf{u}}(t)$$$

*由极点-留数形式转换得到的状态空间实现方程，便于时域EMT仿真集成*


**公式3**: $$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} + s\mathbf{E}$$$

*状态空间模型对应的传递函数形式，用于频域验证与综合*


**公式4**: $$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*用于解析判定模型无源性的哈密顿矩阵，通过计算其纯虚数特征值定位无源性破坏频点*


### 算法步骤

1. 1. 频域采样与初始极点设定：在目标频带内对N端口网络进行频率扫描，获取导纳矩阵频响数据，并初始化一组起始极点（通常为实数或随机复数）。

2. 2. 构建超定线性方程组：将极点-留数模型转化为关于未知极点偏移量的线性最小二乘问题，形成维度与$N \cdot N_p$成正比的系数矩阵。

3. 3. 并行QR分解求解：利用系数矩阵的近似分块对角特性，将全局矩阵划分为多个独立子块。调用Intel MKL并行LAPACK例程对各子块同步执行QR分解，求解极点更新量，此步骤占总计算量95%以上。

4. 4. 极点迭代与留数计算：重复步骤2-3直至极点收敛。固定收敛极点后，再次构建线性方程组，通过最小二乘法直接求解各端口对应的留数矩阵$\mathbf{R}_n$及常数项$\mathbf{D}, \mathbf{E}$。

5. 5. 状态空间综合与无源性校验：将拟合结果转换为状态空间矩阵$(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}, \mathbf{E})$。构建哈密顿矩阵$\mathbf{H}$并计算其特征值，若存在纯虚数特征值则标记无源性破坏区域，必要时进行后处理修正。


### 关键参数

- **模型阶数($N_p$)**: 控制拟合精度的极点数量，直接影响状态空间维度与计算复杂度

- **端口数($N$)**: FDNE边界母线数量，决定导纳矩阵维度$N \times N$及并行子块划分规模

- **频点数量**: 频率扫描采样点数，影响超定方程组的行数与拟合鲁棒性

- **无源性阈值**: 哈密顿矩阵特征值实部容差，用于判定$\lambda(s) > 0$是否满足



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 8端口复杂频响FDNE模型 | 针对具有显著峰谷特征的8端口网络等值模型进行有理逼近测试。在模型阶数、端口数与频点数量同步增加的工况下，并行C语言实现保持了稳定的计算收敛性，QR分解并行化使单次迭代耗时显著降低，系统复杂度不低于$O(N^2)$。 | 相较于传统串行MATLAB实现，底层C+MKL并行方案在相同拟合精度下计算效率显著提升，且摆脱了商业软件依赖；算法扩展性良好，验证了多端口大规模FDNE建模的工程可行性。 |



## 量化发现

- QR分解步骤占据VF/CVF算法总执行时间的95%以上，是并行化优化的核心瓶颈
- CVF成功解除复共轭极点约束，允许独立拟合复极点，提升了非对称/基带频响的拟合灵活性
- 并行C语言实现摆脱了对MATLAB等商业软件的依赖，利用Intel MKL底层库实现高效数值计算
- 算法性能在模型阶数、端口数与频点数量增加时保持稳定，计算效率优于传统串行实现
- 状态空间矩阵维度为$N \cdot N_p \times N \cdot N_p$，系统复杂度不低于$O(N^2)$，并行分块策略有效缓解了维度爆炸问题


## 关键公式

### 极点-留数有理逼近模型

$$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*用于将频域扫描得到的多端口导纳矩阵拟合为有理函数形式，是FDNE综合的基础*

### 无源性判定哈密顿矩阵

$$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*在拟合完成后用于解析检测模型是否满足无源性条件，避免时域仿真中出现能量发散*



## 验证详情

- **验证方式**: 数值基准测试与频域响应拟合对比分析
- **测试系统**: 具有显著峰谷频响特征的8端口测试系统（8-port FDNE）
- **仿真工具**: 自定义C语言实现（集成Intel oneAPI Math Kernel Library/LAPACK），对比基线为MATLAB串行脚本
- **验证结果**: 验证了CVF在导纳矩阵综合中的有效性及并行C实现的计算优势。结果表明，所提方法在保持高拟合精度的同时，显著降低了多端口FDNE的构建时间，且算法扩展性良好，为大规模电力系统电磁暂态仿真中的网络等值提供了高效、开源的解决方案。
