---
title: "A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu"
type: source
year: 2023
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/Mu 等 - 2014 - A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu.pdf"]
---

# A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu

**年份**: 2023
**来源**: `03/Mu 等 - 2014 - A parallel multi-rate electromagnetic transient simulation algorithm based on network division throu.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献


- 提出基于传输线自然延迟的网络分解方法，实现全隐式多速率仿真并行计算
- 推导基于范数原理的保守型多速率仿真稳定判据，为网络划分提供理论依据
- 建立全隐式内插值多速率积分模型，解耦快慢子系统状态变量递推求解过程


## 使用的方法


- [[全隐式积分|全隐式积分]]
- [[内插值法|内插值法]]
- [[传输线等效模型|传输线等效模型]]
- [[多速率仿真|多速率仿真]]
- [[并行计算|并行计算]]
- [[状态空间分析|状态空间分析]]


## 涉及的模型


- [[传输线模型|传输线模型]]
- [[戴维南等值电路|戴维南等值电路]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[多速率仿真|多速率仿真]]
- [[并行计算|并行计算]]
- [[网络分解|网络分解]]
- [[稳定性分析|稳定性分析]]


## 主要发现


- 传输线自然延迟特性实现快慢子系统解耦，单大步长内并行计算显著提升效率
- 不合理网络划分易致全隐式多速率仿真发散，应用所提判据调整后可确保收敛
- 算法在维持全隐式积分精度的同时，有效克服传统外插法带来的精度与稳定性损失


