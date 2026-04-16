---
title: "A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;5;10.1109/TPWRD.2023.3271027"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/03/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf"]
---

# A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers

**作者**: 
**年份**: 2023
**来源**: `03/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf`

## 摘要

—Electromagnetic transient (EMT) modeling for the modularized solid-state transformer (MSST) faces critical difﬁ- culties because the dynamics of the complex-structured submod- ules, which contain dual active bridges (DAB) and multiple active bridges (MAB), are hard to be described in analytical formulas. Ex- isting models have problems of a narrow dynamic frequency band, insufﬁcient simulation accuracy, or are unable to operate under fast transients. This paper proposes a parallel simulation frame- work for MSST that preserves the original model’s broadband characteristics and remarkably improves the simulation efﬁciency. The main novelty towards previous work is the detailed modeling of the multi-winding transformer, the decoupled modeling of the submodules, and the parallel design of si

## 核心贡献


- 基于统一磁等效电路的多绕组变压器详细建模，准确反映铁芯饱和特性。
- 提出基于割集的子模块解耦方法，简化等效电路并突破传统模型速度瓶颈。
- 构建多核并行仿真框架，将子模块计算分配至独立CPU核心实现加速。


## 使用的方法


- [[统一磁等效电路法|统一磁等效电路法]]
- [[割集解耦建模|割集解耦建模]]
- [[并行计算框架|并行计算框架]]
- [[高精度高速等效模型|高精度高速等效模型]]


## 涉及的模型


- [[模块化固态变压器|模块化固态变压器]]
- [[多主动桥|多主动桥]]
- [[双主动桥|双主动桥]]
- [[多绕组变压器|多绕组变压器]]
- [[级联h桥拓扑|级联H桥拓扑]]


## 相关主题


- [[电磁暂态建模|电磁暂态建模]]
- [[并行仿真|并行仿真]]
- [[解耦建模|解耦建模]]
- [[电力电子变压器|电力电子变压器]]
- [[宽频带仿真|宽频带仿真]]


## 主要发现


- PSCAD验证表明框架在保持宽频带特性的同时，仿真效率获得显著提升。
- 解耦等效模型精度与详细模型一致，多核并行大幅缩短长时暂态仿真耗时。
- 有效克服传统模型在方波电压跳变时的数值不稳定问题，保障暂态精度。


