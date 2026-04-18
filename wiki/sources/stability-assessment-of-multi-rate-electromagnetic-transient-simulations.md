---
title: "Stability Assessment of Multi-Rate Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;6;10.1109/TPWRD.2025.3590630"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/Sinkar 等 - 2025 - Stability Assessment of Multi-Rate Electromagnetic Transient Simulations.pdf"]
---

# Stability Assessment of Multi-Rate Electromagnetic Transient Simulations

**作者**: 
**年份**: 2025
**来源**: `35/Sinkar 等 - 2025 - Stability Assessment of Multi-Rate Electromagnetic Transient Simulations.pdf`

## 摘要

—Multi-rate Electromagnetic Transient (EMT) simu- lations use smaller time-steps for parts of the network requiring greater accuracy, and larger time-steps for the rest of the network. This paper presents an analytical approach for evaluating the stability of multi-rate EMT simulations of linear time-invariant (LTI) networks. It is shown that their resulting discrete time sys- tem is inherently time-periodic. Leveraging this characteristic, a sampled-data time-invariant representation of the simulated net- work is derived. The overall simulation’s numerical stability can then be assessed through eigenvalue analysis. The paper shows that contrary to popular belief, a multi-rate EMT simulation may become unstable even if the well-known A-stable trapezoidal rule is used. The proposed approach

## 核心贡献



- 提出了一种评估线性时不变（LTI）网络多速率电磁暂态（EMT）仿真稳定性的解析方法
- 推导了多速率仿真网络的采样数据时不变表示，并建立了基于特征值分析的数值稳定性评估框架

## 使用的方法


- [[multirate]]
- [[numerical-integration]]
- [[state-space]]
- [[interpolation]]

## 涉及的模型


- [[network-equivalent]]

## 相关主题


- [[multirate]]
- [[numerical-integration]]

## 主要发现



- 多速率EMT仿真生成的离散时间系统本质上是时间周期性的
- 即使采用A稳定的梯形积分法则，多速率EMT仿真仍可能出现数值不稳定现象
- 通过特征值分析采样数据时不变模型可准确预测和评估整体仿真的数值稳定性

## 方法细节

### 方法概述

该论文提出了一种基于离散时间周期性提升（lifting）技术的解析方法，用于评估线性时不变（LTI）网络多速率电磁暂态（EMT）仿真的数值稳定性。方法核心在于识别多速率仿真（快速子网络采用小步长Δt，慢速子网络采用大步长ΔT=NΔt）在离散时间域呈现周期性时变特性（周期为ΔT）。通过将周期性时变离散系统转换为等效的采样数据时不变表示（sampled-data time-invariant representation），利用特征值分析判断整体仿真的数值稳定性。该方法适用于非迭代式多速率仿真算法（如基于MATE的方法），可检测即使在使用A稳定梯形积分法则时仍可能出现的不稳定现象。

### 数学公式


**公式1**: $$$\dot{x} = Ax$$$

*连续时域自治LTI系统的状态空间方程，其中A为系统矩阵，x为状态向量*


**公式2**: $$$x(t + \Delta t) = Gx(t)$$$

*单速率离散化后的状态转移方程，G为单步长状态转移矩阵*


**公式3**: $$$G = (I - A\Delta t/2)^{-1}(I + A\Delta t/2)$$$

*采用梯形积分法则（Trapezoidal Rule）时的状态转移矩阵计算式，I为单位矩阵*


**公式4**: $$$\Delta T = N\Delta t, \quad N \in \mathbb{Z}^+, N > 1$$$

*多速率时间步长关系，N为大步长与小步长的整数比*


**公式5**: $$$x(t + \Delta t) = G_0 x(t)$
$x(t + 2\Delta t) = G_1 x(t + \Delta t)$
$\vdots$
$x(t + N\Delta t) = G_{N-1} x(t + (N-1)\Delta t)$$$

*多速率仿真在一个周期ΔT内的分段状态转移，Gk为第k个小步长间隔的时变转移矩阵（因快慢子网络交替更新和采样保持/插值而随k变化）*


**公式6**: $$$X^L(t) = \begin{bmatrix} x(t) \\ x(t + \Delta t) \\ \vdots \\ x(t + (N-1)\Delta t) \end{bmatrix}$$$

*提升（lifting）操作定义的扩展状态向量，将N个连续小步长的状态堆叠，将周期性时变系统转化为时不变系统*


**公式7**: $$$M^L X^L(t + \Delta T) = H^L X^L(t)$$$

*提升后的时不变离散时间系统表示，ML和HL为常数矩阵，用于特征值稳定性分析*


**公式8**: $$$M^L = \begin{bmatrix} I & 0 & \cdots & 0 \\ 0 & I & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{bmatrix}, \quad
H^L = \begin{bmatrix} 0 & 0 & \cdots & G_{N-1} \\ -I & 0 & \cdots & G_{N-2} \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & -I & G_0 \end{bmatrix}$$$

*提升技术中的结构矩阵，ML为选择矩阵（最后一行为零向量），HL包含各子周期转移矩阵Gk和负单位矩阵-I，建立跨周期ΔT的状态映射*


### 算法步骤

1. 网络划分与时间步长选择：将LTI网络划分为快速子网络（需高精度）和慢速子网络，确定小步长Δt和大步长ΔT，确保ΔT = NΔt（N为大于1的整数）

2. 子网络接口处理定义：明确上采样（up-sampling，慢速到快速）方法（如冻结值、线性插值或外推）和下采样（down-sampling，快速到慢速）方法（如最后值采样或平均）

3. 周期性状态转移矩阵推导：在一个完整周期ΔT内，推导每个小步长Δt间隔的状态转移矩阵G0, G1, ..., GN-1，考虑快慢子网络交替求解和接口变量传递机制

4. 提升状态空间构建：应用lifting技术，构造扩展状态向量XL(t) = [x(t)T, x(t+Δt)T, ..., x(t+(N-1)Δt)T]T，将N步周期性时变系统映射为单步时不变系统

5. 时不变系统矩阵组装：按照M^L X^L(t+ΔT) = H^L X^L(t)的形式组装矩阵ML和HL，其中ML为块对角矩阵（最后一行零块），HL包含Gk矩阵和负单位矩阵的特定排列

6. 特征值稳定性判定：计算矩阵(ML)^(-1)HL（或广义特征值问题det(HL - λML) = 0）的特征值，若所有特征值位于复平面单位圆内（|λ| < 1），则多速率仿真数值稳定


### 关键参数

- **N**: 大步长与小步长之比，必须为正整数且N > 1，决定系统周期性和提升向量的维度

- **Δt**: 快速子网络仿真时间步长，用于捕捉高频动态

- **ΔT**: 慢速子网络仿真时间步长，ΔT = NΔt，为系统周期性重复的时间间隔

- **Gk**: 第k个中间步长的离散状态转移矩阵（k = 0, 1, ..., N-1），在多速率仿真中因子网络交替激活和接口插值/保持策略而随k变化

- **XL**: 提升后的状态向量，维度为原状态向量维度的N倍，包含一个完整周期内所有中间时刻的状态

- **A**: 连续系统状态矩阵，决定原LTI网络的动态特性



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 提供的文本片段未包含具体仿真测试案例的详细数值结果 | 论文摘要和引言部分指出，所提方法通过特征值分析可预测多速率仿真的数值稳定性，并发现即使采用A稳定梯形法则仍可能出现不稳定现象，但具体验证案例的数值数据（如误差百分比、仿真耗时等）在提供的Section I-II片段中未展示 | 方法对比了传统单速率仿真（全网络使用Δt）与多速率仿真（分区使用Δt和ΔT）的稳定性特征，指出多速率引入的周期性时变特性可能导致单个子网络稳定但整体仿真不稳定的情况 |



## 量化发现

- 时间步长必须满足整数倍关系：ΔT = NΔt，其中N为严格大于1的整数（N ∈ ℤ+, N > 1），这是应用lifting技术和周期性分析的前提条件
- 离散系统呈现N周期性：在一个大步长周期ΔT内，系统经历N个不同的状态转移矩阵G0, G1, ..., GN-1，形成周期为N的时变离散系统
- 提升后系统维度扩展：通过lifting技术，原n维状态空间扩展为n×N维，时不变表示矩阵ML和HL的维度为(nN)×(nN)
- 矩阵HL具有特定的块下Hessenberg结构：包含负单位矩阵-I在主次对角线下方，以及转移矩阵Gk在最后一列块
- 稳定性判据：多速率仿真系统稳定的充要条件是矩阵对(ML, HL)的广义特征值均位于单位圆内，即|λ(HL, ML)| < 1
- 与单速率仿真的关键差异：单速率使用固定G矩阵，而多速率使用周期性变化的Gk序列，这破坏了单速率下梯形法则A稳定性保证整体稳定的性质


## 关键公式

### 提升后的时不变状态方程

$$$M^L X^L(t + \Delta T) = H^L X^L(t)$$$

*这是论文的核心数学结果，通过lifting技术将周期性时变的多速率离散系统转化为等效的时不变系统，使得可以应用标准特征值分析评估稳定性。适用于任何非迭代式多速率EMT仿真算法（如基于MATE或LIM的方法）。*

### 多速率周期性状态转移

$$$x(t + (k+1)\Delta t) = G_k x(t + k\Delta t), \quad k = 0, 1, \ldots, N-1$$$

*描述在一个大步长ΔT = NΔt周期内，由于快慢子网络交替求解和接口采样保持/插值策略，状态转移矩阵Gk随步数k变化，体现多速率仿真的本质时变特性。*



## 验证详情

- **验证方式**: 基于LTI系统特征值分析的解析验证方法（文中提及将在后续章节通过示例仿真验证，但提供的文本片段未包含具体验证细节）
- **测试系统**: 针对线性时不变（LTI）网络的理论分析框架，适用于任意可划分为快速和慢速子网络的LTI系统（具体测试系统如IEEE标准系统或自定义电路在提供的片段中未明确）
- **仿真工具**: 理论推导涉及状态空间分析和矩阵计算；仿真实现提及基于MATE（Multi Area Thevenin Equivalent）的多速率EMT仿真方法，但未明确指定商用仿真软件（如PSCAD/EMTDC、MATLAB/Simulink或RTDS）的具体版本
- **验证结果**: 理论分析表明：1) 多速率EMT仿真产生周期性时变离散系统；2) 通过lifting技术可获得等效时不变表示；3) 即使各子网络使用A稳定的梯形法则且原连续系统稳定，多速率仿真仍可能因周期性耦合而数值不稳定。具体数值算例结果在提供的Section I-II文本中未包含。
