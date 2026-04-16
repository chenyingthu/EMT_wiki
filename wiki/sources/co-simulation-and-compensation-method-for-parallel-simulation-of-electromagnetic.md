---
title: "Co-simulation and compensation method for parallel simulation of electromagnetic transients"
type: source
authors: ['Boris Bruned']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112312. doi:10.1016/j.epsr.2025.112312"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Bruned 等 - 2026 - Co-simulation and compensation method for parallel simulation of electromagnetic transients.pdf"]
---

# Co-simulation and compensation method for parallel simulation of electromagnetic transients

**作者**: Boris Bruned
**年份**: 2025
**来源**: `10/Bruned 等 - 2026 - Co-simulation and compensation method for parallel simulation of electromagnetic transients.pdf`

## 摘要

Co-simulation and compensation method for parallel simulation of , Mehdi Ouafi a, Jean Mahseredjian b, S´ebastien Denneti`ere a This paper introduces a co-simulation tool designed to parallelize the computation of electromagnetic transients (EMTs) using the Compensation Method (CM). The CM is a delay-free parallel technique that allows decoupling network equations anywhere while maintaining accuracy. It overcomes limitations in the delay-based (trans­

## 核心贡献


- 将补偿法推广至MANA公式，支持非线性网络迭代求解与任意位置无延迟解耦。
- 基于FMI构建主从协同仿真接口，实现补偿电流与戴维南等效的跨步长交互。
- 提出自适应步长与阶数策略处理不连续性，并实现潮流结果自动初始化。


## 使用的方法


- [[补偿法-cm|补偿法(CM)]]
- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[功能模型接口-fmi|功能模型接口(FMI)]]
- [[梯形积分法|梯形积分法]]
- [[牛顿迭代法|牛顿迭代法]]
- [[单边框块对角分解-sbbd|单边框块对角分解(SBBD)]]
- [[自适应步长与阶数控制|自适应步长与阶数控制]]


## 涉及的模型


- [[逆变器接口资源-ibr|逆变器接口资源(IBR)]]
- [[输电线路模型|输电线路模型]]
- [[非线性设备模型|非线性设备模型]]
- [[戴维南等效电路|戴维南等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[协同仿真|协同仿真]]
- [[并行计算|并行计算]]
- [[无延迟网络解耦|无延迟网络解耦]]
- [[逆变器并网系统|逆变器并网系统]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 在含高比例IBR的实际电网中，该方法实现最高六倍加速比且保持精度。
- 补偿法可任意位置解耦网络，避免传统传输线延迟法引入的人工误差。
- 自适应步长策略有效处理开关动作不连续性，潮流初始化显著提升收敛速度。


