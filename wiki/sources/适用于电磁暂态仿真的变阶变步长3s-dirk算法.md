---
title: "适用于电磁暂态仿真的变阶变步长3S-DIRK算法"
type: source
authors: ['叶小晖']
year: 2020
journal: "电力系统自动化"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/叶小晖 等 - 2020 - 适用于电磁暂态仿真的变阶变步长3S-DIRK算法.pdf"]
---

# 适用于电磁暂态仿真的变阶变步长3S-DIRK算法

**作者**: 叶小晖
**年份**: 2020
**来源**: `40/叶小晖 等 - 2020 - 适用于电磁暂态仿真的变阶变步长3S-DIRK算法.pdf`

## 摘要

When dealing with the numerical oscillation in electromagnetic transient simulation, a lower order numerical integration switched may lead to a larger numerical error. Based on the butcher tableau, variable order and variable step 3S-DIRK algorithm is proposed.

## 核心贡献



- 提出适用于电磁暂态仿真的变阶变步长3S-DIRK算法
- 设计基于4种分算法的切换策略，保证切换时等值导纳不变且全程计算精度不低于2阶
- 利用算法的L稳定特性消除数值振荡，并支持变步长计算以提升仿真效率

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]
- [[state-space]]
- [[fixed-admittance]]

## 涉及的模型


- [[network-equivalent]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值振荡抑制|数值振荡抑制]]
- [[数值积分算法|数值积分算法]]
- [[变步长仿真|变步长仿真]]

## 主要发现



- 3S-DIRK算法在整个仿真过程中可保持不低于2阶的计算精度
- 算法的L稳定性能够有效消除电磁暂态计算中的数值振荡现象
- 算法切换策略可在不同工况下保持元件等值导纳恒定，避免切换引入的误差
- 变步长机制结合多分算法切换显著提升了复杂暂态过程的仿真效率与稳定性

## 方法细节

### 方法概述

本文基于布彻(Butcher)矩阵理论，构造了一种三级对角隐式龙格库塔(3-stage Diagonally Implicit Runge-Kutta, 3S-DIRK)积分算法框架。该框架包含4种具有不同特性的分算法：3阶高精度算法(A)、L稳定算法(B)、主动插值算法(C)和被动插值算法(D)。通过设计特定的切换策略，在保持元件等值导纳$G=\lambda/h$恒定的前提下，实现不同工况间的变阶变步长切换。正常计算时采用3阶算法保证精度，故障或开关动作期间切换至L稳定算法(隐式梯形法改造版)消除数值振荡，插值时刻采用高阶插值算法，从而在整个仿真过程中维持不低于2阶的计算精度，同时避免传统CDA方法切换至1阶后退欧拉法带来的数值误差。

### 数学公式


**公式1**: $$$$\begin{cases} F_i = f(t_n + c_i h, y_n + h \sum_{j=1}^s a_{ij} F_j) \\ y_{n+1} = y_n + h \sum_{i=1}^s b_i F_i \end{cases}$$$$

*标准s级龙格库塔法的一般形式，其中$F_i$为中间计算变量，$h$为步长，$a_{ij}$、$b_i$、$c_i$为算法系数*


**公式2**: $$$$\begin{array}{c|c} \mathbf{c} & \mathbf{A} \\ \hline & \mathbf{b}^\mathrm{T} \end{array}$$$$

*布彻(Butcher)矩阵表示法，用于描述龙格库塔算法的系数结构，其中$\mathbf{A}$为权重矩阵，$\mathbf{b}$为权重向量，$\mathbf{c}$为节点向量*


**公式3**: $$$$\mathbf{b}^T \cdot \mathbf{e} = 1, \quad \mathbf{b}^T \cdot \mathbf{C} \cdot \mathbf{e} = \frac{1}{2}, \quad \mathbf{b}^T \cdot \mathbf{C} \cdot \mathbf{C} \cdot \mathbf{e} = \frac{1}{3}, \quad \mathbf{b}^T \cdot \mathbf{A} \cdot \mathbf{C} \cdot \mathbf{e} = \frac{1}{6}$$$$

*龙格库塔算法精度阶数判定条件，分别对应1阶、2阶、3阶精度要求，其中$\mathbf{e}$为单位列向量，$\mathbf{C}=\mathrm{diag}\{c_1,c_2,...,c_s\}$*


**公式4**: $$$$\begin{array}{c|ccc} 0 & 0 & 0 \\ 2\lambda & \lambda & \\ \frac{6\lambda-4\lambda^2-1}{4\lambda} & \frac{1-2\lambda}{4\lambda} & \lambda \\ \hline & \frac{6\lambda-4\lambda^2-1}{4\lambda} & \frac{1-2\lambda}{4\lambda} & \lambda \end{array}$$$$

*3S-DIRK算法的通用布彻矩阵形式(式17)，满足对角隐式(DIRK)条件且主对角元相同($a_{ii}=\lambda$)，具备2阶计算精度基础框架*


**公式5**: $$$$\lambda = \frac{1-\sqrt{3}}{3} \approx 0.423 \quad \text{或} \quad \lambda = \frac{1+\sqrt{3}}{3} \approx 0.577$$$$

*算法A（3阶算法）的参数取值，满足式(7)(8)的3阶精度条件，在正常计算工况下使用以实现3阶精度*


**公式6**: $$$$\lambda = 1 - \frac{\sqrt{2}}{2} \approx 0.293 \quad \text{或} \quad \lambda = 1 + \frac{\sqrt{2}}{2} \approx 1.707$$$$

*算法B（L稳定算法）的参数取值，满足$\lim_{z\to-\infty}R(z)=0$的L稳定条件，用于故障期间消除数值振荡*


**公式7**: $$$$\lambda_{\text{插}} = \frac{\lambda}{k}$$$$

*算法C（主动插值算法）的参数关系，其中$k$为插值系数，通过调整等效步长实现开关时刻的精确插值计算*


**公式8**: $$$$R(z) = \frac{2\lambda(2\lambda^2-4\lambda+1)z^2 - (4\lambda^2+2\lambda-1)z}{4\lambda(1-\lambda z)^2}$$$$

*3S-DIRK算法的稳定函数，用于分析算法稳定性，当$\lambda=1-\sqrt{2}/2$时具备L稳定性（即$R(\infty)=0$）*


**公式9**: $$$$G_{\text{eq}} = \frac{\lambda}{h} = \text{常数}$$$$

*等值导纳恒定条件，通过调整步长$h$与参数$\lambda$的乘积保持不变，确保算法切换时无需重构导纳矩阵*


### 算法步骤

1. 初始化：设置基础步长$h_0$，根据初始工况选择初始算法（通常选用算法A，$\lambda=1-\sqrt{3}/3$），计算并因子化初始导纳矩阵$G=\lambda/h_0$

2. 正常积分步：采用算法A（3阶，$\lambda\approx0.423$）进行电磁暂态计算，利用式(17)的三级计算结构求解微分代数方程，保持3阶计算精度

3. 故障/开关检测：当检测到系统发生故障、开关动作或状态突变时，触发算法切换机制，准备转入数值振荡抑制模式

4. 切换至L稳定模式：将算法参数切换至算法B（$\lambda=1-\sqrt{2}/2\approx0.293$），同时按比例调整步长$h_{\text{new}}=h_0\cdot\frac{1-\sqrt{2}/2}{1-\sqrt{3}/3}$，保持等值导纳$G$不变，利用L稳定性消除非状态变量突变引起的数值振荡

5. 插值计算：在开关动作时刻需要精确同步时，采用算法C（主动插值，$\lambda_{\text{插}}=\lambda/k$）或算法D（被动二阶拉格朗日插值），通过插值系数$k$确定中间时刻的状态变量值

6. 步长调整：根据局部截断误差估计或仿真速度需求，执行变步长策略，调整步长$h$但同步调整$\lambda$保持$\lambda/h$恒定，或在不改变$\lambda$的情况下直接改变步长（被动变步长）

7. 返回正常模式：故障清除或暂态过程结束后，切换回算法A恢复3阶高精度计算，步长恢复至$h_0$，继续保持导纳矩阵不变


### 关键参数

- **$\lambda$**: 对角元参数，决定算法特性，取值$1-\sqrt{3}/3$（3阶）、$1-\sqrt{2}/2$（L稳定）等

- **$h$**: 仿真积分步长，可在$10^{-6}\sim10^{-3}$秒范围内变化

- **$k$**: 插值系数，$0<k<1$，用于确定插值点位置

- **$G_{\text{eq}}$**: 等值导纳，$G=\lambda/h$，在算法切换过程中保持恒定以避免矩阵重构

- **$R(z)$**: 稳定函数，$z=h\cdot\lambda_{\text{eigen}}$，用于判稳定性



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 电力电子开关动作仿真 | 验证在频繁开关动作下，3S-DIRK算法相比传统CDA方法（临界阻尼调整法）的精度优势。CDA方法在抑制数值振荡时切换至后退欧拉法导致精度降至1阶，而3S-DIRK全程保持不低于2阶精度，在开关动作时刻的电压电流波形误差控制在2阶精度范围内 | 相比传统CDA方法（精度降至1阶），计算精度提升1个阶次；与隐式梯形法相比，消除了数值振荡（抑制率100%） |

| 故障暂态过程仿真 | 模拟系统故障及切除过程，验证L稳定算法对数值振荡的消除效果。在故障期间采用$\lambda=1-\sqrt{2}/2$的L稳定算法，故障清除后切换回3阶算法，等值导纳始终保持恒定，无需重新因子化导纳矩阵 | 仿真效率提升，因避免了导纳矩阵的重复重构；数值振荡幅值衰减至0（L稳定特性），而传统梯形法会产生持续振荡 |



## 量化发现

- 计算精度：正常工况下达到3阶精度（局部截断误差$O(h^4)$），故障及整个仿真过程中全程保持不低于2阶精度（局部截断误差$O(h^3)$），而传统CDA方法在故障期间降至1阶
- 算法参数具体数值：3阶算法$\lambda=\frac{1-\sqrt{3}}{3}\approx0.42265$，L稳定算法$\lambda=1-\frac{\sqrt{2}}{2}\approx0.29289$，2S-DIRK算法$\lambda=\frac{2-\sqrt{2}}{2}\approx0.29289$（与3S-DIRK的L稳定形式一致）
- 稳定特性：当$\lambda=1-\sqrt{2}/2$时，稳定函数满足$R(\infty)=0$，具备L稳定性，可完全消除数值振荡；当$\lambda=1-\sqrt{3}/3$时，具备A稳定性且精度最优
- 矩阵计算效率：由于保持等值导纳$G=\lambda/h$恒定，算法切换时导纳矩阵无需重新因子化，计算量节省约30%-50%（避免了每步重构矩阵的运算）
- 步长调节范围：支持变步长计算，步长调节比例与$\lambda$取值匹配，如从$\lambda=0.423$切换至$\lambda=0.293$时，步长同比调整至约69.3%以保持导纳不变


## 关键公式

### 3S-DIRK通用布彻矩阵

$$$$\begin{array}{c|ccc} 0 & 0 & 0 \\ 2\lambda & \lambda & \\ \frac{6\lambda-4\lambda^2-1}{4\lambda} & \frac{1-2\lambda}{4\lambda} & \lambda \\ \hline & \frac{6\lambda-4\lambda^2-1}{4\lambda} & \frac{1-2\lambda}{4\lambda} & \lambda \end{array}$$$$

*作为整个算法的核心框架，通过改变$\lambda$值实现不同特性算法的切换，用于电磁暂态仿真的主积分器*

### 3S-DIRK稳定函数

$$$$R(z) = \frac{2\lambda(2\lambda^2-4\lambda+1)z^2 - (4\lambda^2+2\lambda-1)z}{4\lambda(1-\lambda z)^2}$$$$

*用于分析算法稳定性，判断是否存在数值振荡，当选择特定$\lambda$值使分子次数低于分母时实现L稳定*

### 3阶精度约束条件

$$$$\mathbf{b}^T \cdot \mathbf{C} \cdot \mathbf{e} = \frac{1}{2}, \quad \mathbf{b}^T \cdot \mathbf{C} \cdot \mathbf{C} \cdot \mathbf{e} = \frac{1}{3}, \quad \mathbf{b}^T \cdot \mathbf{A} \cdot \mathbf{C} \cdot \mathbf{e} = \frac{1}{6}$$$$

*用于求解$\lambda$的具体数值，确保算法A达到3阶精度，是算法设计的基础约束方程*



## 验证详情

- **验证方式**: 数字仿真验证（对比分析）
- **测试系统**: 包含电力电子元件的电磁暂态系统（具体为验证算法切换策略和变步长特性的测试系统，以及验证L稳定性的故障系统）
- **仿真工具**: 基于节点电压法的电磁暂态仿真程序（兼容EMTP架构），支持DIRK算法自定义实现
- **验证结果**: 通过2个典型算例验证：1）验证了算法切换时等值导纳恒定，无需重构导纳矩阵；2）验证了全程2阶以上精度，故障期间无数值振荡；3）验证了变步长计算的有效性和效率提升。相比传统CDA方法，在保持数值稳定的同时显著提高了计算精度，证明了3S-DIRK算法在含电力电子元件的复杂电力系统电磁暂态仿真中的优越性
