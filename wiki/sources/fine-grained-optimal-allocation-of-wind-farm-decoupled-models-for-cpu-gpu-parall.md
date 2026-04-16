---
title: "Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2026.3669438"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Liu 等 - 2026 - Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation.pdf"]
---

# Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation

**作者**: 
**年份**: 2025
**来源**: `19、20、21/EMT_task_19/Liu 等 - 2026 - Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation.pdf`

## 摘要

—Parallel simulation based on CPU-GPU heteroge- neous hardware, owing to its high speed-up ratio, has emerged as an effective approach for accelerating electromagnetic transient (EMT) simulation of wind farms. However, most existing studies rely mainly on hardware multi-threading capabilities, with lim- ited quantitative analysis of model–hardware adaptability, result- ing in insufficient exploitation of the complementary advantages of CPUs and GPUs. To this end, this paper proposes a fine- grained optimal allocation method (FGOAM) that formulates the hardware assignment of each subsystem in wind farms as a constrained optimization problem for maximal simulation efficiency. Firstly, a bottom-up quantification method is developed to accurately assess the computational resources and solution

## 核心贡献


- 提出自底向上量化方法将计算分解为顺序与并行步骤以精确评估资源耗时
- 首次将硬件分配建模为整数非线性规划问题实现子系统步级细粒度最优分配
- 提出增强型分配算法通过整数变量约简降低求解复杂度且不牺牲分配最优性


## 使用的方法


- [[节点分析法|节点分析法]]
- [[电容电感支路解耦法|电容电感支路解耦法]]
- [[整数非线性规划|整数非线性规划]]
- [[自底向上量化方法|自底向上量化方法]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[风电场|风电场]]
- [[解耦模型|解耦模型]]
- [[控制系统|控制系统]]
- [[电气系统|电气系统]]


## 相关主题


- [[并行计算|并行计算]]
- [[异构计算|异构计算]]
- [[风电场建模|风电场建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[最优分配|最优分配]]


## 主要发现


- 针对四百台风机风电场最优分配策略使整体电磁暂态仿真速度提升两个数量级
- 自底向上量化方法能精确预测各子系统计算资源需求与单步求解时间
- 增强型算法在保持分配最优性的同时显著降低了整数规划模型的求解复杂度


