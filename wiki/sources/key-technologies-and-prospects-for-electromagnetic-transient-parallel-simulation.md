---
title: "Key Technologies and Prospects for Electromagnetic Transient Parallel Simulation in New Power System"
type: source
authors: ['CNKI']
year: 2024
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Jiang 等 - 2024 - Key Technologies and Prospects for Electromagnetic Transient Parallel Simulation in New Power System.pdf"]
---

# Key Technologies and Prospects for Electromagnetic Transient Parallel Simulation in New Power System

**作者**: CNKI
**年份**: 2024
**来源**: `25/Jiang 等 - 2024 - Key Technologies and Prospects for Electromagnetic Transient Parallel Simulation in New Power System.pdf`

## 摘要

：Driven by the strategic goals of “peak carbon emissions” and “carbon neutrality”, power system is transforming into a new power system marked by extensive integration of new energy sources and a significant presence of power elec- tronic devices. This transformation induces significant changes in its power source structure, and operational characteristics. Electromagnetic transient simulation, possessing the capability to comprehensively and precisely depict the high-frequency dynamic traits of the power system, has become a pivotal tool for understanding the operational fea- tures of the new power system. However, electromagnetic transient simulation techniques under the traditional serial computing mode is inadequate in addressing the simulation scenarios involving the large-scale integ

## 核心贡献


- 系统梳理分网并行算法，提出精确等值与人为延时两类方法的融合与误差补偿机制
- 归纳多速率仿真接口设计与时序策略，明确机电电磁混合仿真的等值与数据交互方法
- 总结多核CPU与GPU及FPGA硬件加速方案，提出算法硬件深度融合的仿真平台发展方向


## 使用的方法


- [[分网并行算法|分网并行算法]]
- [[长传输线自然解耦法|长传输线自然解耦法]]
- [[节点分裂法|节点分裂法]]
- [[支路切割法|支路切割法]]
- [[多区域戴维南等效法|多区域戴维南等效法]]
- [[状态空间节点法|状态空间节点法]]
- [[延迟插入法|延迟插入法]]
- [[多速率仿真|多速率仿真]]
- [[机电电磁混合仿真|机电电磁混合仿真]]
- [[频率相关等值|频率相关等值]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[dfig-model|DFIG]]
- [[分布式电源|分布式电源]]
- [[有源配电网|有源配电网]]
- [[分布参数输电线路|分布参数输电线路]]
- [[同步发电机|同步发电机]]


## 相关主题


- [[并行计算|并行计算]]
- [[多速率仿真|多速率仿真]]
- [[硬件加速|硬件加速]]
- [[机电电磁混合仿真|机电电磁混合仿真]]
- [[实时仿真|实时仿真]]
- [[网络等值|网络等值]]
- [[硬件在环|硬件在环]]
- [[新型电力系统|新型电力系统]]


## 主要发现


- 精确等值法精度高但联络变量计算复杂度随分网数呈立方增长，大规模场景效率受限
- 人为延时法计算量呈线性增长，但缺乏特定元件或步长不当时易引发数值振荡与失稳
- 多速率接口采用并行时序结合诺顿等值可兼顾交直流混联系统仿真精度与计算效率


