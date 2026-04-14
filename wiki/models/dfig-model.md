---
title: "双馈感应发电机 (DFIG)"
type: model
tags: [dfig, wind-turbine, induction-machine, renewable]
created: "2026-04-13"
---

# 双馈感应发电机 (DFIG)

## 概述

双馈感应发电机（Doubly-Fed Induction Generator, DFIG）是风力发电系统中广泛应用的发电机类型。其定子直接并网，转子通过背靠背换流器励磁，可实现变速恒频运行。

## 结构特点

- 绕线式感应电机
- 定子直接连接电网
- 转子通过部分容量换流器励磁
- 变速运行范围宽

## EMT建模方法

### 详细模型
- 完整的d-q轴模型
- 包含转子侧和网侧换流器
- 控制系统详细建模
- 适用于单机暂态分析

### 等值模型
- 风电场等值聚合
- 保留动态特性
- 大规模系统简化
- 机电-电磁混合仿真适用

### 高效实时模型
- 固定导纳建模
- FPGA实现
- 多台风电机组并行

## 控制特性

- 最大功率跟踪（MPPT）
- 有功/无功解耦控制
- 低电压穿越（LVRT）
- 转子侧换流器控制
- 网侧换流器控制

## 暂态特性

- 电网故障响应
-  Crowbar保护动作
- 直流母线电压波动
- 次同步振荡风险

## 相关方法
- [[state-space-method]]
- [[fixed-admittance]]

## 相关主题
- [[wind-farm-modeling]]
- [[real-time-simulation]]


## 论文方法分析
> 基于 18 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 增强型K-means两步聚类法 | 1 | An enhanced K-means two-step clustering method for dynamic equivalent  |
| 概率初始中心选择 | 1 | An enhanced K-means two-step clustering method for dynamic equivalent  |
| KD树加速搜索 | 1 | An enhanced K-means two-step clustering method for dynamic equivalent  |
| Davies-Bouldin指数(DBI)自动定簇 | 1 | An enhanced K-means two-step clustering method for dynamic equivalent  |
| 动态等值建模 | 1 | An enhanced K-means two-step clustering method for dynamic equivalent  |
| 状态空间法 | 1 | Analysis of low frequency interactions of DFIG wind turbine systems in |
| 参与因子分析 | 1 | Analysis of low frequency interactions of DFIG wind turbine systems in |
| 灵敏度分析 | 1 | Analysis of low frequency interactions of DFIG wind turbine systems in |
| 模态分析 | 1 | Analysis of low frequency interactions of DFIG wind turbine systems in |
| SSR风险筛选技术 | 1 | Analysis of low frequency interactions of DFIG wind turbine systems in |
| 电磁暂态(EMT)仿真 | 1 | Analysis of low frequency interactions of DFIG wind turbine systems in |
| 细粒度网络解耦/划分方法 | 1 | Efficient electromagnetic transient simulation for DFIG-based wind far |
| 多线程并行计算 | 1 | Efficient electromagnetic transient simulation for DFIG-based wind far |
| 导纳矩阵降维技术 | 1 | Efficient electromagnetic transient simulation for DFIG-based wind far |
| 电磁暂态-机电暂态混合仿真 | 1 | Electromechanical transient-electromagnetic transient hybrid simulatio |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 双馈感应发电机(DFIG) | 3 |
| 双馈感应发电机(DFIG)风电场 | 2 |
| 逆变器并网资源(IBR) | 2 |
| 动态等值模型 | 1 |
| 详细电磁暂态模型 | 1 |
| 串联补偿输电系统 | 1 |
| 含内外环控制与机械部分的DFIG解析模型 | 1 |
| 新型基准测试网络 | 1 |
| 大型风电场 | 1 |
| 风电场核心电气设备 | 1 |
| 双馈风力发电机组(DFIG) | 1 |
| IEEE 14节点测试系统 | 1 |
| 风电场等值模型 | 1 |
| 跟网型逆变器发电机 | 1 |
| 光伏系统基准模型 | 1 |
### 验证方式分布
- **仿真/对比**: 5 篇
- **仿真**: 4 篇
- **仿真对比**: 2 篇
- **仿真与对比**: 2 篇
- **实验**: 1 篇
- **仿真验证**: 1 篇
- **仿真对比（与Matlab/Simulink离线仿真结果验证）**: 1 篇
- **仿真验证与对比分析**: 1 篇
- **仿真验证与对比**: 1 篇
## 技术演进脉络
### 2017年 (1篇)
- **基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法**
  - 💡 将电流轨迹相似度引入电磁暂态过程，突破传统机电暂态分群局限，实现DFIG机群快速暂态过程的精准动态聚合。
  - 提出基于电流轨迹相似度的电磁暂态同调分群新指标
  - 构建了适用于DFIG机群动态聚合的等效模型
### 2020年 (1篇)
- **Analysis of low frequency interactions of DFIG wind turbine systems in series co**
  - 💡 构建了结合参与因子与灵敏度分析的DFIG低频交互解析评估框架，并证实了简化筛选技术在串联补偿电网SSR风险评估中的工程适用性。
  - 提出了一种基于实际参数的新型基准测试网络，用于深入研究风电与串联补偿系统间的低频交互现象。
  - 建立了涵盖内外环控制及机械动态的通用DFIG风电场解析模型，并引入参与因子分析精准定位关键振荡状态。
### 2021年 (1篇)
- **Mitigation of Subsynchronous Interactions in Hybrid AC/DC Grid With Renewable En**
  - 💡 将基于FPGA硬件并行架构的超实时EMT-动态协同仿真技术应用于含可再生能源的混合交直流电网，实现了次同步相互作用抑制策略的超前快速生成。
  - 提出了一种基于FPGA的超实时仿真平台，用于快速评估和抑制混合交直流电网中的次同步相互作用。
  - 设计了EMT与动态仿真并发运行的协同架构，利用FPGA硬件并行性大幅提升计算速度。
### 2022年 (2篇)
- **Electromechanical transient-electromagnetic transient hybrid simulation of doubl**
  - 💡 在国产自主电力系统分析软件PSD-PSModel中实现了双馈风机的电磁暂态-机电暂态混合仿真，填补了国内相关详细建模与仿真技术的空白。
  - 基于双馈风机运行原理构建了详细的电磁暂态数学模型框架。
  - 在自主开发的PSD-PSModel软件平台上实现了电磁暂态与机电暂态的混合仿真功能。
- **Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in W**
  - 💡 提出了一种基于状态变量递归组合与降阶的结构保持聚合方法，在维持单DFIG模型结构的同时，精确等效多机系统的稳态与主导暂态特性。
  - 提出了一种结构保持的DFIG聚合方法，将多台DFIG等效为单台模型。
  - 聚合模型能够综合考虑各机组不同的转速、参数及连接阻抗差异。
### 2023年 (4篇)
- **Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulat**
  - 💡 提出了一种基于免费ATP平台的跟网型IBR等效时域模型，在准确复现故障动态特性的同时大幅降低了模型复杂度与仿真计算耗时。
  - 提出了一种适用于ATP/ATPDraw环境的跟网型逆变器等效时域模型。
  - 该模型结构更简单，计算耗时显著低于完整基准模型。
- **Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doub**
  - 💡 提出基于虚拟电容等效的定转子解耦方法与并行计算架构，结合FPGA硬件加速实现双馈风机数字孪生的超实时仿真。
  - 提出面向异步机定转子T型等效电路解耦的虚拟电容等效法。
  - 设计了DFIG内部各组件的并行计算算法与FPGA流水线优化架构。
- **Improved methods for optimization of power systems with renewable generation usi**
  - 💡 将参数降维筛选、算法混合与并行计算深度融合，突破了传统EMT仿真优化中计算成本高、易陷局部最优及高维变量难处理的瓶颈。
  - 提出两种参数筛选方法，有效剔除对最优解影响不显著的冗余参数，降低优化维度。
  - 探索多种优化算法的混合策略，结合全局与局部搜索优势以提升寻优精度并避免陷入局部最优。
- **Parallelization of EMT simulations for integration of inverter-based resources**
  - 💡 将FMI标准与TLM网络解耦技术深度融合，构建了支持多速率、无近似且自动初始化的EMT多实例并行协同仿真框架。
  - 提出了一种基于FMI标准的EMT协同仿真工具，实现多个EMT求解器实例的并行计算。
  - 利用传输线传播延迟实现网络无近似解耦，支持子网络独立求解与多速率时间步长设置。
### 2024年 (5篇)
- **Efficient electromagnetic transient simulation for DFIG-based wind farms using f**
  - 💡 将设备级细粒度网络解耦与多线程并行计算深度融合，在保留风机内部状态的同时大幅压缩导纳矩阵规模，实现大规模DFIG风电场高效高精度EMT仿真。
  - 提出了一种针对DFIG风电场的设备级细粒度网络解耦算法，有效降低了系统导纳矩阵的维度。
  - 构建了集成多线程并行计算的可扩展仿真框架，进一步提升了大规模风电场的仿真效率。
- **Inverter-Based Resources Model Verification Using Electromagnetic Transient Play**
  - 💡 将EMT回放仿真技术系统化应用于IBR模型验证，构建了符合电网新规的标准化基准测试框架
  - 提出了一套完整的IBR电磁暂态模型验证解决方案与标准化工作流程
  - 开发了配套的回放仿真工具以支持系统运营商高效开展模型审查
- **Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Sc**
  - 💡 将数据驱动的机器学习建模与面向数据的ECS架构相结合，实现了超大规模可再生能源系统的高精度、超高速并行电磁暂态仿真。
  - 提出了一种融合机器学习与ECS架构的大规模RES详细电磁暂态仿真方法
  - 设计了基于CPU-GPU异构平台的超大规模实体并行计算框架
- **基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模**
  - 💡 首次结合奇异摄动与瓦西里耶娃理论构建直驱风电全环节等效惯量模型，并给出了降阶误差与时间尺度的严格理论判据。
  - 建立了涵盖机械、控制、电气及测控全环节的直驱风电机组频率响应全阶模型。
  - 基于奇异摄动理论推导了考虑不同时间尺度动态特性的等效惯量降阶模型。
- **新能源电力系统细粒度并行与多速率电磁暂态仿真**
  - 💡 将集成电路设计中的延迟插入法引入电力系统，结合GPU实现细粒度并行与多速率解耦仿真，突破了传统节点分析法在大规模强耦合系统中的效率瓶颈。
  - 提出了基于延迟插入法的新能源电力系统细粒度建模方法，支持受控源接入。
  - 结合GPU硬件优势实现了算法的细粒度并行求解，显著提升大规模系统仿真效率。
### 2025年 (4篇)
- **An enhanced K-means two-step clustering method for dynamic equivalent modeling o**
  - 💡 将LVRT特性与增强型两步K-means聚类算法深度融合，实现DFIG风电场动态等值模型的自动化、高精度与高效构建。
  - 提出基于有功功率与LVRT响应的两步聚类策略，有效区分风机的聚类特性。
  - 改进K-means算法，通过概率初始化、KD树加速与DBI指数实现聚类过程自动化与高效化。
- **Fine-grained hardware resource optimization and design for FPGA-based real-time **
  - 💡 提出面向FPGA的细粒度硬件资源优化与自动HDL生成方法，在满足微秒级实时仿真步长的同时大幅降低大规模新能源控制系统解算的硬件资源开销。
  - 构建了算术运算级的硬件资源需求模型，综合考虑最小求解时间与硬件资源约束。
  - 提出了一种自动硬件描述语言生成方法，可快速生成REG控制系统的功能硬件模块。
- **Huang 等 | A Heterogeneous Multiscale Method for Efficient Simulation of Power Sy**
  - 💡 提出结合自动降阶宏观模型与半解析变步长机制的异构多尺度仿真方法，有效解决高比例IBR电力系统多时间尺度刚性方程仿真效率低下的难题。
  - 提出了一种异构多尺度方法，通过微观EMT模型与自动降阶宏观模型的交替计算，实现多时间尺度高效仿真。
  - 引入半解析解法构建自适应变步长机制，在保证快慢动态精度的同时大幅降低计算负担。
- **Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromag**
  - 💡 将延迟解耦技术与多级嵌套快速同步求解算法相结合，有效克服了大规模风电场电磁暂态仿真中的“维数灾难”问题。
  - 提出结合延迟解耦与M-NFSS的建模方法，在保留风电场内部细节的同时有效降低电路节点数量。
  - 构建了适用于大规模DFIG风电场的高效率实时电磁暂态仿真模型，突破了传统方法的硬件资源限制。
## 关键发现汇总
- [2017] **基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法**: 分群结果与详细模型动态响应误差小于3%
- [2017] **基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法**: 等效模型使电磁暂态仿真耗时降低约65%
- [2017] **基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法**: 在电压跌落与短路故障下均保持较高的同调识别准确率
- [2020] **Analysis of low frequency interactions of DFIG wind turbine **: 参与因子分析成功识别出主导临界模态的关键系统状态，为制定针对性抑制策略提供了理论依据。
- [2020] **Analysis of low frequency interactions of DFIG wind turbine **: 灵敏度分析结果表明，通过优化调整DFIG控制参数能够完全避免系统发生低频谐振。
- [2020] **Analysis of low frequency interactions of DFIG wind turbine **: 早期SSR风险筛选技术的评估结果与详细模态分析高度吻合，验证了其在工程规划阶段的实用性与可靠性。
- [2021] **Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr**: FTRT平台实现了远超实时速度的计算加速，显著缩短了复杂电网动态过程的仿真时间。
- [2021] **Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr**: 协同仿真准确捕捉了串联补偿与汽轮发电机间的电气-机械相互作用及次同步振荡特征。
- [2021] **Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr**: 平台能够在扰动发生后提前生成最优潮流调整方案，有效抑制次同步相互作用并维持系统稳定。
- [2022] **Electromechanical transient-electromagnetic transient hybrid**: 所建立的DFIG电磁暂态模型在混合仿真平台中运行稳定且计算结果准确。
- [2022] **Electromechanical transient-electromagnetic transient hybrid**: 仿真有效揭示了双馈风机在电网暂态过程中的控制策略响应特性与动态行为。
- [2022] **Structure Preserving Aggregation Method for Doubly-Fed Induc**: 聚合模型能够精确匹配未降阶系统的稳态响应特性。
- [2022] **Structure Preserving Aggregation Method for Doubly-Fed Induc**: 聚合模型能够准确复现未降阶系统的主导暂态动态响应。
- [2022] **Structure Preserving Aggregation Method for Doubly-Fed Induc**: 模型阶数显著降低，大幅提升了大规模风电场的建模与仿真计算效率。
- [2023] **Equivalent grid-following inverter-based generator model for**: 故障工况下模型输出与基准模型的平均误差约为2.33%。
- [2023] **Equivalent grid-following inverter-based generator model for**: 相比完整基准模型，仿真执行时间减少了约70%。
- [2023] **Faster-than-real-time Simulation of Stator-rotor Decoupling **: 所提方法降低DFIG异步机求解模块所需FPGA资源约77%。
- [2023] **Faster-than-real-time Simulation of Stator-rotor Decoupling **: 基于FPGA的DFIG-IP在500 MHz时钟频率下超实时加速度比可达27.8。
- [2023] **Faster-than-real-time Simulation of Stator-rotor Decoupling **: 单个DFIG-IP占用ZCU106资源不超过20%且满足并网系统仿真精度与速度要求。
- [2023] **Improved methods for optimization of power systems with rene**: 参数筛选方法大幅减少了待优化变量数量，有效降低了高维优化问题的计算复杂度。
- [2023] **Improved methods for optimization of power systems with rene**: 混合优化算法与并行计算相结合，在保证全局寻优能力的同时显著缩短了仿真优化总耗时。
- [2023] **Improved methods for optimization of power systems with rene**: 多复杂度案例测试表明，所提方法在处理含高比例可再生能源的电力系统优化时具有高效性与鲁棒性。
- [2023] **Parallelization of EMT simulations for integration of invert**: 实现了大规模含高比例IBR电网的EMT仿真加速计算，且未引入数值近似误差。
- [2023] **Parallelization of EMT simulations for integration of invert**: 多速率解耦方案允许不同子网络采用独立时间步长，有效平衡了计算效率与精度。
- [2023] **Parallelization of EMT simulations for integration of invert**: 基于FMI与信号量的协同架构成功实现了多核并行任务调度与历史数据的高效同步。
- [2024] **Efficient electromagnetic transient simulation for DFIG-base**: 在50台风机规模的风电场仿真中，该方法实现了两个数量级的计算加速。
- [2024] **Efficient electromagnetic transient simulation for DFIG-base**: 与Matlab/Simulink详细模型对比，最大相对误差仅为1.68%，验证了方法的高精度。
- [2024] **Inverter-Based Resources Model Verification Using Electromag**: 通过回放仿真技术有效验证了IBR EMT模型在复杂暂态工况下的动态响应准确性
- [2024] **Inverter-Based Resources Model Verification Using Electromag**: 所提工具与流程显著提升了ISO/TSO对并网逆变器模型的审查效率与标准化水平
- [2024] **Inverter-Based Resources Model Verification Using Electromag**: 验证方案成功满足IEEE 2800及NERC相关标准对模型精度的合规性要求
## 来源论文

| 论文 | 年份 |
|------|------|
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co|Analysis of low frequency interactions of DFIG wind turbine ]] | 2020 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl|Electromechanical transient-electromagnetic transient hybrid]] | 2022 |
| [[structure-preserving-aggregation-method-for-doubly-fed-induction-generators-in-w|Structure Preserving Aggregation Method for Doubly-Fed Induc]] | 2022 |
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati|Equivalent grid-following inverter-based generator model for]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi|Improved methods for optimization of power systems with rene]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[inverter-based-resources-model-verification-using-electromagnetic-transient-play|Inverter-Based Resources Model Verification Using Electromag]] | 2024 |
| [[machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc|Machine-Learning-Reinforced Massively Parallel Transient Sim]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o|An enhanced K-means two-step clustering method for dynamic e]] | 2025 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Fine-grained hardware resource optimization and design for F]] | 2025 |
| [[huang-等-a-heterogeneous-multiscale-method-for-efficient-simulation-of-power-syst|Huang 等 | A Heterogeneous Multiscale Method for Efficient Si]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |