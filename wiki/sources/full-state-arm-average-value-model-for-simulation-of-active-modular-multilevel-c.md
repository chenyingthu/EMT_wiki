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

- 提出适用于有源型MMC的桥臂全状态平均值仿真模型
- 基于动态平均化理论推导桥臂平均值数学模型及等效电路模型
- 实现计算速度不受子模块个数影响的高效仿真，并支持闭锁状态仿真

## 使用的方法

- [[动态平均化理论|动态平均化理论]]
- [[离散化伴随模型|离散化伴随模型]]
- [[电路整合与化简|电路整合与化简]]
- [[pscad-emtdc仿真验证|PSCAD/EMTDC仿真验证]]

## 涉及的模型

- [[有源型模块化多电平换流器|有源型模块化多电平换流器]]
- [[桥臂全状态平均值模型|桥臂全状态平均值模型]]
- [[完整详细模型-fdm|完整详细模型(FDM)]]
- [[详细等效模型-dem|详细等效模型(DEM)]]
- [[传统平均值模型-avm|传统平均值模型(AVM)]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[模块化多电平换流器建模|模块化多电平换流器建模]]
- [[储能单元集成|储能单元集成]]
- [[换流器闭锁仿真|换流器闭锁仿真]]
- [[柔性直流输电|柔性直流输电]]

## 主要发现

- 模型聚焦子模块低频动态共性，能准确反映桥臂整体暂态特性
- 仿真计算速度不受子模块数量影响，显著提升效率
- 模型可有效用于有源型MMC闭锁状态下的仿真研究
- PSCAD/EMTDC实例验证了模型的有效性与精度
