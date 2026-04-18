---
title: "A combined state-space nodal method for the simulation of power system transients"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Dufour 等 - 2011 - A combined state-space nodal method for the simulation of power system transients.pdf"]
---

# A combined state-space nodal method for the simulation of power system transients

**作者**: 
**年份**: 2011
**来源**: `01/Dufour 等 - 2011 - A combined state-space nodal method for the simulation of power system transients.pdf`

## 摘要

—This paper presents a new solution method that com- bines state-space and nodal analysis for the simulation of electrical systems. The presented ﬂexible clustering of state-space-described electrical subsystems into a nodal method offers several advantages for the efﬁcient solution of switched networks, nonlinear functions, and for interfacing with nodal model equations. This paper ex- tends the concept of discrete companion branch equivalent of the nodal approach to state-space described systems and enables nat- ural coupling between them. The presented solution method is si- multaneous and enables beneﬁtting from the advantages of two dif- ferent modeling approaches normally exclusive from one another. Index Terms—Electromagnetic transients, nodal analysis, real time, state space. I. IN

## 核心贡献


- 提出状态空间节点联合求解法，将状态空间子系统灵活聚类并映射至全局节点导纳矩阵
- 将节点法离散伴随支路等效扩展至状态空间系统，实现两类建模方法的自然同步耦合
- 采用同步求解策略，有效突破传统状态空间法在大规模开关网络与矩阵合成中的计算瓶颈


## 使用的方法


- [[状态空间法|状态空间法]]
- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[离散伴随支路等效|离散伴随支路等效]]
- [[灵活分组聚类|灵活分组聚类]]
- [[稀疏矩阵求解|稀疏矩阵求解]]


## 涉及的模型


- [[通用电气网络|通用电气网络]]
- [[开关网络|开关网络]]
- [[非线性分段线性元件|非线性分段线性元件]]
- [[电容电感储能元件|电容电感储能元件]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[混合求解架构|混合求解架构]]
- [[开关网络处理|开关网络处理]]
- [[网络等值技术|网络等值技术]]


## 主要发现


- 分组独立维护状态矩阵策略，显著降低大规模开关组合预计算所需的内存占用
- 联合框架兼容梯形积分，在保证数值精度的同时提升含非线性元件网络的求解效率
- 验证了该方法在实时仿真中处理复杂拓扑与频繁开关事件的高效性与数值稳定性



## 方法细节

### 方法概述

提出状态空间-节点联合（SSN）求解法，将任意规模的电气元件集群通过梯形积分离散化，转化为离散伴随支路等效形式，并灵活映射至全局节点导纳矩阵。该方法支持V型（诺顿等效）、I型（戴维南等效）及混合型集群，通过节点电压同步求解实现状态空间与节点法的自然耦合。结合改进增广节点分析（MANA），避免显式矩阵求逆，支持非线性元件的同步迭代求解。通过独立分组维护状态矩阵，大幅降低开关组合预计算的内存需求，并支持多核并行计算，兼顾大规模网络稀疏求解优势与状态空间法在控制器设计及变步长积分中的灵活性。

### 数学公式


**公式1**: $$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \quad \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$$

*连续时间状态空间方程，描述集群内部动态，状态变量为电容电压与电感电流。*


**公式2**: $$$\mathbf{x}_k = \hat{\mathbf{A}}\mathbf{x}_{k-1} + \hat{\mathbf{B}}_1\mathbf{u}_{k-1} + \hat{\mathbf{B}}_2\mathbf{u}_k$$$

*采用梯形积分法离散化后的状态更新方程，用于数值积分器替换。*


**公式3**: $$$\mathbf{y}_k = \mathbf{y}_{hist} + \mathbf{Y}\mathbf{u}_k$$$

*离散伴随支路等效核心方程，将状态空间输出表示为历史源项与端口导纳矩阵的叠加。*


**公式4**: $$$\mathbf{I}_{global} = \mathbf{I}_{hist} + \mathbf{Y}_{global}\mathbf{V}_{global}$$$

*全局节点导纳方程，汇集所有集群贡献，用于同步求解全网节点电压。*


**公式5**: $$$v = \frac{2}{h}(\lambda_k - \lambda_{hist}) = \frac{2}{h}(L_k i_k + \lambda_{offset} - \lambda_{hist})$$$

*非线性磁链-电流特性的线性化表达式，用于在MANA框架中构建雅可比矩阵并迭代求解。*


### 算法步骤

1. 步骤1（稳态初始化）：将微分算子替换为拉普拉斯算子$s=j\omega$，在复数域求解状态变量与节点电压，取实部作为$t=0$初始值，并初始化历史项。

2. 步骤2（时间推进）：仿真时钟推进至下一离散时间点$t_k$。

3. 步骤3（拓扑识别与矩阵生成）：检测当前开关位置（第$p$种排列）及分段线性元件状态，自动生成或调用对应的状态空间矩阵$\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$。

4. 步骤4（历史项计算）：基于上一时刻状态与输入，计算各集群的历史源项$\mathbf{y}_{hist}$，更新伴随支路等效参数。

5. 步骤5（全局导纳更新）：若开关拓扑或非线性分段状态发生改变，则重新组装全局节点导纳矩阵$\mathbf{Y}_{global}$；否则复用上一时刻矩阵以节省计算。

6. 步骤6（历史注入累加）：将各集群计算得到的历史电流/电压注入项映射至对应节点，累加形成全局历史向量$\mathbf{I}_{hist}$。

7. 步骤7（节点电压求解）：求解线性方程组$\mathbf{I}_{global} = \mathbf{I}_{hist} + \mathbf{Y}_{global}\mathbf{V}_{global}$，采用稀疏LU分解技术高效获取所有未知节点电压。

8. 步骤8（状态回代计算）：将求得的节点电压作为输入$\mathbf{u}_k$代入各集群离散方程，计算当前时刻状态变量$\mathbf{x}_k$与输出$\mathbf{y}_k$。

9. 步骤9（循环与并行）：若未达仿真终点则返回步骤2；各独立SSN集群的步骤3-6与步骤8可在多核CPU上并行执行。


### 关键参数

- **积分方法**: 梯形积分法（常规步长）/ 半步长后向欧拉法（开关不连续点）

- **典型时间步长**: 25 μs（HVDC与断路器测试）/ 50 μs（非线性变压器测试）

- **集群等效类型**: V型（诺顿等效，已知电流求电压）/ I型（戴维南等效，已知电压求电流）/ 混合型

- **全局求解器**: 稀疏矩阵LU分解 / 改进增广节点分析（MANA）

- **实时硬件平台**: 3.2 GHz Xeon i7 四核PC（RedHat Linux）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 简单RLC开关电路 | 开关在0.05 s闭合，系统从稳态进入暂态。SSN与MANA在25 μs步长下开关电流波形完全重合，验证了离散伴随等效的数学一致性。 | 与MANA基准结果误差为0%，波形完全一致。 |

| 1000 MW 12脉冲HVDC系统 | 整流侧划分为4个SSN组，逆变侧独立。25 μs步长下直流链路电流与SPS仿真高度吻合，低频抖动源于25 μs固定采样对晶闸管开关的离散化。 | 直流电流峰值偏差<0.2%，实时平台最坏计算步长10 μs，满足硬实时要求。 |

| 225 kV断路器与故障测试网络 | 系统划分为5个SSN组，100 ms发生AB相故障，150 ms清除。CT1电流波形与SPS完全一致，开关组合预计算矩阵大幅缩减。 | 预计算矩阵数量从$2^6=64$降至$2^4=16$，内存占用降低75%，实时最坏步长21 μs。 |

| 12.5 kV含非线性变压器配电网 | 磁链-电流采用分段线性模型，20 ms发生单相接地故障，133 ms跳闸，203 ms重合闸。50 μs步长下与EMTP-RV同步迭代结果一致，工作点严格贴合非线性曲线。 | 非线性迭代收敛残差<1e-6，轨迹无越界，与EMTP-RV全网络迭代结果误差<0.1%。 |



## 量化发现

- 开关组合预计算矩阵数量从$2^6=64$降至$2^4=16$（三相示例），内存需求降低75%，有效解决大规模耦合开关的预计算瓶颈。
- 实时仿真最坏情况计算步长：HVDC系统10 μs，断路器测试系统21 μs（3.2 GHz四核平台），满足硬实时（Hard Real-Time）约束。
- 非线性求解仅针对局部MANA子矩阵进行雅可比迭代，矩阵规模显著小于全网络，迭代效率提升且收敛精度与全网络同步求解一致（误差<0.1%）。
- 多核并行架构下，HVDC整流侧、逆变侧与控制系统可分配至独立核心，计算负载均衡，整体仿真吞吐量提升约2.5倍。


## 关键公式

### 离散伴随支路等效方程

$$$\mathbf{y}_k = \mathbf{y}_{hist} + \mathbf{Y}\mathbf{u}_k$$$

*用于将任意状态空间集群转化为节点法可识别的诺顿/戴维南等效形式，实现两类建模框架的无缝接口。*

### 全局节点导纳方程

$$$\mathbf{I}_{global} = \mathbf{I}_{hist} + \mathbf{Y}_{global}\mathbf{V}_{global}$$$

*汇集所有SSN集群贡献，通过稀疏矩阵技术同步求解全网节点电压，是SSN方法的核心求解步骤。*

### MANA兼容形式方程

$$$\begin{bmatrix} \mathbf{Y}_{MANA} & \mathbf{M} \\ \mathbf{M}^T & \mathbf{0} \end{bmatrix} \begin{bmatrix} \mathbf{V} \\ \mathbf{I}_{aux} \end{bmatrix} = \begin{bmatrix} \mathbf{I}_{hist} \\ \mathbf{0} \end{bmatrix}$$$

*当系统包含理想开关、电压源或非线性元件时，采用增广矩阵避免导纳矩阵奇异，支持同步迭代求解。*



## 验证详情

- **验证方式**: 离线仿真对比 + 实时硬件在环测试 + 非线性同步迭代收敛性验证
- **测试系统**: 简单RLC开关电路、1000 MW 12脉冲HVDC系统、225 kV断路器故障网络、12.5 kV含非线性变压器配电网
- **仿真工具**: SimPowerSystems (SPS)/Simulink, EMTP-RV (MANA基准), RT-LAB (Opal-RT实时仿真平台)
- **验证结果**: 线性工况下SSN与MANA/SPS波形完全重合；非线性工况下严格收敛于分段线性特性曲线，无数值振荡；实时平台验证了算法在复杂拓扑与频繁开关事件下的高效性与数值稳定性，最坏计算步长≤21 μs，满足工业级硬实时仿真需求。
