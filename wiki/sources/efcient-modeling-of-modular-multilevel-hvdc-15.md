---
title: "Efﬁcient Modeling of Modular Multilevel HVDC"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient modeling of modular multilevel HVDC converters (MMC) on electromagnetic transient simulati_Gnanarathna 等_2011.pdf"]
---

# Efﬁcient Modeling of Modular Multilevel HVDC

**作者**: 
**年份**: 2010
**来源**: `15/Efficient modeling of modular multilevel HVDC converters (MMC) on electromagnetic transient simulati_Gnanarathna 等_2011.pdf`

## 摘要

—The number of semiconductor switches in a modular multilevel converter (MMC) for HVDC transmission is typically two orders of magnitudes larger than that in a two or three level voltage-sourced converter (VSC). The large number of devices creates a computational challenge for electromagnetic transient simulation programs, as it can signiﬁcantly increase the simula- tion time. The paper presents a method based on partitioning the system’s admittance matrix and deriving an efﬁcient time-varying Thévenin’s equivalent for the converter part. The proposed method does not make use of approximate interfaced models, and mathematically, is exactly equivalent to modelling the entire network (converter and external system) as one large network. It is shown to drastically reduce the computational tim

## 核心贡献


- 提出基于导纳矩阵分割的MMC建模方法，推导高效时变戴维南等效电路
- 采用嵌套快速同步求解技术解耦MMC与外网，实现数学精确等效
- 避免近似接口模型，在保留全网络精度的同时大幅降低EMT仿真耗时


## 使用的方法


- [[导纳矩阵分割|导纳矩阵分割]]
- [[时变戴维南等效|时变戴维南等效]]
- [[嵌套快速同步求解|嵌套快速同步求解]]
- [[节点分析法|节点分析法]]
- [[电容电压平衡控制|电容电压平衡控制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[功率子模块|功率子模块]]
- [[igbt-二极管开关|IGBT/二极管开关]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[网络等值|网络等值]]
- [[计算效率优化|计算效率优化]]
- [[换流器建模|换流器建模]]


## 主要发现


- 所提方法在数学上与传统全网络建模完全等效，未牺牲任何仿真精度
- 仿真验证表明该方法大幅降低计算时间，有效解决频繁开关导致的矩阵求逆瓶颈
- 成功应用于点对点VSC-MMC直流系统，验证了模型在暂态过程中的有效性



## 方法细节

### 方法概述

本文提出一种基于导纳矩阵分割与嵌套快速同步求解（Nested Fast and Simultaneous Solution）的MMC电磁暂态高效建模方法。核心思想是将包含MMC的电力系统划分为外部交流/直流网络（子系统1）与MMC各相阀臂（子系统2）。利用梯形积分法将子模块内的电容与IGBT/二极管双向开关等效为时变电阻与历史电压源串联的戴维南电路。基于阀臂内子模块串联的拓扑特性，通过直接叠加各子模块的等效参数，推导出整个阀臂的精确时变戴维南等效模型（仅含一个等效电阻和一个等效电压源）。该等效模型随后转换为诺顿形式接入主EMT求解器，使主网络导纳矩阵规模从数千节点骤降至仅含接口节点。该方法在数学上与传统全网络节点分析法完全等价，未引入任何近似接口，完整保留了子模块级动态特性，可无缝集成电容电压平衡控制与开关故障仿真。

### 数学公式


**公式1**: $$$\begin{bmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$$

*系统分区节点导纳矩阵方程，将网络划分为外部系统(1)与MMC阀臂(2)*


**公式2**: $$$V_2 = Y_{22}^{-1}(I_2 - Y_{21}V_1)$$$

*子系统2（MMC内部）节点电压表达式，用于后续等效推导*


**公式3**: $$$(Y_{11} - Y_{12}Y_{22}^{-1}Y_{21})V_1 = I_1 - Y_{12}Y_{22}^{-1}I_2$$$

*消去内部节点后的降阶外部网络方程，括号内为等效边界导纳*


**公式4**: $$$v(t) = \frac{\Delta t}{2C}i(t) + v_{hist}(t)$$$

*基于梯形积分法的电容等效模型，将动态电容转化为电阻与历史电压源串联*


**公式5**: $$$V_{th} = \sum_{k=1}^{N} V_{hist,k}, \quad R_{th} = \sum_{k=1}^{N} R_{eq,k}$$$

*阀臂级戴维南等效参数聚合公式，通过串联叠加实现多节点到两节点的精确降阶*


### 算法步骤

1. 网络分区与初始化：将电力系统划分为外部网络与MMC各相阀臂，初始化所有子模块电容电压、开关状态及历史电流/电压项。

2. 控制信号生成：根据参考正弦波与离散量化阈值比较，生成当前时刻需投入（ON）或切除（OFF）的子模块数量指令 $n(t)$。

3. 电容电压平衡排序：在每次电平切换时刻，测量阀臂内所有子模块电容电压并按幅值排序。根据阀臂电流方向，选择电压最低（充电时）或最高（放电时）的指定数量子模块投入运行。

4. 子模块等效计算：根据各子模块开关状态（ON/OFF电阻）与梯形积分公式，计算单个子模块的等效电阻 $R_{eq,k}$ 和历史电压源 $V_{hist,k}$。

5. 阀臂戴维南聚合：利用串联叠加原理，将同一阀臂内所有子模块的等效电阻与历史电压源分别求和，得到该阀臂的戴维南等效参数 $R_{th}$ 和 $V_{th}$。

6. 接口转换与主网求解：将阀臂戴维南等效转换为诺顿等效，接入主EMT求解器。求解降阶后的外部网络导纳矩阵，获取接口节点电压。

7. 内部状态更新：利用接口节点电压反推阀臂电流，更新各子模块电容电压及历史项，为下一时间步迭代做准备。


### 关键参数

- **仿真步长**: 20 μs

- **子模块数量范围**: 2~120个/阀臂

- **直流系统额定值**: 400 MW / 200 kV

- **开关器件模型**: 两态电阻（导通电阻/关断电阻）

- **数值积分方法**: 梯形积分法（A稳定），对比测试2S-DIRK法

- **硬件平台**: Intel Core 2 Duo 3.0 GHz, 3.37 GB RAM, Windows XP



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单阀臂正常稳态与暂态运行 | 12个子模块/阀臂下，触发脉冲、子模块输出电压、电容电压、电容电流及MMC输出波形与传统全模型完全重合，阶梯波形清晰可见。 | 波形误差<0.1%，数学上完全等价 |

| 单子模块开关永久导通故障 | 模拟下管IGBT永久导通故障，模型准确复现了故障瞬间的电压跌落、电容过充及稳态畸变过程。 | 与传统模型暂态及稳态响应一致，验证了故障级建模能力 |

| 电容电压平衡控制投切 | 1.0s切除平衡控制，候选电容电压因占空比差异迅速发散；2.0s重新投入控制，电容电压在数十毫秒内快速恢复均衡。 | 动态响应与传统模型一致，验证了控制接口有效性 |

| 点对点HVDC系统功率阶跃 | 400MW/200kV系统（100子模块/阀臂）功率指令从1.0 p.u.降至0.5 p.u.，系统90%响应时间为47ms，交直流电压波动<8%。 | 传统模型无法在合理时间内完成，等效模型117s完成5s仿真 |

| 逆变器侧单相接地故障(L-G) | 8s施加150ms A相接地故障，准确捕捉到交流电流骤增、直流电压跌落、功率振荡及故障清除后的恢复过程。 | 波形与传统模型高度吻合，传统模型因耗时过长仅能缩减至24子模块/阀臂进行对比 |



## 量化发现

- 120子模块/阀臂（共240个）仿真5s：传统模型耗时>2.5小时，本文模型仅需30秒，计算速度提升约310倍（31107%）
- 完整HVDC系统（100子模块/阀臂，共2400个开关）仿真5s：传统模型预估耗时>14小时，本文模型耗时<2分钟
- 模型精度：所有测试场景下，电压/电流波形与传统全节点模型误差<0.1%，数学严格等价
- 数值积分对比：采用2S-DIRK法替代梯形积分法，仿真精度与计算速度均无显著差异（差异<2%）
- 功率阶跃响应：系统达到90%目标功率仅需47ms，交直流母线电压最大波动幅度<8%


## 关键公式

### 阀臂戴维南等效电压源

$$$V_{th} = \sum_{k=1}^{N} V_{hist,k}$$$

*用于将N个串联子模块的历史电压项直接叠加，构建阀臂级等效电路*

### 阀臂戴维南等效电阻

$$$R_{th} = \sum_{k=1}^{N} R_{eq,k}$$$

*根据各子模块当前开关状态（导通/关断电阻）与电容等效电阻求和，实时更新阀臂阻抗*

### 降阶外部网络节点方程

$$$(Y_{11} - Y_{12}Y_{22}^{-1}Y_{21})V_1 = I_1 - Y_{12}Y_{22}^{-1}I_2$$$

*通过矩阵分割消去MMC内部节点，大幅缩减主EMT求解器需处理的导纳矩阵规模*



## 验证详情

- **验证方式**: 对比仿真验证（与传统全节点EMT模型逐波形对比）
- **测试系统**: 单阀臂测试电路及点对点MMC-HVDC输电系统（400 MW/200 kV，每阀臂100个子模块，共2400个开关器件）
- **仿真工具**: PSCAD/EMTDC (X4 Beta版), Windows XP, Intel Core 2 Duo 3.0 GHz
- **验证结果**: 验证表明所提等效模型在数学上与传统全网络建模完全等价，未牺牲任何仿真精度。在子模块数量增加时，计算耗时呈线性/低阶增长，而传统模型呈指数级增长。成功实现大规模MMC-HVDC系统在个人计算机上的高效暂态仿真，支持正常工况、开关故障、控制投切及电网故障等全场景分析。
