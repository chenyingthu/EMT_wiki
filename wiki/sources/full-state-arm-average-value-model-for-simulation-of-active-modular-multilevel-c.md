---
title: "Full-state Arm Average Value Model for Simulation of Active Modular Multilevel Converter; [有源型模块化多电平"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Tang 等 - 2022 - Full-state Arm Average Value Model for Simulation of Active Modular Multilevel Converter; [有源型模块化多电平.pdf"]
---

# Full-state Arm Average Value Model for Simulation of Active Modular Multilevel Converter; [有源型模块化多电平

**作者**: CNKI
**年份**: 2022
**来源**: `19、20、21/EMT_task_20/Tang 等 - 2022 - Full-state Arm Average Value Model for Simulation of Active Modular Multilevel Converter; [有源型模块化多电平.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献


- 提出有源型MMC桥臂全状态平均值模型，计算速度不受子模块数量影响
- 结合动态平均化与离散化伴随模型构建等效电路，准确反映内部暂态特性
- 设计功能性电路解决闭锁工况二极管插值难题，实现换流器全状态仿真


## 使用的方法


- [[动态平均化理论|动态平均化理论]]
- [[离散化伴随模型|离散化伴随模型]]
- [[梯形积分法|梯形积分法]]
- [[戴维南等效电路|戴维南等效电路]]
- [[平均值建模|平均值建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[储能单元|储能单元]]
- [[子模块|子模块]]
- [[桥臂电抗器|桥臂电抗器]]
- [[双向buck-boost变换器|双向Buck-Boost变换器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[柔性直流输电|柔性直流输电]]
- [[换流器闭锁|换流器闭锁]]
- [[储能集成|储能集成]]
- [[全状态仿真|全状态仿真]]


## 主要发现


- 模型计算效率显著优于详细等效模型，且精度相近，不受子模块数影响
- 等效电路能准确复现子模块电容电压波动与桥臂环流等内部暂态特性
- 闭锁工况下功能性电路有效解决二极管插值问题，实现全状态稳定仿真


