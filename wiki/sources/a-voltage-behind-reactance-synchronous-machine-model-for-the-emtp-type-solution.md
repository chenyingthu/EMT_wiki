---
title: "A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type Solution"
type: source
year: 2006
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/TPWRS.2006.883670.pdf.pdf"]
---

# A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type Solution

**年份**: 2006
**来源**: `04/TPWRS.2006.883670.pdf.pdf`

## 摘要

—A full-order, voltage-behind-reactance synchronous machine model has recently been proposed in the literature. This paper extends the voltage-behind-reactance formulation for the electromagnetic transient program (EMTP)-type solution, in which the rotor subsystem is expressed in coordinates and the stator subsystem is expressed in phase coordinates. The model interface with the nodal-analysis network solution is non-iterative and simultaneous. An example of a single-machine, inﬁnite-bus system shows that the proposed model is more accurate and efﬁcient than several existing EMTP machine models. Index Terms—Computational techniques, electromagnetic tran- sient program (EMTP), phase-domain (PD) model, synchronous machine, voltage-behind-reactance (VBR) model. I. INTRODUCTION

## 核心贡献


- 提出适用于EMTP节点分析的全阶电抗后电压同步电机模型
- 定子采用相坐标转子采用dq坐标实现非迭代同步网络接口
- 定转子方程解耦降低计算负担改善特征值缩放提升数值精度


## 使用的方法


- [[节点分析法|节点分析法]]
- [[电抗后电压法|电抗后电压法]]
- [[相域建模|相域建模]]
- [[dq坐标变换|dq坐标变换]]
- [[补偿法|补偿法]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[全阶模型|全阶模型]]
- [[相域模型|相域模型]]
- [[电抗后电压模型|电抗后电压模型]]
- [[单机无穷大系统|单机无穷大系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[电机网络接口|电机网络接口]]
- [[数值稳定性|数值稳定性]]
- [[仿真效率优化|仿真效率优化]]


## 主要发现


- 单机无穷大系统仿真验证该模型精度与计算效率优于传统模型
- 消除预测校正迭代与单步延迟避免大时间步长下的数值不稳定
- 恒定电感矩阵与解耦结构降低计算负担特征值缩放改善精度


