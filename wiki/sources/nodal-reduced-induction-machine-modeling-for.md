---
title: "Nodal Reduced Induction Machine Modeling for"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nodal reduced induction machine modeling for EMTP-type simulations.pdf"]
---

# Nodal Reduced Induction Machine Modeling for

**作者**: 
**年份**: 2012
**来源**: `27&28/Nodal reduced induction machine modeling for EMTP-type simulations.pdf`

## 摘要

—This paper presents two new induction machine models with a direct interface to an external power system, for EMTP-type simulations. The models’ improved efﬁciency and their overall superiority over existing formulations are shown by numerical simulations involving different machines. It is shown that models that use currents as output variables possess a high degree of numerical accuracy at relatively large time steps making them competitive with a state-of-the-art model that uses the stator currents and rotor ﬂuxes as output variables. The use of a single set of variables is shown to simplify considerably the models’ representations, resulting in highly efﬁcient formulations. Index Terms—EMTP, induction machine, nodal reduction, phase-domain (PD) model, transient simulation, voltage-beh

## 核心贡献


- 提出NR-CF与NR-CC两种新型感应电机模型，实现与外部电网直接接口
- 基于节点缩减法简化相域模型拓扑，显著降低方程数量并提升计算效率
- 证明以电流为输出变量的模型在大步长下具备高精度，性能优于传统VBR模型


## 使用的方法


- [[节点缩减法|节点缩减法]]
- [[相域建模|相域建模]]
- [[电抗后电压模型|电抗后电压模型]]
- [[梯形积分法|梯形积分法]]
- [[状态空间法|状态空间法]]
- [[参考系变换|参考系变换]]


## 涉及的模型


- [[感应电机|感应电机]]
- [[相域模型|相域模型]]
- [[电抗后电压模型|电抗后电压模型]]
- [[节点缩减模型|节点缩减模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电机建模|电机建模]]
- [[数值稳定性|数值稳定性]]
- [[大步长仿真|大步长仿真]]
- [[机网接口|机网接口]]


## 主要发现


- 新型节点缩减模型在计算效率与数值稳定性上全面优于传统相域与VBR模型
- 以电流为输出变量的模型在大步长下仍保持高精度，有效避免积分步长限制
- 单一变量集大幅简化模型拓扑，显著降低节点与支路数量，提升求解速度


