---
title: "风电场建模 (Wind Farm Modeling)"
type: topic
tags: [wind-farm, dfig, pmsg, wind-turbine, aggregation, equivalent-model]
created: "2026-04-14"
---

# 风电场建模 (Wind Farm Modeling)

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
- 多机等值的关键不是“等值台数越少越好”，而是分群指标是否覆盖风速、控制状态、电气距离和故障位置。
- 现有等值方法常以波形对比证明有效，但对弱电网、构网型控制、高比例海上风电和多场站交互的误差边界仍不充分。

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
| [[a-type-4-wind-power-plant-equivalent-model|Hussein 2013 (4型风电等值)]] | 2013 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech|Yang 2011 (永磁风机群等值聚合)]] | 2011 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[基于单机模型扩展的直驱风电场通用等值模型构建方法|基于单机模型扩展的直驱风电场通用等值模型构建方法]] | 2026 |
