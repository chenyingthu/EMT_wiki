---
title: "A state-variable-preserving method for the efficient modelling of inverter-based resources in parall"
type: source
year: 2025
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/Wang 等 - 2025 - A state-variable-preserving method for the efficient modelling of inverter-based resources in parall.pdf"]
---

# A state-variable-preserving method for the efficient modelling of inverter-based resources in parall

**年份**: 2025
**来源**: `04/Wang 等 - 2025 - A state-variable-preserving method for the efficient modelling of inverter-based resources in parall.pdf`

## 摘要

The aggregation models of renewable energy power stations are difﬁcult to apply to the stability research of the fault inside the station or the oscillation analysis between the station and the grid-side system, and the high dimensional characteristics of their detailed model will pose an enormous challenge to the simulation efﬁciency. To alleviate the contradiction between accuracy and efﬁciency, this paper proposes a state-variable-preserving method to efﬁciently model inverter-based resources and a node tearing method to realize parallel simulation of the renewable energy power station consisting of inverter-based resources. The state-variable-preserving model uses discrete state space expression to eliminate the internal nodes on the basis of preserving the original variables of the ge

## 核心贡献


- 提出状态变量保持法，利用离散状态空间消除内部节点并保留原始变量，降低求解规模
- 提出节点撕裂法重构节点电压方程，降低关联变量求解复杂度，适配共母线互联拓扑
- 设计分层并行算法，利用机组与集群求解独立性，显著提升大规模场站EMT仿真效率


## 使用的方法


- [[状态变量保持法|状态变量保持法]]
- [[节点撕裂法|节点撕裂法]]
- [[离散状态空间法|离散状态空间法]]
- [[分层并行算法|分层并行算法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[逆变器型资源|逆变器型资源]]
- [[光伏发电单元|光伏发电单元]]
- [[光伏电站|光伏电站]]
- [[dc-dc变换器|DC/DC变换器]]
- [[dc-ac逆变器|DC/AC逆变器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[新能源场站建模|新能源场站建模]]
- [[网络解耦|网络解耦]]
- [[模型降阶|模型降阶]]


## 主要发现


- 数值精度与稳定性分析验证了所提模型在光伏电站内部故障与振荡分析中的可靠性
- 改变光伏电站规模测试表明，分层并行算法显著降低计算耗时，提升大规模仿真效率
- 节点撕裂法相比传统支路切割法，有效降低了共母线互联拓扑下关联变量的求解复杂度



## 方法细节

### 方法概述

本文提出一种面向逆变器型资源（IBR）并行电磁暂态（EMT）仿真的状态变量保持（SVP）建模与节点撕裂并行算法。SVP方法基于离散状态空间表达式，在完整保留机组原始状态变量（如动态元件历史电流与控制变量）的前提下，通过受控导纳与受控历史电流源等效消除全部内部电气节点，将包含多支路变换器与滤波器的复杂机组对外收缩为单三相节点，大幅降低系统导纳矩阵求解规模。针对新能源场站典型的共母线互联拓扑，提出节点撕裂法重构节点电压方程，以公共母线三相电压为唯一关联变量实现无延迟解耦，相比传统支路切割法显著降低关联变量维度。结合机组与集群求解的强独立性，设计分层并行算法，实现控制更新、系数矩阵映射与分区电压求解的完全并行化，仅保留极小规模的关联变量串行计算，从而在维持详细模型精度的同时突破大规模场站EMT仿真的效率瓶颈。

### 数学公式


**公式1**: $$i_{array} = N_p i_{ph} - N_p i_s \left( e^{\frac{q(u_{array} + i_{array} R_s)}{A k T N_s}} - 1 \right) - \frac{N_p u_{array} + i_{array} R_s}{R_{sh} N_s}$$

*光伏阵列伏安特性方程，描述阵列输出电流与电压的非线性关系，用于构建内部节点注入电流源。*


**公式2**: $$\begin{cases} I_{hPV}(t) = A_{PV} I_{hPV}(t-\Delta t) + B_{PV} U_{PV}(t-\Delta t) + E_{PV} I_{inj}(t-\Delta t) \\ I_{PV}(t) = C_{PV} I_{hPV}(t) + D_{PV} U_{PV}(t) + F_{PV} I_{inj}(t) \end{cases}$$

*离散状态空间表达式，以历史电流为状态变量、端口电压为输入、端口电流为输出，实现内部节点消除与外部等效。*


**公式3**: $$U_p(t) = \left( Y_{pp}(t) - Y_{pg}(t)Y_{gg}^{-1}(t)Y_{gp}(t) - \sum_{k=1}^n Y_{pk}(t)Y_{kk}^{-1}(t)Y_{kp}(t) \right)^{-1} \left( I_p(t) - Y_{pg}(t)Y_{gg}^{-1}(t)I_g(t) - \sum_{k=1}^n Y_{pk}(t)Y_{kk}^{-1}(t)I_k(t) \right)$$

*节点撕裂法关联电压求解方程，用于串行计算公共母线电压，是并行解耦的核心串行步骤。*


**公式4**: $$\begin{bmatrix} U_g(t) \\ U_1(t) \\ \vdots \\ U_n(t) \end{bmatrix} = \begin{bmatrix} Y_{gg}^{-1}(t)I_g(t) \\ Y_{11}^{-1}(t)I_1(t) \\ \vdots \\ Y_{nn}^{-1}(t)I_n(t) \end{bmatrix} - \begin{bmatrix} Y_{gg}^{-1}(t)Y_{gp}(t) \\ Y_{11}^{-1}(t)Y_{1p}(t) \\ \vdots \\ Y_{nn}^{-1}(t)Y_{np}(t) \end{bmatrix} U_p(t)$$

*分区节点电压并行求解方程，在获得关联电压后，各分区可完全独立并行计算节点电压。*


### 算法步骤

1. 初始化阶段：根据网络拓扑、元件参数及开关状态，预先计算并存储SVP模型的六个系数矩阵（A_PV, B_PV, C_PV, D_PV, E_PV, F_PV），建立受控导纳与历史电流源映射关系。

2. 网络方程构建：基于伴随电路模型与梯形法离散化，利用节点分析法（NAM）分别形成电网侧系统的节点导纳矩阵Y_gg与注入电流向量I_g，以及关联分区（公共母线）的Y_pp与I_p，并计算各PV集群与关联分区间的互导纳矩阵。

3. 控制与开关更新：在各并行分区内独立求解Boost与DC/AC控制器（含MPPT、电压电流双环PI控制），通过梯形法离散化控制方程，计算当前步的调制信号与开关状态。

4. 系数矩阵动态更新：根据实时开关状态，动态更新SVP模型的六个系数矩阵，其中前馈矩阵D_PV直接对应传统等效导纳，实现开关动作对网络参数的快速映射。

5. 历史电流与内源处理：计算动态元件历史电流与内部电流源，分别乘以系数矩阵C_PV和F_PV后注入对应节点，完成内部变量到外部端口的等效映射。

6. 关联变量串行求解：利用节点撕裂法公式串行求解公共母线电压U_p(t)，该步骤维度固定为3（三相），计算量极小，构成并行流程的唯一串行瓶颈。

7. 分区电压并行求解：将求得的U_p(t)代入各分区独立方程，利用矩阵求逆与向量运算并行计算电网侧与各PV集群的节点电压U_k(t)。

8. 状态迭代推进：更新历史电流向量与内部状态，进入下一仿真步长循环，重复执行步骤3至7直至仿真结束。


### 关键参数

- **仿真步长**: \Delta t

- **开关导纳**: Y_{sw} = 10^6 (导通), 0 (关断)

- **关联变量维度**: 3 (三相节点电压)

- **传统支路切割关联维度**: 3n (n为分区数)

- **PI控制器参数**: k_p, k_i (电压/电流环比例与积分系数)

- **PV阵列参数**: N_s, N_p, R_s, R_{sh}, i_s, i_{ph}



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 光伏电站内部故障与振荡分析 | 通过数值精度与稳定性分析验证SVP模型在保留原始状态变量前提下的等效准确性。模型能够准确反映场站内部动态特性与机网交互振荡，开关导纳设为10^6确保导通状态数值稳定性。 | 相比传统详细模型，在保持同等精度的前提下消除全部内部节点；相比聚合模型，具备内部故障与多机交互振荡分析能力，数值误差控制在工程允许范围内。 |

| 场站规模扩展效率测试 | 通过改变光伏电站内PV机组与集群数量进行并行仿真耗时测试。节点撕裂法将关联变量维度固定为3，传统支路切割法为3n，随规模扩大求解复杂度显著降低。 | 分层并行算法实现控制更新与分区电压求解的完全并行化，仅保留极小串行步骤。随机组数量增加，计算耗时呈近似线性优化趋势，大规模场站仿真效率显著提升。 |



## 量化发现

- 节点撕裂法将共母线互联拓扑的关联变量求解维度从传统支路切割法的3n（n为分区数）严格降低至固定值3（三相电压）。
- SVP模型将包含多支路Boost、DC/AC及LCL滤波器的复杂机组对外等效为单三相节点，消除全部内部电气节点，导纳矩阵规模大幅缩减。
- 开关导纳参数Y_sw在导通时设为10^6，关断时为0，确保离散状态空间矩阵数值条件数稳定，避免病态矩阵求解。
- 离散状态空间法通过预计算系数矩阵，将开关动作影响直接映射至矩阵参数，避免传统方法中逐支路重构导纳矩阵的O(N^3)计算开销。
- 分层并行算法仅保留关联电压U_p(t)的串行求解步骤，其余控制更新、系数映射与分区电压求解均实现100%并行化，计算负载均衡度高。


## 关键公式

### 离散状态空间表达式

$$\begin{cases} I_{hPV}(t) = A_{PV} I_{hPV}(t-\Delta t) + B_{PV} U_{PV}(t-\Delta t) + E_{PV} I_{inj}(t-\Delta t) \\ I_{PV}(t) = C_{PV} I_{hPV}(t) + D_{PV} U_{PV}(t) + F_{PV} I_{inj}(t) \end{cases}$$

*用于SVP建模核心推导，以历史电流为状态变量、端口电压为输入、端口电流为输出，消除内部节点并保留原始动态特性。*

### 节点撕裂法关联电压求解方程

$$U_p(t) = \left( Y_{pp}(t) - Y_{pg}(t)Y_{gg}^{-1}(t)Y_{gp}(t) - \sum_{k=1}^n Y_{pk}(t)Y_{kk}^{-1}(t)Y_{kp}(t) \right)^{-1} \left( I_p(t) - Y_{pg}(t)Y_{gg}^{-1}(t)I_g(t) - \sum_{k=1}^n Y_{pk}(t)Y_{kk}^{-1}(t)I_k(t) \right)$$

*用于无延迟解耦共母线互联系统，串行求解公共母线电压，维度仅为3，是并行计算的关键串行瓶颈。*

### 分区节点电压并行求解方程

$$\begin{bmatrix} U_g(t) \\ U_1(t) \\ \vdots \\ U_n(t) \end{bmatrix} = \begin{bmatrix} Y_{gg}^{-1}(t)I_g(t) \\ Y_{11}^{-1}(t)I_1(t) \\ \vdots \\ Y_{nn}^{-1}(t)I_n(t) \end{bmatrix} - \begin{bmatrix} Y_{gg}^{-1}(t)Y_{gp}(t) \\ Y_{11}^{-1}(t)Y_{1p}(t) \\ \vdots \\ Y_{nn}^{-1}(t)Y_{np}(t) \end{bmatrix} U_p(t)$$

*在获得关联电压后，各分区（电网侧与各PV集群）可完全独立并行求解节点电压，实现大规模系统的高效计算。*



## 验证详情

- **验证方式**: 数值精度分析、数值稳定性分析、规模扩展效率对比测试
- **测试系统**: 含多个PV集群与电网侧系统通过公共母线互联的光伏发电站（采用集散式拓扑，含DC/DC Boost、DC/AC逆变器及LCL滤波器）
- **仿真工具**: 基于自定义并行求解架构实现（算法设计适配通用EMT求解器与高性能计算平台，文中未指定具体商业软件）
- **验证结果**: 验证表明SVP模型在消除内部节点的同时完整保留了机组原始状态变量，数值精度与稳定性满足内部故障与机网振荡分析需求；节点撕裂法有效克服共母线拓扑下传统解耦方法关联变量维度爆炸问题；分层并行算法随场站规模扩大显著降低计算耗时，实现精度与效率的平衡。
