---
title: "Acceleration of electromagnetic transient simulations in modelica using spatial data locality"
type: source
authors: ['A. Masoom']
year: 2022
journal: "Electric Power Systems Research, 211 (2022) 108577. doi:10.1016/j.epsr.2022.108577"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Masoom 等 - 2022 - Acceleration of electromagnetic transient simulations in modelica using spatial data locality.pdf"]
---

# Acceleration of electromagnetic transient simulations in modelica using spatial data locality

**作者**: A. Masoom
**年份**: 2022
**来源**: `05/Masoom 等 - 2022 - Acceleration of electromagnetic transient simulations in modelica using spatial data locality.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Acceleration of electromagnetic transient simulations in modelica using A. Masoom a,*, T. Ould-Bachir b, J. Mahseredjian a, A. Guironnet c a Department of Electrical Engineering, Polytechnique Montr´eal, Montr´eal, Canada b Department of Computer Engineering, Polytechnique Montr´eal, Montr´eal, Canada

## 核心贡献


- 提出将多条输电线路聚类为单一线路块模型，优化空间数据局部性以提升缓存命中率
- 将线路延迟函数计算迁移至外部向量化C代码，有效降低Modelica原生算子开销
- 重构线路变量与参数为一维数组结构，实现大规模电网电磁暂态仿真加速


## 使用的方法


- [[空间数据局部性优化|空间数据局部性优化]]
- [[向量化c代码调用|向量化C代码调用]]
- [[宽频线路模型|宽频线路模型]]
- [[恒定参数线路模型|恒定参数线路模型]]
- [[模态变换|模态变换]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[宽频线路模型|宽频线路模型]]
- [[恒定参数线路模型|恒定参数线路模型]]
- [[ieee-39节点测试系统|IEEE 39节点测试系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真加速|仿真加速]]
- [[空间数据局部性|空间数据局部性]]
- [[非因果建模|非因果建模]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 线路块模型结合向量化C代码使IEEE 39节点系统仿真时间显著缩短
- 优化后的算法在保持数值稳定性的同时，大幅提升了Modelica仿真效率
- 空间数据局部性优化有效缓解了大规模网络仿真中的内存访问瓶颈


