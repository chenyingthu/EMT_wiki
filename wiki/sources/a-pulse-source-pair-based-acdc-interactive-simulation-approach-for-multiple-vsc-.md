---
title: "A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Multiple-VSC Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2984275"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/03/TPWRD.2020.2984275.pdf.pdf"]
---

# A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Multiple-VSC Grids

**作者**: 
**年份**: 2020
**来源**: `03/TPWRD.2020.2984275.pdf.pdf`

## 摘要

—With the increasing penetration of renewable energies in modern power grids, large amounts of voltage source converters (VSCs) have been installed, resulting in many new transient issues. Electromagnetic transient (EMT) simulation plays an essential role in investigating and solving the issues. However, simulation efficiency plunges when object grids contain multiple VSCs, because each switching event incurs modification or re-decomposition of the network matrix in traditional EMT programs, which is very time-consuming. Thus, this paper proposes a VSC model represented by pulse voltage-current source pairs. Accordingly, a unidirectional loosely-coupled solving algorithm is designed. Synthetically, the authors propose a novel EMT simulation approach adaptive to systems with multiple VSCs. 

## 核心贡献


- 提出基于脉冲电压电流源对的VSC模型，精确表征开关瞬态过程
- 设计单向松耦合求解算法，避免开关事件引发的网络矩阵重构
- 构建多VSC电网交直流交互仿真框架，保持计算网络拓扑恒定


## 使用的方法


- [[脉冲电压电流源对建模|脉冲电压电流源对建模]]
- [[单向松耦合求解算法|单向松耦合求解算法]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[控制系统暂态分析-tacs|控制系统暂态分析(TACS)]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[igbt-反并联二极管开关|IGBT/反并联二极管开关]]
- [[直流侧电容|直流侧电容]]
- [[交直流混合电网|交直流混合电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[开关事件高效处理|开关事件高效处理]]
- [[交直流交互仿真|交直流交互仿真]]
- [[实时仿真加速|实时仿真加速]]


## 主要发现


- 所提方法在保持网络矩阵恒定的同时精确计及开关动作，显著提升仿真效率
- 相比传统EMTP，该方法避免了频繁的矩阵重构与LU分解，计算耗时大幅降低
- 多工况仿真验证表明，该模型在大幅提升计算速度的同时未引入精度损失


