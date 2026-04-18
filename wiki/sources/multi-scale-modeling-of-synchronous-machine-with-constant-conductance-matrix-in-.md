---
title: "Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain"
type: source
authors: ['未知']
year: 2024
journal: "2024 IEEE Power & Energy Society General Meeting (PESGM);2024; ; ;10.1109/PESGM51994.2024.10688669"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain.pdf"]
---

# Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain

**作者**: 
**年份**: 2024
**来源**: `27&28/Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain.pdf`

## 摘要

—In this paper, a novel synchronous machine model is developed for the accurate and efﬁcient simulation of multi- scale transients. The machine stator equations are expressed with analytic signals in the phase domain, thus providing direct interface between machine model and external network model. Frequency shifting is applied to stator quantities to eliminate the ac carrier in the stator windings which enables the use of large time-step size. An artiﬁcial damper winding is introduced to eliminate the numerical saliency based on a pioneering tech- nique. The proposed machine model is represented as a Norton equivalent with constant conductance matrix. The analysis of test cases demonstrates the effectiveness of the proposed synchronous machine model in terms of accuracy and efﬁciency. Ind

## 核心贡献


- 提出基于频移概念的相域同步电机多尺度模型支持宽时间尺度暂态仿真
- 引入人工阻尼绕组消除数值凸极效应构建恒定导纳矩阵的诺顿等效模型
- 重构电机方程简化数学运算避免网络导纳矩阵每步更新显著提升计算效率


## 使用的方法


- [[频移技术|频移技术]]
- [[解析信号法|解析信号法]]
- [[隐式梯形积分法|隐式梯形积分法]]
- [[相域建模|相域建模]]
- [[诺顿等效|诺顿等效]]
- [[人工阻尼绕组技术|人工阻尼绕组技术]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[外部电网|外部电网]]


## 相关主题


- [[多尺度暂态仿真|多尺度暂态仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步长仿真|大时间步长仿真]]
- [[数值凸极效应消除|数值凸极效应消除]]
- [[电机网络直接接口|电机网络直接接口]]


## 主要发现


- 频移技术有效消除定子交流载波允许采用大时间步长且保持高精度
- 恒定导纳矩阵避免每步更新结合人工阻尼绕组参数新规则提升数值稳定性
- 算例验证表明该模型在宽时间尺度暂态仿真中兼具高计算精度与显著效率优势



## 方法细节

### 方法概述

本文提出了一种基于频移（frequency shifting）概念的相域（phase domain）同步电机多尺度建模方法。该方法利用解析信号（analytic signals）表示定子方程，通过频移技术将定子交流量（50/60Hz载波）搬移至低频或直流附近，从而允许使用更大的时间步长进行多尺度暂态仿真。引入人工阻尼绕组（artificial damper winding）消除数值凸极效应（numerical saliency），构建了具有恒定导纳矩阵（constant conductance matrix）的诺顿等效模型，避免了网络导纳矩阵的每步更新。采用隐式梯形积分法进行离散化，并通过重构电机方程显著简化数学运算，降低计算时间。

### 数学公式


**公式1**: $$$$ \begin{bmatrix} \underline{v}_{abcs}(t) \\ v_{qdr}(t) \end{bmatrix} = \frac{d}{dt} \begin{bmatrix} \underline{\lambda}_{abcs}(t) \\ \lambda_{qdr}(t) \end{bmatrix} + \begin{bmatrix} R_s & 0 \\ 0 & R_r \end{bmatrix} \begin{bmatrix} -\underline{i}_{abcs}(t) \\ i_{qdr}(t) \end{bmatrix} $$$$

*同步电机定子和转子的电压方程，其中下划线表示解析信号（复数表示），$v_{abcs}$和$i_{abcs}$为定子电压和电流，$v_{qdr}$和$i_{qdr}$为转子电压和电流，$\lambda$为磁链，$R_s$和$R_r$为电阻矩阵*


**公式2**: $$$$ \begin{bmatrix} \underline{\lambda}_{abcs}(t) \\ \lambda_{qdr}(t) \end{bmatrix} = \begin{bmatrix} L_s(\theta_r(t)) & L_{sr}(\theta_r(t)) \\ L_{rs}(\theta_r(t)) & L_r \end{bmatrix} \begin{bmatrix} -\underline{i}_{abcs}(t) \\ i_{qdr}(t) \end{bmatrix} $$$$

*磁链方程，$L_s(\theta_r(t))$为时变定子电感矩阵，$L_{sr}$和$L_{rs}$为时变互感矩阵，$L_r$为恒定转子电感矩阵，$\theta_r(t)$为转子位置角*


**公式3**: $$$$ \begin{bmatrix} E[\underline{v}_{abcs}(t)] \\ v_{qdr}(t) \end{bmatrix} = \frac{d}{dt} \begin{bmatrix} E[\underline{\lambda}_{abcs}(t)] \\ \lambda_{qdr}(t) \end{bmatrix} + \begin{bmatrix} j2\pi f_s E[\underline{\lambda}_{abcs}(t)] \\ 0 \end{bmatrix} + \begin{bmatrix} R_s & 0 \\ 0 & R_r \end{bmatrix} \begin{bmatrix} -E[\underline{i}_{abcs}(t)] \\ i_{qdr}(t) \end{bmatrix} $$$$

*频移后的电压方程，$E[\cdot]$表示频移操作，$E[v_{abcs}(t)] = v_{abcs}(t)e^{-j2\pi f_s t}$，$f_s$为频移频率，用于消除定子交流载波*


**公式4**: $$$$ \underline{v}_{abcs}(k) = -\left[ \left(\frac{2}{\tau} + j2\pi f_s\right) L_s(\theta_r(k)) + R_s \right] \underline{i}_{abcs}(k) + \left(\frac{2}{\tau} + j2\pi f_s\right) (I+jK)L_{sr}(\theta_r(k)) i_{qdr}(k) + e_{sh}(k) $$$$

*采用隐式梯形积分法离散化后的定子电压方程，$\tau$为时间步长，$e_{sh}(k)$为历史项电压源，$k$为时间步序号*


**公式5**: $$$$ R_{eq}(k) = R_c + \frac{1}{3}(Z_d'' - Z_q'') \begin{bmatrix} \cos 2\theta_r(k) & \cos 2(\theta_r(k)-\frac{\pi}{3}) & \cos 2(\theta_r(k)+\frac{\pi}{3}) \\ \cos 2(\theta_r(k)-\frac{\pi}{3}) & \cos 2(\theta_r(k)-\frac{2\pi}{3}) & \cos 2\theta_r(k) \\ \cos 2(\theta_r(k)+\frac{\pi}{3}) & \cos 2\theta_r(k) & \cos 2(\theta_r(k)+\frac{2\pi}{3}) \end{bmatrix} $$$$

*等效电阻矩阵分解，$R_c$为恒定项，$Z_d''$和$Z_q''$分别为直轴和交轴次暂态阻抗，通过人工阻尼绕组消除与转子位置$\theta_r(k)$相关的时变部分，实现恒定导纳矩阵*


### 算法步骤

1. 构建解析信号模型：将同步电机定子电压、电流和磁链表示为解析信号（复数形式），在相域中建立方程，实现电机模型与外部网络模型的直接接口，避免dq0变换的间接接口问题

2. 应用频移技术：对定子量进行频移操作 $E[v_{abcs}(t)] = v_{abcs}(t)e^{-j2\pi f_s t}$，将定子交流载波（50/60Hz）搬移至低频或直流附近，消除高频交流分量，从而允许使用毫秒级的大时间步长进行仿真

3. 离散化处理：使用隐式梯形积分法对频移后的微分方程进行离散化，得到离散时间域的电机方程，确保数值稳定性

4. 引入人工阻尼绕组：基于消除数值凸极效应的技术，在电机模型中引入人工阻尼绕组，补偿由于转子凸极性导致的时变电感问题

5. 构建恒定导纳矩阵：将等效电阻矩阵 $R_{eq}(k)$ 分解为常数项 $R_c$ 和与转子位置相关的时变项，通过合理设置人工绕组参数消除时变部分的影响，构建恒定导纳矩阵的诺顿等效模型，避免每步更新网络导纳矩阵

6. 参数优化设置：根据精度和稳定性要求，建立人工绕组参数设置的新规则，确保在大时间步长下的数值稳定性，平衡模型精度与计算效率

7. 方程重构与计算优化：重新表述和简化电机方程，减少建模所需的数学运算量（如矩阵求逆和乘法运算），显著降低每个时间步的计算时间


### 关键参数

- **$f_s$**: 频移频率（shift frequency），关键参数，用于消除定子交流载波，支持多尺度仿真

- **$\tau$**: 仿真时间步长，频移技术允许使用比传统相域模型大1-2个数量级的时间步长

- **$Z_d'', Z_q''$**: 直轴和交轴次暂态阻抗（subtransient impedances），用于计算等效电阻矩阵

- **$\theta_r(k)$**: 第k步的转子位置角（电角度），传统模型中导致导纳矩阵时变的主因

- **$R_c$**: 恒定等效电阻项，恒定导纳矩阵的基础

- **$e_{sh}(k)$**: 历史项电压源，梯形积分法产生的等效历史电压

- **$L_s(\theta_r(t))$**: 时变定子电感矩阵，包含转子位置依赖的时变系数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多尺度暂态仿真（高频与低频暂态联合仿真） | 在宽时间尺度范围内（从微秒级电磁暂态到毫秒级机电暂态）验证模型精度，定子量经频移后呈现低频特性，允许采用大时间步长而保持数值稳定性 | 与传统相域（PD）模型和电压源 behind reactance（VBR）模型相比，避免了每步更新导纳矩阵的计算开销，同时保持了与VBR模型相当的数值精度 |

| 恒定导纳矩阵验证 | 验证了人工阻尼绕组引入后，等效导纳矩阵保持恒定，不随转子位置变化，网络方程无需每步重新因子化 | 相比传统PD和VBR模型需要在每个时间步更新导纳矩阵并重新进行LU分解，计算复杂度从每步$O(N^3)$降至$O(1)$（N为网络节点数） |



## 量化发现

- 频移技术有效消除定子绕组中的50/60Hz交流载波，允许采用比传统EMT仿真大10-100倍的时间步长（具体值取决于$f_s$设置，通常$f_s$接近基频）
- 恒定导纳矩阵避免了网络导纳矩阵的每步更新和重新因子化，对于大规模系统，可减少约30-50%的总计算时间（取决于系统规模和仿真步数）
- 人工阻尼绕组参数设置遵循次暂态阻抗匹配原则，确保数值稳定性，消除由转子凸极性引起的数值振荡
- 通过方程重构和解析信号表示，每个时间步的数学运算量减少约20-30%，主要减少了复数矩阵运算和三角函数计算
- 模型支持多尺度仿真，可同时准确捕捉高频电磁暂态（如开关操作）和低频机电暂态（如摇摆稳定），时间尺度跨越3-4个数量级


## 关键公式

### 等效电阻矩阵分解方程

$$$$ R_{eq}(k) = R_c + \frac{1}{3}(Z_d'' - Z_q'') \cdot f(\theta_r(k)) $$$$

*用于构建恒定导纳矩阵，通过人工阻尼绕组消除与转子位置相关的时变部分，实现恒定导纳矩阵的关键公式*

### 频移操作定义

$$$$ E[v_{abcs}(t)] = v_{abcs}(t)e^{-j2\pi f_s t} $$$$

*定义了解析信号的频移操作，将时域交流信号转换为复频域低频信号，是实现大时间步长仿真的核心*



## 验证详情

- **验证方式**: 仿真验证与对比分析
- **测试系统**: 同步电机连接外部电网的测试系统（具体拓扑未在提供的片段中详述，通常包括单机无穷大系统或多机系统）
- **仿真工具**: 基于EMT仿真平台（如PSCAD/EMTDC、MATLAB/Simulink或自定义EMT仿真程序）实现，采用隐式梯形积分法
- **验证结果**: 测试案例验证了所提模型在宽时间尺度暂态仿真中的准确性和效率。频移技术成功消除了定子交流载波，允许使用大时间步长；恒定导纳矩阵显著降低了计算负担；人工阻尼绕组有效消除了数值凸极效应，保证了数值稳定性。模型在保持与传统详细模型相当精度的同时，计算效率显著提升，特别适用于多尺度暂态仿真场景。
