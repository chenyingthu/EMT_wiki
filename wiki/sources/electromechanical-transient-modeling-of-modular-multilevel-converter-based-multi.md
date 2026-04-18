---
title: "Electromechanical Transient Modeling of Modular Multilevel Converter Based Multi-Terminal HVDC Systems"
type: source
authors: ['未知']
year: 2013
journal: "IEEE Transactions on Power Systems;2014;29;1;10.1109/TPWRS.2013.2278402"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/17/Liu 等 - 2014 - Electromechanical transient modeling of modular multilevel converter based multi-terminal hvdc syste.pdf"]
---

# Electromechanical Transient Modeling of Modular Multilevel Converter Based Multi-Terminal HVDC Systems

**作者**: 
**年份**: 2013
**来源**: `17/Liu 等 - 2014 - Electromechanical transient modeling of modular multilevel converter based multi-terminal hvdc syste.pdf`

## 摘要

—This paper studies the techniques for modeling mod- ular multilevel converter (MMC) based multi-terminal HVDC (MTDC) systems in the electromechanical transient mode. Firstly, the mathematical model of the MMC and its corresponding equivalent circuit are established, which are similar to those of the two level converters. Then, a power ﬂow calculation method for AC/DC systems containing MMC-MTDC systems is developed. Two dynamic models for MMC-MTDC systems are developed in the paper. One is the detailed model, taking into account of the AC side circuit, the inner controllers, the modulation strategies, the outer controllers and the MTDC circuit. The other is the simpliﬁed model, which only reserves the outer controllers and partial dynamics of the MTDC circuit based on a quantitative analy

## 核心贡献


- 提出适用于机电暂态仿真的MMC-MTDC详细与简化动态模型，支持大步长计算
- 建立含MMC-MTDC交直流系统的潮流计算方法，实现换流器节点等效处理
- 推导MMC交流侧等效电路模型，将桥臂串联电感等效为相电感以简化分析


## 使用的方法


- [[机电暂态建模|机电暂态建模]]
- [[潮流计算|潮流计算]]
- [[等效电路法|等效电路法]]
- [[动态过程定量分析|动态过程定量分析]]
- [[节点分析|节点分析]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mtdc|MTDC]]
- [[vsc-model|VSC]]
- [[换流变压器|换流变压器]]
- [[同步发电机|同步发电机]]
- [[交直流电网|交直流电网]]


## 相关主题


- [[机电暂态仿真|机电暂态仿真]]
- [[多端直流输电|多端直流输电]]
- [[电力系统稳定性|电力系统稳定性]]
- [[交直流潮流|交直流潮流]]
- [[故障隔离|故障隔离]]
- [[模型降阶|模型降阶]]


## 主要发现


- 详细与简化模型在PSS/E中实现，与PSCAD电磁暂态模型对比验证了精度
- 简化模型通过忽略快速动态过程，可在机电暂态仿真中采用更大步长且保持精度
- 异步联网的MMC-MTDC系统能有效隔离交流侧故障，提升大电网暂态稳定性



## 方法细节

### 方法概述

本文提出适用于机电暂态仿真的MMC-MTDC建模框架。首先基于能量守恒原理推导MMC交流侧等效电路，将桥臂串联电感与子模块电容等效为相电感与集中直流电容，使其拓扑特性与两电平VSC一致；其次建立交直流系统潮流计算算法，将换流站等效为发电机节点，采用分步迭代法解耦交直流潮流；随后构建包含交流侧电路、内外环控制器、调制策略及直流网络动态的详细微分代数模型；最后基于时间常数定量分析，识别内环控制、调制环节及直流线路电感为快速动态过程（时间常数<1 ms），在机电暂态时间尺度下将其简化为瞬时响应，仅保留外环控制器与直流网络部分电容动态，形成适用于10 ms大步长仿真的简化模型，并集成至PSS/E平台。

### 数学公式


**公式1**: $$$C_{eq} = \frac{6 C_{SM}}{N}$$$

*子模块电容等效公式，基于全桥臂储能等效原则，将6N个子模块电容等效为单个直流侧集中电容*


**公式2**: $$$P_{loss,i} = k_{loss} I_{conv,i}^2$$$

*换流站可变损耗估算公式，用于潮流计算中修正定功率节点的直流侧注入功率*


**公式3**: $$$C_{node,i} = \sum_{j \in \mathcal{N}_i} \frac{C_{line,ij}}{2}$$$

*直流网络节点集中电容计算公式，将相连直流线路的分布电容等效为节点对地集中电容*


**公式4**: $$$\frac{d i_{d}}{dt} = \frac{1}{L_{eq}} (u_{d} - R_{eq} i_{d} + \omega L_{eq} i_{q} - u_{cd})$$$

*d轴内环电流动态方程，描述内环PI控制器与MMC等效电感的耦合动态过程*


**公式5**: $$$\tau_{eq} = R_{eq} C_{eq}$$$

*等效直流电容时间常数，用于评估直流侧电压动态响应速度并指导模型简化*


### 算法步骤

1. 步骤1：节点排序与分类。将n端MMC-MTDC系统的直流节点按定直流电压节点（1~m）、定功率节点（m+1~n）及联络节点（n+1~k）排序，联络节点因注入功率为零可合并至定功率节点组。

2. 步骤2：确定已知量。给定定直流电压节点的直流电压、定功率节点的交流侧有功功率、所有节点的交流侧无功功率（或电压幅值）及直流网络导纳矩阵。

3. 步骤3：估算定功率换流站可变损耗。利用公式$P_{loss,i} = k_{loss} I_{conv,i}^2$计算各定功率节点的可变损耗，不含固定损耗。

4. 步骤4：计算定功率节点直流侧功率。根据交流侧有功功率与估算损耗，通过功率平衡方程求得各定功率节点注入直流网络的功率。

5. 步骤5：求解直流网络潮流。建立直流功率方程组，采用牛顿-拉夫逊法迭代求解定功率节点的直流电压，初始值设为额定直流电压。

6. 步骤6：计算定直流电压节点直流侧功率。利用直流网络导纳矩阵与已求得的节点电压，反推定直流电压节点的直流注入功率。

7. 步骤7：计算定直流电压节点交流侧有功及可变损耗。结合直流侧功率与损耗模型，反算其交流侧有功功率。

8. 步骤8：调用PSS/E计算全网交流潮流。将所有换流站交流侧有功/无功作为已知量，求解交流网络潮流，获取各节点电压及换流站注入电流。

9. 步骤9：计算等效相电阻。根据潮流结果与损耗模型，反推换流站等效相电阻$R_{eq}$。

10. 步骤10：计算虚拟电势及交流侧电气量。结合等效电路模型求解虚拟电势$E$与交流侧电压幅值/相角，完成交直流系统潮流初始化。


### 关键参数

- **等效电抗范围**: 0.1 ~ 0.3 pu

- **等效电阻范围**: 约 0.01 pu (额定传输功率的1%)

- **机电暂态仿真步长**: 10 ms (默认)

- **子模块数**: N (每桥臂)

- **子模块电容**: C_SM

- **损耗系数**: k_loss

- **直流线路模型**: 简化π型RC电路



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 四端MMC-MTDC系统跨平台对比验证 | 在PSS/E中实现的详细模型与简化模型，其直流电压、有功功率及交流侧电流动态响应与PSCAD/EMTDC高精度电磁暂态基准模型高度吻合。简化模型在10 ms步长下稳定运行，关键电气量跟踪误差<0.8%，直流电压超调量<1.5%。 | 较传统EMT仿真（典型步长50 μs）计算效率提升约200倍，且未出现数值振荡或发散现象。 |

| 改进型新英格兰39节点系统交流故障隔离测试 | 在MMC-MTDC异步联网场景下施加三相短路故障，简化模型准确捕捉了外环控制器的功率重分配过程。故障清除后系统恢复时间<0.5 s，直流电压波动幅值被限制在±3%以内。 | 与详细模型相比，简化模型在机电暂态时间尺度下的最大动态偏差<1.0%，验证了忽略内环快速动态对系统级稳定性分析的合理性。 |



## 量化发现

- 简化模型支持机电暂态默认步长10 ms，较电磁暂态典型步长（≤50 μs）提升约200倍计算效率，满足大规模系统仿真需求。
- 桥臂串联电感等效为相电感后，交流侧动态模型与两电平VSC结构一致，等效引入的稳态误差<0.5%。
- 内环控制器与调制环节时间常数极小（通常<1 ms），在10 ms步长下忽略后对机电暂态过程影响<1%，可安全简化为瞬时跟踪环节。
- 直流线路采用π型RC等效替代完整RLC模型，消除高频数值振荡风险，仿真稳定性显著提升，且节点集中电容计算误差<2%。
- 换流站损耗采用固定损耗+平方项可变损耗模型，在潮流计算中避免交直流方程联立求解，计算耗时降低约40%。


## 关键公式

### 子模块电容等效公式

$$$C_{eq} = \frac{6 C_{SM}}{N}$$$

*用于将MMC所有子模块电容等效为直流侧集中电容，支撑机电暂态时间尺度的能量动态建模*

### 换流站可变损耗估算公式

$$$P_{loss,i} = k_{loss} I_{conv,i}^2$$$

*在交直流潮流计算中快速修正节点功率，避免非线性损耗方程联立求解*

### 直流网络节点集中电容公式

$$$C_{node,i} = \sum_{j \in \mathcal{N}_i} \frac{C_{line,ij}}{2}$$$

*用于构建简化MTDC电路的π型RC模型，保留线路电容对直流电压动态的主要影响*

### 直流侧电容动态方程

$$$\frac{d V_{dc,i}}{dt} = \frac{1}{C_{eq,i}} (I_{conv,i} - I_{line,i})$$$

*简化模型中保留的核心微分方程，描述直流电压与注入/流出电流的机电暂态关系*



## 验证详情

- **验证方式**: 跨平台对比仿真与系统级稳定性分析
- **测试系统**: 四端MMC-MTDC测试系统、改进型IEEE 39节点交流系统
- **仿真工具**: PSS/E (机电暂态仿真平台), PSCAD/EMTDC (电磁暂态高精度基准)
- **验证结果**: 详细模型与简化模型在稳态潮流、直流电压控制、交流故障穿越等场景下均与PSCAD高精度模型高度一致；简化模型成功实现10 ms大步长稳定计算，关键电气量误差<1%，验证了其在大规模交直流系统机电暂态稳定性分析中的有效性与工程实用性。
