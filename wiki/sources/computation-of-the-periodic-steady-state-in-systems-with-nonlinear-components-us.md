---
title: "Computation of the periodic steady state in systems with nonlinear components using a hybrid time and frequency domain methodology"
type: source
authors: ['A. Semlyen', 'A. Medina']
year: 2004
journal: "IEEE Transactions on Power Systems;1995;10;3;10.1109/59.466497"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Computation_of_the_periodic_steady_state_in_systems_with_nonlinear_components_using_a_hybrid_time_and_frequency_domain_methodology.pdf"]
---

# Computation of the periodic steady state in systems with nonlinear components using a hybrid time and frequency domain methodology

**作者**: A. Semlyen, A. Medina
**年份**: 2004
**来源**: `11/Computation_of_the_periodic_steady_state_in_systems_with_nonlinear_components_using_a_hybrid_time_and_frequency_domain_methodology.pdf`

## 摘要

The basic principles of an eficient new methodology for the calculation of the non-sinusoidal periodic steady state in system with nonlinear and timevarying components are described. All linear parts, including the network and part of he loads. are represented in the frequency domain, while nonlinear and time-varying components, mainly loads, are represented in the time domain. This hybrid procegp b iterative, with periodic, non-sinusoidal, bus voltages U inputs for both fiqumcy domain solutions and time domain simulations: a current mismatch is calculated at each bus and used to update the voltages until convergence is reached. Thus the process, but not the solution, is decoupled for the individual harmonics. Its efficiency is enhand by the use of Newton type algorithms for fast convergen

## 核心贡献


- 提出时频混合迭代架构，线性网络频域求解与非线性负载时域仿真结合实现谐波解耦
- 引入庞加莱映射与牛顿型算法加速时域周期稳态收敛，避免传统暂态积分耗时过长
- 构建基于电流失配量与近似导纳矩阵的节点电压更新机制，保障迭代过程全局收敛


## 使用的方法


- [[时频混合迭代法|时频混合迭代法]]
- [[牛顿型加速算法|牛顿型加速算法]]
- [[庞加莱映射|庞加莱映射]]
- [[谐波潮流计算|谐波潮流计算]]
- [[电流失配法|电流失配法]]
- [[变分方程线性化|变分方程线性化]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[非线性负载|非线性负载]]
- [[非线性电感|非线性电感]]
- [[线性网络|线性网络]]


## 相关主题


- [[周期稳态计算|周期稳态计算]]
- [[谐波分析|谐波分析]]
- [[电磁暂态初始化|电磁暂态初始化]]
- [[混合仿真|混合仿真]]
- [[非线性系统求解|非线性系统求解]]


## 主要发现


- 时频混合架构实现谐波解耦，显著降低非线性系统谐波潮流计算维度与内存需求
- 庞加莱映射结合牛顿法加速时域稳态收敛，克服轻阻尼电路传统仿真耗时难题
- 电流失配结合近似导纳矩阵更新电压，确保迭代收敛且兼容不可微非线性特性



## 方法细节

### 方法概述

本文提出一种时频混合迭代架构，用于高效计算含非线性与时变元件电力系统的非正弦周期稳态。该方法将线性网络部分置于频域求解，利用导纳矩阵直接计算各次谐波电流；将非线性负载置于时域进行微分方程数值积分，通过傅里叶变换获取谐波电流。迭代过程以母线电压为输入，计算频域线性电流与时域非线性电流的失配量，构建实数域导纳矩阵求解电压修正量并更新，直至收敛。为克服传统时域积分收敛缓慢的问题，引入庞加莱映射与牛顿型加速算法，利用极限环邻域动力学的近似线性特性，通过状态转移矩阵外推直接逼近周期稳态，实现谐波解耦计算与快速收敛，适用于谐波潮流计算与电磁暂态仿真初始化。

### 数学公式


**公式1**: $$$\Delta I_h = I_h^L + I_h^N$$$

*电流失配方程，表示第h次谐波下线性网络电流与非线性负载电流之和，用于驱动迭代更新*


**公式2**: $$$G \Delta V_h = \Delta I_h$$$

*电压修正方程，利用近似导纳矩阵G求解电压增量，以消除电流失配*


**公式3**: $$$\dot{x} = f(x, t)$$$

*非线性负载状态空间微分方程，描述系统动态行为*


**公式4**: $$$\Delta \dot{x} = J(t) \Delta x$$$

*变分方程，描述极限环邻域内状态扰动的线性化演化规律*


**公式5**: $$$\Delta x^{i+1} = B \Delta x^i$$$

*庞加莱映射关系式，B为状态转移矩阵，表征相邻周期截面状态点的线性映射*


**公式6**: $$$x^m = x^i + C(x^{i+1} - x^i)$，其中 $C = (I - B)^{-1}$$$

*极限环外推公式，利用庞加莱截面交点直接预测周期稳态初始状态*


**公式7**: $$$\begin{bmatrix} G' & -B'' \\ B' & G'' \end{bmatrix} \begin{bmatrix} \Delta V' \\ \Delta V'' \end{bmatrix} = \begin{bmatrix} \Delta I' \\ \Delta I'' \end{bmatrix}$$$

*实数域导纳矩阵方程，将复数谐波电压电流分解为实部虚部，避免非线性负载的相位旋转假设*


### 算法步骤

1. 初始化各非线性负载母线的基波及各次谐波电压相量 $V_h$，并通过逆傅里叶变换生成时域周期电压波形 $v(t)$。

2. 频域计算：利用线性网络导纳矩阵 $Y_h$，执行稀疏矩阵向量乘法，独立计算各次谐波下的线性电流 $I_h^L = Y_h V_h$。

3. 时域仿真：对每个非线性负载，以 $v(t)$ 为激励进行微分方程数值积分。先运行3-7个完整周期使暂态衰减，随后基于庞加莱截面计算状态转移矩阵 $B$，利用 $C=(I-B)^{-1}$ 外推极限环初始状态，快速获得周期稳态电流 $i(t)$。

4. 谐波变换：对收敛的稳态电流 $i(t)$ 进行傅里叶分析，提取各次谐波分量 $I_h^N$。

5. 失配计算：计算各母线总电流失配量 $\Delta I_h = I_h^L + I_h^N$。

6. 电压更新：构建实数域迭代导纳矩阵 $G$（可仅用线性 $Y_h$ 或叠加非线性负载等效导纳），求解线性方程组 $G \Delta V_h = \Delta I_h$ 得到电压修正量 $\Delta V_h$。

7. 迭代判断：更新母线电压 $V_h \leftarrow V_h - \Delta V_h$，若 $\|\Delta I_h\|$ 或 $\|\Delta V_h\|$ 小于设定容差则终止，否则返回步骤2继续迭代。


### 关键参数

- **状态变量收敛容差**: $10^{-10}$ p.u. (部分测试采用 $10^{-12}$ p.u.)

- **初始暴力积分周期数**: 强阻尼系统3-4个，弱阻尼系统6-7个

- **考虑谐波次数**: 通常前11次，无直流偏置时仅计算奇次谐波

- **迭代矩阵更新策略**: 全牛顿法(每步更新B)、部分更新法(固定B多次)、单次更新法

- **导纳矩阵构建方式**: 纯线性 $Y_h$ 或叠加非线性负载实部/虚部导纳



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 3节点弱阻尼测试系统（7个状态变量） | 采用全时域暴力积分法耗时35.1秒；采用数值微分(ND)加速法耗时6.5秒；采用直接牛顿-拉夫森(NR)法耗时7.9秒。混合迭代法在仅使用线性导纳矩阵时需12次迭代收敛，叠加非线性负载等效导纳后迭代次数降至6次。 | ND加速法计算效率较暴力积分法提升约5.4倍；混合迭代法迭代次数减半，整体求解时间比纯时域方法快一个数量级以上。 |

| 时域加速算法收敛性测试 | 初始运行7个完整周期后，应用ND加速算法。第1次加速后误差降至0.03536 p.u.，第2次降至 $3.67 \times 10^{-3}$ p.u.，第3次降至 $2.23 \times 10^{-4}$ p.u.，第4次达到 $8.98 \times 10^{-10}$ p.u.，满足收敛标准。 | 相比传统固定点迭代法需数十个周期缓慢逼近，牛顿型外推法在3-4次应用内即可实现 $10^{-10}$ 级精度收敛。 |



## 量化发现

- 采用数值微分(ND)加速算法后，时域周期稳态收敛所需完整周期数从数十个降至约16-18个，最大状态变量误差从 $0.07845$ p.u. 降至 $9.76 \times 10^{-11}$ p.u.
- 混合迭代法在仅使用线性导纳矩阵时需12次迭代收敛，叠加非线性负载等效导纳后迭代次数减半至6次，显著增强高谐波畸变或谐振条件下的鲁棒性
- 全时域暴力积分法耗时约35.1秒，而ND加速法仅需6.5秒，计算效率提升约5.4倍；单次完整时域周期计算耗时约0.21秒
- 在弱阻尼系统中，初始需运行6-7个完整周期以消除暂态分量，随后仅需1-2次牛顿外推即可达到 $10^{-10}$ p.u. 精度
- 采用解耦导纳矩阵法（忽略 $G', G''$）在低谐波畸变系统中平均增加约2次迭代，但矩阵规模减半且保持对称稀疏性，存储与求解时间近乎减半


## 关键公式

### 电流失配方程

$$$\Delta I_h = I_h^L + I_h^N$$$

*用于量化频域线性响应与时域非线性响应之间的不平衡，作为迭代驱动信号*

### 电压修正方程

$$$G \Delta V_h = \Delta I_h$$$

*在每次迭代中求解母线电压增量，实现谐波解耦下的全局收敛*

### 庞加莱映射极限环外推公式

$$$x^m = x^i + (I - B)^{-1}(x^{i+1} - x^i)$$$

*在时域仿真中利用相邻周期截面状态点直接预测周期稳态初始值，避免长时间暂态积分*

### 实数域导纳矩阵方程

$$$\begin{bmatrix} G' & -B'' \\ B' & G'' \end{bmatrix} \begin{bmatrix} \Delta V' \\ \Delta V'' \end{bmatrix} = \begin{bmatrix} \Delta I' \\ \Delta I'' \end{bmatrix}$$$

*处理非线性负载时避免复数导纳的相位旋转假设，确保电压电流更新在实数域严格对应*



## 验证详情

- **验证方式**: 对比分析（纯时域暴力积分 vs 时域加速算法 vs 时频混合迭代法）
- **测试系统**: 自定义3节点测试系统（含7个状态变量，弱阻尼特性，含非线性电感负载）
- **仿真工具**: 自主开发的单相交流混合谐波潮流程序（运行于64位KSR1计算机）
- **验证结果**: 验证了时频混合架构的正确性与高效性。时域加速算法成功将周期稳态收敛时间缩短一个数量级；混合迭代法通过合理构建导纳矩阵，在6-12次迭代内实现 $10^{-12}$ p.u. 级收敛，显著优于传统固定点迭代法，且具备处理高次谐波与谐振条件的鲁棒性，为大规模电力系统谐波潮流与EMTP初始化提供了可行方案。
