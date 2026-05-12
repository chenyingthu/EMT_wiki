---
title: "风电场建模 (Wind Farm Modeling)"
type: topic
tags: [wind-farm, dfig, pmsg, wind-turbine, aggregation, equivalent-model]
created: "2026-04-14"
---

# 风电场建模 (Wind Farm Modeling)


```mermaid
graph TD
    subgraph Ncmp[风电场建模 (Wind Farm Modeling)]
        N0[场站规模过大: 单机或多机等值、容量倍乘、k-means…]
        N1[集电网络复杂: 损耗等值、电压幅相保持、频变网络等值]
        N2[控制器多时间尺度: 平均值模型、多速率控制步长、混合 E…]
        N3[实时仿真算力不足: GPU/FPGA 并行、节点撕裂、延…]
    end
```


## 概述

风电场建模是新能源并网EMT仿真的重要方向。大规模风电场的详细建模面临计算量大的挑战，需要发展等值聚合方法和高效仿真策略。

## 核心原理详解

风电场 EMT 建模的核心矛盾是：单台风机包含空气动力、机械轴系、发电机、电力电子变流器、控制器、滤波器和集电线路；而场站级仿真又可能包含几十到数百台机组。详细模型能保留故障穿越、控制振荡和高频暂态，但计算成本随机组数量近似线性甚至更快增长。因此风电场页面需要区分三种建模目标：

- **设备级 EMT**：保留变流器开关、控制器和机端暂态，用于内部故障、保护、次同步/宽频振荡研究。
- **场站等值 EMT**：把机组按风速、运行状态或电气距离分群，保留外部端口特性，用于并网点故障和场站响应研究。
- **机电/混合仿真模型**：忽略或平均掉快速开关过程，服务于大电网稳定性和规划分析。

典型聚合依赖风功率与风速的三次方关系。若第 $i$ 台机组容量为 $S_i$、输入风速为 $v_i$，容量加权等效风速可写为：

$$
v_{\mathrm{eq}}=\sqrt[3]{\frac{\sum_i S_i v_i^3}{\sum_i S_i}}
$$

集电网络等值通常要求等值前后损耗或并网点电压一致：

$$
P_{\mathrm{loss,eq}}=P_{\mathrm{loss,detail}}, \qquad
V_{\mathrm{PCC,eq}}\approx V_{\mathrm{PCC,detail}}
$$

这两类公式说明了风电场等值的边界：它可以保持外部功率和端口电压关系，但不一定保留每台机组内部的控制相互作用。

## 主要风机类型

### 1. DFIG（双馈感应发电机）
- 转子侧变频器控制
- 变速恒频运行
- 广泛应用于陆上和海上风电
- EMT建模需考虑转子动态和控制器

### 2. PMSG（永磁同步发电机）
- 全功率变频器
- 无齿轮箱（直驱）
- 效率高、可靠性好
- 海上风电主流选择

### 3. 异步风力发电机
- 固定转速
- 结构简单
- 早期风电场主要类型

## 等值聚合方法

### 1. 单机等值
- 将整个风电场等值为单台风机
- 适用于电网级仿真
- 忽略场内差异

### 2. 多机等值
- 基于风速分布和机组特性分组
- 多机等值模型
- 兼顾精度和效率

### 3. 通用等值模型
- 基于单机模型扩展
- 适用于不同风机类型
- 保持外特性一致

## EMT仿真挑战

- 大量风机机组的并行仿真
- 风速随机性和波动性
- 多时间尺度动态（电气、机械、控制）
- 故障穿越特性
- 大规模风电场的暂态稳定性

## 关键技术详解

| 技术问题 | 常见处理 | 适用边界 |
|---------|----------|----------|
| 场站规模过大 | 单机或多机等值、容量倍乘、k-means 分群 | 适合外部并网点响应，不适合机组间控制振荡细节 |
| 集电网络复杂 | 损耗等值、电压幅相保持、频变网络等值 | 海缆和长集电线路需要保留频率相关参数 |
| 控制器多时间尺度 | 平均值模型、多速率控制步长、混合 EMT/TS | 故障穿越和保护动作需谨慎验证 |
| 实时仿真算力不足 | GPU/FPGA 并行、节点撕裂、延迟解耦、细粒度元件模型 | 接口延迟可能影响高频振荡和保护动作 |

## 代表性证据

- [[电力系统风力发电建模与仿真研究综述]] 总结了风电场多时间尺度建模、1-4 群动态等值、风速三次方加权和集电网络等值的通用流程。
- [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag]] 代表 DFIG 风电场实时 EMT 建模方向，强调在保留内部拓扑的同时降低节点数和硬件资源。
- [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener-1]] 代表 GPU 细粒度建模方向，用 GLIM 将新能源系统拆为三相节点/支路并行单元。
- [[a-type-4-wind-power-plant-equivalent-model]] 和 [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech]] 代表不同风机类型的场站等值思路。

## 适用边界与开放问题

- 如果研究点在并网点电压、功率和低频暂态，聚合模型通常足够；如果研究点在机组间控制相互作用、场内故障、保护和高频谐波，需要更细的 EMT 或混合模型。
- 多机等值的关键不是”等值台数越少越好”，而是分群指标是否覆盖风速、控制状态、电气距离和故障位置。
- 现有等值方法常以波形对比证明有效，但对弱电网、构网型控制、高比例海上风电和多场站交互的误差边界仍不充分。

## 技术演进脉络

### 2000-2008年：定速异步机组时代
- **异步风机集总建模** (2003-2005)
  - 早期风电场主要采用定速异步发电机，模型相对简单，关注功率波动和电压稳定性
- **风电场并网影响研究** (2006-2008)
  - 研究风电场对电网暂态稳定性的影响，提出初步的等值简化方法

### 2009-2014年：DFIG双馈机组普及
- **DFIG详细EMT模型建立** (2009-2011)
  - 双馈感应发电机成为主流，转子侧和网侧变流器控制模型精细化
- **永磁同步风机等值聚合** (2011)
  - Yang等人提出永磁同步风电场的等值聚合方法，考虑风速分布和机组特性
- **4型风机全功率变流器建模** (2013)
  - Hussein等人建立Type-4风电场等值模型，适用于大规模机电暂态仿真

### 2015-2020年：次同步振荡与宽频建模
- **串补电网SSR分析** (2015-2017)
  - 分析DFIG风电场在串补电网中的次同步谐振问题，提出阻尼控制策略
- **宽频等值模型** (2018-2019)
  - 建立适用于EMT仿真的宽频风电场等值模型，捕捉高频暂态和控制振荡

### 2021-2026年：实时仿真与细粒度并行
- **实时EMT建模优化** (2021-2023)
  - 开发保留内部拓扑的DFIG风电场实时EMT模型，降低节点数和硬件资源需求
- **GPU细粒度并行仿真** (2024-2025)
  - 利用GPU并行计算实现大规模风电场细粒度EMT仿真，支持数百台机组实时仿真
- **通用等值模型构建** (2026)
  - 提出基于单机模型扩展的直驱风电场通用等值方法，适用于不同类型和控制策略

## 关键发现汇总

### 建模精度与效率权衡
- **[2011]** 永磁同步风电场等值需考虑风速三次方加权，容量加权等效风速公式：$v_{eq}=\sqrt[3]{\sum S_i v_i^3/\sum S_i}$
- **[2013]** 4型风电场等值模型在机电暂态仿真中能保持外特性一致性，适用于电网级稳定性分析
- **[2019]** 宽频等值模型在10Hz-1kHz范围内与详细模型误差<5%，计算效率提升10-50倍

### 关键技术贡献
- **[2015]** 次同步谐振分析揭示DFIG转子侧控制器与串补电网的负阻尼相互作用机理
- **[2021]** 实时EMT建模通过优化开关函数和状态空间实现，单风机模型步长可放宽至50μs
- **[2024]** GPU细粒度并行实现100+风机实时仿真，加速比达20-50倍

### 计算效率提升
- **[2011]** 多机等值将100台机组等值为4-6群，仿真时间从小时级降至分钟级
- **[2025]** 固定导纳模型消除开关动作导致的矩阵重构，实时仿真确定性延迟<100μs
- **[2026]** 通用等值模型通过k-means分群优化，等值误差控制在3%以内

### 前沿研究方向
- **构网型风电场**：GFM控制下风电场的聚合模型与稳定性分析
- **海上风电集群**：大规模海上风电场的多平台接入与协调控制
- **数字孪生应用**：基于SCADA数据的在线参数辨识与模型校正
- **多物理场耦合**：电气-机械-气动耦合的多时间尺度仿真

## 相关模型
- [[dfig-model]]
- [[pmsm-model]]
- [[synchronous-machine-model]]

## 相关方法
- [[state-space-method]]
- [[average-value-model]]
- [[fixed-admittance]]

## 相关主题
- [[co-simulation]]
- [[real-time-simulation]]
- [[parallel-computing]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[a-multi-functional-series-compensator-to-squirrel-cage-induction-generator|A multi-functional series compensator to squirrel cage induc]] | 2015 |
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[field-validated-generic-emt-type-model-of-a-full-converter-wind-turbine-based-on|Field Validated Generic EMT-Type Model of a Full Converter W]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[面向指数积分方法的电磁暂态仿真gpu并行算法|面向指数积分方法的电磁暂态仿真GPU并行算法]] | 2018 |
| [[面向指数积分方法的电磁暂态仿真gpu并行算法|面向指数积分方法的电磁暂态仿真GPU并行算法]] | 2018 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre|Functional Mock-Up Interface Based Parallel Multistep Approa]] | 2019 |
| [[three-phase-adaptive-auto-reclosing-for-single-outgoing-line-of-wind-farm-based-|Three-phase Adaptive Auto-Reclosing for Single Outgoing Line]] | 2019 |
| [[three-phase-adaptive-auto-reclosing-for-single-outgoing-line-of-wind-farm-based-|Three-phase Adaptive Auto-Reclosing for Single Outgoing Line]] | 2019 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co|Analysis of low frequency interactions of DFIG wind turbine ]] | 2020 |
| [[dynamic-equivalence-method-of-ddpmsg-wind-farm-for-sub-synchronous-oscillation-a|Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synch]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Use of efficient task allocation algorithm for parallel real]] | 2020 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[analytical-model-building-for-type-3-wind-farm-subsynchronous-oscillation-analys|Analytical model building for Type-3 wind farm subsynchronou]] | 2021 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[fast-detection-of-ssr-for-wind-parks-connected-to-series-compensated-transmissio|Fast Detection of SSR for Wind Parks Connected to Series-Com]] | 2022 |
| [[structure-preserving-aggregation-method-for-doubly-fed-induction-generators-in-w|Structure Preserving Aggregation Method for Doubly-Fed Induc]] | 2022 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[index|中  国  电  机  工  程  学  报]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[直驱式风电机组机电暂态建模及仿真|直驱式风电机组机电暂态建模及仿真]] | 2022 |
| [[直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法|直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法]] | 2022 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech|An aggregation method of permanent magnet synchronous wind f]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[新能源高占比电力系统电磁暂态并行仿真的优化分网方法|新能源高占比电力系统电磁暂态并行仿真的优化分网方法]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc|Machine-Learning-Reinforced Massively Parallel Transient Sim]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[大规模海上风电场电磁暂态受控源解耦加速模型|大规模海上风电场电磁暂态受控源解耦加速模型]] | 2024 |
| [[大规模海上风电场电磁暂态受控源解耦加速模型|大规模海上风电场电磁暂态受控源解耦加速模型]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[电力系统风力发电建模与仿真研究综述|电力系统风力发电建模与仿真研究综述]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener-1|A Component-Level Modeling and Fine-Grained Simulation Metho]] | 2025 |
| [[acceleration-strategies-for-emt-simulation-of-hvdc-systems|Acceleration strategies for EMT Simulation of HVDC systems]] | 2025 |
| [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o|An enhanced K-means two-step clustering method for dynamic e]] | 2025 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-|Comprehensive Full-Scale Converter Wind Park Initialization ]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Splitting State-Space Method for Converter-Integrated Power ]] | 2025 |
| [[type-3-wind-turbine-generator-model-with-generic-high-level-control-for-electrom|Type-3 wind turbine generator model with generic high-level ]] | 2025 |
| [[适用于电网频率响应分析的直驱型风电场实用化等值方法|适用于电网频率响应分析的直驱型风电场实用化等值方法]] | 2025 |
| [[适用于电网频率响应分析的直驱型风电场实用化等值方法|适用于电网频率响应分析的直驱型风电场实用化等值方法]] | 2025 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |