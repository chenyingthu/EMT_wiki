---
title: "Acceleration strategies for EMT Simulation of HVDC systems"
type: source
authors: ['A. Allabadi']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112399. doi:10.1016/j.epsr.2025.112399"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Allabadi 等 - 2026 - Acceleration strategies for EMT Simulation of HVDC systems.pdf"]
---

# Acceleration strategies for EMT Simulation of HVDC systems

**作者**: A. Allabadi
**年份**: 2025
**来源**: `05/Allabadi 等 - 2026 - Acceleration strategies for EMT Simulation of HVDC systems.pdf`

## 摘要

Acceleration strategies for EMT Simulation of HVDC systems☆,☆☆,★,★★ , J. Mahseredjian a, S. Denneti`ere b, A. Abusalah a, I. Kocar a a Polytechnique Montr´eal, Montreal, QC H3T 1J4, Canada b R´eseau de Transport d’Electricit´e, Paris 92932, France This paper investigates electromagnetic transient (EMT) simulation of large-scale multiterminal HVDC (MTDC)

## 核心贡献


- 提出基于传输线解耦的网络并行化策略，利用传播延迟实现多CPU并行计算。
- 设计基于FMI标准的控制系统并行化方法，实现模块化控制子任务分布式求解。
- 融合网络并行、控制并行与优化顺序求解器，构建混合加速策略提升仿真效率。


## 使用的方法


- [[传输线并行化-tlp|传输线并行化(TLP)]]
- [[控制系统并行化-ctrlp|控制系统并行化(CtrlP)]]
- [[优化顺序求解器-oseqctrl|优化顺序求解器(OSeqCtrl)]]
- [[功能模型接口-fmi|功能模型接口(FMI)]]
- [[非迭代雅可比法-nij|非迭代雅可比法(NIJ)]]
- [[主从协同仿真|主从协同仿真]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[dfig-model|DFIG]]
- [[风电场|风电场]]
- [[直流电缆|直流电缆]]
- [[宽带线路模型|宽带线路模型]]
- [[电网等值电源|电网等值电源]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[多端直流输电-mtdc|多端直流输电(MTDC)]]
- [[并行计算|并行计算]]
- [[离线仿真|离线仿真]]
- [[控制系统加速|控制系统加速]]
- [[混合加速策略|混合加速策略]]


## 主要发现


- 控制系统计算占比约87%，其并行化可带来2.1倍加速，主导整体性能提升。
- 混合加速策略在InterOPERA基准系统中实现最高23倍加速且精度无损。
- 传输线并行化在3核CPU下使总仿真时间减半，验证了网络解耦的有效性。


