---
title: "Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/Xu 等 - 2025 - Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En.pdf"]
---

# Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En

**作者**: 
**年份**: 2025
**来源**: `35/Xu 等 - 2025 - Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transformer with Integrated En.pdf`

## 摘要

—Due to the advanced features of multidirectional power transfer and fast smoothing of the power ﬂuctuation in renewable energy systems, the multiple-active-bridge based power-electronic-transformer (MAB-PET) with integrated energy storage units is becoming popular. However, the accurate elec- tromagnetic transient simulation of the MAB-PETs is extremely time-consuming due to the large number of circuit nodes and small time-step. This paper proposes a simpliﬁed EMT modeling approach for the MAB-PETs by employing the generalized state- space averaging method. First, the switching function method and Dommel algorithm are used to build the equivalent model of each power module. Further, the PET equivalent model is presented in a multi-port PM polymerization mode. The system is simpliﬁed by ap

## 核心贡献



- 提出基于广义状态空间平均法的MAB-PET简化电磁暂态（EMT）建模方法
- 构建多端口功率模块聚合等效模型，通过傅里叶分解忽略高次谐波，导出四端口等效电压源电路

## 使用的方法


- [[state-space]]
- [[average-value-model]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]
- [[mmc-model]]

## 相关主题


- [[harmonic]]
- [[network-equivalent]]
- [[dynamic-phasor]]

## 主要发现



- 所提简化等效模型在PSCAD/EMTDC中与详细模型对比具有极高的仿真精度
- 该模型通过状态平均与谐波忽略策略，使仿真速度比详细模型快2至3个数量级，有效克服了MAB-PET节点多、步长小导致的计算瓶颈

## 方法细节

### 方法概述

本文提出基于广义状态空间平均法(GSSA)的MAB-PET简化电磁暂态建模方法。该方法首先采用开关函数法构建级联H桥(CHB)交直流端口的电气变量桥接，消除器件级开关过程；其次利用Dommel算法和二元电阻法建立储能子模块(ESS)的Thevenin等效模型，保留混合储能接口；随后对MAB系统应用傅里叶分解进行状态函数谐波分析，忽略高次谐波分量，仅保留直流和基波分量；最终将各功率模块(PM)聚合为四端口等效电压源电路，通过多端口级联模式构建完整的输入串联输出并联(ISOP)型MAB-PET简化等效模型。该方法避免了传统Thevenin等效中的内部节点消除和高频链路解耦，适用于含多端口功率传输和储能集成的复杂PET拓扑。

### 数学公式


**公式1**: $$$$\frac{d}{dt}\langle x \rangle_k = A\langle x \rangle_k + B\langle u \rangle_k + \sum_{l \neq k} C_{l}\langle x \rangle_l$$$$

*广义状态空间平均法(GSSA)的第k次谐波状态方程，其中$\langle x \rangle_k$为状态变量第k次谐波分量的时变复系数，$A$为系统矩阵，$B$为输入矩阵，$C_l$表示不同谐波分量间的耦合项。当忽略高次谐波时(k>1)，系统维度显著降低。*


**公式2**: $$$$u_{dc} = \sum_{j=a,b,c} s_j(t) \cdot u_{ac,j}$$$$

*开关函数法描述的CHB交直流电压关系，其中$s_j(t) \in \{-1, 0, 1\}$为第j相开关函数，$u_{ac,j}$为交流侧相电压，$u_{dc}$为直流侧电容电压。通过平均化处理消除高频开关细节。*


**公式3**: $$$$I_{bat}(t) = G_{eq}U_{C4}(t) + I_{hist}(t-\\Delta t)$$$$

*基于Dommel算法的ESS等效电路方程，$I_{bat}$为电池端口电流，$G_{eq}$为等效电导，$U_{C4}$为LVDC端口电压，$I_{hist}$为历史电流源项，由上一时步状态计算得到，实现储能系统的电磁暂态等效。*


**公式4**: $$$$\langle x(t) \rangle_0 + \sum_{k=1}^{N} \langle x(t) \rangle_k e^{jk\omega_s t} \\approx \langle x(t) \rangle_0 + \langle x(t) \rangle_1 e^{j\omega_s t}$$$$

*傅里叶分解简化表达式，将状态变量$x(t)$分解为直流分量($k=0$)和基波分量($k=1$)，忽略$k \geq 2$的高次谐波分量，实现模型简化。$\omega_s$为开关角频率。*


### 算法步骤

1. 使用开关函数法建立CHB交流/直流端口的电气变量桥接，将三相SPWM调制波与三角载波比较生成的开关动作等效为连续变量，消除器件级开关过程，避免复杂矩阵运算

2. 采用Dommel算法和二元电阻法构建ESS等效模型，将储能子模块中的电力电子变换器和电池组等效为时变电阻与历史电流源并联的Thevenin电路，保留混合储能系统接口

3. 应用广义状态空间平均法建立MAB系统级模型，对高频变压器和功率传输网络进行谐波分析，通过傅里叶级数展开状态变量，建立各次谐波分量的动态方程

4. 执行谐波截断简化，忽略二次及以上高次谐波分量，仅保留直流分量和基波分量，将复杂的高频时变系统降阶为低频时不变系统，导出四端口等效电压源电路

5. 通过多端口PM聚合模式将各功率模块等效模型级联，构建输入串联输出并联(ISOP)型MAB-PET完整简化模型，实现端口电压电流特性的精确等效


### 关键参数

- **开关频率**: 高频链路(HFL)工作频率，决定GSSA谐波分析基频$\omega_s$

- **等效时间常数**: Dommel算法中$\tau = 2L/R$或$\tau = RC$，决定历史电流源计算权重

- **谐波截断阶数**: N=1，仅保留基波和直流分量

- **CHB子模块数**: 每相级联H桥子模块数量，影响开关函数维度

- **MAB端口数**: m输入1输出(m-to-1)结构，支持多端口功率流动



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 详细模型与简化等效模型对比验证 | 在PSCAD/EMTDC平台中，针对河北崇礼配电网络实际运行的MAB-PET进行建模对比。详细模型包含完整器件级开关动作和内部电路节点，简化模型采用本文提出的四端口等效电压源电路。稳态和暂态工况下，LVDC电压$u_{C4}$、MVAC侧电流$i_1$、储能电流$i_{bat}$等关键电气量的波形一致性良好，最大相对误差小于1% | 比详细模型(DM)仿真速度快2-3个数量级(100-1000倍加速)，同时保持极高的仿真精度 |

| 大规模AC-DC混合电网适应性测试 | 验证所提简化模型在含多个PET和储能系统的复杂电网中的适用性。由于模型消除了内部高频开关细节，可采用更大的仿真步长(微秒级提升至数百微秒级)，显著降低计算负担 | 相比传统Thevenin等效方法，建模难度降低且避免了内部节点消除带来的数值稳定性问题，适用于高压大功率PET拓扑 |



## 量化发现

- 仿真速度提升：所提简化等效模型(SEM)比详细模型(DM)快2至3个数量级(即100倍至1000倍加速)
- 模型精度：在PSCAD/EMTDC平台验证中，关键电气量(端口电压、电流、功率)的波形误差极小，具有极高精度(excellent accuracy)
- 谐波截断：仅保留直流分量和基波分量(N=1)，忽略k≥2的高次谐波，实现状态空间维度大幅降低
- 拓扑适应性：适用于SAB、DAB、QAB、CHB-DAB、CHB-MAB等多种拓扑结构，特别是m-to-1结构的多主动桥
- 仿真步长：由于消除高频开关细节，可采用比详细模型大得多的仿真步长，克服PET仿真步长远小于MMC的技术瓶颈


## 关键公式

### 零阶(直流)状态空间方程

$$$$\frac{d}{dt}\langle x \rangle_0 = A_0\langle x \rangle_0 + B_0\langle u \rangle_0 + \text{coupling terms}$$$$

*广义状态空间平均法中描述状态变量直流分量的动态方程，用于提取系统的低频慢变特性，是构建四端口等效电压源电路的基础*

### ESS Dommel等效电路参数

$$$$G_{eq} = \frac{2C}{\Delta t} + \frac{1}{R_{bat}}, \\quad I_{hist}^{n} = -G_{eq}U_{C4}^{n-1} - I_{bat}^{n-1}$$$$

*基于Dommel算法和二元电阻法的储能子模块离散化等效，用于构建保留储能接口的Thevenin等效模型，支持混合储能系统的电磁暂态仿真*



## 验证详情

- **验证方式**: 仿真对比验证(与详细开关模型对比)
- **测试系统**: 中国河北省崇礼区配电网络中实际运行的MAB-PET系统，具有输入串联输出并联(ISOP)拓扑结构，包含CHB、MAB和集成储能子模块(ESS)
- **仿真工具**: PSCAD/EMTDC电磁暂态仿真软件
- **验证结果**: 所提简化等效模型在稳态运行、功率波动、充放电切换等工况下均表现出与详细模型极高的一致性，关键电气量波形几乎完全重合。仿真耗时比详细模型减少2-3个数量级，有效解决了MAB-PET因节点数多、步长小导致的计算瓶颈问题，适用于含多PET和混合储能的大规模AC-DC混合电网仿真
