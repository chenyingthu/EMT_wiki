---
title: "模块化多电平换流器 (MMC)"
type: model
tags: [mmc, hvdc, converter, sub-module, arm]
created: "2026-04-13"
---

# 模块化多电平换流器 (MMC)

## 概述

模块化多电平换流器（Modular Multilevel Converter, MMC）是当前高压直流输电（HVDC）和柔性交流输电系统的主流拓扑。由多个子模块（SM）级联构成桥臂，具有模块化、可扩展、低谐波等优势。

## 结构特点

- **桥臂结构**：三相六桥臂，每桥臂含N个子模块
- **子模块类型**：半桥（HBSM）、全桥（FBSM）、箝位双子模块等
- **电容电压平衡**：需要复杂的排序和均压算法
- ** circulating current**：桥臂内存在环流

## EMT建模方法

### 1. 详细模型
- 每个子模块单独建模
- 包含开关动态和电容电压
- 计算量极大，适用于少量SM

### 2. 平均值模型 (AVM)
- 桥臂平均化处理
- 忽略开关纹波，保留低频动态
- 计算效率提升1-2个数量级
- 增强平均值模型（考虑环流）

### 3. 等效模型
- Thevenin等效桥臂
- 嵌套快速求解方法
- 任意多端口子模块结构

### 4. 固定导纳模型
- ADC建模，避免矩阵重构
- 适用于实时仿真
- FPGA硬件实现

### 5. 动态相量模型
- 频域MMC建模
- 适用于混合仿真
- 宽频暂态分析

## 关键技术挑战

- 子模块电容电压平衡
- 环流抑制控制
- 直流故障穿越
- 损耗建模（虚假功率问题）
- 大规模MMC-MTDC系统仿真

## 相关方法
- [[average-value-model]]
- [[fixed-admittance]]
- [[state-space-method]]
- [[dynamic-phasor]]

## 相关模型
- [[vsc-model|VSC模型]] - 两电平/三电平换流器对比
- [[fdne-model|频变网络等值(FDNE)]] - MMC外部网络等值
- [[transformer-model|换流变压器]] - MMC换流变建模
- [[cable-model|电缆模型]] - 直流电缆连接
- [[mtdc-model|MTDC模型]] - 多端MMC系统

## 相关主题
- [[vsc-hvdc]]
- [[real-time-simulation]]
- [[co-simulation]]
- [[frequency-dependent-modeling]]
- [[parallel-computing]]


## 论文方法分析
> 基于 73 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 电磁暂态(EMT)仿真 | 7 | Ahmed 等 | A Computationally Efficient Continuous Model for the Modular |
| 平均值建模(AVM) | 6 | Adaptive Modular Multilevel Converter Model for Electromagnetic Transi |
| 机电暂态建模 | 4 | A review of efficient modeling methods for modular multilevel converte |
| 戴维南等效法 | 4 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 等效电路建模 | 4 | Generalized Electromagnetic Transient Equivalent Modeling and Implemen |
| 开关函数法 | 4 | Hybrid-model transient stability simulation using dynamic phasors base |
| 平均值建模 | 3 | A review of efficient modeling methods for modular multilevel converte |
| 状态空间法 | 3 | A state-space approach for accelerated simulation of modular multileve |
| 详细等效模型(DEM) | 3 | An accelerated detailed equivalent model for modular multilevel conver |
| 梯形积分法 | 2 | A review of efficient modeling methods for modular multilevel converte |
| 桥臂等效建模(AEM) | 2 | Adaptive Modular Multilevel Converter Model for Electromagnetic Transi |
| 详细等效建模(DEM) | 2 | Adaptive Modular Multilevel Converter Model for Electromagnetic Transi |
| 戴维南等效电路 | 2 | An accelerated detailed equivalent model for modular multilevel conver |
| 等效电路法 | 2 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 多速率仿真技术 | 2 | Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Ty |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 模块化多电平换流器(MMC) | 37 |
| MMC-HVDC系统 | 9 |
| 子模块(SM) | 5 |
| 详细等效模型(DEM) | 4 |
| 子模块 | 3 |
| 模块化多电平换流器 (MMC) | 3 |
| 详细模型(DM) | 3 |
| 平均值模型 | 3 |
| 平均值模型(AVM) | 3 |
| MMC子模块(SM) | 2 |
| MMC(模块化多电平换流器) | 2 |
| 详细开关模型 | 2 |
| 半桥/全桥子模块 | 2 |
| 半桥子模块(HBSM) | 2 |
| IEEE 39节点交流系统 | 2 |
### 验证方式分布
- **仿真**: 29 篇
- **仿真/对比**: 13 篇
- **仿真对比**: 9 篇
- **仿真与对比**: 4 篇
- **仿真与实验**: 3 篇
- **仿真对比与实验验证**: 2 篇
- **仿真与实验对比**: 2 篇
- **仿真验证与对比**: 1 篇
- **仿真与硬件在环实验**: 1 篇
- **仿真对比（与详细电磁暂态模型进行基准对比）**: 1 篇
- **离线与实时仿真对比验证**: 1 篇
- **仿真与对比验证（基于PSCAD/EMTDC平台，与详细模型和状态空间模型对比）**: 1 篇
- **仿真对比（PSS/E机电暂态与PSCAD电磁暂态结果对比）**: 1 篇
- **仿真验证/对比**: 1 篇
- **HIL硬件在环仿真与PSCAD/EMTDC离线仿真对比**: 1 篇
- **仿真对比与实时硬件实验**: 1 篇
- **仿真对比（GPU并行实现与CPU串行实现对比）**: 1 篇
- **仿真对比验证（与全电磁暂态EMT模型进行多工况对比）**: 1 篇
## 技术演进脉络
### 2006年 (2篇)
- **Hybrid-model transient stability simulation using dynamic phasors based HVDC sys**
  - 💡 将动态相量理论引入HVDC建模，填补了电磁暂态(EMT)与准稳态(QSS)模型之间的空白，实现了兼顾精度与计算效率的交直流系统混合暂态仿真。
  - 推导了基于动态相量理论的详细HVDC系统数学模型。
  - 提出了直流动态相量模型与交流网络的高效接口算法。
- **Hybrid-model transient stability simulation using dynamic phasors based HVDC sys**
  - 💡 将动态相量理论引入HVDC建模，有效填补了电磁暂态(EMT)与准稳态(QSS)模型在计算效率与精度之间的鸿沟，实现了大规模交直流系统的高效混合暂态仿真。
  - 推导了基于动态相量理论的详细HVDC系统数学模型。
  - 提出了直流动态相量模型与交流电网的高效接口算法。
### 2010年 (1篇)
- **Efﬁcient Modeling of Modular Multilevel HVDC**
  - 💡 提出了一种无需近似接口、数学严格等效的导纳矩阵分区与时变戴维南等效方法，从根本上解决了MMC大规模开关器件导致的EMT仿真计算瓶颈。
  - 提出了一种基于导纳矩阵分区和时变戴维南等效的MMC高效建模方法。
  - 证明了该方法在数学上与将整个网络作为单一大型网络建模完全等效，且不牺牲精度。
### 2013年 (2篇)
- **Electromechanical Transient Modeling of Modular Multilevel Converter Based Multi**
  - 💡 提出了一种基于动态过程定量分析的MMC-MTDC简化机电暂态模型，在保留核心控制与网络动态的前提下显著提升了机电暂态仿真的计算效率与步长。
  - 建立了MMC的数学模型及等效电路，揭示了其与两电平换流器模型的相似性。
  - 提出了适用于含MMC-MTDC交直流系统的潮流计算方法。
- **Modular Multilevel Converter Models**
  - 💡 提出基于开关函数原理的MMC新模型与改进AVM，并通过迭代算法首次有效解决了简化模型中子模块闭锁状态的精确建模问题。
  - 提出了一种基于开关函数原理应用于MMC各桥臂的新型电磁暂态仿真模型。
  - 开发了一种改进的平均值模型(AVM)，在保持动态精度的同时显著提升了计算速度。
### 2014年 (2篇)
- **Ahmed 等 | A Computationally Efficient Continuous Model for the Modular Multileve**
  - 💡 提出了一种能准确模拟MMC阻塞状态的连续等效模型，在兼顾计算效率的同时解决了传统模型故障仿真失真的问题
  - 提出了一种计算高效的MMC连续模型，适用于EMT仿真程序
  - 突破了传统平均模型无法描述换流器阻塞状态的局限
- **Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC G**
  - 💡 通过引入拓扑结构改进，解决了传统平均值模型在直流故障工况下暂态仿真失真的问题。
  - 评估了平均值模型在VSC-HVDC电网中MMC仿真的适用性边界。
  - 揭示了现有平均值模型在直流故障工况下暂态仿真精度不足的缺陷。
### 2015年 (4篇)
- **A review of efficient modeling methods for modular multilevel converters**
  - 💡 首次按时间尺度与应用场景对MMC建模方法进行全面分类与横向对比，构建了清晰的模型选型指南与适用边界。
  - 系统梳理了不同时间尺度与应用场景下的MMC高效建模方法研究现状与发展脉络。
  - 对三种微秒级电磁暂态精确模型（受控源通用提速模型、基于后退欧拉法与梯形法的戴维南等效整体模型）进行了严格的横向对比与仿真验证。
- **Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes**
  - 💡 提出了一种改进的MMC详细建模方法，在保持精度的同时进一步优化了计算效率，并首次系统对比了主流建模技术的适用场景。
  - 首次客观对比了三种主流MMC详细建模技术在精度与仿真速度方面的表现。
  - 提出了一种改进的建模方法，进一步提升了现有等效模型的计算效率。
- **Transient Stability Analysis of MMC-HVDC System Considering DC-side Fault**
  - 💡 首次将2D并行矩阵乘法与GPU专用稀疏技术深度融合于EMT仿真，并定量揭示了系统拓扑粒度与GPU硬件加速性能之间的非线性权衡机制。
  - 提出了一种基于GPU的2D并行矩阵向量乘法算法，突破了传统1D方法的性能瓶颈。
  - 开发了专为GPU架构优化的稀疏矩阵处理技术及电力电子开关并行实现方案。
- **模块化多电平换流器戴维南等效整体建模方法**
  - 💡 结合理想开关假设、后退欧拉离散法与插值二极管技术，构建了计算复杂度线性增长且兼顾高精度与超高速的MMC戴维南等效整体模型。
  - 提出了一种基于戴维南等效的MMC电磁暂态整体建模方法，显著提升了高电平数MMC的仿真效率。
  - 采用后退欧拉法离散子模块电容并结合理想关断假设，有效避免了数值振荡并提高了算法稳定性。
### 2016年 (2篇)
- **Current Source Modular Multilevel Converter Modeling and Control**
  - 💡 通过两节点Norton等效电路重构CSMMC桥臂，在消除内部节点提升计算效率的同时，兼顾了系统级动态精度与子模块级详细研究需求。
  - 提出基于Norton等效的CSMMC两节点桥臂等效模型，消除内部中间节点以大幅降低计算负担。
  - 开发适用于子模块级详细研究（如冗余配置与故障安全功能）的混合仿真模型。
- **Improved Accuracy Average Value Models of Modular Multilevel Converters**
  - 💡 通过多项算法改进提出一种兼顾计算效率与高精度的MMC平均值模型，突破了传统AVM在直流故障等复杂工况下精度不足的瓶颈。
  - 系统分析了现有MMC平均值模型在精度与适用性方面的局限性
  - 提出一种改进的高精度MMC-AVM，通过多项算法修改显著提升模型准确性
### 2017年 (3篇)
- **A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems**
  - 💡 将多速率分区仿真、高精度动态接口预测校正与数值振荡抑制技术深度融合，实现了不简化换流器与交流网络动态的大规模交直流系统高效稳定协同仿真。
  - 提出了一种新型多速率EMT协同仿真架构，通过系统分区与差异化步长设置显著提升大规模交直流系统的仿真效率。
  - 构建了基于时变戴维南/诺顿等效的接口模型，并引入滑动窗口预测与逐步校正技术以消除混叠与时延误差。
- **Modeling of Modular Multilevel Converters with Different Levels of Detail**
  - 💡 将IGBT动态电热特性建模与传输线短截线等效相结合，并通过电路分区简化技术，在FPGA上实现了兼顾器件级精度与实时性的大规模MMC系统仿真。
  - 提出基于IGBT动态曲线拟合的非线性开关模型，可在电磁-热仿真中准确复现器件级功率损耗与结温。
  - 将MMC子模块等效为传输线短截线，显著提升计算速度并支持混合桥臂结构以节省FPGA资源。
- **含VSC-HVDC交直流系统多尺度暂态建模与仿真研究**
  - 💡 提出基于移频分析与希尔伯特变换的多尺度暂态建模方法，通过单一模型参数调节即可实现电磁与机电暂态仿真的无缝切换与高效计算。
  - 建立了基于移频分析的VSC相量模型，并推导了移频域与控制系统dq域的数学转换关系。
  - 提出了通过选择性插入π型线段构建直流输电线路多尺度暂态模型的方法。
### 2018年 (8篇)
- **A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT Simulatio**
  - 💡 提出基于基频动态相量的MMC扩展频域建模方法，实现了内部谐波与外部多频分量的高效精确建模，并可直接无缝接入EMT仿真器。
  - 提出了一种适用于EMT仿真的MMC扩展频域动态相量模型。
  - 引入基频动态相量新结构，可在不显著增加计算负担的情况下捕捉外部变量的任意频率分量。
- **An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Rep**
  - 💡 通过引入臂电流初始化机制与闭锁工况等效表征，解决了传统控制信号型AVM初始条件不准及无法模拟闭锁运行的问题。
  - 提出了一种增强型MMC平均值模型，可准确表征换流器闭锁运行工况。
  - 设计了臂电流初始化方法，有效补偿了现有平均值模型的初始条件误差。
- **Fast Electromagnetic Transient Model for MMC-HVDC Considering DC Fault**
  - 💡 基于完整电磁场解构建大地返回阻抗/导纳统一模型，有效弥补传统公式忽略低频导纳的缺陷并显著提升暂态仿真精度
  - 提出基于完整电磁场解的大地返回阻抗与导纳广义计算公式
  - 从完整场解推导出适用于多相地下电缆的准TEM近似参数公式
- **High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Us**
  - 💡 基于Schur补数技术构建广义多端口诺顿等效，实现了对任意多端口子模块MMC的高效降阶EMT建模，在极大压缩矩阵规模的同时不丢失内部状态细节。
  - 提出了一种适用于任意多端口子模块结构MMC的高速高精度EMT建模方法。
  - 利用Schur补数技术递归消去内部节点，构建连接外部网络的广义多端口诺顿等效电路。
- **Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phaso**
  - 💡 提出结合移位相量与开关依赖戴维南等效的MMC建模方法，在FPGA上实现了兼顾子模块级细节与系统级动态的高效实时仿真。
  - 提出基于移位相量的MMC建模方法，通过戴维南等效电路显著提升了子模块级仿真精度。
  - 设计开关依赖的桥臂等效电路，使计算负担在子模块数量大幅增加时仍保持几乎不变。
- **The diode-clamped half-bridge MMC structure with internal spontaneous capacitor **
  - 💡 提出了一种基于二极管钳位与自发电容并联行为的新型半桥MMC拓扑，实现了无需额外传感器和复杂控制算法的电容电压自然平衡。
  - 提出了一种新型二极管钳位半桥MMC拓扑，通过集成钳位二极管和阻尼电阻实现电容电压自发并联平衡。
  - 揭示了拓扑中存在的6种自发电容并联行为(SCPBs)，证明了其无需依赖特定调制策略即可自然平衡电压。
- **Unified High-Speed EMT Equivalent and Implementation Method of MMCs with Single-**
  - 💡 提出了一种基于矩阵输入自动降阶与内部节点动态恢复的统一EMT等效框架，可无缝适配任意新型单端口子模块拓扑。
  - 提出了一种适用于任意单端口子模块结构的统一高速EMT等效方法。
  - 通过矩阵运算自动消去内部节点，避免了繁琐的解析推导过程。
- **双端口子模块MMC电磁暂态通用等效建模方法**
  - 💡 提出递归消去算法将双端口MMC桥臂等效为4个外部节点，在保留全部内部动态信息的同时实现高精度与高速度的电磁暂态仿真。
  - 提出了一种适用于任意新型双端口子模块MMC的电磁暂态通用等效建模方法。
  - 设计了针对双端口结构的递归求解算法，突破了传统单端口等效模型要求全桥臂电流一致的局限。
### 2019年 (11篇)
- **A Two-layer Network Equivalent with Local Passivity Compensation with Applicatio**
  - 💡 首创无需全局优化的局部无源性补偿双层网络等效方法，在保障混合仿真数值稳定性的同时实现了宽频动态的高精度与高效率捕捉。
  - 提出双层频变网络等效(T-FDNE)架构，通过详细层与等效层分别结合扰动测试与解析方法构建导纳矩阵。
  - 设计基于辅助有理函数的局部无源性补偿算法，摒弃全局优化过程，从根本上保障了时域仿真的数值稳定性。
- **A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Conv**
  - 💡 提出了一种基于通用闭锁模块的MMC平均值模型，统一支持多种子模块类型及闭锁/解锁工况的高效仿真与损耗计算。
  - 提出了一种兼容多种子模块类型的通用闭锁模块平均值模型。
  - 实现了MMC在闭锁与解锁双模式下的高精度动态仿真。
- **Electro-mechanical transient modeling of MMC based multi-terminal HVDC system wi**
  - 💡 将MMC直流侧等效为二阶电路用于机电暂态建模，并结合预设故障信息法实现了无需重构拓扑的高效直流故障仿真。
  - 理论推导了适用于直流故障分析的MMC二阶直流侧等效机电暂态模型。
  - 提出了一种基于预设直流故障信息的仿真方法，无需重构直流网络拓扑即可高效处理各类直流故障。
- **Electro-mechanical transient modeling of MMC based multi-terminal HVDC system wi**
  - 💡 提出含二阶直流侧电路的改进MMC机电模型及预设故障信息法，实现无需重构拓扑的高效直流故障暂态稳定仿真。
  - 推导了包含二阶直流侧电路的改进MMC机电暂态模型。
  - 提出基于预设直流故障信息的仿真方法以评估故障对系统稳定性的影响。
- **MMC-UPFC电磁-机电混合仿真技术研究**
  - 💡 提出了一种面向MMC-UPFC的电磁-机电混合仿真接口位置自适应配置方法，实现了大规模电网仿真中局部精细动态与外网准稳态特性的高效耦合。
  - 建立了基于MMC技术的UPFC高精度电磁暂态模型。
  - 探索并提出了混合仿真接口位置针对不同工况的适应性选择策略。
- **Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Elec**
  - 💡 通过多阀戴维南等效聚合技术，在保留子模块完整动态特性的前提下，实现了含储能MMC高精度与低计算复杂度电磁暂态仿真的统一。
  - 提出了一种适用于含嵌入式储能MMC的电磁暂态详细等效模型。
  - 通过将多阀等效为戴维南电路，在保持与详细开关模型同等精度的同时显著降低了计算复杂度。
- **Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System**
  - 💡 首次将并行时间算法引入电力电子仿真，通过粗细时间步模型协同与状态转换机制，有效解决了大规模MMC仿真中空间并行线程受限与计算负担过重的问题。
  - 提出了一种基于并行时间方法的电力电子系统仿真新架构，突破了传统空间并行加速的线程数限制。
  - 设计了粗时间步（平均值模型）与细时间步（详细模型）协同计算机制，实现状态的串行初始化与并行更新。
- **Real-Time MPSoC-Based Electrothermal Transient Simulation of Fault Tolerant MMC **
  - 💡 首次将等效电路与器件级电热模型融合，在MPSoC平台上实现了复杂CDSM拓扑的高精度实时电磁-电热耦合暂态仿真。
  - 提出了适用于实时EMT仿真的CDSM器件级电热模型，可准确呈现开关损耗、结温及瞬态波形。
  - 将系统级等效电路模型与器件级模型相结合，有效降低了计算负担以满足实时仿真需求。
- **Spurious Power Losses in Modular Multilevel Converter Arm Equivalent Model**
  - 💡 首次系统揭示并解析证明了EMT控制模块实现方式导致MMC桥臂等效模型产生虚假功率损耗的机理，并给出了兼顾精度与效率的替代建模方案
  - 揭示了在EMT软件中通过控制模块实现桥臂等效模型时会产生虚假功率损耗的现象及其成因
  - 通过解析推导证明了该虚假损耗的存在条件与影响机制
- **基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法**
  - 💡 通过引入辅助变量将分时段线性非齐次微分方程转化为齐次方程，实现了HVDC系统电磁暂态简化模型的高效解析求解。
  - 提出了一种基于状态空间法的HVDC系统电磁暂态简化模型解析算法。
  - 通过引入辅助变量将非齐次微分方程组转化为齐次形式，大幅降低了计算复杂度。
- **适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型**
  - 💡 提出基于子模块电容电量均分的阀段等效建模方法，在保障仿真精度的同时大幅提升了CH-MMC电磁暂态仿真效率。
  - 提出基于电容电量均分的CH-MMC快速仿真模型，有效降低电磁暂态仿真计算量。
  - 推导了半桥与全桥阀段在正常及闭锁状态下的等效电路，简化了模型拓扑结构。
### 2020年 (5篇)
- **A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analy**
  - 💡 首次将谐波相量域建模与EMT交流模型通过专用传输线接口结合，实现了大规模交直流电网瞬时波形与谐波相量的同步高效协同仿真。
  - 提出了适用于电力电子直流电网的谐波相量域(HPD)建模方法，可同时输出瞬时波形与谐波相量。
  - 设计了HPD传输线模型(HPD-TLM)，实现了EMT交流电网与HPD直流电网的高效接口与协同。
- **Adaptive Modular Multilevel Converter Model for Electromagnetic Transient Simula**
  - 💡 提出了一种可在EMT仿真中根据精度与效率需求动态平滑切换AVM、AEM与DEM的MMC自适应建模框架，并配套了完整的时域初始化策略。
  - 提出了一种集成AVM、AEM和DEM的MMC自适应模型，支持仿真过程中根据精度与计算时间约束平滑切换。
  - 详细阐述了实现不同模型间无缝切换所需的常规MMC模型修改方案。
- **Combining Detailed Equivalent Model With Switching-Function-Based Average Value **
  - 💡 提出了一种可在动态仿真过程中按需平滑切换详细等效模型与开关函数平均值模型的通用MMC建模框架，兼顾了仿真精度与计算效率。
  - 提出了一种结合DEM与SFB-AVM的通用建模框架，支持动态仿真中两种模型的平滑切换。
  - 开发的SFB-AVM能够准确表征包含不同子模块拓扑的MMC动态特性。
- **Hierarchical Device-Level Modular Multilevel Converter Modeling for Parallel and**
  - 💡 结合拓扑重构、网络等效、CPU/GPU异构计算与多速率技术，实现了含高精度器件级非线性模型的大规模MMC高效并行EMT仿真。
  - 提出了一种面向器件级MMC的多层级分层建模方法，有效缓解了大规模换流器与复杂模型带来的计算负担。
  - 通过拓扑重构与网络等效生成大量相同电路单元，实现了基于GPU的大规模并行处理。
- **Spurious power and its elimination in modular multilevel converter models**
  - 💡 首次系统揭示并解决了基于控制框图实现的MMC等效模型中因数值延迟导致的虚假功率问题。
  - 揭示了AEM和AVM模型中因控制框图实现导致的一步延迟会产生非物理的虚假功率。
  - 证明了虚假功率在特定工况下可占换流站总损耗的显著比例甚至超过实际损耗，严重影响仿真精度。
### 2021年 (5篇)
- **Average-Value Model for a Modular Multilevel Converter With Embedded Storage**
  - 💡 针对含子模块级嵌入式储能的MMC拓扑开发了兼顾计算效率与解析能力的平均值模型，填补了系统级分析与元件设计的建模空白。
  - 提出了一种适用于含子模块级储能MMC的高效平均值模型，适用于系统级研究。
  - 实现了对环流和子模块电容电压纹波的解析表征，支持有无环流抑制控制的分析。
- **Electromechanical transient modelling and application of modular multilevel conv**
  - 💡 提出带嵌入式储能的Active MMC机电暂态建模方法及协同控制策略，实现交直流系统有效解耦并增强电网抗扰动能力。
  - 建立了带储能子模块的Active MMC数学模型及其交直流侧等效电路。
  - 提出了MMC换流器与储能子模块协同工作的控制策略。
- **High Frequency Stability Analysis and Suppression Strategy of MMC-HVDC Systems (**
  - 💡 结合参与因子分析与根轨迹法，系统揭示了大链路延时下MMC-HVDC系统高频振荡的关键影响因素及其作用机理。
  - 建立了集成内部动态、控制环路、锁相环及大延时环节的MMC高频状态空间模型
  - 构建了采用多π型等效模拟分布参数特性的交流系统高频通用状态空间模型
- **Parallelization of MMC detailed equivalent model**
  - 💡 通过将MMC桥臂计算与电容均压算法解耦为独立DLL并在多核CPU上并行执行，突破了传统串行求解的瓶颈，实现了高精度DEM模型的高效离线仿真。
  - 提出了一种在离线EMT仿真中将MMC详细等效模型计算并行化至多核CPU的方法。
  - 将每个桥臂封装为独立DLL并与主求解器解耦，通过标准接口实现高效数据交互。
- **Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Tran**
  - 💡 创新性地结合波传播函数与移频相量技术，突破了传统模型在宽频域仿真中精度与效率难以兼顾的瓶颈。
  - 提出波传播函数(WPF)以精确描述MMC子模块的瞬态行为。
  - 开发基于傅里叶级数的移频相量(SFP)模型以加速系统级动态计算。
### 2022年 (5篇)
- **An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Co**
  - 💡 提出基于比例放大控制结构的MMC等效混合模型，在显著降低EMT仿真计算复杂度的同时，克服了传统简化模型无法完整反映内部动态的缺陷。
  - 提出了一种适用于大规模MMC的等效混合仿真模型，有效平衡了仿真精度与计算效率。
  - 设计了比例放大控制结构方法，使简化模型能够完整捕捉MMC的内部动态特性。
- **High-frequency oscillation analysis and suppression strategy of MMC-HVDC system **
  - 💡 首次将广义特征根时滞稳定性分析方法应用于MMC-HVDC高频振荡分析，并结合H∞鲁棒控制实现延时干扰的等效抑制。
  - 建立了MMC-HVDC时滞系统的高阶状态空间模型，直接应用广义特征根法求解时滞稳定裕度，避免了传统近似变换的误差与计算负担。
  - 将链路延时等效为外部干扰，基于混合灵敏度优化设计了H∞鲁棒控制器以抑制高频振荡。
- **MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析**
  - 💡 将移频理论引入含MMC的交直流电网多尺度暂态建模，并结合实时仿真平台实现了无需复杂硬件接口的电磁-机电暂态分区并行计算。
  - 提出了基于希尔伯特变换的移频建模方法，建立了MMC-MTDC系统的电磁-机电暂态移频相量模型。
  - 在RT-LAB实时仿真器上实现了电磁-机电暂态分区并行计算，克服了传统混合仿真接口复杂与数据交互误差的缺陷。
- **混合型MMC全状态高效电磁暂态仿真方法研究**
  - 💡 将闭锁等效优化与改进灵活堆排序算法相结合，构建了同时兼顾混合型MMC解锁与闭锁全状态的高效电磁暂态仿真框架。
  - 提出了一种覆盖解锁与闭锁全运行状态的混合型MMC高效电磁暂态仿真方法。
  - 基于子模块闭锁特性优化了等效电路模型，有效减少内部节点并提升闭锁模式计算效率。
- **计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法**
  - 💡 将半隐式延迟解耦法成功应用于复杂拓扑的CDSM-MMC，首次计及闭锁状态下的并联电容过渡过程，实现了恒定导纳矩阵、无积分切换的高效并行仿真。
  - 提出了计及并联电容过渡过程的CDSM半隐式延迟解耦模型，完整覆盖正常运行与闭锁状态。
  - 构建了导纳矩阵恒定的解耦电路并优化计算时序，大幅降低计算规模且天然支持并行计算。
### 2023年 (10篇)
- **An accelerated detailed equivalent model for modular multilevel converters**
  - 💡 通过仅在闭锁工况下更新导纳矩阵，消除了正常运行期间的矩阵重求逆操作，大幅提升了MMC详细等效模型的仿真计算效率。
  - 提出了一种新型加速详细等效模型策略，消除了MMC正常运行期间的导纳矩阵重求逆操作。
  - 将导纳矩阵更新限制在换流器闭锁工况下，显著降低了大规模电力系统EMT仿真的计算负担。
- **An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Nume**
  - 💡 通过混合数值积分与蛙跳策略实现MMC内外动态方程完全解耦及桥臂恒定电导，大幅突破传统EMTP型仿真的计算效率瓶颈。
  - 提出了一种基于混合数值积分的高效MMC电磁暂态仿真模型。
  - 将MMC桥臂等效为两节点诺顿电路，解耦电容与电感动态方程并采用蛙跳法计算，实现桥臂等效电导恒定。
- **Analysis and general calculation of DC fault currents in MMC-MTDC grids**
  - 💡 提出了一种适用于多端复杂MMC直流电网的短路电流通用解析计算方法，实现了故障前换流器闭锁阶段直流侧短路电流的准确快速求解。
  - 基于解析公式揭示了MMC直流侧短路故障机理及电容、电感、电阻对短路电流的影响规律。
  - 研究了多端复杂电网在不同故障条件下各换流站的放电特性。
- **Electromechanical Transient Modeling of the Low-Frequency AC System With Modular**
  - 💡 提出了面向大规模电网机电暂态仿真的M3C-LFAC系统建模与潮流计算方法，有效兼顾了仿真精度与计算效率。
  - 建立了M3C的精确数学模型及其等效电路。
  - 提出了适用于含M3C-LFAC系统的交流电网迭代潮流计算算法。
- **Equivalent model of nearest level modulation for fast electromagnetic transient **
  - 💡 通过将NLM占空比分解为稳定与波动分量并引入子模块直流电压闭环控制，构建了兼顾毫秒级精度与快速仿真速度的NLM等效模型。
  - 提出了一种用于快速电磁暂态仿真的NLM等效模型，简化了复杂调制过程的描述。
  - 将子模块占空比分解为生成桥臂电压的稳定分量与平衡直流电压的波动分量。
- **Fast electromagnetic transient simulation method for MMC-HVDC system**
  - 💡 将改进EMTP算法的复杂开关处理逻辑转化为可高度并行的细粒度运算级策略，充分释放GPU的高并发计算潜力。
  - 提出了适用于GPU架构的细粒度并行算法运算级并行策略（SIMD与共享内存）。
  - 设计了将改进EMTP算法求解过程分解为大量可并行简单运算的细粒度并行化流程。
- **Generalized Electromagnetic Transient Equivalent Modeling and Implementation of **
  - 💡 提出兼容任意单/双端口子模块的MMC电磁暂态通用建模与拓扑自动识别方法，突破了传统等效模型仅适用于单端口且依赖相同桥臂电流的局限。
  - 提出适用于任意多端口MMC拓扑的电磁暂态通用等效建模方法
  - 设计子模块拓扑自动识别算法，显著降低用户针对特定拓扑的建模工作量
- **Modeling of MMC-based STATCOM with embedded energy storage for the simulation of**
  - 💡 构建了支持多类型换流器模型与储能设备灵活组合的通用EMT建模框架，有效兼顾了仿真精度与计算效率。
  - 提出了一种灵活的建模接口方法，支持不同MMC模型与储能设备模型的便捷耦合。
  - 系统地将四种主流MMC模型应用于含储能的Delta-STATCOM电磁暂态建模。
- **多样性子模块混合型MMC统一外特性高效电磁暂态模型**
  - 💡 提出了一种无需硬编码、基于动态平均化等值的多样性子模块混合型MMC统一外特性模型，有效兼顾了直流电网系统级仿真对精度、效率与模型移植性的多重需求。
  - 提出了基于开关函数与电容动态特性的多样性子模块串联结构统一动态平均化等值方法。
  - 构建了兼顾仿真精度与效率的混合型MMC统一外特性高效电磁暂态模型。
- **多类型子模块MMC电磁暂态通用建模和实现方法**
  - 💡 突破传统单端口MMC建模限制，提出兼容任意多类型/多端口子模块的通用等效建模与拓扑自动识别方法。
  - 提出适用于任意多端口MMC拓扑的电磁暂态通用建模方法
  - 提出子模块拓扑自动识别方法以大幅降低特定拓扑建模工作量
### 2024年 (5篇)
- **An ultra-fast MMC-HVDC fault location algorithm based on transient voltage featu**
  - 💡 将暂态电压物理特征与数据驱动的回归神经网络相结合，在极短数据窗口内实现了MMC-HVDC系统的高精度、强鲁棒单端故障定位。
  - 提出仅需2.5ms故障后数据窗口的超快单端故障定位算法，满足MMC-HVDC快速保护与隔离需求。
  - 理论推导了暂态电压延迟时间、首负峰值时间及幅值与故障距离的映射关系。
- **Shooting method based modular multilevel converter initialization for electromag**
  - 💡 将打靶法引入MMC电磁暂态仿真初始化过程，实现了跨模型精度与复杂控制策略的高效稳态求解，避免了冗长的暂态等待时间。
  - 提出了一种基于打靶法的MMC初始化策略，可精确求解电路的周期稳态工作点。
  - 该策略兼容不同详细程度的MMC模型，并支持包含调制策略与电容电压平衡算法的复杂控制方案。
- **Fast Loss Evaluation Method Based on MMC Average Simulation Model; 基于MMC平均值仿真模型的**
  - 💡 将开关频率曲面、衰减函数损耗注入与平均值模型相结合，实现了MMC损耗兼顾高精度与快速计算的在线评估。
  - 构建了反映任意稳态工况下开关频率分布的开关频率曲面。
  - 提出基于衰减函数的开关损耗注入方法，有效避免注入电压尖峰并改善注入效果。
- **基于模块化多电平换流器的超级电容储能系统高效仿真方法**
  - 💡 结合桥臂戴维南等效与嵌套快速求解技术，突破了MMC-SCES大规模开关器件导致的仿真瓶颈，实现了全动态变量保留与超高速计算的统一。
  - 提出了一种基于桥臂戴维南等效电路的MMC-SCES高效电磁暂态仿真方法。
  - 运用嵌套快速求解技术进行建模，在大幅降低计算耗时的同时完整保留了换流器的所有动态变量。
- **适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型**
  - 💡 将桥臂戴维南等效与嵌套快速求解技术相结合，在保留子模块内部动态特性的前提下实现了MMC-SCES电磁暂态仿真效率的跨越式提升。
  - 提出了一种基于桥臂戴维南等效与嵌套快速求解的MMC-SCES高效电磁暂态仿真方法。
  - 该方法在大幅降低计算规模的同时完整保留了换流器及子模块的所有动态变量。
### 2025年 (3篇)
- **A computationally efficient approach for power semiconductor loss estimation of **
  - 💡 将传统器件级损耗估算扩展至桥臂级整体仿真，在保持高精度的同时大幅降低了EMT仿真的计算负担。
  - 提出了一种面向MMC的桥臂级功率半导体损耗估算方法，显著提升了EMT仿真速度。
  - 该方法能够在稳态和暂态工况下均实现高精度的损耗估算。
- **A state-space approach for accelerated simulation of modular multilevel converte**
  - 💡 将状态空间分析与子模块开关状态分组及辅助变量引入相结合，实现MMC电磁暂态仿真的高效降维与加速。
  - 提出了一种基于状态空间框架的MMC电磁暂态仿真加速方法。
  - 通过按开关状态组合对子模块分组并引入辅助状态变量，显著降低了状态矩阵维度。
- **An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating **
  - 💡 通过改进DEM等效逻辑、融合PSCAD插值机制与加速计算策略，实现了MMC-BESS在闭锁与电池断开等多工况下高精度与高效率的统一仿真。
  - 提出改进的详细等效模型，有效解决同一桥臂上下开关同时关断的仿真难题。
  - 利用辅助PSCAD开关结合内置插值算法，实现换流器闭锁状态的精确模拟。
### 2026年 (5篇)
- **Dead-time effect modeling for hybrid modular multilevel converter using twin map**
  - 💡 提出双映射法结合二极管-H桥建模，突破死区期间子模块隔离限制，实现混合MMC死区效应的高效戴维南等效建模。
  - 提出基于二极管-H桥的死区效应建模方法，有效区分受死区影响与未受影响的子模块。
  - 首创“双映射法”（电容状态映射），在死区内外动态恢复子模块电气行为，消除电路隔离问题。
- **Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulat**
  - 💡 提出融合多速率仿真、开关插值与CPU-GPU混合并行的解耦详细等效建模方法，在保障高精度的同时实现了含储能MMC电磁暂态仿真的数量级加速。
  - 提出了一种解耦详细等效模型(D-DEM)，可精确表征含储能MMC在解锁与闭锁模式下的动态特性。
  - 引入多速率仿真技术与开关插值算法，有效处理多阀组跨步长开关事件并优化计算资源分配。
- **Equivalent modeling of electromagnetic transient for MMC-HVDC based on semi-impl**
  - 💡 结合子模块多状态固有特性，采用戴维南等效与嵌套迭代策略将复杂多子模块网络降维为等效支路，实现高精度与高速度的统一。
  - 提出了一种基于戴维南等效与嵌套迭代的混合式制动电阻变换器电磁暂态等效建模方法。
  - 将含数百个子模块的复杂支路拆解为4类运行状态网络，大幅降低了系统整体节点规模。
- **Fast electromagnetic transient simulation models of modular multilevel converter**
  - 💡 提出了一种将独立子模块电磁暂态模型与通用子模块数值计算模型相结合的混合仿真架构，并衍生出数值计算平均值模型，实现了大规模MMC系统仿真精度与计算速度的有效平衡。
  - 提出了将MMC桥臂等效为自定义数值计算模块与受控电压源组合的详细数值计算模型。
  - 设计了结合独立子模块电磁暂态模型与一般子模块数值计算模型的混合仿真方法，弥补了纯数值模型难以模拟子模块内部电磁暂态过程的缺陷。
- **适用于实时仿真的MMC子模块电容电压优化均衡方法**
  - 💡 提出结合分组排序、电压重构与串并行混合触发的优化均衡策略，在保障实时仿真低时间复杂度的同时有效降低了空间复杂度并解耦了触发耗时。
  - 提出分组排序均压策略，结合组内并行全比较与组间能量平衡因子计算，有效降低了排序算法的空间复杂度。
  - 设计子模块电容电压值重构方法，解决了排序过程中含相同电压值子模块的处理难题。
## 关键发现汇总
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 基于动态相量的HVDC模型与全电磁暂态模型相比具有极高的仿真精度。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 所提接口算法在两区域交直流系统及多馈入HVDC系统的暂态稳定分析中均验证有效。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 直流动态相量模型与全电磁暂态(EMT)模型相比具有极高的仿真精度。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 所提接口算法在两区域交直流系统及多馈入直流系统的暂态稳定分析中均验证有效。
- [2010] **Efﬁcient Modeling of Modular Multilevel HVDC**: 该方法在不损失任何精度的前提下，大幅缩短了MMC系统的电磁暂态仿真时间。
- [2010] **Efﬁcient Modeling of Modular Multilevel HVDC**: 成功实现了对点对点VSC-MMC高压直流输电系统的完整仿真验证。
- [2010] **Efﬁcient Modeling of Modular Multilevel HVDC**: 时变戴维南等效模型在数学上严格等价于全节点网络模型，避免了近似接口模型带来的误差。
- [2013] **Electromechanical Transient Modeling of Modular Multilevel C**: 简化模型通过保留外环控制器与部分直流网络动态，成功实现了机电暂态仿真步长的扩大。
- [2013] **Electromechanical Transient Modeling of Modular Multilevel C**: 四端MMC-MTDC系统的PSS/E机电暂态仿真波形与PSCAD电磁暂态基准模型高度一致。
- [2013] **Electromechanical Transient Modeling of Modular Multilevel C**: 交流故障在MMC-MTDC异步互联的交流电网中能够被有效隔离，系统保持稳定。
- [2013] **Modular Multilevel Converter Models**: 改进的平均值模型与开关函数模型大幅降低了计算负担，允许采用更大的积分步长进行仿真。
- [2013] **Modular Multilevel Converter Models**: 迭代算法成功实现了对子模块闭锁状态的精确捕捉，显著扩展了简化模型的应用范围。
- [2013] **Modular Multilevel Converter Models**: 多模型对比验证表明，所提方法在计算效率与暂态响应精度之间取得了良好的平衡。
- [2014] **Ahmed 等 | A Computationally Efficient Continuous Model for t**: 该模型在保持与详细开关模型高度一致精度的同时，显著降低了计算负担与仿真时间
- [2014] **Ahmed 等 | A Computationally Efficient Continuous Model for t**: 能够准确复现MMC在阻塞状态及故障期间的电压电流动态响应
- [2014] **Ahmed 等 | A Computationally Efficient Continuous Model for t**: 验证了模型在HVDC系统级仿真中的有效性与工程实用性
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 平均值模型仅在子模块电容足够大以维持电压近似恒定时才有效。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 传统平均值模型无法准确复现直流故障下的系统暂态过程。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 改进拓扑后的平均值模型在直流故障工况下精度显著提升，且计算效率大幅提高。
- [2015] **A review of efficient modeling methods for modular multileve**: 三种微秒级电磁暂态精确模型在仿真中均能准确反映MMC动态特性，且计算效率显著优于详细开关模型。
- [2015] **A review of efficient modeling methods for modular multileve**: 电磁暂态平均简化模型在严重交直流故障暂态过程中仍保持较高的仿真精度与适用性。
- [2015] **A review of efficient modeling methods for modular multileve**: 机电暂态模型与实时仿真模型可有效支撑大规模交直流混合电网的系统级分析与硬件在环测试。
- [2015] **Comparison of Detailed Modeling Techniques for MMC Employed **: 传统详细模型因开关器件数量庞大且开关频率高，导致导纳矩阵求逆计算量极大，仿真极慢。
- [2015] **Comparison of Detailed Modeling Techniques for MMC Employed **: 详细等效模型在保持高精度的同时显著降低了计算负担，大幅缩短了仿真时间。
- [2015] **Comparison of Detailed Modeling Techniques for MMC Employed **: 改进模型在等效模型基础上进一步优化了计算效率，验证了其在典型工况下的优越性。
- [2015] **Transient Stability Analysis of MMC-HVDC System Considering **: 在GPU平台上引入稀疏矩阵技术仅能带来微小的仿真时间缩减，与CPU环境下的显著加速效果不同。
- [2015] **Transient Stability Analysis of MMC-HVDC System Considering **: 测试系统粒度过度细化（即增加互联输电线路数量）会显著拖慢GPU仿真的运行速度。
- [2015] **Transient Stability Analysis of MMC-HVDC System Considering **: 基于GPU的并行计算架构在大规模EMT仿真中相比传统CPU串行实现展现出显著的计算加速潜力。
- [2015] **模块化多电平换流器戴维南等效整体建模方法**: 所提整体模型与详细模型对比的暂稳态最大精度误差控制在2‰以内。
- [2015] **模块化多电平换流器戴维南等效整体建模方法**: 在仿真121电平MMC时，该模型的计算加速比达到2770倍以上。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Efﬁcient Modeling of Modular Multilevel HVDC]] | 2010 |
| [[dynamic-averaged-and-simplified-models-for|Dynamic Averaged and Simplified Models for]] | 2013 |
| [[dynamic-averaged-and-simplified-models-for|Dynamic Averaged and Simplified Models for]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[ahmed-等-a-computationally-efficient-continuous-model-for-the-modular-multilevel-|Ahmed 等 | A Computationally Efficient Continuous Model for t]] | 2014 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[fast-voltage-balancing-control-and-fast-19、20、21|Fast Voltage-Balancing Control and Fast]] | 2014 |
| [[fast-voltage-balancing-control-and-fast|Fast Voltage-Balancing Control and Fast Numerical Simulation]] | 2014 |
| [[the-use-of-averaged-value-model-of-modular-37|The Use of Averaged-Value Model of Modular]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[29tpwrd20162590569-2|29/TPWRD.2016.2590569]] | 2016 |
| [[current-source-modular-multilevel-converter-modeling-and-control|Current Source Modular Multilevel Converter Modeling and Con]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[a-new-topology-for-current-limiting-hvdc-circuit-breaker|A new topology for current limiting HVDC circuit breaker]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us|High-Speed EMT Modeling of MMCs With Arbitrary Multiport Sub]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-|The diode-clamped half-bridge MMC structure with internal sp]] | 2018 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified High-Speed EMT Equivalent and Implementation Method ]] | 2018 |
| [[双端口子模块mmc电磁暂态通用等效建模方法|双端口子模块MMC电磁暂态通用等效建模方法]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr|A Novel Ultra-High-Speed Traveling-Wave Protection Principle]] | 2019 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[distance-protection-scheme-for-dc-distribution-systems-based-on-the-high-frequen|Distance Protection Scheme for DC Distribution Systems Based]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2019 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2019 |
| [[mmc-upfc电磁-机电混合仿真技术研究|MMC-UPFC电磁-机电混合仿真技术研究]] | 2019 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[reduced-order-dynamic-model-of-modular|Reduced-Order Dynamic Model of Modular]] | 2019 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Spurious Power Losses in Modular Multilevel Converter Arm Eq]] | 2019 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|A Novel Linking-Domain Extraction Decomposition Method for P]] | 2020 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[characteristics-and-optimal-configuration-of-capacitive-current-limiter-consider|Characteristics and Optimal Configuration of Capacitive Curr]] | 2020 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With ]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Accelerated Electromagnetic Transient (EMT) Equivalent Model]] | 2022 |
| [[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co|An Equivalent Hybrid Model for a Large-Scale Modular Multile]] | 2022 |
| [[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co|An Equivalent Hybrid Model for a Large-Scale Modular Multile]] | 2022 |
| [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix|Analysis and Prospect of Development of China]] | 2022 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir|Characteristic Analysis of High-frequency Resonance of Flexi]] | 2022 |
| [[full-state-arm-average-value-model-for-simulation-of-active-modular-multilevel-c|Full-state Arm Average Value Model for Simulation of Active ]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb|The Averaged-value Model of a Flexible Power Electronics Bas]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报|中  国  电  机  工  程  学  报]] | 2022 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[模块化多电平换流器的高效电磁暂态仿真方法研究|模块化多电平换流器的高效电磁暂态仿真方法研究]] | 2022 |
| [[混合型mmc全状态高效电磁暂态仿真方法研究|混合型MMC全状态高效电磁暂态仿真方法研究]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[高频隔离型电力电子变压器电磁暂态加速仿真方法与展望|高频隔离型电力电子变压器电磁暂态加速仿真方法与展望]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-|Equivalent model of nearest level modulation for fast electr]] | 2023 |
| [[fast-electromagnetic-transient-simulation-of-modular-multilevel-converter-based-|Fast electromagnetic transient simulation of modular multile]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-|Generalized Electromagnetic Transient Equivalent Modeling an]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|Modeling of MMC-based STATCOM with embedded energy storage f]] | 2023 |
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|Modeling of MMC-based STATCOM with embedded energy storage f]] | 2023 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
| [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad|Real-Time Simulation of Power System Electromagnetic Transie]] | 2023 |
| [[多样性子模块混合型mmc统一外特性高效电磁暂态模型|多样性子模块混合型MMC统一外特性高效电磁暂态模型]] | 2023 |
| [[多类型子模块mmc电磁暂态通用建模和实现方法|多类型子模块MMC电磁暂态通用建模和实现方法]] | 2023 |
| [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu|An ultra-fast MMC-HVDC fault location algorithm based on tra]] | 2024 |
| [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu|An ultra-fast MMC-HVDC fault location algorithm based on tra]] | 2024 |
| [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu|An ultra-fast MMC-HVDC fault location algorithm based on tra]] | 2024 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[基于mmc平均值仿真模型的损耗快速评估方法|Fast Loss Evaluation Method Based on MMC Average Simulation ]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[a-computationally-efficient-approach-for-power-semiconductor-loss-estimation-of-|A computationally efficient approach for power semiconductor]] | 2025 |
| [[a-computationally-efficient-approach-for-power-semiconductor-loss-estimation-of-|A computationally efficient approach for power semiconductor]] | 2025 |
| [[a-computationally-efficient-approach-for-power-semiconductor-loss-estimation-of-|A computationally efficient approach for power semiconductor]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[acceleration-strategies-for-emt-simulation-of-hvdc-systems|Acceleration strategies for EMT Simulation of HVDC systems]] | 2025 |
| [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-|An EMT based dynamic frequency scanning tool for stability a]] | 2025 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|An Electromagnetic Transient Simulation Model of MMC-BESS fo]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Splitting State-Space Method for Converter-Integrated Power ]] | 2025 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit|Z-Tool: Frequency-domain characterization of EMT models for ]] | 2025 |
| [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map|Dead-time effect modeling for hybrid modular multilevel conv]] | 2026 |
| [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map|Dead-time effect modeling for hybrid modular multilevel conv]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[fast-electromagnetic-transient-simulation-models-of-modular-multilevel-converter|Fast electromagnetic transient simulation models of modular ]] | 2026 |
| [[fast-electromagnetic-transient-simulation-models-of-modular-multilevel-converter|Fast electromagnetic transient simulation models of modular ]] | 2026 |
| [[适用于实时仿真的mmc子模块电容电压优化均衡方法|适用于实时仿真的MMC子模块电容电压优化均衡方法]] | 2026 |
## 深度增强内容

 基于提供的论文数据，以下是针对 **模块化多电平换流器 (MMC)** 模型的深度增强内容：

---

## 1. 各类模型数学描述

### 1.1 详细开关模型 (Detailed Switching Model, DSM)

详细模型对每个子模块 (SM) 的 IGBT/二极管开关器件进行微观建模，通常采用**二值电阻模型**或**理想开关模型**。

**单个子模块动态方程**（以半桥为例）：
$$
\begin{aligned}
C_{SM} \frac{dv_{C}}{dt} &= S \cdot i_{arm} \\
v_{SM} &= S \cdot v_{C} + (1-S) \cdot v_{C} \cdot \frac{R_{off}}{R_{on}+R_{off}} \approx S \cdot v_{C}
\end{aligned}
$$

其中 $S \in \{0,1\}$ 为开关函数，$v_C$ 为电容电压，$R_{on}$ 和 $R_{off}$ 分别为导通和关断电阻。

**桥臂电流方程**：
$$
L_{arm} \frac{di_{arm}}{dt} + R_{arm}i_{arm} = v_{dc}/2 - v_{arm} - v_{ac}
$$

**特点**：需采用 $1\sim5\,\mu\text{s}$ 级步长，计算复杂度 $O(N^3)$，适用于器件级损耗分析与控制验证。

### 1.2 平均值模型 (Average-Value Model, AVM)

AVM 忽略开关纹波，用受控电压源表征桥臂整体行为。

**桥臂平均电压**：
$$
\bar{v}_{arm} = n_{on} \cdot \bar{v}_{C}^{arm}
$$

其中 $n_{on} \in [0,N]$ 为投入子模块数，$\bar{v}_{C}^{arm}$ 为桥臂平均电容电压。

**环流动力学**（考虑二倍频分量）：
$$
L_{arm} \frac{di_{circ}}{dt} + R_{arm}i_{circ} = \frac{V_{dc}}{2} - \frac{\bar{v}_{u} + \bar{v}_{l}}{2}
$$

**增强型平均值模型 (EAVM)** 引入桥臂电流初始化补偿，闭锁工况下：
$$
i_{arm}(t^+) = i_{arm}(t^-) \cdot \frac{L_{arm}}{L_{arm} + L_{eq}}
$$

**特点**：步长可放宽至 $10\sim100\,\mu\text{s}$，计算效率提升 $20\sim100$ 倍，适用于系统级暂态分析。

### 1.3 详细等效模型 (Detailed Equivalent Model, DEM) - 戴维南等效

基于**梯形积分法**的戴维南等效电路，将子模块群聚合成时变等效电路。

**等效电阻与电压**（梯形法）：
$$
\begin{aligned}
R_{eq} &= \frac{2C_{SM}R_{on} + \Delta t}{2C_{SM} + \Delta t/R_{on}} \approx \frac{\Delta t}{2C_{SM}} \\
v_{th} &= \frac{2C_{SM} - \Delta t/R_{on}}{2C_{SM} + \Delta t/R_{on}} \cdot v_{C}(t-\Delta t) + R_{eq} \cdot i_{arm}(t)
\end{aligned}
$$

**桥臂聚合**：
将 $N$ 个子模块等效为单一戴维南电路：
$$
R_{arm}^{eq} = \sum_{j=1}^{N} R_{eq,j}, \quad v_{arm}^{th} = \sum_{j=1}^{N} v_{th,j}
$$

**加速策略**（恒定导纳矩阵）：
正常运行时导纳矩阵 $G_{net}$ 保持恒定，仅在闭锁/解锁时更新：
$$
G_{net} \cdot V_{node} = I_{inj}
$$

**特点**：精度与 DSM 一致（误差 $<0.1\%$），计算速度提升 $30\sim60$ 倍（FBSM 拓扑提升更显著）。

### 1.4 动态相量模型 (Dynamic Phasor Model)

适用于频域分析和机电暂态混合仿真，保留关键谐波分量。

**10阶动态相量模型**（考虑基频和二倍频）：
$$
\begin{aligned}
\langle v \rangle_0 &= f(\langle i \rangle_0, \langle i \rangle_2, \langle v_C \rangle_0, \langle v_C \rangle_2) \\
\langle v \rangle_2 &= g(\langle i \rangle_0, \langle i \rangle_2, \langle v_C \rangle_2)
\end{aligned}
$$

其中 $\langle \cdot \rangle_k$ 表示第 $k$ 次谐波的动态相量。

**降阶模型**（2阶）：
基于奇异摄动法，仅保留慢变模态（实部 $>-5\,\text{s}^{-1}$）：
$$
\dot{x}_{slow} = A_{reduced} x_{slow} + B_{reduced} u
$$

**特点**：支持 $10\,\text{ms}$ 级大步长，适用于大规模 MMC-MTDC 机电暂态仿真，效率提升约 $200$ 倍。

### 1.5 移位相量模型 (Shifted Phasor Model, SPM)

针对实时仿真的宽频带模型：
$$
v_{arm}(t) = \Re\left\{ \sum_{k=-M}^{M} \langle v \rangle_k(t) \cdot e^{jk\omega_0 t} \right\}
$$

计算复杂度与子模块数 $N$ 解耦，实现 $O(1)$ 准常数复杂度。

---

## 2. 仿真参数参考表

| 模型类型 | 子模块数/电平数 | 仿真步长 | 加速比 (vs DSM) | 典型误差 | 适用场景 | 代表文献 |
|---------|----------------|----------|----------------|---------|---------|---------|
| **详细开关模型 (DSM)** | 20-400 | $1\sim5\,\mu\text{s}$ | 1 (基准) | $<0.1\%$ | 器件级损耗、阀控验证 | 2019, Real-time MPSoC |
| **详细等效模型 (DEM)** | 120-400 | $10\,\mu\text{s}$ | $30\times$(HBSM)<br>$60\times$(FBSM) | $<0.1\%$ | 直流故障分析、保护设计 | 2023, Accelerated DEM |
| **增强平均值 (EAVM)** | 401 电平 | $20\sim50\,\mu\text{s}$ | $20\sim50\times$ | $<0.5\%$ (稳态)<br>$<1\%$ (暂态) | 闭锁工况仿真 | 2018, Enhanced AVM |
| **自适应多模型** | 401 电平 | 可变 ($10\sim50\,\mu\text{s}$) | $10\sim40\times$ | 切换冲击 $<0.1\%$ | 全工况混合仿真 | 2020, Adaptive MMC |
| **移位相量 (SPM)** | 20-200 | $10\,\mu\text{s}$ | $O(1)$ 复杂度 | $<0.5\%$ | 实时仿真、宽频分析 | 2018, Shifted Phasor |
| **动态相量 (10阶)** | 大规模 | $1\sim10\,\text{ms}$ | $200\times$ | $<4\%$ (低频段) | 机电暂态、低频振荡 | 2019, Reduced-Order |
| **机电暂态模型** | 多端 MTDC | $10\,\text{ms}$ | $200\times$ | $<2\%$ ($di/dt$) | 大规模电网稳定性 | 2019, Electro-mechanical |

**关键参数设置建议**：
- **电容值**：$C_{SM} = 6\text{--}15\,\text{mF}$（取决于功率等级和电压纹波要求）
- **桥臂电感**：$L_{arm} = 50\text{--}100\,\text{mH}$，等效电阻 $R_{arm} = 0.1\text{--}0.5\,\Omega$
- **全桥比例** $\eta = N_{FB}/(N_{HB}+N_{FB})$：通常 $0.2\text{--}0.5$ 用于直流故障自清除

---

## 3. 模型选择指南

根据研究目标和计算资源约束，推荐以下选择策略：

### 3.1 按研究目标选择

| 研究目标 | 推荐模型 | 步长建议 | 关键考量 |
|---------|---------|---------|---------|
| **阀基控制器 (VBC) 设计** | DEM 或 自适应模型 | $10\,\mu\text{s}$ | 保留子模块均压逻辑，支持电容电压排序算法验证 |
| **直流故障穿越分析** | EAVM 或 DEM | $10\sim20\,\mu\text{s}$ | 必须准确模拟闭锁瞬间电流连续性（EAVM 初始化补偿） |
| **系统级控制策略** | AVM 或 动态相量 | $50\,\mu\text{s}\sim1\,\text{ms}$ | 忽略开关细节，关注功率/能量动态 |
| **大规模 MTDC 电网** | 机电暂态模型 | $10\,\text{ms}$ | 二阶直流侧等效，预设故障信息避免拓扑重构 |
| **实时硬件在环 (HIL)** | SPM 或 固定导纳模型 | $1\sim5\,\mu\text{s}$ | FPGA 并行架构，恒定导纳避免矩阵重构 |
| **损耗与热评估** | DEM + 损耗计算融合 | $10\,\mu\text{s}$ | 基于桥臂电流解析计算器件损耗，避免纳秒级仿真 |

### 3.2 按系统规模选择

- **小规模 (N < 50)**：可采用 DSM 或 DEM，重点关注控制细节
- **中等规模 (50 ≤ N ≤ 200)**：推荐 DEM 或 AEM，平衡精度与效率
- **大规模 (N > 200 或多端系统)**：必须采用 AVM、自适应模型或机电暂态模型
- **超大规模 (电网级)**：采用多速率协同仿真，MMC 用 EMT 模型，交流网用暂态稳定模型

### 3.3 特殊场景注意事项

1. **虚假功率损耗问题**：使用经典 AEM 时，确保与主网络方程联立求解，或采用可变电阻模型消除单步延迟导致的 $\Delta P(t) = P_{arm}(t) - P_{Ctot}(t)$ 误差。

2. **高频振荡分析**：时滞系统状态空间模型 + 广义特征根法，避免 Pade 近似，直接求解时滞稳定裕度 $\tau_{wd}$。

3. **电热耦合仿真**：采用 MPSoC 架构，步长 $1\sim5\,\mu\text{s}$，结温计算误差 $<1\sim2\%$，迭代收敛需 $2\sim3$ 次。

---

## 4. 前沿研究方向

基于论文分析，MMC 建模领域的前沿方向包括：

### 4.1 多物理场耦合建模
- **电热联合仿真**：融合器件级电热模型与系统级 EMT 仿真，结温计算精度达 $0.1^\circ\text{C}$ 分辨率，支持故障容忍拓扑分析。
- **电磁-机械-热耦合**：考虑阀厅结构、散热系统与电气控制的综合仿真。

### 4.2 智能自适应建模
- **模型自动切换**：基于暂态严重程度自动在 DEM/AVM/机电模型间切换，切换冲击 $<0.1\%$，实现全工况高效仿真。
- **AI 辅助降阶**：利用深度学习提取 MMC 关键动态特征，构建数据驱动的黑箱降阶模型。

### 4.3 异构并行加速
- **时间并行算法 (MGRIT)**：突破空间并行瓶颈，在 5 核并行下实现 $3.47\times$ 加速，适用于含 $1000+$ 子模块的臂内并行。
- **FPGA 硬件加速**：基于 SPM 或固定导纳模型，实现 $O(1)$ 复杂度，支持 400 子模块级实时仿真。

### 4.4 虚假损耗消除与精度提升
- **即时联立求解**：消除 AEM 中的单步延迟，实现与详细模型一致的功率守恒。
- **虚拟二极管方法**：针对闭锁工况，通过 $R_{on}/R_{off}$ 逻辑判断（mΩ 级 vs MΩ 级），精确模拟二极管续流。

### 4.5 混合多速率仿真框架
- **EMT-TS 混合接口**：基于 Bergeron 传输线模型实现零延迟接口，10 秒仿真加速比达 $12.8\times$。
- **移频相量法**：保留除基频外所有频率信息，适用于 VSC-HVDC 多尺度暂态分析。

### 4.6 新型拓扑专用模型
- **混合桥臂 (CH-MMC)**：针对半桥/全桥混合拓扑，构建阀段级等效模型，支持 $\eta$ 参数化配置。
- **储能型 MMC**：含嵌入式 DC-DC 变换器的多阀臂平均值模型，电容需求降低 $50\%$ 以上。

---

**注**：以上模型数学描述中的符号约定遵循电力电子惯例，$u$/$l$ 分别表示上/下桥臂，$N$ 为每桥臂子模块总数，$\Delta t$ 为仿真步长，$C_{SM}$ 为子模块电容。实际应用时请根据具体仿真平台（PSCAD/EMTDC、MATLAB/Simulink、RTDS 等）调整数值积分方法（梯形法/后退欧拉法）。
