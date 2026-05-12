---
title: "线路换相换流器 (LCC)"
type: model
tags: [lcc, hvdc, thyristor, line-commutated, converter]
created: "2026-04-14"
updated: "2026-05-12"
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

## 定义与边界

LCC 模型描述基于晶闸管、依赖交流系统换相的高压直流换流器。它与 [[vsc-model|VSC 模型]] 的边界在于 LCC 需要较强交流电压支撑，控制变量主要围绕触发角、熄弧角和直流电流；VSC 则通过自换相器件独立控制有功/无功。用于 EMT 时，LCC 页面应说明换相过程、阀组等值、控制保护接口和交流系统强度，而不是只给出平均功率方程。

该模型适合常规 HVDC、换相失败、交直流故障和多馈入相互作用研究。若研究对象是高频开关谐波、构网控制或 MMC 内部子模块暂态，应转向 [[vsc-model]]、[[mmc-model]] 或 [[average-value-model|平均值模型]]。

## 量化性能边界

**He 2025 TBSD — 拓扑简化动态LCC模型（Topology-Based Simplified Dynamic Model）**:
- 采用两端口戴维南等效（6脉动桥：3×3导纳矩阵；12脉动桥：5×5矩阵），矩阵维度常数不随换相状态变化
- 单次求解计算量较详细开关模型降低约 **70%**，相对误差 < **0.5%**
- 可精确表征换相失败（导通角异常、熄弧角 γ < γ_min）、交流单相/三相故障等暂态过程
- 换相失败检测准确率优于传统准稳态模型，尤其在弱交流系统（SCR < 2）下
- 数据缺口：原文仅报告单次求解加速比，未给出完整EMT仿真时步下的总体加速比

**Hong 2022 PAVM — 参数化平均值LCC模型（Parametric Average-Value Model）**:
- 基于换相角 μ、熄弧角 γ 和直流电流 I_dc 的参数化查找表，波形重构误差 < **1%**
- 仿真速度较详细开关模型提升 **数个数量级**（原文未报告精确加速比数值）
- 支持交流不对称故障工况（负序分量影响下的换相过程建模）
- 验证平台：PSCAD/EMTDC，故障波形与详细模型高度一致
- 数据缺口：PAVM在弱交流系统（SCR < 2）和极低短路比工况下的精度边界未系统报告

**MATE多速率协同仿真（2019）— 交直流分区多速率接口**:
- 交直流系统分区：AC子网大步长 500 μs，DC子网小步长 50 μs，步长比 10:1
- 基于传输线解耦的MATE（Multi-Area Thévenin Equivalent）接口
- 加速比约 **150–160x**（vs 统一50 μs步长），NRMSE < **7%**
- 验证平台：OPAL-RT实时仿真器，含CIGRE LCC-HVDC基准模型
- 数据缺口：多速率接口在换相失败暂态（μs级快速变化）下的精度未单独评估

**Yao 2023 — 多馈入LCC-HVDC谐波交互模型**:
- 多馈入LCC系统谐波交互导致熄弧角降低 **2.8°–4.5°**（vs 独立LCC工况）
- 谐波畸变率 THD > 5% 时换相失败风险显著增加，模型相对误差 < **3.5%**
- 考虑背景谐波的换相电压畸变修正：基于迭代谐波注入的换相过程重算
- 数据缺口：验证仅基于双馈入LCC系统（2-infeed），多馈入（>3）工况缺乏定量数据

**换相失败关键参数**：
- 最小熄弧角裕度 γ_min = **7°–9°**（典型工程设计值）
- 换相持续时间约 **1.0 ms**（对应工频 **17°** 电角度）
- 交流电压跌落 > 10% 时换相失败概率显著增加（依赖具体系统参数）

**数据缺口声明**：LCC模型的量化性能数据主要来自离线EMT仿真平台（PSCAD/EMTDC），实时仿真平台（RTDS/OPAL-RT）下的加速比数据仅MATE多速率方法报告。不同LCC模型（TBSD/PAVM/开关函数）间的横向对比缺乏统一基准模型和标准化测试工况。多馈入LCC系统（≥3馈入）的换相失败概率和模型精度边界尚缺乏充分验证。

## 相关方法
- [[average-value-model|平均值模型]] - LCC平均值等效
- [[nodal-analysis|节点分析法]] - 换流器节点方程
- [[state-space-method|状态空间法]] - LCC状态空间建模
- [[numerical-integration|数值积分]] - 换相过程离散化

## 相关模型
- [[vsc-model|VSC模型]] - VSC与LCC对比
- [[mmc-model|MMC模型]] - MMC-HVDC对比
- [[transformer-model|换流变压器]] - LCC换流变
- [[fdne-model|频变网络等值(FDNE)]] - 外部网络等值

## 相关主题
- [[co-simulation]]
- [[vsc-hvdc]]
- [[mmc-model]]
- [[network-equivalent]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Networks]] | 2022 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algorithm for LCC-HVDC converters]] | 2025 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulation for control design]] | 2019 |
| [[a-multi-infeed-hvdc-harmonic-interaction-model-for-commutation-failure-analysis|A multi-infeed HVDC harmonic interaction model for commutation failure analysis]] | 2023 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*