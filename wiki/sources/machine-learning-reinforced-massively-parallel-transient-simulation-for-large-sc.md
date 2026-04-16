---
title: "Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Systems;2025;40;1;10.1109/TPWRS.2024.3409729"
tags: ['renewable']
created: "2026-04-13"
sources: ["EMT_Doc/25/Cheng 等 - 2025 - Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy.pdf"]
---

# Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems

**作者**: 
**年份**: 2024
**来源**: `25/Cheng 等 - 2025 - Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy.pdf`

## 摘要

—Renewable energy systems (RESs) are pivotal in the transition to eco-friendly smart grids. The complexity and uncer- tainty of RESs, driven by uncontrollable natural forces like sun- light and wind, bring challenges to integrating RESs into modern power systems. Electromagnetic transient (EMT) simulation is an effective method for studying the integration of RESs. Currently, the EMT simulation of RESs is limited to small-scale and lumped RES models due to the model complexity and nonlinearity, which cannot reﬂect the detailed characteristics of large-scale RESs in practice. This paper introduces a data-oriented, machine learning- enhanced approach to achieve massively parallel EMT simulation on CPU-GPU, designed to efﬁciently model and simulate large- scale, detailed RES. It incorporates 

## 核心贡献


- 提出基于MLP与GRU神经网络的新能源数据驱动建模方法替代传统非线性迭代
- 构建面向数据的实体组件系统架构与GPU实例化策略实现ANN模型高效并行集成
- 采用蒙特卡洛方法生成训练数据精准拟合光伏阵列局部遮荫等多变量非线性特性


## 使用的方法


- [[人工神经网络-ann|人工神经网络(ANN)]]
- [[多层感知机-mlp|多层感知机(MLP)]]
- [[门控循环单元-gru|门控循环单元(GRU)]]
- [[蒙特卡洛数据生成|蒙特卡洛数据生成]]
- [[实体组件系统-ecs-架构|实体组件系统(ECS)架构]]
- [[gpu实例化技术|GPU实例化技术]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]


## 涉及的模型


- [[光伏阵列-pv|光伏阵列(PV)]]
- [[dfig-model|DFIG]]
- [[储能电池系统|储能电池系统]]
- [[风电场|风电场]]
- [[微电网|微电网]]
- [[ieee-118节点系统|IEEE 118节点系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大规模新能源并网|大规模新能源并网]]
- [[并行计算|并行计算]]
- [[机器学习建模|机器学习建模]]
- [[gpu加速仿真|GPU加速仿真]]
- [[数据驱动建模|数据驱动建模]]
- [[新能源场站建模|新能源场站建模]]


## 主要发现


- 在含两百万新能源实体的系统中仿真速度较传统CPU非线性迭代提升四百倍
- 神经网络模型经MATLAB验证精度满足电磁暂态仿真要求且计算结构统一
- 采用单精度浮点数与统一矩阵运算显著降低GPU显存开销与主机设备数据交换延迟


