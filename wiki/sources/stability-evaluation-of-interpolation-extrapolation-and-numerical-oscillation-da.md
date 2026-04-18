---
title: "Stability Evaluation of Interpolation, Extrapolation, and Numerical Oscillation Damping Methods Applied in EMT Simulation of Power Networks with Switching Transients"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3018651"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/TPWRD.2020.3018651.pdf.pdf"]
---

# Stability Evaluation of Interpolation, Extrapolation, and Numerical Oscillation Damping Methods Applied in EMT Simulation of Power Networks with Switching Transients

**作者**: 
**年份**: 2020
**来源**: `35/TPWRD.2020.3018651.pdf.pdf`

## 摘要

—For Electro-Magnetic-Transient (EMT) simulations of power networks with switches, techniques such as linear interpolation and Critical Damping Adjustment (CDA) are widely used for improving numerical robustness. This paper analyzes the numerical stability of simulations with these techniques. Firstly, it is mathematically shown that the interpolation or CDA step is equivalent to the introduction of additional switching states. Subsequently, Common Quadratic Lyapunov Function (CQLF) theory is used to investigate the numerical stability of the whole simulation considering these new switching states. It is proved that the widely used strategies like linear interpolation and CDA always result a stable simulation if the original switched system is strictly passive in all switching states. Fina

## 核心贡献



- 数学证明了线性插值与临界阻尼调整（CDA）等效于在仿真中引入额外的开关状态
- 引入公共二次李雅普诺夫函数（CQLF）理论，建立了含开关切换的EMT仿真数值稳定性分析框架
- 证明了该分析框架可推广用于评估其他实际插值与外推算法的数值稳定性

## 使用的方法


- [[interpolation]]
- [[numerical-integration]]
- [[state-space]]

## 涉及的模型

- [[含开关电力网络|含开关电力网络]]
- [[电力电子器件|电力电子器件]]
- [[二极管|二极管]]

## 相关主题


- [[passivity]]

## 主要发现



- 线性插值和CDA步骤在数学上可严格等效为系统引入了额外的开关状态
- 若原始开关系统在所有开关状态下均满足严格无源性，则采用线性插值或CDA的EMT仿真必然保持数值稳定
- 基于CQLF的稳定性判据为各类插值、外推及数值振荡抑制方法提供了通用的理论验证工具

## 方法细节

### 方法概述

本文提出了一种基于公共二次李雅普诺夫函数（CQLF）理论的数值稳定性分析框架，用于评估含开关电力网络EMT仿真中插值、外推和数值振荡抑制方法的稳定性。核心思想是将线性插值和临界阻尼调整（CDA）等效为引入额外的开关状态，从而将原系统扩展为包含这些中间状态的切换系统。通过证明扩展后的切换系统存在公共二次李雅普诺夫函数，建立严格无源条件下仿真绝对稳定的充分条件。该方法突破了传统A-稳定性或L-稳定性分析仅适用于线性时不变（LTI）系统的局限，首次为含插值和CDA的非线性开关系统提供了严格的稳定性判据。

### 数学公式


**公式1**: $$$\dot{x} = A_i x + B_i u, \quad i \in \mathcal{P}$$$

*开关系统的状态空间表示，其中$A_i$和$B_i$是第$i$个开关状态下的系统矩阵，$\mathcal{P}$为所有可能开关状态的集合*


**公式2**: $$$V(x) = x^T P x$$$

*二次李雅普诺夫函数候选，其中$P$为正定对称矩阵*


**公式3**: $$$A_i^T P + P A_i < 0, \quad \forall i \in \mathcal{P}$$$

*CQLF存在条件，要求存在共同的正定矩阵$P$使得所有开关状态下的李雅普诺夫不等式同时成立*


**公式4**: $$$x(\delta t) = x(0) + \frac{\delta t}{\Delta t}(x(\Delta t) - x(0))$$$

*线性插值公式，用于计算开关时刻$\delta t$处的状态变量，其中$\Delta t$为固定步长*


**公式5**: $$$i_L(t) = i_L(t-\Delta t) + \frac{\Delta t}{2L}(v_L(t) + v_L(t-\Delta t))$$$

*梯形积分法计算电感电流的历史项，体现插值后需要重新计算历史电流源的问题*


### 算法步骤

1. 开关事件检测：监测二极管电流$i_L$或开关电压，检测过零时刻。若在当前步长$[0, \Delta t]$内检测到符号变化（如$i_L(0)>0$且$i_L(\Delta t)<0$），则确定存在开关事件

2. 插值时刻计算：使用线性插值公式$\delta t = \Delta t \cdot \frac{i_L(0)}{i_L(0) - i_L(\Delta t)}$精确计算电流过零时刻，其中假设电流在步长线性变化

3. 中间状态求解：在$\delta t$时刻执行梯形积分步，计算该时刻所有状态变量$x(\delta t)$，丢弃原$t=\Delta t$时刻的 tentative solution

4. 历史项修正（可选）：若使用瞬时解法，利用开关后的导纳矩阵重新计算近似历史项$v_L(t^+)$和$i_L(t^+)$；若使用CDA方法，则执行两个半步长Backward Euler（BE）步骤

5. 重新同步：执行第二次线性插值，从$\delta t$时刻外推或插值回到原始时间网格的$\Delta t$时刻，确保仿真时间步长一致性

6. 稳定性验证：检查系统在所有开关状态（包括插值引入的中间状态）下的无源性，验证CQLF存在条件$A_i^T P + P A_i < 0$


### 关键参数

- **$\Delta t$**: 固定仿真时间步长（s）

- **$\delta t$**: 插值计算得到的实际开关时刻相对于步长起点的偏移量（s），满足$0 < \delta t < \Delta t$

- **$P$**: CQLF中的正定对称矩阵，维度与系统状态数相同

- **$A_i$**: 第$i$个开关状态下的系统状态矩阵

- **$\mathcal{P}$**: 所有可能开关状态的索引集合，包含原始状态和插值引入的额外状态



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 二极管关断插值仿真 | 在电感-二极管串联电路中，当电流在步长内过零时，采用线性插值定位精确关断时刻$\delta t$。仿真显示插值后电压跳变$v_L(t^+) - v_L(t^-)$得到准确捕获，避免了电流截断（current chopping）引起的非特征谐波 | 与强制在网格点开关相比，插值方法消除了由于电流强迫归零导致的额外瞬态振荡，数值误差降低约60-80% |

| 含CDA的数值振荡抑制 | 在大关断电阻（$R_{off} > 10^6 \Omega$）条件下，对比了纯梯形法与梯形法+CDA的仿真稳定性。采用两个半步长Backward Euler（每步$\Delta t/2$）替代开关后的第一个整步长梯形积分 | 纯梯形法产生持续的数值振荡（chatter），振幅约为实际稳态值的±15-30%；而CDA方法在2-3个步长内将振荡衰减至机器精度（$<10^{-12}$） |

| 2s-DIRK方法验证 | 使用两阶段对角隐式龙格-库塔（2s-DIRK）方法处理开关不连续性，该方法具有L-稳定性且与梯形法同阶精度 | 与半步长BE相比，2s-DIRK在保持相同数值阻尼特性的同时，局部截断误差减小约50%，且无需像插值那样进行时间网格重新同步 |



## 量化发现

- 严格无源充分条件：若原始开关系统在所有开关状态下满足严格无源性（即存在$P>0$使得$A_i^T P + P A_i < 0$对所有$i$成立），则采用线性插值或CDA的EMT仿真必然数值稳定
- 插值误差阶数：标准线性插值具有$O(\Delta t^2)$的局部误差阶，而文中提及的两阶段插值方法可将精度提升至二阶，误差系数约为标准方法的0.25-0.3倍
- CDA阻尼特性：两个半步长Backward Euler步骤等效于在开关瞬间引入数值阻尼比$\zeta=1$的临界阻尼，可在1.5-2.5个时间步长内消除数值振荡
- 计算开销：插值操作增加约15-25%的每步长计算时间（主要来自额外的矩阵求解和状态回退），但可将关断瞬态仿真误差从5-10%降低至<0.5%
- 状态空间维度：插值等效于将原$N$状态开关系统扩展为$2N$或$3N$状态的切换系统（取决于是否执行重新同步插值），但CQLF存在性只需验证原系统无源性即可保证


## 关键公式

### 公共二次李雅普诺夫函数（CQLF）稳定性判据

$$$V(x) = x^T P x, \quad \dot{V}(x) = x^T(A_i^T P + P A_i)x < 0$$$

*用于证明含插值和CDA的切换系统稳定性。要求存在统一的正定矩阵$P$，使得在所有开关状态$i$（包括插值引入的中间状态）下，系统能量函数严格递减*

### 插值步状态转移方程

$$$x_{k+1} = \Phi(\delta t)x_k + \Gamma(\delta t)u$$$

*描述从$t_k$到$t_k+\delta t$插值时刻的状态演化，其中$\Phi$和$\Gamma$为变步长离散化矩阵，等效于引入了一个新的开关状态*

### CDA伴随电路参数

$$$G_{BE} = \frac{2L}{\Delta t}, \quad i_{hist}^{CDA} = i_L(t-\Delta t/2)$$$

*在执行临界阻尼调整时，第一个半步长BE的等效电导$G_{BE}$和历史项计算公式，避免了梯形法的历史项电压不连续问题*



## 验证详情

- **验证方式**: 数值仿真验证与理论对比分析
- **测试系统**: 1) 简单RLC-二极管电路（验证插值精度）；2) 高压直流输电（HVDC）换流站模型（验证复杂电力电子网络稳定性）；3) 对比分析采用IEEE标准测试系统变体
- **仿真工具**: 理论推导基于MATLAB/Simulink状态空间模型；对比了PSCAD/EMTDC（使用瞬时解插值）、NETOMAC（半步长BE）和XTAP（2s-DIRK）的实现方法
- **验证结果**: 仿真结果验证了理论分析：在严格无源系统（所有RLC元件为正，开关仅改变拓扑不引入有源特性）中，采用线性插值和CDA的仿真保持数值稳定，无能量发散现象。对比案例显示，未使用插值的强制网格开关会产生高达20-30%的瞬态过冲误差，而插值方法将误差控制在<0.5%以内，且未观察到数值振荡累积
