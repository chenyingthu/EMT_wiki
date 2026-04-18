---
title: "A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations"
type: source
authors: ['Ajinkya Sinkar']
year: 2021
journal: "Electric Power Systems Research, 198 (2021) 107360. doi:10.1016/j.epsr.2021.107360"
tags: ['state-space']
created: "2026-04-13"
sources: ["EMT_Doc/01/Sinkar 等 - 2021 - A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descripto.pdf"]
---

# A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations

**作者**: Ajinkya Sinkar
**年份**: 2021
**来源**: `01/Sinkar 等 - 2021 - A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descripto.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations Ajinkya Sinkar , Huanfeng Zhao , Bolin Qu , Aniruddha M. Gole Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2 Canada

## 核心贡献


- 提出基于修正节点分析自动构建描述符状态空间方程的方法，避免复杂图论操作。
- 设计描述符状态空间方程与伴随电路仿真器的接口算法，实现无延迟的并行计算。
- 验证描述符状态空间方程的稀疏矩阵特性，支持直接进行系统特征值分析。


## 使用的方法


- [[伴随电路法|伴随电路法]]
- [[描述符状态空间方程|描述符状态空间方程]]
- [[修正节点分析|修正节点分析]]
- [[梯形积分法|梯形积分法]]
- [[并行接口技术|并行接口技术]]


## 涉及的模型


- [[集中参数rlc元件|集中参数RLC元件]]
- [[独立电压-电流源|独立电压/电流源]]
- [[ieee-39节点系统|IEEE 39节点系统]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络方程建模|网络方程建模]]
- [[混合仿真接口|混合仿真接口]]
- [[并行计算|并行计算]]
- [[系统特征值分析|系统特征值分析]]


## 主要发现


- 描述符状态空间方程与伴随电路法精度一致，稀疏矩阵特性更利于大规模系统求解。
- 接口算法在IEEE 39节点含HVDC系统中验证成功，实现无时间步延迟的并行加速。
- 描述符状态空间方程可直接导出连续域矩阵，便于直接计算系统特征值无需后处理。



## 方法细节

### 方法概述

本文提出一种基于描述符状态空间方程（DSE）的电磁暂态仿真方法。该方法直接利用修正节点分析（MNA）从电路网表自动生成连续域DSE模型，避免了传统图论法中繁琐的矩阵消元与状态变量线性无关性约束。随后采用梯形积分法对DSE进行离散化，实现隐式时间步进求解。论文系统对比了DSE法与广泛使用的伴随电路（CC）法在精度、计算效率及特征值提取方面的差异。此外，提出了一种无时间步延迟的DSE-CC混合接口算法，将DSE子网等效为诺顿导纳矩阵与历史电流源，无缝嵌入商业CC仿真器中，支持任意电力网络的模块化建模与并行加速计算。

### 数学公式


**公式1**: $$$E\dot{x} = -Ax + Bu$$$

*连续域描述符状态空间方程，其中E通常为奇异矩阵，x包含节点电压、电感电流及电压源电流，允许状态变量线性相关，直接由MNA构建。*


**公式2**: $$$(E + \frac{A\Delta t}{2})x(t) = (E - \frac{A\Delta t}{2})x(t-\Delta t) + \frac{B\Delta t}{2}(u(t) + u(t-\Delta t))$$$

*采用梯形积分法离散化后的DSE更新方程，用于在每个仿真步长内求解当前时刻的状态向量x(t)。*


**公式3**: $$$i_p(t) = G_n v_p(t) + I_{HIST}(t-\Delta t)$$$

*DSE子网与CC仿真器交互的离散域诺顿等效接口方程，将内部动态转化为端口导纳与历史电流源。*


**公式4**: $$$G_n = B^T (E + \frac{A\Delta t}{2})^{-1} \frac{B\Delta t}{2}$$$

*接口等效导纳矩阵计算公式，由离散化DSE矩阵推导得出，用于叠加至CC仿真器的全局导纳矩阵中。*


### 算法步骤

1. 基于电路网表自动构建DSE矩阵：提取节点数、元件参数及拓扑连接关系，生成电容矩阵C、电感矩阵L、电导矩阵G及关联矩阵$A_L, A_{vs}, A_{js}$，按MNA规则组装成奇异矩阵E、系统矩阵A和输入矩阵B。

2. 初始化与时间步进：设定固定仿真步长$\Delta t$，初始化状态向量$x(t)$与输入向量$u(t)$，进入主循环$t = t + \Delta t$。

3. 更新输入与历史项：计算当前时刻独立源值$u(t)$，结合上一时刻状态$x(t-\Delta t)$与输入$u(t-\Delta t)$构建离散方程右端项。

4. 开关状态动态处理：若网络含开关元件，检测其状态跳变，若发生变化则实时更新矩阵A或接口导纳$G_n$。

5. 求解状态变量：调用稀疏线性方程组求解器计算当前时刻状态$x(t)$，完成单步推进。

6. 混合接口数据交换：将DSE子网等效导纳$G_n$叠加至CC仿真器全局导纳矩阵G，将历史电流$I_{HIST}$叠加至全局电流向量J；由CC求解器统一计算端口电压$v_p(t)$后，回代至离散DSE方程更新内部状态$x(t)$，实现零延迟双向耦合。


### 关键参数

- **仿真步长_Δt**: 文中测试采用20 μs、50 μs、200 μs

- **矩阵维度_CC**: $(n_n + n_{vs}) \times (n_n + n_{vs})$

- **矩阵维度_DSE**: $(n_n + n_l + n_{vs}) \times (n_n + n_l + n_{vs})$

- **E矩阵特性**: 通常奇异，秩亏缺数等于纯电容-电压源回路或纯电感-电流源割集数

- **接口等效参数**: Gn（诺顿导纳矩阵），IHIST（历史电流源向量）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 简单RLC网络对比 | DSE独立求解与CC独立求解的时域波形完全重合，相电流IS1与IS2的最大绝对误差严格为0。 | 数学等价，误差为0 |

| 大规模系统运行时间对比 | 在IEEE 39、118节点及IL 200、SC 500节点系统中进行10秒仿真，CC法因求解矩阵维度更小，平均计算速度优于DSE法。 | CC法平均比DSE法快约1.3倍 |

| IEEE 39节点含LCC-HVDC混合接口验证 | 将系统划分为DSE分区与CC分区，在t=0.1s施加单相接地故障。接口仿真与全CC仿真波形高度一致，相电流ITF(A)最大绝对误差为0.003 kA，直流电流Idc误差极小。 | 相对误差仅0.15%，无时间步延迟 |



## 量化发现

- DSE与CC法在时域仿真中数学等价，简单测试用例下相电流最大绝对误差严格为0。
- CC法求解矩阵规模为$(n_n + n_{vs})$，DSE法为$(n_n + n_l + n_{vs})$，导致CC法在大规模系统中平均计算速度快约1.3倍。
- DSE-CC混合接口算法在IEEE 39节点HVDC系统中验证，端口相电流最大绝对误差为0.003 kA，相对误差仅0.15%。
- DSE矩阵束$(-A, E)$可直接提取系统特征值，无需额外后处理；奇异E矩阵导致的秩亏缺会在特征值中表现为$-\infty$，自动兼容C-V回路等代数约束。
- 接口算法实现零时间步延迟（no time-step delay），支持将自定义DSE模型无缝嵌入PSCAD/EMTDC等商业软件，具备并行加速潜力。


## 关键公式

### 连续域描述符状态空间方程

$$$E\dot{x} = -Ax + Bu$$$

*用于直接从电路网表构建系统动态模型，避免传统图论法的复杂消元，允许状态变量线性相关。*

### 梯形积分离散化更新方程

$$$(E + \frac{A\Delta t}{2})x(t) = (E - \frac{A\Delta t}{2})x(t-\Delta t) + \frac{B\Delta t}{2}(u(t) + u(t-\Delta t))$$$

*用于EMT时间步进求解，将连续DSE转化为可迭代计算的线性代数方程组。*

### DSE-CC混合接口诺顿等效方程

$$$i_p(t) = G_n v_p(t) + I_{HIST}(t-\Delta t)$$$

*用于将DSE子网封装为端口等效模型，实现与商业CC仿真器的无延迟数据交互与并行计算。*



## 验证详情

- **验证方式**: 纯数字仿真对比分析（DSE独立求解 vs CC独立求解 vs DSE-CC混合接口求解）
- **测试系统**: 简单RLC测试电路、IEEE 39/118节点系统、Illinois 200节点系统、South Carolina 500节点系统、含LCC-HVDC的IEEE 39节点系统
- **仿真工具**: 自定义DSE求解代码（MATLAB/Python环境）、PSCAD/EMTDC（商业CC仿真器）
- **验证结果**: 验证了DSE与CC法在时域波形上的数学等价性（误差趋近于0）；证实了DSE法在特征值直接提取上的显著优势；混合接口算法在复杂交直流系统中实现高精度（相对误差0.15%）与无延迟数据交换，具备工程实用性与跨平台并行加速潜力。
