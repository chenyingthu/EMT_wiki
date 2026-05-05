---
title: "Energy Storage System"
type: topic
tags: [energy-storage-system]
created: "2026-05-04"
---

# Energy Storage System

## 定义与边界

本页面为自动创建的topic类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用


基于相关研究的应用：

1. - 问题定位：本文提出一种面向含大规模超快充（XFC）系统的输配电网高保真电磁暂态（EMT）仿真的混合数值算法框架。传统EMT仿真器对整个系统采用单一离散化方法（通常为梯形法），导致全局大矩阵求逆计算负担极重。本文首次联合应用基于数值刚度的分离、基于时间常数的分离、微分代数方程（DAE）聚类与聚合以...

2. - 问题定位：本文提出一种面向未来大规模电网的电磁暂态（EMT）高效仿真架构，核心基于传输线传播延迟特性实现网络解耦与并行计算。通过采用基于延迟的线路模型替代传统π型等效，在物理延迟边界处自然切断电气耦合，构建块对角导纳矩阵，使各子网络可在独立处理器上并行求解。针对缺乏天然延迟边界的场景，引入补偿法...

## 主要分支与机制

- 待补充



相关研究中的方法描述：

- - 问题定位：本文提出一种基于CPU-GPU异构计算架构的EMT-TS联合仿真方法，用于高效分析含海量公用级电池储能系统（BESS）的交直流电网暂态交互。针对传统CPU串行处理大规模异构储能单元计算负担重的问题，采用向量化建模技术将不同化学类型（锂离子、铅酸、镍镉）电池的戴维南等效模型转化为同构向量形式，以充分适配GPU的细粒度SIMT并行架构。
- 方法机制：本文提出一种基于CPU-GPU异构计...

## 形式化表达

- 待补充



基于相关研究的公式表达：

$V_{	ext{Bat}} = E_0 + E_{	ext{pol}} + E_{	ext{exp}} + S_{	ext{ch}} E_{	ext{chg}} + (1 - S_{	ext{ch}}) E_{	ext{dsc}}$

$

*电池戴维南等效电压源表达式，包含恒定电压、极化电压、指数区电压及充放电动态电压，$

$为充放电状态二值标志。*

**公式2**: $

## 适用边界与失败模式

- 待补充

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源


- [[electromagnetic-transient-emt-simulation-algorithms-for-evaluation-of-large-scal]]
- [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim]]
- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]]
