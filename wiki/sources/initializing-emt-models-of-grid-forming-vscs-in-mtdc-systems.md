---
title: "Initializing EMT models of grid forming VSCs in MTDC systems"
type: source
authors: ['Ahmad Allabadi']
year: 2024
journal: "Electric Power Systems Research, 235 (2024) 110674. doi:10.1016/j.epsr.2024.110674"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/24/Allabadi 等 - 2024 - Initializing EMT models of grid forming VSCs in MTDC systems.pdf"]
---

# Initializing EMT models of grid forming VSCs in MTDC systems

**作者**: Ahmad Allabadi
**年份**: 2024
**来源**: `24/Allabadi 等 - 2024 - Initializing EMT models of grid forming VSCs in MTDC systems.pdf`

## 摘要

Initializing EMT models of grid forming VSCs in MTDC systems Ahmad Allabadi a,*, Jean Mahseredjian a, Keijo Jacobs a, S´ebastien Denneti`ere b, Ilhan Kocar c, a Department of Electrical Engineering, Polytechnique Montr´eal, Canada b R´eseau de Transport d’Electricit´e, Paris, France c Department of Electrical Engineering, Hong Kong Polytechnic University, Hong Kong

## 核心贡献


- 提出CISS稳态初始化法，精确计算GVSC外环PI积分器初值，消除潮流初始化冲突
- 提出解耦接口DI方法，无需黑盒模型内部参数即可实现GVSC快速稳定启动


## 使用的方法


- [[潮流计算|潮流计算]]
- [[稳态分析|稳态分析]]
- [[时域初始化|时域初始化]]
- [[平均值模型|平均值模型]]
- [[解耦接口法|解耦接口法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[多端直流系统|多端直流系统]]
- [[平均值模型|平均值模型]]
- [[风电场模型|风电场模型]]
- [[变压器|变压器]]
- [[电抗器|电抗器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统初始化|系统初始化]]
- [[多端直流电网|多端直流电网]]
- [[构网型控制|构网型控制]]
- [[黑盒模型|黑盒模型]]
- [[交直流混合系统|交直流混合系统]]


## 主要发现


- 相比传统潮流初始化，所提方法将系统整体初始化时间缩短6.9倍
- 传统辅助电压源法会导致GVSC控制误差为零，引发积分器初值错误
- 在CIGRE BM4基准测试中验证了大规模交直流系统快速稳定初始化的有效性


