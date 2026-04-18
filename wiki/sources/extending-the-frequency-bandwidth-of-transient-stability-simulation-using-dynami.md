---
title: "Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Systems;2022;37;1;10.1109/TPWRS.2021.3094451"
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/18/Kulasza 等 - 2022 - Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors.pdf"]
---

# Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors

**作者**: 
**年份**: 2021
**来源**: `18/Kulasza 等 - 2022 - Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors.pdf`

## 摘要

—This paper presents a novel approach to dynamic phasor-based transient stability simulation. The proposed method is based on the modiﬁed nodal analysis (MNA) approach to circuit simulation, which is used to construct continuous differential- algebraic equations (DAEs). The proposed method makes use of the stamp technique, which makes it possible to construct a general purpose MNA-based simulator. Stamp-based models for common power system components are derived in this work. A new MNA- based synchronous machine model is presented, which represents machines as nonlinear inductances instead of subtransient equiva- lents. The resultant continuous DAEs are numerically solved using the general purpose variable step and variable order library IDA. Simulation results from the IEEE 68 bus test sy

## 核心贡献


- 提出基于改进节点分析的动态相量暂态稳定仿真方法，构建连续微分代数方程。
- 引入Stamp技术构建通用仿真器，推导常见电力元件的标准化伴随模型。
- 提出新型同步机模型，将其表征为非线性电感以替代传统次暂态等效电路。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[改进节点分析法-mna|改进节点分析法(MNA)]]
- [[stamp技术|Stamp技术]]
- [[变步长变阶数值积分-ida|变步长变阶数值积分(IDA)]]
- [[连续微分代数方程-dae-构建|连续微分代数方程(DAE)构建]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[vsc-hvdc|VSC-HVDC]]
- [[交流电网|交流电网]]
- [[非线性电感模型|非线性电感模型]]


## 相关主题


- [[暂态稳定仿真|暂态稳定仿真]]
- [[频带扩展|频带扩展]]
- [[次同步振荡分析|次同步振荡分析]]
- [[大规模电网仿真|大规模电网仿真]]
- [[电力电子设备接入|电力电子设备接入]]


## 主要发现


- 在IEEE多节点测试系统中验证，动态相量仿真结果与电磁暂态仿真高度吻合。
- 计算效率显著提升，CPU耗时最高可达传统电磁暂态仿真的两百倍。
- 有效突破准稳态假设限制，可准确模拟含电力电子设备的大规模交流网络。



## 方法细节

### 方法概述

本文提出一种基于动态相量（Dynamic Phasors, DP）与改进节点分析法（MNA）的暂态稳定仿真新方法，旨在突破传统准稳态假设的频带限制。该方法首先利用Blondel变换构建平衡三相系统的动态相量框架，将瞬时电路方程转化为以相量幅值和相位为状态变量的连续微分代数方程（DAE）组。通过引入电路仿真中的Stamp技术，为线路、变压器及同步电机等常见元件推导标准化伴随模型，其中同步电机被创新性地表征为非线性电感而非传统的次暂态等效电路，从而保留高频电磁暂态特性。系统级DAE方程采用稀疏矩阵结构组装，最终调用SUNDIALS库中的IDA求解器，结合变步长变阶的BDF隐式积分算法进行数值求解。该方法在保留载波解调优势的同时，实现了对次同步振荡等高频动态的精确捕捉，并具备优异的计算效率与可扩展性。

### 数学公式


**公式1**: $$$F(t, y, \dot{y}) = 0$$$

*电力系统动态的通用微分代数方程形式，包含状态变量及其导数。*


**公式2**: $$$x(t) = X(t) \cos (\omega_0 t + \delta(t))$$$

*瞬时实正弦信号的时域表达式，用于定义动态相量提取的原始信号。*


**公式3**: $$$X(t) = P (x(t)) = X(t)e^{j\delta(t)}$$$

*动态相量算子P的定义，提取信号的包络幅值与相对相位。*


**公式4**: $$$\frac{d}{dt} P (x(t)) = \dot{X}(t) + jX(t)$$$

*动态相量微分性质（标幺制下），是构建元件动态相量本构方程的核心数学基础。*


**公式5**: $$$F \left(t, y_n, \frac{1}{\beta_0 h} \sum_{j=0}^k \alpha_j y_{n-j} \right) = 0$$$

*k阶BDF隐式积分离散化公式，用于DAE系统的数值时间推进。*


**公式6**: $$$J = \frac{\partial F}{\partial y_n} + \gamma_k \frac{\partial F}{\partial \dot{y}_n}$$$

*牛顿迭代求解所需的雅可比矩阵形式，其中$\gamma_k = \frac{\alpha_0}{\beta_0 h}$，用于处理非线性代数方程组。*


### 算法步骤

1. 动态相量建模：基于Blondel变换，将各元件的瞬时电压/电流信号通过算子P转换为动态相量形式，利用微分性质$\frac{d}{dt}P(x)=\dot{X}+jX$推导元件的动态相量本构关系。

2. Stamp矩阵构建：针对同步机（非线性电感模型）、输电线路、变压器及电力电子接口等元件，分别推导其在MNA框架下的伴随矩阵（Stamp），明确节点电压、支路电流与内部状态变量的约束关系。

3. 系统级DAE组装：利用MNA的节点KCL方程与元件Stamp，将全网络方程拼接为稀疏结构的连续DAE系统$F(t, y, \dot{y}) = 0$，其中线性网络系数存入矩阵A和T，非线性/时变项归入向量f。

4. 初始值计算：在仿真起始时刻，通过潮流计算或稳态相量分析确定各节点电压、发电机转子角度、励磁及调速器状态的初始值，完成DAE系统初始化。

5. 变步长隐式积分：调用IDA求解器，采用变阶变步长BDF算法。在每个时间步，利用牛顿迭代法求解非线性代数方程组，根据局部截断误差自动调整步长h与积分阶数k，雅可比矩阵按$J = \partial F/\partial y_n + \gamma_k \partial F/\partial \dot{y}_n$更新。

6. 结果输出与重构：记录各时刻动态相量状态变量，必要时通过$x(t) = \text{Re}[X(t)e^{j\omega_0 t}]$还原瞬时波形，进行暂态稳定与次同步振荡分析。


### 关键参数

- **solver**: IDA (SUNDIALS数值计算库)

- **integration_method**: 变步长变阶BDF (Backward Differentiation Formula)

- **machine_representation**: 非线性电感模型 (替代传统次暂态等效电路)

- **phasor_framework**: 平衡三相动态相量 (基于Blondel变换)

- **matrix_structure**: 稀疏矩阵 (A, T, f 分别对应状态、导数与非线性项系数)

- **error_control**: 局部截断误差自适应步长与阶数控制



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 68节点测试系统 | 验证大规模交流网络在故障扰动下的暂态响应，动态相量仿真波形与EMT基准高度重合，准确捕捉机电振荡与网络高频交互。 | 计算速度较传统EMT仿真提升最高达200倍，内存占用显著降低。 |

| 实际400节点电力系统 | 测试方法在真实规模电网中的可扩展性与稀疏矩阵求解效率，成功完成长时程暂态稳定计算，未出现数值发散。 | 保持与EMT一致的精度，CPU时间大幅缩减，验证了MNA架构在超大规模网络中的线性扩展能力。 |

| IEEE 39节点系统（含嵌入式HVDC） | 评估含电力电子设备的混合交直流系统动态特性，准确复现HVDC控制引发的次同步频段振荡及换相过程。 | 突破准稳态假设限制，频带有效扩展至10Hz以上，与EMT结果误差极小，证明方法适用于电力电子化电网。 |



## 量化发现

- 仿真计算速度最高可达传统电磁暂态（EMT）仿真的200倍。
- 频带覆盖范围突破传统准稳态假设（0Hz），可精确模拟频率大于10Hz的次同步振荡及大于20Hz的次同步谐振。
- 动态相量MNA模型与EMT仿真结果在IEEE 68节点、400节点及含HVDC的39节点系统中波形高度吻合，工程误差控制在可接受范围内。
- 采用变步长BDF算法，在穿越高频暂态时自动缩小步长以保证精度，在机电暂态阶段自动放大步长，实现计算效率与数值稳定性的最优平衡。


## 关键公式

### 动态相量微分性质

$$$\frac{d}{dt} P (x(t)) = \dot{X}(t) + jX(t)$$$

*用于将瞬时电路微分方程转换为以动态相量为变量的连续状态方程，是构建MNA伴随模型的核心。*

### 连续微分代数方程(DAE)通用形式

$$$F(t, y, \dot{y}) = 0$$$

*电力系统全网络动态的数学描述框架，MNA与Stamp技术最终组装的目标方程。*

### BDF隐式积分离散公式

$$$F \left(t, y_n, \frac{1}{\beta_0 h} \sum_{j=0}^k \alpha_j y_{n-j} \right) = 0$$$

*IDA求解器在每个时间步用于推进DAE系统状态，支持变步长变阶自适应控制。*

### 牛顿迭代雅可比矩阵

$$$J = \frac{\partial F}{\partial y_n} + \gamma_k \frac{\partial F}{\partial \dot{y}_n}$$$

*在求解非线性DAE代数方程组时，用于构建线性化系统以加速牛顿法收敛。*



## 验证详情

- **验证方式**: 对比仿真分析（与高精度电磁暂态EMT仿真结果进行波形与动态特性对比）
- **测试系统**: IEEE 68节点测试系统、实际400节点电力系统、含HVDC输电系统的IEEE 39节点测试系统
- **仿真工具**: 自研MNA-DP通用仿真器（底层调用SUNDIALS/IDA求解器），对比基准为商业电磁暂态（EMT）仿真软件
- **验证结果**: 在多个标准及实际测试系统中，所提动态相量MNA方法的仿真波形与EMT结果高度一致，成功捕捉次同步振荡等高频动态，同时计算速度最高提升200倍，验证了方法在大规模交直流混合电网中的准确性、高效性与可扩展性。
