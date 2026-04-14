---
title: "平均值模型"
type: model
tags: []
created: "2026-04-13"
---

# 平均值模型

## 论文方法分析
> 基于 13 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 平均值建模(AVM) | 3 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| 参数化平均值建模(PAVM) | 3 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 节点分析法 | 2 | Dynamic Average-Value Modeling of |
| 平均值建模 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 阻塞模块等效法 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 解析损耗计算 | 1 | A Universal Blocking-Module-Based Average Value Model of Modular Multi |
| 增强型平均值模型（Enhanced AVM） | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 桥臂电流初始化方法 | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 控制信号驱动建模 | 1 | An Enhanced Average Value Model of Modular Multilevel Converter for Ac |
| 平均值建模 (Average-Value Modeling) | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 解析表征法 | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 等效电路简化 | 1 | Average-Value Model for a Modular Multilevel Converter With Embedded S |
| 直接接口技术(Direct Interfacing) | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| 节点导纳矩阵联立求解 | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
| EMTP型离散化方法 | 1 | Average-Value Model for Voltage-Source Converters With Direct Interfac |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 平均值模型(AVM) | 3 |
| MMC-HVDC系统 | 2 |
| 模块化多电平换流器（MMC） | 2 |
| 电压源换流器(VSC) | 2 |
| 详细开关模型 | 2 |
| 参数化平均值模型(PAVM) | 2 |
| 模块化多电平换流器(MMC) | 2 |
| MMC | 1 |
| 多类型子模块 | 1 |
| 闭锁模块（Blocking Module） | 1 |
| 带嵌入式储能的模块化多电平换流器 (MMC-ES) | 1 |
| 子模块级电池储能系统 | 1 |
| 详细电磁暂态(DEM)模型 | 1 |
| 交直流电力系统 | 1 |
| 电网换相AC-DC换流器(LCC/LCR) | 1 |
### 验证方式分布
- **仿真/对比**: 4 篇
- **仿真**: 3 篇
- **仿真与实验对比验证**: 1 篇
- **实验与仿真对比验证**: 1 篇
- **仿真对比验证**: 1 篇
- **仿真与对比**: 1 篇
- **仿真对比**: 1 篇
- **仿真与实验**: 1 篇
## 技术演进脉络
### 2014年 (2篇)
- **Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC G**
  - 💡 通过改进传统平均值模型的拓扑结构，解决了其在直流故障暂态下仿真精度不足的问题，兼顾了计算效率与准确性。
  - 评估了平均值模型在VSC-HVDC电网中MMC应用的适用性与局限性。
  - 指出传统平均值模型无法准确模拟直流故障下的暂态过程。
- **Dynamic Average-Value Modeling of**
  - 💡 将数值提取的非线性代数函数方法应用于12脉冲换流器的动态平均值建模，实现了跨仿真平台的高效精确等效。
  - 开发了适用于状态变量和节点分析两类仿真平台的CIGRE HVDC基准系统动态平均值模型。
  - 通过数值提取技术构建了12脉冲换流器的非线性代数函数，有效规避了详细开关级建模的复杂性。
### 2016年 (1篇)
- **Improved Accuracy Average Value Models of Modular Multilevel Converters**
  - 💡 通过多项改进策略优化传统MMC平均值模型，在保持高计算效率的同时显著提升仿真精度并支持直流故障等复杂工况分析。
  - 针对现有MMC平均值模型的局限性提出了多项改进策略。
  - 开发了一种精度显著提升的增强型MMC平均值模型。
### 2018年 (1篇)
- **An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Rep**
  - 💡 提出带桥臂电流初始化机制的增强型平均值模型，在免除调制控制器依赖的同时，实现了对MMC闭锁工况及暂态初始条件的精确高效表征。
  - 提出一种增强型平均值模型，能够精确表征MMC的闭锁运行工况。
  - 引入桥臂电流初始化方法，有效补偿了传统控制信号型AVM的初始条件误差。
### 2019年 (1篇)
- **A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Conv**
  - 💡 通过通用阻塞模块架构首次在同一平均值模型中统一处理多子模块拓扑及闭锁/解锁工况，并集成解析损耗计算功能。
  - 提出了一种通用的基于阻塞模块的平均值模型，可兼容多种子模块拓扑结构。
  - 实现了换流器在闭锁与解锁两种运行模式下的高精度动态仿真。
### 2020年 (1篇)
- **Combining Detailed Equivalent Model With Switching-Function-Based Average Value **
  - 💡 提出了一种将详细等效模型与开关函数平均值模型相结合的通用框架，实现了仿真过程中高精度与高速度模型的平滑动态切换。
  - 提出了一种融合DEM与SFB-AVM的通用桥臂等效电路建模框架。
  - 实现了动态仿真过程中两种模型之间的平滑无缝切换。
### 2021年 (2篇)
- **Average-Value Model for a Modular Multilevel Converter With Embedded Storage**
  - 💡 提出了一种兼顾计算效率与解析能力的MMC-ES平均值模型，突破了传统数值模型难以直接用于控制器调参、小信号分析及元件参数设计的局限。
  - 提出了一种计算高效的MMC-ES平均值模型，显著降低了系统级仿真的计算负担。
  - 实现了对环流和子模块电容电压波动的解析表征，支持含或不含环流抑制控制的分析。
- **Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne**
  - 💡 首次将参数化平均值建模扩展至交流不平衡工况，通过显式建立正负序谐波与直流纹波对电网不平衡度的依赖关系，实现了LCC的高效高精度仿真。
  - 将参数化平均值建模(PAVM)方法扩展至交流电网不平衡工况下的电网换相换流器仿真。
  - 建立了交流侧正负序谐波与直流侧纹波相对于电网不平衡度的解析数学关系。
### 2022年 (2篇)
- **Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail**
  - 💡 首次将考虑内部故障的PAVM方法应用于电网换相逆变器，结合自动故障检测技术，实现了换相失败工况下仿真精度与计算效率的有效平衡。
  - 将参数化平均值建模(PAVM)方法从交流-直流整流器成功扩展至直流-交流逆变器系统。
  - 在平均值模型框架内准确表征了开关器件的换相失败故障动态。
- **Direct Interfacing of Parametric Average-Value Models of AC&#x2013;DC Converters**
  - 💡 通过将PAVM接口方程线性化并直接嵌入节点导纳矩阵，彻底消除了传统EMTP仿真中因间接接口引入的一步时间延迟，实现了大时间步长下的高精度稳定仿真。
  - 提出了一种针对电网换相整流器(LCR)参数化平均值模型(PAVM)的直接接口方法。
  - 通过线性化PAVM接口方程并将其子矩阵和历史项直接嵌入网络节点方程，消除了传统间接接口所需的一步时间延迟。
### 2023年 (1篇)
- **Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMT**
  - 💡 通过将VSC平均值模型转化为节点导纳形式并与系统网络方程联立求解，实现了无延迟的直接接口，突破了传统AVM在大步长仿真中的数值稳定性瓶颈。
  - 提出了一种适用于VSC的直接接口平均值模型，彻底消除了传统间接接口的一步时间延迟。
  - 将AVM方程重构为节点形式，使其能够与外部网络节点方程同步联立求解，从而支持大仿真步长。
### 2024年 (1篇)
- **Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal**
  - 💡 提出基于扩展等效导纳矩阵的直接接口平均值模型，彻底消除传统受控源接口在节点法EMT仿真中的计算延迟，实现大时间步长下的高精度稳定仿真。
  - 将直接接口平均值模型（DI-AVM）的数学公式推广至任意接口节点配置。
  - 构建了假设所有节点浮空的VSC扩展等效导纳矩阵。
### 2026年 (1篇)
- **Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transie**
  - 💡 在时间域内将平均价值模型作为主干并融合谐波分量计算，实现了兼顾高计算效率与精确谐波表征的系统级变流器建模。
  - 提出了一种谐波保留平均价值模型(HP-AVM)，将AVM计算与谐波分量计算集成于统一仿真框架中。
  - 在保持系统级仿真高计算效率的同时，实现了与开关函数模型(SFM)相当的精度。
## 关键发现汇总
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 仅当子模块电容足够大以维持电压近似恒定时，平均值模型才有效。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 改进拓扑后的平均值模型能准确捕捉直流故障暂态，克服了传统模型的缺陷。
- [2014] **Average-Value Models for Modular Multilevel Converters Opera**: 相比详细电磁暂态模型，改进模型在保证关键暂态精度的同时实现了显著的计算加速。
- [2014] **Dynamic Average-Value Modeling of**: 动态平均值模型的大信号时域暂态响应与详细开关级仿真结果高度一致。
- [2014] **Dynamic Average-Value Modeling of**: 相比详细模型，该平均值模型大幅减少了计算时间，具备显著的系统级仿真计算优势。
- [2016] **Improved Accuracy Average Value Models of Modular Multilevel**: 改进后的AVM在仿真精度上显著优于传统平均值模型。
- [2016] **Improved Accuracy Average Value Models of Modular Multilevel**: 新模型能够准确模拟直流故障等暂态过程，验证了其更广泛的适用性。
- [2016] **Improved Accuracy Average Value Models of Modular Multilevel**: 模型在提升精度的同时保持了较高的计算效率，适用于大规模系统仿真。
- [2018] **An Enhanced Average Value Model of Modular Multilevel Conver**: 增强型AVM在显著提升仿真效率的同时，能精确复现桥臂电压纹波和环流动态。
- [2018] **An Enhanced Average Value Model of Modular Multilevel Conver**: 所提初始化方法有效消除了传统AVM在暂态和闭锁过程中的初始条件不匹配问题。
- [2018] **An Enhanced Average Value Model of Modular Multilevel Conver**: 模型无需子模块开关函数即可准确模拟换流器闭锁期间的交直流侧电气行为。
- [2019] **A Universal Blocking-Module-Based Average Value Model of Mod**: 所提模型在41电平MMC-HVDC系统中的仿真精度与详细开关模型及现有先进AVM高度一致。
- [2019] **A Universal Blocking-Module-Based Average Value Model of Mod**: 模型在保持高精度的同时显著提升了电磁暂态仿真效率，适用于大规模系统分析。
- [2019] **A Universal Blocking-Module-Based Average Value Model of Mod**: 解析损耗计算方法能够准确反映不同子模块拓扑下的半导体损耗特性。
- [2020] **Combining Detailed Equivalent Model With Switching-Function-**: SFB-AVM的仿真速度显著优于DEM，且子模块数量越多加速效果越显著。
- [2020] **Combining Detailed Equivalent Model With Switching-Function-**: 所提框架支持在仿真运行中按需切换模型，且切换过程平滑无暂态扰动。
- [2020] **Combining Detailed Equivalent Model With Switching-Function-**: SFB-AVM能够准确反映不同子模块类型MMC的动态电气特性。
- [2021] **Average-Value Model for a Modular Multilevel Converter With **: 所提平均值模型在大幅降低计算复杂度的同时，保持了与详细EMT模型高度一致的动态响应精度。
- [2021] **Average-Value Model for a Modular Multilevel Converter With **: 模型能够准确解析计算环流分量与子模块电容电压纹波，为控制器调参和小信号分析提供理论支撑。
- [2021] **Average-Value Model for a Modular Multilevel Converter With **: 基于该模型的元件 sizing 分析结果与实验数据吻合，验证了其在不同运行工况下的设计指导价值。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 新PAVM能够高精度重构交流电网不平衡工况下的交直流侧电压与电流波形。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 所提模型的计算效率显著高于传统详细开关模型，有效缓解了系统级EMT仿真的计算瓶颈。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 所提PAVM能够准确预测换相失败事件并重构出与详细开关模型高度一致的电气波形。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 该模型通过忽略高频开关事件显著降低了计算负担，大幅提升了系统级仿真的运行速度。
- [2022] **Direct Interfacing of Parametric Average-Value Models of AC&**: 仿真结果表明该方法在较大时间步长下仍能保持极高的仿真精度。
- [2022] **Direct Interfacing of Parametric Average-Value Models of AC&**: 有效消除了传统间接接口导致的数值不稳定问题，显著提升了EMTP类求解器的计算效率与稳定性。
- [2023] **Average-Value Model for Voltage-Source Converters With Direc**: 新模型成功消除了传统接口的一步延迟，允许在EMTP类程序中使用较大的仿真时间步长。
- [2023] **Average-Value Model for Voltage-Source Converters With Direc**: 在较大时间步长条件下，该模型的仿真精度和数值稳定性显著优于现有的VSC平均值模型。
- [2023] **Average-Value Model for Voltage-Source Converters With Direc**: 所提模型在VSC的整流和逆变两种运行模式下均保持有效。
- [2024] **Numerically Efficient Average-Value Model for Voltage-Source**: 在大仿真时间步长下，该模型的数值精度显著优于传统受控源AVM。
