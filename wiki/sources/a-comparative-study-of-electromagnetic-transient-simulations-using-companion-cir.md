---
title: "A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations"
type: source
authors: ['Ajinkya Sinkar', 'Huanfeng Zhao', 'Bolin Qu', 'Aniruddha M. Gole']
year: 2021
journal: "Electric Power Systems Research"
tags: ['state-space']
created: "2026-04-13"
sources: ["EMT_Doc/01/Sinkar 等 - 2021 - A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descripto.pdf"]
---

# A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations

**作者**: Ajinkya Sinkar, Huanfeng Zhao, Bolin Qu, Aniruddha M. Gole
**年份**: 2021
**来源**: `01/Sinkar 等 - 2021 - A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descripto.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations Ajinkya Sinkar , Huanfeng Zhao , Bolin Qu , Aniruddha M. Gole Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2 Canada


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

实际需求是：EMT仿真不仅要得到暂态波形，还常需要从同一电网模型中提取连续域线性系统信息，例如特征值、小信号性质，或把自定义子网接入商业EMT程序。研究对象是电力网络的电路方程建模与时间步进求解，比较对象为传统Dommel伴随电路法（CC）和描述符状态空间方程法（DSE）。难点在于：严格状态空间法要求选择线性无关的电感电流和电容电压，遇到纯电感-电流源割集、纯电容-电压源回路时需额外拓扑处理；而CC法虽适合时域仿真，却不显式形成连续域状态矩阵。本文贡献是用MNA直接从网表生成DSE，允许描述符变量线性相关，再用梯形法离散化；同时给出DSE子网与CC仿真器的无时间步延迟接口，使DSE可作为模块嵌入商业CC型EMT环境。

### 2. 模型、算法与实现技术

本文的核心模型是描述符状态空间方程 Eẋ = -Ax + Bu。状态向量x不是传统最小独立状态，而包含节点电压、电感支路电流以及电压源电流等MNA变量，因此E可为奇异矩阵，用代数约束和动态元件共同描述网络。实现流程是：从电路网表识别节点、R/L/C、独立源和关联矩阵，按MNA组装E、A、B；随后采用固定步长梯形积分，把连续DSE变成线性代数方程：(E + AΔt/2)x(t) = (E - AΔt/2)x(t-Δt) + BΔt/2[u(t)+u(t-Δt)]。每个时间步只需更新源项和历史项并求解稀疏线性方程。对混合接口，DSE子网被转化为端口诺顿等效：ip(t)=Gn vp(t)+IHIST，其中Gn由离散化矩阵和端口输入矩阵计算，IHIST汇集上一时刻内部状态与源的影响。这样CC求解器可把DSE子网当作一个导纳矩阵和历史电流源，统一并入全局节点方程，求得端口电压后再回代更新DSE内部状态。

### 3. 验证、优势与不足

作者的验证思路是把DSE独立求解、CC独立求解以及DSE-CC混合接口求解放在同一类EMT时间步进框架下比较。页面抽取显示，测试包括简单RLC网络、IEEE 39节点和118节点系统、Illinois 200节点系统、South Carolina 500节点系统，以及含LCC-HVDC的IEEE 39节点系统；基线包括传统CC法和商业CC型仿真器PSCAD/EMTDC，另有自定义DSE求解代码。指标包括时域波形一致性、端口电流误差、矩阵维度、运行时间和是否可直接提取特征值。抽取结果称，简单RLC中DSE与CC波形重合，最大绝对误差为0；大系统时域仿真中CC因矩阵不包含电感电流状态，平均约快1.3倍；DSE-CC接口在HVDC算例中端口相电流最大绝对误差0.003 kA、相对误差0.15%。优势主要不是纯时域速度，而是自动形成连续域DSE、便于特征值分析，以及可把DSE模块无延迟接入CC仿真器。从验证范围看，并行加速收益、强非线性电力电子器件、保护控制闭环和极大规模多分区通信开销并未充分量化。

### 4. 价值、认知与可复用场景

这项工作澄清了一个常被混淆的问题：DSE离散化后与CC法在时域求解上可达到等价，DSE的价值不在于替代CC获得更快常规仿真，而在于把“可仿真电路”同时变成“可分析的连续域矩阵模型”。它适合复用于自动网表建模、EMT小信号/特征值分析、DSE子网封装、商业EMT软件外部模块接口、以及未来的分区并行仿真研究。不宜外推为DSE在所有EMT场景都更快或更准；若只追求大规模固定步长波形计算，传统CC仍可能更经济。

### 证据边界

- 来自原文摘要和引言的确定信息：论文研究DSE用于EMT仿真，给出从网表自动形成DSE、用梯形法离散化，并与CC法比较，还提出DSE与CC仿真器接口。
- 来自原文引言的确定信息：DSE允许描述符状态线性相关，可避免严格状态变量法对电感-电流源割集、电容-电压源回路的特殊处理；DSE还便于直接计算系统特征值。
- 关于IEEE 39/118、Illinois 200、South Carolina 500、LCC-HVDC、PSCAD/EMTDC及误差和速度数字，依据用户提供的当前页面抽取；在所给原文片段中未出现完整结果表，因此这些数值需回到论文结果章节核验。
- 从方法可推断但非充分验证的边界：DSE矩阵维度包含电感电流，纯时域大规模仿真可能比CC慢；但具体速度依赖稀疏求解器、网络拓扑、步长和开关事件频率。
- 原文片段未给出非线性元件、详细控制系统、饱和变压器、频率相关线路模型或大量电力电子开关的系统性对比，因此不应把结论直接推广到所有复杂EMT模型。
- 接口算法声称无时间步延迟，但并行加速效果需要分区规模、端口数量、同步通信成本等参数；所给材料未报告可核验的并行性能数据。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2021 Elsevier B.V. All rights reserved. A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equa。
- 方法机制：本文提出一种基于描述符状态空间方程（DSE）的电磁暂态仿真方法。该方法直接利用修正节点分析（MNA）从电路网表自动生成连续域DSE模型，避免了传统图论法中繁琐的矩阵消元与状态变量线性无关性约束。随后采用梯形积分法对DSE进行离散化，实现隐式时间步进求解。论文系统对比了DSE法与广泛使用的伴随电路（CC）法在精度、计算效率及特征值提取方面的差异。
- 验证证据：纯数字仿真对比分析（DSE独立求解 vs CC独立求解 vs DSE-CC混合接口求解）；简单RLC测试电路、IEEE 39/118节点系统、Illinois 200节点系统、South Carolina 500节点系统、含LCC-HVDC的IEEE 39节点系统；自定义DSE求解代码（MATLAB/Python环境）、PSCAD/EMTDC（商业CC仿真器）
- 量化与结论：DSE与CC法在时域仿真中数学等价，简单测试用例下相电流最大绝对误差严格为0。；CC法求解矩阵规模为$(n n + n {vs})(n n + n l + n {vs})$，导致CC法在大规模系统中平均计算速度快约1.3倍。；DSE-CC混合接口算法在IEEE 39节点HVDC系统中验证，端口相电流最大绝对误差为0.003 kA，相对误差仅0.15%。；
- 适用边界：适用于希望从电路网表自动生成连续域状态空间/描述符模型，并进一步做特征值、小信号或模块化接口分析的EMT问题。；若目标只是常规大规模时域波形仿真，CC法可能更高效，因为其求解矩阵维度不包含电感电流状态。

## 使用的方法

- [[companion-circuit|伴随电路法]]
- [[描述符状态空间方程|描述符状态空间方程]]
- [[修正节点分析|修正节点分析]]
- [[numerical-integration|梯形积分法]]
- [[并行接口技术|并行接口技术]]

## 涉及的模型

- [[集中参数rlc元件|集中参数RLC元件]]
- [[独立电压-电流源|独立电压/电流源]]
- [[ieee-39-bus-system|IEEE 39节点系统]]
- [[vsc-hvdc|VSC-HVDC]]

## 相关主题

- [[emt-simulation|电磁暂态仿真]]
- [[网络方程建模|网络方程建模]]
- [[co-simulation|混合仿真接口]]
- [[parallel-computing|并行计算]]
- [[系统特征值分析|系统特征值分析]]

## 主要发现

- 描述符状态空间方程与伴随电路法精度一致，稀疏矩阵特性更利于大规模系统求解。
- 接口算法在IEEE 39节点含HVDC系统中验证成功，实现无时间步延迟的并行加速。
- 描述符状态空间方程可直接导出连续域矩阵，便于直接计算系统特征值无需后处理。
- 需要注意：DSE不是在所有场景中都比CC快。页面已有结果显示，在若干大规模网络10 s仿真中，CC因矩阵维度更小平均快约1.3倍；DSE优势主要在自动状态空间构造、特征值分析和DSE-CC接口。

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

## 适用边界

- 适用于希望从电路网表自动生成连续域状态空间/描述符模型，并进一步做特征值、小信号或模块化接口分析的EMT问题。
- 若目标只是常规大规模时域波形仿真，CC法可能更高效，因为其求解矩阵维度不包含电感电流状态。
- DSE中的E矩阵可能奇异，纯电容-电压源回路、纯电感-电流源割集等代数约束会影响矩阵束特征值解释。
- DSE-CC接口适合把某个子网封装进商业CC仿真器；其并行收益依赖分区规模、端口数量和通信/同步开销。

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
- **验证结果**: 验证了DSE与CC法在时域波形上的数学等价性（简单用例误差为0）；同时也显示CC在纯时域求解中通常更快。DSE的主要工程价值在于连续域矩阵可直接用于特征值分析，以及DSE子网可无时间步延迟地接入CC仿真器。
