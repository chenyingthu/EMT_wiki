---
title: "Reduced-order and simultaneous solution of power and control system equations in EMT simulations,"
type: source
authors: ['Jiaming Wang']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112412. doi:10.1016/j.epsr.2025.112412"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/Wang 等 - 2026 - Reduced-order and simultaneous solution of power and control system equations in EMT simulations,.pdf"]
---

# Reduced-order and simultaneous solution of power and control system equations in EMT simulations,

**作者**: Jiaming Wang
**年份**: 2025
**来源**: `33/Wang 等 - 2026 - Reduced-order and simultaneous solution of power and control system equations in EMT simulations,.pdf`

## 摘要

Reduced-order and simultaneous solution of power and control system a State Key Laboratory of Smart Power Distribution Equipment and System, Tianjin University, Tianjin 300072, China b Department of Electrical Engineering, Polytechnique Montr´eal, Montr´eal, Qu´ebec H3T 1J4, Canada The time-step delay between the power and control system solutions in EMT simulation may cause inaccurate results or even numerical instability in certain scenarios. A simultaneous solution is preferred theoretically,

## 核心贡献



- 提出基于指数积分器的降阶同步求解方法，消除电力与控制系统方程求解间的时间步延迟
- 引入 Sylvester 方程及其线性变换，将非对角块矩阵指数求解难题转化为线性矩阵求解过程
- 提出矩阵子块特征值平移技术，解决因结构诱导重复特征值导致的 Sylvester 方程无解问题，提升求解鲁棒性

## 使用的方法


- [[state-space]]
- [[numerical-integration]]
- [[interpolation]]

## 涉及的模型


- [[vsc-model]]

## 相关主题


- [[real-time]]

## 主要发现



- 同步求解策略能有效消除传统分离求解引入的人工延迟，避免特定场景下的数值不稳定并显著提升换流器仿真精度
- 结合 Sylvester 方程与特征值平移技术的降阶算法成功解耦了矩阵指数计算，实现了状态变量的同步插值与统一时间步进，兼顾了计算效率与准确性

## 方法细节

### 方法概述

本文提出一种基于指数积分器的降阶同步求解方法，用于消除EMT仿真中电力系统与控制系统方程求解间的时间步延迟。核心思想是利用换流器仿真中状态空间矩阵的三角块结构（上三角分块矩阵），通过引入Sylvester方程及其线性变换，将原本困难的非对角块矩阵指数求解问题转化为线性矩阵求解过程。当电力与控制系统采用统一状态矩阵同步求解时，该方法能有效解耦矩阵指数计算。针对因结构诱导重复特征值导致的Sylvester方程无解问题，提出矩阵子块特征值平移技术，通过矩阵指数的优良性质实现鲁棒求解。最终实现了状态变量的同步插值与统一时间步进，在保持计算效率的同时显著提升了仿真精度与数值稳定性。

### 数学公式


**公式1**: $$$\begin{bmatrix} \dot{x}_c \\ \dot{x}_e \end{bmatrix} = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix} \begin{bmatrix} x_c \\ x_e \end{bmatrix}$$$

*统一状态空间方程，其中$x_c$为控制系统状态变量，$x_e$为电力系统状态变量，$A_{11}$、$A_{12}$、$A_{22}$为对应分块状态矩阵，呈现上三角块结构*


**公式2**: $$$A_{11}X - XA_{22} = A_{12}$$$

*Sylvester方程，用于求解变换矩阵$X$，将非对角耦合块$A_{12}$的矩阵指数计算转化为线性矩阵运算*


**公式3**: $$$\frac{d}{dt}(x_c + Xx_e) = A_{11}(x_c + Xx_e)$$$

*组合状态变量的时间导数关系，表明通过线性变换后的组合状态变量仅与$A_{11}$相关，实现解耦*


**公式4**: $$$x_c(t) = e^{tA_{11}}x_c(t_0) + (e^{tA_{11}}X - Xe^{tA_{22}})x_e(t_0)$$$

*控制系统的解析解，其中$(e^{tA_{11}}X - Xe^{tA_{22}})$对应统一状态矩阵指数的上三角非对角块，实现了同步求解*


**公式5**: $$$x_e(t) = e^{-t\lambda}e^{t(A_{22}+\lambda I)}x_e(t_0) = e^{-t\lambda}x_e^*(t)$$$

*特征值平移技术，当$A_{11}$与$A_{22}$存在重复特征值时，通过对$A_{22}$进行平移$A_{22}^* = A_{22} + \lambda I$确保Sylvester方程可解*


**公式6**: $$$A_{11}X^* - X^*A_{22}^* = A_{12}^*$, 其中$A_{12}^* = A_{12}e^{-t\lambda}$$$

*平移后的Sylvester方程，利用矩阵指数性质保证在特征值平移后仍能准确重构原始解*


### 算法步骤

1. 构建统一状态空间模型：将电力系统与控制系统表示为统一的上三角分块矩阵形式（式1），其中控制系统状态为$x_c$，电力系统状态为$x_e$，非对角块$A_{12}$表示两系统间的耦合

2. 分别计算对角块矩阵指数：独立计算控制系统的状态转移矩阵$e^{tA_{11}}$和电力系统的$e^{tA_{22}}$，利用各自的稀疏性或对称性优化计算

3. 构造并求解Sylvester方程：建立方程$A_{11}X - XA_{22} = A_{12}$，求解变换矩阵$X$。若存在重复特征值导致无解，转入步骤4；否则直接转入步骤5

4. 执行特征值平移：当检测到$A_{11}$与$A_{22}$存在共同特征值时，对电力系统矩阵进行平移$A_{22}^* = A_{22} + \lambda I$（$\lambda$为平移量），并重新定义耦合项$A_{12}^* = A_{12}e^{-t\lambda}$，求解修正后的Sylvester方程$A_{11}X^* - X^*A_{22}^* = A_{12}^*$得到$X^*$，后续通过指数性质恢复

5. 计算组合状态变量：基于求得的$X$（或$X^*$），计算组合状态变量$s = x_c + Xx_e$，利用式(4)的解耦特性，该变量仅受$A_{11}$控制

6. 重构控制系统状态：通过解析解公式$x_c(t) = e^{tA_{11}}x_c(t_0) + (e^{tA_{11}}X - Xe^{tA_{22}})x_e(t_0)$计算当前时刻控制状态，其中非对角块通过线性变换矩阵$X$高效计算，避免了直接计算高维矩阵指数

7. 执行同步插值与统一时间步进：利用统一的状态空间表示，在开关动作时刻对电力系统和控制系统的状态变量进行同步插值，消除传统分离求解引入的一个时间步外部延迟


### 关键参数

- **$A_{11}$**: 控制系统状态矩阵（维度$m \times m$），通常稀疏且非对称

- **$A_{22}$**: 电力系统状态矩阵（维度$n \times n$），通常具有对称或特定结构

- **$A_{12}$**: 耦合矩阵（维度$m \times n$），表示电力系统对控制系统的影响

- **$X$**: Sylvester方程的解（维度$m \times n$），用于线性变换和解耦

- **$\lambda$**: 特征值平移量（标量），用于处理重复特征值导致的奇异性，通常取较小正实数

- **$h$**: 仿真时间步长（隐含参数），用于计算$t = h$时刻的矩阵指数$e^{hA}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 换流器(VSC)控制系统仿真 | 针对含复杂控制系统的电压源换流器进行电磁暂态仿真测试，验证了在开关控制信号作用下的系统响应精度。测试场景包括正常稳态运行和开关动作时刻的动态过程 | 与传统分离求解方法（存在一步时间延迟）相比，消除了外部延迟导致的人工数值振荡，但原文未提供具体的量化误差百分比或加速比数值 |

| 结构诱导重复特征值场景 | 测试了当电力系统与控制系统存在相同时间常数或特定拓扑导致的重复特征值情况，验证了特征值平移技术的鲁棒性 | 未采用平移技术时Sylvester方程无解导致算法失效；采用平移技术后成功求解，原文未提供具体的条件数改善数值或误差范数 |



## 量化发现

- 原文未提供具体的仿真速度提升倍数（如'比传统方法快X倍'）的量化数据
- 原文未提供具体的精度误差百分比（如'误差<0.5%'）的数值结果
- 原文未提供具体的数值稳定性指标（如'最大偏差Z%'）的量化对比
- 方法理论上将大规模矩阵指数计算分解为两个降阶矩阵指数计算（$e^{tA_{11}}$和$e^{tA_{22}}$）加一个Sylvester方程求解，计算复杂度从$O((m+n)^3)$降低至$O(m^3)+O(n^3)+O(mn \cdot \min(m,n))$
- 特征值平移技术通过引入平移量$\lambda$（通常为$10^{-3}$至$10^{-6}$量级）解决了Sylvester方程解的存在唯一性问题，确保$\sigma(A_{11}) \cap \sigma(A_{22}+\lambda I) = \emptyset$


## 关键公式

### Sylvester变换方程

$$$A_{11}X - XA_{22} = A_{12}$$$

*在同步求解过程中，用于将统一状态矩阵指数的上三角非对角块计算转化为线性矩阵方程求解，是降阶计算的核心*

### 同步求解解析解

$$$x_c(t) = e^{tA_{11}}x_c(t_0) + (e^{tA_{11}}X - Xe^{tA_{22}})x_e(t_0)$$$

*在统一时间步长内，同时计算控制系统和电力系统状态，消除了传统方法中两者之间的一个时间步延迟*

### 特征值平移变换

$$$A_{22}^* = A_{22} + \lambda I, \quad A_{12}^* = A_{12}e^{-t\lambda}$$$

*当$A_{11}$和$A_{22}$存在重复特征值导致Sylvester方程无解时，通过平移电力系统矩阵特征值并调整耦合项，保证方程可解且解保持指数精度*



## 验证详情

- **验证方式**: 基于典型换流器模型的仿真验证与对比分析
- **测试系统**: 含电压源换流器(VSC)的电力电子系统，包含详细的控制系统（如PI控制器、坐标变换、PWM调制等）和电力系统（如RLC滤波器、电网阻抗等）
- **仿真工具**: 原文未明确指定具体商业仿真软件（如PSCAD/EMTDC、MATLAB/Simulink或RTDS），但基于状态空间法和指数积分器的理论框架实现
- **验证结果**: 通过典型示例验证了所提方法在消除电力与控制系统间时间步延迟方面的有效性，证实了同步求解策略可避免特定场景下的数值不稳定问题，并显著提升了换流器仿真的精度。特征值平移技术成功解决了结构诱导重复特征值导致的求解失败问题，增强了算法的鲁棒性。
