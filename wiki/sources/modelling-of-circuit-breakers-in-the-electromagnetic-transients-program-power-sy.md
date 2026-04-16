---
title: "Modelling of circuit breakers in the Electromagnetic Transients Program - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modelling of circuit breakers in the electromagnetic transients program.pdf"]
---

# Modelling of circuit breakers in the Electromagnetic Transients Program - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Modelling of circuit breakers in the electromagnetic transients program.pdf`

## 摘要

The recent publication of experimental and theoretical results from verified arc models has made pos- sible the implementation and testing of a dynamic circuit breaker model in the Electromagnetic Transients Program (EMTP). An estimator was developed to obtain model parameters from test data. Results from this are given, and it’s data requirements specified. To illustrate an ap- plication of the model not previously possible with the ex- isting capabilities of EMTP, simulations of load current interruption in a multi-terminal HVDC system were per- formed. Results from these are included, along with a discussion of the effects of system and model parameter variation on the interruption process. INTRODUCTION The Electromagnetic Transients Program (EMTP) is an extensively used tool for the an

## 核心贡献


- 在EMTP中集成Avdonin等三种动态电弧微分方程模型
- 开发基于实测数据的断路器模型参数估计器并明确数据需求
- 提出基于补偿法与预测校正迭代的非线性断路器网络接口算法


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[补偿法|补偿法]]
- [[预测校正迭代法|预测校正迭代法]]
- [[参数估计|参数估计]]


## 涉及的模型


- [[断路器|断路器]]
- [[动态电弧模型|动态电弧模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[变压器|变压器]]
- [[同步电机|同步电机]]


## 相关主题


- [[断路器建模|断路器建模]]
- [[电弧动态特性|电弧动态特性]]
- [[电流开断仿真|电流开断仿真]]
- [[暂态恢复电压|暂态恢复电压]]
- [[热与介质击穿|热与介质击穿]]


## 主要发现


- 预测校正迭代法通常仅需3至4次迭代即可收敛，数值稳定性良好
- 动态电弧模型成功应用于多端HVDC系统负荷电流开断仿真验证
- 模型参数变化显著影响开断过程，可准确复现截流与介质击穿现象


