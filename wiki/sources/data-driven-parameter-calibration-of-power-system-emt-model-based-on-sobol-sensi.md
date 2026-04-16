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


