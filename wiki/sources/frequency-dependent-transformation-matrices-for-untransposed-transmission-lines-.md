---
title: "Frequency-Dependent Transformation Matrices for Untransposed Transmission Lines using Newton-Raphson - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/59.535695.pdf.pdf"]
---

# Frequency-Dependent Transformation Matrices for Untransposed Transmission Lines using Newton-Raphson - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `19、20、21/EMT_task_20/59.535695.pdf.pdf`

## 摘要

The frequency-dependent aspects of transmission line transformation matrices along with their asymptotic behav- iours at high and low frequencies are thoroughly investigated in this paper. The Newton-Raphson (NR) method for evalu- ating the transformation matrices as smooth functions of fre- quency is introduced. A different technique which utilizes a conventional diagonalization algorithm and a correlation technique for tracking the order of the eigenvectors and ei- genvalues is used to confirm the validity of the NR method. Transformation matrices for typical line configurations are evaluated and discussed. The paper concludes that the NR method is more efficient and appropriate for use in the time domain frequency-dependent line models in the Electromag- netic Transient Program (EMTP). 

## 核心贡献


- 提出基于牛顿拉夫逊法的频变变换矩阵求解算法，实现宽频范围内特征向量的平滑连续计算
- 引入模平方和归一化约束方程，避免特征向量数值溢出，保障有理函数拟合的数值稳定性
- 克服传统对角化算法的模态跳变缺陷，为EMTP时域频变线路模型提供高效计算方案


## 使用的方法


- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[特征值对角化算法|特征值对角化算法]]
- [[模态跟踪技术|模态跟踪技术]]
- [[有理函数拟合|有理函数拟合]]
- [[梯形积分法|梯形积分法]]
- [[卡森公式|卡森公式]]


## 涉及的模型


- [[非换位输电线路|非换位输电线路]]
- [[多回架空线路|多回架空线路]]
- [[频变线路模型|频变线路模型]]
- [[地下电缆|地下电缆]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[时域仿真|时域仿真]]
- [[模态变换|模态变换]]
- [[线路参数拟合|线路参数拟合]]
- [[电磁暂态程序|电磁暂态程序]]
- [[特征值求解|特征值求解]]


## 主要发现


- 牛顿法生成的模态参数平滑连续，可精确拟合为最小相位有理函数，保障时域仿真数值稳定
- 约束牛顿法彻底消除特征向量跳变现象，计算效率与连续性显著优于传统对角化算法
- 简化大地阻抗公式计算结果与卡森积分高度一致，在宽频暂态分析中误差可忽略不计


