---
title: "A topology-based simplified dynamic model and solving algorithm for LCC-HVDC converters considering commutation failure"
type: source
authors: ['Yangyang He']
year: 2025
journal: "International Journal of Electrical Power and Energy Systems, 173 (2025) 111410. doi:10.1016/j.ijepes.2025.111410"
tags: ['lcc']
created: "2026-04-13"
sources: ["EMT_Doc/04/Chen 等 - 2022 - A Testing Tool for Converter-Dominated Power System Stochastic Electromagnetic Transient Simulation.pdf"]
---

# A topology-based simplified dynamic model and solving algorithm for LCC-HVDC converters considering commutation failure

**作者**: Yangyang He
**年份**: 2025
**来源**: `04/Chen 等 - 2022 - A Testing Tool for Converter-Dominated Power System Stochastic Electromagnetic Transient Simulation.pdf`

## 摘要

A topology-based simplified dynamic model and solving algorithm for LCC-HVDC converters considering commutation failure , Nengling Tai a, Jin Xu b, Wenzhuo Liu c, Panjie Lian c, Haizhen Zhang d a College of Smart Energy, Shanghai Jiao Tong University, Shanghai 200240, China b School of Electrical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China

## 核心贡献


- 提出基于拓扑的简化动态模型，采用理想开关保留晶闸管离散换相特性
- 设计结构稳定求解算法，分解主网与阀级辅助网，保持矩阵维数恒定
- 引入基于直流电流变化率的自适应步长策略，兼顾稳态加速与暂态精度


## 使用的方法


- [[拓扑网络分解|拓扑网络分解]]
- [[理想开关建模|理想开关建模]]
- [[结构稳定节点求解|结构稳定节点求解]]
- [[自适应变步长控制|自适应变步长控制]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[晶闸管阀组|晶闸管阀组]]
- [[简化变压器漏抗模型|简化变压器漏抗模型]]
- [[直流平波电抗器|直流平波电抗器]]


## 相关主题


- [[换相失败机理|换相失败机理]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态等值建模|动态等值建模]]
- [[计算效率优化|计算效率优化]]
- [[交直流系统分析|交直流系统分析]]


## 主要发现


- 模型在稳态与故障工况下均能精确复现换相失败动态，验证了拓扑建模有效性
- 相比PSCAD/EMTDC，该算法在保持高精度的同时显著降低了计算耗时
- 自适应步长策略有效实现了稳态大步长加速与暂态小步长高分辨率的平衡


