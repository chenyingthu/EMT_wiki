---
title: "Comparative study on electromechanical and electromagnetic transient model for grid-connected photov"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Sun 等 - 2014 - Comparative study on electromechanical and electromagnetic transient model for grid-connected photov.pdf"]
---

# Comparative study on electromechanical and electromagnetic transient model for grid-connected photov

**作者**: 
**年份**: 2014
**来源**: `10/Sun 等 - 2014 - Comparative study on electromechanical and electromagnetic transient model for grid-connected photov.pdf`

## 摘要

The computing speed of electromagnetic transient model for grid-connected photovoltaic power system is very slow because of its complexity. To solve this problem, a general electromechanical transient model for grid-connected photovoltaic power system is proposed, in which there are not electrical components and high frequency switching device, and it only consists of pure mathematic calculations, is simple and has fast calculation speed. By comparing the simulation results of this electromechanical transient model with electromagnetic transient model in PSCAD/EMTDC, we found that the simulation time is reduced greatly and the results are agreeable basically, which verifies the correctness and validity of the electromechanical transient model. The electromechanical transient model provides

## 核心贡献


- 提出不含电气元件与高频开关器件的并网光伏通用机电暂态模型
- 基于纯数学计算与传递函数构建光伏阵列、MPPT及逆变器外特性
- 屏蔽厂家内部拓扑差异，实现适用于大规模电站仿真的通用化建模


## 使用的方法


- [[传递函数建模|传递函数建模]]
- [[平均值模型|平均值模型]]
- [[pq解耦控制|PQ解耦控制]]
- [[dq坐标变换|dq坐标变换]]
- [[对比仿真验证|对比仿真验证]]


## 涉及的模型


- [[光伏电池|光伏电池]]
- [[mppt控制器|MPPT控制器]]
- [[dc-dc变换器|DC/DC变换器]]
- [[直流母线电容|直流母线电容]]
- [[并网逆变器|并网逆变器]]
- [[机电暂态模型|机电暂态模型]]
- [[电磁暂态模型|电磁暂态模型]]


## 相关主题


- [[机电暂态建模|机电暂态建模]]
- [[大规模光伏电站仿真|大规模光伏电站仿真]]
- [[新能源并网|新能源并网]]
- [[模型降阶|模型降阶]]
- [[仿真加速|仿真加速]]


## 主要发现


- 机电暂态模型仿真波形与电磁暂态模型基本吻合，验证了模型正确性
- 剔除高频开关与详细电路后，仿真计算时间大幅缩短，显著提升效率
- 该通用模型满足大电网机电暂态分析需求，具备大规模工程实用价值


