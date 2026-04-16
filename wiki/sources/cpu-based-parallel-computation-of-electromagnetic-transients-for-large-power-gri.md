---
title: "CPU based parallel computation of electromagnetic transients for large power grids"
type: source
authors: ['A. Abusalah']
year: 2018
journal: "Electric Power Systems Research, 162 (2018) 57-63. doi:10.1016/j.epsr.2018.04.017"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Abusalah 等 - 2018 - CPU based parallel computation of electromagnetic transients for large power grids.pdf"]
---

# CPU based parallel computation of electromagnetic transients for large power grids

**作者**: A. Abusalah
**年份**: 2018
**来源**: `11/Abusalah 等 - 2018 - CPU based parallel computation of electromagnetic transients for large power grids.pdf`

## 摘要

CPU based parallel computation of electromagnetic transients for large A. Abusalaha, O. Saadb, J. Mahseredjiana,⁎, U. Karaagacc, L. Gerin-Lajoieb, I. Kocara a Ecole Polytechnique Montreal, Quebec H3C 3A7, Canada b IREQ, Hydro-Québec, Varennes, Quebec, J3X 1S1, Canada c Hong Kong Polytechnic University, Hung Hom, Hong Kong

## 核心贡献


- 基于KLU求解器实现共享内存CPU并行计算，自动利用线路自然解耦特性分割稀疏矩阵
- 将并行技术应用于全迭代牛顿法求解器，实现所有非线性模型同步求解且无需人工干预
- 提出基于块三角分解的自动网络撕裂方法，无缝集成至EMTP提升大规模电网仿真速度


## 使用的方法


- [[改进增广节点分析法|改进增广节点分析法]]
- [[klu稀疏矩阵求解器|KLU稀疏矩阵求解器]]
- [[块三角分解|块三角分解]]
- [[牛顿迭代法|牛顿迭代法]]
- [[共享内存并行计算|共享内存并行计算]]
- [[自动网络撕裂|自动网络撕裂]]


## 涉及的模型


- [[分布参数输电线路|分布参数输电线路]]
- [[电缆模型|电缆模型]]
- [[非线性开关模型|非线性开关模型]]
- [[风电机组|风电机组]]
- [[大规模交流电网|大规模交流电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[大规模电网|大规模电网]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[离线仿真|离线仿真]]
- [[电力电子换流器建模|电力电子换流器建模]]


## 主要发现


- KLU并行求解器在魁北克大电网算例中显著缩短计算时间，且全程保持电路级仿真精度
- 自动块三角分解能精准识别线路延迟形成的独立子网，实现多核CPU高效并行加速
- 全迭代牛顿法结合并行计算可有效处理含电力电子换流器的大规模风电并网暂态仿真


