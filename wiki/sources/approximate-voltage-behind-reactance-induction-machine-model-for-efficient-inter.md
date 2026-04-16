---
title: "Approximate Voltage-Behind-Reactance Induction Machine Model for Efficient Interface With EMTP Network Solution"
type: source
authors: ['Liwei Wang', 'Juri Jatskevich']
year: 2010
journal: "IEEE Transactions on Power Systems;2010;25;2;10.1109/TPWRS.2009.2034526"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/09/Wang和Jatskevich - 2010 - Approximate voltage-behind-reactance induction machine model for efficient interface with EMTP netwo.pdf"]
---

# Approximate Voltage-Behind-Reactance Induction Machine Model for Efficient Interface With EMTP Network Solution

**作者**: Liwei Wang, Juri Jatskevich
**年份**: 2010
**来源**: `09/Wang和Jatskevich - 2010 - Approximate voltage-behind-reactance induction machine model for efficient interface with EMTP netwo.pdf`

## 摘要

—A so-called voltage-behind-reactance (VBR) in- duction machine model has recently been proposed for the Electro-Magnetic Transient Program (EMTP) solution as an advantageous alternative to the traditional and phase-domain (PD) models. This paper focuses on achieving an efﬁcient interface of the machine models with the EMTP network. It is shown ﬁrst that a discretized PD model can be formulated to have a constant machine conductance submatrix, which is a very desirable nu- merical property that allows avoiding the re-factorization of the network conductance matrix at every time step. Furthermore, an approximate voltage-behind-reactance (AVBR) model is proposed

## 核心贡献


- 提出近似电压后电抗感应电机模型，忽略转速相关系数实现恒定电导子矩阵
- 证明离散化相域模型可构建恒定电导子矩阵，避免网络矩阵每步重分解
- 实现电机与EMTP网络直接接口，支持机电变量非迭代同步求解


## 使用的方法


- [[隐式梯形积分法|隐式梯形积分法]]
- [[节点分析法|节点分析法]]
- [[电压后电抗法|电压后电抗法]]
- [[相域建模|相域建模]]
- [[恒定电导矩阵技术|恒定电导矩阵技术]]


## 涉及的模型


- [[感应电机|感应电机]]
- [[鼠笼式感应电机|鼠笼式感应电机]]
- [[相域模型|相域模型]]
- [[电压后电抗模型|电压后电抗模型]]
- [[近似电压后电抗模型|近似电压后电抗模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电机网络接口|电机网络接口]]
- [[恒定电导矩阵|恒定电导矩阵]]
- [[非迭代求解|非迭代求解]]
- [[数值效率优化|数值效率优化]]


## 主要发现


- AVBR模型计算效率显著优于传统PD与VBR模型，大幅降低仿真耗时
- 忽略转速相关系数引入的误差极小且边界严格，适用于宽功率范围电机
- 新模型在较大积分步长下仍保持高数值精度，有效避免网络矩阵重复分解


