---
title: "Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet"
type: source
authors: ['Jurij']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Wang - 2010 - Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet.pdf"]
---

# Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet

**作者**: Jurij
**年份**: 2010
**来源**: `26/Wang - 2010 - Modeling of ac machines using a voltage-behind-reactance formulation for simulation of electromagnet.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献


- 提出同步与感应电机VBR离散模型实现机网直接接口并优化特征值尺度
- 引入分段线性磁饱和与恒定电导矩阵近似避免网络矩阵重复分解提升效率
- 优化矩阵对称性实现单步仅需百次浮点运算大幅降低CPU耗时


## 使用的方法


- [[电压源后电抗-vbr-建模|电压源后电抗(VBR)建模]]
- [[隐式梯形积分法|隐式梯形积分法]]
- [[特征值尺度分析|特征值尺度分析]]
- [[分段线性磁饱和处理|分段线性磁饱和处理]]
- [[恒定电导矩阵近似|恒定电导矩阵近似]]
- [[机网直接接口|机网直接接口]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[感应电机|感应电机]]
- [[交流电机|交流电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[机网接口技术|机网接口技术]]
- [[大步长数值仿真|大步长数值仿真]]
- [[磁饱和建模|磁饱和建模]]
- [[状态变量仿真|状态变量仿真]]
- [[数值稳定性|数值稳定性]]


## 主要发现


- VBR模型单步仅需百次浮点运算CPU耗时降至微秒级效率显著优于传统模型
- 引入磁饱和与恒定电导矩阵后模型在毫秒级大步长下仍保持高精度与稳定性
- 近似VBR模型避免导纳矩阵重复分解状态变量仿真效率较传统模型提升740%


