---
title: "Improved methods for optimization of power systems with renewable generation using electromagnetic transient simulators"
type: source
authors: ['D. Kuranage']
year: 2023
journal: "Electric Power Systems Research, 220 (2023) 109308. doi:10.1016/j.epsr.2023.109308"
tags: ['renewable']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kuranage 等 - 2023 - Improved methods for optimization of power systems with renewable generation using electromagnetic t.pdf"]
---

# Improved methods for optimization of power systems with renewable generation using electromagnetic transient simulators

**作者**: D. Kuranage
**年份**: 2023
**来源**: `23/Kuranage 等 - 2023 - Improved methods for optimization of power systems with renewable generation using electromagnetic t.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Improved methods for optimization of power systems with renewable generation using electromagnetic transient simulators✩ a Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada b Manitoba HVDC Research Center, 211 Commerce Drive, Winnipeg, MB, R3P 1A3, Canada

## 核心贡献


- 提出初始与运行时两种参数筛选方法，剔除无显著影响变量以降低优化维度
- 设计面向遗传算法的并行处理架构，并行化目标函数计算以加速EMT仿真评估
- 结合混合优化算法与EMT仿真器，构建高效的可再生能源系统参数整定框架


## 使用的方法


- [[优化驱动电磁暂态仿真-oe-emts|优化驱动电磁暂态仿真(OE-EMTS)]]
- [[参数筛选法|参数筛选法]]
- [[遗传算法-ga|遗传算法(GA)]]
- [[并行计算|并行计算]]
- [[混合优化算法|混合优化算法]]


## 涉及的模型


- [[type-4风电机组控制器|Type-4风电机组控制器]]
- [[并网变流器|并网变流器]]
- [[pscad-emtdc仿真模型|PSCAD/EMTDC仿真模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[优化算法|优化算法]]
- [[并行计算|并行计算]]
- [[可再生能源并网|可再生能源并网]]
- [[控制器参数整定|控制器参数整定]]
- [[基于仿真的优化设计|基于仿真的优化设计]]


## 主要发现


- 参数筛选法有效剔除冗余变量，在保持优化精度的同时显著降低问题维度
- 并行遗传算法大幅缩短高维参数优化耗时，验证了计算效率提升的有效性
- 所提框架成功实现Type-4风机控制器多参数自动整定，克服人工调参局限


