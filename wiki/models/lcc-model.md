---
title: "线路换相换流器 (LCC)"
type: model
tags: [lcc, hvdc, thyristor, line-commutated, converter]
created: "2026-04-14"
---

# 线路换相换流器 (LCC)

## 概述

线路换相换流器（Line-Commutated Converter, LCC）是传统高压直流输电（HVDC）的核心设备。与电压源换流器（VSC）不同，LCC使用晶闸管作为开关器件，依赖交流电网电压实现换相。

## 主要特点

- 晶闸管开关器件，不可控关断
- 依赖交流系统提供换相电压
- 换相失败是主要故障模式
- 只能向有源网络输电
- 大容量、远距离输电经济性好

## EMT建模方法

### 1. 详细换相模型
- 每个晶闸管单独建模
- 精确表征换相过程
- 适用于换相失败分析

### 2. 平均值模型
- 换相周期平均化
- 忽略开关细节
- 适用于系统级暂态仿真

### 3. 开关函数模型
- 使用开关函数表征换相
- 兼顾精度和效率
- 适用于混合仿真

## 主要故障模式

### 换相失败
- 交流电压跌落导致换相不成功
- 直流电压崩溃
- 无功功率突增
- 是LCC-HVDC最严重的故障

### 直流侧故障
- 直流线路短路
- 直流电流激增
- 需要快速保护动作

## 相关方法
- [[average-value-model]]
- [[nodal-analysis]]

## 相关主题
- [[co-simulation]]
- [[vsc-hvdc]]
- [[mmc-model]]


## 论文方法分析
> 基于 4 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 多区域戴维南等效(MATE) | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 多速率联合仿真 | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| MATE传输线模型(MATE-TLM) | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 虚拟阻抗控制策略 | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 理想开关表示法 | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 拓扑分解法（主网络与阀级辅助网络） | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 结构稳定求解算法 | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 自适应时间步长控制策略 | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 参数化平均值建模(PAVM) | 1 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 正负序分量分析 | 1 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 平均值建模扩展 | 1 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 参数化平均值建模（PAVM） | 1 | Average-Value Modeling of Line-Commutated Inverter Systems With Commut |
| 电磁暂态（EMT）仿真 | 1 | Average-Value Modeling of Line-Commutated Inverter Systems With Commut |
| 自动故障检测技术 | 1 | Average-Value Modeling of Line-Commutated Inverter Systems With Commut |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| LCC高压直流输电系统 | 1 |
| 交直流混合电网 | 1 |
| 传输线 | 1 |
| LCC-HVDC换流器 | 1 |
| TBSD（基于拓扑的简化动态模型） | 1 |
| 线换相AC-DC变换器(LCC/LCR) | 1 |
| 详细开关模型 | 1 |
| 电网换相逆变器（LCI） | 1 |
| LCC-HVDC输电系统 | 1 |
| 电力电子开关器件 | 1 |
### 验证方式分布
- **仿真**: 1 篇
- **仿真对比**: 1 篇
- **实验与仿真对比**: 1 篇
- **仿真/对比**: 1 篇
## 技术演进脉络
### 2019年 (1篇)
- **A multi-area Thevenin equivalent based multi-rate co-simulation for control desi**
  - 💡 将MATE多速率联合仿真技术与虚拟阻抗控制策略深度融合，为实用LCC HVDC系统提供了兼顾高精度、高效率仿真与换相失败抑制的一体化解决方案。
  - 提出基于MATE的多速率联合仿真框架，解决传统模型无法兼顾精度与效率的问题。
  - 构建MATE传输线模型并引入加速技术，显著提升大规模电网电磁暂态仿真效率。
### 2021年 (1篇)
- **Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne**
  - 💡 将参数化平均值建模扩展至交流不平衡工况，通过显式解析正负序谐波与直流纹波关系，实现高精度与高计算效率的统一。
  - 将参数化平均值建模(PAVM)方法扩展至交流电网不平衡工况下的LCC仿真。
  - 建立了交流侧正负序谐波与直流侧纹波相对于电网不平衡度的解析关系。
### 2022年 (1篇)
- **Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail**
  - 💡 首次将参数化平均值建模与自动故障检测相结合，为含换相失败故障的LCC-HVDC系统提供了一种高精度、低计算成本的EMT仿真方法。
  - 将参数化平均值建模（PAVM）方法从交流-直流整流器成功扩展至直流-交流逆变器系统。
  - 在平均值模型框架内首次引入并准确表征了开关器件的换相失败故障动态。
### 2025年 (1篇)
- **A topology-based simplified dynamic model and solving algorithm for LCC-HVDC con**
  - 💡 提出融合拓扑分解、定维矩阵求解与自适应步长的TBSD模型，有效解决了LCC-HVDC换相失败仿真中计算效率与阀级动态精度难以兼顾的难题。
  - 提出基于拓扑的简化动态（TBSD）模型，通过理想开关保留晶闸管离散开关特性。
  - 开发结构稳定求解算法，在不同开关拓扑下保持矩阵维度一致以提升求解稳定性。
## 关键发现汇总
- [2019] **A multi-area Thevenin equivalent based multi-rate co-simulat**: 所提MATE多速率联合仿真方法在保持电磁暂态精度的同时大幅降低了计算耗时。
- [2019] **A multi-area Thevenin equivalent based multi-rate co-simulat**: 虚拟阻抗控制策略成功减少了换相失败发生概率并缩短了直流电压与功率的恢复时间。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 所提PAVM在不平衡工况下能高精度重构交流侧与直流侧电压/电流波形。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 相比传统详细开关模型，新模型的计算速度显著提升，大幅降低仿真耗时。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 所提PAVM能够准确预测换相失败事件，并重构出与详细开关模型高度一致的交直流侧波形。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 相比传统详细开关模型，该平均值模型在系统级多场景仿真中实现了更高的计算效率。
- [2025] **A topology-based simplified dynamic model and solving algori**: TBSD模型能够精确复现LCC-HVDC换流器的换相失败动态过程。
- [2025] **A topology-based simplified dynamic model and solving algori**: 相比传统高精度EMT模型，该模型在维持同等精度的前提下显著提升了计算效率。
- [2025] **A topology-based simplified dynamic model and solving algori**: 自适应步长策略有效平衡了仿真速度与暂态波形跟踪精度。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne]] | 2021 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail]] | 2022 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulation for control desi]] | 2019 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algorithm for LCC-HVDC con]] | 2025 |
