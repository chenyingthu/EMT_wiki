---
title: "Fast electromagnetic transient simulation models of modular multilevel converter"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Fast electromagnetic transient simulation models of modular multilevel converter.pdf"]
---

# Fast electromagnetic transient simulation models of modular multilevel converter

**作者**: 
**年份**: 2026
**来源**: `19、20、21/EMT_task_19/Fast electromagnetic transient simulation models of modular multilevel converter.pdf`

## 摘要

To shorten the time expended in electromagnetic transient simulation for modular multilevel converter (MMC), two kinds of fast simulation models are proposed. Through analyzing the principle of the sub-module of MMC, it is put forward to define the bridge arms of MMC as a detailed numerical calculation model, which is composed of a self-defined numerical calculation model and controlled voltage source; on the basis of this model, a simulation method for a hybrid model, which combines electromagnetic transient model of independent sub-module with numerical calculation model for common sub-module, is designed to remedy the defect that it is hard for numerical calculation model to simulate electromagnetic transient process of sub-module. To further improve simulation speed of this model, thro

## 核心贡献


- 提出桥臂数值计算详细模型，以自定义模块与受控源替代子模块开关仿真
- 设计混合仿真方法，融合独立子模块电磁暂态模型与数值模型以分析内部故障
- 建立数值计算平均值模型，简化均压排序与状态差异从而大幅提升仿真速度


## 使用的方法


- [[数值计算建模|数值计算建模]]
- [[平均值模型法|平均值模型法]]
- [[混合仿真方法|混合仿真方法]]
- [[受控电压源等效|受控电压源等效]]
- [[能量平均分配|能量平均分配]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mmc-model|MMC]]
- [[半桥型子模块|半桥型子模块]]
- [[桥臂等效模型|桥臂等效模型]]
- [[受控电压源|受控电压源]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[快速仿真|快速仿真]]
- [[混合仿真|混合仿真]]
- [[环流抑制|环流抑制]]
- [[电压均衡控制|电压均衡控制]]
- [[直流输电|直流输电]]


## 主要发现


- 数值详细模型在保持外特性与环流精度的同时，显著缩短大规模系统仿真耗时
- 混合仿真方法能准确复现子模块内部故障暂态过程，且不降低整体计算精度
- 平均值模型可精确反映电容电压能量波动与环流特性，满足多端直流快速仿真需求


