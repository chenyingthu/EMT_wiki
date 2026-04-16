---
title: "A state-space approach for accelerated simulation of modular multilevel converters"
type: source
authors: ['Jinli Zhao']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112413. doi:10.1016/j.epsr.2025.112413"
tags: ['mmc', 'state-space']
created: "2026-04-13"
sources: ["EMT_Doc/04/Zhao 等 - 2026 - A state-space approach for accelerated simulation of modular multilevel converters.pdf"]
---

# A state-space approach for accelerated simulation of modular multilevel converters

**作者**: Jinli Zhao
**年份**: 2025
**来源**: `04/Zhao 等 - 2026 - A state-space approach for accelerated simulation of modular multilevel converters.pdf`

## 摘要

A state-space approach for accelerated simulation of modular a State Key Laboratory of Smart Power Distribution Equipment and System, Tianjin University, Tianjin 300072, China b Department of Electrical Engineering, Poly-technique Montr´eal, Montr´eal, Qu´ebec H3T 1J4, Canada Modular multilevel converter (MMC) based high-voltage direct current (HVDC) transmission technology has been widely applied in practical engineering. With the continuous increase in transmission voltage and capacity,

## 核心贡献


- 基于开关状态组合对子模块分组并引入虚拟状态变量，大幅降低状态矩阵维度
- 提出基于状态变量分组的高效电容电压均衡算法，完整保留子模块个体动态信息
- 构建状态空间框架下的MMC降阶模型，使计算耗时随电平数呈对数级增长


## 使用的方法


- [[状态空间法|状态空间法]]
- [[降阶建模|降阶建模]]
- [[数值积分|数值积分]]
- [[分段线性开关模型|分段线性开关模型]]
- [[电容电压均衡算法|电容电压均衡算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[hbsm|HBSM]]
- [[mmc-model|MMC]]
- [[电力网络|电力网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真加速|仿真加速]]
- [[状态空间建模|状态空间建模]]
- [[大规模电力电子系统|大规模电力电子系统]]
- [[电容电压均衡|电容电压均衡]]


## 主要发现


- 仿真计算时间随MMC电平数增加呈对数增长，显著提升大规模系统仿真效率
- 降阶模型在保留各子模块电容电压动态的同时，与详细模型仿真精度高度一致
- 所提算法兼容高阶数值积分器，在加速仿真的同时未引入额外精度损失


