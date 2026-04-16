---
title: "Parallelization of EMT simulations for integration of inverter-based resources"
type: source
authors: ['M. Ouafi']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109641. doi:10.1016/j.epsr.2023.109641"
tags: ['ibg']
created: "2026-04-13"
sources: ["EMT_Doc/30/Ouafi 等 - 2023 - Parallelization of EMT simulations for integration of inverter-based resources.pdf"]
---

# Parallelization of EMT simulations for integration of inverter-based resources

**作者**: M. Ouafi
**年份**: 2023
**来源**: `30/Ouafi 等 - 2023 - Parallelization of EMT simulations for integration of inverter-based resources.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Parallelization of EMT simulations for integration of M. Ouafi a, J. Mahseredjian b, J. Peralta c, H. Gras d, S. Denneti`ere a,*, B. Bruned a This paper presents a co-simulation tool to link multiple instances of an electromagnetic transient (EMT) simulation tool for parallel and fast computations. The tool exploits the propagation delays of transmission lines

## 核心贡献


- 提出基于FMI与信号量的多实例协同仿真架构，实现子网络无近似并行求解
- 引入双缓冲通信机制与多速率选项，保障异步数据完整性并支持变步长计算
- 开发免改底层代码的DLL接口方案，实现子网自动划分与潮流自动初始化


## 使用的方法


- [[协同仿真|协同仿真]]
- [[并行计算|并行计算]]
- [[多速率仿真|多速率仿真]]
- [[传输线延迟解耦|传输线延迟解耦]]
- [[fmi接口|FMI接口]]
- [[信号量同步|信号量同步]]
- [[双缓冲通信|双缓冲通信]]
- [[潮流初始化|潮流初始化]]


## 涉及的模型


- [[ibr|IBR]]
- [[风电场|风电场]]
- [[光伏场|光伏场]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[igbt变流器|IGBT变流器]]
- [[详细电路模型|详细电路模型]]


## 相关主题


- [[并行计算|并行计算]]
- [[协同仿真|协同仿真]]
- [[新能源并网|新能源并网]]
- [[大规模电网仿真|大规模电网仿真]]
- [[仿真加速|仿真加速]]
- [[多速率仿真|多速率仿真]]


## 主要发现


- 智利电网大规模IBR仿真验证了该方法在保持精度的同时显著缩短计算时间
- 双缓冲与信号量机制有效避免了多线程数据冲突，实现了无近似误差的稳定并行求解
- 潮流自动初始化大幅减少了非线性IGBT模型的启动耗时，提升了整体仿真效率


