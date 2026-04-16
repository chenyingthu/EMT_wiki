---
title: "Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs"
type: source
authors: ['Peng Li']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106714. doi:10.1016/j.epsr.2020.106714"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Li 等 - 2020 - Interpolation for power electronic circuit simulation revisited with matrix exponential and dense ou.pdf"]
---

# Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs

**作者**: Peng Li
**年份**: 2020
**来源**: `25/Li 等 - 2020 - Interpolation for power electronic circuit simulation revisited with matrix exponential and dense ou.pdf`

## 摘要

Interpolation for power electronic circuit simulation revisited with matrix Peng Li, Zixiang Meng, Xiaopeng Fu⁎, Hao Yu, Chengshan Wang Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin, China With a high penetration of power electronic equipment, transient simulation for power electronic circuit has been a main challenge for performance improvement of the electromagnetic transient simulation tools. In this

## 核心贡献


- 提出基于矩阵指数与密集输出公式的两种L稳定求解器，优化积分与插值组合
- 设计匹配策略实现积分与高阶插值最优组合，提升开关事件处理精度
- 开发三阶高精度与一阶高效求解器，克服现有工具在电力电子仿真中的精度瓶颈


## 使用的方法


- [[矩阵指数积分法|矩阵指数积分法]]
- [[padé逼近|Padé逼近]]
- [[密集输出公式|密集输出公式]]
- [[高阶插值|高阶插值]]
- [[状态空间法|状态空间法]]
- [[缩放平方算法|缩放平方算法]]


## 涉及的模型


- [[tcr|TCR]]
- [[vsc-model|VSC]]
- [[电力电子电路|电力电子电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子电路仿真|电力电子电路仿真]]
- [[开关事件插值|开关事件插值]]
- [[数值积分算法|数值积分算法]]
- [[仿真精度与效率|仿真精度与效率]]


## 主要发现


- 三阶求解器在电力电子仿真中精度显著优于现有主流电磁暂态仿真工具
- 一阶求解器以更低计算成本实现同等精度，大幅提升仿真运算速度
- TCR与VSC-HVDC算例验证了新求解器在开关事件处理上的高精度与高效性


