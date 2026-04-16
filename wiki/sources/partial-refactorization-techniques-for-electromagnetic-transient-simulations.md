---
title: "Partial Refactorization Techniques for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;4;10.1109/TPWRD.2025.3574482"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/Bruned 等 - 2025 - Partial Refactorization Techniques for Electromagnetic Transient Simulations.pdf"]
---

# Partial Refactorization Techniques for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2025
**来源**: `31/Bruned 等 - 2025 - Partial Refactorization Techniques for Electromagnetic Transient Simulations.pdf`

## 摘要

—This paper explores partial refactorization techniques to accelerate the simulation of Electromagnetic Transients (EMTs) in power systems. Direct sparse left-looking LU factorization from the KLU solver is used to solve network equations. The refactoriza- tionstepcanbetime-consumingifthefactorizedmatrixvariesoften as the simulation involves power electronics switching or nonlinear devices. A path-based partial refactorization technique is proposed to accelerate the re-computation of LU factors. In the left-looking algorithm, only a subset of columns that belong to the computed factorization path are refactorized. In addition, Block Triangular Factorization (BTF) is enhanced through partial refactorization, which further accelerates computation through smaller, evolving submatrices. The ne

## 核心贡献


- 提出基于路径的局部重分解技术，精准定位左视LU算法中需更新的列子集
- 将局部重分解与分块三角分解结合，利用动态子矩阵加速网络方程求解
- 首次构建非对称LU因子通用路径重分解框架，并集成至MKLU求解器


## 使用的方法


- [[稀疏直接求解器-klu-mklu|稀疏直接求解器(KLU/MKLU)]]
- [[左视lu分解|左视LU分解]]
- [[基于路径的局部重分解|基于路径的局部重分解]]
- [[分块三角分解-btf|分块三角分解(BTF)]]
- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[近似最小度排序-amd|近似最小度排序(AMD)]]
- [[主元有效性检验|主元有效性检验]]


## 涉及的模型


- [[伴随电路模型|伴随电路模型]]
- [[非线性元件线性化诺顿等效模型|非线性元件线性化诺顿等效模型]]
- [[电力电子开关模型|电力电子开关模型]]


## 相关主题


- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[网络方程求解|网络方程求解]]
- [[电力电子开关暂态|电力电子开关暂态]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 路径法相比传统全量及列索引重分解，大幅削减了矩阵重分解的计算耗时
- 结合BTF的改进算法在大规模实际电网算例中，实现了显著的整体仿真加速
- 该技术可高效处理电力电子频繁开关引发的矩阵突变，且保持数值稳定性


