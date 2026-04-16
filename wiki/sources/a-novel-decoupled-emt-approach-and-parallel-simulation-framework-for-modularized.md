---
title: "A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;5;10.1109/TPWRD.2023.3271027"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/02/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf"]
---

# A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers

**作者**: 
**年份**: 2023
**来源**: `02/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf`

## 摘要

—Electromagnetic transient (EMT) modeling for the modularized solid-state transformer (MSST) faces critical difﬁ- culties because the dynamics of the complex-structured submod- ules, which contain dual active bridges (DAB) and multiple active bridges (MAB), are hard to be described in analytical formulas. Ex- isting models have problems of a narrow dynamic frequency band, insufﬁcient simulation accuracy, or are unable to operate under fast transients. This paper proposes a parallel simulation frame- work for MSST that preserves the original model’s broadband characteristics and remarkably improves the simulation efﬁciency. The main novelty towards previous work is the detailed modeling of the multi-winding transformer, the decoupled modeling of the submodules, and the parallel design of si

## 核心贡献


- 基于UMEC方法建立多绕组变压器模型，精确刻画铁芯饱和与复杂电磁耦合特性
- 提出基于割集的子模块解耦建模方法，简化桥臂等效电路，显著提升仿真速度
- 构建多核并行仿真框架，将子模块等效计算分配至不同CPU核心实现高效计算


## 使用的方法


- [[统一磁等效电路法-umec|统一磁等效电路法(UMEC)]]
- [[割集解耦法|割集解耦法]]
- [[高精度高速等效模型-hem|高精度高速等效模型(HEM)]]
- [[多核并行计算|多核并行计算]]


## 涉及的模型


- [[模块化固态变压器-msst|模块化固态变压器(MSST)]]
- [[多主动桥-mab|多主动桥(MAB)]]
- [[双主动桥-dab|双主动桥(DAB)]]
- [[多绕组变压器|多绕组变压器]]
- [[级联h桥拓扑|级联H桥拓扑]]


## 相关主题


- [[电磁暂态建模|电磁暂态建模]]
- [[并行仿真|并行仿真]]
- [[解耦建模|解耦建模]]
- [[电力电子变压器|电力电子变压器]]
- [[仿真加速|仿真加速]]


## 主要发现


- PSCAD验证表明模型宽频带精度高，有效避免电压跳变引发的数值不稳定问题
- 相比详细模型，并行框架大幅降低计算耗时，实现秒级暂态过程的高效仿真
- 解耦等效电路在保持与详细模型一致精度的同时，显著提升多模块系统的仿真效率


