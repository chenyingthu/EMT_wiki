---
title: "VSC-HVDC"
type: topic
tags: [vsc-hvdc, hvdc, flexible-dc-transmission, voltage-source-converter]
created: "2026-04-14"
---

# VSC-HVDC（柔性直流输电）

## 定义与概述

VSC-HVDC（Voltage Source Converter High Voltage Direct Current）是基于电压源换流器的高压直流输电技术。它通过自关断电力电子器件和快速控制系统实现有功、无功和直流电压控制，常用于新能源并网、海上风电送出、孤岛供电、城市电网接入和多端直流系统。

在 EMT wiki 中，VSC-HVDC 是一个系统级主题：它把 [[models/vsc-model|VSC 模型]]、[[models/mmc-model|MMC 模型]]、直流电缆、控制器、保护和混合仿真接口连接在一起。建模目标通常不是单个器件，而是换流站、直流线路、电网交互和控制保护动作的综合暂态。

## 作用机制

VSC-HVDC 的 EMT 模型通常由以下部分组成：

$$
P_{\mathrm{ac}}\approx v_d i_d+v_q i_q,\qquad
Q_{\mathrm{ac}}\approx v_q i_d-v_d i_q
$$

在同步旋转坐标系中，VSC 控制通常通过 $i_d/i_q$ 或等价变量调节有功、无功和直流电压。EMT 模型需要说明这些控制方程如何与换流器桥臂、PLL、直流网络和保护逻辑耦合。

- **换流器主电路**：两电平、三电平或 MMC 拓扑；工程级 VSC-HVDC 多采用 MMC 或其变体。
- **交流侧接口**：变压器、滤波器、相锁环、交流电网等值和保护测量。
- **直流侧网络**：直流电缆、架空线、直流母线、电抗器、直流断路器或耗能装置。
- **控制系统**：内环电流控制、外环功率/电压控制、直流电压控制、环流控制、子模块电容电压均衡和故障控制。
- **建模层级**：详细开关模型保留开关事件；[[methods/average-value-model|平均值模型]] 牺牲高频开关细节换取系统级效率；混合模型在不同阶段或区域切换粒度。
- **求解加速**：[[methods/fixed-admittance|恒导纳模型]]、[[methods/state-space-method|状态空间法]]、多速率仿真和并行计算常用于缓解大规模 MMC-HVDC 的计算压力。

## 适用边界

- 详细 EMT 模型适合直流故障、闭锁/解锁、保护动作、子模块电容电压、谐波和开关暂态分析。
- 平均值或动态相量模型适合系统级控制、稳定性扫描、机电-电磁混合仿真和大规模多端系统研究。
- 对直流故障穿越、换流器闭锁、直流断路器动作或电缆行波保护，不能只依赖平滑平均模型，应使用可覆盖故障电流路径和保护时标的模型。
- 多端 VSC-HVDC 需要明确直流电压控制分配、站间通信假设和故障隔离策略；这些控制边界会改变 EMT 结果。
- VSC-HVDC 与交流弱电网、风电场或电缆网络耦合时，应同时检查控制带宽、频率相关线路模型和接口延迟。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 | 降低 VSC-HVDC EMT 模型计算强度。 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid]] | 2014 | 评估 MMC 平均值模型在 VSC-HVDC 电网中的适用性。 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems]] | 2015 | VSC-HVDC 的机电-电磁混合仿真接口。 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes]] | 2015 | 比较 VSC-HVDC 中 MMC 详细建模技术。 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含 VSC-HVDC 交直流系统多尺度暂态建模与仿真研究]] | 2017 | 多尺度暂态建模与仿真。 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVDC system]] | 2022 | VSC-HVDC 系统 EMT 建模。 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 | 用动态相量模拟 VSC-HVDC。 |

## 相关页面

- [[models/vsc-model|VSC 模型]]
- [[models/mmc-model|MMC 模型]]
- [[models/lcc-model|LCC 模型]]
- [[models/cable-model|电缆模型]]
- [[methods/average-value-model|平均值模型]]
- [[methods/fixed-admittance|恒导纳模型]]
- [[methods/state-space-method|状态空间法]]
- [[topics/dynamic-phasor|动态相量]]
- [[topics/co-simulation|协同仿真]]
- [[topics/real-time-simulation|实时仿真]]
