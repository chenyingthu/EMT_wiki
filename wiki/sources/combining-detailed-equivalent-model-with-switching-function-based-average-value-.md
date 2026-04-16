---
title: "Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation of MMCs"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Energy Conversion;2020;35;1;10.1109/TEC.2019.2944352"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/10/Meng 等 - 2020 - Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and A.pdf"]
---

# Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation of MMCs

**作者**: 
**年份**: 2020
**来源**: `10/Meng 等 - 2020 - Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and A.pdf`

## 摘要

—Modeling and simulation play a vital role in the design and testing of modular multilevel converter (MMC) high voltage direct current (HVDC) systems. Detailed equivalent model (DEM) and switching-function-based average value model (SFB-AVM) are two major types of accurate and efﬁcient models to represent the dynamic response of the MMCs. However, the DEM and the SFB-AVM possess unique beneﬁts depending on the purpose of the simulation studies. The DEM provides a detailed representa- tion of submodule (SM) switching events and individual capacitor ripples. The SFB-AVM provides faster simulation speed by using arm equivalent capacitance. Combining both models in a universal arm equivalent circuit gives the users the choice of selecting the most appropriate modeling method during dynamic sim

## 核心贡献


- 提出适用于多种子模块拓扑的广义开关函数平均值模型，构建统一桥臂等效电路
- 设计DEM与GSFB-AVM数据交互机制，实现动态仿真中两种模型的平滑无缝切换
- 精确计及不同子模块拓扑下IGBT与二极管的导通及开关损耗，提升模型物理保真度


## 使用的方法


- [[开关函数法|开关函数法]]
- [[平均值建模|平均值建模]]
- [[详细等效建模|详细等效建模]]
- [[统一桥臂等效电路|统一桥臂等效电路]]
- [[实时仿真技术|实时仿真技术]]
- [[模型平滑切换机制|模型平滑切换机制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[hbsm|HBSM]]
- [[fbsm|FBSM]]
- [[cdsm|CDSM]]
- [[mbsm|MBSM]]
- [[vsc-hvdc|VSC-HVDC]]
- [[dem|DEM]]
- [[average-value-model|平均值模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[mmc-model|MMC]]
- [[平均值模型|平均值模型]]
- [[详细等效模型|详细等效模型]]
- [[动态仿真|动态仿真]]
- [[功率器件损耗建模|功率器件损耗建模]]


## 主要发现


- GSFB-AVM仿真速度独立于子模块数量，含4800个子模块的单站CPU耗时仅9.45微秒
- 混合模型在暂态过程中实现平滑切换，兼顾子模块级开关细节与系统级快速仿真需求
- 离线与实时仿真验证表明，该模型在多端HVDC系统中均保持高精度与高效率


