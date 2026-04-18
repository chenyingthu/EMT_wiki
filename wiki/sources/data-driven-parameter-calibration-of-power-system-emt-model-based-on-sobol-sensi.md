---
title: "Data-Driven Parameter Calibration of Power System EMT Model Based on Sobol Sensitivity Analysis and Gaussian Mixture Model"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Systems;2025;40;1;10.1109/TPWRS.2024.3416177"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/12/Data-Driven_Parameter_Calibration_of_Power_System_EMT_Model_Based_on_Sobol_Sensitivity_Analysis_and_Gaussian_Mixture_Model.pdf"]
---

# Data-Driven Parameter Calibration of Power System EMT Model Based on Sobol Sensitivity Analysis and Gaussian Mixture Model

**作者**: 
**年份**: 2024
**来源**: `12/Data-Driven_Parameter_Calibration_of_Power_System_EMT_Model_Based_on_Sobol_Sensitivity_Analysis_and_Gaussian_Mixture_Model.pdf`

## 摘要

—The parameters of power system electromagnetic transient (EMT) model have great inﬂuences on the accuracy of EMT simulation. This paper proposes a data-driven parameter cal- ibration method based on Sobol sensitivity analysis and Gaussian mixture model (GMM) to calibrate the parameters of the power system EMT models. First, the dominant parameters of the power system EMT model are derived based on the derivative-free Sobol sensitivity analysis method. Then, the GMM that describes the relationship between the dominant parameters and the EMT simu- lation errors is established and solved. Finally, an improved particle swarm optimization algorithm is adopted to optimize the EMT simulation errors and the values of the parameters are obtained according to the minimum error and the conditional p

## 核心贡献


- 提出基于无导数Sobol灵敏度分析的主导参数筛选方法，适配各类电力系统模型
- 构建高斯混合模型映射参数与误差关系，利用条件概率不变性高效求解参数后验分布
- 提出数据驱动校准框架，无需精确模型结构与先验分布即可实现高维参数精准辨识


## 使用的方法


- [[sobol全局灵敏度分析|Sobol全局灵敏度分析]]
- [[高斯混合模型-gmm|高斯混合模型(GMM)]]
- [[改进粒子群优化算法-ipso|改进粒子群优化算法(IPSO)]]
- [[数据驱动方法|数据驱动方法]]
- [[条件概率不变性|条件概率不变性]]


## 涉及的模型


- [[电力系统emt仿真模型|电力系统EMT仿真模型]]
- [[黑盒模型|黑盒模型]]
- [[多机测试系统|多机测试系统]]


## 相关主题


- [[参数校准|参数校准]]
- [[数据驱动建模|数据驱动建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[灵敏度分析|灵敏度分析]]
- [[后验分布估计|后验分布估计]]
- [[高维优化|高维优化]]


## 主要发现


- 在四种不同系统测试中，该方法能精准校准各类电力系统EMT模型的所有主导参数
- 相比传统启发式与贝叶斯方法，该方法在高维非线性空间中具有更高计算效率与收敛精度
- GMM有效拟合参数与误差映射，结合IPSO可快速获得最小仿真误差对应的最优参数值



## 方法细节

### 方法概述

本文提出一种数据驱动的电力系统电磁暂态(EMT)模型参数校准框架。首先，采用无导数的Sobol全局灵敏度分析，通过方差分解计算各参数的一阶与总灵敏度指数，筛选出对仿真误差影响显著的主导参数，有效降低优化维度。其次，将主导参数与EMT仿真误差的联合分布建模为高斯混合模型(GMM)，利用期望最大化(EM)算法求解模型参数，并基于贝叶斯信息准则(BIC)自适应确定高斯分量数量。利用GMM的条件概率不变性，在给定误差条件下直接推导参数的后验分布。最后，引入改进粒子群优化(IPSO)算法，通过自适应惯性权重与交叉变异机制搜索最小仿真误差，结合后验分布均值计算得到最终校准参数。该方法无需精确解析模型与先验分布，适用于高维黑盒EMT模型。

### 数学公式


**公式1**: $$$V_F = \frac{1}{W} \sum (y^* - y)^2$$$

*EMT仿真误差目标函数，用于量化仿真结果与参考录波数据之间的均方误差，作为参数校准的优化目标。*


**公式2**: $$$S_i = \frac{V_{x_i}(E_{x_{-i}}(y | x_i))}{V(y)}$$$

*一阶Sobol灵敏度指数，衡量单个参数独立变化对输出方差的贡献比例。*


**公式3**: $$$S_{Ti} = \frac{E_{x_{-i}}(V_{x_i}(y | x_{-i}))}{V(y)}$$$

*总Sobol灵敏度指数，衡量单个参数及其与其他参数所有高阶交互作用对输出方差的总体贡献。*


**公式4**: $$$f(Z) = \sum_{k=1}^K \omega_k N_k(Z | \mu_k, \sigma_k)$$$

*高斯混合模型联合概率密度函数，用于拟合归一化参数与仿真误差之间的高维非线性映射关系。*


**公式5**: $$$\mu^{x\cdot y}_l = \mu^x_l + \sigma^{xy}_l (\sigma^{yy}_l)^{-1} (y - \mu^y_l)$$$

*GMM条件均值更新公式，基于条件概率不变性，在已知误差$y$时计算参数后验分布的均值向量。*


### 算法步骤

1. 数据准备与归一化：收集实际故障录波数据作为参考值$y^*$，在参数校准范围内随机采样生成多组参数组合，运行EMT仿真获取误差$V_F$。对参数向量$X$和误差向量$Y$按式(12)进行归一化处理，构建联合随机变量$Z=[X,Y]$。

2. Sobol主导参数筛选：构建蒙特卡洛采样矩阵A和B，利用式(10)和(11)计算各参数的一阶灵敏度指数$S_i$与总灵敏度指数$S_{Ti}$。设定灵敏度阈值，筛选出指数较大的参数作为主导参数子集，剔除冗余变量以降低后续计算维度。

3. GMM建模与EM求解：将主导参数与误差数据输入GMM。初始化参数集$\Omega_0$与隐变量分布，执行EM算法迭代：E步计算样本属于各高斯分量的后验概率$q^t(R_{cj})$；M步更新权重$\omega_c^t$、均值$\mu_c^t$和协方差$\sigma_c^t$。当似然函数增量小于阈值$\delta$时停止迭代。

4. BIC确定分量数$K$：在预设范围内遍历$K$值，计算自由参数$k_{fp} = K - 1 + KS + S(S+1)/2$，代入BIC公式$V_{BIC} = k_{fp} \ln(N) - 2 \ln(L)$。选取使$V_{BIC}$最小的$K$作为最优高斯分量数，防止过拟合。

5. IPSO误差优化与参数反演：初始化粒子群，位置代表归一化误差$Y$。计算粒子与全局最优粒子的距离$D_{ik}$，按$w_{ik} = w_s - (w_s - w_e)(D_{ik}-1)^2$动态更新惯性权重。若$D_{ik} < D_{min}$，则按概率$p_m$变异、按概率$p_c$交叉。将IPSO寻优得到的最小误差$y_{opt}$代入GMM条件分布，计算后验均值$\bar{X} = \sum \omega'_l \mu^{x\cdot y}_l$作为校准参数，闭环反馈至EMT模型直至收敛。


### 关键参数

- **K**: 高斯混合模型分量数量，由BIC准则自适应确定

- **δ**: EM算法迭代收敛阈值，当似然函数变化小于δ时停止迭代

- **w_s, w_e**: IPSO惯性权重的初始值与终止值，控制全局与局部搜索强度

- **p_c, p_m**: IPSO交叉率与变异率，用于打破早熟收敛并增强种群多样性

- **D_min**: 粒子与全局最优粒子的最小距离阈值，触发交叉变异操作的临界条件

- **N**: 蒙特卡洛采样点数，用于Sobol指数计算与BIC评估的样本规模



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 配电网真实实验基地 | 基于实际故障录波数据进行参数反演，网络包含变压器分接头$k$（5档选项）等关键参数。在32G内存与2.10 GHz Intel Core i7-13700处理器环境下运行，验证了方法在真实物理系统映射中的工程可行性。 | 相较于传统启发式算法与最小二乘法，该方法在高维非线性黑盒模型中避免了局部最优陷阱，且无需模型解析表达式，计算效率与校准精度显著提升。 |

| 多机测试系统及其他3个不同规模系统 | 在4个不同拓扑与复杂度的电力系统上进行泛化测试，均能准确识别并校准所有主导参数。仿真平台基于CloudPSS与Python 3.8实现数据交互。 | 框架具备强通用性，可无缝适配各类EMT仿真模型，克服了传统贝叶斯方法在高维系统中性能下降及卡尔曼滤波处理强非线性困难的问题。 |



## 量化发现

- 采用BIC准则$V_{BIC} = k_{fp} \ln(N) - 2 \ln(L)$平衡模型复杂度与拟合精度，其中自由参数严格计算为$k_{fp} = K - 1 + KS + S(S+1)/2$。
- IPSO惯性权重动态更新公式为$w_{ik} = w_s - (w_s - w_e)(D_{ik}-1)^2$，实现全局探索与局部开发的自适应切换，有效解决传统PSO权重固定导致的早熟问题。
- 参数反演直接利用条件概率均值$\bar{X} = \sum_{l=1}^K \omega'_l \mu^{x\cdot y}_l$，在误差趋近于零时直接输出最优参数估计值，避免重复调用黑盒仿真器。
- 仿真验证平台为CloudPSS与Python 3.8，硬件配置为32GB RAM与2.10 GHz Intel Core i7-13700，证明了算法在常规计算资源下的高效性与低算力依赖。


## 关键公式

### Sobol总灵敏度指数

$$$S_{Ti} = \frac{E_{x_{-i}}(V_{x_i}(y | x_{-i}))}{V(y)}$$$

*用于量化单个参数及其与其他参数交互作用对EMT仿真输出方差的总体贡献，作为筛选主导参数的核心判据。*

### GMM条件概率不变性公式

$$$f_{X|Y}(x | y) = \sum_{l=1}^K \omega'_l N_l(x | y; \mu^{x\cdot y}_l, \sigma^{xx\cdot y}_l)$$$

*在已知仿真误差$Y=y$的条件下，推导参数$X$的后验概率分布，实现从误差到参数的逆向解析映射。*

### IPSO自适应惯性权重公式

$$$w_{ik} = w_s - (w_s - w_e)(D_{ik} - 1)^2$$$

*根据粒子与全局最优解的距离动态调整搜索步长，距离大时增强全局搜索，距离小时强化局部寻优，提升收敛稳定性。*



## 验证详情

- **验证方式**: 数据驱动闭环仿真验证与对比分析
- **测试系统**: 4个不同规模与复杂度的电力系统（含配电网真实实验基地、多机测试系统等）
- **仿真工具**: CloudPSS电磁暂态仿真平台、Python 3.8、桌面PC（32GB RAM, 2.10 GHz Intel Core i7-13700）
- **验证结果**: 所提方法在4个测试系统中均成功筛选出主导参数，并通过GMM与IPSO实现高精度校准。无需依赖模型精确结构或参数先验分布，有效克服了传统梯度法易陷局部最优、卡尔曼滤波处理强非线性困难及高维贝叶斯计算缓慢等缺陷，展现出优异的泛化能力与工程实用性。
