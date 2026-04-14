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

- 改进了vsc的EMT建模方法，提升了系统级暂态分析精度

## 使用的方法

- [[脉冲电压-电流源对建模|脉冲电压-电流源对建模]]
- [[单向松耦合求解算法|单向松耦合求解算法]]
- [[交直流交互仿真|交直流交互仿真]]
- [[网络矩阵恒定技术-避免矩阵重构与lu分解|网络矩阵恒定技术(避免矩阵重构与LU分解)]]

## 涉及的模型

- [[vsc-model]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态(EMT)仿真]]
- [[仿真效率优化|仿真效率优化]]
- [[开关事件处理|开关事件处理]]
- [[大规模电力电子并网仿真|大规模电力电子并网仿真]]

## 主要发现

—With the increasing penetration of renewable energies in modern power grids, large amounts of voltage source converters (VSCs) have been installed, resulting in many new transient issues
